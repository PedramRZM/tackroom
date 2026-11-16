These are verification plans only. No implementation, installation, file changes or app checks were performed.

**Request A**

Record this plan before implementation. Use concrete behavioral examples for discovery, then red/green/refactor for meaningful new tests. Existing Vitest, Testing Library and Playwright suffice; neither Cucumber nor Storybook is needed.

| Example and expected result | Risk → smallest sufficient check | Setup, execution and review evidence |
|---|---|---|
| A viewer directly calls the approval API → permission denied; invoice remains unchanged. | UI restrictions could be bypassed → API integration with real authorization and an isolated test database. | Authenticate as a viewer, submit approval for a pending invoice, then independently reload its persisted fields. Preserve response and before/after state assertions. Exact endpoint and denial contract need confirmation. |
| An approver approves a pending invoice → approved response and persisted approved state. | Authorization, transition and persistence could be wired incorrectly → API/DB integration. | Seed an approver and pending invoice; call approval and reload it. Assert the agreed status and approval metadata using explicit expected values. |
| Approval fails → error response; persisted invoice remains unchanged. | Partial writes or optimistic success could survive failure → integration test plus a component recovery test. | Inject a controlled failure at the relevant external or persistence boundary without mocking the approval handler. Compare persisted invoice fields before/after. In the component, delay then reject approval: pending state clears, pending invoice remains visible, error is understandable and focus remains usable. |
| A viewer downloads an invoice → correct invoice file; no usable approval action. | Download could break or UI permissions could disagree with the server → one Playwright journey. | Sign in as viewer, open the seeded invoice and download it. Assert expected file format and invoice identity/content, not merely that a download event occurred. Capture UI and trace; API denial above remains essential evidence. |
| An approver approves through the UI → approved state survives reload. | Assembled UI/server wiring could fail → one Playwright journey. | Sign in as approver, approve a pending invoice, verify success and reload. Exercise download afterward as nearby regression coverage. |
| Both themes use approved semantic color tokens and remain legible. | Raw colors or wrong tokens could escape one styling surface → static enforcement plus rendered inspection. | Validate CSS, React inline styles and utility classes separately. Inspect both themes at supported phone/desktop widths, including pending, approved and error states. Preserve screenshots, contrast findings and console/network results. |

Resolve the expected behavior for non-pending invoices, repeated approval and failure recovery before encoding those cases. Include the resulting boundary examples at the cheapest sufficient level; do not duplicate the entire matrix in browser tests.

Recommended missing checks:

- **Token enforcement:** inspect `tokens.css`, permitted semantic names and utility framework/version first. Recommend a CSS policy using Stylelint, alongside scoped ESLint AST checks for inline styles and a compatible utility-class rule or narrow tested check. Prove that valid semantic tokens pass while raw hex, named/function colors and unapproved token namespaces fail in each supported surface. Explicitly scope token definitions and approved exceptions. Dynamic classes, spreads and imported values need coverage or documented gaps. These checks require configuration and fixture maintenance; they cannot prove contrast or correct visual meaning.
- **Accessibility:** add `@axe-core/playwright` to the existing browser runner for relevant rendered states. Supplement it with keyboard operation, focus through approval failure, zoom and contrast inspection in both themes. This adds dependency and scan maintenance and does not establish full accessibility.
- **Assertion effectiveness:** confirm focused behavioral tests fail before implementation for the intended missing behavior. If written afterward, introduce a targeted fault in an isolated copy—such as bypassing viewer authorization—and verify the test fails. A mutation-testing package is unnecessary initially.

Before configuring additions, verify official documentation for the actual installed versions. No performance tooling is justified by the stated change.

**Execution and evidence:** use focused Vitest/Playwright selections once actual test paths and package-script forwarding are known. At completion, run the documented `pnpm typecheck`, `pnpm lint`, `pnpm test` and `pnpm test:e2e`. Confirm whether `scripts/agent/check` exists and runs the full required gates; its availability is not established by this scenario.

The review should identify the final revision, dirty-tree status, environment, seeded roles/data, and one evidence entry per criterion. Include actual command summaries, red/green evidence, API responses, persisted-state assertions, browser traces and reviewed screenshots. Label screenshots as inspection or comparison against a reviewed baseline. Report skips, retries, failures and unverified paths. Agent inspection does not establish usability with representative users.

**Request B — independently**

Use one compact verification sentence: “The invoice page renders the heading ‘Invoices’ at the same semantic heading level, with unchanged surrounding layout and behavior.”

Run the existing project checks and inspect the running page before/after at supported phone/desktop widths and themes. Confirm:

- The heading reads exactly **Invoices**, with its heading semantics preserved.
- Font, spacing and surrounding element positions remain unchanged; the shorter text naturally occupies less width.
- Nearby invoice navigation/download behavior still works, with no new console errors.

Keep before/after screenshots and actual check summaries. Update an existing exact-text expectation or screenshot only where this requested wording change legitimately requires it, and review the diff. Do **not** add a new test, scanner, token rule, visual-testing system or dependency solely for this copy change.

**Unknown setup for both plans:** application startup command/URL, installed versions, test filenames, API routes/contracts, authentication fixtures, isolated database provisioning/reset, deterministic invoice/download data, failure injection, supported viewports and screenshot baselines. These must be established in the real application; no passing results are claimed here.