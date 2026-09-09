# Bootcamp Log

A dated record of a 12-week Python job-readiness sprint.
Phase A: CS50P + a portfolio CLI. Phase B: SQL, FastAPI, Docker, CI, and deployed projects.

---

## 2026-08-12 — Sprint Wk 1 · CS50P Wk 0 (Functions & Variables)

Repo setup, git config, .gitignore. Starting CS50P Week 0.

CS50P Week 0 complete: all 5 problems passing check50.

## 2026-08-13 — Sprint Wk 1 · CS50P Wk 1 (Conditionals)

CS50P Week 1 complete: all 5 conditionals problems passing check50.

## 2026-08-19 — Sprint Wk 2 · CS50P Wk 2 (Loops)

CS50P Week 2 complete: all 5 loops problems passing check50.

## 2026-08-20 — Sprint Wk 2 · CS50P Wk 3 (Exceptions)

CS50P Week 3 complete: all 4 exceptions problems passing check50.

## 2026-08-24 — Sprint Wk 2 · CS50P Wk 4 (Libraries)

CS50P Week 4 complete: all 6 problems passing check50.

## 2026-08-27 — Sprint Wk 3 · CS50P Wk 5 (Unit Tests)

CS50P Week 5 complete: all 4 problems passing check50.

## 2026-08-29 — Sprint Wk 3 · CS50P Wk 6 (File I/O)

CS50P Week 6 complete: all 4 problems passing check50.

## 2026-08-30 — Sprint Wk 3 · CS50P Wk 7 (Regex)

CS50P Week 7 complete: all 5 problems passing check50.

## 2026-09-03 — Sprint Wk 4 · CS50P Wk 8 (OOP)

CS50P Week 8 complete: all 3 problems passing check50.

**CS50P coursework complete.**

## 2026-09-04 — Sprint Wk 4 · Finance CLI, Day 1

Started the Finance CLI, my first portfolio project. Design was planned on paper the previous day — what the project should do and how it should behave.

Worked through SQLite persistence, a category enum, and an early `pull` command that outputs stored transactions.

## 2026-09-05 — Sprint Wk 4 · Finance CLI, Day 2

Fixed five bugs from the first filter attempt, removed `ALL` from the category enum, and refactored four hardcoded query branches into one dynamic query builder — which meant writing my first list comprehensions. Also fixed date filtering being silently ignored when no category was given.

`pull` now handles every filter combination through one code path; adding another filter is a single line.

## 2026-09-06 — Sprint Wk 4 · Finance CLI, Day 3

Added CSV export and import commands with row validation. Import reports a
summary of successful rows, plus line numbers and reasons for every rejected row.

## 2026-09-07 — Phase A Complete

**Tripwire:** 4/4 — functions/CSV, classes, comprehensions, try/except.
Written unaided, no notes or help.

**CS50P:** Weeks 0–9 complete, all problem sets passing check50.

**Finance CLI shipped.** Original design and thinking done on paper.

- `add`, `pull`, `summary`, `import-history`, `export-history` commands
- CSV, SQLite, and a dynamic query builder
- 6 pytest tests, type hints, and a README with design decisions

**Phase B starts:** Sprint week 5 — Git deep-dive, SQL + Postgres on the VPS,
and the DSA thread begins at 5 problems/week.

## 2026-09-08 — Sprint Wk 5 ·
- Practiced Git branching and went for my 3PM AI + Optimization Internship Interview

## 2026-09-09 — Sprint Wk 5 ·
- Mid-day classes finished Git Remote problem sets, playbook merge

## 2026-09-09 — Sprint Wk 5 · Git deep-dive
- Git Deep dive, separated Finance CLI intwo its own repo and then removed the files from the bootcamp repo.