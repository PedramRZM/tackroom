# Kent C. Dodds: testing, and working with agents

Sources saved: 21 (collection `people-kentcdodds`). Read in full: the X post, "You Own the
Outcome", and from his `kcd-skills` repository the autopilot skill, its verification reference
and the `review-and-recommend` and `friction-log` skills. Read in part: "Write tests. Not too
many. Mostly integration.", "The Testing Trophy and Testing Classifications", the autopilot
templates (agent index, pull request template, decision record), and his talks page (the
"Closing the Agentic Loop" workshop description only). Saved and not read: "AHA Testing",
"Avoid Nesting when you're Testing", "Common mistakes with React Testing Library", "Static vs
Unit vs Integration vs E2E Tests", "Testing Implementation Details", "How I used Cursor to
migrate frameworks", the `ship-pr` and `visual-recap` skills, the setup-PR reference and the
repository README. Nothing was run from his repository; `npx kcd-skills` was not executed.

## Cross-cutting findings

1. Agents produce output; the person owns the outcome. The human work is deciding what should
   exist, designing the building blocks, and watching results. (OUTCOME, "Output vs outcome",
   "What the human work actually is")
2. Before asking for work: shared understanding first, then options with effort, trade-offs, a
   one-way or two-way door label and a recommendation; the person makes the call. (OUTCOME,
   "First, build shared understanding", "Then, ask for options instead of an answer"; REVIEW skill)
3. A repository is ready for agents when it has a short agent map, one verify command that is
   the same locally and in CI, written decisions including the "no", a way for agents to run
   their own change, and a pull request template built on intent, door, testing and risk.
   (AUTOPILOT, "Principles" and "Rungs")
4. Order of what helps agents ship quality: "unit and integration test suites, typecheck,
   agents running their own change, a control CLI to drive the app, end-to-end tests, and
   decision records". (VERIFICATION, opening)
5. Verification runs through one project command-line tool the agents maintain: check the
   environment, start the app, sign in as a seed user, make authenticated requests, run
   fixtures, drive a browser with a recording, check the deployed version. Local first; a
   preview deployment only for production-like changes. (VERIFICATION, "The model", "Local
   first")
6. Reviewers check every changed test expectation against the pull request's intent; a change
   to an assertion alongside the code it tests must be explained. (VERIFICATION, "Proof in the
   ship loop")
7. Risk decides who reviews: low needs green CI, medium adds an AI reviewer and proof, high adds
   the human. One-way doors and product calls always go to the human. (AUTOPILOT, "Interview")
8. Limit the blast radius: flags with an owner, a metric and a removal condition; a rollback
   runbook; backups with a tested restore. (AUTOPILOT, rungs 8 and 9)
9. Agents file friction after every pull request, with a priority, and other agents fix it.
   (AUTOPILOT, principle 9; FRICTION skill)
10. Testing: "Write tests. Not too many. Mostly integration."; four levels (static, unit,
    integration, end to end); mandated 100% coverage has "diminishing returns". (WRITE-TESTS,
    TROPHY)
11. "Keep skills small." and an agent file that is "a router, not a novel". (OUTCOME, "How to be
    a good collaborator for agents"; talks page, workshop description)
12. "Which framework you pick matters less than it used to." (OUTCOME, "Watch the outcomes")

Contradictions and open questions: he reports not reading 1% of his product's code and letting
agents author and merge most pull requests (talks page, workshop description). That goes
further than Anthropic's customer guidance, which keeps a human approver
(`anthropic-claude-com-org-and-cases.md`). His numbers are his own report about one product.

## Per source

### Prompt on implicit state machines (X post, 2026-11-09) [POST]
File: posts/x/2119812466037428392/post.md   URL: https://x.com/kentcdodds/status/2119812466037428392
Thesis: a prompt he adjusted from one he traces to Steve Ruiz; quotes David Khourshid on why
scattered state logic lets tests pass while illegal states remain possible.
Relevance: high. The prompt is in `prompts/README.md`.

### You Own the Outcome: Product Engineering in the Age of AI (2026-09-24) [OUTCOME]
File: [articles/kentcdodds.com/blog-you-own-the-outcome/article.md](https://kentcdodds.com/blog/you-own-the-outcome)
Thesis: with agents producing the code, the valuable work is judgment about outcomes. Shows a
feature shipped live without him writing or reading the implementation.
Practices: findings 1, 2, 11, 12; "Isolate secrets": agents use credentials without seeing them.
Evidence and numbers: one live-shipped feature (kody#2594). First-hand, single case.
Relevance: high.

### kcd-skills: autopilot skill and references (repository, pushed 2026-11-07, MIT) [AUTOPILOT, VERIFICATION, REVIEW, FRICTION]
Files: [articles/raw.githubusercontent.com/kentcdodds-kcd-skills-main-skills-autopilot-skill-md/article.md](https://raw.githubusercontent.com/kentcdodds/kcd-skills/main/skills/autopilot/SKILL.md),
...-autopilot-references-verification-md, ...-autopilot-references-templates-md,
...-skills-review-and-recommend-skill-md, ...-skills-friction-log-skill-md
Thesis: a ladder of thirteen rungs for making any repository safe for agents to ship in, with an
audit, an interview, a plan and one setup pull request.
Practices: findings 3 to 9.
Tools and files named: `kcd-skills` (npm), Kody, `control-<project>` CLI, Feature Map.
Caveats: built around his own product and tooling (Kody); the scripts were not read or run.
Relevance: high. The closest thing in the corpus to a complete, current, solo-developer setup.

### Testing articles (2019 to 2021) [WRITE-TESTS, TROPHY]
Files: [articles/kentcdodds.com/blog-write-tests/article.md](https://kentcdodds.com/blog/write-tests),
[articles/kentcdodds.com/blog-the-testing-trophy-and-testing-classifications/article.md](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
Thesis: finding 10. Written before coding agents; still the reference for which level to test at.
Relevance: high for test strategy; read in part only.
