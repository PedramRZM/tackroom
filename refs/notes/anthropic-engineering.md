# Anthropic engineering and research posts (28 posts, 2024-12 to 2026-11)

Sources read: 28 of 28, each in full from the saved `article.md`. None failed to load.

Limits of the saved copies (applies to every claim below):

- The saved `article.md` files have no tables, code blocks, figures or footnote text; the converter
  dropped them. A second fetch with `tools/refs article --via jina` returned the same stripped text
  (the six duplicate folders this produced were removed again). Where a number or snippet matters,
  I read it from the HTML of the live page on 2026-11-10 and mark it **[live page, not in saved
  file]**. Those items are data read from the page, not quotes from the saved text.
- The saved URLs are `anthropic.com/research/<slug>`. The posts link to each other as
  `anthropic.com/engineering/<slug>`. On 2026-11-10 `anthropic.com/engineering/claude-code-best-practices`
  redirects to `code.claude.com/docs/en/best-practices`, a different and newer document that is not
  part of this batch; nothing from it is used here.
- No source contained an instruction aimed at the reader. Three posts quote or describe example
  injection prompts to explain attacks (AUTO §Why the prompt-injection probe matters, TRUST §Defending
  against attacks, CONTAIN §Risk we missed: The user as an injection vector). They are
  illustrations, not attempts.

Source keys, oldest first (date is the post date in `meta.json`):

| Key | Date | Title |
| --- | --- | --- |
| BEA | 2024-12-19 | Building effective AI agents |
| SWE | 2025-01-06 | Claude SWE-Bench performance |
| THINK | 2025-03-20 | The "think" tool for complex tool use |
| CCBP | 2025-04-18 | Claude Code Best Practices |
| MARS | 2025-06-13 | How we built our multi-agent research system |
| FRAME | 2025-08-04 | Our framework for safe and trustworthy agents |
| TOOLS | 2025-09-11 | Writing effective tools for AI agents |
| PM1 | 2025-09-17 | A postmortem of three recent issues |
| AUTON | 2025-09-29 | Enabling Claude Code to work more autonomously |
| CTX | 2025-09-29 | Effective context engineering for AI agents |
| SKILLS | 2025-10-16 | Equipping agents with Agent Skills |
| SBX | 2025-10-20 | Making Claude Code safer with sandboxing |
| MCPX | 2025-11-04 | Code execution with MCP for efficient agents |
| ATU | 2025-11-24 | Introducing advanced tool use for Claude |
| HARN1 | 2025-11-26 | Effective harnesses for long-running agents |
| EVALS | 2026-01-09 | Demystifying evals for AI agents |
| CC | 2026-02-05 | Building a C compiler with parallel Claudes |
| NOISE | 2026-02-05 | Infrastructure noise in agentic coding evals |
| LRC | 2026-03-23 | Long-running Claude for scientific computing |
| HARN2 | 2026-03-24 | Harness design for long-running apps |
| AUTO | 2026-03-25 | How we built Claude Code auto mode |
| MA | 2026-04-08 | Scaling Managed Agents with stable interfaces |
| TRUST | 2026-04-09 | Trustworthy agents in practice |
| PM2 | 2026-04-23 | An update on Claude Code quality reports |
| CONTAIN | 2026-05-25 | How we contain Claude across products |
| SCION | 2026-10-13 | Redesigning source control at Anthropic |
| JUDGE | 2026-10-27 | How AI agents shape experts' judgment calls |
| MEM | 2026-11-06 | The components of agent memory |

Locators are section headings of the saved file, written as (KEY §Heading).

## Cross-cutting findings

### Recurring practices

1. Start with the simplest setup and add a component only when it measurably helps; this is said in 2024 and repeated in 2025 and 2026. "we recommend finding the simplest solution possible, and only increasing complexity when needed" (BEA §When (and when not) to use agents); also CTX §Context retrieval and agentic search, HARN2 §Iterating on the harness, MA intro.
2. Every harness component is a bet about a model weakness and goes stale; re-test it on each model release and remove what no longer carries weight. "every component in a harness encodes an assumption about what the model can't do on its own" (HARN2 §Iterating on the harness); MA intro; PM2 §Going forward.
3. Give the agent a machine-checkable target and a way to observe its own output (tests, a reference implementation, a browser). Without one, an autonomous loop solves the wrong problem. CCBP §3b, HARN1 §Testing, CC §Write extremely high-quality tests, LRC §The test oracle, BEA §Agents.
4. Agents over-rate their own work and declare completion early; a separate, deliberately sceptical evaluator with its own context works better than self-review. HARN1 §The long-running agent problem and §Testing, HARN2 §Why naive implementations fall short, CCBP §6a, CC §Looking forward.
5. Treat context as a scarce budget: aim for the smallest set of high-signal tokens, load detail just in time through file paths and search, and keep bulky output out of the window. CTX §The anatomy of effective context, SKILLS §The anatomy of a skill, MCPX, ATU, TOOLS §Optimizing tool responses, CC §Put yourself in Claude's shoes.
6. Persist state in files and git, not in the conversation: a progress or changelog file, a feature or task list, descriptive commits. A fresh session must be able to orient itself from those alone. HARN1, LRC §Memory across sessions and §Git as coordination, CC, CTX §Structured note-taking, MARS §Appendix, MEM.
7. Work on one feature or task at a time and leave the tree mergeable at the end of each session. HARN1 §Incremental progress, HARN2 §The architecture, LRC §Git as coordination.
8. Sub-agents are mainly a context-isolation tool: they explore in their own window and return a short summary or a file reference. They cost many more tokens and pay off for breadth-first, parallelisable work. CTX §Sub-agent architectures, MARS §Benefits of a multi-agent system and §Appendix, CCBP §3a.
9. A delegated task needs an objective, an output format, tool and source guidance, and boundaries; vague one-line briefs cause duplicated and misdirected work. MARS §Prompt engineering and evaluations for research agents (item 2).
10. Invest in the agent-computer interface: few, distinct, well-named tools; descriptions written as for a new hire; errors that say what to do next; outputs that are short by default. BEA §Appendix 2, SWE §Tool Using Agent, TOOLS, CTX, CC.
11. Start evaluating at once with a small set (about 20 to 50 tasks taken from real failures), prefer deterministic graders, grade outcomes over paths, and read transcripts. MARS §Effective evaluation of agents, EVALS §Going from zero to one, TOOLS §Running an evaluation.
12. Small prompt and harness edits can move quality noticeably in both directions, and narrow eval sets miss it; change one thing at a time and measure broadly. PM2 §A system prompt change to reduce verbosity, HARN2 §Iterating on the harness, MARS (emergent behaviours paragraph), PM1 §Why detection was difficult.
13. Per-action approval does not work as oversight at volume: users approve about 93% of prompts and stop reading them. Replace it with boundaries (sandbox), a classifier (auto mode), or plan-level review. SBX, AUTO intro, TRUST §Designing for human control, CONTAIN intro.
14. Put the deterministic boundary first (filesystem and network limits, credentials outside the agent's reach) and treat model-level defences as probabilistic. CONTAIN §Summary, SBX, MA §Decouple the brain from the hands, AUTO §Results.
15. Everything the agent reads is an attack surface, including trusted tools' output, repository config files, skills, and persistent memory. CONTAIN §Trusting what the agent reads and §Looking ahead, SKILLS §Security considerations, AUTO §Threat model, TRUST §Defending against attacks.
16. The commonest real incidents are overeager, well-meant actions that go beyond what was asked (deleting remote branches, hunting for credentials, skipping a failing pre-check), not hostile behaviour. AUTO §Threat model, FRAME §Aligning agents with human values and expectations, CONTAIN §Three types of risk.
17. Prefer heuristics and a few canonical examples to long rule lists; say what something is for and leave the method to the model. With stronger models, fixed rules can reduce performance. CTX §The anatomy of effective context, MARS (prompting strategy paragraph), MEM §Steering Claude to write memory.
18. Code and scripts beat token generation for deterministic or bulk work: put scripts in skills, call tools from code, filter data before it reaches the model. SKILLS §Skills and code execution, MCPX, ATU §Programmatic Tool Calling.
19. Plan before coding and review the plan, since that is where human judgement adds most. CCBP §3a, TRUST §Designing for human control, HARN2 (planner), LRC §Draft a plan and iterate locally.
20. Human sign-off is weaker than it looks: experts adopt an agent's framing on judgement calls without noticing, and autonomous runs make it easy to see passing tests and stop checking. JUDGE, CC §Looking forward, SCION §What we learned building Scion.

### (a) Long-running agent harness patterns

**HARN1 (2025-11-26): initializer plus coding agent across context resets.**

- Problem statement. A loop over context windows with compaction is not enough to build a production-quality web app from a one-line prompt: "compaction isn’t sufficient" (HARN1 §The long-running agent problem). Two failure patterns: the agent tries to build everything at once and runs out of context mid-feature, leaving the next session to guess; later, a session sees progress and declares the project finished (same section).
- Two prompts, one harness. Session one gets an initializer prompt that creates `init.sh`, `claude-progress.txt`, the feature list and an initial git commit. Every later session gets a coding prompt: make incremental progress, then leave structured updates (HARN1 §The long-running agent problem). **[live page, not in saved file]** footnote 1: the two are called separate agents only because the first user prompt differs; system prompt, tools and harness are identical.
- Feature list file. The initializer expands the prompt into a comprehensive requirements file, over 200 features for the claude.ai clone, all marked failing at the start. Coding agents may only flip the `passes` field. JSON was chosen because "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files" (HARN1 §Feature list). The prompt uses strong wording: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." (same section). **[live page, not in saved file]** one entry has the keys `category`, `description`, `steps` (a list of user-level steps) and `passes: false`; the sample session reads `feature_list.json`.
- One feature per session, clean hand-off. The agent is "asked to work on only one feature at a time" (HARN1 §Incremental progress). Clean state means code fit to merge to main: no major bugs, orderly, documented (HARN1 §The long-running agent problem).
- Git and progress notes. The best way found to get a clean state was to "ask the model to commit its progress to git with descriptive commit messages and to write summaries of its progress in a progress file" (HARN1 §Incremental progress). Git also lets the agent revert bad changes and recover a working state.
- Testing requirement. Without explicit prompting Claude marked features done after unit tests or `curl` checks that did not prove the feature worked end to end. It did well once "explicitly prompted to use browser automation tools and do all testing as a human user would" (HARN1 §Testing). Limit: "Claude can’t see browser-native alert modals through the Puppeteer MCP" (same section), and features using them were buggier.
- Session start routine (HARN1 §Getting up to speed): run `pwd`; read git log and progress files; read the feature list and pick the highest-priority unfinished feature; run `init.sh` to start the dev server; run a basic end-to-end check (new chat, send message, get reply) before touching anything new, so a broken state is fixed first.
- **[live page, not in saved file]** summary table of four problems and their fixes: declares victory too early (feature list; pick one feature); leaves bugs or undocumented progress (initial repo and progress file; start by reading notes and git log and running a basic test, end with a commit and progress update); marks features done prematurely (self-verify, mark passing only after careful testing); wastes time working out how to run the app (`init.sh`).
- Costs and durations: none reported in HARN1.
- Open question stated in HARN1 §Future work: "it’s still unclear whether a single, general-purpose coding agent performs best across contexts", or whether testing, QA and cleanup agents would do better. HARN2 answers part of this four months later.

**HARN2 (2026-03-24): planner, generator, evaluator. Revises HARN1.**

- Two failure modes the earlier harness left: loss of coherence as the window fills, including *context anxiety* (wrapping up early near a perceived limit), and lenient self-evaluation (HARN2 §Why naive implementations fall short).
- Context reset versus compaction. A reset clears the window and starts a fresh agent from a structured hand-off artifact; compaction summarises earlier turns in place for the same agent. A reset gives a clean slate but costs orchestration complexity, tokens and latency, and depends on the hand-off holding enough state. Sonnet 4.5 needed resets because compaction alone left context anxiety in place (HARN2 §Why naive implementations fall short).
- What changed with newer models: "Opus 4.5 largely removed that behavior on its own, so I was able to drop context resets from this harness entirely." (HARN2 §The architecture). The build then ran as one continuous session with the Agent SDK's automatic compaction. MA (2026-04-08) confirms: "The resets had become dead weight." (MA intro).
- Evaluator separation. "tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work" (HARN2 §Why naive implementations fall short).
- Frontend loop (HARN2 §Frontend design): four criteria given to both agents, namely design quality, originality, craft, functionality, with the first two weighted higher; evaluator calibrated with few-shot examples and score breakdowns; evaluator drives the live page through the Playwright MCP before scoring; 5 to 15 iterations per generation; runs up to four hours; after each evaluation the generator chooses to refine or to pivot. Caveats: scores plateaued; "I regularly saw cases where I preferred a middle iteration over the last one"; criteria wording (the phrase about museum quality) pulled outputs toward one look.
- Full-stack roles (HARN2 §The architecture):
  - Planner: turns a 1 to 4 sentence prompt into a full product spec; told to be ambitious and to stay at product context and high-level technical design, because wrong low-level detail in a spec cascades into the build.
  - Generator: works in sprints, one feature at a time, on React, Vite, FastAPI and SQLite (later PostgreSQL); self-evaluates before hand-off; uses git.
  - Evaluator: clicks through the running app with the Playwright MCP, checks UI, API endpoints and database state, and grades product depth, functionality, visual design and code quality against hard thresholds; any criterion below threshold fails the sprint and returns detailed feedback.
  - Sprint contract: before each sprint the generator proposes what it will build and how success will be verified, and the evaluator reviews it until both agree. "Sprint 3 alone had 27 criteria covering the level editor" (HARN2 §Running the harness).
  - "Communication was handled via files" (HARN2 §The architecture): one agent writes a file, the other reads it and answers in that file or a new one.
- Tuning the evaluator: "Out of the box, Claude is a poor QA agent." (HARN2 §Running the harness). It found real issues and then talked itself into approving, and it tested superficially. The fix was a loop of reading evaluator logs, finding where its judgement differed from the author's, and editing the QA prompt; it took several rounds.
- First run, Opus 4.5, prompt for a 2D retro game maker. **[live page, not in saved file]** Solo agent: 20 min, $9. Full harness: 6 hr, $200. The saved text gives only "The harness was over 20x more expensive" (HARN2 §Running the harness). The solo build's core play mode did not work; the harness build's did. The planner produced a 16-feature spec over ten sprints.
- Simplifying. A radical cut failed and hid which parts mattered; the working method was "removing one component at a time and reviewing what impact it had on the final result" (HARN2 §Iterating on the harness).
- Removed with Opus 4.6: the sprint construct; the evaluator moved to a single pass at the end. Kept: the planner ("Without the planner, the generator under-scoped", HARN2 §Removing the sprint construct) and the evaluator, whose value now depends on the task: "It is worth the cost when the task sits beyond what the current model does reliably solo." (same section).
- Second run, Opus 4.6, prompt for a browser DAW: "The run was still lengthy and expensive, at about 4 hours and $124 in token costs." (HARN2 §Results from the updated harness). **[live page, not in saved file]** breakdown: planner 4.7 min, $0.46; build round 1, 2 hr 7 min, $71.08; QA round 1, 8.8 min, $3.24; build round 2, 1 hr 2 min, $36.89; QA round 2, 6.8 min, $3.09; build round 3, 10.9 min, $5.88; QA round 3, 9.6 min, $4.06; total 3 hr 50 min, $124.70. QA still caught stubbed features in rounds 1 and 2.
- Standing lesson: on each new model, strip parts that no longer carry weight and add ones that newly pay off (HARN2 §What comes next).

**Simple loops (CC 2026-02-05, LRC 2026-03-23).**

- CC wraps Claude Code in an endless loop, each iteration a fresh session in a fresh container. **[live page, not in saved file]** the script is `while true`, running `claude --dangerously-skip-permissions -p "$(cat AGENT_PROMPT.md)"` and writing to `agent_logs/agent_${COMMIT}.log`. The post says to run it in a container, not on your machine (CC §Enabling long-running Claudes). The prompt asks Claude to break the problem into small pieces, track what it is doing, and choose the next task itself. One session killed its own loop with `pkill -9 bash`.
- LRC, for a tightly coupled numerical code, uses one sequential agent: the plan and rules in `CLAUDE.md` (which the agent may edit), `CHANGELOG.md` as the progress file, a reference implementation as test oracle, commit and push after each unit of work, Claude Code inside `tmux` on a compute node. It adds the *Ralph loop* to counter *agentic laziness*: a loop that re-prompts when the agent claims to be done. **[live page, not in saved file]** invocation: `/ralph-loop:ralph-loop "<task and success criterion>" --max-iterations 20 --completion-promise "DONE"`. LRC also names `/loop` and GSD as similar patterns (LRC §The execution loop).
- Inference: these two posts postdate HARN1 and show that with Opus 4.6 a plain loop plus a progress file plus a strong test oracle is the baseline; the initializer and feature-list machinery of HARN1 is one way to supply the progress file and the oracle, not a requirement.

**Other pieces.** MARS §Appendix (2025-06): summarise finished phases to external memory, start fresh sub-agents with clean context and a careful hand-off, and resume from checkpoints after errors instead of restarting. CTX §Context engineering for long-horizon tasks (2025-09): compaction suits back-and-forth work, note-taking suits iterative development with milestones, multi-agent suits parallel exploration. MA §The session is not Claude's context window (2026-04): keep the full event log outside the context window so that compaction decisions stay recoverable. AUTON (2025-09): checkpoints with `/rewind` cover Claude's edits only, "and we recommend using them in combination with version control" (AUTON §Checkpoints).

### (b) Parallel agents: lessons from the C compiler project (CC, 2026-02-05)

- Setup: 16 agents, each in its own Docker container, a bare git repo mounted at `/upstream`, each agent cloning to `/workspace` and pushing back. No orchestrator: "I don’t use an orchestration agent." (CC §Running Claude in parallel). No agent-to-agent messaging.
- Task locking. An agent claims a task by committing a text file under `current_tasks/` (for example `current_tasks/parse_if_statement.txt`). "If two agents try to claim the same task, git's synchronization forces the second agent to pick a different one." (same section). After the work: pull, merge, push, remove the lock. Merge conflicts were frequent and the agents resolved them.
- The verifier decides what gets built: "it’s important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem" (CC §Write extremely high-quality tests). When new features kept breaking old ones late in the project, the author added a CI pipeline and stricter enforcement so that new commits could not break existing code.
- Test output designed for an agent (CC §Put yourself in Claude's shoes):
  - Context pollution: "The test harness should not print thousands of useless bytes." Print a few lines, log detail to a file, and make logs greppable: "Claude should write ERROR and put the reason on the same line so grep will find it". Pre-compute summary statistics.
  - Time blindness: "Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress." The harness prints progress rarely and has a default `--fast` mode that "runs a 1% or 10% random sample", deterministic per agent and different across agents, so each agent can spot its own regressions while the fleet covers everything.
  - Orientation: each agent starts with no context, so the prompt requires extensive READMEs and progress files kept current.
- Parallelism needs many independent failing tests. With hundreds of failing tests each agent picked a different one. Compiling the Linux kernel was one task, every agent hit the same bug and overwrote the others: "Having 16 agents running didn't help because each was stuck solving the same task." (CC §Make parallelism easy).
- Oracle use. GCC served as a known-good oracle: compile most kernel files with GCC and a random subset with the new compiler; a failure localises the bug to that subset, which is narrowed further. This split one task into many. Delta debugging was still needed for files that failed only in pairs (same section).
- Roles (CC §Multiple agent roles): one agent merging duplicate code, one on compiler speed, one on output code efficiency, one critiquing the design as a Rust developer and restructuring, one on documentation.
- Scale and cost: nearly 2,000 sessions over two weeks, 2 billion input and 140 million output tokens, just under $20,000, a 100,000-line compiler, 99% pass rate on most compiler test suites (CC §Evaluation).
- Ceiling: "New features and bugfixes frequently broke existing functionality." (CC §Evaluation). The generated code is slower than GCC with optimisation off, the 16-bit x86 stage calls GCC, and the Rust quality is below expert level.
- Warning from the author, a former penetration tester: "it is easy to see tests pass and assume the job is done, when this is rarely the case" (CC §Looking forward).
- Contrast, LRC §The premise (2026-03-23): a deeply coupled pipeline "may be better suited to a single agent working sequentially, spawning subagents as needed". Earlier, MARS (2025-06-13) held that "most coding tasks involve fewer truly parallelizable tasks than research" (MARS §Benefits of a multi-agent system). CC shows the condition under which coding does parallelise: a large supply of independent, machine-checked failing tests.

### (c) Context engineering principles (CTX 2025-09-29, with later revisions)

- Definition and goal: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome" (CTX §Conclusion). The reason given is context rot: recall drops as tokens increase, a gradient and not a cliff (CTX §Why context engineering is important).
- Right altitude for prompts. Two failure modes: brittle hard-coded if-else logic, and vague guidance that assumes shared context. The target is "specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics to guide behavior" (CTX §The anatomy of effective context). Organise into labelled sections (XML tags or Markdown headers). Start with a minimal prompt on the best model, then add instructions and examples for observed failures. "minimal does not necessarily mean short" (same section).
- Examples: a few diverse, canonical examples; the post explicitly advises against stuffing a list of edge-case rules into the prompt (same section).
- Tools as context: a minimal, non-overlapping tool set; if a human cannot say which tool applies, the agent cannot either (same section).
- Just-in-time retrieval: keep light identifiers (paths, stored queries, links) and load content with tools at run time. File names, folder structure and timestamps are signals. Claude Code is a hybrid: `CLAUDE.md` loaded up front, `glob` and `grep` for the rest, which avoids stale indexes (CTX §Context retrieval and agentic search). Trade-off: run-time exploration is slower, and without guidance an agent wastes context on dead ends. Advice: do the simplest thing that works.
- Compaction: summarise near the limit and restart with the summary. In Claude Code the model keeps architectural decisions, unresolved bugs and implementation details and continues with the summary "plus the five most recently accessed files" (CTX §Compaction). Tune a compaction prompt for recall first, then precision. Clearing old tool results is the safest light form.
- Structured note-taking: the agent writes notes outside the window (a to-do list, `NOTES.md`) and reads them back after resets (CTX §Structured note-taking).
- Sub-agents: each may use tens of thousands of tokens and "returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)" (CTX §Sub-agent architectures).
- Supporting posts: `/clear` between tasks (CCBP §4f, 2025-04); skills load in three levels, metadata then `SKILL.md` body then linked files (SKILLS §The anatomy of a skill, 2025-10); deferred tool loading and code-side orchestration keep definitions and intermediate results out of context (MCPX, ATU, 2025-11); sub-agents can write results to files and return references, to avoid a *game of telephone* (MARS §Appendix, 2025-06).
- Revisions by later posts:
  - CTX calls compaction "the first lever". HARN1 (2025-11) and HARN2 (2026-03) report that compaction alone was not enough for Sonnet 4.5 on long builds, then that it became enough from Opus 4.5.
  - MA (2026-04) adds that compaction and trimming are irreversible: "irreversible decisions to selectively retain or discard context can lead to failures" (MA §The session is not Claude's context window); keep the raw log retrievable.
  - MEM (2026-11) refines note-taking: stronger models judge what to save better than fixed rules do, and the always-loaded layer must stay small (see (e)).
  - PM2 (2026-04) is a field example of context loss: a bug that dropped earlier reasoning each turn made Claude forgetful and repetitive (PM2 §A caching optimization that dropped prior reasoning).

### (d) Tool-writing principles, and what they mean for a project's own scripts

What the sources say:

- Spend as much effort on the agent-computer interface as on a human interface; "we actually spent more time optimizing our tools than the overall prompt" (BEA §Appendix 2).
- Make mistakes impossible (poka-yoke). The SWE-bench agent confused relative paths after changing directory, so "we simply made the tool always require an absolute path" (SWE §Tool Using Agent). String-replace edits that require exactly one match, with an error otherwise, were the most reliable edit format (same section).
- Choose formats the model writes easily: no line counting, no heavy escaping, close to text seen in the wild (BEA §Appendix 2).
- Fewer, higher-level tools. "More tools don’t always lead to better outcomes." (TOOLS §Choosing the right tools for agents). Prefer `search_logs` over `read_logs`, `schedule_event` over three list and create calls, `get_customer_context` over three lookups.
- Namespace by service and resource (`asana_projects_search`); prefix versus suffix choice affected evals (TOOLS §Namespacing your tools).
- Return meaning, not plumbing: "tool implementations should take care to return only high signal information back to agents" (TOOLS §Returning meaningful context from your tools). Resolve UUIDs to names; offer a `response_format` of concise or detailed.
- Bound output: pagination, filtering, truncation with sensible defaults. "For Claude Code, we restrict tool responses to 25,000 tokens by default." (TOOLS §Optimizing tool responses for token efficiency). When truncating, say how to narrow the query.
- Errors are prompts: state the specific fix, not a code or traceback (same section).
- Descriptions: "think of how you would describe your tool to a new hire on your team" (TOOLS §Prompt-engineering your tool descriptions); unambiguous parameter names such as `user_id`.
- Examples in definitions: one to five realistic examples per tool raised complex-parameter accuracy from 72% to 90% (ATU §Tool Use Examples).
- Many tools: defer loading and search on demand; "Keep your three to five most-used tools always loaded, defer the rest." (ATU §Best practices). MCP tool definitions alone reached 55K to 134K tokens in the examples given.
- Build tools with evals: realistic multi-call tasks, a held-out set, transcripts fed back to Claude Code to refactor the tools (TOOLS §How to write tools). Read what agents leave out: "what agents omit in their feedback and responses can often be more important than what they include" (TOOLS §Analyzing results). A tool-testing agent that rewrote a description cut later task completion time by 40% (MARS §Prompt engineering, item 5).
- Custom shell tools: Claude does not know them. Give the name with usage examples, tell it to run `--help`, and document frequent ones in `CLAUDE.md` (CCBP §2a).
- Scripts inside skills run without their source entering context; state whether a script is to be run or read (SKILLS §Skills and code execution, §Developing and evaluating skills).

Inference, applying this to a repository's own scripts (test runners, linters, migration, dev-server and verification scripts). None of the posts says this about project scripts as a whole; CC says it about a test harness and CCBP about custom bash tools.

- One script per workflow (for example a single check command) instead of many flags the agent must compose.
- Default output of a few lines with a summary count; full detail to a log file whose path is printed; failure lines start with a fixed token such as `ERROR` and carry the reason on the same line (CC).
- A fast default mode that runs a subset, with the full run explicit (CC, time blindness).
- Error messages that name the next command to run (TOOLS).
- Accept and print absolute paths (SWE).
- A `--help` that reads like a tool description, plus a short list of the scripts in the instruction file (CCBP).
- Keep the number of always-loaded MCP servers small; prefer a CLI the agent can call from the shell when it exists (ATU token figures; the CLI preference itself is inference).

### (e) Memory components, and what a file-based project memory should contain

Components named in MEM (2026-11-06):

- Session logs or transcripts: the raw record and the ground truth to check notes against.
- Memory notes: files the agent writes in a memory directory during a session.
- An injected top layer loaded at session start. In Claude Code auto memory, "It loads only the first 200 lines or 25 KB of `MEMORY.md`." (MEM §Dreaming can promote notes up the memory hierarchy), and that header works as an index.
- *Dreaming*: offline passes over logs and notes that correct wrong notes against transcripts, merge duplicates, fix dead links, build linked wiki pages, promote important notes upward and push detail down.
- Search over the corpus or transcripts, which combined with a wiki beat either alone in one test (61% versus 53% search-only and 48% wiki-only, MEM §Dreaming can build new memory representations).
- MEM excludes weights, in-context learning and compaction from its definition of memory.

What good memory content looked like:

- Store what the environment will not tell you. "Fable 5’s approach used memory for things the game didn’t explicitly tell it." (MEM §Claude has learned to judge salience). State readable from the screen each turn is redundant and goes stale. Strategy, plans and tested rules exist only if written down.
- Small and structured beats exhaustive: "Sonnet 3.7 wrote 413 memory files across 225 folders and earned one badge" against nine files in two folders plus `global.md` and four badges for Fable 5 (same section). The large store went out of date and cost steps to maintain.
- A dashboard file: `global.md` held the current goal, a plan, and the model's own rules for using memory; topic folders held route plans and gameplay strategies (same section).
- Rules with provenance and status. The best CL-Bench memories held a rule plus how it was verified, answers already confirmed, and warnings about traps: "Most of its entries included a rule (and also how it knew the rule was true)" (MEM §Memory can be a prediction about what the future will need). Mid-tier models at least marked facts as checked or unconfirmed.
- From the long-running posts: a progress file with current status, completed tasks, failed approaches with reasons, results at checkpoints and known limitations. "The failed approaches are important—without them, successive sessions will re-attempt the same dead ends." (LRC §Memory across sessions). HARN1 uses `claude-progress.txt` plus `feature_list.json` plus git log; CC uses READMEs, progress files, a running document of failed approaches, and `current_tasks/` lock files.

How to instruct it:

- "it helps to tell Claude what memory is for, but not *how* to use it" (MEM §Steering Claude to write memory). A fixed rule such as recording only failures removed much of the benefit for Opus 4.7 and Opus 5.
- Older or weaker models need explicit steps. Telling Sonnet 4.6 to read memory first and test its theories "nearly doubled its benchmark score"; Sonnet 5 read memory unprompted 9 times in 10, Sonnet 4.6 less than half the time (same section). Inference: when the same repository is used through other harnesses or weaker models, an explicit instruction to read the memory index first is still worth its tokens.
- Keep the injected layer small: "Injected memories use up valuable tokens, and an incorrect note can be carried into every session." (MEM §Dreaming can promote notes up the memory hierarchy). The post cites the Claude Code docs' warning that longer instruction files reduce adherence.

Failure modes:

- A wrong note is trusted later. In the Pokémon run a wrong landmark note caused the same fall three times until a dreaming pass corrected it against the transcript (MEM §Dreaming can correct memory).
- A wiki can grow larger than its sources and abstract nothing (MEM §Dreaming can build new memory representations).
- Several agents writing one shared table overwrote each other and lost facts. The fix was one page per contract, written by a single agent, "which quoted the terms word for word rather than summarizing them into a shared table"; a graded brief went from 72% to 100% of criteria (MEM §Dreaming can focus memory on a specific goal).
- Security: persistent memory, `CLAUDE.md` files and state directories are a persistence vector. "An injection that lands in any of these is reloaded each time the agent starts." (CONTAIN §Looking ahead).

Inference, a file-based project memory for a solo developer, assembled from the above: (1) a short index that is always loaded (current goal, next steps, pointers), kept well under the 200-line load limit; (2) topic notes holding verified rules with how they were verified, failed approaches with reasons, and traps; (3) a progress or changelog file per long task; (4) nothing that can be read from the repository, git history or a command; (5) a periodic consolidation pass that checks notes against transcripts or the code, merges duplicates and prunes; (6) review of memory diffs like code, since they are loaded every session.

### (f) Evals: starting small, grader types, and what a solo developer should measure

- Start now and small. "20-50 simple tasks drawn from real failures is a great start" (EVALS §Step 0). "We started with a set of about 20 queries representing real usage patterns." (MARS §Effective evaluation of agents). Early changes have large effects, so small samples show them.
- Sources of tasks: checks you already do by hand before a release, bug tracker, user-reported failures (EVALS §Step 1).
- Task quality: "A good task is one where two domain experts would independently reach the same pass/fail verdict." (EVALS §Step 2). Write a reference solution that passes all graders. A 0% pass rate over many trials usually means a broken task.
- Balance: test both when a behaviour should happen and when it should not. "One-sided evals create one-sided optimization." (EVALS §Step 3).
- Isolation: each trial starts clean. Shared state inflates or deflates results; "we observed Claude gaining an unfair advantage on some tasks by examining the git history from previous trials" (EVALS §Step 4).
- Grader types (EVALS §Types of graders for agents; method lists **[live page, not in saved file]**):
  - Code-based: string or regex match, fail-to-pass and pass-to-pass tests, static analysis (lint, types, security), outcome or state checks, tool-call checks, transcript metrics. Fast, cheap, reproducible; brittle to valid variation.
  - Model-based: rubric scoring, natural-language assertions, pairwise comparison, reference-based, multi-judge consensus. Flexible; non-deterministic and needs calibration against humans.
  - Human: expert review, spot-check sampling, A/B tests. Gold standard; slow and costly.
- Choice rule: "We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation." (EVALS §Step 5).
- Grade the result: "it’s often better to grade what the agent produced, not the path it took" (EVALS §Step 5). Give partial credit on multi-part tasks. Give an LLM judge an *Unknown* option.
- Capability evals start at a low pass rate; regression evals should sit near 100%; capability tasks graduate into the regression suite (EVALS §Capability vs. regression evals).
- Non-determinism: pass@k (at least one of k) versus pass^k (all k). At 75% per trial, three trials all pass about 42% of the time (EVALS §How to think about non-determinism).
- Read transcripts: "we do not take eval scores at face value until someone digs into the details of the eval and reads some transcripts" (EVALS §Step 7). Example: Opus 4.5 on CORE-Bench went from 42% to 95% once grading bugs, ambiguous specs and a constraining scaffold were fixed (EVALS §Step 5).
- Tracked metrics in the coding example **[live page, not in saved file]**: `n_turns`, `n_toolcalls`, `n_total_tokens`, time to first token, output tokens per second, time to last token; graders `deterministic_tests`, `llm_rubric`, `static_analysis`, `state_check`, `tool_calls`. The saved text adds that in practice coding evals use unit tests for correctness and an LLM rubric for quality (EVALS §Evaluating coding agents).
- Noise: infrastructure alone moved Terminal-Bench 2.0 by 6 points, and "leaderboard differences below 3 percentage points deserve skepticism until the eval configuration is documented and matched" (NOISE §Why we care).
- Evals miss things users feel. PM1: "we relied too heavily on noisy evaluations" (PM1 §Why detection was difficult). PM2: a prompt line passed weeks of internal testing and still cost 3% on a broader eval (PM2 §A system prompt change to reduce verbosity).
- Skills and tools follow the same route: find the gaps on representative tasks first, then write the skill (SKILLS §Developing and evaluating skills); build tools against an eval with a held-out set (TOOLS).

Inference, what a solo developer should measure. EVALS addresses product teams building agents; the mapping to a personal coding setup is mine.

- A regression set of 20 to 50 small tasks from one's own repositories where the agent once failed (wrong command, skipped verification, over-engineering, touching unrelated files), each with a deterministic check: tests pass, typecheck and lint clean, diff confined to expected paths, no test files weakened.
- Paired cases for each rule that can over-trigger, for example a skill or sub-agent that should fire and one that should not.
- Per task: pass or fail, turns, tool calls, total tokens, wall time. Run each task several times when comparing two versions of an instruction file, and change one line at a time (PM2's ablation practice).
- A single LLM-rubric grader only for what code cannot check (plan quality, summary honesty), spot-calibrated by hand.
- Read a sample of transcripts weekly (EVALS §How evals fit with other methods suggests weekly sampling for teams).
- Treat public leaderboard gaps of a few points as noise when choosing models or harnesses (NOISE).

### (g) Sandboxing, auto mode and containment

Threat model:

- AUTO §Threat model lists four causes of a dangerous action: overeager behaviour, honest mistakes about blast radius, prompt injection, and a misaligned model (not seen in practice, evaluated each release). The classifier is tuned to the first two.
- CONTAIN §Three types of risk lists user misuse, model misbehaviour and external attackers, and three places to defend: the environment, the model, and the external content the agent reaches.
- Why per-action prompts fail: "in practice users accept 93% of them anyway" (AUTO intro); "Our telemetry showed users approved roughly 93% of permission prompts." (CONTAIN intro).
- Incident log examples: deleting remote branches after a vague clean-up request, grepping the environment for other API tokens after an auth error, deleting the closest-named job, posting a script to a public Gist, retrying a failed deploy with a skip-verification flag (AUTO §Threat model).

What each layer blocks:

| Layer | Blocks | Does not block | Source |
| --- | --- | --- | --- |
| Default permissions (read-only, ask for writes, shell, network) | Writes, shell commands and network access until a human approves | Habitual approval: 93% of prompts are accepted | FRAME, SBX §Keeping users secure, CONTAIN §Pattern 2 |
| Allow rules (`/permissions`, `.claude/settings.json`) | Prompts for commands you listed | Anything a blanket interpreter rule lets through | CCBP §1c, AUTO §How permission decisions work |
| OS sandbox for bash (bubblewrap on Linux, Seatbelt on macOS; `/sandbox`) | Writes outside the working directory; network except through a proxy with a domain allowlist (CONTAIN describes network as denied by default); applies to child processes | Reads of host files by default (CONTAIN says reads are allowed); data leaving through an allowed domain; anything run unsandboxed after an approval | SBX §Sandboxed bash tool, CONTAIN §Pattern 2 and §Risk we missed: Exfiltration through an approved domain |
| Auto mode: prompt-injection probe on tool output | Flags suspicious content and tells the agent to re-anchor on the user's request | Injections it does not recognise; instructions typed by the user | AUTO §How it works, CONTAIN §The user as an injection vector |
| Auto mode: transcript classifier (Sonnet 4.6, two stages) | Destroy or exfiltrate, degrade security posture, cross trust boundaries, bypass review or affect others; more than twenty default block rules | About 17% of real overeager actions; cases where something approval-shaped is in the session | AUTO §The customizable slots, §Results |
| Container or VM (dev container without internet; Claude Code on the web, the Cowork VM and the Managed Agents sandbox also keep credentials outside) | Access to host files and, where they are kept outside, to credentials; lets the agent run unattended | Damage inside the mounted workspace; exfiltration through allowed endpoints | CCBP §3d, SBX §Claude Code on the web, CONTAIN §Pattern 3, MA §The security boundary |
| Scoped credentials and proxies (git proxy, token vault) | Token theft from the sandbox; pushes to other branches | Misuse within the granted scope | SBX §Claude Code on the web, MA §The security boundary |

Measured numbers:

- Sandboxing: "we've found that sandboxing safely reduces permission prompts by 84%" (SBX intro; repeated in CONTAIN §Pattern 2).
- Auto mode, full pipeline: 0.4% false positives on 10,000 real tool calls; "The 17% false-negative rate on real overeager actions is the honest number." (AUTO §Results), on 52 curated cases. Stage 1 alone has an 8.5% false-positive rate (AUTO §Two-stage classification). **[live page, not in saved file]** table: stage 1, 8.5% FPR, 6.6% FNR on overeager, 1.8% FNR on synthetic exfiltration (n = 1,000); full pipeline, 0.4% FPR, 17% FNR, 5.7% FNR.
- Model-level injection resistance: Opus 4.7 on the Gray Swan benchmark holds attack success to roughly 0.1% on single attempts and around 5 to 6% after 100 adaptive attempts (CONTAIN §Three types of risk).
- Direct injection through the user: a phished employee pasted a prompt that asked for `~/.aws/credentials` to be read and posted out. "Across 25 retries of that prompt, Claude completed the exfiltration 24 times." (CONTAIN §Risk we missed: The user as an injection vector).
- Experienced users auto-approve about twice as often as new users and interrupt more (CONTAIN §Pattern 2).

How auto mode decides (AUTO §How permission decisions work):

- Tier 1: built-in read-only tools and the user's allow rules. On entering auto mode "we drop permission rules that are known to grant arbitrary code execution": blanket shell access, wildcarded interpreters (python, node, ruby), package-manager run commands. Narrow rules carry over.
- Tier 2: file edits inside the project directory, no classifier call.
- Tier 3: everything else goes to the classifier: shell commands, web fetches, external tools, sub-agent spawns, file operations outside the project.
- The classifier sees only user messages and tool calls. Assistant text and tool results are stripped so the agent cannot argue its case and injected content cannot reach the classifier.
- Authorisation is read conservatively: "everything the agent chooses on its own is unauthorized until the user says otherwise" (AUTO §The fixed template). A vague clean-up request does not authorise a batch delete, and a question is not a directive.
- Three configurable slots with defaults: environment (trust boundary), block rules, allow exceptions. "By default, the only thing the classifier trusts is the git repo you’re currently working in." (AUTO §The customizable slots). "Run `claude auto-mode defaults` to see the full list." (same section). Edit the defaults instead of starting from scratch.
- Deny and continue: a block returns as a tool result telling the agent to find a safer path. "If a session accumulates 3 consecutive denials or 20 total, we stop the model and escalate to the human." (AUTO §Deny-and-continue). In headless mode (`claude -p`) the process terminates instead.
- Sub-agents: the classifier checks the delegation going out and the sub-agent's action history coming back (AUTO §Multi-agent handoffs).

Positioning, and how later posts revise earlier ones:

- CCBP (2025-04) offered `--dangerously-skip-permissions` in a container without internet as the way to run unattended. SBX (2025-10) added the OS sandbox. AUTO (2026-03) presents auto mode as the replacement for the skip-permissions flag and calls sandboxing "safe but high-maintenance" (AUTO intro). It also says of auto mode: "It is not a drop-in replacement for careful human review on high-stakes infrastructure." (AUTO §Results).
- CONTAIN (2026-05) puts the two together. **[live page, not in saved file]** footnote 1: auto mode is one layer of defence in depth inside a sandbox, not a substitute for one. In the saved text: "The deterministic boundary is what gets hit when everything probabilistic misses." (CONTAIN §Summary).
- SBX (2025-10) claims a compromised session "can't steal your SSH keys, or phone home to an attacker's server". CONTAIN (2026-05) shows the limit of that claim: "The sandbox worked perfectly, and yet the data was exfiltrated." through an allow-listed API domain, and concludes "Every function reachable through any domain on an allowlist is now an attack surface." (CONTAIN §Risk we missed: Exfiltration through an approved domain).
- Pre-trust execution: three reported vulnerabilities ran code before the folder-trust prompt, for example a hook in a cloned repository's `.claude/settings.json`. The fix was to "defer parsing and execution of project-local configuration until after the user accepts the trust prompt" (CONTAIN §Risk we missed: Everything before the trust dialog).
- External content: "An audited connector isn’t the same as audited data" (CONTAIN §Three types of risk). Local tools can be read and pinned; remote MCP servers can change after approval, so try them against fake data first (CONTAIN §Trusting what the agent reads). Install skills only from trusted sources and audit bundled code (SKILLS §Security considerations).
- Custom parts fail first: "Be wary of custom components." (CONTAIN §Summary). The hypervisor, seccomp and gVisor held; Anthropic's own allowlist proxy did not.

Recommended configuration. Inference from the above; no post gives a single recommended setup for a solo developer.

- Turn the bash sandbox on (`/sandbox`; bubblewrap on Ubuntu) with both filesystem and network limits: "effective sandboxing requires *both* filesystem and network isolation" (SBX §Sandboxing: a safer and more autonomous approach).
- Keep the network allowlist short and think of each entry as a capability, since package registries, gists and APIs can receive data.
- Keep credentials out of reach rather than relying on intent: deny reads of `~/.aws`, `~/.ssh`, `.env` files and similar, and prefer short-lived, narrowly scoped tokens (CONTAIN phish result; MA token design).
- Use auto mode for unattended or long runs in place of skip-permissions, inside the sandbox, with the environment slot naming your own GitHub org and trusted hosts. Do not rely on it for production infrastructure.
- Remove blanket interpreter and package-runner allow rules; write narrow ones (specific test, lint, format commands), since auto mode drops the broad ones anyway.
- Run fully unattended loops (`claude -p` in a while loop, Ralph loops) in a container or VM with no host credentials (CC, CCBP §3d, CONTAIN on the reference devcontainer).
- Treat a freshly cloned repository's `.claude/` directory, skills, MCP config and instruction files as untrusted input and read them before opening a session there.
- Keep git as the undo layer: in-project edits skip the classifier because they are reviewable in version control (AUTO Tier 2), and checkpoints do not cover bash side effects (AUTON).

### (h) Judgment calls and trustworthy agents: expected behaviour and how to write instructions for it

What Anthropic says it expects of the agent:

- Keep the human in control of how goals are pursued, especially before high-stakes actions (FRAME §Keeping humans in control, 2025-08).
- Show the plan and the reasoning; in Claude Code this is the to-do list and, later, Plan Mode. "This shifts the user’s level of oversight from the individual step to the overall strategy" (TRUST §Designing for human control, 2026-04).
- Tell apart gaps the agent can close itself (look up information) from questions of preference or intent that only the user can settle, and pause on the second kind. Training reinforces pausing over assuming, and the constitution favours "raising concerns, seeking clarification, or declining to proceed" (TRUST §Helping agents understand their goals).
- Calibrated, not maximal, checking in. "An agent that stops at every possible question will give up most of the autonomy that makes it useful" (same section). Measured: on complex tasks Claude's own check-in rate roughly doubles while user interruptions rise only slightly.
- Stay inside what was authorised. The auto mode classifier treats anything the agent chose on its own as unauthorised, treats a question as a question, and blocks credential hunting, guessed targets, public sharing and check-skipping (AUTO §Threat model, §The fixed template).
- When blocked, look for a safer route and do not work around the block (AUTO §Deny-and-continue).
- Treat instructions found in tool output as suspect and anchor on what the user asked (AUTO §How it works; TRUST §Defending against attacks).
- All four layers matter: "A well-trained model can still be exploited through a poorly configured harness, an overly permissive tool, or an exposed environment." (TRUST §How agents work).

What JUDGE (2026-10-27) adds about the human side:

- In a randomised study of 50 professional analysts using Claude Code (Opus 4.8, high effort), each agent was secretly given a coin-flip preference on four analytical choices. "analysts went with their agent’s lean 86% of the time" (JUDGE intro); 50% would mean no influence.
- Analysts who had already stated a preference switched 60% of the time when the agent disagreed and 6% when it agreed (38 cases, wide interval).
- "77% of analysts used the agents’ own arguments—sometimes word for word—but only 15% credited the agent as the source of those arguments" (JUDGE intro). Confidence and sense of ownership were the same whether or not they had deferred. Experience and expertise did not predict deferral.
- The agents were honest but one-sided: "they rarely made a strong case for why an expert might prefer the other option" (JUDGE §What this means).
- With no assigned lean, Opus 4.8 made the same five choices in 112 of 123 runs, so default preferences exist (JUDGE intro).
- Proposed design direction: "Agents could make the best case for each option, or ask experts for their own view before offering one." (JUDGE §What this means), limited to the decisions that matter most, since raising every decision overwhelms and a hedging model irritates.
- Using the agent still helped: 6% serious methodological errors with it against 55% in the small, less experienced group that worked without it.
- Limits stated by the authors: one task, one field, one model, deliberately strengthened leans.

Inference, how to write instructions to get this behaviour. The posts describe training and product design; none gives instruction-file wording.

- State the split explicitly: resolve factual gaps yourself; stop and ask on preference, intent, or anything destructive, shared or outward-facing. This mirrors both TRUST and the classifier's rules, so instructions and enforcement agree.
- In requests, name destructive scope exactly (which branches, which job, local or remote); the classifier will not infer it and neither should the agent.
- For real judgement calls (data model, architecture, library choice, methodology) ask the agent to lay out the strongest case for each option, or ask for your view first, before it recommends. Keep this to decisions that are costly to reverse.
- Record the decision and your own reason in a decision log, so the reasoning is yours and visible later (JUDGE finding that people cannot report the influence afterwards).
- Do not count your own approval of agent work as an independent check on judgement calls; use a fresh-context reviewer for errors and your own deliberate decision for trade-offs.
- Tell the agent that a blocked or denied action is a boundary to respect and report, not a problem to route around (AUTO deny-and-continue).
- Prefer explaining purpose over issuing long rule lists (CTX altitude, MEM steering result).

### (i) The source-control redesign (SCION, 2026-10-13)

What it describes:

- Anthropic's merge rate went from about 2,500 changes a day (May 2026) to over 30,000 a day (September 2026). Git infrastructure became the bottleneck: nearly 100 GB of main-branch history, a compressed working copy over 25 GB, about 25 million CI checkouts a day, several hundred internal git mirrors (SCION §Growing our monorepo).
- Scion is an in-house version control system; the monorepo was migrated off git in five months by a team of seven, together with a review tool named Antique.
- Design principles (SCION §Principles for agent-scale source control): clients are always online; the server does history, blame, commits, merges and rebases while the client keeps a bounded cache; every query is also an API so jobs often need no checkout; all parts scale horizontally with no packfiles; commits are server-side, cheap and lock-free, and refs other than main and release branches are discouraged; the working copy is optional, sparse or virtualised.
- Mechanics: a *changeset* is a write-ahead-log entry listing changed files against its first parent; blame, path history and commit-graph skip lists are derived data; content-addressed objects served through tiered caches (`scion-daemon`, `scion-cache`, `scion-server`) with over 99% hit rate; client command `scn`.
- Results: infrastructure footprint 200x smaller than the git mirrors, checkouts in seconds instead of minutes, 25% CI CPU saved.
- Process lessons (SCION §What we learned building Scion): engineers supply system-level constraints and frequently refuse what the agent proposes; agents brute-force around constraints (reading the commit log linearly instead of asking the review tool); adversarial review is effective but myopic and pushed Claude to add needless validation; reviewers "now examine the *intent* of the change as opposed to reading every line of code"; hermetic simulations and fuzzing were affordable because Claude wrote them; *superfan* Claudes each watch one component's telemetry in a Slack channel.
- Merge queue: "A proper merge queue, for example, doesn’t make much sense at agent scale." and instead "we’ve invested in post-merge and pre-deploy automated testing" (SCION §What we learned, last item). Concurrent changes can conflict and Claude fixes the conflicts.

Usable today?

- Not the system: "Scion is by no means a suitable replacement for git for general use." (SCION §Contributing to the wider ecosystem). It is in-house, it needs its own review, search and CI, and the post says a public version would be hard to make useful. The proposals are aimed at git forges: server-side RPCs, a different negotiation protocol, sparse and shallow features that compose.
- The post expects this class of problem to reach others over the next six to twelve months, at very large scale only.
- Inference, what transfers to a solo developer now: (1) keep git; CC, LRC and HARN1 all use plain git as the coordination and recovery layer; (2) the review stance (review intent, state hard constraints up front, expect brute-force workarounds, restrain over-defensive output from adversarial review); (3) spending cheap agent effort on tests, simulations and fuzzing; (4) for parallel agents, favour fast automated post-merge checks and quick conflict repair over a serialising queue, but only when the test suite is strong (CC shows what happens otherwise).
- Tension with other posts: SCION's reviewers read for intent, not every line, while CC's author is uneasy about deploying software nobody verified, and JUDGE shows reviewers absorbing agent choices unnoticed.

### (j) Lessons from the two postmortems relevant to users

PM1 (2025-09-17), three infrastructure bugs, August to September 2025:

- Causes were serving-side: requests misrouted to servers configured for the 1M-token context window, a misconfiguration that corrupted token generation, and a compiler bug in approximate top-k sampling. "We never reduce model quality due to demand, time of day, or server load." (PM1 intro).
- Routing was sticky, so some users were hit repeatedly while others saw nothing; about 30% of Claude Code users in the window had at least one misrouted message (PM1 §Context window routing error).
- Their evals did not show it, partly because "Claude often recovers well from isolated mistakes" (PM1 §Why detection was difficult).
- For users: specific, reproducible reports were what isolated the bugs; use `/bug` in Claude Code (PM1 §What we're changing). Inference: sudden, inconsistent quality drops can be platform-side; note the date and version and compare against a known task before rewriting your own instructions.

PM2 (2026-04-23), three product-layer changes, March to April 2026. "The API was not impacted." (PM2 intro); Claude Code, the Agent SDK and Cowork were.

- Default reasoning effort lowered from `high` to `medium` on March 4 to cut latency; users found Claude Code less capable; reverted April 7. "This was the wrong tradeoff." (PM2 intro list). Now: "All users now default to `xhigh` effort for Opus 4.7, and `high` effort for all other models." (PM2 §A change to Claude Code's default reasoning effort). `/effort` changes it.
- A caching optimisation for sessions idle over an hour had a bug that cleared earlier thinking on every later turn. Symptoms: forgetfulness, repetition, odd tool choices, and faster usage-limit drain from cache misses. Shipped March 26, fixed April 10 in v2.1.101. It passed human and automated review, unit and end-to-end tests and dogfooding (PM2 §A caching optimization that dropped prior reasoning).
- One system prompt line to reduce verbosity: "Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail." (PM2 §A system prompt change to reduce verbosity). It passed weeks of internal testing; a broader eval later showed a 3% drop for Opus 4.6 and 4.7; reverted April 20 (v2.1.116).
- Process changes: "We will run a broad suite of per-model evals for every system prompt change to Claude Code", line-by-line ablations, soak periods, gradual rollout, staff using the public build, and model-specific prompt changes gated to the model they target (PM2 §Going forward).
- Opus 4.7 found the caching bug in a back-test of Code Review when given the other repositories as context; Opus 4.6 did not.

Inference for a user's own setup:

- Hard brevity caps in an instruction file are a known way to lose coding quality; ask for concise final messages without word limits on working text, and test the change.
- Effort level is a first-order quality setting; check it before blaming prompts, and keep it high for hard work.
- After a long idle gap, a fresh session with a hand-off note is safer than resuming, and unexplained forgetfulness is worth a restart and a report (`/feedback`).
- Treat each edit to instruction files as a change that needs evidence: one line at a time, a broad task set, and model-specific lines scoped to that model, which matters when the same files serve several models or harnesses.
- Pin or note the client version when comparing behaviour over time.

### (k) Every measured result or number

Numbers marked LP were read from the live page on 2026-11-10 and are not in the saved file.

| Number | What it measures | Source, date | Locator |
| --- | --- | --- | --- |
| 49% vs 45% | SWE-bench Verified, upgraded Claude 3.5 Sonnet vs previous best | SWE, 2025-01 | §Challenges (last paragraph) |
| 500 | Problems in SWE-bench Verified | SWE | intro |
| 12 steps; over 100 turns; >100k tokens | Example run; longer successful runs | SWE | §Examples of agent behavior, §Challenges |
| 0.570 vs 0.370 (54% relative) | tau-bench airline pass^1, think tool plus optimised prompt vs baseline, Claude 3.7 | THINK, 2025-03 | §Performance Analysis |
| 0.812 vs 0.783 | tau-bench retail pass^1, think tool vs baseline | THINK | §Performance Analysis |
| 0.623; +1.6% | SWE-bench score with Claude 3.7 Sonnet; isolated effect of think tool (n=30 vs n=144, p < .001) | THINK | §Performance on SWE-Bench |
| 90%+ | Share of git interactions many Anthropic engineers do through Claude | CCBP, 2025-04 | §3f |
| 2 to 3 | Iterations after which a visual result is typically much better | CCBP | §3c |
| 3 to 4 | Parallel git checkouts engineers run | CCBP | §6b |
| 90.2% | Multi-agent (Opus 4 lead, Sonnet 4 sub-agents) over single-agent Opus 4, internal research eval | MARS, 2025-06 | §Benefits of a multi-agent system |
| 80%; 95% | BrowseComp variance explained by token usage alone; by tokens, tool calls and model choice | MARS | §Benefits |
| 4x; 15x | Tokens used by agents vs chat; by multi-agent systems vs chat | MARS | §Benefits |
| 1 agent, 3 to 10 calls; 2 to 4 sub-agents, 10 to 15 calls each; more than 10 sub-agents | Effort scaling rules in the lead prompt | MARS | §Prompt engineering, item 3 |
| 50 | Sub-agents an early version spawned for simple queries | MARS | §Prompt engineering |
| 40% | Drop in task completion time after a tool-testing agent rewrote a tool description | MARS | §Prompt engineering, item 5 |
| up to 90% | Research time cut by parallel tool calls (3 to 5 sub-agents, 3+ tools each) | MARS | §Prompt engineering, item 8 |
| about 20 | Queries in the first eval set | MARS | §Effective evaluation of agents |
| 30% to 80% | Illustrative size of an early prompt-tweak effect (stated as "might") | MARS | §Effective evaluation of agents |
| 0.0 to 1.0 | Score range of the single LLM judge | MARS | §Effective evaluation of agents |
| 25,000 tokens | Default cap on a tool response in Claude Code | TOOLS, 2025-09 | §Optimizing tool responses |
| 206 vs 72 tokens | Detailed vs concise example tool response | TOOLS | §Returning meaningful context |
| 0.8%; 16% | Sonnet 4 requests misrouted at first; at the worst hour (Aug 31) | PM1, 2025-09 | §1. Context window routing error |
| about 30% | Claude Code users in the period with at least one misrouted message | PM1 | §1 |
| 0.18%; <0.0004% | Misrouted share on Bedrock; on Vertex AI | PM1 | §1 |
| 1,000 to 2,000 tokens | Typical size of a sub-agent's returned summary | CTX, 2025-09 | §Sub-agent architectures |
| 5 | Most recently accessed files re-attached after compaction in Claude Code | CTX | §Compaction |
| 84% | Reduction in permission prompts with sandboxing, internal usage | SBX, 2025-10; CONTAIN, 2026-05 | SBX intro; CONTAIN §Pattern 2 |
| 150,000 to 2,000 tokens (98.7%) | Token use, tools as code files vs all definitions loaded | MCPX, 2025-11 | §Code execution with MCP improves context efficiency |
| 50,000 tokens | Extra tokens when a 2-hour meeting transcript passes through the model twice | MCPX | §2. Intermediate tool results |
| 10,000 rows to 5 | Rows seen by the model after filtering in code | MCPX | §Context efficient tool results |
| 58 tools, about 55K tokens | Five-server MCP setup (GitHub 35 tools, 26K; Slack 11, 21K; Sentry 5, 3K; Grafana 5, 3K; Splunk 2, 2K) | ATU, 2025-11 | §Tool Search Tool, The challenge |
| about 17K; 134K | Jira server alone; largest tool-definition load seen at Anthropic | ATU | same |
| about 77K to about 8.7K (85%) | Context used before work begins, without and with Tool Search | ATU | §Our solution |
| 49% to 74%; 79.5% to 88.1% | MCP eval accuracy with Tool Search, Opus 4; Opus 4.5 | ATU | §Our solution |
| 43,588 to 27,297 tokens (37%) | Average usage with Programmatic Tool Calling on complex research tasks | ATU | §Programmatic Tool Calling |
| 25.6% to 28.5%; 46.5% to 51.2% | Internal knowledge retrieval; GIA benchmark, with Programmatic Tool Calling | ATU | same |
| 200KB to 1KB | Data entering context in the budget example | ATU | same |
| 72% to 90% | Complex parameter handling accuracy with Tool Use Examples | ATU | §Tool Use Examples |
| >10K tokens; 10+ tools; 3 to 5; 1 to 5 | Thresholds for Tool Search; tools kept loaded; examples per tool | ATU | §When to use, §Best practices |
| over 200 | Features in the feature list for the claude.ai clone | HARN1, 2025-11 | §Feature list |
| 20 to 50 | Tasks recommended for a first eval set | EVALS, 2026-01 | §Step 0 |
| 40% to >80% (also stated as started at 30%) | SWE-bench Verified progress in a year | EVALS | §Evaluating coding agents; §Step 7 |
| 42% to 95% | Opus 4.5 on CORE-Bench before and after fixing grading and scaffold | EVALS | §Step 5 |
| about 42% | pass^3 at a 75% per-trial rate | EVALS | §How to think about non-determinism |
| 3 months | Time Bolt took to build its eval system | EVALS | §Why build evaluations? |
| 16; nearly 2,000; two weeks | Agents; Claude Code sessions; duration | CC, 2026-02 | intro; §Evaluation |
| 2 billion in, 140 million out; just under $20,000 | Tokens and API cost | CC | §Evaluation |
| 100,000 lines; 99% | Compiler size; pass rate on most compiler test suites | CC | §Evaluation |
| 1% or 10% | Random test sample in `--fast` mode | CC | §Put yourself in Claude's shoes |
| over 60kb vs 32k | 16-bit output size vs Linux limit | CC | §Evaluation |
| 6 points (p < 0.01) | Terminal-Bench 2.0, most vs least resourced setup | NOISE, 2026-02 | intro |
| 5.8% to 2.1% to 0.5% | Infra error rate at 1x, 3x, uncapped resources | NOISE | §How we got here |
| p = 0.40 | Success-rate difference from 1x to 3x (within noise) | NOISE | §How we got here |
| -1.6 points; almost +4 points | Infra errors and success from 3x to uncapped | NOISE | §How we got here |
| 1.54 points | SWE-bench gain at 5x RAM (227 problems, 10 samples each) | NOISE | §How this affects measurement |
| below 3 points | Leaderboard gap that deserves scepticism | NOISE | §Why we care |
| 0.1% | Accuracy target against the reference solver; reached sub-percent in a few days | LRC, 2026-03 | §Draft a plan; §The result |
| 20 | `--max-iterations` in the Ralph loop example (LP for the command) | LRC | §The execution loop |
| 5 to 15; up to 4 hours | Generator-evaluator iterations; frontend run length | HARN2, 2026-03 | §Frontend design |
| 20 min, $9 vs 6 hr, $200 (LP); over 20x | Solo agent vs full harness, Opus 4.5, game maker | HARN2 | §Running the harness |
| 16 features, 10 sprints; 27 criteria | Planner's spec; sprint 3 contract | HARN2 | §Running the harness |
| about 4 hours, $124 (LP: 3 hr 50 min, $124.70) | Simplified harness, Opus 4.6, DAW | HARN2 | §Results from the updated harness |
| 4.7 min $0.46; 2 hr 7 min $71.08; 8.8 min $3.24; 1 hr 2 min $36.89; 6.8 min $3.09; 10.9 min $5.88; 9.6 min $4.06 (LP) | Planner; build 1; QA 1; build 2; QA 2; build 3; QA 3 | HARN2 | §Results from the updated harness |
| over 2 hours | Builder ran coherently without sprint decomposition | HARN2 | same |
| 93% | Permission prompts users accept | AUTO, 2026-03; CONTAIN, 2026-05 | AUTO intro; CONTAIN intro |
| n = 10,000; 52; 1,000 | Real traffic; real overeager actions; synthetic exfiltration | AUTO | §Results |
| 8.5% to 0.4% | False-positive rate, stage 1 then full pipeline | AUTO | §Two-stage classification |
| 17% | False-negative rate on real overeager actions, full pipeline | AUTO | §Results |
| 6.6%; 1.8%; 5.7% (LP) | Stage 1 FNR overeager; stage 1 FNR exfiltration; full pipeline FNR exfiltration | AUTO | §Results table |
| more than twenty | Default block rules | AUTO | §The customizable slots |
| 3 consecutive or 20 total | Denials before escalation to the human | AUTO | §Deny-and-continue |
| about 60%; over 90% | Drop in p50 and p95 time to first token after decoupling harness and sandbox | MA, 2026-04 | §Many brains, many hands |
| roughly doubles | Claude's check-in rate on complex vs simple tasks | TRUST, 2026-04 | §Helping agents understand their goals |
| March 4 to April 7; March 26 to April 10; April 16 to April 20 | Windows of the three Claude Code regressions | PM2, 2026-04 | intro |
| 3% | Eval drop from the verbosity instruction, Opus 4.6 and 4.7 | PM2 | §A system prompt change |
| ≤25 words; ≤100 words | Limits in the reverted instruction | PM2 | same |
| over an hour; over a week | Idle threshold for the caching change; time to find the root cause | PM2 | §A caching optimization |
| about 0.1%; about 5 to 6% | Opus 4.7 injection success, single attempt; after 100 adaptive attempts (Gray Swan) | CONTAIN, 2026-05 | §Three types of risk |
| roughly 83% | Overeager behaviours auto mode catches | CONTAIN | same |
| 24 of 25 | Runs in which a phished prompt exfiltrated credentials | CONTAIN | §The user as an injection vector |
| about 2x | Experienced users' auto-approve rate vs new users | CONTAIN | §Pattern 2 |
| 3 | Reported vulnerabilities that ran before the trust dialog (mid-2025 to January 2026) | CONTAIN | §Everything before the trust dialog |
| 2,500 to over 30,000 per day | Merged changes, May to September 2026 | SCION, 2026-10 | intro |
| almost 100 GB; over 25 GB; 25 million; over 600 PB | Main history; compressed working copy; CI checkouts per day; naive daily git traffic | SCION | §Growing our monorepo |
| 7 people, 5 months | Team and time to build and migrate | SCION | §What we learned |
| over 99%; 200x; two orders of magnitude; 25% | Cache hit rate; smaller footprint; faster checkouts; CI CPU saved | SCION | §Scaling Scion |
| 20x less memory, 4x faster | Model rewrite of the ingestion pipeline | SCION | §What we learned |
| 86% (92, 82, 81, 90) | Analysts' choices matching the agent's assigned lean, overall and per decision | JUDGE, 2026-10 | intro; §Results |
| 60% vs 6% | Switched from a stated preference when the agent disagreed vs agreed (38 cases; 95% interval 24 to 82 points) | JUDGE | §Results |
| 77%; 15% | Reused the agent's arguments; credited the agent | JUDGE | §Results |
| 54% vs 36%; 82% vs 61% | Recommended rollout by agent lean; recommendation predicted from leans vs base rate | JUDGE | §Results |
| 71 vs 73 | Confidence (0 to 100), full followers vs others | JUDGE | §Results |
| 6% (3 of 50) vs 55% (6 of 11); 65 vs 90 min | Serious errors and median time, with vs without the agent | JUDGE | §Results |
| 112 of 123 | Runs in which Opus 4.8, with no assigned lean, made the same five choices | JUDGE | intro |
| 61 recruited, 50 analysed | Study size | JUDGE | §Study design |
| 413 files in 225 folders, 1 badge vs 9 files in 2 folders plus `global.md`, 4 badges | Memory at about 10,000 steps, Sonnet 3.7 vs Fable 5, Pokémon Red | MEM, 2026-11 | §Claude has learned to judge salience |
| nearly doubled; 9 of 10 vs under half | Sonnet 4.6 score when told to read memory and test theories; unprompted memory reads, Sonnet 5 vs Sonnet 4.6 | MEM | §Steering Claude to write memory |
| 350,000 files, about 420M tokens; 25 questions; 128 sessions | Wiki experiment corpus and scale | MEM | §Dreaming can build new memory representations |
| 13% to 48% | Graded criteria met as dreaming scaled from 2 to 128 sessions | MEM | same |
| 54% to 61% vs 53%; 48% | Search plus wiki as the wiki grew vs search alone; wiki alone at best | MEM | same |
| about 20,000 tokens | Saved per question with search plus wiki | MEM | same |
| 87% vs 73% | Merger questions needing several documents, wiki vs search | MEM | same |
| 72% (41 of 57) to 100% | Brief criteria met before and after rewriting the wiki-building instructions | MEM | §Dreaming can focus memory on a specific goal |
| 200 lines or 25 KB | Portion of `MEMORY.md` loaded per session | MEM | §Dreaming can promote notes up the memory hierarchy |

### Contradictions and open questions

Newer posts revising older ones:

- BEA (2024-12) carries a header note: "Much of the tooling landscape described in this post has changed since December 2024." and points to MA (2026-04). Its principles (simplicity, tools, ground truth) are still cited by HARN2 and MA; its framework list is dated.
- THINK (2025-03) carries a header note that extended thinking has improved, "such that we recommend using that feature instead of a dedicated think tool in most cases".
- CCBP (2025-04) carries a header note: "This blog post is no longer maintained." Dated items in it: the thinking keywords (PM2 describes an effort setting with `/effort` and levels up to `xhigh`, and mentions ultrathink being brought back); `.claude/commands` and the `/project:` prefix (SKILLS, 2025-10, introduces skills); skip-permissions in a container as the only unattended mode (SBX 2025-10, AUTO 2026-03); manual multi-checkout parallelism (AUTON 2025-09 adds sub-agents, hooks, background tasks, checkpoints). Its advice to add emphasis words such as IMPORTANT to instruction files is not repeated in any later post in this batch; CTX (2025-09) and MEM (2026-11) favour explaining and heuristics. Inference: treat emphasis as a last resort and test it.
- HARN1 (2025-11) made context resets and an initializer central. HARN2 (2026-03) dropped resets with Opus 4.5 and sprints with Opus 4.6; MA (2026-04) calls the resets dead weight. What survives: structured hand-off artifacts, one feature at a time, browser-level verification, git discipline.
- CTX (2025-09) calls compaction the first lever. HARN1 says compaction is not sufficient; HARN2 says it became sufficient with Opus 4.5; MA warns it is irreversible.
- SBX (2025-10) says a successful injection is fully isolated by the sandbox. CONTAIN (2026-05) documents exfiltration through an allow-listed domain and credential theft through a pasted prompt.
- FRAME (2025-08) presents per-action approval as the control. AUTO, TRUST and CONTAIN (2026) report 93% approval and move oversight to plans, classifiers and containment.
- MARS (2025-06) says agents are not yet good at real-time coordination and most coding work does not parallelise. CC (2026-02) runs 16 coding agents with no orchestrator, coordinated through git and tests; SCION (2026-10) reports over 30,000 merges a day.

Disagreements between posts:

- LLM judge design. MARS: "a single LLM call with a single prompt outputting scores from 0.0-1.0 and a pass-fail grade was the most consistent" (MARS §Effective evaluation of agents). EVALS: "grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions" (EVALS §Step 5). Different tasks and dates; neither post addresses the other.
- Which model the HARN1 harness used. HARN1 itself names Opus 4.5 as the model that falls short without the harness; HARN2 says the earlier harness "used Sonnet 4.5". Unresolved in the texts.
- SWE-bench Verified starting point: EVALS says 40% to over 80% in a year in one place and that scores started at 30% this year in another.
- Auto mode versus sandbox. AUTO frames them as alternative answers to approval fatigue; CONTAIN's footnote (live page) says auto mode belongs inside a sandbox.
- Orchestrator or not. MARS and HARN2 use a lead or planner; CC deliberately uses none; LRC prefers one sequential agent for coupled work. The texts agree only that the choice depends on how independent the sub-tasks are.
- Fixed rules versus judgement. HARN1 uses rigid rules and strong wording for the feature list; MEM finds fixed memory rules hurt strong models; CTX warns against brittle logic. Inference: rigid rules fit integrity constraints (do not edit the test list), judgement fits content decisions (what to remember).
- Line-by-line review. SCION's engineers review intent only; CC and JUDGE give reasons to doubt that this is enough outside an organisation with Anthropic's test investment.

Open questions the sources leave:

- When an evaluator agent pays for itself. HARN2 says it depends on where the task sits relative to the model's solo ability, with no test for telling in advance.
- How often to consolidate memory and how to keep it correct at acceptable cost (MEM §Thinking backward, looking forward).
- How to measure deferral to an agent in normal work (JUDGE §What this means).
- How much resource and timing noise affects one's own small eval sets (NOISE covers benchmarks only).
- Auto mode's 17% miss rate rests on 52 cases; the post says the set will be expanded.
- None of the 28 posts evaluates harnesses other than Claude Code and the Agent SDK. Everything here about other harnesses is inference.

## Per source

All files are under `refs/articles/anthropic.com/`. Oldest first.

### Building effective AI agents (Anthropic, 2024-12-19)

File: [`refs/articles/anthropic.com/research-building-effective-agents/article.md`](https://www.anthropic.com/research/building-effective-agents)   URL: https://www.anthropic.com/research/building-effective-agents

Thesis: The teams that succeed with LLM agents use simple, composable patterns and not heavy frameworks. Workflows (fixed code paths) and agents (model-directed loops) are different things, and complexity should be added only when it demonstrably improves outcomes.

Practices:
- Five workflow patterns with when-to-use notes: prompt chaining with programmatic gates, routing, parallelisation (sectioning and voting), orchestrator-workers, evaluator-optimizer (§Building blocks, workflows, and agents).
- Evaluator-optimizer fits when a human's feedback demonstrably improves the output and an LLM can give such feedback (§Workflow: Evaluator-optimizer). This is the ancestor of HARN2's generator and evaluator.
- Agents are simple at the core: "They are typically just LLMs using tools based on environmental feedback in a loop." (§Agents). Get ground truth from the environment at each step, add stopping conditions such as a maximum iteration count, and test in sandboxes.
- Three principles: simplicity, transparency (show planning steps), and a carefully built agent-computer interface (§Summary).
- Tool design: give room to think before committing, keep formats close to naturally occurring text, avoid formatting overhead such as line counts or string escaping; write descriptions as for a junior developer, with examples and edge cases; poka-yoke arguments (§Appendix 2).
- If you use a framework, understand the code underneath; wrong assumptions about it are a common source of error (§When and how to use frameworks).

Evidence and numbers: none measured here; refers to the SWE-bench agent. "we actually spent more time optimizing our tools than the overall prompt" (§Appendix 2).

Tools and files named: Claude Agent SDK, Strands Agents SDK, Rivet, Vellum, Model Context Protocol, SWE-bench Verified.

Caveats: header note says the tooling landscape has changed since December 2024 and points to Managed Agents. Coding agents still need human review: "human review remains crucial for ensuring solutions align with broader system requirements" (§Appendix 1, B).

Relevance: high. The vocabulary and the simplicity rule that every later post reuses.

### Claude SWE-Bench performance (Anthropic, 2025-01-06)

File: [`refs/articles/anthropic.com/research-swe-bench-sonnet/article.md`](https://www.anthropic.com/research/swe-bench-sonnet)   URL: https://www.anthropic.com/research/swe-bench-sonnet

Thesis: A minimal scaffold (a prompt, a bash tool, an edit tool) reached 49% on SWE-bench Verified with the upgraded Claude 3.5 Sonnet; the effort went into tool descriptions and error-proofing.

Practices:
- Require absolute paths: "we simply made the tool always require an absolute path" (§Tool Using Agent).
- Edit by string replacement that must match exactly once, with an error message otherwise (§Tool Using Agent).
- Put detailed usage guidance in the tool description, not only the schema (§Tool Using Agent).
- Let the model reproduce the bug with its own script before fixing (§Examples of agent behavior).

Evidence and numbers: 49% vs 45% previous best; "many successful runs took hundreds of turns for the model to resolve, and >100k tokens" (§Challenges).

Tools and files named: Bash Tool, Edit Tool, SWE-Agent framework, SWE-bench Verified (500 problems).

Caveats: with hidden tests the model often believes it has succeeded when it has not, sometimes because it patched at the wrong level of abstraction (§Challenges). Grading was distorted by environment setup problems. The prompt and tool specs are missing from the saved copy.

Relevance: medium. Old model, but the path and edit-format lessons carry to project scripts.

### The "think" tool for complex tool use (Anthropic, 2025-03-20)

File: [`refs/articles/anthropic.com/research-claude-think-tool/article.md`](https://www.anthropic.com/research/claude-think-tool)   URL: https://www.anthropic.com/research/claude-think-tool

Thesis: A no-op tool that gives Claude a place to reason between tool calls improved policy-heavy, sequential tool use on tau-bench with Claude 3.7. Superseded: the header note now recommends extended thinking instead in most cases.

Evidence and numbers: airline pass^1 0.570 vs 0.370 with an optimised prompt; retail 0.812 vs 0.783; +1.6% on SWE-bench (§Performance on τ-Bench, §Performance on SWE-Bench). Long or complex guidance about the tool worked better in the system prompt than in the tool description (§2. Place complex guidance in the system prompt). No gain for single or parallel calls or simple instruction following.

Relevance: low. Historical; the surviving point is that worked examples of reasoning help most in policy-heavy domains.

### Claude Code Best Practices (Anthropic, 2025-04-18)

File: [`refs/articles/anthropic.com/research-claude-code-best-practices/article.md`](https://www.anthropic.com/research/claude-code-best-practices)   URL: https://www.anthropic.com/research/claude-code-best-practices

Thesis: Claude Code is deliberately low-level; this post lists patterns that worked inside and outside Anthropic. Header note: "This blog post is no longer maintained." and the current version lives in the docs.

Practices:
- `CLAUDE.md` content: common bash commands, core files and utilities, code style, testing instructions, repository etiquette, environment setup, unexpected behaviours (§1a). "We recommend keeping them concise and human-readable." (§1a). **[live page, not in saved file]** the example file is about ten lines under the headings Bash commands, Code style, Workflow.
- Locations: repo root (checked in) or `CLAUDE.local.md` (ignored), parent directories, child directories (loaded on demand), `~/.claude/CLAUDE.md` (§1a).
- Tune it like a prompt: "A common mistake is adding extensive content without iterating on its effectiveness." (§1b). Anthropic sometimes runs it through the prompt improver and adds emphasis words to improve adherence.
- Allowed tools: `/permissions`, `.claude/settings.json`, `--allowedTools`; examples `Edit`, `Bash(git commit:*)` (§1c).
- Install `gh`. Document custom shell tools with usage examples and `--help` (§1d, §2a). Check in `.mcp.json` (§2b).
- Explore, plan, code, commit; tell Claude not to code during exploration; use sub-agents early to verify details and preserve context; save the plan to a document or issue as a reset point (§3a).
- Tests first: write tests, confirm they fail, commit them, implement without modifying tests, optionally have independent sub-agents check for overfitting (§3b). "Claude performs best when it has a clear target to iterate against—a visual mock, a test case, or another kind of output." (§3b).
- Visual iteration with screenshots (§3c).
- Unattended runs: "use `--dangerously-skip-permissions` in a container without internet access" (§3d).
- Be specific. **[live page, not in saved file]** poor vs good examples, such as asking for a test for a named edge case and to avoid mocks, or to follow a named existing widget as the pattern (§4a).
- Course-correct with plans, Escape, double Escape, undo (§4e). "Use the `/clear` command frequently between tasks to reset the context window." (§4f).
- Checklists in a Markdown file or GitHub issue for long migrations and lint clean-ups (§4g).
- Headless mode `-p` with `--output-format stream-json` for CI, hooks and fan-out over a generated task list (§5, §6d).
- Separate writer and reviewer contexts: "This separation often yields better results than having a single Claude handle everything." (§6a). Multiple checkouts or `git worktree add` for independent tasks (§6b, §6c).

Evidence and numbers: anecdotal; 90%+ of git interactions through Claude for many engineers (§3f).

Tools and files named: `CLAUDE.md`, `CLAUDE.local.md`, `~/.claude/CLAUDE.md`, `.claude/settings.json`, `~/.claude.json`, `.mcp.json`, `.claude/commands/`, `$ARGUMENTS`, `/init`, `/permissions`, `/clear`, `--allowedTools`, `--mcp-debug`, `--dangerously-skip-permissions`, `-p`, `--verbose`, `gh`, Puppeteer MCP, git worktrees.

Caveats: superseded in detail by later posts (thinking keywords, slash-command paths, safe YOLO mode); see Contradictions. The `/engineering/` URL now redirects to the docs page, which is a different text.

Relevance: high for the workflow patterns, which later posts keep; low for exact commands.

### How we built our multi-agent research system (Anthropic, 2025-06-13)

File: [`refs/articles/anthropic.com/research-multi-agent-research-system/article.md`](https://www.anthropic.com/research/multi-agent-research-system)   URL: https://www.anthropic.com/research/multi-agent-research-system

Thesis: An orchestrator with parallel sub-agents beats a single agent on breadth-first research, mainly because it spends more tokens across separate context windows. The cost is high and the prototype-to-production gap is wide.

Practices:
- Delegation brief: "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." (§Prompt engineering and evaluations for research agents, item 2).
- Put effort-scaling rules in the prompt, since agents judge effort poorly (item 3).
- Tool heuristics: look at all available tools first, match tool to intent, prefer specialised tools (item 4).
- Let the model improve prompts and tool descriptions from observed failures (item 5).
- Search broad first, then narrow (item 6). Use thinking as a planning scratchpad (item 7). Call tools in parallel (item 8).
- Watch the agent step by step with the real prompts and tools to build a mental model (item 1).
- Evaluate from day one with a small set; one LLM judge call with a rubric; keep human testing (§Effective evaluation of agents).
- Judge end state, not each turn, for agents that change state (§Appendix).
- Resume from checkpoints, tell the agent when a tool is failing, combine with deterministic retries (§Production reliability and engineering challenges).
- Sub-agents write outputs to files and return references: "Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator." (§Appendix).

Evidence and numbers: +90.2% on an internal eval; "token usage by itself explains 80% of the variance" on BrowseComp (§Benefits of a multi-agent system); "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats" (same); 40% faster task completion after tool description rewrite; up to 90% less research time with parallel calls.

Tools and files named: Console simulations, MCP servers, extended and interleaved thinking, rainbow deployments.

Caveats: "most coding tasks involve fewer truly parallelizable tasks than research" (§Benefits). Sub-agents ran synchronously, so the lead could not steer them. Small changes to the lead prompt changed sub-agent behaviour unpredictably. Human testers found a bias toward SEO content farms that evals missed.

Relevance: high for delegation briefs and the cost model of sub-agents.

### Our framework for safe and trustworthy agents (Anthropic, 2025-08-04)

File: [`refs/articles/anthropic.com/news-our-framework-for-developing-safe-and-trustworthy-agents/article.md`](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents)   URL: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents

Thesis: Five principles for agents: human control, transparency, alignment with human values and expectations, privacy across interactions, and secure interactions. Updated by TRUST (2026-04).

Practices: Claude Code is read-only by default, "It has read-only permissions by default" (§Keeping humans in control while enabling agent autonomy), and shows a to-do checklist. The over-reach example is an agent asked to organise files that deletes and restructures (§Aligning agents with human values and expectations).

Relevance: low. Policy framing; the concrete mechanisms are in AUTO, TRUST and CONTAIN.

### Writing effective tools for AI agents (Anthropic, 2025-09-11)

File: [`refs/articles/anthropic.com/research-writing-tools-for-agents/article.md`](https://www.anthropic.com/research/writing-tools-for-agents)   URL: https://www.anthropic.com/research/writing-tools-for-agents

Thesis: Tools are contracts between deterministic systems and non-deterministic agents, so they should be designed for agents and improved through an eval loop, with the agent helping to analyse transcripts and refactor.

Practices:
- Prototype, connect locally (`claude mcp add <name> <command> [args...]`), try it yourself (§Building a prototype). Give Claude the library docs, for example `llms.txt` files.
- Evaluation tasks should be realistic and need several calls; avoid toy sandboxes; pair each with a verifiable outcome; do not over-specify the expected path (§Generating evaluation tasks).
- Run with plain while-loops over the API; ask for reasoning and feedback before tool calls; collect runtime, call counts, tokens and errors (§Running the evaluation).
- Paste transcripts into Claude Code to refactor tools; keep a held-out test set (§Collaborating with agents).
- Principles: few high-impact tools, namespacing, meaningful context, token-efficient responses, engineered descriptions (§Principles for writing effective tools); details in section (d) above.

Evidence and numbers: 25,000-token default response cap in Claude Code; 206 vs 72 tokens for detailed vs concise; appending the year to web search queries degraded results until the description was fixed (§Analyzing results).

Tools and files named: MCP, Desktop extensions (DXT), `response_format` enum, `search_contacts`, `schedule_event`, `search_logs`, `get_customer_context`, tool annotations.

Caveats: response format (XML, JSON, Markdown) and prefix vs suffix naming had model-dependent effects with no universal answer. The example responses and error messages are missing from the saved copy.

Relevance: high. Directly applicable to MCP servers and, by inference, to project scripts.

### A postmortem of three recent issues (Anthropic, 2025-09-17)

File: [`refs/articles/anthropic.com/research-a-postmortem-of-three-recent-issues/article.md`](https://www.anthropic.com/research/a-postmortem-of-three-recent-issues)   URL: https://www.anthropic.com/research/a-postmortem-of-three-recent-issues

Thesis: Three overlapping infrastructure bugs degraded responses between August and early September 2025; none was deliberate throttling, and Anthropic's evals failed to catch them.

Practices and evidence: see section (j). Routing misdirected up to 16% of Sonnet 4 requests at the worst hour; sticky routing concentrated the damage. Fixes: corrected routing, rollbacks, exact top-k. Changes: more sensitive evals, evals on production systems, faster debugging tools. Users are asked to report through `/bug` or thumbs down.

Caveats: privacy controls limited engineers' access to failing interactions, which slowed diagnosis.

Relevance: low to medium. Useful mainly as a reminder that quality shifts can be platform-side and that reports with specifics get fixes.

### Enabling Claude Code to work more autonomously (Anthropic, 2025-09-29)

File: [`refs/articles/anthropic.com/news-enabling-claude-code-to-work-more-autonomously/article.md`](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)   URL: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously

Thesis: Product announcement: VS Code extension, terminal 2.0, checkpoints, and the renamed Claude Agent SDK with sub-agents and hooks.

Practices: checkpoints save code state before each change; rewind with Esc twice or `/rewind`, restoring code, conversation or both. Limit: "Checkpoints apply to Claude’s edits and not user edits or bash commands, and we recommend using them in combination with version control." (§Checkpoints). Hooks run actions at set points (tests after changes, lint before commits); background tasks keep dev servers alive (§Subagents, hooks, and background tasks).

Relevance: low. Feature list; the checkpoint limit is the one durable fact.

### Effective context engineering for AI agents (Anthropic, 2025-09-29)

File: [`refs/articles/anthropic.com/research-effective-context-engineering-for-ai-agents/article.md`](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)   URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

Thesis: The job has moved from wording prompts to curating everything in the window. Context has diminishing returns, so aim for the smallest high-signal set and use retrieval, compaction, notes and sub-agents to manage long tasks.

Practices: see section (c). Key points: right altitude for system prompts; minimal non-overlapping tools; canonical examples over rule lists; just-in-time retrieval through identifiers; hybrid of up-front `CLAUDE.md` plus `glob` and `grep`; compaction tuned for recall then precision; tool-result clearing; `NOTES.md`-style notes; sub-agents returning 1,000 to 2,000 token summaries.

Evidence and numbers: mostly qualitative; cites context rot research; Pokémon agent keeps tallies over thousands of steps from its own notes (§Structured note-taking).

Tools and files named: `CLAUDE.md`, `NOTES.md`, `glob`, `grep`, `head`, `tail`, memory tool, context editing (tool result clearing).

Caveats: run-time exploration is slower than pre-computed retrieval; over-aggressive compaction loses details whose importance shows later. The post expects prescriptive engineering to matter less as models improve.

Relevance: high. The conceptual base for instruction files, skills and sub-agent design.

### Equipping agents with Agent Skills (Anthropic, 2025-10-16)

File: [`refs/articles/anthropic.com/research-equipping-agents-for-the-real-world-with-agent-skills/article.md`](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills)   URL: https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills

Thesis: A skill is a folder with a `SKILL.md` plus optional files and scripts, loaded by progressive disclosure, so procedural knowledge can be packaged without filling the context window.

Practices:
- Three levels: "At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt." (§The anatomy of a skill); the body loads when relevant; linked files (the PDF skill's `reference.md`, `forms.md`) load only when needed.
- Because of this, "the amount of context that can be bundled into a skill is effectively unbounded" (same section).
- Bundle scripts for deterministic work; they run without entering context (§Skills and code execution).
- Start from observed gaps on representative tasks, then write the skill (§Developing and evaluating skills).
- Split `SKILL.md` when it grows; keep mutually exclusive paths in separate files; "It should be clear whether Claude should run scripts directly or read them into context as reference." (same section).
- Watch real use, and tune `name` and `description`, since they decide triggering.
- Have Claude write its successful approaches and mistakes into the skill, and reflect when it goes wrong.

Evidence and numbers: none measured.

Tools and files named: `SKILL.md` with YAML frontmatter (`name`, `description`), `reference.md`, `forms.md`, the PDF skill.

Caveats: "We recommend installing skills only from trusted sources." (§Security considerations); audit bundled code, dependencies and any instruction to contact external network sources.

Relevance: high. Defines the skill format the setup will use.

### Making Claude Code safer with sandboxing (Anthropic, 2025-10-20)

File: [`refs/articles/anthropic.com/research-claude-code-sandboxing/article.md`](https://www.anthropic.com/research/claude-code-sandboxing)   URL: https://www.anthropic.com/research/claude-code-sandboxing

Thesis: OS-level filesystem and network isolation lets Claude run with far fewer prompts while limiting what a prompt-injected session can do. Two products: the sandboxed bash tool and Claude Code on the web.

Practices:
- Both boundaries are needed; without network isolation files can be exfiltrated, without filesystem isolation the sandbox can be escaped (§Sandboxing: a safer and more autonomous approach).
- Sandboxed bash: read and write in the working directory, no modification outside it; network only through a unix socket to a proxy that enforces a domain allowlist and asks about new domains; applies to spawned subprocesses; configurable paths and domains; enabled with `/sandbox` (§Sandboxed bash tool).
- Claude Code on the web: credentials stay outside the sandbox; a git proxy checks a scoped credential and the push target before attaching the real token (§Claude Code on the web).

Evidence and numbers: "we've found that sandboxing safely reduces permission prompts by 84%" (intro).

Tools and files named: Linux bubblewrap, macOS seatbelt, `/sandbox`, `anthropic-experimental/sandbox-runtime` (open source).

Caveats: beta research preview at the time. CONTAIN (2026-05) shows data leaving through an allow-listed domain despite a working sandbox, and AUTO (2026-03) calls sandboxing high-maintenance.

Relevance: high. The base containment layer on Linux.

### Code execution with MCP for efficient agents (Anthropic, 2025-11-04)

File: [`refs/articles/anthropic.com/research-code-execution-with-mcp/article.md`](https://www.anthropic.com/research/code-execution-with-mcp)   URL: https://www.anthropic.com/research/code-execution-with-mcp

Thesis: Loading every MCP tool definition and passing every intermediate result through the model wastes tokens. Presenting servers as code APIs on a filesystem lets the agent load what it needs and process data in code.

Practices:
- Generate a file tree such as `./servers/<server>/<tool>.ts`; the agent lists and reads only the needed files. "Models are great at navigating filesystems." (§Progressive disclosure). Or add a `search_tools` tool with a detail-level parameter.
- Filter, join and aggregate in the execution environment and return only the result (§Context efficient tool results).
- Loops and conditionals in code instead of repeated tool calls (§More powerful and context-efficient control flow).
- Intermediate data stays out of the model's context; the harness can tokenise personal data (§Privacy-preserving operations).
- Save working code as reusable functions and add a `SKILL.md` (§State persistence and skills).

Evidence and numbers: "This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%" (§Code execution with MCP improves context efficiency), an illustrative scenario.

Caveats: running agent-written code needs sandboxing, resource limits and monitoring. All code samples are missing from the saved copy.

Relevance: medium. Supports keeping MCP use small and preferring scripts; the build-out is for agent builders.

### Introducing advanced tool use for Claude (Anthropic, 2025-11-24)

File: [`refs/articles/anthropic.com/research-advanced-tool-use/article.md`](https://www.anthropic.com/research/advanced-tool-use)   URL: https://www.anthropic.com/research/advanced-tool-use

Thesis: Three API beta features address tool-scale problems: Tool Search Tool (deferred loading), Programmatic Tool Calling (orchestration in code) and Tool Use Examples.

Practices:
- Mark rarely used tools `defer_loading: true`; "Keep your three to five most-used tools always loaded, defer the rest." (§Best practices). Use when definitions exceed about 10K tokens or there are 10 or more tools.
- "The most common failures are wrong tool selection and incorrect parameters" (§Tool Search Tool, The challenge), especially with similar names.
- Programmatic calling for large data, three or more dependent calls, and parallel operations; document return formats; opt in idempotent tools via `allowed_callers`.
- Examples: realistic values, minimal to full variants, one to five per tool, only where the schema leaves ambiguity.

Evidence and numbers: about 77K to 8.7K tokens; Opus 4 49% to 74% and Opus 4.5 79.5% to 88.1% on MCP evals; 37% fewer tokens with programmatic calling; "tool use examples improved accuracy from 72% to 90% on complex parameter handling" (§Tool Use Examples). Full list in section (k).

Tools and files named: `defer_loading`, `allowed_callers`, `code_execution`, regex and BM25 search tools.

Caveats: each feature adds a step or tokens; the post lists when they are not worth it. Code samples missing from the saved copy.

Relevance: medium. The token figures justify trimming MCP servers; the features themselves are API-level.

### Effective harnesses for long-running agents (Anthropic, 2025-11-26)

File: [`refs/articles/anthropic.com/research-effective-harnesses-for-long-running-agents/article.md`](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)   URL: https://www.anthropic.com/research/effective-harnesses-for-long-running-agents

Thesis: Agents working across many context windows need more than compaction. An initializer session that creates a feature list, progress file and init script, followed by coding sessions that each finish one feature and leave a clean, committed state, lets work continue across resets.

Practices: see section (a) for the full procedure: feature list in JSON with only the `passes` field editable; one feature at a time; descriptive commits and a progress file; browser-level end-to-end testing; a fixed start-of-session routine.

Evidence and numbers: over 200 features in the claude.ai clone list. No cost or duration figures.

Tools and files named: `init.sh`, `claude-progress.txt`, `feature_list.json` (file name from the live page), Puppeteer MCP, Claude Agent SDK, the `autonomous-coding` quickstart.

Caveats: tuned for full-stack web apps; vision and browser-tool limits leave some bugs unseen; the single-agent versus multi-agent question was left open. Partly superseded by HARN2 and MA.

Relevance: high. The artifacts carry over even where resets are no longer needed.

### Demystifying evals for AI agents (Anthropic, 2026-01-09)

File: [`refs/articles/anthropic.com/research-demystifying-evals-for-ai-agents/article.md`](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)   URL: https://www.anthropic.com/research/demystifying-evals-for-ai-agents

Thesis: Evals turn a vague sense that the agent got worse into something actionable. Start early with a small set from real failures, combine code, model and human graders, grade outcomes, and keep reading transcripts.

Practices: see section (f). Vocabulary: task, trial, grader, transcript, outcome, evaluation harness, agent harness, suite (§The structure of an evaluation). Eight-step roadmap from §Step 0 to §Step 8. Eval-driven development: write capability evals before the agent can pass them (§Step 8).

Evidence and numbers: "20-50 simple tasks drawn from real failures is a great start" (§Step 0); CORE-Bench 42% to 95% after fixes; Claude Code's own evals began with concision and file edits, then over-engineering (§Why build evaluations?).

Tools and files named: SWE-bench Verified, Terminal-Bench, tau-bench and tau2-bench, BrowseComp, WebArena, OSWorld, Harbor, Braintrust, LangSmith, Langfuse, Arize Phoenix.

Caveats: path-checking graders are brittle; LLM judges need human calibration; saturated evals hide progress; frameworks are only as good as the tasks. Grader tables and YAML examples are missing from the saved copy.

Relevance: high for method, medium for scale: written for product teams, so the solo mapping is inference.

### Building a C compiler with parallel Claudes (Anthropic, author not named in the saved copy, 2026-02-05)

File: [`refs/articles/anthropic.com/research-building-c-compiler/article.md`](https://www.anthropic.com/research/building-c-compiler)   URL: https://www.anthropic.com/research/building-c-compiler

Thesis: Sixteen Claude instances in a bare loop, coordinated only by git and tests, built a 100,000-line C compiler that compiles Linux. Most of the work was designing tests and feedback so that agents could orient themselves; the approach has a visible ceiling.

Practices: see section (b): lock files in `current_tasks/`, near-perfect verifiers, terse greppable output, `--fast` sampled test runs, READMEs and progress files, an oracle to split a monolithic task, specialised roles.

Evidence and numbers: nearly 2,000 sessions, two weeks, just under $20,000, 2 billion input and 140 million output tokens, 99% on most compiler suites (§Evaluation).

Tools and files named: Docker containers, `/upstream`, `/workspace`, `current_tasks/`, `AGENT_PROMPT.md` (live page), GCC as oracle, GCC torture tests.

Caveats: an early research prototype; no inter-agent communication or goal management; regressions grew as the codebase grew; the author states unease about unverified autonomous output. The loop script is missing from the saved copy.

Relevance: high. The clearest evidence on test design for unattended and parallel agents.

### Infrastructure noise in agentic coding evals (Anthropic, 2026-02-05)

File: [`refs/articles/anthropic.com/research-infrastructure-noise/article.md`](https://www.anthropic.com/research/infrastructure-noise)   URL: https://www.anthropic.com/research/infrastructure-noise

Thesis: Resource limits and their enforcement change agentic benchmark scores by more than typical leaderboard gaps, so small differences between models or harnesses are not reliable.

Practices: specify both a guaranteed allocation and a kill threshold per task; calibrate the band so floor and ceiling scores fall within noise; report the configuration; run at several times and days (§What we recommend). "Two agents with different resource budgets and time limits aren't taking the same test." (intro).

Evidence and numbers: 6-point spread on Terminal-Bench 2.0; infra errors 5.8% to 0.5%; 1.54 points on SWE-bench at 5x RAM; pass rates also vary with time of day (anecdotal).

Relevance: medium. Guards against over-reading leaderboards when picking models or harnesses, and against memory-starved local eval runs.

### Long-running Claude for scientific computing (Siddharth Mishra-Sharma, Anthropic, 2026-03-23)

File: [`refs/articles/anthropic.com/research-long-running-claude/article.md`](https://www.anthropic.com/research/long-running-claude)   URL: https://www.anthropic.com/research/long-running-claude

Thesis: A non-expert can run a multi-day autonomous build of a numerical solver with four things: a plan in `CLAUDE.md`, a progress file, a test oracle and a simple loop.

Practices:
- Spend most of the human time on the instructions and plan, iterated with Claude; the agent may update `CLAUDE.md` as it learns (§Draft a plan and iterate locally).
- `CHANGELOG.md` as long-term memory with status, completed tasks, failed approaches and reasons, accuracy tables, known limits. "The failed approaches are important—without them, successive sessions will re-attempt the same dead ends." (§Memory across sessions).
- An oracle is required: "long-running autonomous scientific work today crucially depends on the agent having a way to know whether it’s making progress" (§The test oracle). Tell the agent to grow the test suite.
- Git rules in `CLAUDE.md`: "Commit and push after every meaningful unit of work." and "Never commit code that breaks existing passing tests." (§Git as coordination).
- Run inside `tmux`, check progress from the commit log, re-prompt when needed; Ralph loop against early stopping (§The execution loop).

Evidence and numbers: sub-percent agreement with the reference in a few days; target 0.1%.

Tools and files named: `CLAUDE.md`, `CHANGELOG.md`, `pytest tests/ -x -q`, tmux, SLURM, Ralph loop plugin, `/loop`, GSD.

Caveats: test coverage had gaps: "for a while it was only testing the code at a single (fiducial) parameter point" (§The result); elementary domain mistakes; result is not production-grade. Coupled work suits one sequential agent, unlike CC.

Relevance: high. The smallest complete recipe for a long unattended task.

### Harness design for long-running apps (Anthropic, author not named in the saved copy, 2026-03-24)

File: [`refs/articles/anthropic.com/research-harness-design-long-running-apps/article.md`](https://www.anthropic.com/research/harness-design-long-running-apps)   URL: https://www.anthropic.com/research/harness-design-long-running-apps

Thesis: Separating generation from evaluation, with explicit grading criteria, lifts both subjective design quality and functional correctness. Each harness part should be re-tested against new models, and several parts became unnecessary within months.

Practices: see section (a): planner, generator and evaluator roles; sprint contracts; file-based communication; evaluator driven through Playwright with hard thresholds; evaluator prompt tuned from logs; removal of resets and sprints.

Evidence and numbers: solo 20 min and $9 vs harness 6 hr and $200 (live page); DAW run 3 hr 50 min and $124.70 (live page; about 4 hours and $124 in the saved text); 5 to 15 design iterations, up to four hours.

Tools and files named: Claude Agent SDK, Playwright MCP, frontend-design skill (`plugins/frontend-design/skills/frontend-design/SKILL.md`), React, Vite, FastAPI, SQLite, PostgreSQL.

Caveats: one author's experiments on a handful of prompts, no controlled metric; evaluator still missed nested bugs and small layout issues; the one direct comparison cost over 20x a solo run; Claude cannot hear, so QA on the audio app was limited. Cost tables, the evaluator findings table and the example plan are missing from the saved copy.

Relevance: high. The best account of when a separate evaluator is worth it and of pruning scaffolding.

### How we built Claude Code auto mode (Anthropic, 2026-03-25)

File: [`refs/articles/anthropic.com/research-claude-code-auto-mode/article.md`](https://www.anthropic.com/research/claude-code-auto-mode)   URL: https://www.anthropic.com/research/claude-code-auto-mode

Thesis: Auto mode replaces per-action approval with a prompt-injection probe on inputs and a two-stage transcript classifier on actions, aimed at overeager behaviour and honest mistakes. It is safer than skipping permissions and weaker than careful manual review.

Practices: see section (g): three permission tiers; broad interpreter rules dropped on entry; classifier blind to assistant text and tool results; conservative reading of user intent; environment, block and allow slots; deny and continue with 3 and 20 denial limits; checks at both ends of sub-agent hand-offs.

Evidence and numbers: 0.4% false positives; 17% false negatives on 52 real overeager actions; 8.5% stage 1 false positives; 93% of manual prompts accepted. Including assistant messages and tool results made the classifier worse on the overeagerness set (§Why we strip assistant text and tool results).

Tools and files named: `claude auto-mode defaults`, `--dangerously-skip-permissions`, `claude -p`, Sonnet 4.6 as classifier.

Caveats: most misses come from finding approval-shaped evidence that does not cover the action's blast radius; prompt changes to fix this cost more than they gained. Not for high-stakes infrastructure. The results table is missing from the saved copy.

Relevance: high. Defines how unattended Claude Code runs are gated and how to phrase requests so intent is unambiguous.

### Scaling Managed Agents with stable interfaces (Anthropic, 2026-04-08)

File: [`refs/articles/anthropic.com/research-managed-agents/article.md`](https://www.anthropic.com/research/managed-agents)   URL: https://www.anthropic.com/research/managed-agents

Thesis: Because harness assumptions go stale, Managed Agents fixes only three interfaces (session log, harness, sandbox) and lets implementations change. Decoupling them improved reliability, security and latency.

Practices:
- "harnesses encode assumptions about what Claude can’t do on its own" (intro), so question them often.
- Keep the durable event log outside both the harness and the context window; a crashed harness resumes from it (§Decouple the brain from the hands).
- Security by structure: "make sure the tokens are never reachable from the sandbox where Claude’s generated code runs" (§The security boundary). Git tokens are wired into the remote at sandbox setup; MCP credentials sit in a vault behind a proxy.
- Treat the sandbox as a tool call and provision it only when needed.

Evidence and numbers: "our p50 TTFT dropped roughly 60% and p95 dropped over 90%" (§Many brains, many hands).

Tools and files named: `execute(name, input)`, `provision`, `wake(sessionId)`, `getSession`, `emitEvent`, `getEvents()`.

Caveats: hosted service design; narrow token scoping is called an assumption about what the model cannot do with a limited token.

Relevance: medium. The credential pattern and the log-outside-context idea transfer; the service itself is for agent builders.

### Trustworthy agents in practice (Anthropic, 2026-04-09)

File: [`refs/articles/anthropic.com/research-trustworthy-agents/article.md`](https://www.anthropic.com/research/trustworthy-agents)   URL: https://www.anthropic.com/research/trustworthy-agents

Thesis: An agent is model, harness, tools and environment, and each is both a capability and a point of oversight. The post shows how the 2025 framework became product decisions and what the wider ecosystem should build.

Practices: see section (h): per-action permissions give way to Plan Mode for multi-step work; training rewards pausing on ambiguity; injection defence is layered and still not a guarantee, so users must choose tools, data, permissions and environments with care.

Evidence and numbers: "On complex tasks, users interrupt Claude only slightly more frequently than on simple ones, but Claude's own rate of checking in roughly doubles." (§Helping agents understand their goals).

Tools and files named: Plan Mode, Claude Cowork, agent teams docs, MCP.

Caveats: deciding when to ask is described as one of the harder unsolved problems; no standard benchmark exists for injection resistance or for surfacing uncertainty.

Relevance: medium. States the intended ask-versus-act behaviour that instructions should align with.

### An update on Claude Code quality reports (Anthropic, 2026-04-23)

File: [`refs/articles/anthropic.com/research-april-23-postmortem/article.md`](https://www.anthropic.com/research/april-23-postmortem)   URL: https://www.anthropic.com/research/april-23-postmortem

Thesis: Three changes in the product layer, not the model or API, made Claude Code worse for some users in March and April 2026: a lower default effort, a bug that dropped prior reasoning, and a verbosity instruction.

Practices: see section (j). The exact instruction that hurt: "Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail." (§A system prompt change to reduce verbosity).

Evidence and numbers: "One of these evaluations showed a 3% drop for both Opus 4.6 and 4.7." (same section); fixed versions v2.1.101 and v2.1.116; usage limits reset for subscribers on April 23.

Tools and files named: `/effort`, `/feedback`, `clear_thinking_20251015` with `keep:1`, Code Review, effort levels `medium`, `high`, `xhigh`.

Caveats: internal evals and dogfooding missed all three at first; two unrelated internal experiments masked the caching bug.

Relevance: high. Direct evidence that small instruction and setting changes degrade coding quality, and how the vendor now tests them.

### How we contain Claude across products (Anthropic, 2026-05-25)

File: [`refs/articles/anthropic.com/research-how-we-contain-claude/article.md`](https://www.anthropic.com/research/how-we-contain-claude)   URL: https://www.anthropic.com/research/how-we-contain-claude

Thesis: Supervision by approval is fallible and model-level defences are probabilistic, so the blast radius must be capped by containment at the environment layer. The post gives three isolation patterns and the incidents that broke assumptions.

Practices:
- Three patterns: ephemeral gVisor container (claude.ai), human-in-the-loop OS sandbox (Claude Code), local VM with mounted workspace and credentials left in the host keychain (Cowork).
- Order of work: "The deterministic boundary is what gets hit when everything probabilistic misses." (§Summary).
- Match isolation to the user's ability to judge what the agent is about to do (§Summary).
- Treat project open, config load and localhost listeners as untrusted inbound requests (§Risk we missed: Everything before the trust dialog).
- An allowlist entry grants every function behind that domain (§Risk we missed: Exfiltration through an approved domain).
- Resolve symlinks before validating paths: "symlink resolution has to happen *before* path validation, not after" (§Pattern 3).
- Remote tools can change after approval: "Run it against fake data first" (§Trusting what the agent reads). Inspect tool output before it enters context, with a small fast classifier.
- Read-only access can be deployed more widely than write access (§Three types of risk).
- Prefer mature primitives: "Be wary of custom components." (§Summary).

Evidence and numbers: 93% approvals; 84% fewer prompts with the sandbox; auto mode catches roughly 83% of overeager actions; Opus 4.7 at about 0.1% and 5 to 6% injection success; "Across 25 retries of that prompt, Claude completed the exfiltration 24 times." (§Risk we missed: The user as an injection vector); "experienced users auto-approve roughly twice as often as new users, but they also interrupt the agent mid-execution more frequently" (§Pattern 2).

Tools and files named: gVisor, seccomp, Seatbelt, bubblewrap, `sandbox-runtime`, reference devcontainer, `.claude/settings.json` hooks, `~/.aws/credentials`, Files API, OTLP exports, mount modes read-only, read-write, read-write-no-delete.

Caveats: forward risks without solutions yet: persistent memory poisoning, trust escalation through sub-agent output, agent identity. VM isolation also hides activity from endpoint detection tools. The comparison table and footnote are missing from the saved copy.

Relevance: high. The threat model and the incident record behind any containment choice.

### Redesigning source control at Anthropic (Anthropic, 2026-10-13)

File: [`refs/articles/anthropic.com/research-redesigning-source-control/article.md`](https://www.anthropic.com/research/redesigning-source-control)   URL: https://www.anthropic.com/research/redesigning-source-control

Thesis: At over 30,000 merges a day, git's offline-first design became the bottleneck, so Anthropic built Scion, a server-centric version control system, in five months with seven people. It is a case study, not a product.

Practices: see section (i). "In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day." (intro). Not for general use: "Scion is by no means a suitable replacement for git for general use." (§Contributing to the wider ecosystem).

Evidence and numbers: 200x smaller footprint, over 99% cache hits, 25% CI CPU saved, 20x less memory and 4x faster ingestion after a model rewrite.

Tools and files named: Scion, `scn`, `scion-daemon`, `scion-cache`, `scion-server`, Antique, Spanner, Claude Mythos Preview, Claude Tag, Piper, Sapling.

Caveats: unusual workload and token budget; adversarial review described as effective but myopic; agents brute-forced around constraints during the migration. Footnotes are missing from the saved copy.

Relevance: low to medium. Nothing to install; the review and constraint lessons transfer.

### How AI agents shape experts' judgment calls (Amaç Herdağdelen, Hailey Joren, Alex Tamkin, Anthropic, 2026-10-27)

File: [`refs/articles/anthropic.com/research-agents-judgment-calls/article.md`](https://www.anthropic.com/research/agents-judgment-calls)   URL: https://www.anthropic.com/research/agents-judgment-calls

Thesis: In a randomised study, professional analysts followed their agent's secretly assigned preference on open analytical choices 86% of the time, explained the choices in the agent's words, and still felt the work was their own. A human in the loop is an independent check only if the judgement is really theirs.

Practices: see section (h). The stake for review: "a human reviewer is only an independent check if their judgment is their own" (intro). Design ideas offered: argue each option, or ask for the user's view first, only on the decisions that matter. The trade-off named: "a mealy-mouthed model will just irritate the people who try to use it" (§What this means).

Evidence and numbers: 86% following; 60% vs 6% switching; 77% reuse and 15% credit; 6% vs 55% serious errors with and without the agent; 112 of 123 identical default choices. Full list in section (k).

Tools and files named: Claude Code in web VS Code, Claude Opus 4.8 at high effort.

Caveats: leans were deliberately strengthened; one hour-long task in one unfamiliar field with one model; the no-agent comparison group was small and less experienced.

Relevance: medium to high. Shapes how the setup should handle architecture and design decisions and what review can be trusted for.

### The components of agent memory (Anthropic, 2026-11-06)

File: [`refs/articles/anthropic.com/research-components-of-agent-memory/article.md`](https://www.anthropic.com/research/components-of-agent-memory)   URL: https://www.anthropic.com/research/components-of-agent-memory

Thesis: Agent memory works as a division of labour: quick notes written in-session on a prediction of future need, and offline consolidation (dreaming) that checks notes against transcripts, builds navigable representations and keeps the always-loaded layer small. Newer models judge what to remember far better, and prescriptive rules can hurt them.

Practices: see section (e). Guidance style: "it helps to tell Claude what memory is for, but not *how* to use it" (§Steering Claude to write memory). Load limit: "It loads only the first 200 lines or 25 KB of `MEMORY.md`." (§Dreaming can promote notes up the memory hierarchy). Size discipline: "So the top layer of the memory hierarchy has to stay relatively small" (same section).

Evidence and numbers: 413 files and 1 badge vs 9 files and 4 badges; wiki scores 13% to 48% over 128 sessions; search plus wiki 61% vs 53%; 72% to 100% after instruction rewrite. Full list in section (k).

Tools and files named: `MEMORY.md`, `global.md`, memory directory in Managed Agents, memory tool, dreaming, knowledge-wiki quickstart, CL-Bench 1.0, Harvey LAB; models Sonnet 3.7, Sonnet 4.6, Opus 4.7, Sonnet 5, Opus 5, Opus 5.5, Sonnet 5.5, Fable 5.

Caveats: dreaming costs compute and its output is not available at once; wikis can bloat and carry errors; in-session note-taking distracts from the task; the right cadence is an open question. Figures are missing from the saved copy, so per-model benchmark values are not available.

Relevance: high. The most recent statement on what project memory should hold and how to instruct it.

