import typer
from datetime import datetime

app = typer.Typer()
now = 0
        
@app.command()
def add(amount: float, category: str, date: datetime = now, note: str = ""):
    now = datetime.now()

    print(f"Amount: ${amount:.2f}\nCategory: {category}\nDate: {date.date()}")
    if note:
        print(f"Note: {note}")

if __name__ == "__main__":
    app()