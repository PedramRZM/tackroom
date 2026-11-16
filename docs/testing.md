# Testing and performance

What the sources say about what to test, how to get a model to write tests worth having, and
how to test performance; and where each piece lives in the template. The skills that carry this
into a project are `write-tests`, `verify`, `performance` and `lock-tests`.

The original synthesis used the saved practitioner notes and Kent C. Dodds's testing articles.
The [2026-11-15 audit](../refs/notes/2026-11-15-verification-workflow-audit.md) adds primary
testing/tool documentation and carries the earlier BDD research into the template. Backend
performance and random-input testing still rest on few first-hand reports, as marked below.

## Which tests, at which level

**Start with types and lint, choose the smallest boundary that proves each behavior, and keep
a few end-to-end journeys to check the assembled product.** Integration-heavy is a useful web
application default, not a percentage target for every project; a parser or algorithm library
can reasonably need far more unit/property tests.

- Kent C. Dodds's Testing Trophy has four layers, cheapest first: static (types, lint), unit,
  integration, end to end. His rule is "Write tests. Not too many. Mostly integration.": the
  higher the level, the more confidence each test buys, and the more it costs in speed and
  reliability, so integration is where most of the value sits
  ([`refs/articles/kentcdodds.com/blog-write-tests/article.md`](https://kentcdodds.com/blog/write-tests);
  `blog-the-testing-trophy-and-testing-classifications`).
- He is against coverage targets: mandated 100% gives "diminishing returns" and produces tests
  that say little about whether the application works (same post, "Not too many."). An agent
  asked for full coverage did exactly that in one team's account: it "wrote trivial tests"
  (`refs/notes/devcon-2-harness-specs-verification.md` (c), Cormack).
- For agents specifically, Dodds orders what helps them ship quality: "unit and integration
  test suites, typecheck, agents running their own change, a control CLI to drive the app,
  end-to-end tests, and decision records"
  ([`refs/articles/raw.githubusercontent.com/kentcdodds-kcd-skills-main-skills-autopilot-references-verification-md/article.md`](https://raw.githubusercontent.com/kentcdodds/kcd-skills/main/skills/autopilot/references/verification.md)).
- Addy Osmani, from inside the Claude Code team: if you could have only one kind, end-to-end
  tests on a small set of important flows, with failure output that says which step failed
  ([`refs/articles/addyo.substack.com/p-agentic-verification/article.md`](https://addyo.substack.com/p/agentic-verification), via
  `refs/notes/people-osmani-karpathy-willison.md`).

These are compatible: Dodds's "integration" for a web app is a page or handler tested with only
the outside world replaced, and both keep the end-to-end set small.

One dissent is on record: OpenAI's Ryan Lopopolo requires 100% coverage, as a device that
forces small, typed, decomposed code and not as proof of correctness
(`refs/notes/devcon-2-harness-specs-verification.md` (c)).

## Getting a model to write tests worth having

The failure the sources keep reporting is not that agents skip tests. It is that they write
tests that cannot fail, and adjust tests until they pass.

| Do | Why | Where in the template |
|---|---|---|
| Write the test from the behaviour (the acceptance criterion, the bug report), not from the code | A test derived from the code only confirms that the code does what it does (Farley, [`refs/videos/libNzUdL9eM/transcript.md`](https://www.youtube.com/watch?v=libNzUdL9eM), 05:09) | `write-tests`; task format in `WORKFLOW.md` |
| For a bug, failing test first; for new code, break the change and watch the test go red | A test that has never failed proves nothing. Osmani's verifier reverts the fix to check (`refs/notes/people-osmani-karpathy-willison.md`, finding 2) | `write-tests`; `WORKFLOW.md` step 6; the reviewer checks it |
| Protect existing tests while the code is being fixed | Anthropic's playbook: commit the failing test, then block test edits with a hook (`refs/notes/anthropic-claude-com-org-and-cases.md`, finding 6) | `/lock-tests` |
| When an expectation changes with the code, say why | Dodds has reviewers check every changed test expectation against the pull request's intent (verification reference, "Proof in the ship loop") | pull request template; `reviewer` |
| Keep tests fast, deterministic and quiet | Slow or flaky tests teach the agent to retry instead of fix (Osmani, same post) | `write-tests`; `scripts/agent/check` prints one line per check |
| Treat a flaky test as a bug | Agents treat flakiness as normal and will flip code back and forth chasing it (Cormack, [`refs/videos/xHxfeWtkXrM/transcript.md`](https://www.youtube.com/watch?v=xHxfeWtkXrM), 13:28) | `write-tests` |
| Do not accept tests as the only proof | Tests pass while the wrong thing ships; they cannot judge security or design (`refs/notes/devcon-2-harness-specs-verification.md` (c)) | `verify` asks for the running app; `second-opinion` |

What stays the human's: deciding which behaviours matter enough to test, and reading the
evidence. Simon Willison's line for it: "the one thing you absolutely cannot outsource to the
machine is testing that the code actually works"
([`refs/articles/simonwillison.net/2025-mar-11-using-llms-for-code/article.md`](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)).

## Random-input testing: properties, fuzzing, differential tests

You asked about "gorilla" testing. Nothing in the corpus uses that name. What the sources do
cover is the family it belongs to: tests that throw generated inputs at the code.

- **Property-based tests.** Osmani: "Example tests say what should happen; properties say what
  must not." Four families: a round trip, an invariant, idempotency, and equivalence of two
  implementations. Tools he names: fast-check (TypeScript), Hypothesis (Python), proptest
  (Rust). His advice is to ask the agent for properties, not examples.
- **Differential tests** for rewrites and migrations: run old and new on the same generated or
  replayed inputs and compare, keeping a list of approved intentional differences.
- **Fuzzing.** In one team's Rust storage project, fuzz and property tests found real issues
  that example tests had not, and their habit after each bug was to ask what kind of test would
  have caught it (`refs/notes/devcon-2-harness-specs-verification.md`, Cormack entry). Thariq
  Shihipar's post on effort levels reports that at high effort the model, unprompted, wrote
  randomised tests against a reference implementation and fuzzed
  (`refs/notes/anthropic-claude-dev-blog.md`, EFFORT entry; the wording is the notes' summary).

Evidence here is thin: a handful of first-hand reports, no measurements. The `write-tests`
skill mentions properties for code with invariants and stops there. Random UI-clicking
("monkey" testing) does not appear in the corpus at all.

## End-to-end and what the agent can see

The Claude Code team's most repeated tip is to give the agent a way to check its own work end
to end, which for a web app means driving a browser
(`refs/notes/x-posts.md`, finding 1; [`refs/posts/x/2044847858634064115/post.md`](https://x.com/bcherny/status/2044847858634064115)). The pieces
the sources describe:

- A way to **start the app and reach it**, to **sign in as a seed user**, and to **seed the
  data** a check needs. Dodds puts these in one project command-line tool with a skill that
  points at it, and adds a generated map of routes with notes on how to reach each feature
  (verification reference, "The model" and "Feature Map"). Osmani describes the same idea as a
  feature map.
- **Evidence in the pull request**: the commands run and their results, and a recording when
  the interface changed.
- **Production-like checks only when needed**: a preview deployment for migrations, real
  OAuth, webhooks and platform bindings; everything else locally.

The template's `verify` skill asks for this evidence and has a "This project" section for the
start, sign-in, seed and reach notes. It does not ship a control tool: that is project code,
and the sources that have one built it for one product.

## Performance

The method comes from one strong first-hand account, Anthropic's two-week effort that made
claude.ai about three times faster ([`refs/articles/claude.dev/blog-how-we-made-claude-ai-faster/article.md`](https://claude.dev/blog/how-we-made-claude-ai-faster/),
summarised in `refs/notes/anthropic-claude-dev-blog.md`, FAST entry), plus the Claude Code
docs and Boris Cherny's own prompts:

1. **Measure first.** "With Claude, measuring something makes it tractable."
2. **Prefer deterministic metrics** (instruction counts, renders, style recalculations, layout
   shifts by region) over wall-clock time, for both the working loop and the gate.
3. **Make each benchmark prove it tracks the real outcome**, or throw it out.
4. **Pin behaviour first**: in their work unit tests always came before optimisations, and
   anything a user could notice shipped behind a short-lived flag.
5. **Prove a fix with repeated runs**: red 20 of 20 before, green 20 of 20 after.
6. **Ratchet**: every benchmark is also a CI guard that can only move in the good direction.
7. **Stop at diminishing returns**: they rejected a 900-line change that saved 2 ms.
8. **The human supplies ambition, taste and direction**: by default the model is careful
   about scope and pads its estimates.

In the template: the `performance` skill carries the loop, and `scripts/agent/ratchet <name>
<value>` is the guard. Call it from `scripts/agent/check` with whatever number the project
cares about; it fails when the number is worse than the recorded best.

### Client side

- The docs' own examples state a measurable target: "get the bundle size under 200KB and show
  me what you removed", and `/goal get the homepage Lighthouse score to 90 or above, stop after
  5 tries.` (both in `prompts/README.md`).
- The Claude Code team's sample verification skill ends with a performance trace and a Core
  Web Vitals audit through the Chrome DevTools tool
  ([`refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`](https://claude.com/resources/articles/getting-started-with-loops)).
- Lab numbers are for before-and-after on one machine. They are not what users experience; the
  claude.ai work reported its outcome as the 75th-percentile time until the page could be typed in.

Setting it up in a web project: one script that builds, measures what you care about (bundle
bytes per route, a Lighthouse run against a fixed page, a count of requests) and calls
`ratchet` for each. Add it to `scripts/agent/check` as a `full` step so the quick run stays fast.

### Server side

The corpus is thin here, and I am saying so instead of padding. What it does support:

- Cherny's prompt for a speed rewrite makes the **original test suite the oracle** and the
  stop condition **proof**: "dont stop until you have conclusively proven that the new impl is
  faster", followed by a target, "hoping for p99 < 10ms" ([`refs/posts/x/2042352725481177315/post.md`](https://x.com/bcherny/status/2042352725481177315)).
- Agents propose plausible but unverified optimisations
  (`refs/notes/devcon-2-harness-specs-verification.md` (c), Walter), which is the reason for
  measuring before and after.

The rest is my inference from the client-side method, not from a source: fix the dataset,
count queries per request and guard the count with `ratchet`, read the query plan of the slow
ones, benchmark with repeated runs, and load-test only when concurrency is the question.

## What was added to the template for this

- `write-tests` skill: levels, how to write a test that can fail, what not to do.
- `performance` skill: the measure, change, prove, guard loop.
- `scripts/agent/ratchet`: a number that can only get better.
- Pull request template: say why any existing test's expectation changed.
- `verify` skill: what to record so an agent can drive the real app.

These do not yet have a comparative outcome eval. The 2026-11-15 scratch exercise checks that
the revised guidance can be followed; it cannot establish improved defect detection or cost.
Per `docs/principles.md` (6 and 12), try each on real work and delete guidance that adds no value.

## Verification before implementation

The missing connection was a pre-code verification plan, rather than another testing tool.

The [2026-11-16 cross-harness trial](evidence/1-verification-before-implementation/multi-harness.md)
found that OpenCode read the shared guidance but omitted required checks. A five-line omission
reminder did not resolve the failures in a fresh run and was removed. Codex's planning runs
passed; Claude's account restriction prevented a response. These are planning observations,
not evidence of universal compliance or a controlled usefulness comparison.
The workflow now asks the implementer to record a compact mapping in the task or existing plan:

**criterion/example → expected result and its source → risk → smallest sufficient check/tool
→ data/environment → command or UI steps → evidence.**

BDD supplies shared examples, TDD supplies the red/green/refactor loop, and unit/integration/E2E
describe the boundary exercised. They are complementary. Cucumber's definition separates
discovery, formulation and automation; it does not mean every example needs a browser test.
Our choice to keep examples in ordinary task text unless collaborators maintain Gherkin is a
judgment call. [Saved BDD source](../refs/articles/cucumber.io/docs-bdd/meta.json),
[prior research](../refs/notes/2026-11-13-claude-team-bdd-e2e.md).

For substantive behavior, write a focused failing example before implementation and confirm
the reason for failure. For trivial edits, reuse existing checks and direct inspection. Move
exhaustive edge cases to cheap tests; use a small integrated journey set to prove wiring.
Neither the pyramid nor the trophy establishes a universal optimum. The portable synthesis
and worked invoice example are in
[`write-tests/references/verification-tools.md`](../template/.agents/skills/write-tests/references/verification-tools.md).
Sources: [Vocke's practical pyramid](https://martinfowler.com/articles/practical-test-pyramid.html),
[Dodds's classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications).

## Recommend quality tools for the actual project

The agent now inspects the installed stack, explains existing coverage and recommends only
checks for uncovered risks, with setup/runtime cost and blind spots. Repeated mechanical
review findings belong in tested compiler/lint rules where feasible. This is a selection
procedure, not a dependency bundle.

| Need | Candidate | Necessary qualification |
|---|---|---|
| JS/TS syntax and structural constraints | ESLint built-in or scoped AST rule | Test custom rules with valid/invalid fixtures; a style rule does not prove product behavior |
| CSS design-token usage | Stylelint property-value and custom-property allowlists | Match the real syntax and approved names; excluding hex or checking variable names alone is insufficient |
| CSS-in-JS or utility tokens | Existing design-system rule or tested syntax-aware check | Atlassian's rule targets its API; CSS lint does not cover arbitrary JS/class strings |
| UI behavior | Existing component runner and critical Playwright journeys | DOM assertions cannot establish layout; browser exploration does not create a durable suite |
| Visual regression | Playwright screenshots or an existing Storybook visual workflow | Stable environment and reviewed baselines; detects differences, not design quality |
| Accessibility | axe-core plus manual interaction/assistive-technology checks | A clean automated scan is incomplete evidence |
| Performance | Existing budgets, Lighthouse CI, field Web Vitals | Lab regressions and user experience are different measurements |
| Weak assertions | Manual negative control or targeted Stryker run | Mutation adds cost and cannot establish that the requirements are right |

For the token example, first prove that valid semantic usage passes and raw hex, named/function
colors and wrong token namespaces fail in each supported style surface. Token definitions,
generated/vendor files and approved exceptions need explicit scope. This fixture matrix is
our judgment, grounded in how the documented rules work—not a claim that a single rule covers
all frontends. Full primary URLs, saved paths, dates and locators are in the
[audit source register](../refs/notes/2026-11-15-verification-workflow-audit.md).

## Product evidence is more than a green suite

The `verify` skill separates behavior, visuals, accessibility, usability and performance.
Record the tested revision/environment, roles/data, output and relevant artifacts. Report
skips and flaky retries. Test expectations, screenshot baselines and gate configuration changes
need reasons tied to the requested behavior. Review evidence again after further edits.

Playwright documents both screenshot environment sensitivity and the limits of automated
accessibility testing. W3C recommends combined human and automated evaluation; observing real
users is necessary for claims about their experience. An agent review can identify likely UX
problems but is not user research. [Visual comparisons](https://playwright.dev/docs/test-snapshots),
[accessibility tests](https://playwright.dev/docs/accessibility-testing),
[W3C evaluation](https://www.w3.org/WAI/test-evaluate/).

Trusted enforcement remains separate: hooks in a writable workspace and a second model are
feedback mechanisms, not an unchangeable acceptance gate. The project's own CI/verifier must
run reviewed checks when that assurance is needed. The [follow-up tasks](../tasks/README.md)
cover the real-app setup pilot and a comparative eval; no application-specific lint or browser
suite is claimed to have been installed by this portable template change.
