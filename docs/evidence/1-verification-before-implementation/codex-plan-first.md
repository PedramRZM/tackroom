Applied the project’s exact [write-tests skill](.agents/skills/write-tests/SKILL.md), [verify skill](.agents/skills/verify/SKILL.md), and shared [verification-tools reference](.agents/skills/write-tests/references/verification-tools.md).

This is a planning exercise. No files were changed, dependencies installed, network tools used, or application checks run.

**Request A**

Record these examples and expected results before implementation. Use the installed Vitest, Testing Library and Playwright tools; most permission and failure cases belong at the API/persistence boundary.

| Example → expected result | Risk → smallest sufficient check | Data/environment and execution | Review evidence |
|---|---|---|---|
| Viewer directly calls approval API → denied; invoice unchanged | Authorization bypass → API integration test through the real handler and authorization layer, with an isolated database | Authenticated viewer and pending invoice; send the actual approval request, then independently read persisted invoice data | Denial response and before/after persisted values |
| Approver approves pending invoice → approved and persisted | Incorrect transition or wiring → API/database integration test | Authenticated approver and pending invoice; call approval, then read it back | Successful response and persisted approved status |
| Approval fails → invoice unchanged | Partial writes → integration test injecting a controlled failure at the external or persistence boundary | Fresh pending invoice; induce the relevant failure, then inspect persisted data | Failure response and unchanged invoice fields, including status and approval metadata |
| Viewer downloads invoice → correct download; no approval action | UI permissions and assembled download flow → one Playwright journey | Sign in as viewer, open seeded invoice, download, inspect content against that invoice; verify approval action is absent | Download assertions, rendered state, screenshots and console findings |
| Approver approves pending invoice → UI shows approved state that survives reload | Assembled critical flow → one Playwright journey | Sign in as approver, open pending invoice, activate approval, inspect result and reload | Assertions before/after reload, screenshots and console findings |
| Both themes use approved semantic tokens and remain legible | Unenforced source policy and theme defects → static enforcement plus rendered inspection | Exercise CSS, inline styles and utility classes; inspect invoice states in both themes at representative mobile and desktop widths | Rule fixtures, theme screenshots, contrast and keyboard/focus findings |

Before implementing meaningful behavior, confirm focused tests fail because the required behavior is missing, rather than because setup is broken. After implementation, repeat them and preserve the red/green evidence. If written afterward, prove effectiveness with a targeted fault in an isolated copy. Do not mock the authorization or transition being tested.

Missing checks worth recommending:

- **Token enforcement:** inspect `tokens.css`, approved semantic names and existing plugins first. Use a suitable Stylelint policy for CSS and scoped ESLint AST rules for inline styles; add a compatible utility-class check. Cover arbitrary values and dynamic classes, or explicitly report analysis gaps. Reject hex, named/function colors, and unapproved token namespaces. Valid tokens, token definitions and approved exceptions must pass. Test each supported style surface. Cost: configuration, fixtures and exception maintenance; static rules cannot prove contrast or visual quality.
- **Accessibility scanning:** consider `@axe-core/playwright` for relevant rendered states. Cost: dependency and browser-test maintenance. Supplement with keyboard, focus and zoom checks; automated scans do not establish full accessibility.
- **No additional behavior runner:** Cucumber and Storybook are unnecessary for these examples. Existing tools suffice. A targeted deliberate fault can establish assertion effectiveness without adding a mutation-testing platform.

Before configuring additions, verify official documentation for the installed versions during implementation; that verification has not happened here. Wire selected gates into both CI and the project check command, without suppressing existing violations.

Concrete future verification commands supplied by the scenario are:

```text
pnpm typecheck
pnpm lint
pnpm test
pnpm test:e2e
```

The verify skill also requires the full `scripts/agent/check`; its availability and contents must be established in the real application. Focused test filenames and commands remain unknown.

Setup that must be established before execution: app startup command and URL, authenticated role fixtures, isolated database provisioning/reset, invoice factories, API route/method/payload, download format, deterministic failure injection, theme controls, and stable browser/fonts/data. Agree on the API denial/error contract and failure cases if existing conventions do not settle them.

For review, identify the final revision and uncommitted changes; report one evidence line per criterion, actual command summary output, screenshots, console findings, and nearby regression checks. Include download behavior after approval and recovery after failure where they share changed code. Show skips, quarantines and retry-green results. Security review must also inspect server authorization and transaction boundaries; passing tests alone cannot establish security.

**Request B**

Use a one-sentence verification plan: “The invoice heading reads ‘Invoices’; its heading semantics, layout and nearby behavior remain unchanged.”

Proportionate verification:

- Inspect the diff for the single text replacement. If an existing assertion expects “Invoices list,” update that expectation and explain why.
- Run existing project checks, including the full check wrapper when available; retain actual output.
- In the running app, capture before/after screenshots at representative mobile and desktop widths in both themes. Confirm the heading reads “Invoices,” retains its semantic level, and causes no wrapping, spacing or nearby layout change. Read the browser console and smoke-test the nearest existing interaction.

Do **not** add a new test suite, snapshots, accessibility scanner, token rules or other tooling solely for this copy edit. Existing checks and direct inspection are sufficient.

App startup, URL, sign-in and data setup remain unknown. Neither request is verified against an application; all results above are expected outcomes and planned evidence.