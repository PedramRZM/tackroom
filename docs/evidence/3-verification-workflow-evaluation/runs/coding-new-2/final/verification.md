Verification plan (before implementation)

Use Python standard-library unittest through `scripts/agent/check`; no dependencies or gate changes.
- Fee: 4999 -> 500, 5000/5001 -> 0; boundary regression risk -> unit test, alongside existing lower/higher examples.
- Approval: pending invoice + approver -> True and persisted approved; viewer/unknown role, missing ID and approved invoice -> False and unchanged rows. Risk is authorization and persistence -> integration tests using a fresh temporary SQLite file and connection per test, reopened to inspect persisted rows; fixtures removed by cleanup.
- Save: failure preserves saved/draft, stops saving and reports Save failed; success saves draft and clears error. Risk is losing edits or mutating input -> unit tests with explicit expected states, unrelated fields and input snapshots.
- Color: all three exact tokens pass unchanged; raw colors, arbitrary variables, malformed expressions and whitespace variants fail. Risk is overly permissive validation -> unit examples through valid_color.
- Heading: exact bytes Invoices plus newline -> direct inspection, no new copy-only test.

First run the added behavior tests against original code to establish failures, then implement and run the full check command. No rendered UI exists: reducer checks establish state behavior only; visual, accessibility and usability evidence are unavailable.

Results: final uncommitted scratch tree (repository has no HEAD), Python 3.10.13.
- Before fixes: full command ran 7 tests, FAILED (failures=14); failures exposed fee boundary, approval denial, failed-save state and permissive colors.
- AC1: delivery boundary test passed for 4999, 5000 and 5001; existing low/high fee examples passed.
- AC2: real temporary SQLite file tests passed for successful persisted approval and rejected viewer/unknown/missing/already-approved/non-pending cases. Reopened connections checked persisted rows, and the caller connection checked unchanged rows on denial.
- AC3: success/failure state expectations, unrelated field preservation and non-mutation checks passed.
- AC4: three exact tokens passed; raw colors, arbitrary variables, malformed expressions and whitespace variants were rejected.
- AC5: direct byte assertion printed: Heading exact bytes: PASS (Invoices plus newline)
- Full scripts/agent/check output summary:
  Ran 7 tests in 0.029s
  OK
No skips, retries or quarantines. Only standard-library tools used; check command unchanged.
Not verified: rendered visual appearance, accessibility and usability (no rendered UI exists). Reducer evidence is state evidence only. Heading evidence is exact file content, not a layout claim. No commit created.
