Read `task.md`, the shipped `write-tests` and `verify` skills, their tool-selection reference, and the relevant `ui-craft` verification guidance. No files changed, dependencies installed, or app checks run.

**A — Invoice permissions, approval and themes**

Design these checks before implementation, deriving expectations from the request:

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Viewer directly calls approval API → denied; invoice unchanged | UI restrictions could conceal missing server authorization. API integration test through the real handler and isolated database. | Seed viewer and pending invoice; call the actual approval endpoint; assert the agreed denial status and reread persisted state. Keep response and before/after state evidence. Exact endpoint, status and fixtures are unknown. |
| Approver approves pending invoice → approved and persisted | Transition or persistence could be broken. API/database integration test. | Seed approver and pending invoice; approve, then fetch independently. Expect approved state after reread. |
| Approval fails during persistence → invoice unchanged | Partial writes could survive failure. Integration test with controlled failure at the storage boundary, retaining the real transaction behavior. | Compare relevant invoice fields and related transactional records before/after. Cover failure after a write has begun where feasible, rather than only rejecting before any write. |
| Viewer downloads invoice → correct file; approval unavailable | Download permission or assembled UI/server wiring could regress. One Playwright journey. | Sign in as viewer, open seeded invoice, download and inspect expected content; approval action is absent or unavailable. A screenshot alone cannot prove download success. |
| Approver submits approval → updated invoice; failure → recoverable error and unchanged invoice | UI could show success prematurely or retain stale optimistic state. Testing Library integration with network responses controlled at the boundary; one successful browser journey. | Delay, succeed and reject approval. Assert resulting status, pending behavior, error, preserved context and ability to retry. Inspect console output. |
| Both themes use approved semantic tokens and remain readable | Raw colors can escape typecheck and ordinary lint; token names alone do not establish contrast. Static enforcement plus rendered inspection. | Inspect normal, pending, error and disabled states at supported phone/desktop sizes in both themes. Retain named screenshots and contrast/keyboard findings. |

Recommend these targeted additions:

- **Token enforcement across all three style surfaces:** CSS property-value/custom-property rules, an ESLint AST rule for inline styles, and a compatible utility-class rule or narrow tested check. Inspect `tokens.css`, actual framework/version and existing configuration before selecting packages. Require approved semantic names; reject raw hex, named/function colors, arbitrary unapproved variables and utility color bypasses. Explicitly scope token definitions and justified exceptions.
- Prove the policy with valid and invalid fixtures for **each** style surface. Dynamic classes and computed style values may need explicit restrictions or remain documented gaps. Add selected rules to the normal lint/CI gate.
- A scoped `@axe-core/playwright` integration would catch common accessibility defects in relevant rendered states. It adds dependency and fixture maintenance; supplement it with keyboard, focus, zoom and contrast inspection. It cannot establish full accessibility.

Use existing Vitest, Testing Library and Playwright; no Storybook or Cucumber is needed. First confirm focused permission and failure tests fail for the missing behavior, then implement and confirm they pass. Deliberately bypass authorization or transaction rollback in an isolated copy if needed to demonstrate that assertions detect those faults.

Future execution uses the supplied `pnpm typecheck`, `pnpm lint`, `pnpm test`, and `pnpm test:e2e`; focused selectors must be discovered. The verify skill also names `scripts/agent/check`: establish whether it exists and what it runs before promising its full-run evidence.

Unknown setup includes app startup/health checks, API contract, authentication, seeded roles, database/reset commands, download format, supported viewports and theme controls.

**B — Heading copy only**

Expected result: the heading reads **“Invoices”**, retains its heading level and styling, and causes no unintended surrounding layout or interaction change. Its text width will naturally change.

The proportionate plan is:

1. Inspect the diff to confirm only the heading text changed.
2. Run existing applicable checks and inspect the rendered page at the normal viewport, with one narrow-width check for wrapping or displacement.
3. Compare before/after screenshots: only the intended text changes; surrounding positions, heading semantics and console state remain sound. Briefly exercise the nearest existing invoice-list interaction.

Do **not** add a dedicated text-only test, snapshot suite, token rule, accessibility scanner or other dependency for this change. Update an existing assertion only if it legitimately names the old heading; review that expectation change.

Startup, route and fixture setup remain unknown. Discover any full-check wrapper before invoking it. Review evidence should contain the one-line diff, actual existing-check output and direct visual inspection; no checks have run here.

**C — CLI archive backed by SQLite**

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Admin archives pending item → success; archived state persists | CLI wiring or durable storage could fail. CLI process integration against a real isolated SQLite file. | Seed pending item, run actual archive command, then reopen the database through a fresh connection/process. Assert archived state and agreed exit/output contract. |
| Reader or unknown role directly invokes archive operation → denied; storage unchanged | CLI argument handling could be the only authorization barrier. Integration through the callable application/service boundary, plus a CLI denial case. | Use trusted identity fixtures; assert denial and unchanged logical database contents. A supplied role flag must not grant authority. |
| Archive fails during a multi-write operation → storage unchanged | Incomplete rollback. Real SQLite transaction integration with controlled failure after an initial write. | Compare all affected tables before/after; assert no partial archive, history or related changes persist. Avoid byte-for-byte SQLite file comparisons. |
| Admin attempts to archive a non-pending item → denied; unchanged | State transition boundary could be missed. Focused public-operation integration test. | Seed a known non-pending state. Define exact error/exit behavior before implementation. |

Keep SQLite real in persistence tests; replace only unavailable external boundaries. A notification fake may record the outgoing request and simulate failures, but it does not prove provider delivery.

**Local evidence:** role denial, transaction rollback, durable archive, CLI exit/output and outgoing notification intent where the contract defines one.

**External gap:** real notification authentication, delivery and provider behavior remain unverified. Notification failure semantics are also unspecified: decide whether archive remains committed, rolls back or queues a retry before writing those expectations. Do not infer this from implementation.

CLI syntax, runtime/test runner, schema, migration/seed/reset commands, identity source, notification contract and test environment are unknown. Do not assume the invoice app’s `pnpm` commands apply. Discover the existing runner and use a temporary SQLite database per test. No browser, Cucumber or new database dependency is justified by the request.

**D — Profile editor with optimistic saving**

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Save succeeds → committed data matches saved draft | UI may claim success without persistence. Component integration plus one Playwright journey against real persistence. | Edit, save, then reload/fetch independently. Expect saved values. |
| Save fails → last committed data preserved, draft retained, retry available | Optimistic state could become committed accidentally or discard user input. Testing Library integration with delayed/rejected network responses. | Start with committed value A, edit to B, reject save. Assert persisted data remains A, editable draft remains B and retry is usable. |
| Retry succeeds → B becomes committed | Recovery could lose the draft or remain stuck pending. Continue the same integration scenario. | Retry B, accept response, then independently reread persistence. Expect B and cleared error/pending state. |
| User edits again while saving; responses fail or arrive out of order → newer draft/success is preserved | Stale responses could overwrite current work. Deterministic component tests controlling response order. | Save B, edit to C, resolve/reject earlier requests. Define whether overlapping saves are blocked, serialized or versioned; test the selected contract. |
| Server save fails after work begins → stored profile unchanged | A mocked HTTP rejection cannot prove storage rollback. Handler/storage integration with real isolated persistence. | Inject transactional failure; reread stored profile and affected records. |
| Keyboard-only save/error/retry → all controls reachable, draft retained, error announced | Failure feedback could be inaccessible. Browser keyboard test plus live-region/accessible-name assertions. | Tab through editing and saving; reject save; verify visible error, appropriate announcement semantics, sensible focus and reachable retry. |

For rendered evidence, delay and reject saves at supported phone/desktop widths. Inspect pending/error/retry states, zoom, focus visibility and unobstructed controls. Keep behavior traces/assertions separate from screenshots.

Recommend semantic-token enforcement for **CSS stylesheets and inline styles**, using the same tested allowlist approach described in A. Valid declared semantic tokens must pass; raw hex, named/function colors and undeclared or wrong-namespace variables must fail. Explicitly scope token definitions and approved exceptions. Static rules cannot establish rendered contrast.

A scoped axe integration is useful for common form/error defects, with ongoing state-fixture maintenance. Keyboard tests and announcement markup checks supplement it; actual screen-reader announcement behavior remains unverified until exercised with named assistive technology. Representative-user usability also remains unverified.

Use the supplied TypeScript, ESLint, Vitest/Testing Library and Playwright tools. Discover actual commands, profile route, app startup, persistence fixtures, reset procedure and authentication setup; they are unknown. Confirm the skill’s full-check wrapper exists before using it.

For every plan’s eventual review, record the final revision, environment, roles/data, criterion-by-criterion results, exact command summaries and evidence paths. Disclose failures, skips, flaky retries and uncovered criteria. These are planned expected results, not observed passes.