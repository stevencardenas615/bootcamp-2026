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

## 2026-09-10 — Sprint Wk 5 · Internship Results
- Got an email offer back from the internship in my area, really excited and will be taking it.

## 2026-09-11 — Sprint Wk 5 · Cloud Computing Assignments + AWS Academy Ch1 + 2
- Worked on my assignments and on another learning quest (AWS) that's going to be alongside my bootcamp for now to further push myself

## 2026-09-13 — Sprint Wk 5 · Postgres + DSA · Week 5 close

- SQL refresher: JOINs, keys/constraints, indexes, normalization (pgexercises)
- SSH keys set up for the VPS — ed25519, key-only login working, `ssh vps` alias
- Postgres 16 installed on the VPS, `steven` role + `inventory` database created, localhost-only, connected from laptop through an SSH tunnel with psycopg
- DSA 5/5: Two Sum, Valid Anagram, Contains Duplicate, First Unique Char, Best Time to Buy/Sell Stock, I'm pushing to wk 6: Inventory API schema by hand

**Week 5 done:** Git deep-dive, PR cycle, finance-cli split to its own repo,
SQL, SSH keys, Postgres on VPS, DSA thread started. Article 1 published,
6 Builder Center badges.

## 2026-09-15 — Sprint Wk 6 · Schema + FastAPI
- Designed the Inventory API schema by hand — users, manifests, products; NUMERIC for money, CHECK on status, three indexes. Committed as schema.md on repo
- FastAPI tutorial: First Steps through Request Body / Pydantic. uv set up, fastapi-practice test running to understand

## 2026-09-16 — Sprint Wk 6 · Cloud+ Ch. 4
- Cloud+ Ch. 4 (Networking) with labs and sims. Class assignments that came up, mostly small Python Projects

## 2026-09-17 — Sprint Wk 6 · Cloud+ Ch. 5 + AWS Academy 3–4
- Cloud+ Ch. 5 (Connectivity), all labs, sims and videos.
- AWS Academy modules 3–4, IAM lab
- Buisness Data Analytics 2 hour class video, assignments and quiz completed
- DSA 1/5: Majority Element — Counter + walk the counts

## 2026-09-18 — Sprint Wk 6 · DSA 268 + 349
- Completed DSA problems 268 and 349
- Worked on C# Assignments and Class

## 2026-09-19 — Sprint Wk 6 · DSA 125 + 283
- Completed DSA problems 125 and 283
- Filled out the remaining work forms for internship on Tuesday 9/22

## 2026-09-20 — Sprint Wk 6 · Week 6 close
- Day of Rest, Sister's 13th birthday

## 2026-09-21 — Sprint Wk 7 · Throwaway API
- Built the throwaway employees API: EmployeeCreate/Employee models, dict storage, POST/GET/GET-one/PUT/DELETE with 404s — all five working in /docs

## 2026-09-22 — Sprint Wk 7 · Noteology Day 1
- First day at Noteology (AI + Digital Optimization intern). Normalized and replaced:
 - product photos on 42 of 46 candle products on the live Shopify store, verified all 42 on the storefront. Dry run → one product batch on every step.
- Caught an AI quality review that passed bad output — full-res check found repeated flames, glowing labels, a garbled clock. Reworked prompts, approved 12 images.
- Resume updated: finance CLI, pytest/FastAPI/Postgres skills, Noteology role, AWS cert in progress
- DSA 1/5: Reverse String (#344) — two pointers, in-place swap

## 2026-09-23 — Sprint Wk 7 · Inventory API kickoff
- Created the inventory-api repo, uv project setup, app/ + tests/ structure
- Wrote all 10 Pydantic models — products, manifests, users — three shapes each (Create / response / Update)
- Design decisions: raw SQL over SQLAlchemy (noted in LATER.md), soft delete via status, default status NOT_AVAILABLE so nothing sells by accident, selling gets its own endpoint, PATCH over PUT for partial edits
- Caught two security bugs in my own models: the response model was returning password_hash, then after the first fix it inherited the plaintext password. Split into UserBase / UserCreate / User / UserInDB. Separating essentially a one way traffic to enter user passwords and preventing it from being returned.
- DSA 2/5: Squares of a Sorted Array (#977) — two pointers from both ends, filling the output back to front

## 2026-09-24 — Sprint Wk 7 · Noteology Day 2
- 27/27 main product images and 28/28 lifestyle scenes live and verified on draft products; fixed 6 defective live images
- Put the project under git, moved Shopify credentials to .env, added AI deny rules
- Wrote highlighted_rows.py by hand
- DSA: 

## 2026-09-25 — Sprint Wk 7 · Noteology Day 3
- Brand-learning assignment: Noteology + Olfactif customer walkthroughs, search and AI-visibility research
- DSA: 26 Remove Duplicates from sorted array

## 2026-09-26 — Sprint Wk 7 · Coursework
- Class assignments, family time
- DSA: 643 Max Average Subarray and 3 Longest Substring

## 2026-09-27 — Sprint Wk 7 · Applications + DB connection · Week 7 close
- First 5 applications out: Guardian, Amazon, Qumulo, GM (long shots), GE HealthCare (first eligible one). Tailored cover letters for each. Started an application tracker.
- Learned to read eligibility first: most big-company internships require bachelor's enrollment and a grad window I don't fit yet — the ESU transfer is what unlocks them.
- Updated resume internship section and LinkedIn Profile
- inventory-api: .env + .env.example, app/db.py with a FastAPI connection dependency (dict_row). App connected to Postgres on the VPS through the SSH tunnel.

**Week 7 close:** models + DB connection done, 5 applications, DSA 5/5.
Rolling to wk 8: schema.sql, first endpoints.

## 2026-09-28 — Sprint Wk 8 · Rest day
- Took the day off.

## 2026-09-29 — Sprint Wk 8 · Schema live + transfer plan
- inventory-api: wrote schema.sql — users, manifests, products with identity
  keys, foreign keys, CHECK on status, NUMERIC money — plus three indexes.
  Ran it on the VPS with psql; all 3 tables and indexes live. Aligned model
  date types with the SQL.
- Transfer: built the ESU plan (rolling admission, fall 2027 decisions from
  Jan 1), emailed transfer admissions and the Clear Path Scholarship office,
  set up reminders in Hermes
- Applications: re-checked eligibility and withdrew one application
- Took a seasonal part-time job starting Oct 4 (Sun/Mon/Tue nights) — calendar
  will stretch; replan Saturday
- DSA 1/5: Two Sum II (#167) — two pointers on sorted input, no hash map needed

## 2026-09-30 — Sprint Wk 8 · Manifest endpoints
- Inventory API: /health with DB connect timeout, seeded first user,
  POST/GET/GET-by-id for /manifests (raw SQL, %s placeholders, RETURNING *, 404s)
- Lined up recommendation letter writers for transfer scholarship

## 2026-10-01 — Sprint Wk 8 · Product endpoints, PATCH, sell
- Products: POST/GET/GET-by-id; caught ForeignKeyViolation → 400 instead of 500
- PATCH /products/{id}: dynamic UPDATE with psycopg.sql (only fields sent)
- POST /products/{id}/sell: atomic UPDATE ... WHERE status='available', 404 vs 409
- Fixed VS Code interpreter/workspace; learned editor warnings ≠ runtime errors
- DSA 2/5: Contains Duplicate II (#219), hash map of number → last index

## 2026-10-04 — Sprint Wk 8 · Soft delete, filtering, registration
- DELETE /products/{id} as soft delete (sold items protected → 409)
- Lists hide deleted; ?status= filter (Enum query param → free 422)
- GET /manifests/{id}/products with 404 vs empty [] distinction
- Auth started: Argon2 hashing via pwdlib (security.py), POST /auth/register with UniqueViolation → 409; hash never selected back out
- Auth: POST /auth/token login (OAuth2 form, verify Argon2 hash, 401 with no user enumeration) → signed JWT (HS256, 30-min exp, secret in .env)
- get_current_user dependency + GET /auth/me; tested with /docs Authorize
- DSA 3/5: Merge Sorted Array (#88), three pointers, fill from the back. Week 8 closed at 3/5.
- Replanned the week around Amazon nights: Fri evening off, Mon/Tue 30-min days

## 2026-10-07 — Sprint Wk 9 · Transfer thread
- Submitted ESU transfer application (Fall 2027, CS) — a month ahead of target
- Wrote and emailed Clear Path scholarship statement
- Homework

## 2026-10-09 — Sprint Wk 9 · Auth wired in
- DSA 1/5: Valid Palindrome II (#680), two pointers + one skip, try both with `or`
- All inventory routes require a token (decorator dependencies); entered_by comes from the JWT user
- Design call: everything protected except health/register/token — least privilege + audit trail
- Test database (inventory_test) on the VPS; pytest + TestClient with get_db overridden
- 9 auth tests green: register/409/422, login/401s, /me with and without token
- Coverage baseline 69%; product + manifest routes are the gap

## 2026-10-10 — Sat · Family cookout, no bootcamp
## 2026-10-11 — Sun · Prepared for work
## 2026-10-12 — Mon · Fell asleep after work; ESU: Kathi confirmed GPA won't exclude me, letters are the last piece; Amazon manager agreed to write one
## 2026-10-13 — Tue · Amazon
## 2026-10-14 — Wed · Dushok agreed to write a letter; picked up extra shift

## 2026-10-16 — Fri · Product tests, 88% coverage
- test_products.py: 13 tests — default status, FK 400, auth 401, get/404, PATCH rules, sell once-only, delete rules, list hides deleted
- Tests found a real bug: ProductCreate accepted status=sold → split ProductBase; create takes EditableStatus only
- Coverage 69% → 88% (target was 80%); 22 tests total
- Dwayne's recommendation letter is in (1 of 3)

## 2026-10-17 — Sat (early AM) · Cleanup
- PATCH refuses sold products (409) + test; 23 tests green
- Refactor: main.py split into routers/auth, manifests, products + deps.py; main.py is 14 lines
- Router-level auth dependency replaces per-route copies
- Connection[dict] everywhere; timestamp → timestamptz in schema and both DBs
- SSH keepalive added after the tunnel dropped mid-run

## 2026-10-18 — Sun · Inventory API deployed
- Replanned: Wed rest; Thu/Fri/Sat are project blocks; Sun–Tue Amazon 30-min days
- Dockerized the API (uv-based image, .dockerignore keeps .env out), compose.yml with Traefik labels
- Found nginx was wrong for this box: Traefik (host network, Let's Encrypt) already owns 80/443
- Container on host network → Postgres stays localhost; Traefik routes api.scardenas.tech with a real cert
- https://api.scardenas.tech/health → ok. Project checklist complete: VPS-deployed, JWT, 88% coverage
- Bots probed the hostname within a minute of the cert; hardening is next
- Hardened the VPS: non-root sudo user with key, ufw (22/80/443 only), key-only SSH, root login disabled
- GitHub Actions CI: tests run against a Postgres service on every push; green on first run

## 2026-10-19 — Mon · Applications
- Applied: Navy Federal (Mobile Developer, San Diego), CACI (remote); wrote the Navy Federal cover letter
- Reviewed all US Amazon tech internships: all SDE roles require a bachelor's; Data Engineer intern is the one that fits
- 15 applications out total

## 2026-10-20 — Tue · Amazon
- 30-min day (shift)

## 2026-10-21 — Wed · Rest

## 2026-10-22 — Thu · Applications + transfer plan B
- Applied: GDIT (Bossier City), Epic Games (backend), Lumen (remote data); three tailored cover letters. 20 out.
- Clear Path funding at ESU ran out; researched transfer options (Bloomsburg, ESU, WGU, Penn State) and PASSHE Pledge
- Emailed Prof. Saporito, Bloomsburg admissions, ESU transfer center, LCCC financial aid (SAP)

## 2026-10-23 — Fri · Rest

## 2026-10-24 — Sat · API security fix + Job Tracker kickoff
- API: registration closed behind ALLOW_REGISTRATION (default off); 24 tests, CI green, deployed; 403 verified live
- Job Tracker kickoff: Saturday questions, schema (applications + status_events, CHECKs, FK, 5 indexes), jobtracker DB created on VPS