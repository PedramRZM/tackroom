Read `task.md`, the shipped `write-tests` and `verify` skills, their tool reference, and the applicable `ui-craft` guidance. These are four independent plans. No files changed, dependencies installed, or app checks run.

For substantive changes A, C and D, write focused tests before implementation and confirm they fail because the behavior is missing, then implement and refactor while green. Derive expectations from the requirements. Keep role and failure matrices at integration level; use a few browser or CLI journeys to prove wiring.

**A — Invoice permissions, approval and themes**

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Viewer directly calls approval API → denied; invoice unchanged | UI hiding cannot enforce authorization. Handler integration test using real authentication/authorization and an isolated database. | Seed viewer and pending invoice; call the actual approval endpoint; assert the documented denial response and reread stored invoice fields, including status/version/timestamps. Keep response and test output. Endpoint and exact denial contract are unknown. |
| Approver approves pending invoice → approved and persisted | Authorization and state transition may be wired incorrectly. API/database integration. | Seed approver and pending invoice; submit approval; assert success, reread through a fresh database connection, and fetch again through the API. |
| Approval fails during persistence → invoice unchanged | Partial writes can survive a failed request. Inject a controlled failure after a write begins, inside the real transaction boundary. | Compare persisted invoice state before and after failure. Include related approval records if present. A mocked error response alone is insufficient. |
| Approver submits a nonpending invoice; unknown role submits approval → no unauthorized transition | Boundary and default-deny behavior. Focused integration cases. | Agree the nonpending response contract before implementation; assert denial/rejection and unchanged storage. |
| Viewer opens invoice and downloads it → correct file; no approval action | Assembled UI/server wiring. One Playwright journey. | Sign in as viewer, open seeded invoice, download, verify file identity/content and absence of approval controls. Save trace and relevant assertions. |
| Approver approves; approval fails and retry succeeds → truthful status and usable recovery | Pending/error UI can mislead or strand users. Testing Library with network-boundary stubs, plus one real browser approval journey. | Delay and reject requests; assert no premature final approval, visible error, preserved invoice context and usable retry. Inspect console and keyboard focus. |

Theme enforcement needs more than screenshots:

- Inspect `tokens.css` and define the approved semantic-token policy. Cover CSS stylesheets, React inline styles and utility classes separately.
- Recommend a scoped CSS token rule, an ESLint AST rule for inline styles, and a compatible utility-class rule or narrowly tested checker. Reuse existing tooling where possible; add Stylelint only if it is the smallest maintainable CSS solution.
- For **each syntax**, prove approved semantic tokens pass; raw hex, named colors, color functions, wrong namespaces and raw fallback colors fail. Token definitions and reviewed exceptions must pass. Test arbitrary utility values; document dynamic/imported styles the rules cannot resolve.
- Cost: rule fixtures, policy maintenance and CI runtime. Static rules cannot establish contrast or visual quality. Framework/version compatibility is unknown; consult installed-version official documentation before configuring anything.

Render invoice normal, pending and error states in both themes at supported phone and desktop widths. Inspect contrast, focus visibility, overflow and zoom. Recommend `@axe-core/playwright` for common accessibility defects, with dependency/runtime and triage costs; supplement it with keyboard checks. Screen-reader paths remain unverified unless exercised.

**B — Heading copy only**

Expected result: the heading reads **“Invoices”**, retaining its heading level, typography, container geometry and surrounding behavior.

Use the existing checks and directly inspect the rendered heading at representative widths/themes. Compare before/after screenshots: only the intended text and its glyph width should differ; neighboring positions, wrapping and controls should remain stable. Check the accessible heading name and browser console, and briefly exercise the nearest existing invoice action.

Add no tests, tools, scanner, token policy or new snapshot suite for this copy edit. If an existing assertion or reviewed snapshot explicitly contains the old heading, update only that expectation and explain why. No user study or performance testing is warranted.

**C — CLI archive backed by SQLite**

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Admin archives pending item → success and durable archived state | In-memory success can conceal missing persistence. CLI integration against a temporary real SQLite database. | Invoke the executable with admin identity; assert documented exit/output; terminate it, reopen the database in a fresh process and query the stored item. |
| Reader or unknown role directly invokes archive → denied; storage unchanged | A CLI wrapper may bypass the domain/service permission check. Test both the executable and the directly callable archive boundary. | Seed each identity and pending item; assert nonzero denial result and unchanged relevant rows. Do not mock authorization. |
| Admin archives nonpending or missing item → documented rejection; no mutation | State-boundary behavior. Focused integration cases. | Agree exact output/exit contracts; compare database state before/after. |
| Archive encounters a write failure → failure and unchanged storage | Partial writes and broken transaction handling. Real SQLite transaction test with deterministic failure after mutation begins. | Assert rollback of the item and related rows using a fresh connection. Keep database assertions and CLI output. |
| Ordinary read/list still works after archive | Nearby regression. Existing CLI integration smoke check. | Invoke the neighboring command and assert the agreed visibility of archived items. That visibility policy is currently unknown. |

Use the project’s existing CLI/language test runner once discovered; do not assume the web project’s commands apply. Temporary database creation, migrations, identity injection, CLI invocation and reset commands are unknown.

Replace the unavailable notification service only at its external boundary for local tests. Record the request payload and simulate success, rejection and timeout. Local evidence can prove application handling and any durable outbox entry; it cannot prove provider authentication, delivery or real retry behavior.

The notification/commit contract needs resolution: if notification failure means archive failure, storage must remain unchanged; if notification is asynchronous, archive may succeed with durable delivery work recorded. Do not invent this policy. Real-service verification remains a named gap requiring an appropriate service environment.

**D — Optimistic profile editor**

| Example → expected result | Risk and smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| Save committed profile P0 with draft P1; reject save → storage remains P0, draft remains P1, retry available | Optimistic state can destroy committed data or user input. Testing Library interaction test plus API/database failure test. | Seed P0, type P1, submit, delay then reject. Assert truthful failure state, retained fields and usable retry; independently reread persisted P0. |
| Retry P1 successfully → P1 persists | Recovery may appear successful without storing data. Component integration and one browser journey against real persistence. | Retry through the UI, assert confirmation, then reload/fetch through a fresh session and verify P1. |
| Older failure arrives after newer success → newer success remains | Stale responses can roll back good data. Deterministic component test controlling response order. | Send two saves where concurrency is supported; resolve newer success first, then older failure. Assert latest committed result and draft remain correct. If saves are serialized, prove that policy instead. |
| Edit while saving; double-activate Save → later draft preserved, no unintended duplicate effects | Pending state may lose edits or create conflicting writes. Component interaction tests. | Hold response, edit again and activate Save rapidly; assert the agreed scheduling policy and final data. Define that policy before implementation. |
| Keyboard-only failed save and retry → reachable controls, preserved context, announced error | Recovery may be inaccessible. Browser keyboard test and manual assistive-technology check. | Tab through fields, submit, reject, reach Retry and succeed. Assert sensible focus, field associations and an accessible error/status announcement; verify actual announcement with a screen reader if available. |

Apply the token policy to **both CSS stylesheets and inline styles**: approved semantic tokens pass; raw hex/named/function colors, undeclared tokens and raw fallbacks fail; definitions and approved exceptions pass. Use tested CSS and ESLint rules with documented dynamic-value gaps. Their maintenance cost is justified by the explicit constraint; screenshots alone cannot enforce it.

Use Playwright to delay/reject saves and inspect normal, pending, failed and recovered states at supported widths and themes. Check stable controls, long input/error text, zoom, focus and error contrast. Recommend the same scoped accessibility scanner addition as A. Automated scans do not prove spoken announcements or full accessibility. Representative-user understanding and recovery remain unverified without user observation.

**Execution and evidence for review**

For A, B and D, the supplied existing commands are:

```text
pnpm typecheck
pnpm lint
pnpm test
pnpm test:e2e
```

Focused test selectors are unknown. The verify skill also requires the full `scripts/agent/check`; its existence and coverage are unverified. Inspect it before execution, report a missing script explicitly, and retain output from the applicable existing commands. Proposed token/accessibility gates should enter the normal check command and CI only after their fixtures demonstrate effectiveness. No Storybook or Cucumber addition is needed.

For each independent change, record the final revision/uncommitted diff, environment, role and fixtures; then one evidence line per criterion with actual command output or interaction result. Attach storage assertions, CLI/API output, browser traces, screenshots and console findings as applicable. Distinguish visual inspection from reviewed-baseline comparison. Report skips, retries, failures and unverified criteria explicitly.

App startup, authentication seeds, fixture/reset commands, database setup, supported viewports, browser/font configuration and existing baselines are unknown. Those must be discovered and documented before execution. No passing result is claimed here.