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
   
@app.command()
def add(amount: float, category: AllowedCategory, date: datetime = None, note: str = ""):
    conn, cursor = db_connect("transactions.db")

    if date is None:
        date = datetime.now()

    date_str = date.strftime("%Y-%m-%d")

    cursor.execute("INSERT INTO history (amount, category, date, note) VALUES (?, ?, ?, ?)", (amount, category, date_str, note))
    db_disconnect(conn)

@app.command()
def pull():
    conn, cursor = db_connect("transactions.db")
    history = cursor.execute("SELECT * FROM history ORDER BY date DESC").fetchall()

    if not history:
        print("No Transaction")
    else:
        for row in history:
            print(f"{row[2]} | {row[1].upper()} | ${row[0]:.2f}", end="")
            if row[3]:
                print(f" | Note: {row[3]}")
            else:
                print("")

        
if __name__ == "__main__":
    app()