These are verification plans only. No files were changed, dependencies installed, or app checks run: this directory is a planning harness.

## Request A

Use concrete behavior examples to define expectations before implementation. Keep permission and persistence cases at the API/database boundary, with a few Playwright journeys proving the assembled application.

| Example and expected result | Risk → smallest sufficient check | Setup and execution | Review evidence |
|---|---|---|---|
| Viewer directly calls approval API → denied; invoice unchanged | UI-only authorization → Vitest integration test through the real handler and authorization layer, using an isolated real database | Authenticate as viewer; request approval of a pending invoice; reread persisted invoice independently | Actual denial response and before/after stored values |
| Approver approves pending invoice → approved and persisted | Incorrect transition or wiring → API/database integration | Authenticate as approver; approve seeded pending invoice; reread storage | Response plus persisted approved state and required approval metadata |
| Approval fails → invoice unchanged | Partial writes → integration test with controlled failure at the persistence/transaction boundary | Capture stored invoice; induce failure during approval, including after a write but before commit where applicable; reread independently | Failure response and unchanged persisted invoice, including status and approval metadata |
| Viewer downloads invoice → correct file; no approval action available | Broken download or role-dependent UI → one Playwright journey against the real application | Sign in as viewer, open seeded invoice, download it; inspect available actions | Download content matches seeded invoice; approval action absent; trace and console results |
| Approver uses approval control → pending, then approved; rejected request leaves UI and storage unchanged | Broken UI wiring or optimistic recovery → focused Testing Library failure cases and a critical Playwright approval journey | Delay/reject requests at the network boundary for component checks; exercise real approval in browser; refresh after failure | Assertions for final state, usable recovery and retained focus/context; independent storage assertion for persistence claims |
| Both themes use approved semantic tokens and remain legible | Hard-coded colors and theme defects → static enforcement plus rendered inspection | Test CSS, React inline styles and utility classes; render relevant success, pending and error states in both themes | Passing/failing policy fixtures, reviewed theme screenshots and contrast/accessibility findings |

Expected results come from the scenario, not production helper functions. Before implementation, confirm focused behavior tests fail for the missing behavior rather than broken setup. For existing behavior, introduce a targeted fault in an isolated copy to demonstrate that important assertions detect it.

**Missing checks to recommend**

- **Semantic token enforcement:** inspect `tokens.css`, existing lint configuration and utility framework first. Use a narrowly scoped CSS policy, such as Stylelint, plus existing ESLint with a suitable or custom AST rule for inline styles and compatible utility-class enforcement. A CSS-only rule cannot cover all three surfaces.
- Test each supported surface with an approved semantic token that passes, and forbidden hex, named/function colors, wrong token namespaces and raw/arbitrary utility values that fail. Token definitions and explicitly approved exceptions must pass. Document dynamic classes, spreads, computed values and other unsupported syntax as gaps. Review existing violations rather than suppressing them.
- **Accessibility:** recommend `@axe-core/playwright` for relevant rendered states, complemented by keyboard, focus and zoom checks. It adds a dependency and scan runtime; it cannot establish full accessibility or assistive-technology support.
- Reuse Playwright screenshot comparison where available. Otherwise capture and review stable before/after images; introduce only focused baselines warranted by the theme risk. Baseline approval requires inspection.

These additions carry rule maintenance, fixture upkeep and browser runtime costs. Verify installed versions and current official documentation before configuring them. Do not add Storybook, Cucumber, a mutation-testing framework or performance tooling for this scope.

**Rendered verification remains separate**

- **Interaction:** prove download contents, approval results and failure recovery. Exercise delayed responses and rapid repeat activation; check that no misleading success or stale rollback appears.
- **Visual:** inspect both themes at supported phone and desktop widths—provisionally 412px and 1440px—with stable fonts/data. Check clipping, overflow, action hit areas and pending/error layout stability. Label evidence as inspection or comparison against a reviewed baseline.
- **Accessibility:** scan relevant states and manually check keyboard access, focus retention, zoom and contrast. Report untested screen-reader paths.
- **Usability:** review clarity and recovery as an agent. Representative-user task completion remains unverified unless users are observed; this plan does not require a user study.

**Unknown setup and decisions**

The scenario does not establish API routes, denial/error status contracts, authentication fixtures, database engine/reset procedure, failure-injection mechanism, download format, approval metadata, non-pending transition rules, application startup/URL, supported devices or utility framework/version. Inspect existing conventions and document exact setup before execution. Resolve behavior-changing ambiguities rather than inventing requirements.

Known commands are `pnpm typecheck`, `pnpm lint`, `pnpm test` and `pnpm test:e2e`. Focused test-file commands remain unverified. Check whether `scripts/agent/check` exists and invokes the required full gates; do not assume it does.

For review, record the tested revision and dirty state, environment, fixtures/roles, one evidence line per criterion, actual command summary output, screenshots/traces, and all skips, retries or gaps. Run full checks against the final tree and review relevant authorization code, test expectations, token exceptions and gate changes.

## Request B

Change only “Invoices list” to “Invoices.”

Proportionate verification:

1. Inspect the diff: only the intended heading text changes; heading semantics, styles and behavior remain unchanged.
2. Run the existing full project checks and retain their actual output. Update an existing exact-text assertion only where the requested wording legitimately changes its expectation.
3. Open the invoice page and confirm the rendered heading is “Invoices.” Compare before/after screenshots at relevant phone/desktop widths and both themes. Expect unchanged surrounding layout and controls, with no clipping or new console errors.
4. Smoke-test a nearby existing interaction, such as opening an invoice. Confirm heading level and accessible name remain appropriate.

Do **not** add a new test, dependency, accessibility scanner or visual-testing system solely for this copy edit. Review any existing snapshot change explicitly. Usability with representative users and comprehensive accessibility remain unverified; neither is required to establish this small change.

Startup, URL and data setup are still unknown. No passing checks or browser results can be reported until the real application is available.