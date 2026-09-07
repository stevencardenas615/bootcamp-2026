import typer
from datetime import datetime
import sqlite3
from enum import Enum
import csv
from pathlib import Path

app = typer.Typer()

user_database = "transactions.db"

class AllowedCategory(str, Enum):
    RENT = "rent"
    FOOD_DINING = "food_dining"
    SUBSCRIPTIONS = "subscriptions"
    TRANSPORTATION = "transportation"
    UTILITIES = "utilities"
    HEALTHCARE = "healthcare"
    MISC = "misc"

def db_connect(database_file: str | Path,) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(database_file)
    conn.execute("CREATE TABLE IF NOT EXISTS history (amount REAL, category TEXT, date TEXT, note TEXT)")
    return conn, conn.cursor()

def db_disconnect(connector: sqlite3.Connection) -> None:
    connector.commit()
    connector.close()

def search_builder(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None) -> tuple[list[str], list[str]]:
    
    filters = [
        ("category = ?", choice.value if choice else None, choice is not None),
        ("date >= ?", start.strftime("%Y-%m-%d") if start else None, start is not None),
        ("date <= ?", end.strftime("%Y-%m-%d") if end else None, end is not None)
        ]

    where_prompts = [sql for sql, val, active in filters if active]
    parameters = [val for sql, val, active in filters if active]

    return where_prompts, parameters
   
@app.command()
def add(amount: float, category: AllowedCategory, date: datetime | None = None, note: str = "") -> None:
    conn, cursor = db_connect(user_database)

    if date is None:
        date = datetime.now()

    date_str = date.strftime("%Y-%m-%d")

    cursor.execute("INSERT INTO history (amount, category, date, note) VALUES (?, ?, ?, ?)", (amount, category, date_str, note))
    db_disconnect(conn)

@app.command()
def pull(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None) -> None:
    conn, cursor = db_connect(user_database)

    where_prompts, parameters = search_builder(choice, start, end)

    query = "SELECT * FROM history"
    if where_prompts:
        query += " WHERE " + " AND ".join(where_prompts)
    query += " ORDER BY date DESC"

    history = cursor.execute(query, parameters).fetchall()
                    
    if not history:
        print("No Transaction")
    else:
        for row in history:
            print(f"{row[2]} | {row[1].upper()} | ${row[0]:.2f}", end="")
            if row[3]:
                print(f" | Note: {row[3]}")
            else:
                print("")

    db_disconnect(conn)

@app.command()
def summary(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None) -> None:
    conn, cursor = db_connect(user_database)

    where_prompts, parameters = search_builder(choice, start, end)

    query = "SELECT category, SUM(amount) FROM history"

    if where_prompts:
        query += " WHERE " + " AND ".join(where_prompts)

    query += " GROUP BY category ORDER BY SUM(amount) DESC"

    report = cursor.execute(query, parameters).fetchall()

    if not report:
        print("No Transactions")
    else:
        output = [f"{row[0].upper()}: ${row[1]:.2f}" for row in report]
        total = [row[1] for row in report]
        for line in output:
            print(line)
        print(f"TOTAL: ${sum(total):.2f}")

    db_disconnect(conn)

@app.command()
def export_history(filename: str, choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None) -> None:

    conn, cursor = db_connect(user_database)

    where_prompts, parameters = search_builder(choice, start, end)

    query = "SELECT * FROM history"
    if where_prompts:
        query += " WHERE " + " AND ".join(where_prompts)
    query += " ORDER BY date DESC"

    history = cursor.execute(query, parameters).fetchall()

        
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = ["amount", "category", "date", "note"])
        writer.writeheader()
        for row in history:
            writer.writerow({"amount": row[0], "category": row[1], "date": row[2], "note": row[3]})

    db_disconnect(conn)

@app.command()
def import_history(filename: Path) -> None:
    if not  filename.exists():
        print(f"Error: File '{filename}' does not exist.")
        raise typer.Exit(code=1)

    conn, cursor = db_connect(user_database)

    success_count = 0
    failed_rows = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            current_line = reader.line_num
            try:
                raw_amount = row["amount"]
                raw_category = row["category"]
                raw_date = row["date"]
                note = row.get("note", "").strip()

                amount = float(raw_amount)
                valid_date = datetime.strptime(raw_date, "%Y-%m-%d")
                date_str = valid_date.strftime("%Y-%m-%d")

                if raw_category not in [item.value for item in AllowedCategory]:
                    raise ValueError("Incorrect Category")

                cursor.execute("INSERT INTO history (amount, category, date, note) VALUES (?, ?, ?, ?)", (amount, raw_category, date_str, note))
                success_count += 1
            except (KeyError, ValueError, TypeError) as error:
                failed_rows.append(f"Line {current_line}: Error {error} | Data: {dict(row)}")
                continue

    db_disconnect(conn)
    print(f"Successfully Imported: {success_count} rows")
    print(f"Skipped (BAD INPUT): {len(failed_rows)} rows")
    if failed_rows:
        print("Failed Rows:")
        for failure in failed_rows:
            print(failure)

if __name__ == "__main__":
    app()