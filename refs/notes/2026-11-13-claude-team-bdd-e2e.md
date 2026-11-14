# Claude team testing, BDD and browser verification

Research date: 2026-11-13. Scope: testing evidence for a human-supervised, board-driven
development harness. Research and proposals only; no production access or template changes.

## Questions

1. What testing practices are directly reported by Anthropic staff or visible in their public
   projects, and what is merely general official advice?
2. Is there primary evidence that the Claude team uses BDD, Gherkin or Cucumber, rather than
   behavior-based acceptance criteria and end-to-end browser testing?
3. What does tackroom already provide, and what remains missing for isolated task environments,
   preview verification, screenshots, videos and human approval?
4. How can acceptance tests and independent checks resist an implementer weakening its own
   definition of success?

## Findings: what is actually evidenced

**No primary evidence located that the Claude Code team standardizes on Cucumber,
Gherkin, or a named BDD framework.** Searches of the existing Anthropic material and
the sources below establish behavior verification, test-driven bug fixing, E2E checks,
and independent review. That is not enough to infer a company-wide BDD framework.
This is a bounded research result, not a claim that nobody at Anthropic uses one.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Claude Code team's October review article [A1] | Before PR: runnable verification, fresh-context review, internal bug-finding/simplification/E2E skills. Blocking lint/types/tests/build, risk-scaled human approval, merge queue, staged rollout and rollback | Public source for all internal skills, a standard BDD runner, or identical practice across every Anthropic team |
| Sachin Malhotra's CI account [A2] | Deterministic test selection using package relevance and test-result history; stale selection can miss new/fixed tests or run known flaky tests | A reason for a small project to build Anthropic-scale test selection |
| Jason Clinton's security engineering account [A6] | Narrow automated reviewers, deterministic SAST, invariant tests such as cross-user data isolation, and dynamic security testing in staging | Proof that agent reviewers have no shared blind spots, or that automated approval is appropriate for this pilot |
| Applied AI SDLC playbook [A3] | Runnable acceptance criteria, failing regression test first and protecting tests from agent edits | Purely first-person reporting of the Claude Code team's process; the playbook mixes internal and customer advice |
| Lydia Hallie's talk [A4] | Per-task tests and completion hooks, separate validation agents, orchestrator/implementer separation | A formal Cucumber/Gherkin workflow |
| Anthropic's public `webapp-testing` skill [A5] | Python Playwright scripts, server lifecycle helper, rendered-page inspection, screenshots and console inspection | Their complete internal E2E suite, or proof every team uses Python for browser tests |
| Playwright's official test agents [P1] | Planner explores the app, generator turns a plan into tests, healer attempts repairs | An independent correctness oracle: the healer can output a skipped test when it believes functionality is broken |

The public Anthropic webapp skill recommends `networkidle` and even fixed waits.
Playwright's best-practices guide instead emphasizes role-based locators, auto-waiting
and retrying assertions. **Recommendation:** use explicit readiness and user-visible
assertions in durable tests; do not copy every line of the public skill into our test
standard. Treat it as a useful server/browser workflow example. [A5, P2]

## BDD in this system

Cucumber describes BDD as collaborative discovery, formulation of concrete examples,
and automation. It is broader than the tool. The user's supervised scoping stage is
a good place for that collaboration. **Inference:** start with short Given/When/Then
examples in the issue, then implement them as ordinary Playwright Test and integration
tests. Add a Gherkin runner only if humans will actively maintain `.feature` files;
otherwise it adds another representation to keep synchronized. [B1]

An illustrative acceptance example, to be approved during scope:

> Given a member can see an invoice but cannot approve payments, when they open the
> invoice, they can download it and cannot approve payment, including through a direct
> API request.

The visible behavior needs a browser check; the direct API prohibition needs an
authorization integration test. A screenshot alone cannot establish the latter.
For bugs, reproduce the failure against the old revision and show that the same test
passes after the fix. For new behavior, agree on expected examples before implementation.

## Proposed verification contract (judgment call)

1. **Scope:** record current behavior, expected behavior, affected roles, examples,
   non-goals and edge cases. Map each criterion to its checking method. Freeze a scope
   revision; an agent cannot quietly redefine it after discovering implementation costs.
2. **Fast checks:** type/lint/build plus relevant unit and integration tests. Put business
   rules, authorization, DB constraints, migration compatibility, retries and idempotency
   here when a browser adds little value. Keep a small set of critical E2E journeys.
3. **Stable browser suite:** use Playwright Test for repeatable journeys. Pin browser
   and dependency versions, deterministic data, roles, and locale/time where relevant.
   Use user-facing locators and retrying assertions. A task's database is isolated;
   parallel mutating tests also need separate users/data within that task. Playwright's
   auth guide explicitly recommends one account per parallel worker for shared-state
   mutations. [P2, P3]
4. **Deployed preview:** after the feature branch deployment succeeds, verify its exact
   deployment ID, source commit, health and migrated seed data before testing. Test
   production-build behavior there, including redirects, auth callbacks and webhook
   integrations in provider test mode. A passing local dev-server test does not replace
   this stage. Mocks are appropriate for uncontrolled third parties in deterministic
   tests; retain a few real test-mode integration checks for boundaries that matter.
5. **Fresh user-perspective review:** give a separate agent the approved criteria,
   roles and preview URL, without the implementer's success narrative. Have it attempt
   the task, exercise failure/empty/permission states, inspect console/network errors,
   and report reproducible blockers. Add visual/accessibility review where relevant.
   A second model may reduce some shared errors but does not guarantee independence.
6. **Evidence and human review:** attach criterion-to-test mapping, command exit results,
   skipped/flaky counts, test changes, exact SHA/deployment, screenshots and a short
   successful-journey video. Preserve failure traces and Playwright HTML reports. A
   fresh commit invalidates the old evidence and ship approval. Then wait for the human.

For review videos, explicitly record the selected acceptance journey even when it passes.
`retain-on-failure` alone would discard the success video the user wants. Use failure
screenshots and trace-on-first-retry for the ordinary suite to keep cost manageable;
Playwright recommends traces for CI diagnosis because they retain DOM/network context.
Do not record every full suite run indefinitely. Suggested pilot retention: 14 days
for bulky artifacts, longer for the small evidence manifest and approved release record.
Authenticated browser state is sensitive: never commit it or put it in a public artifact.
[P2, P3, P4]

### Prevent passing by weakening the test

Protected CI evaluates the approved criteria/test baseline from a trusted revision.
Builder changes to acceptance tests, fixtures, test selection, CI or skip markers are
visible and require separate review. Test locks inside the writable workspace are only
one defense; a worker with shell access can bypass an advisory convention. The release
gate must not rely solely on checks that the same worker can rewrite.

Use the Playwright planner and generator when they reduce work. Limit a healer to
proposed repairs: changing selectors or fixtures may be valid, but skipping a required
scenario, deleting an assertion or substituting a mock for required live behavior does
not satisfy acceptance. A retry-green result stays marked flaky. Record the original
failure, cap repair rounds, and escalate after three rounds or a task budget limit.
The three-round starting point is informed by the Claude Code review team's convergence
policy; it remains a pilot choice for browser repair. [A1, P1]

### What is new relative to tackroom

`docs/testing.md`, `/write-tests`, `/lock-tests`, `/verify`, `/verify-ui` and the independent
review agents already provide much of the reasoning. The missing operational pieces are:

- A concrete, project-specific startup/seed/login/health contract replacing placeholders.
- Approved behavior examples with test ownership and criterion-to-evidence mapping.
- A trusted preview verifier keyed to an immutable deployment and commit.
- Separate test identities/data per task and parallel test worker.
- Durable artifact storage and review evidence, including a passing-journey video.
- External protection against weakening acceptance tests or approving one's own release.
- Measured flake, escaped-bug, reviewer-noise and rework feedback for the dream loop.

Start with one real bug, its regression test and one critical user journey. Do not
generate a huge E2E suite or add multiple agent personas before that loop is reliable.

## Source register and limits

Existing Anthropic synthesis notes were used as an index, with A1's verification/review
sections, A2's complete article, A4's earlier transcript audit, and A5's full skill checked.
P1 and B1 were read in full. P2/P3/P4 are living reference docs; the cited sections were
checked, not a complete audit of the Playwright documentation. No browser suite was run
against an Anthropic internal project or a deployed user application.

| Key | Author/date and URL | Saved file and locator |
|---|---|---|
| A1 | Addy Osmani, Morgan Westlee Lunt, Qing Wang, 2026-10-15, [team review](https://claude.dev/blog/solving-code-review-at-anthropic/) | `refs/articles/claude.dev/blog-solving-code-review-at-anthropic/article.md`; Layer by layer, How we make the reviewer better |
| A2 | Sachin Malhotra, 2026-09-14, [test impact analysis](https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic) | `refs/articles/claude.com/resources-articles-agentic-coding-is-straining-ci-heres-how-we-scaled-test-impac/article.md`; architecture and redesign |
| A3 | Louis Claxton, 2026-08-21, [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) | `refs/articles/claude.com/resources-articles-the-ai-native-sdlc-playbook/article.md`; feedback loop/testing, existing full review in `anthropic-claude-com-org-and-cases.md` |
| A4 | Lydia Hallie/Anthropic, publication date unavailable in saved metadata, [Claude Code talk](https://www.youtube.com/watch?v=vlfCjWuv4es) | `refs/videos/vlfCjWuv4es/transcript.md`; 11:12–13:14, 14:15, 15:16; see `2026-11-13-anthropic-staff-talks-articles.md` |
| A5 | Anthropic skills maintainers, undated moving `main`, [webapp-testing](https://raw.githubusercontent.com/anthropics/skills/main/skills/webapp-testing/SKILL.md) | `refs/articles/raw.githubusercontent.com/anthropics-skills-main-skills-webapp-testing-skill-md/article.md`; server helper and best practices; public implementation evidence |
| A6 | Jason Clinton, 2026-07-21, [security SDLC](https://claude.com/resources/articles/how-anthropic-secures-its-ai-native-software-development-lifecycle) | `refs/articles/claude.com/resources-articles-how-anthropic-secures-its-ai-native-software-development-life/article.md`; Test (CI), Deploy (CD); first-person security-team evidence, sections rechecked |
| P1 | Microsoft/Playwright maintainers, living docs, [test agents](https://playwright.dev/docs/test-agents) | `refs/articles/playwright.dev/docs-test-agents/article.md`; Planner, Generator, Healer |
| P2 | Same, [best practices](https://playwright.dev/docs/best-practices) | `refs/articles/playwright.dev/docs-best-practices/article.md`; user-visible behavior, isolation, assertions, CI debugging |
| P3 | Same, [authentication](https://playwright.dev/docs/auth) | `refs/articles/playwright.dev/docs-auth/article.md`; shared account versus account per worker; sensitive saved state |
| P4 | Same, [use options](https://playwright.dev/docs/test-use-options) | `refs/articles/playwright.dev/docs-test-use-options/article.md`; recording options |
| B1 | Cucumber maintainers, living docs, [BDD](https://cucumber.io/docs/bdd/) | `refs/articles/cucumber.io/docs-bdd/article.md`; three practices; primary definition rather than framework marketing |

Living docs checked 2026-11-13; extraction dates such as January 1 are not reliable
publication dates. This note recommends a workflow; it does not change current skills.
