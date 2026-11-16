# Verification plan

Use the existing standard-library unittest runner; no dependencies or check-command changes.

- Delivery: 4999 → 500, 5000/5001 → 0; boundary regression risk → unit examples alongside existing nearby checks, `scripts/agent/check`.
- Approval: approver + pending → True and persisted approved; viewer/unknown + pending, missing ID, and already approved → False and unchanged rows; authorization/storage risk → integration tests with fresh temporary SQLite file per test and a second connection to inspect persisted data, `scripts/agent/check`.
- Save: failure preserves saved/draft and sets error; success saves draft and clears error; both stop saving, preserve unrelated fields, and leave input unchanged → pure reducer tests with distinct values and copied input, `scripts/agent/check`. These establish state only, not rendered behavior.
- Color: each of three exact allowed strings passes unchanged; arbitrary variables, raw colors, malformed expressions, and whitespace fail → table-driven unit checks, `scripts/agent/check`. No CSS parser or rendered contrast claim.
- Heading: exact bytes `Invoices\n` → direct Python byte comparison; no new regression test for this copy-only change.

Run new behavior tests before production edits to establish failures, then the full existing check after fixes. No rendered UI exists: visual, accessibility, and usability checks are unavailable and remain unverified. There is no HEAD revision in this scratch repository; all supplied files are staged additions and implementation changes will remain uncommitted.

# Results

Environment: Python 3.10.13, local scratch tree, no commits/HEAD. Only Python standard library used.

- AC1: boundary examples 4999, 5000, 5001 passed along with existing 100/6000 checks.
- AC2: approver persistence observed through separate SQLite connection; all denial cases returned False with both local and persisted rows unchanged. Each test uses a fresh temporary database, closed and deleted by unittest cleanup.
- AC3: success/failure exact result, unrelated field preservation, distinct result object, and unchanged input passed. State evidence only.
- AC4: all three exact strings passed; arbitrary/raw/malformed/whitespace examples rejected. The boolean validator does not transform input values.
- AC5: direct byte comparison printed `Heading bytes: OK`.
- Red evidence: `before-check.txt` records `Ran 6 tests` and `FAILED (failures=14)` before production edits, with failures on all four reported logic bugs.
- Full check: `after-check.txt` records `Ran 8 tests in 0.025s` and `OK`; no skips or retries. Existing checks and their expectations were preserved.
- `git diff --check` passed.

Unverified: rendered visual, accessibility, and usability behavior (no UI exists); no claims about contrast or general CSS validation. No external application integration is provided in this exercise.
