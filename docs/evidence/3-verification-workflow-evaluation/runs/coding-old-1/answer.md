Implemented all five changes using standard library only. No commit created.

- AC1: Delivery boundary tests pass, including 5000 cents.
- AC2: Isolated SQLite tests verify persisted approval and unchanged storage for rejections.
- AC3: Reducer tests verify success, failure, preserved fields and input immutability.
- AC4: Exact color allowlist and malformed-value tests pass.
- AC5: Heading verified as exactly `b'Invoices\n'`.

Regression tests failed before fixes. Full `scripts/agent/check` result:

```text
Ran 8 tests in 0.034s

OK
```

`git diff --check` passed.

Unverified: visual, accessibility and usability behavior—no rendered UI exists; reducer evidence covers state only.