---
name: write-tests
description: Design verification before implementation, choose checks and quality tools that fit the project, and write tests that can actually fail. Use for a feature or bug that needs tests, test strategy or coverage, and flaky, slow or weakened tests.
---

# Writing tests

A test is worth having when it would catch a real mistake and gives confidence that the thing
works for whoever uses it. Count that, not coverage.

## Before implementation

Inspect the existing checks, test runner, fixtures and relevant conventions. For a substantive
change, put a compact verification plan in the task or existing plan before editing production
code. One sentence is enough for a small fix; a copy-only change may need only existing checks
and a direct inspection, not a new test.

For each criterion, record: **example and expected result → risk → smallest sufficient check
and tool → data/environment → command or UI steps → evidence**. Include failure, boundary or
permission examples where they affect the outcome. Derive expected results from the task,
domain rule or trusted reference, not from the implementation you are about to write. Resolve
ambiguity that would change the behavior; label any setup or command not yet verified.

BDD is discovery of shared behavior through concrete examples, optionally Given/When/Then.
TDD is the red/green/refactor development loop. Unit, integration and E2E describe test scope.
Use them together; neither BDD nor TDD requires putting every example through a browser or
installing a Gherkin runner.

Choose checks for uncovered risks and explain the choice, even when the existing tools suffice.
When choosing tools, enforcing a code/design constraint, or testing a UI, read
[verification-tools.md](references/verification-tools.md). Recommend the smallest useful
addition with its limits and maintenance cost; do not install a catalog of tools by default.

## Which level

Use the lowest level that gives real confidence in the behaviour. From cheapest to most
expensive:

1. **Static**: types and lint. They catch typos and wrong shapes for free. If a mistake could
   be caught here, tighten the type or add the lint rule instead of writing a test.
2. **Unit**: one function or module with real logic (parsing, pricing, state transitions),
   tested through its inputs and outputs.
3. **Integration**: several parts working together through a public surface, with only the
   outside world replaced: a request handler against a real test database, a page or component
   with the network stubbed at the boundary. Favor these when interaction between parts is the
   risk; logic-heavy libraries may need more unit/property tests. No fixed ratio fits every app.
4. **End to end**: the running app driven like a user. Keep these to the few flows that must
   never break (sign in, pay, the core action), because they are slow and can be flaky.

## Writing one

- Start from the behaviour: an acceptance criterion, a bug report, what a caller observes. Do
  not derive the test from the implementation; a test written from the code only confirms that
  the code does what it does.
- Assert on what a user or caller can see. Do not assert on internals, call counts or private
  state unless that is the behaviour.
- For a bug or meaningful new behavior: write a focused test first and confirm it fails for
  the missing behavior, not broken setup. Implement, then refactor while it stays green. If a
  test was added after the code, remove the fix or introduce a targeted fault in an isolated
  copy and confirm it goes red. Preserve the working change; never discard someone else's edits.
- Where code has an invariant, test the property over generated inputs instead of a few
  examples: a round trip (encode then decode), something that must always hold, doing it twice
  equals doing it once, two implementations agreeing. For a rewrite or migration, run old and
  new on the same inputs and compare.
- Keep the inner loop deterministic: seed randomness, control time, replace uncontrolled
  external services at their boundary. Integration/E2E checks may use real isolated services
  when that boundary is what must be proved; name that environment and its reset procedure.

## Do not

- Mock the thing under test, or assert on a value the test itself just computed.
- Add a retry, a sleep or a looser assertion to get a pass. A flaky test is a bug: fix the
  cause, or quarantine it and file a task saying so.
- Weaken, skip or delete an existing test to make a change pass. If a test is wrong, stop and
  say which one and why. When an expectation legitimately changes with the code, say why in the
  pull request.
- Chase a coverage number. It produces trivial tests.

## Gotchas

- Tests written in the same session as the code share its assumptions. An existing test, the
  task's own check, or the running app is stronger evidence than a new test alone.
- Tests cannot judge security or design, and they pass while the wrong thing ships. They are
  one signal; `verify` asks for the others.
- Snapshot tests of large output get approved without being read. Prefer a few explicit assertions.

## This project

Add what is specific here as it is learned: how to get a test database, the factories or
fixtures to use, which flows have end-to-end coverage, the command for one test file.
