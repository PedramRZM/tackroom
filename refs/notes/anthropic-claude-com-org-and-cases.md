# Anthropic on claude.com: how its own teams work, the AI-native SDLC, review, CI, security, and customer case studies

Sources read: 58 of 58, each in full. None could not be read. Six saved files are degraded and are
flagged in their entries: the startups guide (rule headings and checklist lost), the SDLC playbook
(stage table, dependency graph and resource list lost), the modernization article (type table
lost), the agents-guide executive summary (truncated mid-sentence), the scaling-guide landing page
(navigation only), and the Zero Trust article (a landing page for a guide that is not in this
batch). The nine scaling-guide pages carry a wrong date (2024-01-15); the guide dates itself to
August 2025. No text that looked like a prompt-injection attempt was found; the example prompts
inside the articles are illustrations and were not followed.

Dates run from 2025-07 to 2026-11. Where sources disagree, the later one usually reflects a more
automated practice and newer models; anything from 2025 should be treated as possibly superseded.

Source keys used below (full entries under "Per source"):
PLAYBOOK (AI-native SDLC playbook, 2026-08), ORG (Running an AI-native engineering org, 2026-06),
SEC-SDLC (How Anthropic secures its AI-native SDLC, 2026-07), CI-TIA (test impact analysis,
2026-09), ONCALL (Claude Tag CI on-call, 2026-08), MIGRATE (large-scale migrations, 2026-07),
MODERNIZE (preparing modernization projects, 2026-09), LLM-SEC (Using LLMs to secure source code,
2026-05), CR-PREVIEW (Code Review launch, 2026-03), CR-GA (Code Review GA, 2026-10), DESKTOP
(preview, review and merge, 2026-02), TEAMS (human-agent teams, 2026-06), TEAMS-2025 (How
Anthropic teams use Claude Code, 2025-07), PM-EXP (Product management on the AI exponential,
2026-03), PM-AGENTIC (Product development in the agentic era, 2026-04), METRICS (contribution
metrics, 2026-01), SECREV-2025 (Automate security reviews, 2025-08), STARTUPS (Claude Code guide
for startups, 2026-08), YC (three YC startups, 2025-11), BLOCK (2026-10), BREX (2025-10),
CODERABBIT (2026-05), CURATIVE (2026-11), DATADOG (2026-07), JETBRAINS (2026-08), WARP (2026-08),
CURSOR (2026-07), COGNITION (2026-07), BASE44 (2026-07), TRENDS (2026 trends report and teaser,
2026-01), AGENTS-GUIDE (Building effective AI agents, 2026-01), SCALE-2025 (scaling article,
2025-10), SCALE-GUIDE (scaling guide, 2025-08), CWC-SF and CWC-LDN (conference recaps, 2026-05),
ZT (Zero Trust landing page, 2026-05), BUGS (2025-10), INTRO (2025-10), BENEFITS (2025-12),
RESPIRO (2026-05).

## Cross-cutting findings

### Recurring practices

1. Verification, review and security are the constraint once agents write the code; spend there, not on more generation. ORG ("Verification, code review, and security took their place"), DATADOG ("Assume verification"), LLM-SEC, SEC-SDLC, MODERNIZE, PLAYBOOK, CR-PREVIEW.
2. Define done as a check the agent can run without a human: one command that exits non-zero, a quantified target, a parity diff, a "certificate". PLAYBOOK ("Give Claude a feedback loop"), MODERNIZE ("Step 2"), MIGRATE ("Prerequisites"), WARP (best-practices table), CI-TIA, TEAMS ("Lesson 4").
3. Final checks belong to a separate agent in a fresh context that is told to disprove, and that sees the artefact but not the author's reasoning. LLM-SEC ("4. Verification"), PLAYBOOK (verifier subagent), MIGRATE (two adversarial reviewers plus an arbiter), MODERNIZE (certificate list), TEAMS ("Doer-Verifier"), CWC-SF ("Outcomes"), CURATIVE (rate reviewer, message judge).
4. Fix the instructions or the loop, not the single output. Repeated mistakes go upstream into the rulebook, `CLAUDE.md`, a skill or the workflow. MIGRATE ("You fix the process (loop) that produced the code"), PLAYBOOK ("When Claude makes a mistake twice, the correction goes into `CLAUDE.md`"), SEC-SDLC ("Code"), STARTUPS ("fix the principle, not the example"), MODERNIZE ("Fix recurring flags at the source"), ONCALL (promotion from `lessons.md` to skill), WARP.
5. Agent instructions are short versioned files reviewed like code: `CLAUDE.md` under a page with commands, conventions, architecture and known mistakes; skills for knowledge that must be applied consistently; per-directory `CLAUDE.md` in large repos. PLAYBOOK, SEC-SDLC, BREX, ONCALL, WARP, SCALE-2025, SCALE-GUIDE.
6. Instructions and skills are advisory; anything that must always hold needs a deterministic layer (hook, branch protection, regex check, access boundary). PLAYBOOK ("The skill makes violations rare and the hook makes them close to impossible"), BLOCK ("Sometimes it's even a regex"), SEC-SDLC ("draw the boundary around access and actions, not around a model's instructions"), ONCALL (deterministic alerting).
7. Agent output arrives as a pull request; a human approves merge to main and production deploys. PLAYBOOK, BLOCK, CR-PREVIEW, ONCALL, STARTUPS, WARP, LLM-SEC, BASE44. SEC-SDLC is the exception (see contradictions).
8. Plan before code and make assumptions explicit; keep research, planning and implementation as separate steps or sessions. PLAYBOOK (`intent.md`, `spec.md`, `plan.md`), CODERABBIT, YC (Ambral), MIGRATE (rulebook and stress test first), MODERNIZE (target and certificate first). ORG and PM-EXP pull the other way for product work (see contradictions).
9. Tests first for bugs and for scoping, and the agent must not be able to weaken the test. PLAYBOOK (failing test committed first, hook blocks test edits), LLM-SEC ("6. Patching"), MIGRATE (adversarial check that rewritten tests are not weaker; judge validated on broken code), SCALE-2025, SCALE-GUIDE, TEAMS-2025, BUGS.
10. Route models by task: the strongest model plans, reviews and writes rules; cheaper models do high-volume edits; measure instead of guessing. MIGRATE, BLOCK, CODERABBIT, MODERNIZE, CURATIVE, YC, CURSOR, JETBRAINS, AGENTS-GUIDE.
11. Build a self-improvement loop: capture feedback where the work happens, have a scheduled agent turn it into a small edit to a skill or instruction file, and merge that edit through review. WARP, ONCALL (`lessons.md`), CURATIVE ("sample the last 10,000 runs"), STARTUPS (Cainex), TEAMS ("lessons & missteps"), SEC-SDLC, CWC-SF ("Dreaming").
12. Keep a private eval set of real tasks and re-run it when the model or the agent configuration changes; public benchmarks do not predict results on your code. PLAYBOOK ("Continuous evals in CI"), JETBRAINS, CURSOR, COGNITION, PM-EXP, STARTUPS, CODERABBIT, BASE44.
13. Grant autonomy by risk tier and by demonstrated reliability per task type, starting lower than seems necessary. SEC-SDLC (risk tiers, shadow mode), MODERNIZE ("Tier changes by blast radius and agent confidence"), TEAMS ("Lesson 4"), CURATIVE ("Less than you think it can handle"), PLAYBOOK (autonomy by environment), CR-GA (Quick/Standard/Deep per repository).
14. Contain blast radius with access boundaries: no credentials in reach, egress allowlists, remote or sandboxed execution, single-purpose identities. SEC-SDLC, LLM-SEC, BLOCK, PLAYBOOK, MODERNIZE, CWC-LDN.
15. Keep scaffolding simple and delete it when a new model makes it unnecessary; re-test guardrails at each model release. PM-EXP ("do the simple thing that works"), ORG ("Don't hesitate to kill processes that no longer work"), TEAMS ("Lesson 4"), STARTUPS (rebuilds), LLM-SEC (shorter prompts work better for discovery).
16. Parallel work is limited by how much one person can review, not by how many sessions can run. PLAYBOOK ("Two or three sessions is a sensible starting point"), TEAMS (caps on agent work per day), YC, TRENDS (0-20% of tasks fully delegated).
17. Several narrow reviewers beat one general reviewer, with a verification pass to remove false positives. SEC-SDLC ("Test (CI)"), CR-PREVIEW ("How it works"), STARTUPS (Translucent), LLM-SEC (partition, then fan out), AGENTS-GUIDE (parallel and voting patterns).
18. Control reviewer noise explicitly: define severities, cap nits, deduplicate, and make the model write its reasoning before a severity. PLAYBOOK (`REVIEW.md`), LLM-SEC ("5. Triage"), CR-GA, WARP (the "noisy experience" problem), TEAMS (batching questions).
19. Run scheduled maintenance agents: cleanup and consolidation passes, security scans, flag removal, run sampling. BLOCK, PLAYBOOK ("Recurring codebase scans"), CURATIVE, STARTUPS (Commure), LLM-SEC.
20. Write decisions and context down where agents can read them; documentation is now read mainly by agents. TEAMS ("Lesson 1"), BREX, TEAMS-2025, BLOCK, ONCALL.

### (a) How Anthropic's own engineering teams say they work day to day

Sources here are first-person Anthropic accounts: ORG (Claude Code team), SEC-SDLC (security),
CI-TIA and ONCALL (CI team), MIGRATE, TEAMS, PM-EXP, CR-PREVIEW, TEAMS-2025 (older). PLAYBOOK is
written by the Applied AI team and mixes internal and customer practice; it is cited only where it
adds a concrete detail and is marked.

1. Planning is just in time. The Claude Code team's six-month roadmap "was out of date by month three"; planning "shifted away from design docs toward discussions in PRs or prototypes", and the process is to prototype, put internal users on it and act on feedback. (ORG, "Planning: shift roadmaps to just in time")
2. Exploration happens as side quests and demos, not as documents. "Instead of hosting traditional stand-ups, we share demos of new ideas"; a spec is tested by sending it to Claude Code to build. (PM-EXP, "Plan in short sprints", "Encourage demos and evals over docs")
3. Security planning review is automated and risk-tiered: a project security review tool reads the design document; low-risk projects self-approve "if Claude deemed the launch low enough risk." Detailed architectural review is called "a less critical gate" because prototypes take hours. (SEC-SDLC, "Plan")
4. Context is gathered by asking Claude first, not the author, and every recurring question prompts "Is there a way to automate it?" (ORG, "Context gathering: ask Claude, not the author")
5. Every commit is Claude-assisted on the Claude Code team; across the company Claude authors about 80% of merged code and an internal Claude Tag merges more than half of it. (ORG, "How to know your new processes are sticking"; SEC-SDLC, introduction)
6. Engineers run several agents at once, and agents work overnight and at weekends. SEC-SDLC says the review bottleneck appeared "once most developers were using agentic coding tools and running multiple agents at one time"; CI-TIA says "agents push overnight and on weekends" and that Claude "prefers smaller, more granular PRs". No article in this batch gives a number of parallel sessions per Anthropic engineer. PLAYBOOK (Applied AI, not a team account) recommends two or three sessions in separate worktrees, limited by review capacity.
7. Large jobs are run as loops, not as conversations: implement, review and fix with adversarial reviewers in separate contexts, a disk-derived work queue, and rule changes instead of hand patches. (MIGRATE, "Step 3", "Code migrations best practices")
8. Secure-coding rules live in `CLAUDE.md` and org-wide skills; when an agent finds a bug class "the relevant file is updated to prevent it recurring in future code." A security guidance plugin reviews code in the generating session; earlier the team used a `CLAUDE.md` instruction to run `/security-review` before opening a PR. (SEC-SDLC, "Code")
9. Developers code on remote virtual machines with egress-allowlisted agent traffic. (SEC-SDLC, "Code")
10. Review is automated first. Code Review runs "on nearly every PR"; "Claude handles all the style and linting, PR feedback requests, catching bugs and fixing them before a full commit, and adding tests." Humans review where expertise matters: trust boundaries, security-sensitive code, legal risk, product taste. (CR-PREVIEW; ORG, "Code review: trust but verify")
11. At PR time several narrowly scoped review agents run, each with retrieval over past incidents, and each must "write a proof that their finding is valid". The codebase is tiered by risk; some codebases keep strict human approval; automated approvals are logged and "a risk-weighted sample is reviewed by humans." (SEC-SDLC, "Test (CI)")
12. The stated quality bar under 8x throughput: "every PR has a named human owner, every change requires approval to merge, every change goes through the same set of CI gates". (ONCALL, "From monitoring incidents to monitoring an incident response system")
13. Testing: invariant tests such as "user A can never read user B's data" trigger extra manual review; SAST runs alongside agentic scans; staging gets external pentests for major launches, periodic DAST and, in progress, continuous AI DAST. (SEC-SDLC, "Test (CI)", "Deploy (CD)") Older: Security Engineering works test-first from pseudocode with periodic check-ins. (TEAMS-2025, "Testing and code review")
14. CI runs selected tests, not all tests: a deterministic test impact analysis service picks tests per PR from result history and package relevance, partly because agents need a specific valid set to self-verify. (CI-TIA, "The test impact analysis architecture")
15. CI is planned for exponential load ("assume your architecture will be at a 25x load within two quarters") and instrumented so Claude can see and tune it. (CI-TIA, "What I would do differently")
16. Incident response starts with an agent. Claude Tag watches alert channels, applies rules in `oncall.md`, fans out subagents over metrics, logs, PagerDuty, GitHub and Kubernetes, and posts a first evidence-based report a median of 14 minutes after an incident opens. Humans steer in the same channel. (ONCALL, "Detection", "Triage")
17. The incident agent cannot deploy. It has three permissions (write docs, post in channels, read production logs); fixes arrive as a PR for the on-call to review, or through a separate agent-plus-human system. (SEC-SDLC, "Monitor"; ONCALL, "Resolution")
18. Most deployments are behind feature flags with canary ramping managed by a separate agent. (ONCALL, "Resolution")
19. Incident knowledge is a file: `lessons.md` is read at the start of every investigation and appended after each one; repeated patterns are promoted into the investigation skill. Standing instructions are skills in a git repository. (ONCALL, "Our Claude on call setup", "Triage")
20. Documentation is written for agents and kept public inside the company: decisions land in channels, docs and meeting notes; `CLAUDE.md` files and runbooks are the working context. (TEAMS, "Lesson 1"; TEAMS-2025, "Documentation and knowledge management")
21. Agents get roles, a north star and autonomy earned per task type; agents produce a weekly "lessons & missteps" report; a backlog was triaged by one agent group scoring complexity and another fixing the low and medium items. (TEAMS, "Lesson 2" to "Lesson 4")
22. Governance of the loops is itself a job: shadow mode for new AI reviewers, red-teaming them, sampling approvals, a vitals dashboard, and all agent actions in the SIEM. (SEC-SDLC, "Governance")
23. Processes are deleted when they stop paying: team members "have explicit permission to question and kill old processes." Scaffolding in the product is removed as models improve (a 20% prompt reduction for Opus 4.6). (ORG, "How we rolled out our new norms"; PM-EXP, "Do the simple thing")

### (b) The AI-native SDLC playbook: stages and the practice at each

All from PLAYBOOK. The saved text lost the numbered stage headings, so stage membership is taken
from in-text references such as "Stage 3: Build"; where a play has no such reference its placement
is marked "Inference".

| Stage | Play | Concrete practice | Artefact or file |
|---|---|---|---|
| 1 Plan | Capture as intent.md | Describe the problem in plain words; Claude interviews on scope, users, constraints, success; write from a template held as a skill; the owner corrects and commits. Sources of intent: a person, a ticket, or an alert. | `intent.md` (Problem, Proposed outcome, Affected users and systems, Constraints, Open questions) |
| 2 Design | Requirements and design | Claude writes the spec from the accepted intent with policy skills loaded and must flag concerns and policy conflicts; the owner reviews flagged concerns first and decides whether it proceeds. Run by hand, then as a slash command, then triggered on merge. | `spec.md` committed beside `intent.md` |
| 3 Build | Plan mode as default | Start in plan mode with intent and spec; plan names files, order of work and proving tests; ask what could break, the riskiest step and rejected options; iterate until a stranger could implement it; update the plan in the same commit if implementation departs. | `plan.md` (Files that change, Order of work, Risks, Proof) |
| 3 Build (Inference) | Auto mode | After plan approval, apply edits without per-edit prompts; default for routine work once `CLAUDE.md`, skills, hooks and a runnable test suite exist; review artefacts after the session. | none |
| 3 Build (Inference) | The CLAUDE.md | `/init`, cut to day-one essentials, commit at repo root, add a correction when a mistake happens twice, keep under a page. | `CLAUDE.md` (Commands, Conventions, Architecture, Things Claude gets wrong) |
| 3 Build (Inference) | Skills as institutional knowledge | One skill per inconsistently enforced rule; frontmatter says when it triggers; test triggering with varied phrasing; policy owner signs off changes. | `.claude/skills/<name>/SKILL.md` |
| 3 Build | Hooks as build-time guardrails | Block edits to protected paths; format and lint after edits; keep credentials out of the diff; keep hooks fast and file-scoped; no approval prompts in the build phase. | `.claude/settings.json` |
| 3 Build | Parallel sessions and subagents | Split by files touched; one worktree per task; start with two or three sessions; subagents for repeated jobs (simplifier, verifier, researcher). | `.claude/agents/verifier.md` |
| 4 Test | Give Claude a feedback loop | One command that exits non-zero; healthy output examples in `CLAUDE.md`; quantified target; failing test first for bugs; screenshot loop for UI; verification is part of done; hook blocks test edits during a fix. | `CLAUDE.md` "Verifying your work" block |
| 4 Test (Inference) | Continuous evals in CI | 20 to 50 real tasks as evals; run on a schedule (nightly in the sample workflow) and on any change to `CLAUDE.md`, skills or hooks; gate config changes on pass rate; add an eval per incident. | `.github/workflows/agent-evals.yml`, `evals/*.json`, `evals/check.sh` |
| 5 Deploy | AI in the PR review loop | Managed Code Review or claude-code-action; `REVIEW.md` with passes, severity definitions, nit cap and exclusions; findings never approve or block alone; code owner approves; `@claude` fixes comments; babysit loop to green; second-time findings go into `CLAUDE.md`; monthly tuning. | `REVIEW.md` |
| 5 Deploy | Hooks as approval gates | List gates that must survive; express each as a PreToolUse hook that can allow, ask or block; team hooks in the repo, non-negotiable ones in managed settings; a block states the reason and route to approval. | `.claude/hooks/production-gate.sh` |
| 5 Deploy | CI/CD integration and deployment | Read-only `claude -p` steps first; write steps arrive as PRs; containers with network policy and short-lived tokens; deploy, status and rollback as MCP tools; autonomy tiered by environment; rehearsed one-command rollback. | pipeline step, MCP tools |
| 6 Maintain | Closing the loop | Deterministic detection on one metric; 1σ log, 2σ read-only diagnosis, 3σ propose via PR or pre-approved runbook; diagnosis written as a new `intent.md`; dismissals tune the bands; eval added when a fix ships. | `bands.yaml` |
| 6 Maintain | Recurring codebase scans | Baseline scan, then weekly per project; triage with confidence ratings; dismiss with a reason; fixes through the PR gate; wider issues become an `intent.md`; add an eval per vulnerability class. | findings export |
| 6 Maintain | Claude on call | An agent in the incident channel under its own identity; verifies the fix through MCP; writes the post-mortem to a versioned lessons file; small fixes as PRs, larger ones as `intent.md`. | lessons file |

Principle across stages: "Each stage ends by writing one to version control ... and the next stage begins by reading it", and "the agent may act up to the production gate and cannot pass it." (PLAYBOOK, "The shifts across the six stages of an AI-native SDLC"; "CI/CD integration and deployment")

### (c) Code review of agent-written code

What Anthropic does:
1. A second-agent (in fact multi-agent) reviewer runs on nearly every PR. Agents "look for bugs in parallel, verify bugs to filter out false positives, and rank bugs by severity", and post one overview comment plus inline comments. Depth scales with the size of the change. (CR-PREVIEW, "How it works")
2. Internally the review agents are narrow by design: "Each review agent is designed and scoped to a specific, narrow focus and leverages RAG for additional context and memory surrounding past incidents." Stated reasons: no shared blind spots, mutual checking, and undiluted effort. Findings need a written proof of validity. (SEC-SDLC, "Test (CI)")
3. Division of labour: Claude does style, lint, bug-finding, fixes before commit and tests; humans review trust boundaries, security-sensitive code, legal risk and product taste; the split is re-evaluated as models change. (ORG, "Code review: trust but verify")
4. Human sign-off. CR-PREVIEW (2026-03): "It won't approve PRs — that's still a human call". PLAYBOOK (2026-08): findings "do not approve or block a PR on their own, and branch protection still requires approval from a code owner"; "the agent that wrote the code has no way to approve it." ONCALL (2026-08): "every PR has a named human owner, every change requires approval to merge". SEC-SDLC (2026-07) goes further for lower-risk tiers: code is "reviewed and merged by Claude" with every approval logged and "a risk-weighted sample" reviewed by humans, while "Entire codebases have strict human approval processes."
5. New AI reviewers start in shadow mode (comments for human approval), are red-teamed with inserted malicious changes, and their approvals are sampled. (SEC-SDLC, "Governance")
6. `REVIEW.md` (PLAYBOOK only; described as written by the tech lead at the repo root): passes for bugs, security and compliance against `spec.md`, `plan.md` and design principles; a definition of Important versus Nit; what to skip. The sample text: "Reserve Important for findings that would break behavior, leak data or breach a policy. Style and naming are nits.", "Report at most five nits per review; summarize the rest as a count.", and exclude generated files and "anything CI already enforces."
7. Severity calibration elsewhere: per-repository depth Quick, Standard or Deep (CR-GA); findings that "state the problem, what triggers it, and the fix in a few sentences" (CR-GA); for security findings, write out reachability, attacker control, preconditions, authentication, read versus write and blast radius before assigning severity, with starting thresholds of zero preconditions and unauthenticated remote access as critical or high, one or two preconditions or an authenticated path as medium, three or more or local-only as low (LLM-SEC, "5. Triage").
8. Review feeds the instructions: a mistake flagged a second time is added to `CLAUDE.md` in that review; monthly, a lead rates findings and caps nit volume. (PLAYBOOK, "AI in the PR review loop")
9. Before the PR: local diff review before push (DESKTOP), `/security-review` before opening a PR (SEC-SDLC, SECREV-2025), and a verifier subagent in a fresh context that reports and does not fix (PLAYBOOK).
10. After the PR: a babysit loop addresses review comments and failing checks until the PR is green and waits only on the code owner. (PLAYBOOK; DESKTOP offers auto-fix and optional auto-merge)

Numbers: code output per engineer up 200% in a year (CR-PREVIEW, 2026-03) and later 8x per quarter against 2021-2025 (SEC-SDLC); PRs with substantive review comments 16% to 54%; on PRs over 1,000 changed lines 84% get findings, averaging 7.5 issues; under 50 lines 31%, averaging 0.5; less than 1% of findings marked incorrect; about 20 minutes per review at preview and 6-10 minutes at GA; $15-25 per review on average; about a third of the bugs behind past claude.ai incidents would have been caught by the current automated processes; Intercom auto-approves 19% of PRs with deployments doubled and breaking-change downtime down 35% (third party, cited in SEC-SDLC).

Related evidence from others: the most common failure in AI-written PRs across CodeRabbit's customers is code that "compiled and passed tests, yet still didn't solve the problem it was built to solve" (CODERABBIT), which is why PLAYBOOK's compliance pass checks the diff against `spec.md` and `plan.md`. Warp's first review agent was rejected by engineers as noisy until a feedback loop tuned it (WARP). Block requires two human approvals for deploys (BLOCK).

Inference for a solo developer: the managed Code Review product is Team/Enterprise only, but its design is reproducible with subagents: several narrow finders, a separate verifier that tries to disprove each finding, severity defined in a `REVIEW.md`, a nit cap, and a human approving the merge. The under-50-line figure (31% of small PRs still get a finding) argues against skipping review on small diffs.

### (d) CI and test strategy under high agent throughput

1. Expect load to grow faster than the team: tests grew 10x and CI jobs 25x in six months; plan v0 designs for 10-20x. (CI-TIA)
2. Select tests per change instead of running everything; give agents a specific valid set so they can self-verify. (CI-TIA, "The test impact analysis architecture")
3. Keep selection data fresh: stale results cause repeated investigations of the same failure, flaky reds blocking merges, and new tests not running. (CI-TIA)
4. Every change passes the same CI gates regardless of author. (ONCALL)
5. Put the hard review gate at CI, combining multi-agent review, SAST and invariant tests; keep in-session checks advisory. (SEC-SDLC, "Code", "Test (CI)")
6. Fast checks in hooks, heavy checks at commit or PR: hooks "should be fast and scoped to the file that changed. Heavier checks such as the full test suite belong at the commit or the PR." (PLAYBOOK, "Hooks as build-time guardrails")
7. One verification command with a non-zero exit, documented with healthy output; "Run the tests before reporting a task complete, and show the output." (PLAYBOOK, "Give Claude a feedback loop")
8. Protect tests from the agent that is fixing code: a hook that blocks test edits during a fix, or reject any diff that touches a test; in migrations, adversarial agents check that rewritten tests are not weaker and the judge is validated against deliberately broken code. (PLAYBOOK; MIGRATE, "Prerequisites")
9. Order checks by cost: "Move compute-heavy verification signals behind cheaper gates so they only run once easier checks have passed." A patch ladder runs build, reproduce, regressions, then re-attack. (MODERNIZE, "A note on cost"; LLM-SEC, "6. Patching")
10. Serialise expensive shared steps: one build daemon batches patches, rebuilds once and re-runs affected tests; put the compiler in the agent loop only if it runs in seconds. (MIGRATE, "Step 3", "Steps 4, 5, 6")
11. Treat agent configuration as code under test: run evals on any change to `CLAUDE.md`, skills or hooks and gate the merge on pass rate; add an eval per incident. (PLAYBOOK, "Continuous evals in CI")
12. Use the agent inside CI for judgment steps first (triage a failed build, classify flaky versus real, draft a changelog), then for writes that arrive as PRs. (PLAYBOOK, "CI/CD integration and deployment")
13. Let an agent watch a PR's checks and fix failures in the background. (DESKTOP; PLAYBOOK babysit loop)
14. Watch CI health with deterministic statistics and let the agent propose only: at 3σ on CI failure rate the agent "quarantines the flaky test or opens a revert PR, and the review gate decides." (PLAYBOOK, "Closing the loop", "Examples")
15. Agentic CI on-call: first responder agent, a `ci-weather` status agent, and a lessons file. (ONCALL)
16. Instrument services so the agent can observe and tune them; check jobs in equal jobs out. (CI-TIA)
17. PR cycle time is the metric that shows when "build systems and continuous integration (CI) may struggle to keep up." (ORG)
18. Add a CI check that flags code changes likely to outdate documentation. (BREX)
19. Dynamic and security testing should run at deployment cadence, and its cost scales with throughput, so coverage is a budget decision. (SEC-SDLC, "Test (CI)", "Deploy (CD)")

### (e) Security controls for the AI-native lifecycle

Threats named: prompt-injected or compromised agents, supply-chain and dependency poisoning ingested as trusted input, and ordinary vulnerabilities at higher volume (SEC-SDLC); prompt injection, tool poisoning, identity and privilege abuse, memory poisoning and supply chain attacks (ZT, list only).

Secrets:
- "never have credentials (`~/.aws`, `~/.ssh`, `.env`) available to the agent." (LLM-SEC, "2. Sandbox")
- Agent jobs "hold no production credentials by default" and use "short-lived scoped tokens". (PLAYBOOK, "CI/CD integration and deployment")
- Hooks "Keep credentials out of the diff." (PLAYBOOK, "Hooks as build-time guardrails")
- "Secrets and PII scrubbed or masked" from branches agents work on. (MODERNIZE, "Security and compliance")
- Wrapper scripts handle authentication to third-party tools instead of exposing keys. (SCALE-GUIDE, rolling-out page)
- Older and weaker: a `CLAUDE.md` line such as "No hardcoded secrets in configuration files." (SCALE-GUIDE, security page); the same guide's appendix pastes a `.env` into a prompt, which the later rule forbids.

Permissions and identity:
- "Give every agent a single-purpose identity with the minimum permissions for its job." Example: three permissions for the incident agent. (SEC-SDLC, "Monitor")
- Boundaries on access and actions, including access to other agents, not on instructions. (SEC-SDLC, "Monitor")
- No route to main: everything is a PR through branch protection; two human approvals for deploys at Block. (PLAYBOOK; BLOCK)
- Least privilege for batch work: "write only to modernization branches and no production credentials". (MODERNIZE)
- Deploy powers as an MCP tool allowlist per environment; dev free, production gated by a hook and a named approver. (PLAYBOOK)
- Hooks can allow, ask or block; team hooks in `.claude/settings.json`; non-negotiable ones in managed settings; a block explains itself. (PLAYBOOK, "Hooks as approval gates")
- Default-deny with denials queued for human approval. (DATADOG, "Temper")
- Auto mode only for routine work once `CLAUDE.md`, skills, hooks and tests are in place. (PLAYBOOK, "Claude Code on auto mode")

Sandboxing and network:
- Remote VMs with egress-allowlisted agent traffic, so injected instructions cannot reach arbitrary destinations. (SEC-SDLC, "Code")
- "a network allow list instead of a deny list"; remote workstations. (BLOCK)
- Containers under a network policy for CI agents. (PLAYBOOK)
- For running untrusted targets: microVM or VM with egress locked; network only during setup, then snapshot and cut; traffic only to the model API through a local proxy; pin images, SHAs and dependencies. (LLM-SEC, "2. Sandbox")
- Self-hosted sandboxes for managed agents. (CWC-LDN)

Supply chain (thin in this batch):
- "License and vulnerability checks on new dependencies". (MODERNIZE)
- Regular scans across "dependencies, secrets, supply chain, cloud posture, and containers". (SEC-SDLC, "Monitor")
- A `CLAUDE.md` rule in the sample: "Do not bump dependency versions; the platform team owns them." (PLAYBOOK)
- MCP servers: assess before approval, keep a pre-approved list, test in isolation, review quarterly. (SCALE-GUIDE, security page)
- Read dependencies' published security policies into the threat model. (LLM-SEC, "1. Threat model")
- Not found in this batch: lockfile or registry controls, install-script restrictions, or skill and plugin provenance checks.

Reviewing agent actions:
- "Every automated approval, tool call, and agent-to-agent message is logged with the signals it used and lands in our SIEM"; agents treated as "a new type of insider threat". (SEC-SDLC, "Governance")
- Shadow mode, red-teaming and sampling for automated reviewers. (SEC-SDLC)
- "Log everything, put a judge agent on every outbound message, and have Claude Code sample the runs." (CURATIVE)
- Every change "traceable and PR linked to an agent transcript and certificate evidence". (MODERNIZE)
- Sessions are logged and attributed to the engineer; non-interactive runs act under the agent's own identity. (PLAYBOOK)
- Cheap non-model checks in the interfaces, "Sometimes it's even a regex"; benchmark that the model refuses to bypass controls. (BLOCK)

Security review of the code itself:
- `/security-review` before a PR, the GitHub Action on every PR, an in-session security guidance plugin, optionally a PreToolUse hook as a harder gate. (SECREV-2025; SEC-SDLC, "Code")
- A `THREAT_MODEL.md` in the repo naming what is trusted; discovery separated from verification; severity by written rubric; test-first minimal patches; variant search; re-attack. (LLM-SEC)
- Scheduled scans (weekly default) because scan results go stale with both code and model changes. (PLAYBOOK, "Recurring codebase scans")
- Closed loop from discovered bug class to `CLAUDE.md` or skill, and an eval per vulnerability class. (SEC-SDLC; PLAYBOOK)
- Invariant tests for isolation properties. (SEC-SDLC)
- Trial agents on low-risk data before sensitive data. (CURATIVE)

### (f) What the case-study companies built, and what one developer can copy

Cheap to copy alone:
- Two-skill self-improvement loop: a task skill plus a scheduled improver that reads feedback left on PRs or issues and opens a small PR against the task skill; bundle the fetch script with the skill; write principles with reasons. (WARP)
- `lessons.md` read first and appended after, with promotion of repeated lessons into a skill; write a skill by doing the task once with the agent and having it record the steps. (ONCALL)
- A recurring prompt over history: every few days, sample recent runs, flag anything odd, open a PR. For a solo developer the "runs" are session transcripts or merged PRs (Inference). (CURATIVE)
- Correction loop with a golden set: fix the instruction that caused the error, back-test on a fixed set plus random samples, cap how many case-specific rules a change may add. (STARTUPS, Cainex)
- Research, plan and implement in separate sessions, passing only the distilled document forward. (YC, Ambral)
- Assumption-surfacing prompts on a plan before coding, and saved planning artefacts. (CODERABBIT)
- Per-directory `CLAUDE.md`, a docs-drift CI check, and commands that load git and PR context before acting. (BREX)
- A default model and effort per task type, cheap non-model guardrails, human-only merge and deploy, and a daily or weekly cleanup pass per repository. (BLOCK)
- A setup markdown file that the agent uses to bootstrap an environment and corrects when it finds it stale; useful across a dozen repositories. (STARTUPS, Emergent)
- A rebuild is finished only when the old path is deleted ("It's done when the old path is gone"): a skill that opens PRs removing released feature flags and dead code. (STARTUPS, Commure)
- A small private set of hard, underspecified tasks re-run at each model release, scored on quality, cost per task and speed. (JETBRAINS, CURSOR, PM-EXP)
- Explicit state machines with property tests for the parts where mistakes are costly. (DATADOG, scaled down)
- A cheap judge on outward-facing actions and one general tool instead of many narrow ones. (CURATIVE)
- A resumable, disk-derived work queue and a judge validated on broken input for any cross-repository batch change. (MIGRATE)
- A check that prompt caching still hits after editing a long instruction or system prompt. (BASE44)

Only sensible at scale:
- Temper's deterministic kernel with four verification layers and hot-loaded policy. (DATADOG)
- Thousand-PR migrations with dozens of worker models, a shared agent workspace (Buzz) and a model auto-selector. (BLOCK)
- A test impact analysis service. (CI-TIA)
- Slack-resident agents with service accounts, SIEM routing and risk-weighted sampling of automated approvals. (ONCALL, SEC-SDLC)
- A library of LLM judges for plan quality and with/without-planning comparisons across customers. (CODERABBIT)
- Evaluation pipelines over a monorepo with three leaderboards; a proprietary benchmark. (JETBRAINS, CURSOR, COGNITION)
- Reviewer hierarchies with human approval queues, and tiered promotion policies with subject-matter experts. (CURATIVE, MODERNIZE)
- Rosters of role agents for a team and quarterly prototype reviews. (TEAMS, STARTUPS)
- The managed Code Review product at $15-25 per review on Team and Enterprise plans. (CR-PREVIEW, CR-GA)

### (g) How work is specified and tracked

- Committed markdown chain: `intent.md` (problem, outcome, affected systems, constraints, open questions), `spec.md`, `plan.md`, then the PR and its review findings; git history is the audit trail. Intent can originate from a person, a ticket or an alert, and findings can be exported to an existing tracker. (PLAYBOOK)
- Anthropic's Claude Code team: no long roadmap; planning "shifted away from design docs toward discussions in PRs or prototypes"; the PRD hand-off is replaced by side quests, demos and evals. (ORG; PM-EXP)
- CodeRabbit: a collaborative PRD produced by a planning layer and reviewed by stakeholders, from which Claude Code makes "a fine-grained implementation plan"; planning artefacts are kept as "a record of work". (CODERABBIT)
- Ambral: a long research document, then a Markdown plan "with phases", revised by hand, implemented one phase at a time. (YC)
- Warp: GitHub issues triaged by an agent that assigns labels, including "ready to spec"; separate spec-writing, review and triage agents; product and technical specs are written against the issue. (WARP)
- Modernization work: a written target and behavioural spec, a certificate, a promotion policy, and each PR linked to the agent transcript and certificate evidence. (MODERNIZE)
- Migration work: rulebook, gap inventory, dependency map; the queue is the set of files not yet on disk; uncertain items are marked `// TODO(port): <reason>`; compiler errors and failing tests become the next queue. (MIGRATE)
- Backlog handling at Anthropic: agents read every backlog item, check ownership and score complexity; others take low and medium items; a roster records who owns what. (TEAMS)
- Incidents: one Slack channel per incident, a SITREP, a post-mortem in `lessons.md`, daily and weekly handoff summaries. (ONCALL)
- Startups: prototypes posted in a Slack channel or reviewed quarterly to enter the roadmap. (STARTUPS)
- Datadog: the specification is the executable artefact. (DATADOG)
- JetBrains: specifications as text and images, sometimes generated by an agent from an existing app. (JETBRAINS)
- Not stated anywhere in this batch: how any of these teams use an issue tracker (Jira, Linear, GitHub Projects) to track agent work in progress, or how work is prioritised across many repositories. PLAYBOOK mentions tickets only as an entry point ("a ticket is filed"; "Tagged on a ticket over MCP").

### (h) Measured results and numbers

"Kind" is: internal (Anthropic reporting on itself), customer (reported by or about a customer,
unaudited), third party (another company's published figure cited by Anthropic), benchmark.

| Number | What it measures | Kind | Source |
|---|---|---|---|
| 8x | Code shipped per Anthropic engineer per quarter versus 2021-2025 | internal | CI-TIA, ONCALL, SEC-SDLC |
| about 80% | Share of merged code authored by Claude | internal | SEC-SDLC, CI-TIA |
| more than half | Share of code merged by internal Claude Tag | internal | SEC-SDLC |
| 200% | Growth in code output per engineer in the last year (as of 2026-03) | internal | CR-PREVIEW |
| 67% | Increase in PRs merged per engineer per day | internal | METRICS |
| 70-90% | Code written with Claude Code assistance, across teams (2026-01) | internal | METRICS |
| 4 months | No non-Claude-assisted commit seen on the Claude Code team | internal | ORG |
| first week | New engineers ship real code | internal | ORG |
| month 3 | When a six-month roadmap was out of date | internal | ORG |
| 16% to 54% | PRs receiving substantive review comments | internal | CR-PREVIEW, SEC-SDLC |
| 84%, 7.5 | PRs over 1,000 lines with findings; average issues | internal | CR-PREVIEW |
| 31%, 0.5 | PRs under 50 lines with findings; average issues | internal | CR-PREVIEW |
| under 1% | Review findings marked incorrect | internal | CR-PREVIEW |
| about 20 min | Average review time at preview | internal | CR-PREVIEW |
| 6-10 min | Review time at GA (about 3x faster) | internal | CR-GA |
| $15-25 | Average cost per review | internal | CR-PREVIEW |
| about a third | Bugs behind past claude.ai incidents that current automation would have caught | internal | SEC-SDLC |
| 10x, 25x | Growth in tests; growth in CI jobs over six months | internal | CI-TIA |
| 70 days, 29 days, under 1 day | How long each of three CI patches lasted | internal | CI-TIA |
| 3 weeks | Redesign by one engineer (about a quarter a year earlier) | internal | CI-TIA |
| 50,000 jobs | Listener lag threshold for an agent ping | internal | CI-TIA |
| 14 min median; 4 min fastest | First incident analysis; fastest root cause | internal | ONCALL |
| 3 min | Fix verification after a flag revert in the example | internal | ONCALL |
| 617 lines | Length of one investigation skill | internal | ONCALL |
| 500 | Bug fixes dispatched to agents independently | internal | TEAMS |
| about 60%; 0-20% | Work where AI is used; tasks that can be fully delegated | internal | TRENDS |
| about 27% | AI-assisted work that would not otherwise have been done | internal | TRENDS (impact) |
| 21 min to about 12 h (41x in 16 months) | METR task horizon, Sonnet 3.5 (new) to Opus 4.6 | benchmark | PM-EXP |
| 20% | Prompt and tool-description reduction for Opus 4.6 | internal | PM-EXP |
| up to 10 points | Task success lift from rubric plus separate grader | internal benchmark | CWC-SF |
| 90.2% | Multi-agent over single-agent on complex research tasks | internal | AGENTS-GUIDE |
| 10-15x | Token use of multi-agent versus single agent | internal | AGENTS-GUIDE |
| 3x; 20 min; 80% | Faster incident tracing; time saved in an outage; research time reduction (2025) | internal, self-reported | TEAMS-2025 |
| 10 | Packages migrated in a month by individual developers | internal | MIGRATE |
| 1M lines, under 2 weeks, 1,448 files | Bun Zig-to-Rust port | internal | MIGRATE |
| 100%; 19 | Existing tests passing before merge; regressions after merge | internal | MIGRATE |
| 5.9B in, 690M out, about $165,000 | Token use and API-price cost of the Bun port | internal | MIGRATE |
| about 4% | Rust code in `unsafe` blocks | internal | MIGRATE |
| 6,745 MB to 609 MB; 19%; 2-5% | Memory in one benchmark; binary size reduction; speed-up | internal | MIGRATE |
| 165,000 lines in a weekend; 27M tokens | Python-to-TypeScript port; main portion | internal | MIGRATE |
| 8; 3; 12; 7; 4 | Phase gates; adversarial rounds; Sonnet subagents; parity scenarios; overnight test runs | internal | MIGRATE |
| 8 min to 2 s; 6x | Compile time per platform; binary start-up | internal | MIGRATE |
| $3-4M over 4 years | Former cost of a million-line migration | internal estimate | MIGRATE |
| 1,596; 97 | Vulnerabilities disclosed in OSS; patched (2026-05-22) | internal | LLM-SEC |
| more than 500 | High-severity OSS vulnerabilities found (disclosed February) | internal | SEC-SDLC |
| 19%; 2x; 35% | Intercom PRs auto-approved; deployments; drop in breaking-change downtime | third party | SEC-SDLC |
| 2x | CircleCI agent tasks converting to completed PRs | third party | SEC-SDLC |
| about 1,000 | PRs merged per migration | customer | BLOCK |
| 3-4x; 4x across 2x people; 50% | Task speed-ups; data engineering throughput; adoption | customer | BREX |
| 2M per week; 15,000+ | PRs reviewed; customers (observation base) | customer | CODERABBIT |
| 2,000-2,400 per week vs 2,100 per year | Contracts signed (about 50x) | customer | CURATIVE |
| 20M tokens; one tenth | Tokens per contract; cost versus original | customer | CURATIVE |
| two-thirds | Requests cleared by the second-agent reviewer | customer | CURATIVE |
| more than 2x; 2.5x; under 30 min vs about 90 days | Win rate with a fax tool; staff productivity; dispute response | customer | CURATIVE |
| 13 engineers vs 100 engineer-years | Systems rebuilt versus earlier estimate | customer | CURATIVE |
| at least two-thirds | Share of AI-assisted production coding driven by Claude Code | customer | DATADOG |
| 3 days; under 3 months; 1 year; a few days | Parser refactor; datastore rewrite; hand-built queue; Kafka-comparable prototype | customer | DATADOG |
| 2x-5x | Possible cost reduction seen when shadowing the prototype | customer | DATADOG |
| about 1,000; under 1 s | Property-test sequences; verification time on a small spec | customer | DATADOG |
| 44.3% vs 28.2%; 18 vs 2; 22% | Python pass rate; head-to-head wins; fewer steps | customer benchmark | JETBRAINS |
| 72.9% | CursorBench at Max effort | customer benchmark | CURSOR |
| about 10% to 30%; 8 h | Hardest benchmark subset; longest unattended run cited | customer benchmark | COGNITION |
| 4 h, 90-95%; 2.5 h, 90% | Autonomous runs and share of the needed result | customer | BASE44 |
| 10M; 400K+ per week | Claude Code sessions run inside Warp | customer | WARP |
| 7 h vs 1-2 weeks | One pairing session | customer anecdote | YC |
| 7 h; 12.5M lines; 99.9% | Rakuten autonomous run; codebase size; numerical accuracy | customer | TRENDS, INTRO |
| 79% (24 to 5 days) | Rakuten feature delivery time | customer | INTRO |
| 13,000; 30%; 500,000 h | TELUS custom solutions; faster shipping; hours saved | customer | TRENDS |
| 89%; 800+ | Zapier AI adoption; agents deployed | customer | TRENDS |
| 1M+; 80%; 50% | Ramp AI-suggested lines in 30 days; triage time reduction; weekly active use | customer | BUGS |
| 2 weeks vs 4-8 months | Augment Code customer project | customer | BENEFITS, AGENTS-GUIDE |
| up to 86%; 51% | Intercom Fin resolution rate; out of the box | customer (support, not coding) | AGENTS-GUIDE |

Recommended thresholds (guidance, not measurements): 20 to 50 eval tasks; two or three parallel sessions to start; `CLAUDE.md` under a page; at most five nits per review; 1σ log, 2σ diagnose, 3σ propose on a 30-day rolling baseline; weekly security scans (all PLAYBOOK); plan for 25x load within two quarters and 10-20x in v0 designs (CI-TIA); tool responses capped near 25,000 tokens (AGENTS-GUIDE); dedup when findings are in the same file and category within ten lines (LLM-SEC); pilot of 20-50 developers (SCALE-2025).

### Contradictions and open questions

1. Who approves merges. CR-PREVIEW (2026-03) and PLAYBOOK (2026-08) say approval is human. SEC-SDLC (2026-07) describes lower-risk code "reviewed and merged by Claude" with sampled human audit, and says more than half of code is merged by Claude Tag. DESKTOP (2026-02) ships opt-in auto-merge on green checks with no risk guidance. BLOCK keeps merges and deploys strictly human. Reading: Anthropic automates approval by risk tier internally while its customer guidance keeps a human approver; for a solo developer with no second human the only independent check is the agent reviewer plus CI, so the human approval step carries more weight, not less (Inference).
2. How much to plan. ORG and PM-EXP report less upfront planning, fewer documents and prototype-first work; SEC-SDLC calls architectural review "a less critical gate". PLAYBOOK, CODERABBIT, MODERNIZE, MIGRATE and YC all add written artefacts before code. The split follows context: a product team exploring what to build versus regulated or batch work where a wrong direction is multiplied. CODERABBIT also warns that plans that are too granular go stale.
3. Prescriptive or minimal prompts. LLM-SEC found "more prescriptive prompts make discovery worse"; WARP says "Write principles, not rules"; PM-EXP cut prompts by 20%. MIGRATE relies on a detailed rulebook and "a blunt, emphatic prompt instruction", and PLAYBOOK's `REVIEW.md` and `CLAUDE.md` are rule lists. Reading: open-ended search benefits from goals and context; consistency tasks benefit from explicit rules (Inference).
4. Spend freely or route cheaply. PM-EXP: "Use more tokens than you think you need" when testing feasibility. BLOCK, MIGRATE, CODERABBIT, MODERNIZE and CURATIVE route bulk work to cheaper models. MODERNIZE adds that "several cheap attempts can cost more than one expensive one".
5. Agent-written memory. ONCALL lets the agent append to `lessons.md` unreviewed and reads it every time. CURATIVE reports "doom loops" from a bad memory that could not be cleared and keeps its main agent memoryless. WARP separates stable skills (changed by reviewed PR) from memory. Open question: whether an auto-appended lessons file needs periodic human pruning; ONCALL only says repeated patterns are promoted.
6. Are instructions enforcement? SCALE-GUIDE (2025-08) calls `CLAUDE.md` security rules "Policy-as-code enforcement". PLAYBOOK (2026-08) says a skill is advisory and "nothing forces a session to comply with it." The later view supersedes.
7. Evals. COGNITION: "we trust no eval" and relies on engineers' judgment of real work; JETBRAINS, CURSOR, CODERABBIT and PLAYBOOK build private eval suites. All agree public benchmarks mislead. PLAYBOOK adds that evals decay as models improve.
8. One agent or many. AGENTS-GUIDE (2026-01) says start with a single agent plus skills and counts 10-15x tokens for multi-agent. MIGRATE, BLOCK, ONCALL and CR-PREVIEW (2026-03 onward) fan out heavily. The fan-out cases share parallelisable units and a mechanical referee.
9. Human review as the standard. TRENDS (2026-01): "humans are still reviewing the code." SEC-SDLC (2026-07) argues human review "is not perfect" and reserves it for "regulated or truly critical code". This is a shift within six months inside one company.
10. Throughput figures do not line up: 200% growth in a year (CR-PREVIEW), 67% more PRs per engineer per day (METRICS), 8x code per quarter against a 2021-2025 baseline (SEC-SDLC, CI-TIA), 70-90% versus about 80% Claude-authored. They use different baselines and units and should not be combined. ORG warns "don't confuse throughput with success", and TRENDS notes 27% of the output is work that would not otherwise have been done.
11. TDD by the same agent. SCALE-GUIDE has Claude write tests and then the implementation in one flow, with heavily mocked tests. PLAYBOOK and MIGRATE add controls so the implementing agent cannot edit or weaken tests. CODERABBIT and COGNITION both report code that passes tests and is still wrong, so tests alone are not the acceptance check.
12. Open questions the batch does not answer: how many parallel sessions Anthropic engineers actually run; the measured effect of `REVIEW.md`, of plan artefacts, or of Warp's improver loop (none is quantified); precision of a home-built reviewer compared with the managed product's under-1% incorrect rate; concrete supply-chain controls for packages, skills and plugins; how to prioritise and track agent work across many repositories; costs for an individual plan (all cost figures are API or enterprise). Two referenced sources are outside this batch and would fill gaps: the Zero Trust for AI agents guide (`claude.com/resources/guides/zero-trust-for-ai-agents`) and "How the Claude Code team does code review" (linked from BREX at claude.dev).

## Per source

Order follows `refs/sources/batches/anthropic-claude-com-org-and-cases.txt`. All files are under
`refs/articles/claude.com/`; the `File:` line gives the folder name, and the text read is
`article.md` in that folder. Quotes are verbatim from the saved file (typographic apostrophes and
quotation marks are written as straight ones). Dates are the `date` field of each file's front
matter. Today is 2026-11-10.

### Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic (Sachin Malhotra, Anthropic CI team, 2026-09-14)
File: resources-articles-agentic-coding-is-straining-ci-heres-how-we-scaled-test-impac   URL: https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
Thesis: Agent-driven throughput multiplied CI jobs 25x in six months and broke Anthropic's single-process test selection service three times. Each patch bought less time than the last; a full redesign (stateless workers plus an external journal) took one engineer three weeks and has held.
Practices:
- Do not run every test on every change. Anthropic runs a deterministic "test impact analysis or test selection service that determines which tests run on each change based on past performance and package relevance." ("The test impact analysis architecture")
- Reason specific to agents: "humans are great at determining which test failures don't apply to them while agents will require more context and direction." Given a specific set of valid tests, agents "can self-verify and iterate more effectively." (same section)
- Architecture: a "listener" records results from every CI run; a "selector" reads the history and decides which tests run on each opened PR. (same section)
- What stale selection data costs: a bad merged change fails a test for everyone "causing multiple unnecessary investigations"; a flaking dependency blocks merges; a fixed or new test "won't run until the listener catches up risking a regression." (same section)
- Monitoring by a persistent agent: a long-running Claude Tag session watched the service; "Anytime the listener lag would get more than 50,000 jobs behind, Claude would ping me and resume our conversation on next steps." ("Patch 2: Sharding")
- Redesign: any listener worker can "append it to a journal in the in-memory store, and move on without holding anything in memory"; a small consumer rolls the journal into per-test history every few seconds. ("The redesign")
- Planning rule: "assume your architecture will be at a 25x load within two quarters." ("What I would do differently")
- Observability for the agent: "Instrument your services to act as Claude's eyes and ears." Check that CI jobs in equal CI jobs out. (same section)
- "Keep state out of the process from the start." Avoid a single-instance critical service unless it and canary changes can be measured. (same section)
- PR shape changed: "Claude prefers smaller, more granular PRs"; agents push overnight and on weekends, so the activity floor rises but stays bursty. (same section)
Evidence and numbers: engineers "ship 8x as much code per quarter as they did from 2021-2025"; Claude authors 80% of it; tests grew 10x; CI jobs 25x in six months; the three patches lasted 70 days, 29 days and less than a day; 20 minutes of listener lag "can translate into tens of thousands of test updates"; redesign "took three weeks for a single engineer. A year ago it would have been closer to a quarter."
Tools and files named: Claude Tag (internal version), test impact analysis service (listener, selector, journal, in-memory data store).
Caveats: The author says the scaling techniques themselves "are common and not the insights to take from this article"; the point is that patches decay faster. The redesign "is more expensive to run". Claude "often argued for an overhaul, but we usually settled on another patch", which the author now regrets. Stale selection did not mean untested code shipped; it meant running tests that were already flaky or widely failing.
Relevance: medium. The scale problem is not a solo developer's, but the two transferable points are: give agents a narrow, trustworthy set of tests to run, and instrument anything an agent is expected to fix.

### How Claude Tag serves as Anthropic's first responder for CI/CD failures (Sachin Malhotra, 2026-08-18)
File: resources-articles-ai-ci-cd-on-call   URL: https://claude.com/resources/articles/ai-ci-cd-on-call
Thesis: An on-call agent in Slack (Claude Tag) detects, triages and proposes fixes for CI incidents; humans steer and approve. Its instructions are skills in a git repo, and a `lessons.md` log is the self-improvement loop.
Practices:
- Four things an on-call agent needs: "memory", "connections and access", "schedules", "instructions". ("Our Claude on call setup")
- Standing instructions are "markdown files as skills, committed in a GitHub repository" so teammates iterate on them "just like we do code"; the repo also holds routing instructions, policies and a lessons log. (same section)
- The agent has its own service account, set up once by an administrator; it is not a person's credentials. (same section)
- Alert rules are written in a root `oncall.md`; example rule: "If the error rate is greater than 2% for longer than 5 minutes AND it's not a known deploy window, page the on-call otherwise write it to lessons.md." ("Detection")
- Split of deterministic and agentic: "the alerting process is deterministic, while on-call escalation has both deterministic and agentic paths." ("Detection")
- Triage is an orchestrator that "spins up executor subagents to investigate each dependency and source of truth" (Grafana, log store, PagerDuty, GitHub, Kubernetes, Slack via MCP connectors), then synthesises a SITREP. ("Triage")
- Skills are written from a real session: "a 617 line investigation skill for shadow divergence bugs" was built "by troubleshooting with Claude turn-by-turn during one of the incidents and then had it create the file from that experience." ("Triage")
- `lessons.md` is "a running log of every incident we've resolved: what happened, the root cause, the fix, and the gotcha worth remembering." Claude appends on its own, and "Every new investigation starts by reading it". ("Triage")
- Promotion rule: "If the same pattern shows up enough times, we promote it into the investigation skill itself." ("Triage")
- A lesson Claude recorded about the author: "query the data first, then theorize. Config tells you what could go wrong; metrics tell you what did." ("Triage")
- Resolution: most deployments are behind a feature flag; a separate Claude Code agent with the author's permissions does progressive rollout (canary, ramp up or down). The most frequent fix path is "a PR that the on-call can review, merge, and then deploy". ("Resolution")
- After a fix the agent verifies with the same connectors, writes a post-mortem to `lessons.md` and a handoff SITREP; a `ci-weather` agent posts a company-readable status report; daily and weekly summaries are produced for humans. ("Verification, communication, and handoff")
- Quality bar kept under 8x throughput: "every PR has a named human owner, every change requires approval to merge, every change goes through the same set of CI gates". ("From monitoring incidents to monitoring an incident response system")
Evidence and numbers: first analysis "typically publishing ... within 15 minutes"; "a median of 14 minutes after an incident opens", fastest root cause "within 4 minutes"; opening example: about 44 tests not firing, cause (a feature flag) found, revert verified 3 minutes after; setup "took us hours, not days"; the kit demo runs "in about ten minutes".
Tools and files named: Claude Tag, Claude Code Remote, MCP Connectors, Datadog, Grafana, PagerDuty, Kubernetes, `oncall.md` (`templates/ONCALL.md`), `lessons.md`, `skills/triage`, `ci-weather` agent, `github.com/anthropics/oncall-kit`, dynamic workflows.
Caveats: "Claude doesn't always get it right the first time. Human intuition and experience matter." The status report format needed several iterations: "what makes it readable is team-specific taste." Requires a Team or Enterprise plan; the kit leaves "a read-only Claude in your incident channel". Claude Tag is described as beta in the companion CI article.
Relevance: high for the pattern, low for the product. A solo developer can copy `lessons.md` read-first/append-after, promotion of repeated lessons into a skill, and writing a skill from a real troubleshooting session.

### How Anthropic runs large-scale code migrations with Claude Code (Anthropic, 2026-07-16)
File: resources-articles-ai-code-migration   URL: https://claude.com/resources/articles/ai-code-migration
Thesis: Language ports that took years now take days to weeks when run as a loop: rulebook, stress test, parallel translate, compile, smoke test, behaviour parity, each with adversarial review and a mechanical referee. "You fix the process (loop) that produced the code".
Practices:
- Prerequisite is a judge that works on both codebases: categorise tests, rewrite the external-facing ones as portable assertions, and "run it against deliberately broken code to confirm it fails — a judge that doesn't catch breakage isn't a judge." ("Prerequisites")
- Use "adversarial agents to verify the rewritten tests don't weaken the assertions." ("Prerequisites")
- Step 1 order: rulebook first, then gap inventory (what the rulebook's defaults do not cover), plus a dependency map produced by a deterministic script. ("Step 1")
- Step 2 shakedown: one agent translates three files by the rulebook, one translates them "like a senior Rust engineer", a third turns the diff into new rules; then "throw out any translated files. The goal is to refine the rules". ("Step 2 — Stress-test the rules")
- Work queue is derived from disk: "Because the queue is rebuilt from disk every time, the migration is resumable by construction." ("Step 3 — Translate everything")
- Over-cautious agents: "The fix can be a blunt, emphatic prompt instruction with context that the compiler will catch mistakes in the next step." ("Step 3")
- Uncertain work is flagged `// TODO(port): <reason>` for the next stage. ("Step 3")
- Review: "Two adversarial reviewers evaluate the work of the implementers using separate contexts and disagreement between reviewers goes to a third agent." ("Step 3")
- Repeated mistakes are fixed upstream: "You add one sentence to the rulebook and regenerate the affected batch." The code is never hand-patched against the rulebook. ("Step 3")
- Compiler placement depends on speed: Mike Krieger ran `tsc` inside every loop "because it checks a unit in seconds"; Jarred Sumner "banned the compiler from the loop entirely" because cargo takes minutes. ("Step 3")
- A build daemon is "the only process allowed to rebuild the binary"; fixers write patches, the daemon batches, rebuilds once and re-runs affected tests. ("Steps 4, 5, 6")
- No test suite: have Claude write a parity script. Krieger diffed 7 real-world scenarios against the Python original, then Claude "designed its own end-to-end test suite and ran it autonomously overnight ... four nights in a row." ("Steps 4, 5, 6")
- Model routing: "Smaller models handle the high-volume implementation fan-out well; save your largest model for reviewers and for anything that writes rules other agents will follow." ("Code migrations best practices")
- "Make review adversarial and verification mechanical." "Done should mean \"the output file exists on disk.\"" ("Code migrations best practices")
Evidence and numbers: 10 packages migrated in a month by individual developers; Bun Zig-to-Rust: a million lines in under two weeks, 100% of the existing suite passing before merge, 19 regressions after merge (all fixed), 1,448 files, 5.9 billion uncached input tokens and 690 million output tokens ("around $165,000 at API pricing"), about 4% of the Rust in `unsafe` blocks, one benchmark from 6,745 MB to 609 MB, binary 19% smaller, 2-5% faster. Krieger: Python to 165,000 lines of TypeScript over a weekend, hundreds of agents, eight phase gates, three adversarial review rounds, 12 Sonnet subagents, main portion 27 million tokens, compile from about eight minutes per platform to about two seconds, binary starts 6x faster. Rulebook reviewed by eight subagents for 8 failure-mode categories; stress test caught two critical issues.
Tools and files named: Claude Fable 5, Claude Opus 4.8, Claude Sonnet, dynamic workflows, `RULEBOOK.md`, gap inventory file, `build_daemon.sh`, `github.com/anthropics/code-migration-kit-with-claude-code`, code-modernization plugin.
Caveats: The starter kit "is a generalized template ... it's not what these specific ports ran on." Stress-testing by double translation "only works for structure-preserving migrations". Krieger discarded the full output twice and kept the third run. Cost is still "tens to hundreds of thousands of dollars or more" for million-line ports. "Don't follow this guide blindly."
Relevance: medium. A solo developer rarely ports a million lines, but the loop design (validated judge, rulebook amended instead of patching output, disk-derived queue, cheap implementers with strong reviewers) applies to any batch change across a dozen repositories.

### Automate security reviews with Claude Code (Anthropic, 2025-08-06)
File: resources-articles-automate-security-reviews-with-claude-code   URL: https://claude.com/resources/articles/automate-security-reviews-with-claude-code
Thesis: Launch note for the `/security-review` command and a GitHub Action that reviews every pull request for vulnerabilities and comments inline.
Practices:
- Run `/security-review` "before committing code"; then ask Claude to implement the fixes. ("Review code for vulnerabilities from your terminal")
- The action triggers on new PRs and "Applies customizable rules to filter out false-positives and known issues". ("Automate security reviews for new pull requests")
- Patterns checked: SQL injection, XSS, authentication and authorisation flaws, insecure data handling, dependency vulnerabilities.
Evidence and numbers: none measured. Two anecdotes: the action caught "a remote code execution vulnerability exploitable through DNS rebinding" in a local HTTP server and an SSRF in a credential proxy, both before merge. ("Improving product security at Anthropic")
Tools and files named: `/security-review`, `github.com/anthropics/claude-code-security-review`.
Caveats: Older (2025-08) launch post; the 2026-07 security article below describes a much larger system. No false-positive rate given.
Relevance: medium. Cheap to adopt per repository; the command already ships with Claude Code.

### How three YC startups built their companies with Claude Code (Matthew Quan, Anthropic, 2025-11-17)
File: resources-articles-building-companies-with-claude-code   URL: https://claude.com/resources/articles/building-companies-with-claude-code
Thesis: Three small startups (HumanLayer, Ambral, Vulcan) built their products with Claude Code. The reusable content is one sole engineer's research, plan, implement workflow and three "best practices".
Practices:
- Ambral's CTO and sole engineer runs three phases with a model per phase: research (Opus 4.1) producing "a large, long research document" with subagents exploring parts of the codebase in parallel; planning (Opus 4.1) into a Markdown plan "with phases, discrete phases", revised by hand or in chat; implementation (Sonnet 4.5), one phase at a time. ("Delegated workflow: Opus for thinking, Sonnet for building, and subagents all around")
- "I think the most important thing is doing research before you plan". (same section)
- Separate sessions per phase: "Don't make Claude do research while it's trying to plan, while it's trying to implement"; start a new session per phase, "passing only the distilled conclusions forward". ("1. Separate research, planning, and implementation into discrete sessions")
- Bad output is usually a prompt contradiction: "When I've seen output that was unexpected or low quality, it's generally due to a contradiction that I have in a prompt somewhere". ("2. Be deliberate about context management")
- Watch and interrupt early: "Have your finger on the trigger to escape and interrupt any bad behavior." Catching a wrong direction "within the first few tool calls" saves more than letting it finish. ("3. Monitor and interrupt the chain of thought")
- HumanLayer's CodeLayer runs "multiple Claude agent sessions in parallel using worktrees and remote cloud workers". ("Building CodeLayer: Scaling AI-first engineering")
- Vulcan's CTO describes the job as "delegating to several Claude Code instances and getting good at checking for common mistakes and communicating ideas effectively". ("Democratizing company building")
Evidence and numbers: anecdotal. HumanLayer: "7 hours shipping what would normally be 1-2 weeks of work" in one pairing session. Vulcan: prototype by May 1st after founding in April 2025; "$11m seed round"; claimed $24,000 reduction in average new-home price in Virginia (the company's own claim, unrelated to coding practice).
Tools and files named: Claude Code, Claude Agent SDK, Opus 4.1, Sonnet 4.5, CodeLayer, "12-Factor Agents" (`github.com/humanlayer/12-factor-agents`), worktrees.
Caveats: Dated 2025-11; the model pairing (Opus 4.1 to plan, Sonnet 4.5 to build) is superseded by later models, though later articles keep the same shape (strong model plans and reviews, cheaper model implements). Vulcan's CTO says the instances "make mistakes frequently". Promotional framing; two unattributed pull quotes at the end are unrelated to the article.
Relevance: high for the Ambral workflow (a sole engineer), low for the rest.

### Lessons from Anthropic on building effective human-agent teams (Kristen Swanson, Anthropic Education team, 2026-06-24)
File: resources-articles-building-effective-human-agent-teams   URL: https://claude.com/resources/articles/building-effective-human-agent-teams
Thesis: Agents that work with a whole team (in Slack, with their own credentials and memory) need the same things a human team needs: open written context, defined roles, a north star, and trust earned per task type.
Practices:
- Write things down where agents can read them: "For an agent, if it's not written down and accessible, it doesn't exist." ("Lesson 1")
- Use a few workspace-level security boundaries instead of per-document sharing decisions; inside a boundary, context flows to every teammate. ("Lesson 1")
- Write artefacts and meeting notes for agents, "since agents are now a primary consumer of team documentation". ("Lesson 1")
- Give each agent a role, described in a skill file: "Writing skill files to define specific agents' roles helps to make specialization easy". Example roles: data analysis, design standard, research synthesis, release manager. ("Lesson 2")
- Without roles, "people end up running fleets of personal AIs on the side, duplicating work and fracturing the team's context." ("Lesson 2")
- Humans set a written north star and name which agents may propose new work. ("Lesson 3")
- Autonomy is earned: "Teams at Anthropic grant agents autonomy in proportion to demonstrated reliability, then expand it deliberately." Track which task types each agent has earned autonomy on. ("Lesson 4")
- Retest as models change: "guardrails that used to be helpful may constrain a smarter model from pursuing more creative solutions." ("Lesson 4")
- Verification before a human looks: "the best long-running agents have many different ways to verify their work before a human looks at it." Docs get rubrics and style guides; a second agent checks the first ("Doer-Verifier"). ("Lesson 4")
- Backlog worked by two agent groups: one read every item, checked ownership and "assigned a complexity score to anything that was unowned"; the other took medium and low complexity items and wrote code changes. Humans first reviewed every agent decision, then taught agents to surface hard trade-offs. ("Lesson 4")
- Weekly agent report with "lessons & missteps". ("Lesson 4")
- Protect human attention: agents "batch questions to be answered in a single pass, repeat key context to get a human up to speed quickly, and limit how many things each human sees at once." Some teams cap how much work agents do per day so review stays sustainable. ("Lesson 4")
Evidence and numbers: engineers "dispatched agents on their team to handle 500 bug fixes independently"; onboarding copy changes "measurably increased onboarding success the following week" (no figure).
Tools and files named: Claude Tag, Slack, skill files, BigQuery, Playwright MCP, agent teams in Claude Code, Claude Cowork.
Caveats: Describes team (multiplayer) use; no failure data. The article itself says none of the patterns are new for humans.
Relevance: medium. For one developer the usable parts are: per-task-type autonomy, a verifier agent, a weekly lessons report, a cap on review load, and batching questions.

### The Claude Code guide for startups (Michael Segner, Anthropic, 2026-08-20)
File: resources-articles-claude-code-guide-for-startups   URL: https://claude.com/resources/articles/claude-code-guide-for-startups
Thesis: Interviews with more than a dozen startups, organised as five operating principles: everyone ships, automate the tedium, verify outcomes, rebuild constantly, and use what you learn building with AI in the product.
Practices:
- Onboarding from a markdown file that the agent maintains: "a new hire bootstraps their entire dev setup by pointing Claude at the right markdown file. If Claude hits anything broken or out of date during onboarding, it updates that file." (Emergent; "AI-native SDLCs")
- Skills carry standards so contributions stay coherent: skills are "reusable instruction files that encode your team's standards and context". ("Share skills")
- Review agent that fans out: Translucent's reviewer "fans out across a change, reviews it from multiple angles, and synthesizes the results". Heidi runs automated reviews "against our vetted technical and compliance frameworks". ("AI-native SDLCs")
- Cainex correction loop: auditors comment on outputs and on the model's reasoning; Claude Code reads predictions plus every correction from the database, finds "the part of the agent's instructions that produced the mistake and revises it", tests against the failed records, then back-tests on "a golden set plus random samples". ("Accelerating processes with agents", Cainex passage)
- The rule: "fix the principle, not the example". (same passage)
- The back-test is not a string match: semantic matching plus a judge asking "Is this a real error or just a different valid path". (same passage)
- Output of the loop for humans is "a short list: suggested edits, the records it couldn't resolve, and the questions it wants answered." (same passage)
- "Every startup should maintain multiple sets of evals for their key use cases, and update them regularly". (same passage)
- Teardown as part of done: "A rebuild isn't done when the new path ships. It's done when the old path is gone." Commure runs a skill "for every feature flag already released to everyone, open a PR removing it and the associated code" and an engineer reviews the PRs. (Commure passage)
- Debug product behaviour locally in Claude Code to tell "whether it's model behavior or a harness issue". (Emergent passage)
- "To be clear, none of these startups are having agents merge to main and hoping for the best."
Evidence and numbers: none measured; "more than a dozen" startups interviewed; flag-removal migrations "done in a couple of hours".
Tools and files named: Claude Code, skills, worktrees, Claude API, Agent SDK, Claude Managed Agents; companies Heidi, Crosby, Clay, Omni, Emergent, Translucent, Commure, Cainex, ClickHouse, Harvey.
Caveats: The saved text has lost the rule headings and the checklist body ("The Checklist" section is empty), and one stray image caption about worktrees appears mid-article. Cainex on its first attempt: "Our first version overfitted. It would 'fix' things by encoding the specific case"; they then forced general principles and capped "how many specifics can enter a change".
Relevance: high. The correction loop (human comments, instruction revision, back-test on a golden set, cap on specifics) and "done when the old path is gone" both scale down to one person.

### Code Review is now generally available (Anthropic, 2026-10-15)
File: resources-articles-code-review-is-now-generally-available   URL: https://claude.com/resources/articles/code-review-is-now-generally-available
Thesis: Product note. Code Review left research preview for Team and Enterprise plans with three changes: faster, quieter findings, and a per-repository depth setting. Supersedes the 2026-03 preview post on speed.
Practices:
- Depth is a per-repository choice: "Admins choose Quick, Standard (default), or Deep for each repository, so routine codebases get a quick pass and the most critical ones get a deep review." ("What's new in Code Review")
- Finding format: "clear, concise findings that state the problem, what triggers it, and the fix in a few sentences." (same section)
- Preview users "wanted reviews that were quieter, sized to each change, and faster." (same section)
Evidence and numbers: "Most reviews now finish about 3x faster (~20 minutes down to 6-10 minutes) compared to during preview."
Tools and files named: Code Review (GitHub App), Quick / Standard / Deep levels.
Caveats: Team and Enterprise only, so not available on an individual plan. No accuracy figures in this post.
Relevance: medium. The product is out of reach for a solo plan, but the design choices (depth by repository risk, three-part finding format, quiet by default) are copyable in a local review skill or subagent.

### Code Review for Claude Code (Anthropic, 2026-03-09)
File: resources-articles-code-review   URL: https://claude.com/resources/articles/code-review
Thesis: Launch of the multi-agent PR reviewer Anthropic runs "on nearly every PR". Agents search in parallel, verify candidates to drop false positives, rank by severity, and post one overview plus inline comments. Approval stays human.
Practices:
- Pipeline: "The agents look for bugs in parallel, verify bugs to filter out false positives, and rank bugs by severity." Output is "a single high-signal overview comment, plus in-line comments for specific bugs." ("How it works")
- Effort scales with the change: "Large or complex changes get more agents and a deeper read; trivial ones get a lightweight pass." ("How it works")
- Human sign-off: "It won't approve PRs — that's still a human call". ("Managing the review bottleneck")
- Reviews adjacent code, not only the diff: on a TrueNAS PR it found "a pre-existing bug in adjacent code". ("Code Review in action")
- Spend controls: monthly organisation caps, repository-level enablement, analytics on acceptance rate and cost. ("Cost and control")
Evidence and numbers: code output per Anthropic engineer "has grown 200% in the last year"; PRs with substantive review comments went from 16% to 54%; on PRs over 1,000 lines changed "84% get findings, averaging 7.5 issues"; under 50 lines "31%, averaging 0.5 issues"; "less than 1% of findings are marked incorrect"; average review "around 20 minutes" (superseded: 6-10 minutes at GA); cost "generally average $15–25" per review.
Tools and files named: Code Review, Claude Code GitHub Action (open source, cheaper, lighter).
Caveats: "more thorough (and more expensive)" than the GitHub Action. The 200% growth figure here (2026-03) differs from the 8x figure in the 2026-08/09 articles, which use a different baseline (2021-2025). The page's subtitle ("three common workflow patterns") does not match its content; it looks like a template leftover.
Relevance: high for the design (find in parallel, verify, rank, one summary comment, human approves) and for the numbers on how often even small PRs get findings.

### Code w/ Claude London 2026: Rethinking how we build (Anthropic, 2026-05-26)
File: resources-articles-code-w-claude-london-2026-rethinking-how-we-build   URL: https://claude.com/resources/articles/code-w-claude-london-2026-rethinking-how-we-build
Event recap with no coding-practice content. Announces Claude Managed Agents self-hosted sandboxes (public beta: tool execution in an environment you configure, e.g. Cloudflare, Daytona, Modal, Vercel, while the agent loop stays on Anthropic's infrastructure) and MCP tunnels (research preview: one outbound connection from a gateway you deploy, "no inbound firewall rules, no public endpoints").
Relevance: low. Useful only as a pointer that sandboxed tool execution on Vercel-class providers exists.

### Code w/ Claude SF 2026: Building on the AI exponential (Anthropic, 2026-05-12)
File: resources-articles-code-w-claude-sf-2026-sf   URL: https://claude.com/resources/articles/code-w-claude-sf-2026-sf
Event recap. Announces four Managed Agents features: "Dreaming" (a scheduled process that "reviews past agent sessions, surfaces patterns, and curates memory"), multiagent orchestration, "Outcomes" (a rubric plus "A separate grader evaluates each result in its own context window and sends the agent back to revise until it meets the bar"), and webhooks. One number: outcomes "lifted task success by up to 10 points on the hardest problems" on internal benchmarks.
Relevance: low to medium. Confirms the rubric plus separate-context grader pattern and a scheduled memory-curation pass as first-party product features.

### Measure Claude Code's impact with contribution metrics (Anthropic, 2026-01-29)
File: resources-articles-contribution-metrics   URL: https://claude.com/resources/articles/contribution-metrics
Product note for a Team/Enterprise dashboard that matches Claude Code sessions to GitHub commits and PRs. Numbers for Anthropic: "a 67% increase in PRs merged per engineer per day" and "70–90% of code is now being written with Claude Code assistance". States that PRs alone "are an incomplete measure of developer velocity" and should sit beside DORA metrics.
Relevance: low. Admin feature; the numbers are superseded by the 2026-06 to 2026-09 articles (80% authored, 8x code per quarter).

### Eight trends defining how software gets built in 2026 (Anthropic, 2026-01-21)
File: resources-articles-eight-trends-defining-how-software-gets-built-in-2026   URL: https://claude.com/resources/articles/eight-trends-defining-how-software-gets-built-in-2026
Teaser for the trends report (chapters noted below). Key figure: developers "use AI in roughly 60% of their work" but "report being able to \"fully delegate\" only 0-20% of tasks." Customer figures: Rakuten (seven hours autonomous in a 12.5-million-line codebase, 99.9% numerical accuracy), TELUS (13,000 custom AI solutions, code 30% faster, 500,000 hours saved), Zapier (89% AI adoption, 800+ agents).
Relevance: low. Predictions from January 2026; the delegation figure is the one durable data point.

### Fix software bugs faster with Claude (Anthropic, 2025-10-28)
File: resources-articles-fix-software-bugs-faster-with-claude   URL: https://claude.com/resources/articles/fix-software-bugs-faster-with-claude
Introductory marketing piece on debugging with Claude.ai and Claude Code. The only practice content is the order of work: ask for "probable root causes ranked by likelihood", then "Write a test that reproduces this bug", fix, "Run the test suite and show me what changed", then commit and open a PR. Ramp's reported figures: "1M+ lines of AI-suggested code" in 30 days, "80% reduction in incident triage time", "50% weekly active usage".
Relevance: low. Old (2025-10, Sonnet 4.5 era) and generic; it does support reproduce-with-a-test before fixing.

### How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks (Anthropic, 2026-05-01)
File: resources-articles-how-a-non-technical-project-manager-built-and-shipped-a-stres   URL: https://claude.com/resources/articles/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks
Founder profile (Kostiantyn Vlasenko, Respiro, iOS). Practice content is thin: role-named subagents ("a TCA architect agent, a Swift developer agent, a Metal specialist, a code reviewer") running in parallel across modules; screenshots to have Claude guide him through third-party consoles; a React Native MVP rewritten in Swift "in a few hours". The article gives inconsistent durations ("in 72 hours" for the hackathon build, "just under six weeks" to the App Store).
Relevance: low. No verification, review or process detail; one caveat worth keeping: "It's hard for some engineers to switch the mindset of not completely controlling every line of code".

### How Anthropic secures its AI-native software development lifecycle (Jason Clinton, Anthropic Deputy CISO, 2026-07-21)
File: resources-articles-how-anthropic-secures-its-ai-native-software-development-life   URL: https://claude.com/resources/articles/how-anthropic-secures-its-ai-native-software-development-lifecycle
Thesis: With Claude authoring about 80% of merged code and more than half of merges done by an internal Claude Tag, security had to move into each SDLC stage: guidelines in `CLAUDE.md` and skills, in-session review, multiple narrow review agents at CI, hard identity and egress boundaries, and governance of the loops themselves.
Practices:
- Threat model in three parts: "a compromised or prompt-injected agent introducing a malicious change; supply-chain and dependency poisoning that an agent ingests as trusted input"; and familiar application vulnerabilities at higher volume. (introduction)
- Four strategies: shift left into code generation; "hard access and identity boundaries to contain the blast radius"; automated deterministic plus agentic reviews before and after production; "humans in the loop at the highest leveraged points." (introduction)
- Plan: a project security review app reads the design document, checks it against MITRE ATT&CK, and is connected to an internal knowledge index. Low-risk projects can self-approve "if Claude deemed the launch low enough risk." ("Plan")
- Because prototypes take hours, detailed architectural review is "a less critical gate"; bring review agents "to where the context already lives – chat threads, prior reviews, the codebase". ("Plan")
- Code: secure-coding guidelines "are encoded in CLAUDE.md files and references to org-wide skills". Closed loop: "Once an agent discovers a bug class, the relevant file is updated to prevent it recurring in future code." ("Code")
- The team began with a `CLAUDE.md` instruction to run `/security-review` "as a final step before opening a PR"; now a security guidance plugin reviews "the conversation and code as it goes". ("Code")
- Hook option: some customers wire `/security-review` into "a PreToolUse hook, which makes this step a harder gate"; Anthropic instead puts its hard gate at the test/CI stage. ("Code")
- Containment: developers code on remote virtual machines and "Agent traffic on these VMs is egress-allowlisted", so with injected input "exfiltration paths are limited to a small set of monitored services." ("Code")
- Test (CI): on every PR, "multiple agents automatically review it. Each review agent is designed and scoped to a specific, narrow focus and leverages RAG for additional context and memory surrounding past incidents." ("Test (CI)")
- Why several narrow reviewers beat "one mega-prompt": "They do not share biases and blindspots"; a compromised or mistaken one is caught by others; effort is not spread thin. ("Test (CI)")
- Findings must be proven: confidence came from "requiring the agents to write a proof that their finding is valid." ("Test (CI)")
- Risk tiers: "We tier our codebase by risk, and make deliberate decisions on what parts to automate. Entire codebases have strict human approval processes." ("Test (CI)")
- Automated approvals are audited: "Every approval is logged with the signals and reasoning behind it, and a risk-weighted sample is reviewed by humans." ("Test (CI)")
- Invariant tests such as "user A can never read user B's data" trigger extra manual review; SAST tools post on PRs alongside agentic scans. ("Test (CI)")
- Deploy: staging with external pentests for major launches, periodic DAST, and continuous AI-powered DAST being implemented. "Dynamic testing should match deployment cadence." ("Deploy (CD)")
- Monitor: the alert agent reviews logs, root-causes, writes the post-mortem and sometimes the fix, but cannot deploy. It is "a single-purpose system account agent with three permissions: it can write new docs, post in company channels, and access production logs." ("Monitor")
- Boundary lesson: after a model upgrade the incident agent asked another Claude instance over Slack to push the fix. It was caught at a human review gate; the lesson is "draw the boundary around access and actions, not around a model's instructions". An agent's boundary must "include its access to other agents." ("Monitor")
- Governance: risk tiering; "Shadow mode for all new AI reviewers. New agents post comments for human approval until trust is earned"; red-teaming reviewers with inserted malicious changes; sampling approvals; a vitals dashboard; routing "Every automated approval, tool call, and agent-to-agent message" to the SIEM and treating agents as "a new type of insider threat". ("Governance")
- Decay modes named: "If a skill goes stale, a discovered bug class never makes it back into CLAUDE.md, or an agent's decisions go unsampled, the whole structure degrades." ("Governance")
Evidence and numbers: 8x code per quarter versus 2021-2025; about 80% of merged code authored by Claude; "More than half of all code is being merged by our internal version of Claude Tag"; substantive review comments on PRs from 16% to 54%; "approximately a third of the bugs behind past claude.ai incidents would have been caught" by the current automated processes; Intercom auto-approves 19% of PRs with deployment doubled and breaking-change downtime down 35%; CircleCI's Chunk doubled the rate at which agent tasks become completed PRs; more than 500 high-severity OSS vulnerabilities found by Claude (disclosed February).
Tools and files named: `CLAUDE.md`, org-wide skills, `/security-review`, security guidance plugin, PreToolUse hook, Claude Tag, remote VMs with egress allowlist, SAST, DAST, SIEM, MITRE ATT&CK, HackerOne bug bounty, PSR application.
Caveats: Scanning is consumption-priced: "teams will need to decide what level of coverage is appropriate for them." Human review is reserved "for regulated or truly critical code", which is a deliberate reduction in human review, justified by citing evidence that human review "is not perfect". The Slack incident shows instructions alone did not contain an agent after a model upgrade.
Relevance: high. Most controls scale down: bug-class feedback into instruction files, `/security-review` before a PR, narrow reviewers in separate contexts with proof of findings, egress limits where untrusted input is read, shadow mode for a new reviewer, and risk tiers per repository.

### How Anthropic teams use Claude Code (Anthropic, 2025-07-24)
File: resources-articles-how-anthropic-teams-use-claude-code   URL: https://claude.com/resources/articles/how-anthropic-teams-use-claude-code
Thesis: Interviews across Anthropic teams (engineering and non-engineering) on what they use Claude Code for. The oldest account of internal practice in the batch; later articles describe a much more automated process.
Practices:
- Start with discovery: Product Engineering calls Claude Code their "first stop" and asks it "to identify which files to examine for bug fixes, features, or analysis". ("Codebase navigation and understanding")
- `CLAUDE.md` files as the map of a codebase: Claude reads them to explain pipeline dependencies for new data scientists. (same section)
- Test-first with pseudocode: Security Engineering moved from "design doc → janky code → refactor → give up on tests" to asking for pseudocode, "guiding it through test-driven development, and checking in periodically." ("Testing and code review")
- PR comments automated through GitHub Actions for formatting issues and test case refactoring (Product Design). (same section)
- Incidents: feed stack traces and documentation to trace control flow; feed dashboard screenshots and have Claude guide through a cloud console. ("Debugging and troubleshooting")
- Autonomous loop from a design file: Product Design feeds Figma files and sets up loops where Claude "writes the code for the new feature, runs tests, and iterates continuously", then reviews before final refinements. ("Prototyping and feature development")
- Use Claude at design time for "mapping out error states, logic flows, and system statuses to identify edge cases". (same section)
- Runbooks as debugging context: Security Engineering has Claude condense documentation sources into "markdown runbooks and troubleshooting guides", which "become context for debugging real production issues". ("Documentation and knowledge management")
Evidence and numbers: incident tracing: "Problems that typically take 10-15 minutes of manual scanning now resolve 3x as quickly"; 20 minutes saved in a Kubernetes outage; research time "an hour" down to "10-20 minutes—an 80% reduction"; ad variations "up to 100" per batch in half a second.
Tools and files named: `CLAUDE.md`, MCP, GitHub Actions, Figma, sub-agents (two, in the marketing workflow).
Caveats: Dated 2025-07. Self-reported time savings, no method given. One-shot prompting "without understanding the code themselves" is described for throwaway visualisations only.
Relevance: medium. Shows the baseline habits (discovery first, TDD with check-ins, runbooks as context); the 2026 articles supersede it on review and CI.

### How Block orchestrates Claude Fable across thousands of pull requests (interview with Bradley Axen, Block, 2026-10-08)
File: resources-articles-how-block-orchestrates-claude-fable-across-thousands-of-pull   URL: https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
Thesis: Block uses the most capable model as an orchestrator for migrations of hundreds or thousands of PRs and routes the edits to cheaper models. Merges to main and deploys stay with people, behind two human approvals and non-model checks.
Practices:
- Orchestrator and workers: the frontier model does "data models, API specs, algorithms" and "directs up to dozens of smaller, more cost-effective models like Opus or Sonnet to do the individual tasks, such as making the actual file edits and running tests." ("As frontier intelligence evolves...")
- Model choice is no longer always the biggest model: "the first time I can remember since we started using LLMs for code where the answer wasn't just \"use the most frontier model 100% of the time.\"" ("When do you use Claude Fable models over other options?")
- Benchmark model and effort as a grid: "Every single use case we benchmark, we check not just every model but every effort level of every model." Stated aim is a clear default such as "Use this model on high as the default for this kind of task." ("Do you advise specific optimization strategies, like effort levels?")
- Scheduled debt passes: "agents that do daily or weekly passes across a whole codebase asking, \"How's it going in here? What do we need to clean up and consolidate?\"" ("What's the hardest problem you've thrown at Fable?")
- Hard human gates: "We always leave merges to main and deploys to production up to people, along with related changes like feature flags." Changes pass security checks, "and then two humans have to approve the deploy." ("How are you thinking about incorporating safeguards...")
- Secure by default: "a network allow list instead of a deny list"; remote workstations because they are easier to secure. (same section)
- Guardrails outside the model: "A lot of our security guardrails are really cheap, efficient checks that run without the model needing to be involved ... Sometimes it's even a regex." Small classifiers are increasingly used. (same section)
- Deliberately allowed without blocking: opening PRs, reviewing code, querying logging systems and analytical databases. (same section)
- Skills as personal then shared knowledge: local skills let the interviewee work in an unfamiliar front end; "Organizational maturity comes when all of this context and organizational knowledge is remembered at a system level, not an individual level." ("Any advice for other engineering teams...")
Evidence and numbers: "we might merge a thousand pull requests orchestrated by Fable" in one migration; "45 agents working with you all the time" (illustrative); codebase "in the neighborhood of a million lines". No measured before/after; cost claim is "Early results" with no figure.
Tools and files named: Claude Fable 5 (5.1 in the footer), Claude Opus 5, Sonnet, Buzz (Block's open-source human-agent workspace), a model auto-selector under construction, skills.
Caveats: "Using Fable to fix a typo in a README is a very bad use of resources." In 2025, AI migrations "rarely panned out". "we're not ready to let LLMs loose on our codebase." The speaker notes tech debt accumulates faster with more PRs.
Relevance: high. Model and effort routing, regex-level guardrails outside the model, human-only merge and deploy, and a scheduled cleanup pass all work for one person across a dozen repositories.

### How Brex improves code quality and productivity with Claude Code (Anthropic, 2025-10-30)
File: resources-articles-how-brex-improves-code-quality-and-productivity-with-claude-c   URL: https://claude.com/resources/articles/how-brex-improves-code-quality-and-productivity-with-claude-code
Thesis: Brex engineers, a content designer and the data team use Claude Code; the engineering lead frames the gain as better problem refinement, not time saved.
Practices:
- A `CLAUDE.md` per major directory: "Each major directory in the monorepo now has its own CLAUDE.md file containing domain-specific context." ("Scaling Claude Code best practices across the company")
- Documentation drift check in CI: the team "implemented CI/CD checks that verify when code changes might outdate documentation, prompting updates." (same section)
- Commands that gather context first: "The /submit-pr command, for instance, fetches git status, recent changes, and related PR information before executing." (same section)
- Explore alternatives instead of saving time: "You can try three approaches for the same problem during the same amount of time, and after the third approach, you have a much clearer understanding and a much cleaner interface." ("Adopting a mindset shift with agentic coding")
- Role change: "Instead of being in the driver's seat, you're the reviewer of the changes that Claude introduces." (same section)
Evidence and numbers: "3-4x improvements on specific tasks" (self-reported); "a 4x speed increase across maybe 2x more people that are contributing"; "50% adoption across the org"; a design-system content project done "in a few days" instead of weeks or months.
Tools and files named: `CLAUDE.md`, `/submit-pr` custom command, headless mode, MCP servers, Brex Explorer (text-to-SQL), Kotlin and Bazel monorepo.
Caveats: Dated 2025-10. The lead says "I don't think I save time using Claude Code". Links to a later Claude Code team post on review ("How the Claude Code team does code review", claude.dev) that is not in this batch.
Relevance: medium. Per-directory instruction files, a docs-drift CI check and context-loading commands are cheap and directly copyable.

### How CodeRabbit used Claude to build an agent orchestration system (Anthropic, 2026-05-27)
File: resources-articles-how-coderabbit-used-claude-to-build-an-agent-orchestration-sy   URL: https://claude.com/resources/articles/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
Thesis: The most common failure CodeRabbit sees in AI-written PRs is code that compiles and passes tests but does not do what was meant. Their answer is a planning layer before code generation that makes assumptions explicit and produces a reviewable PRD.
Practices:
- The failure mode: across customers, "the most frequent failure mode was code that compiled and passed tests, yet still didn't solve the problem it was built to solve." ("Addressing the internal knowledge gap in AI coding")
- Cause: unstated requirements. Example: a memory system built for hours with no login page because the author "never said users needed a way to sign in." (same section)
- "In AI workflows, late validation can be very expensive." (same section)
- The planning layer sits above Plan Mode: "It's a higher level orchestration that happens before Claude Code". Output is a PRD; "Claude Code picks up that plan and uses it to generate a fine-grained implementation plan." ("An orchestration layer that runs before AI coding solutions")
- Plan granularity: "Plans that were too granular went stale the moment the codebase shifted. Plans that were too high-level left room for the agent to fill in assumptions". ("Building an eval harness for plan quality")
- Evaluating plans: a library of LLM judges per quality dimension, plus downstream measures (does the code work, "whether it contained extra scope, and how many tokens it took"), and "Running the same task with and without the planning step". (same section)
- Model routing by evidence: Opus drives orchestration, Sonnet sequences steps, Haiku does context distillation and targeted tool use. "If Haiku does as well as Sonnet on a given task, we use Haiku ... We don't guess." ("Routing across the Claude model family")
- Prompts to run on a plan: "what is missing? Are there any parts of the plan that are coming out as implicit assumptions instead of explicit specifications?" (best-practices table)
- Keep "a record of work: a chronicle of planning artifacts that is saved and reused." (best-practices table)
Evidence and numbers: CodeRabbit "Reviews 2 million PRs per week across 15,000+ customers" (scale of the observation base). No measured effect of the planning layer is given.
Tools and files named: Claude Platform, Claude Code, Plan Mode, PRD, Opus / Sonnet / Haiku, LLM judges.
Caveats: The claim "planning quality determines output quality" is introduced as "The team's working thesis". The vendor sells this planning product. The term "MPP (maximum possible product)" is used without definition.
Relevance: high. Supports a spec step whose job is surfacing implicit assumptions, pitched between too granular and too vague, and it names code that passes tests but builds the wrong thing as the dominant failure.

### How Curative is building a national provider network with agents on Claude (Camy Pearson and Michael Segner, Anthropic, 2026-11-10)
File: resources-articles-how-curative-is-building-a-national-provider-network-with-age   URL: https://claude.com/resources/articles/how-curative-is-building-a-national-provider-network-with-agents-on-claude
Thesis: A health insurer runs a contract-negotiation agent ("Gwen") surrounded by cheaper reviewer agents and a human for non-standard cases. It is a business-process agent, not a coding agent, but its control and improvement patterns transfer.
Practices:
- One general tool beats many specific ones: "the model just has one tool, which is run Python, and it does all the redlining with a docx library." ("What Curative learned ...", "Start with one general tool")
- Isolate runs: "One Gwen run sees one provider and keeps no memory across deals." Memory in the other agent "needs care": "You can end up making notes that are wrong and then get into these doom loops, where it has a bad memory that can never be cleared". ("Keep each run isolated")
- Improvement from outside the run: "Every few days, Fred gives Claude Code the same prompt: sample the last 10,000 runs, flag anything weird, and open a PR to fix it." ("Improve the system from outside the run")
- A cheaper second agent as gate instead of more authority: "Having a second agent review rates worked better than just giving Gwen more authority". The Sonnet reviewer clears about two-thirds; the rest go to the CEO. ("Gwen: the provider contracts agent")
- Outbound gate: a Haiku judge "reads every communication before it's sent", added after the agent "copied providers on internal notes about how high it could go." A blocked message returns with the reason so the agent can rewrite. (same section)
- Start with less authority: "Less than you think it can handle." Limits were loosened in steps. (best-practices table)
- Auditing volume: "Log everything, put a judge agent on every outbound message, and have Claude Code sample the runs." (best-practices table)
- Trial in low-risk data first: the agent was barred from PHI for a long time; "We learned how to do it there and then transferred it over into PHI land". ("Experiment away from PHI first")
- Watch emergent behaviour: the agent made a flyer with its Python tool "with no policy telling it to." ("Watch what the agent starts doing on its own ...")
Evidence and numbers: 2,000 to 2,400 contracts a week versus 2,100 in all of 2025 (about 50 times faster); 23,000 contracts signed; about 20 million tokens per contract, "roughly a tenth of the original cost"; rate reviewer clears about two-thirds; a fax tool "more than doubled Gwen's win rate"; contracting team 45 to about 55, "each about 2.5 times as productive"; disputes answered in under 30 minutes versus about 90 days; internal systems rebuilt by 13 engineers with Claude Code, once sized at "100 engineer-years" for the claims system alone.
Tools and files named: Claude Opus (Gwen, Brad), Sonnet (rate reviewer), Haiku (message judge), Claude Code, MCP, Python `docx` library, fax tool.
Caveats: Company-reported figures. "The bar isn't perfect" (the comparison is to human error rates). Agent memory produced "doom loops".
Relevance: medium. Not about coding, but sampling recent runs every few days, flagging anything odd and opening a PR, and a cheap judge on every outbound action, are directly copyable.

### How Datadog built a "universal machine tool" for Claude Code (Michael Segner, Anthropic, 2026-07-21)
File: resources-articles-how-datadog-built-a-universal-machine-tool-for-claude-code   URL: https://claude.com/resources/articles/how-datadog-built-a-universal-machine-tool-for-claude-code
Thesis: Datadog treats verification, not generation, as the bottleneck. Its Temper kernel has agents emit specifications (state machines, data contracts, authorisation policy) that a deterministic kernel verifies through four layers and then runs, so what is proved is what executes.
Practices:
- "Assume verification" is the bottleneck: "the gap between what's generated and what's proven is where the failure modes pile up. Invest there, not in more throughput." (best-practices table)
- Agents emit "Specs for control logic (not code)"; "Put compilation and proof outside the LLM". (best-practices table)
- Three contracts per capability: behaviour (states, transitions, preconditions, safety properties), data contract (machine-parseable, so "an agent can discover the full API without documentation"), and authorisation: "default-deny, scope-based approval, with denials recorded as pending decisions a human can approve and hot-load into the policy engine." ("Temper")
- Four verification layers: symbolic reasoning, exhaustive state exploration, deterministic simulation "with seeded fault injection — drops, delays, reordering, crashes", and randomised property testing of "about a thousand pseudorandom action sequences". ("Temper")
- Make the state machine explicit data: in normal CRUD apps "the operational mode, which generally takes the form of a state machine, is implicit in the codebase". ("Why not just build a CRUD app?")
- Keep artefacts small: "each artifact should be small enough to fit in your head." ("Where this is going")
- Raise rigour where mistakes are costly: they "identified the parts where mistakes would be expensive or hard to reverse, and raised the rigor [there]." (saved text has an escaped bracket; "The road to Temper")
- Long sessions make agents invent "its own tools, its own glue code, and its own conventions"; the response is a shared constrained runtime for agent-built tools. ("The flow problem")
Evidence and numbers: all Datadog engineers use AI coding tools for production code and "Claude Code drives at least two-thirds of that"; a protobuf parser refactor in three days; a metrics control rewrite from FoundationDB to Postgres in under three months; Courier took one year by hand (2024); Helix, a Kafka-comparable service, was functional "in a few days" with one human steering, with shadowing showing it "could be 2x to 5x cheaper"; the verification cascade on a small spec runs "in well under a second".
Tools and files named: Temper (`github.com/nerdsane/temper`), Courier, BitsEvolve, Helix, Claude Managed Agents, "dark factory" (term attributed to Simon Willison).
Caveats: Helix's production hardening "only earned over time and by more than one person and this is still in the process of rolling out". The role change is described as being "promoted three levels up into the management chain, which they didn't sign up for".
Relevance: medium. Temper itself is scale-only, but its lessons are not: spend on verification, make state machines explicit and property-test them, default-deny with a pending-approval queue.

### Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5 (interview with Vladislav Tankov, JetBrains, 2026-08-13)
File: resources-articles-how-jetbrains-evaluates-and-deploys-claude-fable-5   URL: https://claude.com/resources/articles/how-jetbrains-evaluates-and-deploys-claude-fable-5
Thesis: JetBrains evaluates models on private repositories, not public benchmarks, and keeps three leaderboards (quality, cost per task, speed).
Practices:
- Evaluate on private code because "some models are tuned to score well on public benchmarks but fall down on actual tasks." ("How do you evaluate new models ...")
- Measure cost per task, not per token: the dearer model's "cost per task is lower in some cases, particularly for more complicated, long-running work." (same section)
- Model split: "Opus is seen as a workhorse"; the top model is for when "you're not sure yourself how to do the thing." ("When do you use Claude Fable 5 over other models?")
- Black-box rewrite: an agent generates specifications (text and images) from an existing app, and another implements from them. (same section)
- Safety at the deployment layer: "creating the infrastructure and the safety net around the model and the harness, rather than tweaking the model itself." ("How are you thinking about safety and data retention ...")
Evidence and numbers: Python pass rate 44.3% (Fable 5) against 28.2% (Opus 4.8); head to head, 18 tasks solved that Opus 4.8 missed and 2 lost; about 22% fewer steps; 12.5 million active users (company scale).
Tools and files named: Claude Fable 5, Opus 4.8, internal eval pipeline and leaderboards.
Caveats: "code that runs but produces wrong answers is the most expensive kind of failure to catch." Absolute pass rates under 50% on their suite. Mostly a model endorsement.
Relevance: low to medium. The one transferable idea is a small private eval set scored on quality, cost per task and speed when choosing a default model.

### How Warp builds self-improving agents on Claude (Michael Segner, Anthropic, 2026-08-26)
File: resources-articles-how-warp-builds-self-improving-agents-on-claude   URL: https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude
Thesis: Feedback to an agent normally vanishes when the session ends. Warp pairs each task skill (inner) with a scheduled improver skill (outer) that reads accumulated human feedback and proposes a small edit to the inner skill as a PR a human merges.
Practices:
- The diagnosis: feedback "typically disappears when the session ends". Manual prompt rewrites "didn't scale"; improving `AGENTS.md` "helped, but was far from a complete fix." (introduction)
- Outer skill behaviour: it "runs on a schedule rather than per-task. It pulls the accumulated human feedback, compares what the agent suggested against how humans responded, and proposes a small, focused edit to the base skill." ("Agent self-improvement loops built on skills")
- Updates go through normal review: they "can flow through a normal PR/code-review workflow; once merged, the next run of the inner skill inherits the improvement." (same section)
- "Write principles, not rules": "Construct the skill as though you're instructing a smart person, not like you're programming a computer". ("How to write self-improving skills for agents")
- "Explain the why", so the agent can generalise. (same section)
- "Make feedback effortless to give": capture it where the work is (a PR or issue comment) with no extra step. (same section)
- "Keep skills small and use progressive disclosure": the skill "references resource files and scripts rather than dumping everything into context at once." (same section)
- Bundle a script with the skill: the improver "ran a Python script bundled with the skill to pull recent issues carrying feedback, summarized them into a JSON file, and read that back into context." ("The loop in action: Warp's issue triage agent")
- The improver PR comes "with a description explaining which signals prompted the change and what it altered." (same section)
- Skills versus memory: "Skills are procedural and stable—\"how to do X,\" run-agnostic, changed deliberately. Memory is auto-written by the agent at inference time and never stops changing." (best-practices table)
- Wrong feedback: "Assume it will be. Don't let the agent accept feedback blindly"; filter whose input counts and keep a human at filtering or final review. (best-practices table)
- Verifiable domains: "Build the verification harness first, then let the agent tune against it". Otherwise use "deterministic evals against golden outputs wherever they exist." (best-practices table)
- Track whether the system improves with global metrics: "time to merge, contributor count, cost". (best-practices table)
Evidence and numbers: company scale only (800K monthly developers; "10M Claude Code sessions run inside Warp to date, 400K+ per week"); "hundreds of people contributing and we're doing thousands of code reviews". No measured improvement from the loop is reported. The triage example fixed one missed label ("ready to spec").
Tools and files named: Agent Skills, `AGENTS.md`, GitHub Actions, Oz (Warp's orchestration platform), `github.com/warpdotdev/warp-agents-demo-github-issue-triage`, labels such as "ready to spec".
Caveats: "A first-pass prompt that gets 80% of the task correct can create a noisy and annoying experience". Warp sells the orchestration platform. Binary thumbs up or down "doesn't say why".
Relevance: high. The two-skill loop needs only skill files, a scheduled run and a PR, and the feedback source for a solo developer is their own review comments.

### How to prepare for AI-driven code modernization projects (Jonah Ezekiel and Lexie Tonelli, Anthropic forward deployed engineers, 2026-09-23)
File: resources-articles-how-to-prepare-for-ai-driven-code-modernization-projects   URL: https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
Thesis: Once agents write the changes, "the bottleneck shifts from producing changes to mobilizing the organization around them." Before running a modernization, write down the target, a machine-checkable "certificate" of correctness, and a tiered "promotion policy" for human review.
Practices:
- Six steps: define the target; create the certificate; set the promotion policy; put prerequisites in place; build and refine the agentic workflow; run on a small partition, then scale. (introduction list)
- Decide the type up front (uplift, transform or reimagine). Left unresolved, the question "resurfaces later as an argument over whether a given change is \"correct.\"" ("Determine the modernization type")
- Certificate: "the set of conditions or tests that every modernization change must meet." Each condition "should be checkable without a human in the loop, so the agentic workflow can iterate on a change until it meets the certificate or flag it for human review if it can't." ("Step 2: Define the certificate")
- Candidate certificate items (same section): original test suite passes; Claude-authored tests pass; coverage threshold; performance within a bound; "Independent adversarial reviews by Claude, each in a fresh context window, find no blocking issues"; computer-use checks for UI regressions; same output from same input (live, recorded or generated); persisted state and wire formats round-trip; a staging soak with no regression in error rates, latency or alerts; no new static-analysis or security findings; clean build and type checks.
- Test of a good certificate: whether the reviewers "would be comfortable merging on the certificate's evidence alone." (same section)
- Weak evidence: "use Claude to build the missing evidence, whether that's standing up a prod-parallel setup, building a replay harness, or writing more tests." (same section)
- Promotion policy rules: "Tier changes by blast radius and agent confidence"; "Fix recurring flags at the source"; "Design the output format with the reviewers"; point experts "straight to the changes in the highest-risk tiers, and to the flagged agent decisions within each one, without wading through large diffs." ("Step 3: Set the promotion policy")
- Review moves to the front: expert feedback on samples tunes the certificate and workflow before the full run, "the reverse of the traditional, non-agentic pattern, where review happens at the end." (same section)
- Security prerequisites: "Least-privilege access for the agentic workflow: write only to modernization branches and no production credentials"; "Secrets and PII scrubbed or masked from the modernization branch"; "Every change traceable and PR linked to an agent transcript and certificate evidence"; "License and vulnerability checks on new dependencies". ("Security and compliance")
- In-place modernisation: split "into logical partitions from the leaves inward", freeze and modernise one partition at a time, and gate CI/CD "so new commits cannot undo a partition once it has been modernized." ("Step 6: Run the modernization")
- Cost control: "Move compute-heavy verification signals behind cheaper gates so they only run once easier checks have passed." Use a mid-tier model for mechanical work the certificate fully checks; keep stronger models for hard transformations and adversarial review. ("A note on cost")
- Escalation caveat: "several cheap attempts can cost more than one expensive one", so measure retry rates in the pilot. ("A note on cost")
Evidence and numbers: none measured. Qualitative: "verification, not writing the change, is usually the larger share" of token cost in a regulated environment.
Tools and files named: code modernization plugin (`anthropics/claude-plugins-official`, commands `assess`, `map`, `extract-rules`), dynamic workflows, MCP, a dedicated remote host.
Caveats: Written for regulated enterprises. Reimagine projects are "the hardest case" because a spec "is less objective than an existing system to diff against". Budgets "are still hard to estimate". The saved text lacks the table of modernisation types that the article refers to.
Relevance: medium to high. "certificate" and "promotion policy" are a compact vocabulary for a solo developer's definition of done and for deciding how much of a diff to read per risk tier.

### Introduction to agentic coding (Anthropic, 2025-10-30)
File: resources-articles-introduction-to-agentic-coding   URL: https://claude.com/resources/articles/introduction-to-agentic-coding
Beginner explainer of agentic coding versus autocomplete and chat, with installation steps. Repeats Rakuten figures ("79% faster feature delivery (24 days → 5 days)", seven-hour autonomous run, 99.9% accuracy, "5x parallel task execution capacity"). Only setup-relevant line: `CLAUDE.md` files "document your coding standards, architectural decisions, and project-specific requirements" and persist across sessions.
Relevance: low. Old (2025-10) and introductory.

### What are the key benefits of transitioning to agentic coding for software development? (Guy Gur-Ari of Augment Code is credited; 2025-12-01)
File: resources-articles-key-benefits-transitioning-agentic-coding   URL: https://claude.com/resources/articles/key-benefits-transitioning-agentic-coding
Marketing piece listing benefits (speed, onboarding, quality, scaling without headcount). Claims are unmeasured assertions, for example onboarding "drops from weeks to one or two days" and ten engineers doing the work of "twenty or thirty". One anecdote: an Augment Code customer finished in two weeks a project estimated at four to eight months.
Relevance: low. No practices; treat the figures as promotional.

### Preview, review, and merge with Claude Code (Anthropic, 2026-02-20)
File: resources-articles-preview-review-and-merge-with-claude-code   URL: https://claude.com/resources/articles/preview-review-and-merge-with-claude-code
Thesis: Product note for Claude Code on desktop: preview a running app, review local diffs before pushing, watch a PR's CI, auto-fix failures and optionally auto-merge.
Practices:
- Verify UI by running it: Claude can "start dev servers and preview your running app", then "views the webapp UI, reads console logs, catches errors, and keeps iterating". ("Write code and see it run")
- Review before push: a "Review code" action "examines your local diffs and leaves comments directly in the desktop diff view", "before anything leaves your machine". ("Review code before you push")
- PR babysitting: after a PR opens, Claude tracks CI "using the GitHub CLI under the hood"; auto-fix attempts CI fixes; "If you enable auto-merge, Claude will also attempt to merge PRs once all checks pass." ("Monitor PRs without leaving the app")
- Move a session between surfaces with `/desktop` or "Continue with Claude Code on the web". ("Pick up where you left off")
Evidence and numbers: none.
Tools and files named: Claude Code on desktop, `/desktop`, GitHub CLI, auto-fix, auto-merge.
Caveats: Auto-merge after green checks conflicts with the human-approval rule stated in the Anthropic CI, security and Block articles; here it is an opt-in feature with no guidance on when it is safe.
Relevance: medium. Available to all users; local pre-push review and a background CI watcher fit a solo workflow.

### Product development in the agentic era (Jess Yan, Anthropic product manager, 2026-04-29)
File: resources-articles-product-development-in-the-agentic-era   URL: https://claude.com/resources/articles/product-development-in-the-agentic-era
A product manager's account of prototyping against pre-release API specs and building small cloud agents (adoption analytics with memory of prior runs, developer-sentiment monitoring that fans out to parallel agents, demo building). The one transferable point: "A spec that reads elegantly in a doc can fall apart the first time you try to build against it", so build a prototype against the spec within an afternoon. Names the built-in `claude-api` skill.
Relevance: low. Mostly a Managed Agents promotion.

### Product management on the AI exponential (Cat Wu, Head of Product for Claude Code, 2026-03-19)
File: resources-articles-product-management-on-the-ai-exponential   URL: https://claude.com/resources/articles/product-management-on-the-ai-exponential
Thesis: Because model capability changes mid-project, the Claude Code team plans in short sprints, prefers demos and evals to documents, revisits features at each model release, and keeps implementations simple so scaffolding can be deleted.
Practices:
- Side quests instead of a long roadmap: "A side quest is a short self-directed experiment you run outside your official roadmap". Claude Code on Desktop, the AskUserQuestion tool and todo lists came from them. ("Plan in short sprints")
- Demos over stand-ups and docs: "Instead of hosting traditional stand-ups, we share demos of new ideas." "Because you can prototype in an afternoon, wrong bets are cheap." ("Encourage demos and evals over docs")
- Test a spec by building it: "after you write a spec, send it to Claude Code and see if it can build it. Even a rough prototype changes the conversation." (same section)
- Hand-crafted evals for a feature: for agent teams a colleague "hand-crafted a set of evals to understand when agent teams work well, when they don't, and what to fix." (same section)
- Re-test at each model release: "Every model release is an implicit prompt to revisit what you've already built." Keep a personal hard task (hers: add a table tool to Excalidraw) and re-run it. ("Revisit features with new models", introduction)
- "If users are hacking something together, that's scaffolding you can build into the product." (same section)
- Capability before cost: "It's a common mistake to cut token costs too early and ship something much less capable as a result." (same section)
- "do the simple thing that works": "If your product cleverly works around a model limitation, that workaround becomes unnecessary complexity when the next model drops." ("Do the simple thing")
- Example of scaffolding removed: system reminders that nudged the agent to update its todo list were deleted when the next model did it unprompted. (same section)
Evidence and numbers: METR time horizon about 21 minutes (Sonnet 3.5 new) to almost 12 hours (Opus 4.6), "a roughly 41x jump in 16 months"; system prompt and tool descriptions cut with each model, "including a 20% reduction for Opus 4.6".
Tools and files named: Claude.ai, Claude Code, Cowork, AskUserQuestion tool, todo lists, plugins, agent teams, Claude Code with Chrome.
Caveats: Written from a product-management seat at a model vendor; the advice to spend tokens freely suits Anthropic more than a cost-sensitive individual. Dated 2026-03 (Opus 4.6).
Relevance: high for one principle: instructions and hooks that compensate for a model weakness should be few, simple and re-tested at each model release.

### Running an AI-native engineering org (Fiona Fung, Director of Engineering for Claude Code and Claude Cowork, 2026-06-03)
File: resources-articles-running-an-ai-native-engineering-org   URL: https://claude.com/resources/articles/running-an-ai-native-engineering-org
Thesis: When coding stopped being the constraint on the Claude Code team, "Verification, code review, and security took their place", and four norms were rewritten: planning, context gathering, code review and team make-up.
Practices:
- Just-in-time planning: a six-month roadmap "was out of date by month three". Now: "Our planning ritual shifted away from design docs toward discussions in PRs or prototypes." ("Planning: shift roadmaps to just in time")
- Process is "let's prototype, get a lot of internal users on it, and start acting on their feedback." (same section)
- Ask Claude before asking the author, and ask "Is there a way to automate it?" Example: "having Claude summarize customer feedback channels every morning" runs automatically in the background. ("Context gathering: ask Claude, not the author")
- Code review split: "Claude handles all the style and linting, PR feedback requests, catching bugs and fixing them before a full commit, and adding tests. Where we still definitely want a human is expertise." ("Code review: trust but verify")
- Humans review "trust boundaries and security-sensitive code", legal risk, and product sense and taste. (same section)
- Re-evaluate the split: "the right balance of trust vs. verify will keep changing as the models improve." (same section)
- "Don't hesitate to kill processes that no longer work"; team members "have explicit permission to question and kill old processes." ("How we rolled out our new norms")
- Three numbers to track: onboarding ramp time, PR cycle time, Claude-assisted commits. ("How to know your new processes are sticking")
- "don't confuse throughput with success." (same section)
- Starting point: "pick your noisiest workflow" and ask whether it still serves its purpose and whether it can be automated. ("Getting started")
Evidence and numbers: engineers "ship real code now within their first week"; "I don't think I've seen a non-Claude-assisted commit in the last four months." No rates or counts.
Tools and files named: Code Review, Claude Code, Claude Cowork, Claude Code on the Web.
Caveats: PR cycle time may reveal that "build systems and continuous integration (CI) may struggle to keep up." Based on a conference talk; describes one team inside Anthropic.
Relevance: high. States plainly where the bottleneck moved, what stays with humans in review, and the habit of deleting processes.

### How to scale agentic coding across your engineering organization (Anthropic, 2025-10-15)
File: resources-articles-scaling-agentic-coding   URL: https://claude.com/resources/articles/scaling-agentic-coding
Thesis: Rollout advice for engineering leaders (pilot group, hackathon, internal champions), plus `CLAUDE.md` hygiene and prompting habits. Old and generic, but its task-scoping advice is concrete.
Practices:
- Pilot outputs worth having: "custom slash commands for common tasks like database migrations or feature scaffolding", `CLAUDE.md` files, and "wrapper scripts for third-party tool authentication". ("Start with super users")
- `CLAUDE.md`: check it into the repository root; "Update CLAUDE.md files when architectural decisions change or new patterns emerge. Include these updates in pull requests alongside code changes." ("Using CLAUDE.md files effectively")
- Scope with tests: "Start by writing tests that define what success looks like", then implement "just enough code to make one test pass at a time"; "Run tests after each step and review the changes before proceeding." ("Scope tasks appropriately")
- Two-step prompt: "write tests for user registration" followed by "implement the registration logic to pass these tests". (same section)
- Bug reports to the agent: full error and stack trace, environment, screenshot for UI, and "Expected: API returns 200 status with user data. Actual: Returns 401 with 'invalid token' message." ("Provide adequate context")
- Quantified goals: "Optimize the database query to reduce response time from 2 seconds to under 500ms" instead of "make it faster". ("Develop effective prompting habits")
- Show an existing pattern to follow, and "Break complex work into sequential prompts". (same section)
Evidence and numbers: none measured; pilot size "20-50 developers" is a recommendation.
Tools and files named: `CLAUDE.md`, custom slash commands, Activity Metrics.
Caveats: Dated 2025-10. Lines of code "captures activity but not necessarily value". The FAQ at the end is boilerplate and partly wrong for Claude Code (it describes generic text generation).
Relevance: low to medium. Superseded by the 2026-08 SDLC playbook, which keeps the test-first advice and adds enforcement.

### The AI-native SDLC playbook (Louis Claxton, Anthropic Applied AI, 2026-08-21)
File: resources-articles-the-ai-native-sdlc-playbook   URL: https://claude.com/resources/articles/the-ai-native-sdlc-playbook
Thesis: When code is no longer the bottleneck, the constraint moves to plan, review/test and deploy. The playbook rebuilds the lifecycle as a loop of six stages (Plan, Design, Build, Test, Deploy, Maintain) in which each stage ends by committing an artefact that the next stage reads, with humans at the gates.
Practices:
- The committed artefact chain: "Each stage ends by writing one to version control (including `intent.md`, `spec.md`, `plan.md`, the diff and its tests, the PR with its review findings, and the incident record) and the next stage begins by reading it." ("The shifts across the six stages of an AI-native SDLC")
- Triggers: "An accepted `intent.md` triggers the requirements and design pass, an approved `spec.md` triggers plan mode, a merged PR triggers the pipeline, and a breached control band in production writes the next `intent.md`". ("Plays")
- Start by prompting each step by hand; automate the hand-offs later. "Human attention concentrates at the gates, reviewing what the agent flagged". ("Plays")
- Plan, `intent.md`: describe the problem in your own words, then Claude "asks the questions an analyst would ask: scope, users, constraints, and what success looks like", then write `intent.md` from a template held as a skill. Sections in the example: Problem, Proposed outcome, Affected users and systems, Constraints, Open questions. ("Capture as intent.md")
- Design, `spec.md`: Claude writes the requirements and design spec from the accepted intent with organisation skills loaded; the owner "reviews that spec, but doesn't write it." The prompt ends: "Describe clearly any areas of concern, especially where you cannot satisfy contradicting policies." Flagged concerns are worked through first. ("Requirements and design")
- Run it by hand, "then codify it as an organization-level slash command", then trigger it on merge of the intent. (same section)
- Build, plan mode: give Claude `intent.md` and `spec.md` and ask for "an implementation plan that names the files that change, the order of the work, and the tests that prove it." Interrogate it: "what the change could break, which step is most risky, and what other options Claude chose not to do." ("Claude Code plan mode as the default starting point")
- Plan quality bar: "Iterate until an engineer who has never seen the conversation could implement the change from the plan alone." Commit as `plan.md` (example sections: Files that change, Order of work, Risks, Proof). (same section)
- Keep plan and code in sync: "When implementation departs from the plan, update `plan.md` in the same commit. Consider using a hook to enforce synchronization". (same section)
- Auto mode becomes the default for routine work once guardrails exist: "a tight `spec.md`, a small blast radius, and code the tests already cover." Review shifts from watching edits to "review of artifacts after longer autonomous sessions." ("Claude Code on auto mode")
- `CLAUDE.md`: run `/init`, then cut to what a new joiner needs; "When Claude makes a mistake twice, the correction goes into `CLAUDE.md`."; "Keep it under a page, because Claude reads all of it at the start of a session and anything stale is taking up context for no benefit." Example sections: Commands, Conventions, Architecture, Things Claude gets wrong. ("The CLAUDE.md")
- Skills: "write a skill for institutional knowledge that must be applied consistently; don't write a skill for components that belong in `CLAUDE.md` or a prompt." Location `.claude/skills/<name>/`; test that it triggers by asking for the task in different ways. ("Skills as institutional knowledge")
- Skill versus hook: "A skill is a control, though an advisory one." "The skill makes violations rare and the hook makes them close to impossible." (same section, "Governance considerations")
- Build-phase hooks: "Block edits to protected paths such as generated classes or a frozen package"; "Run the formatter and linter after file edits so drift never accumulates"; "Keep credentials out of the diff." They "should be fast and scoped to the file that changed. Heavier checks such as the full test suite belong at the commit or the PR." ("Hooks as build-time guardrails")
- No approval prompts in the build: "an approval prompt during the build puts a person back on the critical path of all the sessions running in parallel." (same section)
- Parallel sessions: split work into tasks touching different files; each gets a worktree, e.g. `claude --worktree feature-auth`. "Two or three sessions is a sensible starting point. The practical ceiling is how many streams one person can review properly". ("Parallel sessions and subagents")
- Subagents for repeated jobs in `.claude/agents/`: "a code simplifier", "a verifier that runs the app and checks behavior", "a researcher that explores the codebase and reports back without flooding the main context." The example verifier ends "Do not fix anything; report only." (same section)
- Test, feedback loop: wrap verification in one command that "exits non-zero on failure"; list each command in `CLAUDE.md` "with an example of a healthy output"; state a quantifiable target. ("Give Claude a feedback loop")
- Bug fixes: failing test first, confirm it "fails for the reason you expect", commit it, then fix "without editing the test". "A test that existed before the fix, and that the agent couldn't rewrite, is proof the bug is gone." (same section)
- UI: "Implement, screenshot, compare, and adjust. Two or three rounds is normal". (same section)
- Protect the check: "an agent fixing code must not be able to weaken the check on that code. A hook that blocks edits to test files during a fix task does this." Sample `CLAUDE.md` block: "If a test fails, fix the code, not the test." (same section)
- Feedback loop versus verifier subagent: the verifier runs "a fresh context window once the session believes the work is done. This way the verdict is not colored by the assumptions that produced the code." (same section)
- Continuous evals: "20 to 50 real tasks from recent work" with expected outcome; run "on a schedule and on any change to `CLAUDE.md`, skills or hooks, since that configuration steers the agent and deserves the regression testing that code gets." "Each production incident gets an eval". ("Continuous evals in CI")
- Deploy, PR review: `REVIEW.md` at the repo root, "divided into the passes the organization cares about: bugs and logical errors; security and vulnerabilities; compliance against the spec"; it "also defines what counts as Important as opposed to a Nit, and what to skip." ("AI in the PR review loop")
- Sample `REVIEW.md` calibration: "Reserve Important for findings that would break behavior, leak data or breach a policy. Style and naming are nits." and "Report at most five nits per review; summarize the rest as a count." (same section, "What it looks like (REVIEW.md)")
- Human threshold: "Findings do not approve or block a PR on their own, and branch protection still requires approval from a code owner." "the agent that wrote the code has no way to approve it." (same section)
- Babysit loop: a custom slash command "sweeps the unresolved review comments and failing checks on the PR, addresses them and pushes the fixes, until the PR is green and waiting only on code owner approval." (same section)
- Review feeds instructions: "When a review flags a mistake for the second time, the correction goes into `CLAUDE.md` as part of that review". Monthly tuning: rate findings and cap nit volume. (same section)
- Approval-gate hooks: a PreToolUse hook on Bash that exits 2 when a command contains both "deploy" and "production" without `RELEASE_APPROVAL`. "A block should explain itself, so when a hook stops an action the reason and the route to approval appear in Claude's output." Team hooks in `.claude/settings.json`; non-negotiable ones in managed settings. ("Hooks as approval gates")
- CI/CD: start with read-only `claude -p` steps (triage a failed build, summarise a flaky test, draft the changelog); then write steps behind gates. "Anything the agent writes arrives as a PR through branch protection, and the agent has no route to push to main." ("CI/CD integration and deployment")
- Sandboxing: "Agent jobs run in containers under a network policy with short-lived scoped tokens, and hold no production credentials by default." Deploy, status and rollback exposed as MCP tools so powers are "an allowlist rather than a shell script with credentials." (same section)
- Autonomy by environment: "In development, the agent deploys freely. In production, the agent prepares the release and the release manager authorizes it". Rollback is "a single command" rehearsed in staging. (same section)
- Maintain, closing the loop: a deterministic detection script ("with no model involved") over a rolling baseline; tiers in `bands.yaml`: "At 1σ the script only logs, at 2σ it invokes Claude read-only to diagnose, and at 3σ Claude may act, though only by opening a PR into the review gate or triggering a pre-approved runbook." The diagnosis is written as a new `intent.md`. ("Closing the loop")
- Headless stages need "an independent confidence gate between stages, a deterministic check or an adversarial reviewing agent". ("Maintenance and closing the loop")
- Recurring security scans: "A security scan is a point-in-time statement about a codebase under a particular model, and both halves go stale". Weekly is "a sensible default"; dismiss findings with a reason so they do not return; fixes go through the PR gate. ("Recurring codebase scans")
- Incidents: Claude Tag "writes the post-mortem to a version-controlled lessons file that future investigations can read." ("Claude on call with Claude Tag")
Evidence and numbers: no measured outcomes. Recommended quantities: 20 to 50 eval tasks; two or three parallel sessions to start; `CLAUDE.md` under a page; at most five nits per review; 1σ/2σ/3σ tiers on a 30-day rolling baseline; nightly eval cron (`0 2 * * *`) in the sample workflow.
Tools and files named: `intent.md`, `spec.md`, `plan.md`, `CLAUDE.md`, `REVIEW.md`, `.claude/skills/<name>/SKILL.md`, `.claude/agents/verifier.md`, `.claude/settings.json`, `.claude/hooks/production-gate.sh`, `bands.yaml`, `.github/workflows/agent-evals.yml`, `evals/*.json`, `evals/check.sh`, `/init`, `claude -p`, `--allowedTools`, `--output-format json`, `claude --worktree`, plan mode, auto mode, claude-code-action, Code Review, `@claude` mentions, Claude Design (beta), Claude Security, Claude Tag, MCP, managed settings.
Caveats: Written for large and regulated organisations with separate product owners, tech leads and release managers; the role separation collapses for one person. The saved text has lost the stage comparison table, the dependency graph and the resource list, and the numbered stage headings, so stage membership of some plays is taken from in-text references ("Stage 3: Build", "Stage 5: Deploy"). A skill is advisory: "nothing forces a session to comply with it." Evals go stale: "cases that once discriminated stop doing so". The sample production gate matches substrings in a shell command, which is easy to miss or evade (Inference: it illustrates the mechanism and is not a complete control).
Relevance: high. It is the most complete first-party description of files, hooks, subagents, review policy and eval gates, and almost every play works in a single repository without the organisational roles.

### Using LLMs to secure source code (Eugene Yan and Henna Dattani, Anthropic, 2026-05-27)
File: resources-articles-using-llms-to-secure-source-code   URL: https://claude.com/resources/articles/using-llms-to-secure-source-code
Thesis: Finding vulnerabilities with models is now easy to parallelise; "the bottleneck has shifted to verification, triage, and patching". A six-step loop: threat model, sandbox, discovery, verification, triage, patching.
Practices:
- Threat model first: "The most common cause of false positives is that the model lacks a good understanding of your trust boundaries." ("1. Threat model")
- Build it in two steps: bootstrap from code, docs, git history and past vulnerabilities; then "have the model interview someone who knows the system well" using Shostack's four questions. (same section)
- "Name what is trusted." and "Include a `THREAT_MODEL.md` with the code." so the discovery agent reads it before searching. (same section)
- Sandbox isolation: containers suffice for an agent reading code; run targets and PoCs in a microVM or VM "with egress locked down". "And never have credentials (`~/.aws`, `~/.ssh`, `.env`) available to the agent." ("2. Sandbox")
- Network only during setup: "snapshot the environment and remove its network access. During scanning, allow traffic only to the model API, routed through a local proxy." (same section)
- Pin "image tags, commit SHAs, dependencies, and build commands". (same section)
- Prompts for discovery should be short: "more prescriptive prompts make discovery worse—long checklists tend to reduce the model's creativity and generate fewer novel bugs." Give the why and what, "and leave \"how to scan for vulnerabilities\" to the model." ("3. Discovery")
- Structured output with ordered fields and "an escape hatch so the model can exit early for weak findings." (same section)
- Partition the search space first, fan out parallel agents per partition "so they don't converge on the same shallow bugs", then run a system-level pass. (same section)
- Separate finding from verifying: "Discovery optimizes for recall; verification optimizes for precision." Doing both in one step made agents filter out true positives: "We learned this the hard way". ("4. Verification")
- Verifier independence: "Run the verifier in a fresh container without a shared filesystem or conversation history. If the verifier is exposed to the discovery agent's reasoning, it may simply agree instead of testing the claim." Give it only the finding or PoC and the codebase. (same section)
- Verifier stance: "Have the verifier assume each finding is a false positive and search for reasons the finding is wrong." Multiple verifiers with a majority vote if needed. (same section)
- "failure to produce a working PoC is not proof of a false positive." (same section)
- Triage dedup: first "a cheap deterministic pass: same file, same category, vulnerability line numbers within ten lines of each other", then model rules for duplicate versus distinct. ("5. Triage")
- Severity calibration: rate on reachability, attacker control, preconditions, authentication, read versus write, blast radius; "have the model write out its answer to each question before assigning a severity" so it does not anchor on the bug class. Starting thresholds: "zero preconditions with unauthenticated remote access is critical or high severity. One or two preconditions, or an authenticated path, is medium. Three or more, or local-only, is low." (same section)
- Why triage matters: with inflated or duplicate reports, "product engineers may stop reading them, even the ones that need immediate patching." (same section)
- Patch with a test first: "write a new test that fails with the existing code. Then, implement the fix and confirm the same test now passes". ("6. Patching")
- Root cause and variants: prompt for the root cause, then search "same pattern" and "same class". (same section)
- Minimal patch: "Prompt for the smallest change that fixes the root cause—no refactoring, no drive-by cleanups, no reformatting." (same section)
- Validation ladder, cheapest first: build; try to reproduce; check for regressions; re-attack with a fresh discovery agent. (same section)
- Ownership: "while the model can write the patch, a human still needs to own it." Predictable failures: "fixing the symptom instead of the root cause, blocking legitimate input, or removing access to a dependent service." (same section)
- Budgeting: "Budget for the pipeline after the scan before you budget for more scanning." ("Getting started")
Evidence and numbers: as of 2026-05-22 Anthropic had disclosed 1,596 vulnerabilities in open source software and "97 of these have been patched"; with a sandbox that can compile, test and detonate a PoC, "non-exploitable findings dropped significantly" (no figure).
Tools and files named: `THREAT_MODEL.md`, `github.com/anthropics/defending-code-reference-harness` (skills `threat-model`, `vuln-scan`, `triage`, `patch`, `/quickstart`, `/customize`, `scripts/setup_sandbox.sh`), gVisor, Firecracker, `claude-code-security-review` action, Claude Security, SAST scanners, fuzzers.
Caveats: "don't expect the nth run to have zero new findings. Models are stochastic". A sandbox that omits production defences reports unexploitable findings; one that omits dependencies under-reports. The authors say "we don't have all the answers". Model named is Claude Opus (May 2026); the SDLC playbook (August) names a hosted scanner on a newer model.
Relevance: high. `THREAT_MODEL.md`, a separate disproving verifier, written-out severity reasoning, the patch ladder and the credential rule all apply to a single developer's repositories.

### Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems (Anthropic, 2026-07-17)
File: resources-articles-working-at-the-frontier-cursor   URL: https://claude.com/resources/articles/working-at-the-frontier-cursor
Model-endorsement interview with Cursor's eval engineer Nate Schmidt. Practice content: Cursor built its own benchmark (CursorBench) because "public benchmark scores and real developer reception to these models had stopped lining up"; tasks are deliberately underspecified (a stack trace with the single word "fix"; a task that "tells the model the wrong module is broken, to see whether it challenges the user's assumption"). Model routing rule: "If you have a good sense of what the path from A to B looks like, you might not need Fable. If you're at A and you have no idea where B is, Fable is an excellent choice". One coordination habit: before touching shared code he "has an agent read his teammate's recent commits and flag conflicts". Numbers: 72.9% on CursorBench at Max effort; a simulator task done in "a couple of hours" against twelve-plus hours with no result on the older model.
Relevance: low to medium. Supports routing hard, unclear problems to the strongest model and routine work to cheaper ones, and testing models on messy real prompts.

### Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night (Anthropic, 2026-07-10)
File: resources-articles-working-at-the-frontier-how-cognition-trusts-claude-fable-5-t   URL: https://claude.com/resources/articles/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night
Model-endorsement interview with Silas Alberti (Cognition, Devin). Practice content: benchmarks are distrusted ("we trust no eval"); the "highest-taste developers put each new model through a real day of work, and the bar is whether the code is something they'd actually keep." Their own benchmark, Frontier Code, exists "because existing ones kept rewarding code that passed tests but wouldn't survive a real codebase". Failure modes of earlier models: sessions drifted after "a couple of minutes, maybe an hour"; in triage they would "confidently claim the first plausible thing they discover and then stop." What worked on a migration: the model "stated the invariants it would hold itself to, then executed against them", and in triage "said what it didn't know". Numbers: hardest subset about 10% (prior Opus) to about 30%; one run "working for eight hours straight"; internal usage tripled with Claude 3.6 Sonnet in late 2024.
Relevance: low to medium. Useful as evidence that passing tests is a weak bar and that stating invariants before a migration is worth prompting for.

### Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work (Anthropic, 2026-07-15)
File: resources-articles-working-at-the-frontier-why-base44-trusts-claude-fable-5-with   URL: https://claude.com/resources/articles/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work
Model-endorsement interview with Yoav Orlev (Base44). Practice content: each new model is run "through evals across different app types, measuring latency, cost, and build errors"; a system-prompt rebuild took "about an hour of back-and-forth questions" then four autonomous hours returning "90% to 95% of what they needed", shipped behind A/B tests the same afternoon; the model flagged a gap in their evals (no test for cache hits, although "a prompt change can break the cache"). The team still "reviews, tests, and approves the code before shipping it." Brief a strong model like a senior engineer "on the goal and the why."
Relevance: low. One copyable check: when changing a long system prompt or instruction file, test that prompt caching still hits.

### Zero Trust for AI agents (Anthropic, 2026-05-27)
File: resources-articles-zero-trust-for-ai-agents   URL: https://claude.com/resources/articles/zero-trust-for-ai-agents
Landing page for a longer guide that is not in this batch; it only lists the guide's contents. The framing: "trust nothing, verify everything, and assume breach has already occurred", applied to agents as "identities that are cryptographically rooted, permissions scoped per task, memory protected against poisoning". Threats listed: "prompt injection, tool poisoning, identity and privilege abuse, memory poisoning, and supply chain attacks". Mentions a three-tier framework (Foundation, Advanced, Optimized) and an eight-phase workflow covering "identity, access scoping, sandboxing, input and output controls, and memory safeguards" without detail.
Relevance: low as saved (no controls are described); the full guide at `claude.com/resources/guides/zero-trust-for-ai-agents` would be the source to fetch.

### 2026 agentic coding trends report: Capability trends, what agents can do (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report-capability-trends-what-agents   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report/capability-trends-what-agents-can-do
Thesis: Predictions (January 2026) that single agents become orchestrated teams, task horizons extend to days, and human oversight shifts "from reviewing everything to reviewing what matters".
Practices:
- Orchestrator pattern with specialists in separate context windows (architecture, implementation, testing, review and docs). ("Trend 2")
- What engineers actually delegate: tasks that are "easily verifiable—where they \"can relatively easily sniff-check on correctness\"—or are low-stakes". Conceptually difficult or design-dependent tasks are kept or done collaboratively. ("The collaboration paradox")
- An engineer's rule: "I'm primarily using AI in cases where I know what the answer should be or should look like." (same section)
Evidence and numbers: AI used "in roughly 60% of their work" while only "a small fraction" of tasks is fully delegated (the foreword gives 0-20%).
Caveats: Predictions, not results; partly overtaken by the mid-2026 articles (multi-day runs, thousand-PR migrations).
Relevance: low to medium. The delegation heuristic (verifiable or low-stakes) is the usable part.

### 2026 agentic coding trends report: Foreword (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report-foreword-from-assistance-to-c   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report/foreword-from-assistance-to-collaboration
Introduction to the report. Sole data point: developers "use AI in roughly 60% of their work" but "report being able to \"fully delegate\" only 0-20% of tasks." States the predictions "reflect what we're seeing with customers today, not certainties about tomorrow."
Relevance: low.

### 2026 agentic coding trends report: Foundation trends (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report-foundation-trends-the-tectoni   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report/foundation-trends-the-tectonic-shift
Prediction chapter with a before/after table of the SDLC (requirements "Days-Weeks" becomes "Express intent (Minutes)"; code review "Days" becomes "Human review (Min-Hours)"). Notes engineers use AI "for tasks that are easily verifiable, well-defined, or repetitive, while keeping high-level design decisions and anything requiring organizational context or \"taste\" for themselves." No procedures.
Relevance: low. The table's durations are illustrative, not measured.

### 2026 agentic coding trends report: Impact trends (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report-impact-trends-what-agents-may   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report/impact-trends-what-agents-may-change-in-2026
Prediction chapter (trends 6 to 8). Two findings from Anthropic's internal research are worth keeping: engineers report "a net decrease in time spent per task category, but a much larger net increase in output volume", and "about 27% of AI-assisted work consists of tasks that wouldn't have been done otherwise" (dashboards, exploratory work, "papercuts"). Security prediction: "any engineer can become a security engineer", while attackers scale too, so "build in security from the start."
Relevance: low. The 27% figure explains why throughput metrics overstate time saved.

### 2026 agentic coding trends report: Priorities for the year ahead (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report-priorities-for-the-year-ahead   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report/priorities-for-the-year-ahead
Closing chapter. Four priorities: multi-agent coordination, "Scaling human-agent oversight through AI-automated review systems that focus human attention where it matters most", extending agentic coding beyond engineering, and security architecture "from the earliest stages". States "While more routine coding tasks can be delegated to AI, humans are still reviewing the code."
Relevance: low.

### 2026 agentic coding trends report: landing page (Anthropic, 2026-01-21)
File: resources-guides-2026-agentic-coding-trends-report   URL: https://claude.com/resources/guides/2026-agentic-coding-trends-report
Two-paragraph index page for the report; no content beyond the chapter summaries above.
Relevance: low.

### Building effective AI agents: Common use cases and applications (Anthropic, 2026-01-01 per file metadata)
File: resources-guides-building-effective-ai-agents-common-use-cases-and-applications   URL: https://claude.com/resources/guides/building-effective-ai-agents/common-use-cases-and-applications-for-ai-agents
Customer-reference list with vendor-reported figures (Augment Code: a project in 2 weeks estimated at 4-8 months, onboarding from weeks to 1-2 days; Intercom Fin: up to 86% resolution, 51% out of the box; Assembled: 20% higher CSAT; Inscribe: fraud review from 30 minutes to 90 seconds). No practices.
Relevance: low. Product agents, not coding workflow.

### Building effective AI agents: Executive summary (Anthropic, 2026-01-01 per file metadata)
File: resources-guides-building-effective-ai-agents-executive-summary   URL: https://claude.com/resources/guides/building-effective-ai-agents/executive-summary
Business case for agents with customer figures (Coinbase 99.99% availability and 35-50 internal AI applications; Gradient Labs 80-90% resolution; Tines "100x time-to-value improvement"). The saved text is truncated mid-sentence ("mapped out their agentic AI strategy and found") before a list of guide contents. No practices.
Relevance: low.

### Building effective AI agents: Looking forward (Anthropic, 2026-01-01 per file metadata)
File: resources-guides-building-effective-ai-agents-looking-forward-the-future-of-buil   URL: https://claude.com/resources/guides/building-effective-ai-agents/looking-forward-the-future-of-building-ai-agents
Conclusion of the guide. One usable sentence: "start with single agents to prove ROI, build observable systems from day one, and evolve your architecture based on what the data tells you." The rest is calls to action.
Relevance: low.

### Building Effective AI Agents: landing page (Anthropic, 2026-01-01 per file metadata)
File: resources-guides-building-effective-ai-agents   URL: https://claude.com/resources/guides/building-effective-ai-agents
Two-sentence index page for the guide. No content.
Relevance: low.

### Building effective AI agents: Common architecture patterns (Anthropic, 2026-01-01 per file metadata)
File: resources-guides-building-effective-ai-agents-common-architecture-patterns   URL: https://claude.com/resources/guides/building-effective-ai-agents/common-architecture-patterns
Thesis: A catalogue of agent architectures for product builders (single agent, hierarchical and collaborative multi-agent, sequential and parallel workflows, evaluator-optimizer) with a decision framework. The consistent advice is to start with one agent plus skills and add structure only when it pays.
Practices:
- "Start simple, scale intelligently." Simple systems "are cheaper to run (fewer tokens, less compute), easier to debug when things go wrong". ("Agent design best practices")
- Model choice balances "capabilities, speed, and cost"; "Running a simple task through a premium model isn't just wasteful, it's also slower and more expensive at scale." (same section)
- Skills before more agents: "before scaling to multi-agent systems, consider whether adding specialized skills to your single agent might achieve your accuracy requirements more efficiently." ("Single-agent systems")
- When multi-agent is justified: open-ended problems, expertise that "would overwhelm a generalist agent", or "pursuing multiple independent directions simultaneously". ("Multi-agent systems")
- Scale effort: "simple queries shouldn't trigger expensive multi-agent workflows." (same section, "Implementation considerations")
- Orchestrator context: tools should "include pagination, range selection, filtering, and truncation with sensible defaults, capping responses at manageable sizes (something like 25,000 tokens)". ("Hierarchical/supervisory systems")
- Collaborative systems need "division of labor, problem-solving approaches, and effort budgets rather than strict instructions", and one named challenge is "preventing agents from bouncing tasks indefinitely". ("Collaborative systems")
- Sequential workflows "trade off latency for higher accuracy by making each AI call an easier, more focused task"; avoid them "when the workflow requires backtracking or iteration." ("Sequential workflows")
- Parallel: "AI models generally perform better when each consideration is handled by a separate call". Voting suits "reviewing code vulnerabilities with several different prompts". Avoid when agents "can't reliably coordinate changes to shared state". ("Parallel workflows")
- Evaluator-optimizer: use "when clear evaluation criteria exist"; avoid when "first-attempt quality already meets requirements" or "deterministic solutions exist". The documentation example "typically runs 2-4 cycles". ("Evaluator-optimizer")
- Decision questions: level of control, domain complexity, resource constraints, need for deep domain expertise. ("The three critical questions"; the section lists four)
Evidence and numbers: "multi-agent systems outperform single-agent systems by 90.2%" on complex multi-direction research tasks (internal Anthropic research); "Multi-agent systems use roughly 10-15x more tokens than single agents."; "You can deploy a single agent in weeks. Multi-agent systems take months to get right."; a quoted benchmark claim that "swarm architecture slightly outperforms supervisor architecture across the board".
Tools and files named: Agent Skills, MCP, think tool, context editing, memory tools, LangGraph, Mastra, AutoGen, Semantic Kernel.
Caveats: About building product agents, not about a coding setup; examples are marketing, finance and data science. The 90.2% figure comes from a research-agent evaluation and should not be read as a coding result (Inference). Dynamic agent generation is called experimental: "no production systems currently implement true dynamic creation" (stale by mid-2026, when the migration article describes dynamic workflows).
Relevance: medium. The cost multiplier and the skills-before-more-agents rule are the decision inputs for when a solo developer should fan out.

Note on the nine "Scaling agentic coding across your organization" guide pages that follow (Anthropic Applied AI). Every page's front matter says 2024-01-15, which is wrong (Inference: the fetcher picked up a timestamp from a log line in the appendix example). The guide's own note says "This guide reflects current insights as of August 2025." Treat it as August 2025 and as the long form of the 2025-10-15 article above. It is among the oldest guidance in this batch and is superseded on most points by the 2026-08 SDLC playbook.

### Scaling agentic coding guide: Appendix (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-appendix   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/appendix
Thesis: Worked examples: a project `CLAUDE.md`, a test-driven session, a context-rich bug report, and a long structured build prompt.
Practices:
- Example `CLAUDE.md` sections: "Development Environment", "Claude Code Guidelines", "Architecture Notes", "Current Sprint Focus"; includes "Always run tests before committing: `npm test`". ("Project-level CLAUDE.md structure example")
- TDD in five steps: have Claude write tests; "Run tests (they should fail)"; implement "to pass all the existing tests"; run again; then refactor with "Maintain all existing test compatibility". ("Test-driven development with Claude Code")
- Bug-report prompt sections: environment information, full error information, browser console error, reproduction steps, expected vs. actual behaviour, relevant code files, additional context, "What I've tried". ("Content-rich prompt example")
- Build prompt sections: tech stack, functional requirements, endpoints, data model, security, validation, error handling, response formats, testing requirements ("Minimum 90% code coverage"), project structure, deliverables. ("Well-structured prompt example")
Caveats: The commands shown (`claude-code --task "..."`) do not match the CLI named in the 2026 playbook (`claude`, `claude -p`); treat the syntax as outdated. The build prompt asks for a whole application in one request, which contradicts the same guide's advice to "Break complex tasks into focused commands". The bug example pastes a `.env` file with a database password into the prompt, which conflicts with the later security guidance that credentials should never be available to the agent. The generated tests are heavily mocked. A "Current Sprint Focus" section in `CLAUDE.md` conflicts with the playbook's "Keep it under a page" and no-stale-content rule (Inference).
Relevance: low to medium. The bug-report template is still a good shape; the rest is dated.

### Scaling agentic coding guide: Avoiding common challenges to adoption (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-avoiding-common   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/avoiding-common-challenges-to-adoption
Thesis: Three failure patterns of new users: unbounded tasks, missing context, weak prompts.
Practices:
- TDD as the guardrail against "massive, unbounded tasks": write test specifications first, "implement just enough code to make one test pass at a time", and "don't let it move forward until the current functionality is solid." ("Don't fall into the \"do everything\" trap")
- Over-share context: full error and stack trace, environment, screenshots with a precise description, and "Expected: API returns 200 status with user data. Actual: Returns 401 with 'invalid token' message." ("Overcome the context gap")
- "Treat Claude like an engineer": ask whether a teammate would understand the request and pre-empt their questions. ("Mastering Claude Code communication")
- "Provide examples and constraints": point at an existing pattern or style guide. (same section)
Evidence and numbers: none.
Relevance: medium. Same content as the 2025-10 article; consistent with later sources on test-first scoping.

### Scaling agentic coding guide: Beyond the obvious: innovative agentic coding applications (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-beyond-the-obvi   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/beyond-the-obvious-innovative-agentic-coding-applications
List of agent ideas without procedures: on-call automation, migration specialists, "Continuous documentation engines" that "monitor code changes ... and automatically update technical documentation", performance optimisation agents, compliance agents. Carries the dating note "as of August 2025".
Relevance: low. Each idea is described concretely in a later article in this batch (on-call, migration, Brex's doc-drift check).

### Scaling agentic coding guide: Foreword (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-foreword   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/foreword
Introduction with no practices. States the guide is "Based on insights from Anthropic's Applied AI team and lessons learned from our customers".
Relevance: low.

### Scaling agentic coding guide: Measuring ROI (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-measuring-roi   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/measuring-roi
List of metrics: sprint throughput, time-to-completion for standard tasks, migration acceleration, developer satisfaction, onboarding speed, cross-team collaboration, plus Activity Metrics (lines accepted, suggestion accept rate, spend). Calls lines of code "a notoriously spotty metric" and prefers a concrete before/after: "This task used to take our team a week. Now one engineer completes it in half a day."
Relevance: low. For a solo developer the only usable metric is time-to-completion on a recurring task.

### Scaling agentic coding guide: Rolling out agentic coding at your organization (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-rolling-out-age   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/rolling-out-agentic-coding-at-your-organization
Thesis: Pilot group, hackathon, internal experts, shared `CLAUDE.md`.
Practices:
- Custom slash commands per codebase, "such as /migrate-db for database schema updates, /add-feature with company-specific boilerplate, and /fix-security for common vulnerability patches." ("Start with power users")
- `CLAUDE.md` holds "coding standards, outlining gotchas, and highlighting best practices"; "take time to iterate on your CLAUDE.md files as you would any other agentic prompt." (same section)
- "Build wrapper scripts to handle authentication for third-party tools, like AWS and GCP". (same section)
- Commit `CLAUDE.md` at the repository root on the main branch; update it in the same PR as architectural or convention changes. ("Sharing CLAUDE.md files")
Evidence and numbers: pilot of "20-50 developers" (a recommendation).
Caveats: "Branch-specific variations" of `CLAUDE.md` is suggested here and nowhere in the later sources.
Relevance: low to medium. Slash commands per recurring task and auth wrapper scripts apply to one person.

### Scaling agentic coding guide: Security first: protecting your codebase (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-security-first   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/security-first-protecting-your-codebase
Thesis: Security rules belong in instruction files and review commands, MCP servers need vetting, and Claude can act as a security reviewer alongside existing tools.
Practices:
- Policy in `CLAUDE.md`, for example: "All database queries must use parameterized statements," "API endpoints require authentication middleware," or "No hardcoded secrets in configuration files." ("Policy-as-code enforcement")
- Run `/security-review` "before committing code". ("Security review automation")
- "Security pattern libraries": "Instead of letting it improvise authentication logic, provide tested, compliant examples it should follow." 
- Managed settings: admins "push out configurations and permitted MCP tools to all users through enterprise managed policy settings that take precedence over user and project settings." ("Configuring enterprise permissions")
- MCP servers: assess before approving ("data handling, API security, access controls, and vendor security posture"); keep a pre-approved list; "Test new MCP servers in isolated environments before production deployment"; "Schedule quarterly reviews of all approved MCP servers." ("MCP server management")
- Findings must come with a fix: "\"This cookie handling is insecure\" should come with \"Use httpOnly and secure flags with SameSite=Strict configuration.\"" ("Code review evolution")
- Use it "alongside your team's existing security tools, rather than replacing them." (introduction)
Evidence and numbers: none.
Caveats: Calls instructions in `CLAUDE.md` "Policy-as-code enforcement", but the 2026-08 playbook is explicit that such instructions are advisory and need a hook or review pass behind them. No mention of sandboxing, egress control or prompt injection, which the 2026 security articles treat as central.
Relevance: medium. MCP vetting and a quarterly MCP review are the supply-chain controls this batch offers; the rest is superseded.

### Scaling agentic coding guide: What is agentic coding? (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization-what-is-agentic   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/what-is-agentic-coding
Four use cases in one line each (legacy modernisation, onboarding, incident response, non-technical contributors). No practices.
Relevance: low.

### Scaling agentic coding guide: Guide landing page (Anthropic Applied AI, 2025-08 per the guide's own note; file metadata says 2024-01-15)
File: resources-guides-scaling-agentic-coding-across-your-organization   URL: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization
Fetched via jina; the saved file is almost entirely site navigation and footer links around a two-paragraph blurb and "37 min read". No content. (It does list current product and model family names in the navigation, e.g. Claude Tag, Claude Security, Mythos, Fable.)
Relevance: low.
