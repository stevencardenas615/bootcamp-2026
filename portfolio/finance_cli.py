import typer
from datetime import datetime
import sqlite3
from enum import Enum
from contextlib import closing

app = typer.Typer()

class AllowedCategory(str, Enum):
    RENT = "rent"
    FOOD_DINING = "food_dining"
    SUBSCRIPTIONS = "subscriptions"
    TRANSPORTATION = "transportation"
    UTILITIES = "utilities"
    HEALTHCARE = "healthcare"
    MISC = "misc"

def db_connect(database_file):
    conn = sqlite3.connect(database_file)
    conn.execute("CREATE TABLE IF NOT EXISTS history (amount REAL, category TEXT, date TEXT, note TEXT)")
    return conn, conn.cursor()

def db_disconnect(connector):
    connector.commit()
    connector.close()

def search_builder(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None):
    
    filters = [
        ("category = ?", choice.value if choice else None, choice is not None),
        ("date >= ?", start.strftime("%Y-%m-%d") if start else None, start is not None),
        ("date <= ?", end.strftime("%Y-%m-%d") if end else None, end is not None)
        ]

    where_prompts = [sql for sql, val, active in filters if active]
    parameters = [val for sql, val, active in filters if active]

    return where_prompts, parameters
   
@app.command()
def add(amount: float, category: AllowedCategory, date: datetime | None = None, note: str = ""):
    conn, cursor = db_connect("transactions.db")

    if date is None:
        date = datetime.now()

    date_str = date.strftime("%Y-%m-%d")

    cursor.execute("INSERT INTO history (amount, category, date, note) VALUES (?, ?, ?, ?)", (amount, category, date_str, note))
    db_disconnect(conn)

@app.command()
def pull(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None):
    conn, cursor = db_connect("transactions.db")

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
def summary(choice: AllowedCategory | None = None, start: datetime | None = None, end: datetime | None = None):
    conn, cursor = db_connect("transactions.db")

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
        
if __name__ == "__main__":
    app()