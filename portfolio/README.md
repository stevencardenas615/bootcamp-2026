# Finance CLI

A command-line tool for saving and searching your personal finances.

## What it does

Stores transactions in a local SQLite database with a category, amount, date and optional note. Transactions can be filtered by category or date(s) including ranges. Results or transaction history can be exported into an existing or non-existing csv file. Transaction history could also be imported into the database, streamlining usability. Transaction total amounts can also be calculated using date ranges, results are separated by category and a total line displayed at end.

## Setup

Requires Python 3.10+

```bash
pip install typer
python finance_cli.py --help
```

The database is created automatically on first use.

## Usage

### Add a transaction

```bash
python finance_cli.py add 1.99 food_dining
```

### Pull transactions

```bash
python finance_cli.py pull --choice food_dining
```

```
2026-09-06 | FOOD_DINING | $14.50 | Note: Lunch burrito
2026-09-05 | FOOD_DINING | $5.00
2026-09-04 | FOOD_DINING | $1.99 | Note: water bottle from grocery store
2026-09-04 | FOOD_DINING | $0.99 | Note: chips from grocery store
2026-09-04 | FOOD_DINING | $7.25 | Note: coffee
2026-09-04 | FOOD_DINING | $3.99 | Note: jollyranchers from grocery store
2026-09-03 | FOOD_DINING | $7.99 | Note: Ritas
```

### Transaction summary

```bash
python finance_cli.py summary
```

```
RENT: $4200.00
FOOD_DINING: $281.32
TRANSPORTATION: $264.78
MISC: $117.23
UTILITIES: $85.20
SUBSCRIPTIONS: $48.97
TOTAL: $4997.50
```

### Export history to CSV

```bash
python finance_cli.py export-history transaction_history.csv
```

CSV file created `transaction_history.csv`:

```
amount,category,date,note
14.5,food_dining,2026-09-06,Lunch burrito
250.0,rent,2026-09-05,
5.0,food_dining,2026-09-05,
82.39,transportation,2026-09-04,
250.0,rent,2026-09-04,
1.99,food_dining,2026-09-04,water bottle from grocery store
9.99,subscriptions,2026-09-04,spotify
0.99,food_dining,2026-09-04,chips from grocery store
7.25,food_dining,2026-09-04,coffee
3.99,food_dining,2026-09-04,jollyranchers from grocery store
```

### Import history from CSV

Given `september.csv`:

```
amount,category,date,note
45.20,food_dining,2026-09-01,groceries
1200.00,rent,2026-09-01,September rent
abc,utilities,2026-09-02,bad amount
60.00,foood,2026-09-03,typo in category
35.99,subscriptions,2026-09-04,streaming
```

```bash
python finance_cli.py import-history september.csv
```

```
Successfully Imported: 3 rows
Skipped (BAD INPUT): 2 rows
Failed Rows:
Line 4: Error could not convert string to float: 'abc' | Data: {'amount': 'abc', ...}
Line 5: Error Incorrect Category | Data: {'amount': '60.00', 'category': 'foood', ...}
```

Invalid rows are skipped and reported with their line number and reason;
valid rows are still imported.


## Design Decisions

**SQLite** The reason why I ended up using SQLite is because memory was being deleted on every instance when using the CLI. SQLite allows us to store this in a local database

**Dynamic Query Builder** I used a dynamic query builder to prevent the confusing and constant if statements in the project. Adding another filter would've added another 4 lines of code of an if statement. The dynamic query builder helps significantly in streamlining the creation of future commands because of reusability.

**Enum for categories** By using Enum for categories we can control, filter and check user input to ensure that it matches with what we are allowing. It's an all in one check that starts right from the CLI.

**Import skips bad rows and reports them** For ease of use I decided in skipping the bad rows and printing the results at the end. The results show what row and for what reason data was rejected and not stored. This aids in the search of your csv file to view whats wrong. It also ensures that at least all data is checked and given a chance to be imported.

## Testing

```bash
pytest
```

Covers the query builder testing the inputs such as category, start and end dates
