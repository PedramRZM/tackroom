Applied the project’s `write-tests`, `verify`, and shared `verification-tools.md` reference. These are plans only: no files changed, dependencies installed, network used, or app checks run. This directory is a planning harness.

### Request A

Use concrete behavior examples for discovery, then red/green/refactor for meaningful new behavior. Existing Vitest, Testing Library, and Playwright suffice for behavioral coverage; Cucumber and Storybook are unnecessary.

| Example and expected result | Risk → smallest sufficient check | Setup and execution | Review evidence |
|---|---|---|---|
| An authenticated viewer directly requests approval → denied; invoice remains unchanged | UI restrictions can be bypassed → API integration through the real authorization handler and isolated persistence | Seed viewer and pending invoice; call approval endpoint directly; compare persisted invoice before/after | Actual denial response and persisted-state assertions |
| An approver approves a pending invoice → approval succeeds and persists | Authorization, transition and storage may be wired incorrectly → API/DB integration | Seed approver and pending invoice; request approval; read persisted result | Response and explicit approved-state assertions |
| Approval fails → invoice remains unchanged | Partial writes or optimistic UI can leave false success → integration failure case, plus component test for recovery | Induce a deterministic failure at the relevant external/persistence boundary; inspect stored invoice. In the component, return an API failure | Unchanged persisted invoice; UI remains pending, reports failure and permits appropriate recovery |
| Viewer downloads an invoice → correct file downloads; approval action is unavailable | Assembled UI/server wiring may break → one Playwright journey | Sign in as seeded viewer, open invoice, download; inspect file content and approval controls | Download assertions, before/after screenshots and console output |
| Approver approves through the UI → pending becomes approved and remains approved after reload | Component tests cannot prove full wiring → one Playwright journey | Sign in as approver, open seeded pending invoice, approve, reload | Persisted visible status and interaction evidence |
| Both themes use approved semantic tokens and remain legible | Raw colors or unsuitable token choices can escape behavioral tests → static enforcement plus rendered inspection | Exercise both themes at 412px and 1440px, including pending, approved and failure states | Theme screenshots, contrast/accessibility findings and rule-fixture results |

**Resolve before implementation:** exact denial status/body, approval success contract, relevant failure modes and boundaries, and behavior for already approved or otherwise nonpending invoices. Do not invent those domain rules. Add focused unit tests only if transition logic has meaningful boundaries beyond what integration tests cover.

**Missing checks to recommend:**

- **Token enforcement across all three style surfaces.** Inspect `tokens.css` and actual syntax first. Use CSS property/value and approved-token rules, a scoped ESLint AST rule for inline styles, and a compatible utility-class rule or narrow tested check. Recommend Stylelint only if needed for CSS coverage. Reject raw hex, named colors, color functions, and unapproved token namespaces; merely accepting `var(--anything)` is insufficient.
- Prove each rule with valid and invalid fixtures for CSS, inline styles and utility classes. Token definitions and approved exceptions must pass. Explicitly report dynamic classes or expressions that cannot be analyzed. Maintenance includes allowlists, exceptions and syntax coverage; lint cannot prove rendered contrast.
- **Accessibility scanning:** recommend `@axe-core/playwright` for relevant rendered states, supplemented by keyboard, focus and zoom inspection. This adds dependency and browser runtime cost and cannot establish full accessibility.
- Use existing Playwright for visual evidence; introduce screenshot regression baselines only where repeated regression protection warrants their stabilization and review cost. No performance tooling or broad mutation suite is justified by this request.

Before configuring additions, verify documentation for the installed versions during implementation. That was not done here because network use is prohibited.

**Execution and evidence:** first confirm focused tests fail for missing behavior, rather than broken setup. Use deterministic data and controlled failures; never mock the authorization or transaction behavior being proved. Deliberately introduce representative token violations to demonstrate enforcement.

Known commands are `pnpm typecheck`, `pnpm lint`, `pnpm test`, and `pnpm test:e2e`. The skill requires the full `scripts/agent/check`; its availability and composition must be confirmed in the actual app. Ensure it and CI invoke the selected gates. Exact focused-test commands remain unknown.

Report the final revision and uncommitted changes, environment, seeded roles/data, one observed result per criterion, actual command summary lines, screenshots and API evidence. Include failures, skips and retry-green results. Review security enforcement and token-policy scope alongside tests. Label visual evidence as inspection or reviewed-baseline comparison; representative-user usability and untested assistive-technology paths remain unverified.

### Request B

Change only the heading text to **“Invoices.”** Proportionate verification is existing checks plus direct rendered inspection; add no tests or tools solely for this copy edit.

- Run the existing full check command once its availability is confirmed. Update an existing heading assertion only if it legitimately expects “Invoices list,” and explain that expectation change.
- Open the same page before and after with stable data, fonts and viewport. Confirm the heading reads “Invoices,” retains its semantic heading level, and introduces no unintended wrapping, spacing or neighboring layout change at 412px and 1440px in both themes.
- Capture before/after screenshots, inspect the console, and exercise the closest existing invoice interaction to confirm it still works. Review any existing screenshot baseline change against the requested text change.
- No new accessibility scanner, screenshot suite, mutation testing, Cucumber, Storybook or performance tooling is warranted. Inspect heading semantics and zoom directly; do not claim a full accessibility audit or user study.

For both requests, app startup/health commands, route, API contract, authentication fixtures, isolated database setup/reset, failure injection, installed versions and exact test-file commands are unknown. These must be established in the real application before either plan can produce verification results.