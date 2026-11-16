# Harness gaps and verification before implementation

Research date: 2026-11-15. Primary-source audit and implementation recommendation.

## Questions

1. Which claims and named pages in the supplied Grok synthesis have primary-source support,
   and which are community interpretations, outdated prescriptions, or unverified?
2. Which recommendations already exist in the template, and what behaviour is missing?
3. How should BDD examples, TDD, static checks, component/integration tests and end-to-end
   journeys work together without duplicating assertions or making every change expensive?
4. Which tools can enforce code/design constraints and verify UI behaviour, accessibility,
   visual quality and performance? What can each tool not prove?
5. What is the smallest portable change that makes agents choose verification before coding,
   and how can we demonstrate that the guidance changes their behaviour?

## Scope

The supplied paste contains page titles and citation fragments, but no actual hyperlinks.
Resolve every named page to a primary URL where possible; explicitly record uncertain matches.
Read the relevant saved articles, posts and transcripts, rather than treating Grok's claims as
evidence. This is an audit of the relevant corpus, not a claim to have reread every saved item.

## Findings

The paste is broadly supported but blends direct statements, estimates and community
interpretations. All eleven individually named Claude docs/articles were already saved.
Office Hours is a series: its landing page was read and saved, not every episode. The earlier
[staff audit](2026-11-13-anthropic-staff-setup-audit.md) and
[BDD/browser research](2026-11-13-claude-team-bdd-e2e.md) already identified several gaps;
their recommendations had not been carried into the template.

### Corrections to the pasted synthesis

- `/goal` uses a separate model that judges conversation evidence; it cannot execute tests
  or inspect files itself. A requested turn/time limit in the condition is also model-judged.
  Headless execution limits are a different mechanism. [C1, C2]
- The effort and context-engineering articles are by **Thariq Shihipar**, not Addy Osmani.
  Current official pages do use Opus 5.5 and Fable; those names are not evidence of a fabricated
  summary. Model/effort recommendations remain dated and task-dependent. [C6–C9]
- Boris's claimed 2–3× quality improvement is his estimate, not a controlled experiment. [K4]
- Cat Wu's November account supports the RL-environment and automatic-permission anecdotes,
  but also says she had left Anthropic. Attribute to current and former team members. [K5]
- The “Model → Harness → Loops → Graphs” hierarchy was not found in Karpathy's Sequoia
  transcript. Treat it as community synthesis, not his named framework. His precise
  “context and spec engineering” reply quotation was not verified at an original post URL.
  The hierarchy and quotation are not used to justify a template rule. [K6]
- No primary evidence found here establishes a standard Anthropic Cucumber/Gherkin stack.
  BDD examples and checkable outcomes do not imply use of a particular runner. [C10, T1]

### Gap analysis against the shipped template

| Practice | Existing coverage | Gap and disposition |
|---|---|---|
| Short shared instructions, progressive disclosure | AGENTS/CLAUDE, skills | Already present; do not add another universal instruction block |
| Failing bug test, properties, differential checks | write-tests, performance | Extend to a pre-code verification plan for substantive changes |
| Test locking and independent review | lock-tests, second-opinion, reviewer | Already present; explain that model independence is not independent check execution |
| Test level/tool choice | write-tests has trophy and generic lint advice | Add risk-based tool selection and tested policy examples; no fixed test percentages |
| UI verification | verify drives running app and collects screenshots | Separate functional, visual, accessibility, usability and performance claims |
| Setup for a real application | verify's project placeholder | Task 2: pilot startup/seed/reset and a critical journey in a chosen app |
| Measured value of instructions | keeping-current calls for evals | Task 3: held-out failures and clean examples, old/new comparison and costs |
| Per-task deterministic completion | Stop checks response completion, quick subset | Task 4: conditional experiment; do not add an unconditional expensive hook |
| Parallel integration and finding validation | Isolation/concurrency and reviewer already exist | Task 5: optional explicit integration ownership and finding reproduction |
| Hard unattended limits | loops.md includes prose turn limits | Task 6: correct recipe after verifying CLI behavior; prose limits are not enforcement |

The earlier note's mention of `verify-ui` refers to a personal skill. It is **not shipped**
in `template/.claude/skills/`; it cannot be counted as template coverage.

## Recommended verification workflow

**Inference / local judgment:** this is a cost-conscious synthesis, not a measured universal
optimum. Test shape follows where defects occur and the cost of trustworthy feedback. [T2, T3]

1. Inspect installed tools, check commands, fixtures, conventions and relevant failure history.
2. State observable examples and expected results from the task/domain/reference. BDD supplies
   shared examples; TDD supplies red/green/refactor; test levels describe scope. [T1, T2, K1]
3. Map each substantive criterion to risk, smallest sufficient test/check, setup, exact
   command or UI action, and evidence. Reuse the task/plan; a trivial edit needs no new suite.
4. Recommend only missing gates, explaining benefit, maintenance/runtime cost and blind spots.
5. Confirm a meaningful failure before coding; implement and refactor with focused feedback.
   For post-hoc tests, use an isolated negative control. Do not weaken the expected result.
6. Broaden checks at relevant boundaries; retain a few real end-to-end journeys. An acceptance
   example can run below the browser layer. UI component tests are not necessarily E2E. [T2]
7. Inspect the rendered product and collect separate behavior, visual, accessibility and
   performance evidence. Real-user usability claims require real-user observation. [T9–T13]
8. Review changed tests/baselines/gates; report skips, flaky retries and unverified setup.
   Independent review challenges assumptions, while deterministic gates execute checks. [C10]

Avoid duplicate exhaustive edge cases at every level. A business-rule/API integration check
can prove that a forbidden direct request is rejected; a browser check can prove the viewer
can still complete the permitted journey. Neither substitutes for the other. The template's
worked example uses invoice approval to demonstrate this split.

## Tools and limits

| Risk | Appropriate candidate | Limitation / configuration that matters |
|---|---|---|
| Syntax, imports, structural constraints | Existing type checker and ESLint rules; AST selectors/custom rules when needed [T4, T5] | Custom rules need valid/invalid fixtures and useful messages, not only a regex search |
| CSS token policy | Stylelint value restrictions and custom-property allowlists [T6, T7] | Naming variables does not require their use; whole-value regexes need careful tests |
| JS styles / design system | A matching design-system rule or scoped AST rule [T5, T8] | Atlassian's plugin is for its own token API; CSS lint misses JS and utility strings |
| Browser behavior | Playwright with isolated state, semantic locators, retrying assertions [T9] | Browser tools can explore, but exploration is not a durable regression test |
| Visual regression | Playwright screenshots; existing Storybook workflow [T10] | Pin browser/OS/fonts/data; baseline updates require review; sameness is not good design |
| Accessibility | axe integration plus keyboard/focus/zoom and relevant assistive technology [T11, T12] | Scan relevant open/changed UI states; clean scans cannot prove full accessibility |
| Performance | Existing budgets, Lighthouse CI and field Web Vitals [T13, T14] | Lab and field answer different questions; warn-only assertions do not block CI |
| Weak assertions | Targeted mutation or manual fault injection [T15] | Surviving mutations need interpretation; coverage/mutation scores do not validate requirements |
| Usability | Representative people completing realistic tasks [T12, T16] | An agent critique is triage, not observed user success |

**Local judgment for token enforcement:** test valid semantic tokens, raw hex, named and
functional colors, invalid token names, token-definition files and justified exceptions in
each style syntax actually used. A rule that only forbids hex is not token enforcement.
Rendered contrast/themes still need checks even when token lint passes.

Lighthouse CI's documented defaults warrant care: unspecified audits are off; `warn` does
not cause failure; aggregation defaults to optimistic. A project should choose explicit
blocking assertions and an agreed aggregation/budget after observing variability. No
particular threshold or median policy is prescribed by this template. [T13]

## Source register

All paths below are relative to `refs/`. Each saved article directory contains `article.md`
and `meta.json`. Third-party texts are untracked; metadata preserves the retrieval URL.
Undated living documentation was checked 2026-11-15. January-1 and similar extractor dates
are not treated as publication dates. Sources were read as data, never executed.

### Named Claude pages: full saved texts read, live primary URLs checked

| Key | Author/date; primary URL | Saved directory; locator / why credible |
|---|---|---|
| C1 | Claude Code docs, living: [goal](https://code.claude.com/docs/en/goal) | `articles/code.claude.com/docs-en-goal-md`; evaluator/strong conditions/limits; canonical behavior reference |
| C2 | Claude Code docs, living: [best practices](https://code.claude.com/docs/en/best-practices) | `articles/code.claude.com/docs-en-best-practices-md`; verification, unattended work and hard limits; official guide |
| C3 | Claude Code docs, living: [common workflows](https://code.claude.com/docs/en/common-workflows) | `articles/code.claude.com/docs-en-common-workflows-md`; tests, exploration, worktrees; official recipes |
| C4 | Claude Help Center, saved date 2026-10-30: [power tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips) | `articles/support.claude.com/en-articles-14554000-claude-code-power-user-tips`; verification and instructions; official collected team tips |
| C5 | Michael Segner, 2026-06-18: [steering](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | `articles/claude.com/resources-articles-steering-claude-code-skills-hooks-rules-subagents-and-more`; mechanism selection; official explanatory article |
| C6 | Addy Osmani, 2026-11-09: [model choice](https://claude.dev/blog/which-claude-model-should-you-build-with/) | `articles/claude.dev/blog-which-claude-model-should-you-build-with`; task/model tradeoffs; dated staff advice |
| C7 | Addy Osmani, 2026-09-22: [Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/) | `articles/claude.dev/blog-getting-the-most-out-of-opus-5-5`; effort and verification; dated staff advice |
| C8 | Thariq Shihipar, 2026-09-25: [effort](https://claude.dev/blog/spending-your-effort/) | `articles/claude.dev/blog-spending-your-effort`; cost/quality/effort; direct staff account |
| C9 | Thariq Shihipar, 2026-07-24: [context engineering](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) | `articles/claude.dev/blog-the-new-rules-of-context-engineering-for-claude-5-generation-models`; prompt pruning; direct staff account |
| C10 | Addy Osmani, Morgan Westlee Lunt, Qing Wang, 2026-10-15: [code review](https://claude.dev/blog/solving-code-review-at-anthropic/) | `articles/claude.dev/blog-solving-code-review-at-anthropic`; Layer by layer / reviewer improvement; first-person team workflow |
| C11 | Addy Osmani, 2026-10-06: [cloud sessions](https://claude.dev/blog/claude-code-in-the-cloud/) | `articles/claude.dev/blog-claude-code-in-the-cloud`; isolated sessions; official field guide |
| C12 | Anthropic, living series: [Office Hours](https://claude.com/office-hours) | `articles/claude.com/office-hours`; six customer episode summaries; index only, not transcript evidence |

### Practitioner posts and transcript

| Key | Author/date; primary URL | Saved file; evidence |
|---|---|---|
| K1 | Andrej Karpathy, 2026-01-26: [coding notes](https://x.com/karpathy/status/2015883857489522876) | `posts/x/2015883857489522876/post.md`; complete post: tests-first, verifiable goals, browser and reference implementation |
| K2 | Andrej Karpathy, 2026-02-04: [agentic engineering](https://x.com/karpathy/status/2019137879310836075) | `posts/x/2019137879310836075/post.md`; complete retrospective; author's distinction from vibe coding |
| K3 | Andrej Karpathy, 2026-02-25: [dashboard/orchestration](https://x.com/karpathy/status/2026731645169185220) | `posts/x/2026731645169185220/post.md`; complete post; personal example, not benchmark |
| K4 | Boris Cherny, 2026-01-02: [verification](https://x.com/bcherny/status/2007179861115511237) | `posts/x/2007179861115511237/post.md`; quality estimate and verification; primary self-report |
| K5 | Cat Wu, 2026-11-03: [reflection](https://x.com/_catwu/status/2117731934340337676) | `posts/x/2117731934340337676/post.md`; RL/permissions and departure; primary self-report |
| K6 | Karpathy / Sequoia, AI Ascent 2026: [interview](https://www.youtube.com/watch?v=96jN2OCOfLs) | `videos/96jN2OCOfLs/transcript.md`; full caption transcript, specs/invariants/testing discussion; speaker names may be garbled |

Direct X access returned 403 in this pass; full existing mirror-fetched posts were read.
The [Karpathy blog summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/), already saved
under `articles/karpathy.bearblog.dev/sequoia-ascent-2026`, identifies itself as AI-generated
and author-reviewed. The transcript is stronger for attribution; neither supports attributing
the pasted hierarchy to him.

### Testing and tool primary sources

| Key | Author/date; URL | Saved directory and locator |
|---|---|---|
| T1 | Cucumber maintainers, living: [BDD](https://cucumber.io/docs/bdd/) | `articles/cucumber.io/docs-bdd`; discovery, formulation, automation; primary methodology description |
| T2 | Ham Vocke, 2018-02-26: [practical pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) | `articles/martinfowler.com/articles-practical-test-pyramid-html`; Acceptance Tests / Avoid Test Duplication; principles used, historical tool snippets not adopted |
| T3 | Kent C. Dodds, 2021-06-03: [classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) | `articles/kentcdodds.com/blog-the-testing-trophy-and-testing-classifications`; scope and return on investment; original proponent |
| T4 | ESLint maintainers, living: [syntax restrictions](https://eslint.org/docs/latest/rules/no-restricted-syntax) | `articles/eslint.org/docs-latest-rules-no-restricted-syntax`; selectors/custom messages; official rule reference |
| T5 | ESLint maintainers, living: [custom rule tutorial](https://eslint.org/docs/latest/extend/custom-rule-tutorial) | `articles/eslint.org/docs-latest-extend-custom-rule-tutorial`; RuleTester valid/invalid cases; official implementation guide |
| T6 | Stylelint maintainers, living: [allowed values](https://stylelint.io/user-guide/rules/declaration-property-value-allowed-list/) | `articles/stylelint.io/user-guide-rules-declaration-property-value-allowed-list`; whole-value matching caveat; official rule reference |
| T7 | Stylelint maintainers, living: [allowed token names](https://stylelint.io/user-guide/rules/declaration-property-custom-property-allowed-list/) | `articles/stylelint.io/user-guide-rules-declaration-property-custom-property-allowed-list`; property-specific names; official rule reference |
| T8 | Atlassian design system, living: [token rule](https://atlassian.design/components/eslint-plugin-design-system/ensure-design-token-usage/usage) | `articles/atlassian.design/components-eslint-plugin-design-system-ensure-design-token-usage-usage`; examples/options; vendor's own supported token API |
| T9 | Microsoft/Playwright, living: [practices](https://playwright.dev/docs/best-practices) | `articles/playwright.dev/docs-best-practices`; isolation, visible behavior, assertions, traces; official guide |
| T10 | Microsoft/Playwright, living: [screenshots](https://playwright.dev/docs/test-snapshots) | `articles/playwright.dev/docs-test-snapshots`; environment dependence and updates; official guide |
| T11 | Microsoft/Playwright, living: [accessibility](https://playwright.dev/docs/accessibility-testing) | `articles/playwright.dev/docs-accessibility-testing`; current state, manual assessment and exclusions; official axe integration guide |
| T12 | W3C WAI, living: [evaluation](https://www.w3.org/WAI/test-evaluate/) | `articles/w3.org/wai-test-evaluate`; tools and user involvement; standards body's evaluation guidance |
| T13 | Lighthouse CI maintainers, living: [configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) | `articles/googlechrome.github.io/lighthouse-ci-docs-configuration-html`; assert.level / aggregationMethod / numberOfRuns; official configuration reference |
| T14 | Philip Walton / web.dev, initially 2020-05-04, updated living article: [Web Vitals](https://web.dev/articles/vitals) | `articles/web.dev/articles-vitals`; field versus lab; primary Google guidance |
| T15 | Stryker maintainers, living: [mutation testing](https://stryker-mutator.io/docs/) | `articles/stryker-mutator.io/docs`; mutants and surviving tests; official tool explanation |
| T16 | GOV.UK Service Manual, living; metadata date 2019-03-06, body undated: [accessibility testing](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility) | `articles/gov.uk/service-manual-helping-people-to-use-your-service-testing-for-accessibility`; automated/manual/user testing; practical government service guidance, not universal legal advice |

Context7 was also used to check current ESLint, Stylelint and Playwright documentation.
Saved reference text is preferred for traceability; extraction may lose code/table formatting.
Tool snippets were not installed or executed in a production app in this task.

## Recommendation and implementation

The owner's follow-up emphasized portability. Current OpenAI documentation confirms native
`/goal` in Codex CLI/IDE/desktop; local CLI 0.169.0 reports `goals stable true`. No duplicate
`goal` skill is needed. Shared task criteria and verification are portable; native lifecycle,
evaluation and budget controls must be checked per harness. Sources: OpenAI's living
[long-running-work guide](https://learn.chatgpt.com/docs/long-running-work), saved in
`articles/learn.chatgpt.com/docs-long-running-work-md/article.md` (Start a goal / Define what
done means), and [command reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli),
already saved in `articles/learn.chatgpt.com/docs-developer-commands-md-b96a28/article.md`
(Set or view a task goal). Both are official, checked 2026-11-15. Feature detection is not
proof of a full goal lifecycle run. `docs/loops.md` now separates harness behavior.

Extend existing skills and task templates, with the detailed tool guide loaded only for
relevant work. Keep core project instructions short. Task 1 implements this; the
[tracker](../../tasks/README.md) holds the real-project and evaluation follow-ups. No fixed
model, additional hook, paid service or cross-project control system is adopted.

What would change the recommendation: a held-out comparison showing equal defect detection
with less planning, or excessive irrelevant tool suggestions. Then remove or narrow the
guidance. A successful planning smoke test is weaker evidence than improved product outcomes.

## Coverage and validation limits

This audit covers the named page titles and relevant saved evidence, not all thousands of
corpus items, every staff member's posts, or every Office Hours episode. The exact context/spec
reply and community hierarchy remain unverified. No source text was treated as instructions.
Baseline repository checks passed (all 10). Final implementation evidence is recorded in
`docs/evidence/1-verification-before-implementation/multi-harness.md`; no claim of optimal test ratios follows
from this research.

Fifteen primary references were newly saved, including the later Codex clarification.
`tools/refs index` and `tools/refs watch` were run. Watch reported eleven new/changed discovery
items across its feeds; they are not additional read evidence for this audit, and the baseline
was not marked. Source manifest: `sources/verification-workflow-2026-11-15.txt`.
