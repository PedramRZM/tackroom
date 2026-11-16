# Choose checks for the risk

Start with the repository's installed tools and exact commands. A recommendation names the
uncovered failure, the chosen check, its setup/runtime cost and its blind spots. Verify current
official documentation for the installed version before configuring a new rule or tool.
The choices below are candidates, not required dependencies.

## Match the check to the claim

| Claim or risk | First choice | What it does not prove |
|---|---|---|
| Types, forbidden imports/syntax, architecture boundaries | Existing compiler/linter; ESLint AST rule for JS/TS, or the language's equivalent | Intended behavior or a sensible architecture |
| Business rules, parsing, state transitions | Existing unit runner; property tests for invariants; differential tests for rewrites | Correct wiring through the full application |
| Components, handlers, persistence or authorization interact correctly | Integration/component tests through public surfaces; Testing Library where appropriate; real isolated DB when DB behavior matters | Real browser layout or uncontrolled providers |
| A critical user journey works through the assembled product | Existing E2E runner; Playwright Test for a web project needing one | Every edge case or a useful product |
| Layout regressed | Playwright screenshot comparisons; existing Storybook visual workflow | Whether the baseline is good design |
| Common accessibility defects | axe-core integration, such as `@axe-core/playwright`, on relevant rendered states | Full accessibility; add keyboard/focus/zoom and relevant assistive-technology checks |
| Performance regressed | Existing bundle/query budgets; Lighthouse CI for controlled lab checks; field Web Vitals when available | Lab scores do not prove real-user performance |
| Assertions might be ineffective | A deliberate fault in an isolated copy; targeted mutation testing such as Stryker for important logic | Correct requirements; surviving mutations need interpretation |
| Users understand and can complete the task | Observe representative users attempting realistic tasks | An agent critique or automated score is not user research |

Use browser tools for exploration and immediate evidence. Save a repeatable regression in the
project's test runner when the behavior warrants one. A browser interaction is not automatically
an E2E test suite. Keep most edge cases at a cheaper boundary and a small number of real journeys
to prove wiring. Avoid asserting the same exhaustive matrix at every level.

## Example: enforce design tokens

For Tailwind v4, consider the official [`@shadcn/lint`](https://github.com/shadcn-ui/lint)
ESLint/Oxlint plugin. Select policies for the actual design system; installation alone does not
enforce them. When the optional `ui-craft` skill is installed, its
[verification reference](../../ui-craft/references/verification.md) covers static-analysis
blind spots and complementary browser checks. Otherwise use the guidance below and the
project's existing tools; the optional UI profile can be added when needed.

First inspect the token source, allowed semantic names, style syntax and existing lint plugins.
Use a design system's own rule when it fits. Atlassian's token rule targets its token API;
do not install it in an unrelated design system and assume coverage.

- **CSS:** Stylelint property-value rules can restrict values, and custom-property allowlists
  can constrain token names by property. Scope token definitions, generated/vendor files and
  justified exceptions explicitly. Validate the policy against the project's actual CSS.
- **JS/TS styles:** use the existing design-system ESLint rule, or a scoped AST rule with
  actionable messages. Test it with valid and invalid cases, using RuleTester for a custom rule.
- **Utility classes:** use a compatible rule for the installed framework/class syntax or a
  narrow tested check. Cover arbitrary values and dynamic classes explicitly, or report them
  as gaps. A CSS-only rule does not inspect these source strings.

Rejecting hex alone misses named colors and color functions. Checking variable names alone
does not require token use. An arbitrary `var(--anything)` is not necessarily an approved token.
Lint can enforce an approved token API; rendered checks must still assess contrast and themes.

Prove a policy works before adding it to the check command: valid semantic token passes;
forbidden hex, named/function color and wrong token namespace fail in supported syntax;
token definitions and approved exceptions pass. Include a case in each style surface the app
uses and name anything the rule cannot analyze. Do not quietly suppress existing violations.

## Example: one behavior, several checks

Suppose the requirement is: a viewer may download an invoice but may not approve it.

| Expected example | Check and reason | Setup/evidence |
|---|---|---|
| Viewer directly requests approval → denied, invoice unchanged | API/DB integration: hiding a control cannot enforce permissions | Isolated viewer + invoice; assert denial and persisted state |
| Approver approves a pending invoice → approved | Integration checks transition and persistence; unit/property checks cover rule edges | Trusted domain examples; do not compute expected results using production code |
| Viewer opens invoice → download works, no approval action | One browser journey: assembled UI and server wiring | Seeded role/data; assert downloaded content and visible state |
| Both themes use approved tokens and remain legible | Static token rules plus rendered theme/contrast inspection | Known-bad lint fixture; named viewport/theme screenshots and accessibility findings |

In the actual task, replace these descriptions with exact commands or UI steps and expected
outputs. Record what should fail before implementation. Do not add Cucumber merely to store
these examples; use it when collaborators already maintain executable feature files.

## Keep the feedback loop affordable

- Inner loop: relevant lint/types and focused behavior tests. Full project checks at completion.
- Broader boundary: integration tests, build and critical E2E journeys as the task requires.
- UI: stable data/fonts/browser/viewport for visual checks; review baseline changes against
  the intended change. Never approve new snapshots just because the test runner offers to.
- Expensive mutation, browser matrices and benchmarks: run for the risk they address, not for
  every copy edit. Record duration and flaky retries before optimizing the suite.
- For blocking Lighthouse CI budgets, choose explicit error-level assertions and aggregation;
  warnings do not fail the command, and its default aggregation is optimistic. Measure variance
  before choosing thresholds; do not treat an unconfigured run as an enforced budget.

The project check command and CI should call the same selected gates. Treat skips, quarantine
and retry-green results as visible limitations; give quarantined tests an owner and repair task.
Workspace hooks and a second model are useful feedback, not tamper-proof independent execution.
Where trusted acceptance enforcement is required, it belongs outside the implementer's writable
workspace and must use reviewed tests/configuration.

## Primary references

Workflow and test mix: [BDD](https://cucumber.io/docs/bdd/),
[Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications),
[Playwright practices](https://playwright.dev/docs/best-practices).
Policy rules: [ESLint selectors](https://eslint.org/docs/latest/rules/no-restricted-syntax),
[custom rule tests](https://eslint.org/docs/latest/extend/custom-rule-tutorial),
[Stylelint values](https://stylelint.io/user-guide/rules/declaration-property-value-allowed-list/),
[Stylelint token names](https://stylelint.io/user-guide/rules/declaration-property-custom-property-allowed-list/),
[Atlassian token rule](https://atlassian.design/components/eslint-plugin-design-system/ensure-design-token-usage/usage).
Product evidence: [visual comparisons](https://playwright.dev/docs/test-snapshots),
[accessibility](https://playwright.dev/docs/accessibility-testing),
[W3C evaluation](https://www.w3.org/WAI/test-evaluate/),
[mutation testing](https://stryker-mutator.io/docs/),
[Lighthouse CI](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html).

The combination and examples are local judgment; these sources do not establish a universally
optimal test pyramid. The research register is in tackroom's `docs/testing.md`.
