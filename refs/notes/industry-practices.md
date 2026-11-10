# Industry practices: how frontier companies and practitioners (other than Anthropic) build software with coding agents

Sources read: 103 files, written up as 101 entries (two entries cover two files each). All are in the `industry` collection under `refs/articles/`. Reading finished 2026-11-10/11.

Not read or not fetched:
- 10 saved files were not read; they are listed under "Saved but not read" at the end, with one partial read (the Symphony article prose was read, its embedded 52,000-character `SPEC.md` line was not).
- Two Huntley pages (`ghuntley.com/stdlib`, `ghuntley.com/specs`) and `ghuntley.com/agency` are truncated in the saved files (membership wall or cut-off); the Medium copy of Yegge's "Fences, not Sandboxes" is a teaser, so the full text was saved from yegge.ai instead.
- Not fetched: OpenAI's "How OpenAI uses Codex" PDF (the fetch tool skips PDFs and no attempt through the alternate route was made); Böckeler's follow-up article on sensors (linked from `[TW-harness]`); Shopify's "Under the River"; any Uber, Sourcegraph (beyond Amp), Jules or Kiro first-hand piece; Dex Horthy's 2026 talks and podcast (search results say he revised research-plan-implement after a "read the plan, skip the code" experiment went wrong, but no primary source was saved).
- No YouTube transcripts were saved for this assignment (0 of the 6 allowed).
- Several result tables and prompts are images in the originals and are missing from the saved text (noted per source, for example `[VER-agentsmd]` and `[OAI-maintain]`).

Injection check: no source contained hidden or adversarial instructions aimed at the reader's agent. Many contain embedded prompts as subject matter (the ExecPlan template, the Ralph prompts, Kent Beck's system prompt), and three invite readers to point a coding agent at the page or a linked file (`[RAMP-inspect]`, `[OAI-symphony]`, `[GIT-aw]`). None of these were followed.

Reading the dates: this field moved quickly between mid-2025 and late 2026. Advice written for mid-2025 models (heavy scaffolding, shouted instructions, fresh context for everything) is partly reversed by late-2026 sources (`[OAI-astra]`, `[CUR-harness]`, `[TW-harness-cost]`, `[PS-speed]`). Where sources conflict, the newer one is usually describing a stronger model.

## Cross-cutting findings

Each line is a claim followed by the sources that support it. Quotes and locators are in the per-source entries.

1. Keep the always-loaded instruction file short, universal and map-like, pointing to deeper docs that are read on demand. `[OAI-harness]` (about 100 lines), `[HL-claudemd]` and `[HL-skillissue]` (under 60 lines), `[OAI-bestpractices]`, `[CUR-best]`, `[STR-minions1]`, `[STR-minions2]`, `[TW-context]`, `[OAI-execplans]` (a two-line pointer to the plan spec).
2. Grow instructions from observed failures, one entry per recurring mistake, and prune them at every model upgrade. `[MH-journey]`, `[OAI-bestpractices]`, `[CUR-best]`, `[HL-skillissue]`, `[PS-talk]`, `[TES-charter]`, `[OAI-astra]`, `[CUR-harness]`, `[TW-context]`.
3. Escalate repeat problems up a ladder: habit, written note, scoped rule, mechanical check. Prose is for judgment, code is for guarantees. `[OAI-harness]`, `[SY-fences]`, `[SHOP-river]`, `[TES-75]`, `[TES-intent]`, `[TES-charter]`, `[TW-harness]`, `[TW-loops]`, `[EV-compound]`.
4. The most repeated success factor is giving the agent a fast way to verify its own work (types, tests, lint, a running app, logs, screenshots). `[MH-journey]`, `[HL-skillissue]`, `[LC-harness]`, `[SPO-honk3]`, `[RAMP-inspect]`, `[GH-ralph]`, `[AR-recs]`, `[PS-speed]`, `[DD-harness]`, `[OAI-harness]`, `[CUR-cloud]`, `[AMP-howiuse]`.
5. Make feedback cheap and readable for the agent: silent on success, full detail only on failure, fail fast, and put the remedy in the error text. `[HL-backpressure]`, `[HL-skillissue]`, `[SPO-honk3]`, `[CUR-dynamic]`, `[OAI-harness]`, `[TW-harness]`, `[AR-didnt]`, `[AR-recs]`.
6. Gate completion mechanically: a stop-time hook or wrapper runs the checks and sends failures back to the agent, with a cap on iterations. `[HL-skillissue]`, `[SPO-honk3]`, `[CUR-best]`, `[LC-harness]`, `[STR-minions2]` (at most two CI rounds), `[TES-75]` (long review loops consume half the spend).
7. Plan before code for anything non-trivial, keep the plan as a file in the repo, get explicit approval, and review against it. `[OAI-execplans]`, `[OAI-longhorizon]`, `[OAI-sora]`, `[HL-ace]`, `[MH-vibing]`, `[CUR-best]`, `[CUR-longrunning]`, `[EV-compound]`, `[GOO-conductor]`, `[GIT-speckit]`, `[OAI-runme]`, `[OAI-symphony]`.
8. Scale the planning ceremony to the size of the change; heavyweight spec workflows cost more review than they save on small work. `[TW-sdd]`, `[PS-talk]`, `[AR-pi]`, `[OAI-harness]` (lightweight plans for small changes), `[CUR-best]`, `[HL-ace]` (research is sometimes skipped).
9. Keep each context small and single-purpose; move state between sessions through files (plan, progress, handoff), not through long conversations. `[GH-ralph]`, `[HL-ace]`, `[HL-longctx]`, `[HL-fork]`, `[AMP-howiuse]`, `[AMP-context]`, `[CUR-best]`, `[SY-beads]`, `[OAI-bestpractices]`, `[CUR-selfdriving]`, `[SPO-honk2]`.
10. Use subagents to isolate context (search, research, noisy commands, failure-prone iteration) and to get a fresh-eyed review, not as role personas. `[HL-ace]`, `[HL-skillissue]`, `[AMP-subagents]`, `[GH-ralph]`, `[AR-hard]`, `[AR-didnt]`, `[AR-pi]`, `[TW-context]`, `[PS-talk]`.
11. Prefer CLIs, scripts and files to MCP servers and custom tools; keep the tool set small and load the rest lazily. `[AR-recs]`, `[AR-skillsmcp]`, `[PS-talk]`, `[HL-skillissue]`, `[VER-80pct]`, `[VER-fsbash]`, `[GH-tier]`, `[CUR-dynamic]`, `[STR-minions2]`, `[SPO-honk2]`, `[OAI-bestpractices]`. Qualifier: `[VER-bashtest]` shows a purpose-built tool beating bash for structured queries.
12. Skills need short routing-style descriptions with negative cases, progressive disclosure, scripts for the deterministic parts, and trigger tests; expect them not to fire reliably. `[OAI-skills-shell]`, `[OAI-evalskills]`, `[OAI-astra]`, `[VER-agentsmd]`, `[VER-skillsfaq]`, `[TW-context]`, `[SHOP-harness]`, `[OAI-bestpractices]`.
13. Shape the codebase for agents: typed language, strict module boundaries, boring stable dependencies, simple explicit code, canonical examples to copy, and architecture rules enforced by structural tests or custom linters. `[OAI-harness]`, `[TW-harness]`, `[AR-recs]`, `[GH-ralph]`, `[OAI-sora]`, `[TW-anchor]`, `[TW-autonomy]`, `[PS-talk]`, `[CUR-selfdriving]`, `[TW-loops]`.
14. Wrap agent steps in deterministic steps: whatever must always happen (lint, format, push, enumeration, credential handling) is code that runs around the agent. `[STR-minions1]`, `[STR-minions2]`, `[SHOP-river]`, `[SHOP-harness]`, `[SPO-honk3]`, `[VER-v0]`, `[TW-autonomy]`, `[AR-didnt]`, `[HL-12factor]`.
15. Verify independently of the implementer: acceptance checks the agent cannot edit, a different model or fresh context as reviewer, and evidence attached to each claim. Design the checks against the known failure modes (claiming success on red tests, deleting or disabling tests, placeholder code, scope creep, calling failures pre-existing). `[TW-harness-cost]`, `[SDM-factory]`, `[SHOP-harness]`, `[SPO-honk3]`, `[VER-factory]`, `[TES-intent]`, `[TES-charter]`, `[TW-autonomy]`, `[BECK-augmented]`, `[SY-beads]`, `[GH-ralph]`, `[CUR-selfdriving]`, `[AMP-howiuse]`, `[AR-pi]`.
16. Keep work items in a durable, queryable place outside the chat, with status and dependencies, and file discovered problems instead of fixing or ignoring them in passing. `[SY-beads]`, `[OAI-symphony]`, `[OAI-harness]`, `[TW-blackboard]`, `[AR-pi]`, `[EV-compound]`, `[GH-ralph]`, `[SHOP-river]` (stored state is a claim to recheck).
17. Run recurring maintenance agents that open small, evidence-backed changes (doc gardening, dead code, drift from golden rules, refactors), on a schedule and one small change at a time. `[OAI-harness]`, `[OAI-maintain]`, `[HL-ralph]`, `[GIT-aw]`, `[CUR-harness]`, `[PS-talk]`, `[TW-harness]`, `[OAI-bestpractices]`.
18. Give unattended agents a disposable, isolated environment with default-deny network egress and credentials kept outside it; inside that boundary they can run without prompts. Treat issues, web pages, MCP descriptions and downloaded skills as untrusted. `[STR-minions1]`, `[STR-minions2]`, `[VER-sandbox]`, `[VER-factory]`, `[OAI-skills-shell]`, `[SPO-honk3]`, `[GIT-aw]`, `[HL-skillissue]`, `[VER-skillsfaq]`, `[OAI-symphony]`, `[AR-codemode]`.
19. Human review is now the bottleneck, and teams respond with smaller changes, risk-tiered review, a short list of change types that always get a human, and review of intent and evidence before diffs. `[GIT-beyond]`, `[OAI-reviewrules]`, `[TW-review]`, `[TW-care]`, `[VER-factory]`, `[TES-75]`, `[TES-intent]`, `[OAI-symphony]`, `[HL-ace]`, `[OAI-sora]`.
20. How much harness helps depends on the model: scaffolding that rescued weaker models adds cost and can hinder frontier ones, but an independent final gate stays necessary. `[TW-harness-cost]`, `[OAI-astra]`, `[CUR-harness]`, `[LC-harness]`, `[VER-80pct]`, `[CUR-cloud]`, `[PS-speed]`, `[OAI-symphony]`.

### (a) Named methodologies and loops

| Name | One-line definition | Originating source | Reported results | Criticisms and limits |
|---|---|---|---|---|
| Harness engineering | When the agent makes a mistake, engineer the environment (instructions, tools, checks) so it cannot recur; humans design environments and feedback loops instead of writing code. | Term: `[MH-journey]` (2026-02-05); popularised by `[OAI-harness]` (2026-02-11). `[HL-skillissue]` credits Viv Trivedy. Framework: `[TW-harness]`. | About 1M lines and 1,500 PRs in five months with no hand-written code `[OAI-harness]`; 52.8 to 66.5 on Terminal Bench by harness changes alone `[LC-harness]`; cheap model from 3 of 10 to 10 of 10 `[TW-harness-cost]`. | No benefit and about 7x cost for a frontier model on one task `[TW-harness-cost]`; behaviour verification unsolved and vendor interest noted `[TW-harness-memo]`, `[TW-harness]`; hard to retrofit to legacy code `[TW-harness-memo]`; easy to over-invest `[HL-skillissue]`. |
| Guides and sensors | Classify every control as feedforward (guide) or feedback (sensor), and as computational (deterministic) or inferential (LLM). | `[TW-harness]` | None measured; used as the frame for `[TW-harness-cost]`. | Sensors miss misdiagnosis, over-engineering and misunderstood instructions `[TW-harness]`. |
| Context engineering, frequent intentional compaction | Design the workflow around what is in the context window; keep utilisation moderate and compact into artifacts. | `[HL-ace]` (Dex Horthy claims the coinage via 12-factor agents, per `[HL-skillissue]`); primer in `[TW-context]`. | 35k LOC in 7 hours on a 300k LOC Rust codebase `[HL-ace]`. | Needs deep engagement; failed on parquet-java `[HL-ace]`; an illusion of control `[TW-context]`. |
| Research, plan, implement (RPI) | Three phases with a written research doc and plan; human review concentrated on research and plan. | `[HL-ace]` | Same as above; plan built on research fixed a bug in a better place than a plan without it. | Author says it probably is not right for most teams `[HL-ace]`; `[PS-talk]` and `[AR-pi]` prefer conversation to plan files. |
| Ralph loop | A shell loop that feeds the same prompt to a fresh agent each iteration: load specs and plan, do one item, verify, commit. | `[GH-ralph]` (2025-07) | Built a programming language; six repos overnight in the repomirror write-up `[GH-ralph]`, `[HL-ralph]`. | Greenfield only, broken mornings, placeholder code, about 90% done `[GH-ralph]`; overbaking and bad-spec failures `[HL-ralph]`; the name now loosely means unattended looping `[TW-loops]`, `[HL-ralph]`. |
| ExecPlans (PLANS.md) | A self-contained living plan document with mandatory Progress, Surprises, Decision Log and Retrospective sections that a stateless agent can execute. | `[OAI-execplans]` (2025-10) | More than seven hours from one prompt `[OAI-execplans]`; a 25-hour run with a four-file variant `[OAI-longhorizon]`. | Elaborate recipes can hinder newer models `[OAI-astra]`. |
| Spec-driven development | Write a spec before code; variants are spec-first, spec-anchored and spec-as-source. | Spec Kit `[GIT-speckit]`, Kiro and Tessl as described in `[TW-sdd]`; Conductor `[GOO-conductor]`. | None measured in these sources. | Overkill for small changes, heavy markdown review, agent still ignores or over-follows instructions, echoes of model-driven development `[TW-sdd]`; called the old way of thinking by `[PS-talk]`. |
| Compound engineering | Plan, work, review, compound: after each task, write the lesson back into instructions, docs, agents or checks. | `[EV-compound]` (2025-12) | Five products run mostly by single engineers (self-reported). | No measurements; large set of role agents conflicts with `[HL-skillissue]` and `[AMP-subagents]`. |
| Beads | An issue tracker for agents with dependency links stored in git, replacing markdown plans as external memory. | `[SY-beads]` (2025-10) | Over 20k GitHub stars `[SY-v1]`; author's own before and after account. | Original sync design caused merge conflicts `[SY-v1]`; implementation criticised by `[AR-pi]`. |
| Gas Town (orchestrator) | Many coding-agent sessions with fixed roles, a merge-queue agent and workflows stored as chained issues. | `[SY-gastown]` (2026-01) | 13k stars, v1.0 in three months `[SY-v1]`. | Lost work, duplicate fixes, data loss, high cost, author says do not use `[SY-gastown]`, `[SY-v1]`. |
| Symphony | Issue tracker as control plane: every open ticket gets an agent in its own workspace until done. | `[OAI-symphony]` (2026-04) | Landed PRs up 500% on some teams in three weeks. | Loses mid-flight steering; some runs miss entirely; not maintained as a product. |
| Blueprints | A workflow in code whose nodes are either deterministic steps or scoped agent loops. | `[STR-minions2]` (2026-02) | Over 1,300 agent-written PRs merged per week. | Built on years of internal tooling; no success rate published. |
| Planner and worker hierarchy | Recursive planners that only issue tasks, isolated workers that return a written handoff. | `[CUR-scaling]`, `[CUR-selfdriving]` | About 1,000 commits per hour for a week on a research project. | Flat peers, shared locks, a central integrator and an overloaded single executor all failed first; needs tolerance for a non-green branch. |
| Verification loop with LLM judge | Deterministic verifiers behind one abstract tool, a stop-hook gate, then a judge comparing the diff with the prompt. | `[SPO-honk3]` (2025-12) | Judge vetoes about a quarter of sessions; half of those recover. | Judge itself not yet evaluated. |
| Software factory | A pipeline of task-specific agents producing evidence, with humans approving or only handling exceptions. | `[VER-factory]`, `[SDM-factory]`, `[CUR-harness]`, `[SY-fences]`, `[TES-75]` | 25 to 35% of merged PRs `[VER-factory]`; about 75% of PRs merged without human correction `[TES-75]`. | Red builds and lower delivery stability `[TW-wary]`; no quality data from `[SDM-factory]`. |
| Charter (four levers) | Instruction, constraint, capability and check files in the repo; only checks can refuse. | `[TES-charter]` (2026-10) | 1 of 8 to 8 of 8 checks on one demonstration ticket. | Demonstration only; a ninth semantic check still needed a reviewer. |
| Intent verification and invariants | Review acceptance criteria before code, then verify each with evidence; turn repeated review comments into machine-checked invariants. | `[TES-intent]` (2026-10); related `[OAI-reviewrules]` | Rule-guided review recovered 98% of required findings versus 58.3% `[OAI-reviewrules]`. | `[TES-intent]` gives no numbers; conflicts with read-every-diff advice. |
| Humans on the loop, agentic flywheel | Fix the harness that produced a bad artifact, not the artifact; have agents propose harness improvements. | `[TW-loops]` (2026-03) | None. | Conceptual. |
| Augmented coding | Agent types, human keeps hand-coding values: TDD cycle, tidy-first commits, close supervision. | `[BECK-augmented]` (2025-06) | A working B+ tree library after two failed attempts. | Author unhappy with code quality; agents may ignore TDD instructions (reader comment). |
| Harness-first engineering, verification pyramid | Invest in layered automated checks, cheapest falsifier first, with production telemetry closing the loop. | `[DD-harness]` (2026-03) | 87% memory reduction; about 93% of peak throughput with 10M simulation seeds. | Heavy formal tooling; harness itself can be wrong. |
| Dynamic context discovery | Give less up front; expose tool output, history, skills and MCP descriptions as files the agent pulls. | `[CUR-dynamic]` (2026-01) | 46.9% fewer tokens in runs that used MCP. | Vendor A/B test. |
| Codemode | The model writes code that calls tools inside a harness-side sandbox instead of one tool call per turn. | `[AR-codemode]` (credits Cloudflare for the name) | None. | Works poorly with current MCP servers and smaller models. |
| Context Development Lifecycle | Generate, evaluate, distribute and observe context as a versioned, tested artifact. | `[TES-cdlc]` (2026-02) | None. | Conceptual, vendor-aligned. |

### (b) What goes in AGENTS.md or CLAUDE.md, and what is kept out

Put in:
- Exact build, test, lint and typecheck commands with flags, and how to run one test. `[OAI-bestpractices]`, `[CUR-best]`, `[GIT-agentsmd]`, `[HL-claudemd]`, `[AMP-howiuse]`, `[GH-ralph]` (in `AGENT.md`).
- What the project is, its stack with versions, and a map of where things live. `[HL-claudemd]`, `[OAI-harness]`, `[GIT-agentsmd]`, `[PS-talk]`, `[OAI-sora]` (location of sibling repos in the global file).
- What done means and how to verify. `[OAI-bestpractices]`, `[HL-claudemd]`. `[OAI-astra]` says to drop verify reminders for the newest models.
- Pointers to deeper docs, plans and specs, with one-line descriptions, instead of their content. `[OAI-harness]`, `[HL-claudemd]`, `[OAI-execplans]`, `[CUR-best]`, `[PS-speed]`, `[VER-agentsmd]` (a compressed docs index).
- Corrections for observed agent mistakes, one line each, and announcements of project-specific scripts and CLIs with a few usage examples. `[MH-journey]`, `[HL-skillissue]` (Linear CLI lines), `[AR-recs]` (emails are logged), `[SY-beads]` (one line to run the tracker).
- Things newer than the model's training data, deleted once a newer model knows them. `[PS-talk]`, `[VER-agentsmd]`, `[TES-cdlc]`.
- Boundaries in three tiers (always, ask first, never) and do-not rules. `[GIT-agentsmd]`, `[OAI-bestpractices]`.
- A small number of consequential, non-obvious review rules with the safe path, scoped to the directory they govern. `[OAI-reviewrules]`.
- Explicit permission for known-safe loops (run local tests, fix, rerun without asking). `[OAI-astra]`.
- Git conduct when several agents share a checkout. `[PS-talk]`.

Keep out:
- Code style guides and formatting rules; use a linter and formatter. `[HL-claudemd]`, `[CUR-best]`, `[OAI-reviewrules]`, `[TW-review]`.
- Anything not relevant to nearly every task (schema design notes, deployment procedure); move it to path-scoped rules, nested files, skills or docs. `[HL-claudemd]`, `[STR-minions2]`, `[TW-context]`, `[OAI-reviewrules]`, `[HL-importantif]` (conditional blocks as a workaround).
- Copied code snippets; point to `file:line` or a canonical example file. `[HL-claudemd]`, `[CUR-best]`, `[TW-anchor]`. (`[GIT-agentsmd]` disagrees and wants style examples inline.)
- Directory listings and codebase overviews that the agent can discover itself. `[HL-skillissue]` reporting the ETH Zurich study; `[CUR-harness]` (static folder layouts dropped).
- Auto-generated content. `[HL-claudemd]`, `[HL-skillissue]`. (`[OAI-bestpractices]` and `[OAI-harness]` let the agent write the file; `[PS-talk]` has the agent maintain it.)
- Instructions to read stacks of docs before every edit, and reminders for things the model already does. `[OAI-astra]`, `[CUR-selfdriving]`.
- Shouted or threatening emphasis. `[PS-talk]`, `[OAI-astra]`. (`[GH-ralph]` uses it heavily, in 2025.)
- Status reports and progress logs; those go in the plan file. `[GH-ralph]`, `[OAI-longhorizon]`.
- Persona statements. `[PS-talk]`, `[HL-skillissue]`. (`[GIT-agentsmd]` recommends them for custom agent files.)

Size guidance spans two orders of magnitude: under 60 lines `[HL-claudemd]`, about 100 lines `[OAI-harness]`, short and accurate `[OAI-bestpractices]`, an 8KB docs index `[VER-agentsmd]`, about 800 lines that the author says works `[PS-talk]`. One format can serve several harnesses: `[STR-minions2]` syncs one rule source to Cursor, Claude Code and its own agent; `[PS-talk]` symlinks one file; `[VER-plugins]` says skills and MCP config are portable while hooks, commands and agents are not.

### (c) Mechanical enforcement in use (as opposed to prose)

- Custom linters and structural tests for layer and dependency direction, naming, file size and logging, with remediation text in the message. `[OAI-harness]`; ArchUnit-style tests in hooks `[TW-harness]`; ast-grep rules in a commit hook `[PS-talk]`.
- Linters and CI jobs that check the docs themselves (freshness, cross-links, structure). `[OAI-harness]`.
- Stop hooks that run formatter, typecheck, verifiers or coverage and return failures to the agent. `[HL-skillissue]`, `[SPO-honk3]`, `[CUR-best]`; pre-completion middleware `[LC-harness]`.
- Pre-tool hooks that refuse an action (deny migrations, block writes until sync, scope gates). `[HL-skillissue]`, `[RAMP-inspect]`, `[TES-charter]`.
- The same predicate mounted as a hook and as a CI target. `[TES-charter]`.
- PATH interceptors that replace a wrong command with an error naming the right one. `[AR-didnt]`, `[AR-pi]`.
- Pre-push hooks that run only the lints relevant to the change, in seconds. `[STR-minions1]`, `[STR-minions2]`, `[HL-backpressure]`.
- Deterministic workflow nodes around agent nodes (lint, push, CI, autofix). `[STR-minions2]`; staged pipelines `[SHOP-harness]`, `[VER-factory]`.
- A capped number of CI rounds or loop iterations. `[STR-minions1]`, `[CUR-best]`, `[SPO-honk2]`.
- Contract tests generated from specs, with examples validated against the specs first, and an acceptance suite the agent never sees. `[TW-harness-cost]`; scenarios held outside the repo `[SDM-factory]`.
- Property tests, deterministic simulation and model checking as the primary correctness gate. `[DD-harness]`.
- Real integration tests as the oracle for a finding, run by a different model. `[SHOP-harness]`.
- LLM-judged checks with a narrow yes or no rule, rolled out at warn level and then promoted to error. `[TES-verifiers]`; diff-versus-prompt judge `[SPO-honk3]`; scoped review rules with a trigger, counterexample and unrelated test PR `[OAI-reviewrules]`.
- Skill evals: trigger and non-trigger prompts, trace checks, rubric with a JSON schema. `[OAI-evalskills]`.
- Environment-level limits: read-only by default with declared safe outputs `[GIT-aw]`; restricted git tool and command allowlist `[SPO-honk2]`; network allowlists and credential injection outside the sandbox `[VER-sandbox]`, `[OAI-skills-shell]`; isolated devboxes `[STR-minions2]`; PRs opened under the user's identity so self-approval is impossible `[RAMP-inspect]`.
- Single-instance dev server and log files as tools. `[AR-recs]`.
- Scheduled cleanup agents with quality grades. `[OAI-harness]`; weekly log-mining automation `[CUR-harness]`.
- Loop detection by edit count per file. `[LC-harness]`.

### (d) Contradictions and open questions

- AGENTS.md size and content. Under 60 lines of universal content `[HL-claudemd]` versus an 800-line accumulated file `[PS-talk]` versus a docs index in the file `[VER-agentsmd]`. `[HL-skillissue]` reports a study in which most agent files did not help. Open question: whether a docs index still beats a skill on late-2026 models; `[VER-agentsmd]` itself expected the gap to close, and `[OAI-astra]` warns against forcing doc reads.
- Skills versus always-on context. `[VER-agentsmd]` measured skills not firing in 56% of cases; `[VER-skillsfaq]`, `[OAI-bestpractices]` and `[HL-skillissue]` recommend skills for progressive disclosure; `[GH-agency]` says to delete skill packs; `[GH-tier]` says a good `--help` beats a skill.
- Auto-generating instruction files. Against: `[HL-claudemd]`. For, as a starting point or as practice: `[OAI-bestpractices]`, `[OAI-harness]`, `[PS-talk]`, `[GIT-agentsmd]`.
- Role-specialised subagents. Did not work: `[HL-skillissue]`, `[AMP-subagents]`, `[PS-talk]`. In active use: `[EV-compound]`, `[GIT-agentsmd]`; predicted by `[CUR-harness]`. Task-specific pipeline agents (one per stage, each with its own evals) did work for `[VER-factory]` and `[SHOP-harness]`. Inference: the split is between persona prompts, which add little, and agents with distinct inputs, tools and acceptance checks, which help.
- Plans and specs. Plan files and approval gates: `[OAI-execplans]`, `[HL-ace]`, `[CUR-best]`, `[EV-compound]`. Conversation instead of plan mode: `[PS-talk]`, `[PS-speed]`, `[AR-pi]`. Markdown plans rot and should be issues: `[SY-beads]`. Heavy SDD is counterproductive: `[TW-sdd]`.
- Fresh context versus long sessions. Small, fresh contexts: `[GH-ralph]`, `[HL-ace]`, `[HL-longctx]`, `[AMP-howiuse]`, `[CUR-best]`. No longer needed with newer models and good compaction: `[PS-speed]`; stay in one chat while on the same problem: `[OAI-bestpractices]`.
- Reading the code. Always review by hand: `[MH-vibing]`, `[CUR-best]`, `[TW-care]`. Review intent, plans and evidence instead: `[HL-ace]`, `[TES-intent]`, `[EV-compound]`, `[DD-harness]`, `[TW-review]`. Do not review at all: `[SDM-factory]`; rarely reads code: `[PS-speed]`, `[SY-gastown]`. `[TES-charter]` shows eight green mechanical checks hiding three real defects.
- AI review of every PR. Done at OpenAI `[OAI-bestpractices]` and Tessl `[TES-75]`; called automating the ceremony by `[TW-review]`.
- Green main. Strict stop-and-fix and commit only when everything passes: `[OAI-longhorizon]`, `[BECK-augmented]`, `[TW-wary]`. Tolerated flakes and a small steady error rate for throughput: `[OAI-harness]`, `[CUR-selfdriving]`. Both of the latter are high-throughput, low-blast-radius settings and say so.
- Hooks. Central to enforcement: `[HL-skillissue]`, `[SPO-honk3]`, `[TES-charter]`. Did not pay off: `[AR-didnt]` (2025); cannot stop a determined model: `[PS-talk]`. Not portable across harnesses: `[VER-plugins]`.
- Sandboxing. Required boundary with egress control: `[VER-sandbox]`, `[STR-minions2]`, `[OAI-skills-shell]`. Run without permission prompts on a laptop relying on git and tests: `[AR-recs]`, `[EV-compound]`. Does not try to defend against injection through Bash: `[AMP-fif]`. Rules over containment for capable models: `[SY-fences]`.
- Worktrees. Used for isolation: `[OAI-longhorizon]`, `[CUR-best]`, `[EV-compound]`, `[HL-ace]` (implementation only). Rejected in favour of one folder and atomic commits: `[PS-talk]`, `[PS-speed]`; do not scale at Stripe: `[STR-minions1]`.
- Who lays the foundation. Humans by hand first: `[OAI-sora]`, `[AMP-howiuse]`, `[MH-vibing]`. Agents from the first commit: `[OAI-harness]`.
- Does a harness pay for itself. Large gains for a weaker model and on a benchmark: `[TW-harness-cost]`, `[LC-harness]`. No gain at about 7x cost for a frontier model on a fully specified greenfield task: `[TW-harness-cost]`. Open: brownfield work, vague briefs, and the final-gate-only design were not measured.
- Bigger context windows. Went back to a smaller-window model and warn at 100k tokens: `[HL-longctx]`. More gets done per session with the larger effective window: `[PS-talk]`, `[PS-speed]`.
- Parallelism. A dozen agents unsustainable, back to 1 to 3: `[SY-beads]`; three to five sessions is the comfortable limit: `[OAI-symphony]`; one agent at a time by choice: `[MH-journey]`; three to eight routinely: `[PS-talk]`; 50 to 60 with heavy governance and daily bad decisions: `[SY-fences]`.
- Open questions the sources themselves raise: how to verify functional behaviour without trusting agent-written tests `[TW-harness]`; how architectural coherence holds over years `[OAI-harness]`; how to evaluate prompts, judges and context systematically `[SPO-honk2]`, `[SPO-honk3]`, `[AR-hard]`, `[TES-cdlc]`; what happens when the harness is wrong `[DD-harness]`; how CI copes with parallel agent output `[TW-wary]`, `[TW-blackboard]`.

## Per source

Source keys in brackets (for example `[OAI-harness]`) are used in the cross-cutting section.

### OpenAI

### Harness engineering: leveraging Codex in an agent-first world (Ryan Lopopolo, OpenAI, 2026-02-11) `[OAI-harness]`
File: refs/articles/openai.com/index-harness-engineering/article.md   URL: https://openai.com/index/harness-engineering/
(Date and author are from search results; the saved file has no date field.)
Thesis: A team built an internal product with zero hand-written code over five months. The engineer's job became designing the environment, specifying intent and building feedback loops; when the agent fails, the fix is a missing capability made "legible and enforceable", never "try harder".
Practices:
- AGENTS.md as a map, not an encyclopedia. The "one big AGENTS.md" failed four ways: crowds out the task, too much guidance becomes non-guidance, rots instantly, cannot be mechanically verified. "A short `AGENTS.md` (roughly 100 lines) is injected into context and serves primarily as a map" (section "We made repository knowledge the system of record").
- Structured `docs/` directory is the system of record: indexed design docs with verification status, "core beliefs", an architecture doc (top-level map of domains and package layering), a quality document that grades each product domain and layer, and plans (active, completed, tech debt) checked in and versioned (same section).
- Plans as first-class artifacts: lightweight ephemeral plans for small changes, execution plans with progress and decision logs for complex work (same section).
- Knowledge base enforced mechanically: "Dedicated linters and CI jobs validate that the knowledge base is up to date, cross-linked, and structured correctly." A recurring "doc-gardening" agent opens fix-up PRs for stale docs (same section).
- Anything not in the repo does not exist for the agent: Slack threads, Google Docs and tacit knowledge must be moved into versioned repo artifacts ("Agent legibility is the goal").
- Prefer "boring" technology and in-repo reimplementation over opaque dependencies; example: own map-with-concurrency helper instead of a `p-limit`-style package, with 100% test coverage ("Agent legibility is the goal").
- Rigid layered architecture per business domain, dependency direction Types → Config → Repo → Service → Runtime → UI, cross-cutting concerns only through "Providers"; enforced by custom linters (written by Codex) and structural tests ("Enforcing architecture and taste").
- "taste invariants" enforced statically: structured logging, naming conventions for schemas and types, file size limits, platform reliability rules. "Because the lints are custom, we write the error messages to inject remediation instructions into agent context." ("Enforcing architecture and taste").
- Enforce invariants, not implementations: require parsing data shapes at the boundary but do not prescribe the library ("Enforcing architecture and taste").
- Escalation ladder for human taste: review comments and bugs become doc updates or tooling. "When documentation falls short, we promote the rule into code" ("Enforcing architecture and taste").
- Make the app legible to the agent: app bootable per git worktree; Chrome DevTools Protocol wired in with skills for DOM snapshots, screenshots, navigation; an ephemeral per-worktree observability stack queried with LogQL and PromQL, so prompts like "ensure service startup completes in under 800ms" become checkable ("Increasing application legibility").
- PR loop: agent reviews its own change locally, requests further agent reviews, responds to feedback and iterates until all agent reviewers are satisfied; the post calls this a Ralph Wiggum loop and links ghuntley.com/loop ("Redefining the role of the engineer").
- Entropy control: "golden principles" encoded in the repo plus recurring background Codex tasks that scan for deviations, update quality grades and open small refactoring PRs, most reviewable in under a minute and automerged ("Entropy and garbage collection").
- Minimal blocking merge gates and short-lived PRs; "Test flakes are often addressed with follow-up runs rather than blocking progress indefinitely." The post says this would be irresponsible in a low-throughput environment ("Throughput changes the merge philosophy").
Evidence and numbers: about 1M lines of code, roughly 1,500 PRs merged in five months, three engineers growing to seven, 3.5 PRs per engineer per day, estimated 1/10th of hand-written time; single Codex runs of "upwards of six hours"; before automation the team spent every Friday (20% of the week) cleaning up "AI slop".
Tools and files named: `AGENTS.md`, `docs/`, execution plans, custom linters, structural tests, Chrome DevTools Protocol, LogQL, PromQL, OpenTelemetry, `gh`, repository-embedded skills, Aardvark.
Caveats: Greenfield repo shaped by agents from the first commit. The end-to-end autonomy "should not be assumed to generalize without similar investment". The authors do not know how architectural coherence evolves over years. The relaxed merge gates conflict with the user's own rule against retrying to get to green (Inference).
Relevance: high. The clearest first-hand description of map-style AGENTS.md, docs-as-system-of-record, and lints whose error messages teach the agent.

### Using PLANS.md for multi-hour problem solving (OpenAI Cookbook, 2025-10-01) `[OAI-execplans]`
File: refs/articles/developers.openai.com/cookbook-articles-codex-exec-plans/article.md   URL: https://developers.openai.com/cookbook/articles/codex_exec_plans
Thesis: A full `PLANS.md` template ("ExecPlan") that lets Codex work for hours from one prompt. The plan is a self-contained living design document a stateless agent or a novice could execute.
Practices:
- AGENTS.md carries only a two-line pointer: "When writing complex features or significant refactors, use an ExecPlan (as described in .agent/PLANS.md) from design to implementation." (section "AGENTS.md").
- Non-negotiables: "Every ExecPlan must be fully self-contained."; living document; novice can implement end to end; must produce demonstrably working behaviour; define every term of art (section "Requirements").
- Mandatory sections: `Progress` (checkbox list with timestamps, the only place checklists are allowed), `Surprises & Discoveries`, `Decision Log`, `Outcomes & Retrospective`, plus Purpose / Big Picture, Context and Orientation, Plan of Work, Concrete Steps, Validation and Acceptance, Idempotence and Recovery, Artifacts and Notes, Interfaces and Dependencies ("Skeleton of a Good ExecPlan").
- Acceptance phrased as observable behaviour (an HTTP 200 from a named URL) not internal attributes ("added a HealthCheck struct"); "Validation is not optional." (section "Guidelines").
- During implementation the agent must not ask for "next steps"; it proceeds to the next milestone, resolves ambiguity itself and commits frequently ("How to use ExecPlans and PLANS.md").
- Prototyping milestones and spikes are encouraged to de-risk; prefer additive changes then subtractions that keep tests passing ("Prototyping milestones and parallel implementations").
- Prose first: "Prefer sentences over lists."; do not point to external docs, embed the knowledge (sections "Formatting", "Requirements").
Evidence and numbers: a similar PLANS.md "has enabled Codex to work for more than seven hours from a single prompt".
Tools and files named: `.agent/PLANS.md`, `AGENTS.md`, "ExecPlan", `gpt-5.2-codex`.
Caveats: The term ExecPlan is arbitrary and untrained; the template is long and written for 2025 models. [OAI-astra] (2026-09) warns that elaborate recipes can now hinder.
Relevance: high. A ready template for the plan artifact, and the pattern of AGENTS.md pointing to a plan spec.

### Run long horizon tasks with Codex (Derrick Choi, OpenAI Developers, 2026-02-23) `[OAI-longhorizon]`
File: refs/articles/developers.openai.com/blog-run-long-horizon-tasks-with-codex/article.md   URL: https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
(Author inferred from the linked repo `derrickchoi-openai/design-desk`; the saved file has no byline.)
Thesis: A 25-hour uninterrupted run built a design tool from a blank repo. What made it work was "durable project memory" in four markdown files plus verification at every milestone, not a clever prompt.
Practices:
- Four-file stack under `docs/`: `prompt.md` (spec: goals, non-goals, hard constraints, deliverables, "Done when"), `plans.md` (milestones small enough for one loop, acceptance criteria and validation commands per milestone, decision notes), `implement.md` (runbook: plan is source of truth, validate after each milestone, keep diffs scoped, update docs), `documentation.md` (status, decisions, how to run and demo, known issues) (section "The key idea: durable project memory").
- "Stop-and-fix rule: if validation fails, repair before moving on" (Plan.md key sections).
- Loop: plan, edit, run tools (tests/build/lint), observe, repair, update docs/status, repeat ("Why Codex can stay coherent on long tasks").
- Use git worktrees to isolate runs and keep diffs reviewable (same section).
Evidence and numbers: "Codex ran for about 25 hours uninterrupted, used about 13M tokens, and generated about 30k lines of code." GPT-5.3-Codex at Extra High reasoning.
Tools and files named: `Prompt.md`, `Plan.md`, `Implement.md`, `Documentation.md`, `/plan`, git worktrees.
Caveats: "This was an experiment, not a production rollout"; the result "was not perfect or production-ready". Single run, no comparison arm.
Relevance: high. Smallest concrete file layout for a long autonomous run.

### Codex best practices (OpenAI docs, undated, mentions GPT-6.1 Sol so current as of late 2026) `[OAI-bestpractices]`
File: refs/articles/developers.openai.com/codex-learn-best-practices/article.md   URL: https://developers.openai.com/codex/learn/best-practices
Thesis: Treat Codex as a teammate you configure over time: right context per task, AGENTS.md for durable guidance, config for consistency, MCP for external context, skills for repeated work, scheduled tasks for stable workflows.
Practices:
- Prompt with four parts: Goal, Context, Constraints, "Done when" (section "Strong first use").
- Plan first for hard tasks: Plan mode (`/plan`, Shift+Tab), ask the agent to interview you, or a `PLANS.md` template ("Plan first for difficult tasks").
- A good AGENTS.md covers repo layout, how to run, build/test/lint commands, conventions and PR expectations, constraints and do-not rules, what done means and how to verify. "A short, accurate `AGENTS.md` is more useful than a long file full of vague rules." Add rules only after repeated mistakes; when it grows, reference task-specific markdown files ("Make guidance reusable with AGENTS.md").
- "When Codex makes the same mistake twice, ask it for a retrospective and update `AGENTS.md`." (same section; line break in source between "update" and the file name).
- Layering: global `~/.codex/AGENTS.md`, repo-level, subdirectory; closest file wins (same section).
- Keep a `code_review.md` referenced from AGENTS.md so review is consistent; `/review` against base branch, uncommitted changes or a commit ("Improve reliability with testing and review").
- MCP only when context lives outside the repo or changes often; "Add tools only when they unlock a real workflow." ("Use MCPs for external context").
- Skills: one job each, start from 2 to 3 concrete use cases, description says what and when and includes trigger phrases; personal in `$HOME/.agents/skills`, team in `.agents/skills` ("Turn repeatable work into skills").
- "skills define the method and scheduled tasks define the schedule"; do not schedule a task before it is reliable manually ("Use scheduled tasks for repeated work", "Common mistakes").
- One chat per coherent unit of work; subagents for bounded exploration, tests, triage ("Organize long-running chats").
- Start with default permissions and loosen only for trusted repos ("Configure Codex for consistency").
Evidence and numbers: "At OpenAI, Codex reviews 100% of PRs."
Tools and files named: `AGENTS.md`, `~/.codex/config.toml`, `.codex/config.toml`, `PLANS.md`, `code_review.md`, `SKILL.md`, `$skill-creator`, `/init`, `/review`, `/compact`, `/fork`, `/resume`, `/subagents`, `codex mcp add`.
Caveats: Vendor documentation, no measurements. Lists eight "common mistakes", including full permissions before understanding the workflow and one chat for an entire project.
Relevance: high. Concise checklist that maps directly to a cross-harness setup (AGENTS.md, `.agents/skills`).

### Shell + Skills + Compaction: tips for long-running agents (OpenAI Developers, 2026-02-11) `[OAI-skills-shell]`
File: refs/articles/developers.openai.com/blog-skills-shell-tips/article.md   URL: https://developers.openai.com/blog/skills-shell-tips
Thesis: Ten tips for API-level skills, hosted shell and server-side compaction, from OpenAI's own work and Glean's production use.
Practices:
- Write descriptions as routing logic: when to use, when not to use, outputs and success criteria. "Your skill’s description is effectively the model’s decision boundary." (tip 1).
- Add negative examples ("Don’t call this skill when…") and edge cases; making skills available can initially reduce correct triggering (tip 2).
- Put templates and worked examples inside the skill, not the system prompt; they cost nothing until the skill triggers (tip 3).
- For determinism, name the skill explicitly: "Use the `<skill name>` skill." (tip 5).
- Security: "Combining skills with open network access creates a high-risk path for data exfiltration." Default posture: skills allowed, shell allowed, network only with a minimal per-request allowlist; treat tool output as untrusted (tip 6).
- Two-layer allowlists (org and request) and `domain_secrets` so the model sees placeholders like `$API_KEY` while a sidecar injects real values only for approved destinations (tips 8, 9).
- Write artifacts to one handoff location (`/mnt/data`): "tools write to disk, models reason over disk, developers retrieve from disk" (tip 7).
Evidence and numbers: Glean: skill routing initially dropped triggering by about 20% in targeted evals, recovered after negative examples; a Salesforce skill raised eval accuracy 73% to 85% and cut time-to-first-token 18.1%.
Tools and files named: `SKILL.md`, `/responses/compact`, `previous_response_id`, `network_policy`, `domain_secrets`, `/mnt/data`.
Caveats: API-platform oriented, customer numbers are self-reported by one early customer.
Relevance: medium. Skill-description and network-containment advice transfers; the API details do not.

### Testing Agent Skills Systematically with Evals (OpenAI Developers, 2026-01-22) `[OAI-evalskills]`
File: refs/articles/developers.openai.com/blog-eval-skills/article.md   URL: https://developers.openai.com/blog/eval-skills
Thesis: Evaluate a skill like any prompt: a prompt set, a captured run, deterministic checks on the trace, then a rubric-graded pass with structured output.
Practices:
- Define success before writing the skill in four categories: outcome, process, style, efficiency goals (section 1).
- Trigger manually first to expose triggering, environment and execution assumptions; every manual fix is a candidate eval (section 3).
- Small CSV of prompts with `id,should_trigger,prompt` covering explicit invocation, implicit invocation, contextual invocation and at least one negative control; "a small set of 10–20 prompts is enough to surface regressions and confirm improvements early" (section 4).
- Deterministic graders over `codex exec --json` JSONL traces: did it run the command, did the file exist, in what order (section 5).
- Rubric grading with a second read-only `codex exec` constrained by `--output-schema` to a JSON schema with `overall_pass`, `score`, `checks[]` (section 6).
- Extensions: command count for thrashing, token budget from `turn.completed`, build check, runtime smoke check, `git status --porcelain` cleanliness, permission regressions (section 7).
Evidence and numbers: none measured; worked example only.
Tools and files named: `codex exec --json`, `--full-auto`, `--sandbox workspace-write`, `--output-schema`, `evals/setup-demo-app.prompts.csv`, `evals/style-rubric.schema.json`, `.codex/skills/<name>/SKILL.md`, `$skill-creator`.
Caveats: Codex-specific flags; the harness-neutral part is the method.
Relevance: high. A cheap, portable recipe for regression-testing skills, including negative trigger cases.

### Rethinking skills and prompts for GPT-6 Astra (OpenAI Developers, 2026-09-11) `[OAI-astra]`
File: refs/articles/developers.openai.com/blog-rethinking-skills-and-prompts-for-gpt-6-astra/article.md   URL: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
Thesis: Instructions accumulated for older models now hurt. With each model release, prune skills, AGENTS.md and boundary language.
Practices:
- Skill descriptions: "skill descriptions should be as short as possible while making it clear when the model should use them"; with too many skills Codex shortens descriptions to fit, so the model sees less of each (section "Better skills").
- Progressive disclosure inside skills: for multi-workflow skills "make the root document a minimal router that points to supporting docs and scripts" (same section).
- Elaborate step-by-step recipes can now hinder: "overly specific guidance can now hinder results where it previously helped" (same section).
- Repository skills steer other contributors' agents on other models; consider which models will read them (same section).
- AGENTS.md: revisit each instruction. "Prompting the model to read files before every edit is a great way to burn context and slow work down." Instructions to run tests can now cause unnecessary testing ("Up-to-date AGENTS.md").
- Use AGENTS.md to grant permission for a known-safe workflow (local tests on disposable fixtures: run, fix, rerun without asking) (same section).
- Strong "ask first" language written for older models can make the new model stop too early; define completion up front if you want persistence ("Decision boundaries", "Persistence").
Evidence and numbers: none.
Tools and files named: `AGENTS.md`, `$skill-creator`.
Caveats: Specific to one model generation and one vendor; it directly contradicts earlier advice (including [OAI-bestpractices]' advice to state what done means and how to verify it and [OAI-execplans]' prescriptive template) for the newest models.
Relevance: high. The most recent statement that instruction files should shrink as models improve, and that over-triggering skill descriptions are a real failure.

### Maintaining software with the GPT-6 family (OpenAI Core Experimentation team, 2026-10-14) `[OAI-maintain]`
File: refs/articles/developers.openai.com/blog-maintaining-software-with-the-gpt-6-family/article.md   URL: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
Thesis: Agents now do large-scale maintenance (dead code, stale experiments, CI speed) from short prompts, provided each change comes with evidence and review is fanned out to owning teams.
Practices:
- Start with one small maintenance task, ask for evidence and a small draft PR, compare models and effort levels, then scale to a subdirectory, then the codebase; feed review comments into the next prompt (section "Start small, review, and expand").
- Ask the agent to write its own follow-up prompt and to prioritise findings using instrumentation (CPU cost) ("Tracking down stale experiments").
- The model escalated a finding for human review because a flag was marked "Permanent" (same section).
- Revisit prompt corrections on new model releases because they can become obsolete ("Improving cost effectiveness").
Evidence and numbers: "we merged more than 1,400 pull requests, deleting over 800k lines of code" by five engineers part-time over two weeks; a container image went from 3.31GB to 1.72GB; about 30 CI PRs took median CI from roughly 10 minutes to 4.5; "GPT-6.1 Sol Ultra produced 92% as many findings as GPT-6 Astra Ultra at 14% of the API cost."
Tools and files named: Codex, Statsig.
Caveats: "some proposals added more complexity than their expected benefit justified". The prompts themselves were images and are not in the saved text.
Relevance: medium. Evidence for scheduled maintenance loops and for testing cheaper model tiers per task.

### How we used Codex to ship Sora for Android in 28 days (OpenAI, late 2025) `[OAI-sora]`
File: refs/articles/openai.com/index-shipping-sora-for-android-with-codex/article.md   URL: https://openai.com/index/shipping-sora-for-android-with-codex/
Thesis: Four engineers shipped a production Android app in 28 days by hand-building the foundation, then letting Codex fill in code inside that structure, planning before every non-trivial change.
Practices:
- Lay the foundation by hand: architecture, modularisation, dependency injection, navigation, auth and base networking, plus a few representative features end to end; then point the agent at them ("Laying the foundation by hand").
- Reference by example: "build this settings screen using the same architecture and patterns as this other screen" worked far better than a bare request (same section).
- Understand, then plan, then implement: ask the agent to summarise how a feature works, correct its understanding, co-write a mini design doc, then apply one step at a time; save the plan to a file when the context window fills ("Planning with Codex before coding").
- Review against the plan: "we could check the implementation against our plan rather than reading a diff without context" (same section).
- Many `AGENTS.md` files through the codebase, maintained by Codex; `~/.codex/AGENTS.md` lists where sibling repos live (section "Onboarding a new senior engineer" and the section on cross-platform work).
- Parallel sessions hit Brooks's law: the bottleneck moves to decisions, feedback and integration ("Distributed engineering").
Evidence and numbers: 28 days, 4 engineers, roughly 5 billion tokens, 99.9% crash-free, "we estimate was 85% written by Codex" (phrase from "Laying the foundation by hand"), internal build in 18 days.
Tools and files named: `AGENTS.md`, `~/.codex/AGENTS.md`, GPT-5.1-Codex.
Caveats: One-shot "Build the Sora Android app based on the iOS code. Go" was tried and abandoned. Codex "couldn’t see the app actually run" at the time. The file notes Sora was discontinued on 2026-04-26.
Relevance: medium. Contradicts [OAI-harness] on who builds the foundation (humans here, agents there).

### Automating repetitive work at OpenAI with Codex (OpenAI Developers, 2026-08-25) `[OAI-runme]`
File: refs/articles/developers.openai.com/blog-automating-repetitive-work-at-openai-with-codex/article.md   URL: https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex
Thesis: An OpenAI engineer runs recurring operational work (model evaluations) by giving Codex a goal cell in a shared notebook; the notebook then holds the plan, commands, outputs, dead ends and decisions for the next run.
Practices: goal outline of four lines: review a previous run, write a detailed plan in the notebook, "Wait for me to review and approve the plan before beginning.", document commands, output and interpretation; before finishing, capture decisions "that would otherwise disappear into the conversation"; write a companion `*.index.md` so earlier runs are discoverable by agents.
Evidence and numbers: none.
Tools and files named: Runme notebooks, WebMCP, `*.index.md`, Codex persistent goal, automatic approval review.
Caveats: One person's workflow on operations tasks, not product code.
Relevance: low to medium. A small example of plan approval plus a run log that feeds the next run.

### Custom Code Review rules for Codex (OpenAI Developers, 2026-07-20) `[OAI-reviewrules]`
File: refs/articles/developers.openai.com/blog-custom-code-review-rules-for-codex/article.md   URL: https://developers.openai.com/blog/custom-code-review-rules-for-codex
Thesis: Put a few scoped, consequential, non-obvious review rules in AGENTS.md so an agent reviewer can cite them; leave mechanical checks to CI.
Practices:
- A `## Code Review Rules` section in AGENTS.md, repository-wide at the root and service-specific in nested AGENTS.md files (section "Rules as an interface").
- "Start with a consequential, non-obvious invariant." "If removing a rule would not change the review, leave it out." ("Writing rules that hold up").
- State the invariant and the safe path (for example keep the existing name or add a backward-compatible event) (same section).
- Describe outcomes, not function names; prune rules that produce noise (same section).
- "Keep formatting and other mechanical checks in CI." (same section).
- Test a rule with three PRs: one that should trigger, one safe counterexample, one unrelated ("Getting started").
Evidence and numbers: "rule-guided variants recovered 98% of the required custom findings, compared with 58.3% in the baseline control"; OpenAI weekly PR volume "has more than doubled since Q4". Evaluated on coverage, restraint, retention and actionability.
Tools and files named: `AGENTS.md` (`## Code Review Rules`, `### Breaking changes`), `@codex review`, openai/codex repo AGENTS.md lines 85 to 110.
Caveats: "Codex Code Review is still an additional reviewer; tests, branch protections, and required approvals continue to provide hard enforcement." Broad instructions "could easily create noise".
Relevance: high. A measured case for a small number of scoped review rules, and a test procedure for each rule.

### An open-source spec for Codex orchestration: Symphony (Alex Kotliarskyi, Victor Zhu, Zach Brock, OpenAI, 2026-04-27) `[OAI-symphony]`
File: refs/articles/openai.com/index-open-source-codex-orchestration-symphony/article.md   URL: https://openai.com/index/open-source-codex-orchestration-symphony/
(The article prose was read in full. Line 134 of the saved file is the embedded `SPEC.md`, about 52,000 characters with line numbers fused into the text; it was not read.)
Thesis: After harness engineering, the next bottleneck was human context switching across sessions. Symphony makes the issue tracker the control plane: every open ticket gets an agent in its own workspace until done.
Practices:
- Core invariant: "For every open task, guarantee that an agent is running in its own workspace." (section "Using Symphony to build Symphony").
- Ticket statuses in Linear act as the state machine; blocked tasks are not started, so a dependency tree of tickets runs as a DAG (example: React upgrade blocked on a Vite migration) ("Turning our issue tracker into an agent orchestrator").
- Plan ticket first: an agent analyses code, Slack or Notion and writes an implementation plan; once approved it generates a tree of tasks with dependencies (same section).
- Agents file follow-up issues for out-of-scope improvements instead of doing them (same section).
- The team workflow lives in a `WORKFLOW.md` file (check out repo, mark in progress, add PR, move to Review, attach video); Symphony makes agents follow it (section "Using Symphony to build Symphony").
- Review packet includes a video walkthrough of the feature working ("An increase in exploration").
- Give objectives, not strict transitions: "treating agents as rigid nodes in a state machine doesn’t work well" ("Progress comes with new, different problems").
- Keep the tracker token away from sub-agents by exposing a `linear_graphql` dynamic tool call instead of MCP or the token ("Using Symphony to build Symphony").
- When a ticket-level run misses, add guardrails and skills rather than patch the result ("Progress comes with new, different problems").
Evidence and numbers: "most people could comfortably manage three to five sessions at a time before context switching became painful"; landed PRs up 500% in the first three weeks on some teams; 15K GitHub stars by 2026-04-23; reference implementation in Elixir built in one shot, then re-implemented in TypeScript, Go, Rust, Java and Python to find spec ambiguities.
Tools and files named: `SPEC.md`, `WORKFLOW.md`, Linear, Codex App Server (JSON-RPC), `tmux`, `gh`, `linear_graphql`.
Caveats: Not maintained as a product. Loses mid-flight steering; "Sometimes the agent produced something that completely missed the mark." Ambiguous, judgment-heavy work stays interactive. "500%" is for "some teams".
Relevance: medium. Useful as the tracker-as-control-plane pattern and the WORKFLOW.md idea; heavier than a solo developer needs.

### Vercel

### AGENTS.md outperforms skills in our agent evals (Jude Gao, Vercel, 2026-01-27) `[VER-agentsmd]`
File: refs/articles/vercel.com/blog-agents-md-outperforms-skills-in-our-agent-evals/article.md   URL: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
Thesis: For framework knowledge missing from training data (Next.js 16 APIs), a compressed docs index placed in AGENTS.md beat a skill, because passive context removes the decision to look something up.
Practices:
- Put an index, not the docs, in AGENTS.md: a pipe-delimited list of doc file paths under `.next-docs/` that the agent reads on demand; compressed from about 40KB to 8KB with no loss in pass rate (section "Addressing the context bloat concern").
- Add one steering line: "IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning for any Next.js tasks." (section "The hunch that paid off").
- Skills are still right for "vertical, action-specific workflows that users explicitly trigger" such as a version upgrade or a migration (section "What this means for framework authors").
- Harden evals before trusting them: remove test leakage, resolve contradictions, assert on observable behaviour, and target APIs outside the training data (section "Building evals we could trust").
Evidence and numbers: "In 56% of eval cases, the skill was never invoked." Skill alone gave no improvement over baseline, and was worse on tests (58% vs 63%). An explicit instruction to use the skill raised triggering to 95%+ and pass rate to 79%. AGENTS.md index: 100% pass rate across Build, Lint and Test. Wording was fragile: "invoke first" versus "explore first" changed outcomes on the same skill. (The result tables are images and are not in the saved text.)
Tools and files named: `AGENTS.md`, `.next-docs/`, `npx @next/codemod@canary agents-md`, skills.sh.
Caveats: One framework, one eval suite, January 2026 models; the post itself says "The gap may close as models get better at tool use". The three explanations (no decision point, consistent availability, no ordering issues) are called a "working theory". [OAI-astra] later warns against forcing doc reads before every edit.
Relevance: high. Directly informs what belongs in always-loaded instructions versus skills, for exactly the user's stack.

### We removed 80% of our agent's tools (Andrew Qu, Vercel, 2025-12-22) `[VER-80pct]`
File: refs/articles/vercel.com/blog-we-removed-80-percent-of-our-agents-tools/article.md   URL: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
Thesis: An internal text-to-SQL agent (d0) with 17 specialised tools was replaced by one bash tool over a directory of semantic-layer files, plus SQL execution. It became faster, cheaper and more reliable.
Practices:
- Start with "Model + file system + goal" and add complexity only when proven necessary (section "What this means for agent builders").
- Let the model read well-structured source files with `grep`, `cat`, `find`, `ls` instead of building retrieval and validation tools around them (section "v2").
- "Every tool is a choice you’re making for the model." (section "Lessons learned").
Evidence and numbers: 5 representative queries; success 80% to 100%, 3.5x faster, 37% fewer tokens; worst case old 724 s, 100 steps, 145,463 tokens and failed, new 141 s, 19 steps, 67,483 tokens.
Tools and files named: `ToolLoopAgent`, Vercel Sandbox, Cube semantic layer (YAML, Markdown, JSON), Claude Opus 4.5.
Caveats: "This only worked because our semantic layer was already good documentation." Only five queries. Not a coding agent.
Relevance: medium. Supports fewer tools and good file structure over custom tooling.

### Building a software factory for AI SDK (Lars Grammel, Vercel, 2026-08-12) `[VER-factory]`
File: refs/articles/vercel.com/blog-building-a-software-factory-for-ai-sdk/article.md   URL: https://vercel.com/blog/building-a-software-factory-for-ai-sdk
Thesis: To clear a backlog of 1,000+ issues and almost 800 PRs, the AI SDK team built `ai-sdk-factory`: one agent per task, each producing documented evidence, with a human merging every change and review depth scaled to risk.
Practices:
- One agent per task (classification, bug reproduction, bug fix, PR review, backports, docs, feature analysis, feature implementation), each with its own prompts, context and evals. A single agent with a skill per step was tried and rejected for maintenance and troubleshooting burden (section "Build one agent per task").
- Evidence chain: the analysis agent writes and runs a failing probe (`issue-17898-type-probe.ts`) to prove the feature is missing before specifying it; the implementer runs a live end-to-end test and attaches it (sections "Analysis", "Implementation").
- Risk-scaled human review: docs fixes get a glance, provider changes focused validation, a new public API deep review (section "How do we align automation and effort to risk?").
- Assume attacker-controlled input on a public repo; every agent runs in an isolated sandbox with only the secrets its task needs, plus network shielding; "nothing is merged without approval from a human" (section "Secure everything from the start").
- Build locally through a CLI first, move to managed infrastructure once several steps are reliable (section "Build value locally, then move to the cloud").
- Classify every run as success, flawed, blocked or manual; flawed means better prompt, context or a new eval case; blocked means provision what was missing; manual marks a deliberate boundary to revisit (section "Improving the factory becomes the job").
Evidence and numbers: four weeks in, 25 to 35% of merged PRs authored by the factory; over 75% of issues closed in July closed by the factory; open issues from 1,022 to 844; over 50% of merges on the v6 release line.
Tools and files named: `ai-sdk-factory`, Vercel Sandbox, Vercel Queues, Neon Postgres, eve.
Caveats: Four weeks of data. The intro says "closes 70-80% of issues" while results say over 75% in July. Deliberately keeps the human merge.
Relevance: medium. The run-outcome taxonomy and evidence-first review packet scale down to one person.

### How we made v0 an effective coding agent (Max Leiter, Vercel, 2026-01-07) `[VER-v0]`
File: refs/articles/vercel.com/blog-how-we-made-v0-an-effective-coding-agent/article.md   URL: https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent
Thesis: v0's reliability comes from three pipeline parts around the model: a dynamic system prompt, stream rewriting ("LLM Suspense") and post-generation autofixers.
Practices:
- Inject version-specific library knowledge when intent is detected (embeddings plus keywords) instead of relying on web search, and keep the injection stable for prompt-cache hits (section "Dynamic system prompt").
- Provide hand-curated example directories in a read-only filesystem for the agent to search (same section).
- Fix known failure classes deterministically: rewrite non-existent `lucide-react` icon imports via embedding search, add missing `package.json` dependencies, AST checks for `QueryClientProvider` (sections "LLM Suspense", "Autofixers").
Evidence and numbers: "code generated by LLMs can have errors as often as 10% of the time"; autofixes run in under 250 ms; icon rewrite within 100 ms.
Tools and files named: LLM Suspense, autofixers, AI SDK, lucide-react.
Caveats: Product pipeline, not a developer setup. Web search summarised by a small model is called "a bad game of telephone".
Relevance: low. Supports deterministic post-processing and curated examples over search.

### Agent skills explained: An FAQ (Eric Dodds, Vercel, 2026-01-26) `[VER-skillsfaq]`
File: refs/articles/vercel.com/blog-agent-skills-explained-an-faq/article.md   URL: https://vercel.com/blog/agent-skills-explained-an-faq
Thesis: Reference FAQ on the Agent Skills format and how it differs from MCP, tools, rules and system prompts.
Practices:
- `SKILL.md` frontmatter: `name` 1 to 64 characters, lowercase letters, numbers and single hyphens, must match the directory name; `description` 1 to 1024 characters; optional `license`, `compatibility` (max 500 characters), `metadata`, `allowed-tools` (sections "YAML frontmatter", "Which SKILL.md frontmatter fields are optional?").
- `scripts/` for steps that must run the same way every time: "a script is often more auditable than a paragraph" (section "What is the scripts directory for?").
- `references/` loaded on demand; do not duplicate content between `SKILL.md` and `references/`; for huge reference files put grep patterns in `SKILL.md` (section "What is the references directory for?").
- Security: treat bundled scripts like any code you run, review them and pin versions (section "Are skills secure?").
Evidence and numbers: none.
Tools and files named: `SKILL.md`, `scripts/`, `references/`, `assets/`, `npx skills add <owner/repo>`, skills.sh.
Caveats: Published one day before [VER-agentsmd], which found skills often not invoked; this FAQ calls skills "the recommended approach for most teams".
Relevance: medium. Useful as a format reference.

### What we learned building agents at Vercel (Malte Ubl, 2025-11-06) `[VER-learned]`
File: refs/articles/vercel.com/blog-what-we-learned-building-agents-at-vercel/article.md   URL: https://vercel.com/blog/what-we-learned-building-agents-at-vercel
Thesis: Pick internal agent projects where humans do low-cognitive-load, high-repetition work; keep a human approval step.
Evidence and numbers: lead triage from 10 people to 1; abuse agent cut time to ticket closing 59%.
Relevance: low. Business-process agents, not coding setup. One reusable heuristic: ask "what part of your job do you hate doing the most?".

### How to build agents with filesystems and bash (Ashka Stephen, Vercel, 2026-01-09) `[VER-fsbash]`
File: refs/articles/vercel.com/blog-how-to-build-agents-with-filesystems-and-bash/article.md   URL: https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash
Thesis: Structure domain data as files and give the agent bash in a sandbox; retrieval becomes precise and context stays minimal.
Practices: map domains to directory hierarchies; agent loads files on demand with `ls`, `grep`, `cat`; agent reasoning and tool execution run on separate compute (sections "How agents read filesystems", "Mapping your domain to files").
Evidence and numbers: sales call summary agent from about $1.00 to about $0.25 per call on Claude Opus 4.5 with better output.
Tools and files named: `bash-tool`, Vercel Sandbox.
Caveats: Tested and partly contradicted by [VER-bashtest].
Relevance: low to medium. Reinforces files as the context interface.

### Testing if "bash is all you need" (Ankur Goyal, Braintrust, on Vercel blog, 2026-01-13) `[VER-bashtest]`
File: refs/articles/vercel.com/blog-testing-if-bash-is-all-you-need/article.md   URL: https://vercel.com/blog/testing-if-bash-is-all-you-need
Thesis: On structured-data questions, a SQL agent beat a bash agent at first; after fixing tools and the eval, a hybrid (bash plus SQLite) was the most reliable because it verified its own results.
Evidence and numbers: initially SQL 100% accuracy, bash 53%, basic file tools 63%; bash used 7x more tokens, cost 6.5x more and took 9x longer. Hybrid consistently 100% at roughly two times the tokens of pure SQL. Five eval questions had wrong or ambiguous expected answers.
Practices: give the agent the purpose-built tool for structured queries and a shell for exploration and verification (section "What this means for agent design"); hand-check failed eval cases because the eval itself is often wrong (section "Debugging the results").
Caveats: Single dataset (GitHub issues and PRs), Claude Sonnet 4.5.
Relevance: medium. A measured counterweight to "bash is all you need", and a reminder that evals need auditing.

### A sandbox without a network boundary is only half a sandbox (Brandon Tuttle, Vercel, 2026-08-10) `[VER-sandbox]`
File: refs/articles/vercel.com/blog-a-sandbox-without-a-network-boundary-is-only-half-a-sandbox/article.md   URL: https://vercel.com/blog/a-sandbox-without-a-network-boundary-is-only-half-a-sandbox
Thesis: Compute isolation does not stop exfiltration. A sandbox needs default-deny egress control and credentials injected outside the untrusted environment.
Practices:
- "Isolation without egress control contains the process, not its consequences." (intro).
- Phase connectivity: allow the package registry during trusted setup, remove it before generated code runs, briefly allow an output destination, end with no outbound access (section "Useful sandboxes need selective connectivity").
- Keep credentials out of the sandbox: an environment-variable credential "is a transferable bearer credential"; inject the auth header at the host firewall for one destination, optionally matched by path and method (section "Keep credentials outside untrusted compute").
- Known bypass classes: an open DNS resolver, an empty allowlist that fails open, hostname parsing differences between policy engine and proxy, a trusted package service used as a relay (section "A network bypass can be a sandbox escape").
Evidence and numbers: none.
Tools and files named: Vercel Sandbox firewall, `networkPolicy`, SNI inspection, `sandbox.update({ networkPolicy: 'deny-all' })`.
Caveats: Product post; the threat model is general.
Relevance: medium. A checklist for local sandbox and network settings: default-deny egress, no long-lived secrets inside.

### Introducing Agent Plugins (Jonathan Hefner, Vercel, 2026-08-06) `[VER-plugins]`
File: refs/articles/vercel.com/blog-introducing-agent-plugins/article.md   URL: https://vercel.com/blog/introducing-agent-plugins
Thesis: Agent Plugins 1.0.0 is a vendor-neutral packaging format: a directory with `plugin.json`, `skills/` and `mcp.json`.
Practices: only Skills and MCP servers are portable; "Other components, such as commands, hooks, and agents, remain with clients." (section "Small on purpose"). Client-specific data goes in a namespaced directory (for example `com.example.client/`).
Evidence and numbers: launch support in ChatGPT and Codex, Cursor, GitHub Copilot, Kiro, VS Code. Steering committee from AWS, Cursor, Microsoft, OpenAI, Vercel.
Caveats: Claude Code is not in the launch list in this post. Hooks and subagents are explicitly not portable.
Relevance: medium. Tells a cross-harness setup which parts can be shared (skills, MCP) and which must be per-harness (hooks, commands, agents).

### Introducing: React Best Practices (Shu Ding, Vercel, 2026-01-14) `[VER-react]`
File: refs/articles/vercel.com/blog-introducing-react-best-practices/article.md   URL: https://vercel.com/blog/introducing-react-best-practices
Thesis: 40+ React and Next.js performance rules in 8 categories ordered by impact, written for agents; rule files compile into one `AGENTS.md` and also ship as a skill.
Practices: order rules by impact (waterfalls and bundle size first); each rule has an impact rating and an incorrect/correct code pair.
Relevance: low to medium. An example of rule structure (impact rating plus before/after), installable with `npx skills add vercel-labs/agent-skills`.

### Making every harness durable (Pranay Prakash, Vercel, 2026-05-03) `[VER-durable]`
File: refs/articles/vercel.com/blog-making-every-harness-durable/article.md   URL: https://vercel.com/blog/making-every-harness-durable
Thesis: `durable-harness` wraps Pi, OpenCode, Codex and Claude Code so a session survives crashes: each model and tool call is logged as intent then outcome, and a queue resumes the turn.
Practices: mark each tool with a replay policy, `replay: 'safe'` (re-run after crash) or `'never'` (tell the model it may have run, let it check) (section "Tools"). Keep non-conversation state (to-do list, plan) as typed documents in the session log (section "Documents").
Relevance: low. Cloud infrastructure for hosted agents; the idempotency labelling idea is the transferable part.

### Thoughtworks / martinfowler.com / Kent Beck

### Harness engineering for coding agent users (Birgitta Böckeler, martinfowler.com, 2026-04-02) `[TW-harness]`
File: refs/articles/martinfowler.com/articles-harness-engineering-html/article.md   URL: https://martinfowler.com/articles/harness-engineering.html
Thesis: The user-built "outer harness" around a coding agent is a control system of guides (feedforward) and sensors (feedback), each either computational (deterministic) or inferential (LLM-based). The human steers by improving the harness whenever an issue recurs.
Practices:
- Classify every control on two axes. Guides steer before the agent acts; sensors observe after and help it self-correct. Feedback-only gives an agent that keeps repeating mistakes; feedforward-only "encodes rules but never finds out whether they worked" (section "Feedforward and Feedback").
- Make sensor output LLM-readable: "custom linter messages that include instructions for the self-correction - a positive kind of prompt injection" (same section).
- Computational sensors (tests, linters, type checkers, structural analysis) are cheap enough to run on every change; inferential ones (AI review, LLM as judge) are expensive and probabilistic, "Not on every commit." (sections "Computational vs Inferential", "Maintainability harness").
- Example table: coding conventions = feedforward, inferential (AGENTS.md, Skills); bootstrap instructions = skill plus script; code mods = OpenRewrite recipes; structural tests = pre-commit or agent hook running ArchUnit; review instructions = skills (section "Examples").
- Steering loop: "Whenever an issue happens multiple times, the feedforward and feedback controls should be improved" (section "The steering loop").
- Keep quality left: fast controls before commit (linters, fast tests, basic review agent); expensive ones post-integration (mutation testing, broad review); continuous drift sensors outside the change lifecycle (dead code, coverage quality, dependency scanners) (section "Timing: Keep quality left").
- Three regulation categories: maintainability harness (easiest, lots of existing tooling), architecture fitness harness (fitness functions), behaviour harness (hardest) (section "Regulation categories").
- Harnessability: strong typing, clear module boundaries and opinionated frameworks make a codebase easier to harness; legacy is where it is most needed and hardest (section "Harnessability").
Evidence and numbers: none measured; a mental model. Points to a follow-up article on sensors (not saved).
Tools and files named: AGENTS.md, Skills, OpenRewrite, ArchUnit, pre-commit hooks, LSP, mutation testing, "approved fixtures" pattern.
Caveats: Sensors do not reliably catch "Misdiagnosis of issues, overengineering and unnecessary features, misunderstood instructions". Relying on AI-generated tests for behaviour "puts a lot of faith into the AI-generated tests, that's not good enough yet". Open questions: keeping guides and sensors from contradicting each other; whether a silent sensor means quality or poor detection. "A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important."
Relevance: high. The most useful vocabulary for organising a setup: every piece is a guide or a sensor, computational or inferential.

### Harness Engineering - first thoughts (Birgitta Böckeler, 2026-02-17) `[TW-harness-memo]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-harness-engineering-memo-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html
Thesis: First reaction to [OAI-harness]; superseded by [TW-harness]. Groups OpenAI's harness into context engineering, architectural constraints and garbage collection, and notes what is missing.
Practices: ask "What’s your harness today?": pre-commit hook contents, ideas for custom linters, architectural constraints, structural testing frameworks such as ArchUnit (section "What’s your harness today?").
Caveats: "What I am missing in the write-up is verification of functionality and behaviour." Notes OpenAI has "a vested interest in us believing in AI-maintainable code". Attributes the term to Mitchell Hashimoto's post ("Maybe the term was an afterthought inspired by" it). Retrofitting a harness to an old codebase may be like running static analysis for the first time and "drowning in alerts".
Relevance: medium. Records the origin of the term and an independent critique of the OpenAI post.

### Context Engineering for Coding Agents (Birgitta Böckeler, 2026-02-05) `[TW-context]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-context-engineering-coding-agents-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
Thesis: A primer on context configuration features, classified by what they are (instructions versus guidance, or context interfaces) and by who decides to load them: the LLM, the human, or the agent software.
Practices:
- Who loads: LLM (skills; non-deterministic whether it loads), human (slash commands), agent software at deterministic points (hooks) (section "If and when").
- Feature map for Claude Code as of January 2026: CLAUDE.md for "most frequently repeated general conventions that apply to the whole project"; path-scoped rules to keep CLAUDE.md small; skills for lazy-loaded guidance, instructions and scripts; subagents for own-context tasks, a different model, or a second-opinion review; MCP servers for API access; hooks "When you want something to happen deterministically every single time"; plugins for distribution (section "Example: Claude Code").
- Build context up gradually: "build context like rules files up gradually, and not pump too much stuff in there right from the start" (section "How much").
- Sharing setups works better inside a team than between strangers; copied configurations cause repeated or contradictory instructions (section "Sharing context configurations").
Evidence and numbers: none.
Tools and files named: CLAUDE.md, AGENTS.md, `.claude/rules` with `paths`, slash commands (noted as deprecated in Claude Code, superseded by skills), SKILL.md, subagents, MCP, hooks, plugins.
Caveats: "Illusion of control": instructions raise probability, they do not ensure; "there are no unit tests for context engineering". Expects skills to absorb slash commands and rules. Notes a trend to replace MCP servers with skills describing CLIs.
Relevance: high. A neutral decision table for where each kind of instruction should live.

### Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl (Birgitta Böckeler, 2025-10-15) `[TW-sdd]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-sdd-3-tools-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
Thesis: "Spec-driven development" covers three different levels (spec-first, spec-anchored, spec-as-source). The three tools tried are heavy for real problem sizes, produce a lot of markdown to review, and still do not make the agent follow instructions.
Practices:
- Definitions: spec-first (write a spec, use it for the task), spec-anchored (keep the spec for later evolution), spec-as-source (humans edit only the spec) (section "Definition").
- Distinguish specs (task or feature specific) from the "memory bank" (rules files, product and codebase descriptions relevant to every session) (section "What is a spec?").
- Kiro: Requirements → Design → Tasks, one markdown file each; requirements as user stories with GIVEN/WHEN/THEN acceptance criteria; steering files `product.md`, `structure.md`, `tech.md` (section "Kiro").
- spec-kit: Constitution, then Specify → Plan → Tasks via slash commands, with templates and checklists as a definition of done per step; one branch per spec (section "Spec-kit").
- Tessl Framework: spec-as-source, one spec per code file, generated code marked `// GENERATED FROM SPEC - DO NOT EDIT`, tags `@generate`, `@test` (section "Tessl Framework").
Evidence and numbers: Kiro turned a small bug into "4 “user stories” with a total of 16 acceptance criteria". With spec-kit on a 3 to 5 point story the author judged she could have implemented the feature with plain AI-assisted coding in the same time.
Tools and files named: Kiro, spec-kit, Tessl Framework, `tessl document --code`, `tessl build`, constitution, memory bank.
Caveats: "I’d rather review code than all these markdown files." The agent ignored research notes and regenerated existing classes as duplicates, and also over-followed a constitution article. Compares spec-as-source to model-driven development: risk of "Inflexibility *and* non-determinism". Tools tried in September 2025 and may have changed.
Relevance: high. The strongest critique of heavyweight SDD; supports a small, size-scaled spec step.

### Humans and Agents in Software Engineering Loops (Kief Morris, 2026-03-04) `[TW-loops]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-humans-and-agents-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
Thesis: Humans should be "on the loop": not out of it (vibe coding) and not gatekeeping every line, but building and improving the harness that runs the how-loop.
Practices:
- The test of in-the-loop versus on-the-loop is what you do with a bad result: fixing the artefact is in the loop; "The “on the loop” way is to change the harness that produced the artefact" (section "Humans on the loop").
- Agentic flywheel: have the agent review the results of each workflow step and recommend harness improvements, first applied interactively, then queued in the backlog, later auto-approved by score (section "The agentic flywheel").
- Clean internal structure still matters because agents work faster and "spiral less" in it (section "Humans outside the loop").
Evidence and numbers: none.
Caveats: Footnote: "ralph loop" is now used loosely for leaving agents looping, but "as originally described the operator plays an important role in steering" (wording paraphrased from footnote 1). Conceptual piece.
Relevance: medium. Names the rule the user already follows: fix the setup, not just the output.

### Are Harnesses Worth the Cost? (Naresh Jain, martinfowler.com, 2026-10-13) `[TW-harness-cost]`
File: refs/articles/martinfowler.com/articles-are-harnesses-worth-the-cost-html/article.md   URL: https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
Thesis: A controlled experiment: the same API service built 10 times per condition, with and without a behavioural harness (contracts, examples, contract tests, mocks). The harness did nothing for a frontier model except add cost, but took a cheap model from 3 of 10 to 10 of 10.
Practices:
- Separate the inner loop (feedback to the agent while building) from the outer loop (independent acceptance: 178 tests the agent never sees) (section "Experiment setup").
- Give verification a source independent of the implementing agent: contract checks generated deterministically from supplied OpenAPI and AsyncAPI specs and human-supplied examples; the agent is told to fix the implementation "rather than weaken the expectations" (section "Keeping guides and sensors in sync").
- Validate guides against sensors first: an "examples validate" command checks example payloads against the specs before any test runs (same section).
- Require recorded evidence of the final verification, "rather than the agent’s claim alone" (same section).
- Recommendation: for cost-optimised models run the harness throughout development; for frontier models "run the automated tests once as a deterministic final verification gate before acceptance" (section "What this means in practice").
Evidence and numbers: GPT-6 Sol: 10 of 10 both ways; with harness 11,331,970 tokens, 19 min 53 s, about $2.679; without 1,076,371 tokens, 6 min 51 s, about $0.406 (about 10.5x tokens, 7x cost). GPT-6 Luna: without harness 3 of 10 (but 94.8% of checks passed), with harness 10 of 10 at about $0.273 versus $0.086. Harnessed Luna cost about 33% less than unharnessed Sol. Failures clustered at protocol boundaries: timeout to `202` flow, a `__TypeId__` Kafka header, `"categories": null`, `415` instead of the specified `400`, an env var name mismatch (`ORDER_API_API_KEY` vs `ORDER_API_KEY`).
Tools and files named: Specmatic, OpenAPI, AsyncAPI, CTRF reports, Codex `/goal`, Docker, an API-development skill, an agent plugin with MCP tools.
Caveats: One greenfield Java service, an unusually detailed brief, low reasoning effort, 10 runs per cell; guides and sensors were added together so their effects cannot be separated; costs exclude building and maintaining the harness. The author works at Specmatic, the tool used. The "final gate only" condition was not measured.
Relevance: high. The only controlled cost/benefit measurement of a harness in this set; argues for an independent final gate always and continuous sensors when using cheaper models.

### Maybe We Shouldn't Be Reviewing All This Code (Rachel Laycock, Thoughtworks CTO, 2026-09-02) `[TW-review]`
File: refs/articles/martinfowler.com/rachels-ramblings-code-review-html/article.md   URL: https://martinfowler.com/rachels-ramblings/code-review.html
Thesis: Code review has been overloaded with jobs (quality gate, security, architecture, mentoring). Move judgment earlier and automate what is deterministic; review by exception.
Practices: design before implementing; encode architectural constraints as fitness functions; automate formatting, linting, known security problems; reserve human review for fundamental architectural change, sensitive security boundaries, huge blast radius, unfamiliar critical code, or "I’m not confident about this" (sections "Shift the judgment left", "Review by exception").
Evidence and numbers: cites (second-hand) Meta lines per human-landed diff up 106% in a year and DX median PR size up 64%.
Caveats: Opinion piece. Rejects "an AI agent pretending to be the human reviewer" as "automating the ceremony"; this conflicts with [OAI-bestpractices] (Codex reviews 100% of PRs). Shares the worry about "cognitive and intent debt".
Relevance: medium. For a solo developer: decide which change classes get a careful human read and automate the rest.

### Why are good developers so wary of agentic development? (Rachel Laycock, 2026-10-29) `[TW-wary]`
File: refs/articles/martinfowler.com/rachels-ramblings-good-devs-wary-html/article.md   URL: https://martinfowler.com/rachels-ramblings/good-devs-wary.html
Thesis: Experienced developers' caution reflects that nobody has yet lived with agent-built systems in production. A Thoughtworks all-agent experiment showed where time goes and what broke.
Evidence and numbers: in the week-long no-hand-written-code experiment the team estimated about two thirds of time at the whiteboard and one third on the harness; the application ran but "the build was frequently red"; cites DORA 2025: AI adoption linked to higher throughput but lower delivery stability.
Practices: humans design the feedback (tests, contracts, architecture checks, pipeline) and put learning into the harness so the next run gets it right (section "A week at the whiteboard").
Caveats: Open questions the team did not settle: the role of TDD when the agent writes tests alongside code, batch size (stories to epics) versus CI capacity, how much up-front design. "Built is not the same as working in production."
Relevance: medium. A dated, honest failure report: parallel agents overwhelmed CI.

### An Accidental Blackboard (Giles Edwards-Alexander, Thoughtworks, 2026-09-02) `[TW-blackboard]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-an-accidental-blackboard-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html
Thesis: Ten engineers running many agents in one monorepo found that plan files committed to the repo, updated with progress and frequently rebased, became a shared blackboard that agents used to coordinate.
Practices: plans stored in the repo, linked to numbered spec sections, with lines marked in progress or done plus notes on how each was implemented; agents told to commit and rebase from main continually could see each other's progress and wait for dependencies (section "Emergent behaviour from tuning our approach").
Caveats: Emergent, not designed; the author is "not convinced I would be able to reliably prompt our agents into doing it again". Frequent pushes overloaded CI, and backing off removed the coordination signal. He argues the channel should sit outside source control (a project called Talwrn).
Relevance: medium. Supports plan files with status as a coordination surface for parallel worktrees; warns about CI load.

### Augmented Coding: Beyond the Vibes (Kent Beck, 2025-06-25) `[BECK-augmented]`
File: refs/articles/tidyfirst.substack.com/p-augmented-coding-beyond-the-vibes/article.md   URL: https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes
Thesis: Augmented coding keeps the hand-coding value system (tidy code, tests, coverage) while the agent types. Beck built a B+ tree library with a TDD-driven system prompt and close supervision.
Practices:
- Three warning signs to interrupt on: "Loops.", "Functionality I hadn't asked for (even if it was a reasonable next step).", and "Any indication that the genie was cheating, for example by disabling or deleting tests." (answer to "What were the warning signs").
- System prompt (Appendix 1): "Always follow the instructions in plan.md."; on "go", take the next unmarked test in `plan.md`, write it, implement only enough to pass; Red → Green → Refactor; separate structural from behavioural changes and never mix them in a commit; commit only when all tests pass and all compiler and linter warnings are resolved.
- Unsticking tactic: when the agent stalled in Rust ownership complexity, write the algorithm in Python with the same tests, then transliterate back (answer to "What was surprising about the Python version?").
Evidence and numbers: about 4 weeks; the repo is `BPlusTree3` because the first two attempts "had accumulated so much complexity that the genie completely stalled".
Tools and files named: `plan.md`, Augment Remote Agent.
Caveats: He feels "not so good about the code quality". A reader comment reports that AI "simply ignored my instructions to use a TDD cycle". June 2025 models.
Relevance: high. A compact, tested instruction set for test-first, small-commit work and a list of stop signals.

### Anchoring AI to a reference application (Birgitta Böckeler, 2025-09-25) `[TW-anchor]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-anchoring-to-reference-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html
Thesis: Keep code samples for the agent in a compilable reference application rather than in markdown, and use its commits to scope "drift detection" in other codebases.
Practices: two steps: have the agent write a drift report, edit it, then ask for the fix; scope by reference commits to avoid irrelevant comparisons; use deterministic codemods (OpenRewrite) when the change is mechanical.
Relevance: medium. Supports pointing the agent at real example code instead of prose patterns.

### I still care about the code (Birgitta Böckeler, 2025-07-09) `[TW-care]`
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-i-still-care-about-the-code-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html
Thesis: LLMs are "inferrers", not compilers, so using them is constant risk assessment over impact, probability and detectability.
Practices: the on-call test: if you were on call for the application, "at which point would you be ok with deploying a 1,000 or 5,000 LOC change set?"; minimum to stay on top of is the test code.
Relevance: medium. A three-factor rule for how much review a change needs.

### How far can we push AI autonomy in code generation? (Birgitta Böckeler and team, 2025-08-05) `[TW-autonomy]`
File: refs/articles/martinfowler.com/articles-pushing-ai-autonomy-html/article.md   URL: https://martinfowler.com/articles/pushing-ai-autonomy.html
Thesis: A multi-agent workflow could generate simple Spring Boot CRUD apps nearly unattended, but every run showed new problems ("whac-a-mole"); human oversight remained necessary.
Practices:
- Strategies tried: common stack with strong framework and established patterns; separate agents per step (requirements analyst through code reviewer) for fresh context; deterministic scripts for bootstrapping; code examples in prompts ("the most effective strategy"); a reference application served over MCP; generate-review loops; modularisation by aggregate (section "The strategies").
- Reusable prompts, static analysis on large change sets, and maximising the abstraction level (script or codemod instead of free generation) are the takeaways for supervised work (section "What you can take away").
Evidence and numbers: about 15 iterations with 3 to 5 entities, 25 to 30 minutes and $2 to 3 each ($4 to 5 with thinking); a 10-entity schema ran 4 to 5 hours with human interventions; 15 to 20 applications in total.
Failure modes named: overeagerness (unrequested endpoints and business logic), assumptions filling requirement gaps (a `priority` value set changed between runs), brute-force fixes (`@JsonIgnore`, skip the test), "Declaring success in spite of red tests", static analysis issues (TODOs left, duplicated literals). For brute-force fixes: "We don't have any idea how to prevent this."
Tools and files named: Roo Code, Kilo Code, SonarQube, MCP reference-application server, Claude Sonnet 3.7 and 4.
Caveats: Mid-2025 models; simple application. The author asks whether more control is counterproductive (the "Bitter Lesson" question). Workflow development had 10 to 20 minute feedback loops and inconsistent prompts.
Relevance: medium. A catalogue of failure modes that verification gates should target; some may be reduced with 2026 models (not tested here).

### Practitioners: Mitchell Hashimoto, Armin Ronacher

### My AI Adoption Journey (Mitchell Hashimoto, 2026-02-05) `[MH-journey]`
File: refs/articles/mitchellh.com/writing-my-ai-adoption-journey/article.md   URL: https://mitchellh.com/writing/my-ai-adoption-journey
Thesis: A six-step personal path from chat to always-on agents. Step 5 coins "harness engineering" for the habit of engineering away each agent mistake. (Step headings were lost in extraction; the steps are identifiable from the text.)
Practices:
- Definition: "anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again" (harness engineering section).
- Two forms: (1) "Better implicit prompting (AGENTS.md)" for simple things such as wrong commands or wrong APIs; in Ghostty's file "Each line in that file is based on a bad agent behavior"; (2) "Actual, programmed tools", such as scripts to take screenshots or run filtered tests, paired with an AGENTS.md line announcing them (same section).
- Three rules learned by redoing his own manual commits with an agent: split sessions into clear, actionable tasks; for vague requests separate planning and execution sessions; "If you give an agent a way to verify its work, it more often than not fixes its own mistakes and prevents regressions." (reproduce-your-own-work section).
- End-of-day agents: block the last 30 minutes to start deep research, parallel explorations of vague ideas, and issue or PR triage with `gh`; "I would NOT allow agents to respond", reports only (end-of-day section).
- Delegate known-good task types and work on something else; "turn off agent desktop notifications" so the human controls interruptions (outsourcing section).
- Know when not to use an agent; revisit that prior as models change (footnote 2).
Evidence and numbers: a background agent is running "10 to 20% of a normal working day"; triage agents usually finished in under half an hour. He runs one agent at a time and does not yet want more.
Tools and files named: `AGENTS.md` (example: ghostty `src/inspector/AGENTS.md`), `gh`, Claude Code, Amp deep mode.
Caveats: Personal account, no measurement. He worries about skill formation in juniors. States no financial ties to AI companies.
Relevance: high. Origin of the term and the simplest operating rule: every recurring mistake becomes either one AGENTS.md line or a tool.

### Vibing a Non-Trivial Ghostty Feature (Mitchell Hashimoto, 2025-10-11) `[MH-vibing]`
File: refs/articles/mitchellh.com/writing-non-trivial-vibing/article.md   URL: https://mitchellh.com/writing/non-trivial-vibing
Thesis: A complete log of the 16 agent sessions behind one shipped macOS feature, with the human planning first, cleaning up between sessions, and reviewing everything by hand.
Practices:
- Plan before prompting, and ask for a plan with no code; save it "to something like `spec.md`" and reference it in later sessions (first-session tip).
- Small chunks: prototype the UI only first, because smaller work is easier to review (first session).
- "Anti-slop" cleanup sessions after each chunk: move code, add docs, restructure; cleanup forces understanding and helps future sessions (cleanup section).
- Scaffold then fill: write a file of function stubs with descriptive names and `TODO` comments, then ask the agent to complete it (backend section).
- When the agent cannot fix a bug after a few attempts, stop: "AI is no longer the solution; it is a liability." He will not ship code he does not understand (slop zone section).
- Final prompt always asks what is missing, with "Don't write any code" and a request to consult a stronger read-only subagent (the Amp oracle) (last-prompt section).
Evidence and numbers: 16 sessions, $15.98 in tokens, about 8 hours wall clock over 3 days. One session's output was thrown away entirely ("really bad job"); four consecutive attempts at a titlebar bug failed and he changed the design.
Tools and files named: Amp, the oracle subagent, `spec.md`, `@file` mentions.
Caveats: Footnote: "Please don't ever ship AI-written code without a thorough manual review." October 2025 models.
Relevance: high. A realistic picture of session size, failure rate and the plan/implement/cleanup rhythm for a solo maintainer.

### Agentic Coding Recommendations (Armin Ronacher, 2025-06-12) `[AR-recs]`
File: refs/articles/lucumr.pocoo.org/2025-6-12-agentic-coding/article.md   URL: https://lucumr.pocoo.org/2025/6/12/agentic-coding/
Thesis: Agents succeed when tools are fast, clear and hard to misuse, the code is simple, and the ecosystem is stable.
Practices:
- Tool rules: anything can be a tool (script, MCP server, log file); tools must be fast, tell the agent clearly about misuse, be "protected against an LLM chaos monkey", and be observable (tools section).
- Put critical commands in a `Makefile`; make `make dev` refuse a second start (pidfile, error "services already running") and always tee output to a log file the agent can read (`make tail-log`) (Makefile example).
- In debug mode log emails to stdout so the agent can complete a sign-in flow from the log; tell it so in `CLAUDE.md` (logging section).
- Prefer plain scripts and CLIs to MCP; use MCP only when the alternative is too unreliable (MCP section).
- Code style for agents: functions with long descriptive names over classes, no inheritance or clever hacks, plain SQL, and "Keep important checks local" so permission checks are visible where routes are added (simple-code section).
- Be more conservative about dependency upgrades, and prefer generated code to new dependencies (stability section).
- Refactor at the right time, for example extract a component library before Tailwind classes are spread over 50 files (refactoring section).
Evidence and numbers: none; reports Go working better than Python or Rust for agents (test caching, low churn), and TanStack file routes with `$` confusing the shell.
Tools and files named: `claude --dangerously-skip-permissions` (alias `claude-yolo`), Docker, playwright-mcp, `psql`, `Makefile`, shoreman fork, `CLAUDE.md`, container-use.
Caveats: He says the post will "age very poorly". Runs with all permission checks disabled and suggests Docker to manage the risk. June 2025.
Relevance: high. Concrete dev-environment rules (single-instance dev server, log file, local checks) that are cheap to adopt.

### Agentic Coding Things That Didn't Work (Armin Ronacher, 2025-07-30) `[AR-didnt]`
File: refs/articles/lucumr.pocoo.org/2025-7-30-things-that-didnt-work/article.md   URL: https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
Thesis: Most workflow automations he built (slash commands, hooks, print mode, subagents) did not stick. Talking to the agent with more context beat elaborate pre-written prompts.
Practices:
- Automation rule: only automate what you do regularly, and delete any automation you stop using (opening list).
- Evaluate an automation by running the same task three times and judging the variance by "would I accept the result" (near the end).
- PATH interceptors instead of hooks: small scripts in `.claude/interceptors` placed first on `PATH` that print the right command and exit 1 (example: "This project uses uv, please use 'uv run python' instead.") (hooks section).
- Let slash commands read `git status` to find their target files instead of taking arguments (slash commands section).
- Subagents: good for investigation, bad for tasks mixing reads and writes (sub-tasks section).
Failed attempts listed: `/fix-bug`, `/commit` (never matched his style), `/add-tests`, `/fix-nits`, `/next-todo`; hooks gave no gains for him in yolo mode and per-Edit formatter hooks forced re-reads; print mode was slow and hard to debug.
Evidence and numbers: none measured.
Caveats: "it encourages mental disengagement": automation makes it easier to stop thinking like an engineer. July 2025 Claude Code; hooks have since gained abilities (Inference from later sources such as [HL-skillissue]).
Relevance: high. A counterweight to building many commands; supplies a deletion rule and a cheap evaluation rule.

### Skills vs Dynamic MCP Loadouts (Armin Ronacher, 2025-12-13) `[AR-skillsmcp]`
File: refs/articles/lucumr.pocoo.org/2025-12-13-skills-vs-mcp/article.md   URL: https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
Thesis: He moved all MCP servers to skills. Skills add no tool definitions, only a short summary and a pointer to a manual for using tools the agent already has.
Practices: have the agent write its own tool as a skill and maintain it, so it stays under your control; MCP tool descriptions are "both too long to eagerly load it, and too short to really tell the agent how to use it"; MCP servers change tool descriptions at will, which breaks skill files that document them.
Evidence and numbers: loading the Sentry MCP cost "around 8k tokens out of the box".
Tools and files named: mcporter, `.mcp.json`, Sentry MCP, Playwright skill.
Caveats: Personal experience; he expects this to change. Partly revised in [AR-codemode].
Relevance: medium. Supports CLI-plus-skill over MCP for a solo setup.

### Agent Design Is Still Hard (Armin Ronacher, 2025-11-21) `[AR-hard]`
File: refs/articles/lucumr.pocoo.org/2025-11-21-agents-are-hard/article.md   URL: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
Thesis: Lessons from building agents: SDK abstractions break, explicit caching is preferable, reinforcement inside the loop does heavy lifting, failures need isolation, a shared file system is the key building block, and evals remain unsolved.
Practices: inject reminders of the objective and task status in tool results; Claude Code's todo tool is "basically just an echo tool" that works as self-reinforcement; run failure-prone iteration in a subagent and report back only success plus a brief note on what did not work; keep the system prompt static for caching and send dynamic data in a later message; avoid dead ends by giving all tools the same file system.
Caveats: "We find testing and evals to be the hardest problem here." Context editing invalidates caches.
Relevance: low to medium. For agent builders; the reinforcement and failure-isolation ideas explain why todo lists and subagents help.

### What is Codemode (Armin Ronacher, 2026-10-06) `[AR-codemode]`
File: refs/articles/lucumr.pocoo.org/2026-10-6-codemode/article.md   URL: https://lucumr.pocoo.org/2026/10/6/codemode/
Thesis: Pi 1.0 added MCP support through "Codemode": the model writes JavaScript that calls tools inside a sandbox on the harness side, so calls compose without passing every result through the context.
Practices: separate the trusted harness ("brain") from the execution environment ("hands"); sandboxing bash does not sandbox the harness; MCP tools are not exposed to the model directly but discovered by tool search inside Codemode; probe 5 to 10 items, then script the rest. MCP servers should return structured content with `outputSchema` and consistent result shapes.
Caveats: MCP via Codemode works "not amazingly well" yet; durability is harder; the pattern does not work well with smaller models. He says this is not a reversal of his CLI-first advice.
Relevance: low to medium. Signals where harness tool-calling is heading in late 2026; little to configure today.

### Fast and Hard Code (Armin Ronacher, 2026-08-22) `[AR-fast]`
File: refs/articles/lucumr.pocoo.org/2026-8-22-fast-hard-code/article.md   URL: https://lucumr.pocoo.org/2026/8/22/fast-hard-code/
Thesis: With agents, language familiarity matters less, so people pick "hard" languages (Rust, Zig) and technologies for speed and size.
Relevance: low. Context for the user's Rust work; no setup practices.

### Pi: The Minimal Agent Within OpenClaw (Armin Ronacher, 2026-01-31) `[AR-pi]`
File: refs/articles/lucumr.pocoo.org/2026-1-31-pi/article.md   URL: https://lucumr.pocoo.org/2026/1/31/pi/
Thesis: Pi is a deliberately minimal coding agent (shortest system prompt he knows, four tools: Read, Write, Edit, Bash) that the agent extends by writing its own extensions and skills.
Practices:
- Ask the agent to extend itself instead of downloading extensions or skills; "they are hand-crafted by my clanker and not downloaded from anywhere" (near the end).
- Throw skills away when unused (same section).
- Agent review before human review: a `/review` extension branches into a fresh context, gets findings, brings fixes back; the prompt calls out things he cares about, such as newly added dependencies (extensions list).
- To-do items as markdown files in `.pi/todos` that sessions can claim; he prefers this to Beads' implementation (extensions list).
- No plan mode: encourage the agent to ask questions in prose; `/answer` collects them into an input box (extensions list).
- Enforce `uv` over `pip` with both a skill and an extension that intercepts `pip` and `python` calls (near the end).
Tools and files named: Pi, OpenClaw, mcporter, `.pi/todos`, `/answer`, `/todos`, `/review`, `/control`, `/files`, CDP browser skill.
Caveats: A fan's description of one tool. Slash commands were being migrated to skills "to see if this works equally well".
Relevance: medium. Shows a small core plus self-written skills, and pairing a prose instruction with a mechanical interceptor.

### HumanLayer (Dex Horthy, Kyle)

### Getting AI to Work in Complex Codebases, also known as Advanced Context Engineering for Coding Agents (Dex Horthy, HumanLayer, August 2025) `[HL-ace]`
File: refs/articles/raw.githubusercontent.com/humanlayer-advanced-context-engineering-for-coding-agents-main-ace-fca-md/article.md   URL: https://raw.githubusercontent.com/humanlayer/advanced-context-engineering-for-coding-agents/main/ace-fca.md
(No date in the saved file; images dated 2025-08-29 and a reference to a talk "on August 20th" place it in late August 2025.)
Thesis: Brownfield work with agents succeeds when the whole workflow is designed around context management ("frequent intentional compaction") through research, plan and implement phases, with human review concentrated on research and plans.
Practices:
- Keep context utilisation "in the 40%-60% range" and compact deliberately into artifacts (section "What works even better: Frequent Intentional Compaction").
- Research: understand the relevant files and information flow, output a research document. Plan: exact steps, files to edit, and "being super precise about the testing / verification steps in each phase". Implement: phase by phase, compacting status back into the plan file after each verified phase (same section).
- Only the implement step needs a git worktree; research and planning happen on main (same section).
- Intentional compaction prompt: write progress to `progress.md` with end goal, approach, steps done and current failure, then start a fresh context (section "Slightly Smarter: Intentional Compaction").
- Optimise the context window for correctness, completeness, size, trajectory; worst is incorrect information, then missing information, then noise (section "Why obsess over context?").
- Subagents are "about context control", not role-play: use a fresh window for finding, searching and summarising, and return a compact result (section "Back to compaction: Using Sub-Agents").
- Leverage hierarchy: "a bad line of a **plan** could lead to hundreds of bad lines of code", and a bad line of research to thousands; review research and plans first (section "On Human Leverage").
- Throw away bad research and rerun with more steering (section "The research").
Evidence and numbers: a bug fix in a 300k LOC Rust codebase (BAML) approved by the maintainer; 35k LOC for cancellation and WASM in about 7 hours by two people (one PR merged, one still open at writing); the plan built with research fixed the bug "in the *best* place" compared with a no-research plan; team of three spends about $12k per month on Opus; an intern shipped 2 PRs on day one.
Tools and files named: `.claude/commands/research_codebase.md`, `create_plan.md`, `implement_plan.md`, `thoughts/shared/research/`, `thoughts/shared/plans/`, `progress.md`, Claude Code `Task()` subagents, Ralph loop.
Caveats: "You have to engage with your task when you're doing this or it WILL NOT WORK." A 7-hour attempt to remove Hadoop from parquet-java failed because research did not go deep enough and nobody was a codebase expert. The team lost two weeks to a race condition. He says the approach "probably isn't" right for most teams. Vendor of a tool built on the method. Dex later reported problems with reading plans instead of code (from a search summary of a 2026 podcast, not a saved source).
Relevance: high. The origin of research-plan-implement with concrete artifacts and an honest failure section.

### Writing a good CLAUDE.md (Kyle, HumanLayer, 2025-11-25) `[HL-claudemd]`
File: refs/articles/humanlayer.dev/blog-writing-a-good-claude-md/article.md   URL: https://www.humanlayer.dev/blog/writing-a-good-claude-md
Thesis: CLAUDE.md (or AGENTS.md) is the one file in every session, so it should be short, universally applicable and hand-written, covering WHAT, WHY and HOW, with everything else disclosed progressively.
Practices:
- Instruction budget: frontier thinking models follow about 150 to 200 instructions with reasonable consistency (citing arXiv 2507.11538); Claude Code's system prompt already has about 50; as count rises, adherence drops uniformly, so the model begins to "ignore all of them uniformly" (section "Less (instructions) is more").
- Claude Code wraps CLAUDE.md in a system reminder saying the context "may or may not be relevant", so non-universal content raises the chance the whole file is ignored (section "Claude often ignores CLAUDE.md").
- Length: "general consensus is that < 300 lines is best, and shorter is even better"; HumanLayer's root file is under sixty lines (section "CLAUDE.md file length & applicability"; the source escapes the `<` as `\<`).
- Progressive disclosure: an `agent_docs/` folder (`building_the_project.md`, `running_tests.md`, `code_conventions.md`, `service_architecture.md`, `database_schema.md`, `service_communication_patterns.md`) listed in CLAUDE.md with one-line descriptions (section "Progressive Disclosure").
- "Prefer pointers to copies": use `file:line` references, not code snippets, because snippets go stale (same section).
- "Never send an LLM to do a linter's job": no style guides in CLAUDE.md; use a formatter and linter, optionally a `Stop` hook that runs them and shows errors (section "Claude is (not) an expensive linter").
- Do not use `/init` or auto-generate the file (section "Don't use /init").
Evidence and numbers: the instruction counts above, from one cited paper and their own reading of the harness.
Tools and files named: `CLAUDE.md`, `AGENTS.md`, `agent_docs/`, `ANTHROPIC_BASE_URL` logging proxy, `Stop` hook, Biome, slash commands.
Caveats: "Your mileage may vary." The instruction-budget research "hasn't been investigated in an incredibly rigorous manner". Conflicts with [OAI-bestpractices], which recommends `/init` as a starting point, and with [VER-agentsmd], which puts a docs index in the file.
Relevance: high. The clearest statement of what to keep out of the always-loaded file.

### Context-Efficient Backpressure for Coding Agents (Dex Horthy, HumanLayer, 2025) `[HL-backpressure]`
File: refs/articles/humanlayer.dev/blog-context-efficient-backpressure/article.md   URL: https://www.humanlayer.dev/blog/context-efficient-backpressure
(Metadata says 2025-09-12; the byline in the text says December 9, 2025.)
Thesis: Verification output should cost almost no context on success and show full detail only on failure.
Practices:
- `run_silent "<description>" "<command>"`: capture output to a temp file, print `✓ description` on exit 0, otherwise print `✗ description` and the full output (section "a pretty dumb fix").
- Fail fast: `pytest -x`, `jest --bail`, `go test -failfast`, so the agent sees one failure at a time (section "make it smaller over time").
- Filter stack frames and timing noise; run these checks in a pre-push hook and a subset per plan phase (same section).
- Watch for models piping tests to `head -n 50` or `/dev/null`, which forces reruns of long suites (section "im tired of context-anxious models").
Evidence and numbers: a passing test run can waste 2 to 3% of the context window; refers to a "~75k token" smart zone for Claude models.
Tools and files named: `hack/run_silent.sh` in humanlayer/humanlayer.
Caveats: "Not a full fix"; the token comparison uses an unofficial tokenizer.
Relevance: high. A ten-line wrapper that applies directly to typecheck, lint and test commands.

### Skill Issue: Harness Engineering for Coding Agents (Kyle, HumanLayer, 2026-03-12) `[HL-skillissue]`
File: refs/articles/humanlayer.dev/blog-skill-issue-harness-engineering-for-coding-agents/article.md   URL: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
Thesis: Most agent failures are configuration problems. The post assigns each configuration surface one job: AGENTS.md for universal onboarding, MCP for tools, skills for progressively disclosed knowledge, sub-agents for context control, hooks for control flow, back-pressure for verification.
Practices:
- AGENTS.md: answers the ETH Zurich study of 138 agent files (LLM-generated files hurt and cost 20%+ more; human-written helped about 4%; directory listings did not help) by restating: hand-write, few instructions, universally applicable, progressive disclosure. "Our CLAUDE.md is under 60 lines." (section "The ETH Zurich Study").
- MCP: tool descriptions go into the system prompt, so "never connect to one you don’t trust"; turn off servers you are not using; prefer a CLI when one is well represented in training data (GitHub, Docker, databases) (sections "MCP Servers Are for Tools", "Too Many Tools Is Bad").
- Replace a broad MCP server with a small CLI plus about six usage lines in CLAUDE.md (their Linear CLI example) (section "Always Be Context-Engineering").
- Skills: treat registries "like you'd treat `npm install random-package`"; registries have distributed hundreds of malicious skills (section "Skills Are for Reusable Knowledge").
- Sub-agents: role-based ones ("frontend engineer", "backend engineer") "doesn't work"; use them as a "context firewall" for locating code, analysing patterns, tracing flows and research; they return condensed answers with `filepath:line` citations; run the parent on an expensive model and sub-agents on cheaper ones (section "Sub-Agents Are for Context Control").
- Hooks: notifications, approvals (auto-deny any Bash call that runs migrations, with an instruction to ask the user), integrations, verification. Example `Stop` hook runs Biome and TypeScript typecheck in parallel, silent on success, exit code `2` with errors on stderr to re-engage the agent (sections "Hooks Are for Control Flow", "An Example Hook").
- Back-pressure: typecheck and build, unit and integration tests, coverage (a `Stop` hook prompts the agent if coverage drops), UI checks with Playwright or agent-browser; all must be context-efficient (section "Back-Pressure Increases Your Chances of Success").
- Process: "Starting simple and adding configuration only when the agent actually failed"; throw away what does not help (section "Closing Notes").
Evidence and numbers: early on, running the full suite after every change put 4,000 lines of passing tests into context and the agent lost the task; Terminal Bench 2.0 example of Opus 4.6 at #33 in Claude Code and #5 in another harness (cited from Viv Trivedy).
What did not work: designing the ideal harness up front; installing dozens of skills and MCP servers "just in case"; running the full 5+ minute suite at the end of every session; micro-optimising which sub-agent gets which tool.
Tools and files named: `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, `Stop` hook, `$CLAUDE_PROJECT_DIR`, Biome, turbo, Linear CLI, agent-browser, `Explore` sub-agent.
Caveats: Credits the term "harness engineering" to Viv Trivedy and quotes Hashimoto's definition; calls it a subset of context engineering, which other sources nest the other way round ([TW-harness] calls the outer harness a system of controls broader than context). Says Codex lacks a hooks equivalent, which was true in March 2026; the Agent Plugins post [VER-plugins] later confirms hooks remain client-specific.
Relevance: high. The most complete single map from failure type to configuration surface, with a working Stop hook.

### A Brief History of Ralph (Dex Horthy, HumanLayer, January 2026) `[HL-ralph]`
File: refs/articles/humanlayer.dev/blog-brief-history-of-ralph/article.md   URL: https://www.humanlayer.dev/blog/brief-history-of-ralph
(Metadata says 2026-06-01; the byline says January 6, 2026.)
Thesis: A timeline of the Ralph technique from June 2025 to January 2026 with lessons from using it.
Practices and lessons:
- The point of Ralph "is not "run forever" but in "carve off small bits of work into independent context windows"" (December 2025 section).
- Bad specs give poor results; "if you are iterating/exploring, you probably don't want ralph in the first place" (August 2025 lessons).
- For existing codebases keep the change set manageable: run desired-state loops once on a cron overnight and merge small iterations (August 2025 refactor lesson).
- Code is cheap: instead of rebasing a stale Ralph PR, rerun the loop on fresh code (same section).
- Standards-driven refactor: write `REACT_CODING_STANDARDS.md` with an expert in about an hour, then loop on "make sure the code base matches the standards" (same section).
Evidence and numbers: a 6-hour loop produced a refactor plan and completed it; the PR was never merged because of conflicts. A Ralph-built GTD tool "sucked" because he read neither specs nor code.
Caveats: Critical of Anthropic's official ralph-wiggum plugin: it needs `--dangerously-skip-permissions`, installs an opaque stop hook, and breaks if its state file is deleted. "Overbaking": left too long, Ralph adds bizarre features (post-quantum cryptography support).
Relevance: medium. Useful limits on when a loop fits: clear desired state, small nightly change sets.

### Long-Context Isn't the Answer (Kyle, HumanLayer, 2026-03-23) `[HL-longctx]`
File: refs/articles/humanlayer.dev/blog-long-context-isnt-the-answer/article.md   URL: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
Thesis: After trying Opus 4.6 with a 1M window they went back to Opus 4.5: instruction adherence was worse even at short lengths, because the instruction budget does not scale with the window.
Practices: keep each window small through sub-agents, progressive disclosure and quiet verification; their tool now warns at the 100k token mark regardless of window size ("only 10% of the context window" for a 1M model); a `subagent-orchestrator` skill tells the main agent to delegate all non-trivial operations (research to locator and analyzer sub-agents, noisy bash to a Bash sub-agent).
Evidence and numbers: observational over "a couple of weeks"; no measurements of their own.
Caveats: Model-specific (March 2026) and anecdotal. Other researchers' corpus includes Anthropic's own 1M-context guidance, which may disagree.
Relevance: medium. Supports a fixed token threshold for compaction or handoff rather than a percentage.

### Context Forking to Save Time, Tokens and Trouble (Kyle, HumanLayer, 2026-05-15) `[HL-fork]`
File: refs/articles/humanlayer.dev/blog-context-forking-to-save-time-trouble-and-tokens/article.md   URL: https://www.humanlayer.dev/blog/context-forking-to-save-time-trouble-and-tokens
Thesis: Treat the context window as a stack you can only push to or pop from; rewinding or forking reuses good built-up context.
Practices: three uses: rewind to re-steer after a miss; fork after research to explore several designs; rewind to before a context-wasteful operation (for example the agent reading 40,000 tokens of output).
Relevance: medium. A cheap habit: fork after research, rewind instead of correcting in place.

### Getting Claude to Actually Read Your CLAUDE.md (Dex Horthy, HumanLayer, 2026-03-17) `[HL-importantif]`
File: refs/articles/humanlayer.dev/blog-stop-claude-from-ignoring-your-claude-md/article.md   URL: https://www.humanlayer.dev/blog/stop-claude-from-ignoring-your-claude-md
Thesis: Wrapping conditional sections of CLAUDE.md in `<important if="condition">` tags improved adherence for him.
Practices: do not wrap universal content (project identity, structure, stack); make conditions narrow, for example `<important if="you are writing or modifying tests">`; a skill automates the rewrite (`npx skills add humanlayer/skills --skill improve-claude-md`).
Caveats: "We don't have a rigorous explanation for why this helps." Anecdotal; Claude Code specific. Path-scoped rules ([TW-context]) are the mechanical alternative (Inference).
Relevance: medium. Worth a test, not a default.

### 12-Factor Agents README (Dex Horthy, HumanLayer, 2025) `[HL-12factor]`
File: refs/articles/raw.githubusercontent.com/humanlayer-12-factor-agents-main-readme-md/article.md   URL: https://raw.githubusercontent.com/humanlayer/12-factor-agents/main/README.md
Thesis: Good production agents are "mostly just software" with LLM steps at the right points; the README lists twelve factors (own your prompts, own your context window, own your control flow, compact errors into context, small focused agents, stateless reducer, and others) but the detail is in linked files that were not saved.
Evidence and numbers: builders using frameworks reach a "70-80% quality bar" then start over (anecdotal, from about 100 conversations).
Relevance: low for a coding setup. It is about building agents; only the factor names were available.

### Geoffrey Huntley

### Ralph Wiggum as a "software engineer" (Geoffrey Huntley, 2025-07-14) `[GH-ralph]`
File: refs/articles/ghuntley.com/ralph/article.md   URL: https://ghuntley.com/ralph/
Thesis: Ralph is a bash loop that feeds the same prompt file to a coding agent forever (`while :; do cat PROMPT.md | claude-code ; done`). Each iteration gets a fresh context, loads the same specs and plan, does one thing, verifies and commits. The operator tunes the prompt by watching failures.
Practices:
- "One item per loop." Ask for one thing per iteration and let the agent choose the most important item from the plan; relax only when it is going well (section "one item per loop").
- "deterministically allocate the stack the same way every loop": always load the plan (`fix_plan.md`) and the specs (`specs/*`) (section "first some fundamentals").
- Specs come from a long requirements conversation, then are written one per file into a specifications folder (same section).
- Keep the main context as a scheduler: push searching and summarising to subagents; allow many subagents for search and writes but "only 1 subagent for build/tests" to avoid bad back pressure (section "extend the context window").
- "don't assume it's not implemented": tell the agent to search before creating, because ripgrep-based search can miss existing code and cause duplicate implementations (section of that name).
- Back pressure: "Anything can be wired in as back pressure to reject invalid code generation" (types, tests, static analysers, security scanners); the wheel must turn fast; for dynamic languages wire in a type checker (section "phase two: backpressure").
- After a change, run only the tests for the unit changed (same section).
- Have the agent document why each test matters, as notes for future loops that lack the reasoning (section "capture the importance of tests in the moment").
- Self-improvement: update `AGENT.md` with learned commands "but keep it brief", and record every noticed bug in `fix_plan.md` (section "ralph can take himself to university"). The prompt also says not to put status reports in `AGENT.md` (prompt item ending "DO NOT PLACE STATUS REPORT UPDATES INTO @AGENT.md").
- Separate planning loops (regenerate the TODO list by comparing code with specs, searching for TODO and placeholder implementations) from building loops; he deletes and regenerates the TODO list often (section "the todo list").
- Commit and push when tests pass; tag when build and tests are clean; on a broken morning, decide between `git reset --hard` and rescue prompts (section "you will wake up to a broken code base").
Evidence and numbers: built the CURSED programming language this way; cites the repomirror write-up (six repos shipped overnight). Context budget "approximately 170k".
Tools and files named: `PROMPT.md`, `fix_plan.md`, `specs/*`, `AGENT.md`, Amp oracle, subagents.
Caveats: "There's no way in heck would I use Ralph in an existing code base"; greenfield only, expect "90% done". "you'll wake up to a broken codebase". Models tend to placeholder implementations. A duplicated keyword in his lexer spec wasted a month. Needs "senior expertise guiding Ralph". The full prompt relies on shouting and long runs of 9s for priority, a style [OAI-astra] says newer models over-react to (Inference).
Relevance: high as a pattern (fresh context per task, fixed spec plus plan stack, back pressure), low as a literal overnight loop for a brownfield product.

### everything is a ralph loop (Geoffrey Huntley, 2026-01-17) `[GH-loop]`
File: refs/articles/ghuntley.com/loop/article.md   URL: https://ghuntley.com/loop/
Thesis: Ralph is a mindset: program the loop rather than build "brick by brick". Single process, single repo, one task per loop; no multi-agent communication needed.
Practices: "watch the loop"; when a failure domain appears, fix it "so it never happens again"; running the loop manually with a pause (CTRL+C to progress) still counts.
Caveats: Promotional and sweeping ("software development is dead - I killed it"). No data. Calls Gas Town "level 8" orchestration and his own Loom "level 9".
Relevance: low to medium. Confirms the supervised, one-task-per-iteration reading of Ralph that [OAI-harness] links to.

### nobody should type code by hand anymore. here's what's left. (Geoffrey Huntley, 2026-10-13) `[GH-agency]`
File: refs/articles/ghuntley.com/agency/article.md   URL: https://ghuntley.com/agency/
(The saved text ends after part 1 of 4; the parts on verification and skill packs are not in the file.)
Thesis: The models are no longer the constraint; "what's left is vision, verification and agency". The summary line says "Delete your skill packs, put the whole system under test".
Evidence: anecdote that the missing 20% of early agent output was "completeness and verification" (stubs and partial implementations), and "We don't get stubs anymore."
Relevance: low. Mostly career commentary in the part that was saved; the practical parts were not captured.

### --help on your CLI is all you need for LLM context until you don't. (Geoffrey Huntley, 2026-10-09) `[GH-tier]`
File: refs/articles/ghuntley.com/tier/article.md   URL: https://ghuntley.com/tier/
Thesis: Tools the model already knows from training (for example `gh`) need no skill or MCP. For a new tool, build a good CLI and optimise its `--help` so a model can reach outcomes by walking subcommands with the fewest tool calls.
Practices: measure whether a model can complete tasks from `--help` alone and tune the wording in a loop; publish docs so one web search answers the agent's question.
Relevance: medium. For the user's own scripts: invest in `--help` text and test it with an agent instead of writing a skill.

### the eighteen-month recap (Geoffrey Huntley, talk of May 2026, posted 2026-09-27) `[GH-recap]`
File: refs/articles/ghuntley.com/eighteen-month-recap/article.md   URL: https://ghuntley.com/eighteen-month-recap/
Thesis: Industry and labour-market commentary: software development now costs less than minimum wage; hire for curiosity about how agents work.
Relevance: low. No setup practices. One line worth keeping: "Removing waste from your organization and processes is a bigger accelerator than AI itself."

### ghuntley.com/stdlib and ghuntley.com/specs (Geoffrey Huntley, 2025-02 and 2025-03) `[GH-stdlib]`
Files: refs/articles/ghuntley.com/stdlib/article.md, refs/articles/ghuntley.com/specs/article.md
Only the opening paragraphs were captured (1,225 and 689 characters); the bodies appear to be behind a membership wall. The visible text says the "stdlib" (a library of rules) plus "specs" methods work best with a language that gives compiler soundness and good compiler errors. Not usable as evidence beyond that.

### Steve Yegge

### Introducing Beads: A coding agent memory system (Steve Yegge, 2025-10-13) `[SY-beads]`
File: refs/articles/steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a/article.md   URL: https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a
Thesis: Markdown plan files rot and confuse agents across sessions. A small issue tracker (`bd`) with first-class dependencies, stored in git, gives agents queryable external memory and stops discovered work from being lost.
Practices:
- Replace markdown plans with issues that have parent/child (epic) and blocking links; the agent queries ready work (`bd ready --json`) instead of interpreting prose (sections "It’s Issues All The Way Down", Appendix A).
- One line in `AGENTS.md` or `CLAUDE.md` telling the agent to run `bd quickstart` is the whole integration (section "The End of Lost Work").
- File discovered problems as issues linked with `discovered-from`, instead of ignoring "unrelated" failures (same section and Appendix A).
- Make sessions throwaway: kill the agent after each issue; fine-grained issues keep each session near the start of its context window (section "Famous Last Words").
- Claim work with `status: in_progress` so multiple agents do not collide (Appendix A).
Evidence and numbers: before Beads he had "six hundred and five" decaying plan files; he ripped out 70 thousand lines of plan-management code; a 350k-line orchestrator was abandoned; converting an old TODO list produced 128 issues in half an hour. Running a dozen concurrent agents "was only sustainable for about 2 weeks"; he went back to 1 to 3.
Failure modes named: nested phase plans lose the outer plan after compaction ("Descent Into Madness"); near the context limit agents disavow failing tests as "pre-existing", disable tests, or build side databases ("Famous Last Words"); Claude deleting the database with `DROP TABLE`.
Tools and files named: `bd`, Beads, JSONL in git, SQLite, `AGENTS.md`, `CLAUDE.md`.
Caveats: Alpha software at the time; written a week after invention; the appendix is Claude describing why it likes the tool. He says "GitHub Issues doesn’t work" without evidence. [AR-pi] criticises the Beads implementation and uses markdown to-do files instead; [SY-v1] admits the original SQLite plus JSONL sync was "janky" with merge conflicts.
Relevance: high. The problem statement (plans rot, discovered work is lost, sessions should be disposable) is well evidenced; the specific tool is optional.

### Welcome to Gas Town (Steve Yegge, 2026-01-01) `[SY-gastown]`
File: refs/articles/steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04/article.md   URL: https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
Thesis: Gas Town is an orchestrator for 20 to 30 Claude Code instances with seven agent roles, all state in Beads, and workflows expressed as chains of issues so work survives session death.
Practices:
- Roles: Mayor (the agent you talk to), Polecats (ephemeral workers that produce merge requests), Refinery (merges one change at a time through a merge queue), Witness (unsticks workers), Deacon and Dogs (patrol and maintenance loops), Crew (long-lived named agents for interactive work) (section "Gas Town 101").
- Durable workflows: "molecules" are checklists encoded as chained issues the agent must close one at a time, so a crash or compaction resumes at the next open step (example: a 20-step release process agents used to skip steps in) (section "Molecular Expression of Work").
- "an agent is not a session": identity, hook and mail persist in git; sessions are disposable; any session can "hand off" and restart (sections "Gastown Universal Propulsion Principle", "Gas Town Workflow").
- Review amplification: a "Rule of Five" formula makes each step get reviewed four more times with different focus areas (section "Planning in Gas Town").
- An eight-stage ladder of adoption from near-zero AI to building an orchestrator; Gas Town is for stage 6 or 7 and up (section "WARNING DANGER CAUTION").
Evidence and numbers: 17 days old, 75k lines, 2000 commits at launch; fourth orchestrator attempt of 2025; "I’ve never seen the code".
Caveats (the author's own): "Some bugs get fixed 2 or 3 times"; "some work gets lost"; "expensive as hell" (multiple Claude accounts); agents often ignore the instruction to run their hook, so the system nudges them through tmux; "Do not use Gas Town." The planning bottleneck moves to the human: it "churns through implementation plans so quickly" that design work cannot keep up.
Relevance: low for adoption, medium for ideas: merge queue agent, checklist-as-issues for long procedures, sessions as disposable.

### Gas Town: from Clown Show to v1.0 (Steve Yegge, 2026-04-03) `[SY-v1]`
File: refs/articles/steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec/article.md   URL: https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec
Thesis: Three months on, Beads and Gas Town reach 1.0; Beads moved to Dolt; the value of the Mayor is that one agent reads the workers' output so the human does not have to.
Practices: Beads as "the Why" alongside git's what/where/who/how: a versioned ledger of work items and their history (section "Beads is the Missing Why").
Evidence and numbers: Beads over 20k GitHub stars, Gas Town 13k; early versions had "serial killer sprees" (the Deacon killing workers mid-job) and a "22-nose Clown Show" where the Mayor had repeated "massive data loss".
Caveats: Promotional. Admits the v0 architecture had "bidirectional sync, 3-way merge, two sources of truth, race conditions". Gas Town is in maintenance mode in favour of a successor (Gas City).
Relevance: low to medium. Documents real failure history of a popular orchestrator and of git-synced task storage.

### Fences, not Sandboxes (Steve Yegge, 2026-08-24) `[SY-fences]`
Files: refs/articles/yegge.ai/essays-fences-not-sandboxes/article.md (full text); refs/articles/steve-yegge.medium.com/fences-not-sandboxes-5719cd9b04bd/article.md (teaser only)   URL: https://yegge.ai/essays/fences-not-sandboxes/
Thesis: Running 50 to 60 agents on one product, his agents built a system of written rules with a lifecycle and mechanical enforcement. He argues agents should be governed by explicit rules and polite refusals ("fences") rather than containment.
Practices:
- Rule lifecycle that tightens on repeat violation: "first custom, then advisories/warnings, then written law in the constitution that all agents must obey, and finally, mechanical enforcement" (section "The Rise of Rule of Law").
- A fence is "any mechanism that turns you away if you aren't supposed to be there": a program that refuses by policy, for example only one model tier may message humans, enforced at the Slack and email boundary (section "Fences, not Sandboxes").
- Record each clarification and incident postmortem as a ruling; prune obsolete rulings (he added a role for that) (section "The Rise of Rule of Law").
Evidence and numbers: about 270 commits per day through the merge queue (capacity 500); the factory is about 600k lines, "mostly bash", approaching 1:1 with the product; 450 "legal artifacts"; over 100 fences; equivalent of $122k per month in API tokens through 21 subscription accounts.
Caveats: "every morning, when I've left it to its own devices overnight, it has made at least one terrible decision"; one agent did an unplanned release "that broke everyone". He rates the best model's judgment as "approximately a sixth grader". The rule base accumulated cruft and needed pruning. "Not a sandbox" contradicts [VER-sandbox] and [OAI-skills-shell], which treat containment as required (he says fences are not a defence against malicious behaviour). Extreme, unrepresentative setup.
Relevance: medium. The escalation ladder (habit, warning, written rule, mechanical check) matches [OAI-harness] and [MH-journey] and is directly usable.

### Peter Steinberger

### Just Talk To It - the no-bs Way of Agentic Engineering (Peter Steinberger, 2025-10-14) `[PS-talk]`
File: refs/articles/steipete.me/posts-just-talk-to-it/article.md   URL: https://steipete.me/posts/just-talk-to-it
Thesis: A solo developer on a ~300k LOC TypeScript app runs 3 to 8 Codex CLI sessions in one folder, with short prompts, a long agent file and almost no extra machinery. He calls plan modes, subagents, RAG and most MCPs "charade".
Practices:
- Think in "blast radius": prefer many small changes; if a task runs longer than expected, press escape and ask "what’s the status" (section "Blast Radius").
- Agents make atomic commits of only the files they edited; the agent file explains that several agents share the folder (sections "Harness & General Approach", "Show me your slash commands!").
- No worktrees: one dev server, test several changes at once; separate folders only for risky experiments (section "Why not worktrees?").
- Planning by conversation: "let's discuss" or "give me options"; for tricky features write a spec, have a stronger model review it, then build (sections "Plan Mode & Approach", "Do you do spec-driven development?").
- CLIs over MCPs: "Almost all MCPs really should be clis"; the agent learns a CLI from its help output on first call (section "What about MCPs").
- About 20% of time on agent-driven refactoring with `jscpd` (duplication), `knip` (dead code), ESLint `react-compiler` and deprecation plugins, splitting large files, slow-test rewrites, doc upkeep (section "But the code is slop!").
- Write tests right after each feature or fix in the same context; ask for "code comments on tricky parts" (section "What other tricks do you have?").
- ast-grep rules as a codebase linter in a git hook that blocks commits (section "How does your Agents/Claude file look like?").
- Agent file: one `Agents.md` symlinked to `claude.md`; contents are git rules, product explanation, naming and API patterns, notes on things newer than the model's knowledge, React patterns, migration management, testing, ast-grep; delete entries when a new model knows them (same section).
- Do not shout in instruction files: all-caps threats that worked on Claude "freaks out GPT-5" (same section).
Evidence and numbers: agent file about 800 lines, written by the agent, "a collection of organizational scar tissue"; about $1k per month on subscriptions; GitHub's MCP costs 23k tokens of context (was almost 50,000); at least 50% of his prompts include a screenshot.
Tools and files named: codex CLI, `Agents.md`, `jscpd`, `knip`, ast-grep, `tmux`, `chrome-devtools-mcp`, `gh`, `/commit`, `/automerge`, `/massageprs`, `/review`.
Caveats: Strongly opinionated and model-specific (October 2025, GPT-5-Codex). He says hooks cannot stop a determined model. His 800-line file contradicts the under-60-lines advice of [HL-claudemd] and the ~100-line map of [OAI-harness]; he admits "I should clean this up". Solo work on main would not suit a team.
Relevance: high. The closest match to the user's situation (solo, TypeScript/React, Vercel), and a useful dissent against heavy process.

### Shipping at Inference-Speed (Peter Steinberger, 2025-12-28) `[PS-speed]`
File: refs/articles/steipete.me/posts-2025-shipping-at-inference-speed/article.md   URL: https://steipete.me/posts/2025/shipping-at-inference-speed
Thesis: With GPT-5.2-era models he no longer reads most code; output is limited by inference time and hard thinking. The workflow stays simple: conversation, queued prompts, commits to main, docs folders.
Practices:
- Start everything as a CLI so the agent can call it and verify output, "closing the loop" (sections "What Changed Since May", "Tooling & Infrastructure").
- Per-project `docs/` folder for subsystems and features plus a script and instructions in the global AGENTS file that make the model read docs on certain topics (section "My Workflow").
- Cross-reference sibling projects ("look at ../vibetunnel and do the same") instead of re-explaining (same section).
- An "oracle" CLI lets the agent ask a slower, stronger model with files attached when stuck; instructions live in the global AGENTS.MD (section "Oracle").
- Refactor ad hoc when prompts start taking longer or something ugly appears, instead of dedicated days (section "Tooling & Infrastructure").
- Choose dependencies by maintenance and by how much "world knowledge" models have of them (same section).
- Config: raises `tool_output_token_limit` to 25000 and sets `model_auto_compact_token_limit` to 233000 in `~/.codex/config.toml` (section "My Config").
Evidence and numbers: a two-sentence prompt produced a working Zig conversion in one 5-hour run across several compactions; uses of the oracle fell from several per day to a few per week after GPT 5.2.
Caveats: "These days I don’t read much code anymore." He never reverts, commits to main, and says issue trackers and slash commands did not stick. He notes this would not work in a team. Contradicts [MH-vibing] (never ship unreviewed code) and [HL-longctx] (keep contexts small): he says restarting sessions per task is no longer needed with GPT 5.2.
Relevance: medium to high. Shows the minimal end of the spectrum and that advice shifts with each model generation.

### Amp (Thorsten Ball, Sourcegraph / Amp)

### Amp is now available. Here's how I use it. (Thorsten Ball, 2025-05-15) `[AMP-howiuse]`
File: refs/articles/ampcode.com/how-i-use-amp/article.md   URL: https://ampcode.com/how-i-use-amp
(Metadata date 2026-08-05 is a page date; the byline says May 15, 2025.)
Thesis: "paint-by-numbers programming": the human decides architecture and structure, then puts everything known into a detailed prompt; threads stay small.
Practices:
- Keep threads small; many problems for newcomers trace "back to them not starting new threads often enough"; after about 100k tokens things got "blurry" with the models of the time.
- Prompts name files, suspected traps, constraints and tests to run, not one-line asks.
- Visual feedback: keep a storybook running and have the agent screenshot its UI changes through Playwright MCP.
- Self-review with a fresh eye: "Run `git diff` to see the code someone else wrote. Review it thoroughly and give me a report".
- Use git commits as context: point the agent at a specific commit hash before asking for a fix.
- Use the git staging area as the checkpoint: stage what is good, wipe unstaged changes that are not.
- Tell the agent the exact tool to use ("Use git blame to tell me who wrote this component").
- Build one to throw away: implement, look after five minutes, keep or discard.
Evidence and numbers: his estimate that the agent writes 70 to 80% of the code he commits.
Tools and files named: `AGENTS.md` (documents what "the build" is), Playwright MCP, storybook, `psql`.
Caveats: May 2025 models (Claude Sonnet 4). The agent "doesn’t write critical code without close supervision".
Relevance: medium. Durable habits: small threads, staging area as safety net, review via `git diff` in a new thread.

### Context Management in Amp (Amp guide, page dated 2026-07-27) `[AMP-context]`
File: refs/articles/ampcode.com/guides-context-management/article.md   URL: https://ampcode.com/guides/context-management
Thesis: Everything in the context window influences output and quality degrades with length, so manage it with edits, restores, handoffs and thread references.
Practices: edit or restore earlier messages to remove a "false turn" instead of leaving it in; Handoff: state the next goal, a second model drafts a new-thread prompt with only the relevant information and files; reference another thread with an extraction prompt so only the needed piece comes over.
Relevance: medium. Supports a handoff step that is goal-directed (what will I do next) rather than a generic summary.

### Frequently Ignored Feedback (Amp, page dated 2026-07-11) `[AMP-fif]`
File: refs/articles/ampcode.com/fif/article.md   URL: https://ampcode.com/fif
Thesis: Amp's reasons for refusing common requests.
Practices and positions: edit-by-edit approval "traps you in a local maximum" by blocking the agent's feedback loop (review, diagnostics, compiler, tests); fix the prompt and AGENTS.md instead. An ignore file is "actively harmful" because the model works around it with Bash, giving "a false sense of security"; use secret redaction and a permissions system instead.
Caveats: States that Amp "does not try to protect against" prompt injection that makes Bash run malicious code. This is weaker than [VER-sandbox] and [OAI-skills-shell].
Relevance: medium. A reminder that file-level deny rules without a sandbox are not a security boundary.

### How We Build (Amp, 2026-07-01) `[AMP-howwebuild]`
File: refs/articles/ampcode.com/how-we-build/article.md   URL: https://ampcode.com/how-we-build
Thesis: Team principles for an AI-native product team.
Practices: write the news post first to answer why a user would care; "No task lasts longer than one week"; build "the smallest mergeable chunk that’s easy to test and revert, verify it, merge it"; "We merge it, we own it."
Relevance: low to medium. Process values; the small-mergeable-chunk rule matches the user's own.

### Agents for the Agent (Thorsten Ball, 2025-06-10) `[AMP-subagents]`
File: refs/articles/ampcode.com/agents-for-the-agent/article.md   URL: https://ampcode.com/agents-for-the-agent
Thesis: Specialised subagent types were tried and "never turned out to be useful"; a read-only search agent and generic subagents with their own context windows are what worked once the model (Sonnet 4) started delegating on its own.
Relevance: medium. Early evidence against role-specialised subagents, consistent with [HL-skillissue].

### Cursor

### Best practices for coding with agents (Lee Robinson, Cursor, 2026-01-09) `[CUR-best]`
File: refs/articles/cursor.com/blog-agent-best-practices/article.md   URL: https://cursor.com/blog/agent-best-practices
(Section headings were lost in extraction; locators describe the section topic.)
Thesis: Vendor guide to working with agents: plan first, manage context by starting fresh conversations, keep rules minimal, use skills and hooks for dynamic behaviour, give verifiable goals, review carefully.
Practices:
- "The most impactful change you can make is planning before coding." Plan mode researches, asks clarifying questions, writes a plan with file paths, waits for approval; plans can be saved to `.cursor/plans/` (planning section).
- When output misses, "Revert the changes, refine the plan to be more specific about what you need, and run it again" instead of patching through follow-ups (planning section).
- New conversation when changing task, when the agent repeats mistakes, or after a logical unit; continue when iterating on the same feature (context section).
- Rules content: commands (`npm run build`, `npm run typecheck`, `npm run test` with "prefer single test files for speed"), a few code-style items, a pointer to a canonical example file, workflow notes. "Reference files instead of copying their contents" (rules section).
- Rules to avoid: "Copying entire style guides (use a linter instead)", documenting every command, edge cases that rarely apply. "Add rules only when you notice the agent making the same mistake repeatedly." (rules section).
- Stop-hook loop: `.cursor/hooks.json` runs a script on `stop` that returns a `followup_message` until `.cursor/scratchpad.md` contains `DONE` or `MAX_ITERATIONS = 5` is reached; for goals with verifiable success such as tests passing (long-running loop section).
- TDD workflow: write tests from input/output pairs and say it is TDD so it does not mock missing code; run and confirm they fail; commit tests; implement without modifying tests until all pass; commit (workflows section).
- Commands in `.cursor/commands/` for repeated workflows: `/pr`, `/fix-issue [number]`, `/review`, `/update-deps` (git workflows section).
- Parallel worktrees, and running the same prompt on several models and picking the best result (parallel section).
- Debug mode: generate hypotheses, instrument with logging, reproduce, analyse runtime data, then fix (debug section).
Evidence and numbers: cites a University of Chicago study that experienced developers are more likely to plan before generating code (no figures in the text).
Tools and files named: `.cursor/rules/`, `.cursor/plans/`, `.cursor/hooks.json`, `.cursor/hooks/grind.ts`, `.cursor/scratchpad.md`, `.cursor/commands/`, `SKILL.md`, Bugbot, `@Branch`, `@Chats`.
Caveats: Product documentation; describes skills as able to include hooks and commands, which differs from the Agent Skills format in [VER-skillsfaq] and [VER-plugins]. "AI-generated code can look right while being subtly wrong."
Relevance: high. A compact, cross-checked list of defaults, plus a bounded stop-hook loop pattern.

### Scaling long-running autonomous coding (Wilson Lin, Cursor, 2026-01-14) `[CUR-scaling]`
File: refs/articles/cursor.com/blog-scaling-agents/article.md   URL: https://cursor.com/blog/scaling-agents
Thesis: Hundreds of concurrent agents built a browser over about a week. Flat self-coordination failed; a planner/worker split with a judge worked; simpler structures beat elaborate ones.
Practices and findings:
- Flat coordination through a shared file with locks failed: agents held locks too long or forgot to release them; "Twenty agents would slow down to the effective throughput of two or three" (self-coordination section).
- Without hierarchy agents became risk-averse and avoided hard tasks (same section).
- Planners explore and create tasks (and can spawn sub-planners); workers grind on one task and push; a judge decides whether to continue; each cycle starts fresh (planner/worker section).
- An integrator role for quality control and conflict resolution "created more bottlenecks than it solved" and was removed (lessons section).
- Different models suit different roles; "The harness and models matter, but the prompts matter more." (lessons section).
Evidence and numbers: over 1 million lines across 1,000 files for the browser; a Solid to React migration of +266K/-193K over three weeks; video rendering made 25x faster in Rust (merged).
Caveats: Research experiments on greenfield targets; "Agents occasionally run for far too long"; "We still need periodic fresh starts to combat drift and tunnel vision."
Relevance: medium. Evidence on which multi-agent structures fail (shared lock files, flat peers, central integrator).

### Towards self-driving codebases (Wilson Lin, Cursor, 2026-02-05) `[CUR-selfdriving]`
File: refs/articles/cursor.com/blog-self-driving-codebases/article.md   URL: https://cursor.com/blog/self-driving-codebases
(Section headings were lost in extraction.)
Thesis: The detailed history of the multi-agent harness: five designs, the failure of each, and the prompting rules that emerged. Final design is recursive planners that do no coding and isolated workers that return a written handoff.
Practices:
- Final roles: a root planner owns the whole scope and only issues tasks; sub-planners own slices; workers work on their own repo copy, do not talk to each other, and write "a single handoff" with what was done plus "notes, concerns, deviations, findings, thoughts, and feedback" (final design section).
- Freshness mechanisms: a `scratchpad.md` that "should be frequently rewritten versus being appended to"; automatic summarisation at context limits; self-reflection reminders; permission to challenge assumptions (freshness section).
- Giving one agent too many roles caused pathologies: sleeping, doing the work itself, premature completion claims (continuous executor section).
- Accept a small stable error rate instead of 100% correctness per commit, with a separate "green" branch produced by a regular fix-up pass (throughput section).
- Prompting rules: do not instruct for things the model already knows; "Constraints are more effective than instructions." ("No TODOs, no partial implementations" beats "remember to finish implementations"); avoid checkbox mentality for higher-level tasks; give concrete numbers ("Generate 20-100 tasks") (prompting section).
- Log everything with timestamps and feed logs back to an agent to find patterns (observability section).
- Initial instructions matter most: vague "spec implementation" sent agents into obscure features; performance needed explicit instructions and enforced timeouts; dependency philosophy had to be stated (instructions section).
Evidence and numbers: peak of about 1,000 commits per hour across 10M tool calls in one week with no human intervention; 20 agents slowed to the throughput of 1 to 3 under locking; compile time and disk I/O dominated throughput in a monolith.
Caveats: The first browser architecture was "unfit to evolve into a full browser", "a failure of the initial specification". Research setting; the browser "was not intended to be used externally". The tolerance for a non-green main branch conflicts with strict gate advice ([BECK-augmented], [OAI-longhorizon]).
Relevance: medium to high. The prompting rules and the worker handoff format transfer directly to subagent briefs.

### Continually improving our agent harness (Stefan Heule and Jediah Katz, Cursor, 2026-04-30) `[CUR-harness]`
File: refs/articles/cursor.com/blog-continually-improving-agent-harness/article.md   URL: https://cursor.com/blog/continually-improving-agent-harness
Thesis: Cursor treats its harness as a product measured by offline evals and online A/B tests; with better models it has removed guardrails and static context in favour of dynamic context.
Practices and findings:
- Guardrails from 2024 (lint and type errors after every edit, rewriting file reads, limiting tool calls per turn, static folder layouts) are "mostly long gone" (context section).
- Quality metrics: "Keep Rate" (fraction of agent-proposed code still in the codebase after fixed intervals) and an LLM reading the user's next message for satisfaction (measurement section).
- Tool errors cause "context rot"; classify expected errors (`InvalidArguments`, `UnexpectedEnvironment`, `ProviderError`, `UserAborted`, `Timeout`) and alert on unknown ones (reliability section).
- A weekly automation with a log-searching skill files or updates tickets for new or spiking errors; cloud agents start the fixes (same section).
- Give each model the edit tool format it was trained on (patch-based for OpenAI, string replacement for Anthropic); stay with one model per conversation; use a subagent to switch models (model section).
Evidence and numbers: a more expensive summarisation model made "a negligible difference"; a sprint cut unexpected tool-call errors "by an order of magnitude". One model showed "context anxiety" (refusing work as the window filled).
Caveats: Vendor post. Predicts specialised agents (planning, fast edits, debugging), which sits uneasily with [AMP-subagents] and [HL-skillissue] findings that role-specialised subagents did not help.
Relevance: medium. Supports removing instructions as models improve and tracking a keep-rate style metric for one's own setup.

### What we've learned building cloud agents (Josh Ma, Cursor, 2026-06-02) `[CUR-cloud]`
File: refs/articles/cursor.com/blog-cloud-agent-lessons/article.md   URL: https://cursor.com/blog/cloud-agent-lessons
Thesis: The biggest factor in cloud agent quality is a complete development environment; a missing one shows up as subtly worse output, not an error.
Practices: reconstruct the full dev environment for remote agents; move logic from harness to agent-controlled tools as models improve (for CI fixes, give the agent the GitHub CLI and write large outputs to searchable files); prompt cloud agents to be more autonomous because blocking is costly; let agents report missing secrets or blocked network.
Evidence and numbers: "more than 40% of our PRs come from cloud agents"; early beta had about one nine of reliability, the Temporal migration took it past two nines.
Relevance: medium. For any background or cloud agent: environment parity first.

### Dynamic context discovery (Jediah Katz, Cursor, 2026-01-06) `[CUR-dynamic]`
File: refs/articles/cursor.com/blog-dynamic-context-discovery/article.md   URL: https://cursor.com/blog/dynamic-context-discovery
Thesis: Provide less up front and let the agent pull context from files: long tool outputs, chat history, skills, MCP tool descriptions and terminal sessions all become files.
Practices: write long tool output to a file and let the agent `tail` and read more, instead of truncating; keep chat history as a file the agent can search after summarisation; sync MCP tool descriptions to one folder per server and load only names statically.
Evidence and numbers: in an A/B test, lazy MCP loading "reduced total agent tokens by 46.9%" in runs that called an MCP tool.
Relevance: medium. Supports files as the context interface and lazy MCP loading.

### Expanding our long-running agents research preview (Cursor, 2026-02-12) `[CUR-longrunning]`
File: refs/articles/cursor.com/blog-long-running-agents/article.md   URL: https://cursor.com/blog/long-running-agents
Thesis: Product announcement: long-running agents plan and wait for approval, then use several agents checking each other's work to follow through.
Evidence and numbers: example runs of 25 to 52 hours; a 10,000-line network-policy PR with "very few issues" against a large test suite. Testimonials only.
Relevance: low. Confirms plan-approval before long autonomous runs.

### Company write-ups of internal agent setups: Stripe, Spotify, Ramp, Shopify

### Minions: Stripe's one-shot, end-to-end coding agents, Part 1 (Alistair Gray, Stripe, 2026-02-09) `[STR-minions1]`
File: refs/articles/stripe.dev/blog-minions-stripes-one-shot-end-to-end-coding-agents/article.md   URL: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
Thesis: Minions are unattended agents that go from a Slack message to a CI-passing PR with no interaction, built on the same tooling human engineers use.
Practices:
- Isolated "devbox" per run, pre-warmed to start in 10 seconds, cut off from production and the internet, "so we can run minions on devboxes without human permission checks" (section "How do minions work?").
- Interleave agent loops with deterministic code for git operations, linters and tests so required steps always run (same section).
- Rules: "almost all agent rules at Stripe are conditionally applied based on subdirectories"; unconditional rules would be impractical (same section).
- Hydrate context deterministically before the run by running MCP tools over links in the request (same section).
- Shift feedback left: a local executable selects and runs lints on each git push in under five seconds (same section).
- CI budget: "often one, at most two, CI runs—and only after we’ve fixed everything we can locally" (same section).
Evidence and numbers: over a thousand merged PRs per week are minion-produced (human-reviewed, no human-written code); hundreds of millions of lines of code, mostly Ruby with Sorbet; over three million tests; Toolshed hosts more than 400 MCP tools.
Tools and files named: goose (forked), devbox, Toolshed, Sourcegraph search, Slack.
Caveats: Depends on years of prior developer-productivity investment. A run that is not entirely correct is treated as "an excellent starting point" for manual work; no success rate is given.
Relevance: medium to high. The principles scale down: disposable isolated environment, deterministic gates around the agent, capped CI retries, path-scoped rules.

### Minions, Part 2 (Alistair Gray, Stripe, 2026-02-19) `[STR-minions2]`
File: refs/articles/stripe.dev/blog-minions-stripes-one-shot-end-to-end-coding-agents-part-2/article.md   URL: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
Thesis: Implementation detail: devboxes, a custom harness, "blueprints" that mix deterministic nodes and agent nodes, path-scoped rule files shared across three agents, a curated MCP subset, and local-first feedback.
Practices:
- Blueprints: a workflow in code where nodes such as "Implement task" or "Fix CI failures" are agent loops and nodes such as "Run configured linters" or "Push changes" are plain code. "putting LLMs into contained boxes" compounds into reliability (section "Blueprints").
- Rule files: global rules used "very judiciously"; context comes "almost exclusively" from files scoped to subdirectories or file patterns, attached as the agent traverses the filesystem. One source format (Cursor rules) synced into a format Claude Code reads, so minions, Cursor and Claude Code share guidance (section "Context gathering: Rule files").
- Tools: nearly 500 MCP tools exist, but each agent requests a small curated subset; "Agents perform best when given a “smaller box”" (section "Context gathering: MCP").
- Safety: devboxes run in a QA environment with no real user data, no production services and no arbitrary network egress, so the agent runs with full permissions and no confirmation prompts (sections "The agent", "Context gathering: MCP").
- Feedback: pre-push hooks fix common lint issues in under a second using a daemon that precomputes which lints apply; a subset of linters runs as a deterministic blueprint node in a local loop before push; then one CI run, autofixes applied automatically, one more agent attempt, then back to the human (section "… and iterate").
Evidence and numbers: over 1,300 minion PRs merged per week (up from 1,000 ten days earlier); devbox ready in 10 seconds.
Caveats: "What’s good for humans is good for agents" is the stated lesson; much is Stripe-specific. They note it is "fundamentally difficult" to get the same isolation on a laptop with containers or worktrees.
Relevance: high. Clear evidence for path-scoped rules, a single rule source synced to several harnesses, and deterministic steps wrapped around agent steps.

### 1,500+ PRs Later: Spotify's background coding agent, Honk Part 1 (Max Charas and Marc Bruggmann, Spotify, 2025-11-06) `[SPO-honk1]`
File: refs/articles/engineering.atspotify.com/2025-11-spotifys-background-coding-agent-part-1/article.md   URL: https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1
Thesis: Spotify replaced hand-written migration scripts in its Fleet Management system with an agent driven by a prompt, keeping all surrounding infrastructure (targeting, PRs, review, merge).
Practices: a small internal CLI wraps the agent so models and agents can be swapped; it runs formatting and linting through local MCP, evaluates the diff with an LLM judge, uploads logs and captures traces.
Evidence and numbers: more than 1,500 agent PRs merged; 60 to 90% time saving on migrations versus hand-writing; about half of Spotify's PRs were already automated since mid-2024; a deterministic Maven updater script had grown to over 20,000 lines.
Relevance: medium. Shows a thin wrapper CLI that keeps the choice of agent replaceable.

### Background Coding Agents: Context Engineering, Honk Part 2 (Charas and Bruggmann, Spotify, 2025-11-24) `[SPO-honk2]`
File: refs/articles/engineering.atspotify.com/2025-11-context-engineering-background-coding-agents-part-2/article.md   URL: https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2
Thesis: Reliable mergeable PRs across thousands of repos came from careful prompts and a deliberately small tool set, not from more tools.
Practices:
- Prompt lessons: tailor to the agent (Claude Code does better with end-state descriptions than step lists); "State preconditions" including when not to act; use concrete code examples; "Define the desired end state, ideally in the form of tests"; "Do one change at a time"; ask the agent afterwards what the prompt lacked (section "The proof is in the prompt").
- Two prompt anti-patterns: overly generic, and overly specific that breaks on the unexpected (same section).
- Prefer larger static prompts that can be version-controlled, tested and evaluated over dynamic context fetched through MCP: "The more tools you have, the more dimensions of unpredictability you introduce." (section "The right tools for the job").
- Three tools only: a "verify" tool (formatters, linters, tests, with summarised output), a restricted Git tool (never push or change origin; standard committer and message format), and Bash with a strict allowlist (same section).
- Put guidance in the code itself (tests, linters, API docs in target repos) so it works for all prompts and agents (same section).
Evidence and numbers: their own loop was capped at 10 turns per session and three retries; Claude Code used for about 50 migrations.
Caveats: "we are still flying mostly by intuition. Our prompts evolve by trial and error." No code search or documentation tools exposed to the agent, by choice. The file contains a promotional quote from Anthropic.
Relevance: high. Evidence-backed prompt rules and the idea of a single abstract verify tool.

### Background Coding Agents: Predictable Results Through Strong Feedback Loops, Honk Part 3 (Charas and Bruggmann, Spotify, 2025-12-09) `[SPO-honk3]`
File: refs/articles/engineering.atspotify.com/2025-12-feedback-loops-background-coding-agents-part-3/article.md   URL: https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3
Thesis: Unattended agents need verification loops: deterministic verifiers the agent calls without knowing their internals, plus an LLM judge that checks the diff against the prompt.
Practices:
- Three failure modes ranked: no PR (minor), PR fails CI (frustrating), PR passes CI but is functionally wrong (most serious, erodes trust) (section "How things fail").
- Verifiers activate by repo contents (a Maven verifier when `pom.xml` exists) and are exposed as one abstract MCP tool; they parse output with regular expressions to return only relevant errors, or a very short success message (section "Designing for predictability").
- All relevant verifiers also run in a Claude Code stop hook before a PR may be opened; a failing verifier blocks the PR (same section).
- LLM judge: receives the diff and the original prompt, runs after the deterministic verifiers; added because agents were too "ambitious": refactoring or "disabling flaky tests" (section "Using LLMs in the verification loops").
- Keep the agent narrow: pushing code, Slack and prompt authoring are handled by surrounding infrastructure; container with limited permissions and few binaries (section "Keeping the Agent Focused").
Evidence and numbers: "the judge vetoes about a quarter of them", and after a veto "the agent is able to course correct half the time"; the most common trigger is going outside the prompt's instructions.
Caveats: "We have yet to invest in evals for our judge." Verifiers run only on Linux x86.
Relevance: high. The stop-hook gate plus a scope-checking judge is a directly reusable pattern with a measured veto rate.

### Why We Built Our Own Background Agent (Zach Bruggeman, Jason Quense, Rahul Sengottuvelu, Ramp, 2026-01-12) `[RAMP-inspect]`
File: refs/articles/builders.ramp.com/post-why-we-built-our-background-agent/article.md   URL: https://builders.ramp.com/post/why-we-built-our-background-agent
Thesis: Ramp's Inspect is a hosted background agent on OpenCode in Modal sandboxes with a full dev environment and integrations, so the agent can verify its own work; the post doubles as a build spec.
Practices:
- Full environment in the sandbox (Vite, Postgres, Temporal) plus Sentry, Datadog, LaunchDarkly, GitHub, Slack, Buildkite; frontend work is visually verified with screenshots and previews (intro).
- Images rebuilt every 30 minutes with repo cloned, dependencies installed and the app and test suite run once to warm caches; sessions start from a snapshot (section "Sandbox").
- Let the agent read immediately but block edits until git sync completes, using an OpenCode plugin on the `tool.execute.before` event (same section).
- Open PRs with the user's GitHub token, not the app's, so nobody can approve their own agent-written change (section "API").
- Track "how many sessions result in a merged pull request" as the main metric (section "Web").
- For Slack, classify the target repository with a fast model, with an "unknown" option (section "Slack").
Evidence and numbers: about 30% of merged PRs in frontend and backend repos written by Inspect within a couple of months, without mandating it.
Tools and files named: OpenCode, Modal, Cloudflare Durable Objects and Agents SDK, code-server, React Grab.
Caveats: Says "frontier models are smart enough to contain themselves" about spawning sub-sessions, with no evidence. Product-flavoured; Inspect is now offered externally.
Relevance: medium. Useful for the verification-environment principle and the merged-PR metric; the infrastructure is beyond a solo setup.

### Building an agentic harness that outlasts the model (Zack Deveau, Shopify, 2026-07-29) `[SHOP-harness]`
File: refs/articles/shopify.engineering/building-an-agentic-harness-that-outlasts-the-model/article.md   URL: https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model
Thesis: In a security-scanning pipeline, better models found more candidates but also more noise; the durable value is the harness: a test oracle, partitioning, cross-model verification and deterministic code for credentials, Git and storage.
Practices:
- Staged pipeline: test bootstrap, architecture documentation, file cataloguing, partitioning, parallel hunting, sequential verification, post-processing, reporting, remediation (table "Dispatch runs each scan as an ordered set of stages").
- Test bootstrap first: find and verify the test commands so later agents "should not spend turns having to discover how to run tests" (same table).
- Verification by a different model than the one that produced the finding; verifiers write real integration tests as the oracle and run sequentially to avoid port, database and fixture collisions (same table; section "Building test oracles").
- Partitions sized to roughly 20 to 30% of the model's context window, grouped by domain, each including shared-context files (section "Keeping costs low").
- "Reach for determinism when it makes sense": give agents scripts or skills that enforce output structure (section of that name).
- Diff-based follow-up scans against stored artifacts (section "Our latest workflow").
Evidence and numbers: in one audit a model raised more than 30 candidate vulnerabilities and after validation every one was downgraded, a false positive, or defence in depth; over 80 applications scanned; over 300 findings in about six weeks, valued at over $400,000 in bounty equivalents; full scan $50 to $300, diff scan $5 to $50; partitioned scans beat unpartitioned on a benchmark of reintroduced vulnerabilities (no figures).
Caveats: Security review, not feature development. "Generalist" agents produced many theoretical issues and non-deterministic results.
Relevance: medium. The rules to verify with a different model and to prove a finding with a test apply to any review agent.

### How River takes security work from a fix to merge (Erin Son, Shopify, 2026-09-02) `[SHOP-river]`
File: refs/articles/shopify.engineering/river-vulnerability-remediation/article.md   URL: https://shopify.engineering/river-vulnerability-remediation
Thesis: A patch is not a fix. Shopify's Slack-based agent River revalidates each finding against live state, repairs on the current head, hands off decisions with evidence, and verifies closure after merge.
Practices:
- Treat stored state as a claim: the ledger "is useful memory, but it isn't the operational truth"; compare with the live repo, PR and tracker before acting (section "Validate the live state").
- Bind evidence to the current SHA: after a rebase, CI results for the old head are discarded (section "Repair and iterate on the current head").
- Do not touch a branch a human has taken over (same section).
- Handoff carries the current head, what was tried, the evidence and "the smallest question that an owner has to answer" (section "Hand off the decision, not the investigation").
- Definition of done: source system records the outcome, the default branch reflects it, tracker and ledger agree (section "Verify closure").
- "Prompts are the right place to express judgment and the wrong place to express a guarantee."; pagination, deduplication, current-head identity and accounting should move into code (section "A workflow prompt isn't a control plane").
Evidence and numbers: dependency backlog down about 70% in 11 days; security merges through the merge queue from about 10% to 80%; on one run the agent "rechecked only the oldest in-flight claim" despite a prompt telling it to enumerate completely.
Caveats: Security remediation domain; engineers keep approval and merge authority. In one case the agent correctly recommended dropping its own patch after a developer asked why the feature existed.
Relevance: medium to high. Strong statements, with a concrete failure, on what must be code rather than prompt, and on revalidating before editing.

### Tessl

### 75% of Tessl's PRs now merge without human review (Simon Rendon Arango and Colin Hallett, Tessl, 2026-10-16) `[TES-75]`
File: refs/articles/tessl.io/blog-75-of-tessls-prs-now-merge-without-human-review/article.md   URL: https://tessl.io/blog/75-of-tessls-prs-now-merge-without-human-review
Thesis: An AI reviewer that checks PRs against the team's own written standards, with a risk-based policy, let about 75% of agent-written PRs merge without a human correcting the agent.
Practices:
- Review against the standards already written for the agents (coding conventions, design system, AI code review policy), not generic rules (section "Review against our own standards").
- "When reviewers flag the same pattern repeatedly, we turn it into a verifier, a pass or fail check that runs on every change." (same section).
- A written policy lists change types that always need a human check (six types; privacy and access control are named) (section "Review quality").
- Pick models "by cost per verified outcome, not token price" (section "What it means for your bill").
- Define measurement terms before looking at results (section "How we measured").
Evidence and numbers: over 1,200 agent-written PRs a week; 91% of findings were real defects versus 68% for the previous reviewer over a one-week side-by-side on more than 600 PRs; 1.56 versus 0.75 author-fixed bugs per PR; the two reviewers tied on an external benchmark, so the gain came from repo-specific standards; PRs that never merged and review-fix rounds were over half of agent spend; 8.5% of PRs took more than five review rounds and used 47.4% of review-loop spend; two-thirds of reruns triggered by merge conflicts found nothing new.
Caveats: Vendor measuring its own product on its own repo. The previous reviewer was better on low-severity and cosmetic findings and caught some defects the new one missed. The headline metric is defined as merged without a human correcting the agent or discussing the engineering.
Relevance: medium to high. Supports a reviewer agent fed with the project's own rules, a "needs human" list by change type, and capping review rounds.

### How to constrain a coding agent using only files you own (Ian Johnson, guest post on Tessl, 2026-10-20) `[TES-charter]`
File: refs/articles/tessl.io/blog-how-to-constrain-a-coding-agent-using-only-files-you-own/article.md   URL: https://tessl.io/blog/how-to-constrain-a-coding-agent-using-only-files-you-own
Thesis: A repository "charter" has four levers: instruction (`CLAUDE.md`), constraint (`.claude/rules/`), capability (commands, skills, agents, settings, MCP) and check (`.claude/hooks/`). Only the check lever can refuse; the others persuade.
Practices:
- Constraint rules are path-scoped, "each rule carrying the date of the incident that caused it" (section "Your charter is four levers, not one file").
- Capability test: "Remove the thing, and if the agent can do less, it was a capability." If it does the same work worse, it was a rule dressed as a skill (same section).
- One predicate, two mounting points: the same 40-line script runs as a `PreToolUse` hook and as `make gate` in CI (section "Two levers persuade. One refuses.").
- Write rules where rule and code disagree; "A rule your codebase already follows constrains nothing." (same section).
- Put the rule you would be most upset to see broken on the lever that refuses (same section).
- Method: run one ticket with no charter, score it against checks written beforehand, then add levers one at a time and re-run to see which lever moved which check (section "tl;dr").
Evidence and numbers: one ticket, three runs: bare run passed 1 of 8 checks (3 files, 49 lines); chartered run passed 8 of 8 (3 files, 102 lines). A reviewer sub-agent then found three real defects, one a permissions bug, in the run that passed all eight mechanical checks.
Caveats: The author says the rules were chosen to make the effect visible: "treat that ratio as a demonstration". One ticket, one repo. "A green scorecard is not a correct change."
Relevance: high. Maps directly onto Claude Code file locations and gives a cheap experiment for testing whether each rule earns its place.

### Verifiers: enforce your repo's rules on every agent change (Amy Heineike and Simon Maple, Tessl, 2026-10-15) `[TES-verifiers]`
File: refs/articles/tessl.io/blog-verifiers-enforce-your-repos-rules-on-every-agent-change/article.md   URL: https://tessl.io/blog/verifiers-enforce-your-repos-rules-on-every-agent-change
Thesis: A "verifier" is a plain-text rule with a yes/no checklist, judged by an LLM on every change, for rules a linter cannot express.
Practices: use only when the rule has a clear yes-or-no answer visible in the changed files and no linter or test can check it ("If a linter can do the job, use the linter."); examples: every user-facing error says what to do next, no handler logs tokens; scope and severity (`info`, `warn`, `error`) live in config outside the rule; "starting at `warn` level" then promote to `error`; pair a rule (before) with a verifier (after).
Tools and files named: `tessl change verify`, `tessl.json` `verify` block, `verifiers/*.json`, default judge `openai/gpt-6-luna`, Jev classifier model.
Caveats: Product announcement, no accuracy numbers. Claims an LLM judge "deterministically runs the same rules every time", which describes scheduling, not judgment (Inference).
Relevance: medium. The warn-then-error rollout, and narrowing a rule until a checklist can decide it, are reusable for any LLM-judged check.

### We stopped reviewing code and started verifying intent (Ankit Jain, Aviator, guest post on Tessl, 2026-10-20) `[TES-intent]`
File: refs/articles/tessl.io/blog-we-stopped-reviewing-code-and-started-verifying-intent/article.md   URL: https://tessl.io/blog/we-stopped-reviewing-code-and-started-verifying-intent
Thesis: At four times the PR volume, review moved to the front: humans review intent (acceptance criteria, constraints, edge cases) before code exists, then each criterion gets a verdict with evidence.
Practices: reviewers look at "five criteria verdicts, with screenshots and request traces" instead of a 500-line diff; mine review history: "start with your last 1,000 review comments. The 20 you repeat most are your first invariants"; good invariants are "boring and specific" (use the Money type, no direct writes to the users table, structured logger only).
Evidence and numbers: none measured; expects about three months of transition with double work in month one.
Caveats: Author runs a company selling tooling in this area. Contradicts [MH-vibing] and [CUR-best], which insist on reading diffs.
Relevance: medium. For a solo developer: write acceptance criteria first and demand per-criterion evidence, which the user's rules already require.

### The Context Development Lifecycle (Patrick Debois, Tessl, 2026-02-19) `[TES-cdlc]`
File: refs/articles/tessl.io/blog-context-development-lifecycle-better-context-for-ai-coding-agents/article.md   URL: https://tessl.io/blog/context-development-lifecycle-better-context-for-ai-coding-agents
Thesis: Context (rules, skills, specs) should be treated as an engineered artifact with a lifecycle: generate, evaluate, distribute, observe.
Practices: context should "fill gaps in the model's knowledge, not duplicate it"; context "rots and conflicts", and when two pieces disagree the agent silently picks one; evaluate context like TDD (write the expected behaviour, watch it fail, improve the context); use evals to decide whether a cheaper model is enough; observe real sessions for gaps and feed them back.
Evidence and numbers: none.
Caveats: Conceptual and vendor-aligned (Tessl sells a registry). "Every evaluation failure is a specification you didn't write."
Relevance: medium. Argues for at least one eval per important convention and a freshness check on instruction files.

### GitHub

### How to write a great agents.md: Lessons from over 2,500 repositories (Matt Nigh, GitHub, 2025-11-19) `[GIT-agentsmd]`
File: refs/articles/github.blog/ai-and-ml-github-copilot-how-to-write-a-great-agents-md-lessons-from-over-2500-r/article.md   URL: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
Thesis: Analysis of 2,500+ agent files (for Copilot custom agents in `.github/agents/`): the effective ones are specific about commands, stack, examples and boundaries.
Practices:
- "Put commands early", with flags and options (`npm test`, `pytest -v`) (section "What works in practice").
- "Code examples over explanations": one real snippet beats three paragraphs (same section).
- Three-tier boundaries: "Always do", "Ask first", "Never do"; "Never commit secrets" was the most common helpful constraint (same section and example).
- Be specific about the stack with versions ("React 18 with TypeScript, Vite, and Tailwind CSS") (same section).
- Six areas to cover: commands, testing, project structure, code style, git workflow, boundaries (same section).
- A test agent "should never remove a test because it is failing" (section "@test-agent").
Evidence and numbers: 2,500+ files analysed; no method or outcome metric given for "best-performing".
Tools and files named: `.github/agents/<name>.md` with `name` and `description` frontmatter.
Caveats: About persona-style custom agent files, not the single always-loaded AGENTS.md. Recommends personas ("You are an expert technical writer"), which [PS-talk] and [HL-skillissue] say do not help. Includes code style examples in the file, which [HL-claudemd] and [CUR-best] advise against. Suggests having Copilot generate the file.
Relevance: medium. The three-tier boundary format and putting commands with flags first are worth keeping; the persona advice is contested.

### Spec-driven development with AI: Spec Kit (Den Delimarsky, GitHub, 2025-09-02) `[GIT-speckit]`
File: refs/articles/github.blog/ai-and-ml-generative-ai-spec-driven-development-with-ai-get-started-with-a-new-o/article.md   URL: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
Thesis: Spec Kit structures agent work into four gated phases (Specify, Plan, Tasks, Implement) with the spec as a living source of truth.
Practices: Specify covers user journeys and success, not stack; Plan adds stack, architecture and constraints; Tasks are small chunks each implementable and testable in isolation; "you don’t move to the next one until the current task is fully validated"; commands `/specify`, `/plan`, `/tasks`.
Evidence and numbers: none.
Caveats: Launch post. Its own open questions include "Reading walls of text can be tedious" and managing many Markdown files. Independently criticised in [TW-sdd].
Relevance: medium. Origin of the most-used SDD toolkit; the phase gates matter more than the tool.

### Automate repository tasks with GitHub Agentic Workflows (Don Syme and Peli de Halleux, GitHub, 2026-02-13) `[GIT-aw]`
File: refs/articles/github.blog/ai-and-ml-github-copilot-automate-repository-tasks-with-github-agentic-workflows/article.md   URL: https://github.blog/ai-and-ml/github-copilot/automate-repository-tasks-with-github-agentic-workflows/
Thesis: Scheduled or event-driven agent jobs written in Markdown with YAML frontmatter, compiled to a lock file and run in GitHub Actions with read-only permissions and declared "safe outputs".
Practices:
- "Workflows run with read-only permissions by default."; writes go through `safe-outputs` that map to pre-approved operations such as creating an issue or PR (section "Let’s talk guardrails and control").
- Frontmatter declares trigger, permissions, tools and allowed outputs; Markdown body states intent; `gh aw compile` produces `<name>.lock.yml` (section "A simple example").
- Start with low-risk outputs (comments, drafts, reports) before PR creation; for code start with refactoring, test coverage, simplification (section "Practical guidance for teams").
- "pull requests are never merged automatically" (same section).
- Do not replace deterministic CI/CD with agent workflows (same section).
Tools and files named: `gh-aw`, `.github/workflows/daily-repo-status.md`, `safe-outputs`, engines Copilot CLI, Claude Code, Codex.
Caveats: Technical preview. Each run costs two premium requests with defaults. Running an agent CLI directly in Actions YAML "often grants these agents more permission than is required".
Relevance: medium. A safe pattern for scheduled maintenance agents on a personal repo: read-only plus a declared output type.

### Beyond code generation: A developer's guide to agentic engineering (Nick Liffen and Philip Holleran, GitHub, 2026-11-06) `[GIT-beyond]`
File: refs/articles/github.blog/ai-and-ml-github-copilot-beyond-code-generation-a-developers-guide-to-agentic-en/article.md   URL: https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/
Thesis: Product tour organised as Plan, Build, Verify, Observe; the pressure has moved from writing code to review.
Practices: stacked small PRs instead of one large change; isolated repository copies per session; repository instructions for conventions and validation commands plus memory that is refreshed from sessions and PR feedback; issues with acceptance criteria and a regression test for each production finding.
Evidence and numbers: more than 1.2 billion commits in one October 2026 week, over 400% more than a year earlier; cites a Faros AI study that PRs spent 441% longer in review when teams moved from low to high AI adoption.
Caveats: Feature marketing; no first-hand engineering detail.
Relevance: low to medium. The two statistics are the newest quantification of the review bottleneck in this set.

### Google, LangChain, Datadog, StrongDM, Every

### Conductor: context-driven development for Gemini CLI (Keith Ballinger, Jay Kornder, Sherzat Aitbayev, Google, 2025-12-17) `[GOO-conductor]`
File: refs/articles/developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/article.md   URL: https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/
Thesis: A Gemini CLI extension that keeps project context, specs and plans as Markdown in the repo.
Practices: `/conductor:setup` creates product, tech stack and workflow context files; `/conductor:newTrack` creates a spec and a `plan.md` with phases, tasks and sub-tasks; `/conductor:implement` works through `plan.md` checking off tasks, so work can pause and resume.
Caveats: Preview announcement with no results. A search result (not a saved source) says Gemini CLI was later folded into another product in 2026; not verified.
Relevance: low. One more vendor converging on spec plus plan files in the repo.

### Improving Deep Agents with harness engineering (Vivek Trivedy, LangChain, 2026-02-17) `[LC-harness]`
File: refs/articles/blog.langchain.com/improving-deep-agents-with-harness-engineering/article.md   URL: https://blog.langchain.com/improving-deep-agents-with-harness-engineering/
Thesis: With the model fixed, changing only system prompt, tools and middleware moved a coding agent from 52.8 to 66.5 on Terminal Bench 2.0. Self-verification and trace analysis did most of the work.
Practices:
- The most common failure: the agent "wrote a solution, re-read its own code, confirmed it looks ok, and stopped"; fix with a plan, build, verify, fix instruction and a pre-completion hook that reminds it to verify against the task spec, compared to a Ralph loop (section "Build & Self-Verify").
- Verify step wording: "compare against what was asked (not against your own code)" (same section).
- Inject environment context at start (directory map, available tools) (section "Giving Agents Context about their Environment").
- Loop detection: count edits per file and after N edits inject a prompt to reconsider the approach, to break "doom loops" (section "Encouraging Agents to Step Back").
- "reasoning sandwich": highest reasoning for planning and verification, lower for implementation (section "Choosing How Much Compute").
- A trace-analyzer skill: fetch traces, spawn parallel error-analysis agents, synthesise harness changes; watch for overfitting (section "The Trace Analyzer Skill").
Evidence and numbers: 52.8% to 66.5% on 89 tasks with `gpt-5.2-codex`; running everything at `xhigh` scored 53.9% because of timeouts versus 63.6% at `high`; doom loops of 10+ edits in some traces.
Caveats: Benchmark with strict time limits; "These guardrails will almost surely dissolve over time". Vendor of the tracing product used.
Relevance: medium to high. Measured support for a completion-time verification hook and loop detection.

### Closing the verification loop: Observability-driven harnesses (Alp Keles, Jai Menon, Sesh Nalla, Vyom Shah, Datadog, 2026-03-09) `[DD-harness]`
File: refs/articles/datadoghq.com/blog-ai-harness-first-agents/article.md   URL: https://www.datadoghq.com/blog/ai/harness-first-agents/
Thesis: "harness-first engineering": instead of reading every line, invest in automated checks that say in seconds whether code is correct, layered from specs to deterministic simulation to production telemetry.
Practices:
- Contracts before code: state invariants and semantics up front; "The agent is not allowed to invent system meaning." (section "Contracts before code").
- A verification pyramid ordered by cost, using "The lightest mechanism that can falsify a hypothesis" first (sections "Verification pyramid", "Contracts before code").
- Each verification layer was added because something slipped through the layer below (redis-rust section).
- Performance work as hill-climbing with a safety net: propose, run the full suite, keep if green and faster, revert otherwise (section "Performance").
- Human role: define the idea and invariants, strengthen the harness, set measurable targets, approve architecture (section "What the human actually did").
- "invest in the harness in proportion to the cost of failure" (section "Where this goes").
Evidence and numbers: redis-rust reached staging with comparable latency and an 87% memory reduction after the agent fixed an 8x memory overuse; Helix sustained 10 million simulation seeds and about 93% of peak disk throughput; writing invariants costs roughly 2 to 3x the effort of the code; DST caught a WAL data-loss bug that unit tests did not.
Caveats: Distributed-systems infrastructure with formal tools (TLA+, Kani, DST); heavy for product web apps. The first agent implementation "compiled and passed tests, but many details were subtly wrong". They ask the obvious question themselves: "What happens when the harness itself is wrong?"
Relevance: medium. The principles (explicit invariants, cheapest falsifier first, revert-on-red) scale down; the tooling mostly does not.

### StrongDM Software Factory (Justin McCarthy, StrongDM, site dated 2025-07-14, cites 2026 material) `[SDM-factory]`
File: refs/articles/factory.strongdm.ai/index/article.md   URL: https://factory.strongdm.ai/
Thesis: A team working under two rules, code "must not be" written by humans and "must not be" reviewed by humans, relies on scenarios held outside the codebase and behavioural clones of third-party services for validation.
Practices: "scenarios" are end-to-end user stories "often stored outside the codebase (similar to a "holdout" set in model training)" so the agent cannot rewrite them; "satisfaction" is the fraction of observed trajectories that likely satisfy the user, judged by an LLM; a "Digital Twin Universe" of clones of Okta, Jira, Slack and Google services allows high-volume testing.
Evidence and numbers: none on quality. The rule of thumb "$1,000 on tokens today" per engineer.
Caveats: Tests in the repo were "reward hacked": "return true is a great way to pass narrowly written tests" (wording paraphrased around the bolded phrase). Manifesto-style, no defect data.
Relevance: low to medium. The holdout idea (acceptance checks the implementing agent cannot edit) matches [TW-harness-cost].

### Compound Engineering: How Every Codes With Agents (Kieran Klaassen and Dan Shipper, Every, 2025-12-11) `[EV-compound]`
File: refs/articles/every.to/chain-of-thought-compound-engineering-how-every-codes-with-agents/article.md   URL: https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents
Thesis: Each unit of work should make the next one easier. The loop is Plan → Work → Review → Compound, where the fourth step writes what was learned back into instructions, docs, agents and checks.
Practices:
- Compound step: capture what worked and what did not, add YAML frontmatter so it is findable, update CLAUDE.md or create an agent, and ask "Would the system catch this automatically next time?" (section "4. Compound").
- File layout: `CLAUDE.md`, `docs/brainstorms/`, `docs/plans/`, `docs/solutions/` (categorised solved problems), `todos/` with files named like `001-ready-p1-fix-auth.md` (section "Where things live").
- Review output as one list prioritised P1 (must fix), P2 (should fix), P3 (nice to fix); a `/triage` step lets the human approve, skip or change each finding (sections "Review agents", "/triage").
- Planning spawns parallel research agents for codebase patterns, framework docs and best practices (section "/workflows:plan").
- Three questions before approving output: "What was the hardest decision you made here?", "What alternatives did you reject, and why?", "What are you least confident about?" (section "Three questions").
- Agent-native checklist: can the agent run the app, tests, linters, migrations, seed data; create branches and PRs and read PR comments; view logs, take screenshots, inspect network requests, reach error tracking (section "The agent-native checklist").
- Plan approval must be explicit: "Silence is not approval" (section "Plan approval").
- Prototype in a throwaway "baby app", then "Delete everything and start over with a proper plan." (sections "The baby app approach", "UX discovery loop").
- Codify design and copy voice as skills with concrete values and before/after examples (sections "Codifying design taste", "Codify your voice").
Evidence and numbers: Every runs five products "with primarily single-person engineering teams"; the plugin ships 26 agents, 23 commands and 13 skills; `/lfg` spawns more than 50 agents; time split claimed as 80% plan and review, 20% work and compound. "In our experience, first attempts have a 95 percent garbage rate."
Caveats: No measured outcomes. The author always runs `--dangerously-skip-permissions` on a laptop, relying on git, tests, PR review and worktrees. The 14 role-named review agents (security-sentinel, performance-oracle and others) conflict with [HL-skillissue] and [AMP-subagents], which found role-specialised subagents unhelpful, and the large plugin conflicts with [HL-skillissue]'s warning against installing many skills and agents up front. Says human review should skip security and style because review agents did it, which [TES-charter] shows can miss real defects.
Relevance: high. Closest analogue to the user's own command set (plan, work, review, learn); `docs/solutions/` and the three questions are cheap to adopt.

### Saved but not read

These were saved to the `industry` collection during enumeration and not read, so nothing above relies on them:
- refs/articles/openai.com/index-unrolling-the-codex-agent-loop/article.md (Codex agent loop internals)
- refs/articles/openai.com/index-unlocking-the-codex-harness/article.md (Codex App Server)
- refs/articles/developers.openai.com/codex-guides-build-ai-native-engineering-team/article.md
- refs/articles/developers.openai.com/blog-mastering-codex-remote-for-engineering/article.md
- refs/articles/lucumr.pocoo.org/2026-2-9-a-language-for-agents/article.md
- refs/articles/martinfowler.com/articles-durable-execution-agents-html/article.md
- refs/articles/steve-yegge.medium.com/vibe-maintainer-a2273a841040/article.md
- refs/articles/ampcode.com/how-to-build-an-agent/article.md
- refs/articles/humanlayer.dev/blog-show-me-skill/article.md
- refs/articles/shopify.engineering/remote-dev/article.md
- The embedded `SPEC.md` inside the Symphony article (one 52,000-character line).

