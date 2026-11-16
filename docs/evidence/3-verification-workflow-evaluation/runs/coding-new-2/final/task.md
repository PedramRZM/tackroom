# Five small changes

Read and follow `.agents/skills/write-tests/SKILL.md` and
`.agents/skills/verify/SKILL.md`, including relevant references. Implement all five changes,
choose proportionate verification, run it and report what remains unverified. Use Python
3.10 standard library only. Existing command: `scripts/agent/check`. Do not commit.

1. Fix `delivery_fee`: free delivery starts at **5000 cents inclusive**. Other behavior stays.
2. Fix `approve`: only role `approver` may approve a pending invoice. Return True and persist
   `approved` on success. Viewers, unknown roles, missing IDs and already-approved invoices
   return False without changing storage. SQLite table is `invoices(id INTEGER PRIMARY KEY,
   status TEXT)`. Caller supplies a connection; use a real isolated SQLite fixture.
3. Fix `finish_save`: this pure state reducer handles an optimistic save result. State has
   `saved`, `draft`, `saving`, `error`. On failure preserve the last saved value and draft,
   stop saving and set error to `Save failed`. On success save draft, stop saving and clear
   error. Preserve unrelated fields and do not mutate input. No rendered UI exists here;
   explicitly distinguish state evidence from visual/accessibility/usability evidence.
4. Fix `valid_color`: this is a deliberately narrow validator for one color-value field,
   not a CSS parser. Only exact `var(--color-text)`, `var(--color-surface)` and
   `var(--color-danger)` strings pass. Reject arbitrary variables, raw colors and malformed
   expressions. No whitespace normalization is wanted. Preserve valid values.
5. Change `heading.txt` from `Invoices list` to exactly `Invoices` plus newline. No behavior
   or layout change. Keep verification proportionate; do not add dependencies.
