Implemented all five changes using Python 3.10 standard library only. Added regression tests, including real isolated SQLite fixtures; no dependencies or commits added.

Verification:
- Confirmed tests failed before the fixes.
- `scripts/agent/check`: `Ran 7 tests` — `OK`.
- Heading bytes verified as exactly `Invoices\n`.
- `git diff --check` passed.

Visual, accessibility and usability remain unverified because no rendered UI exists. Reducer tests establish state behavior only. Details are in `verification.md`.