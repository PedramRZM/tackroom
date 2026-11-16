Implemented all five changes, using only the standard library. No commit created.

- AC1: Delivery boundary tests pass, including 5000 cents.
- AC2: Isolated SQLite tests verify persisted approval and unchanged storage for rejected requests.
- AC3: Tests verify success/failure state, preserved fields, and input immutability.
- AC4: Exact allowed colors pass; malformed and other values fail.
- AC5: Exact heading bytes verified: `b'Invoices\n'`.

Regression tests failed before the fixes. Full `scripts/agent/check` output:

```text
Ran 8 tests in 0.002s

OK
```

Unverified: visual, accessibility, and usability behavior—no rendered UI exists; reducer tests provide state evidence only.