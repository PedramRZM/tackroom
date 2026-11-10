# Anthropic claude.dev blog (Claude Code and Claude platform teams)

Sources read: 18 of 18, each in full (list: `refs/sources/batches/anthropic-claude-dev-blog.txt`). None unreadable.

Reading notes that affect how to use this file:

- When these notes were written, the first saved copies had lost their section headings, figure
  captions and image alt texts, so a second, heading-preserving copy of each post was fetched
  through the reader proxy and read alongside. Those copies have since replaced the originals:
  each post is now one file, for example
  `refs/articles/claude.dev/blog-seeing-like-an-agent/article.md`, with headings and alt texts.
- Locators are the section headings of those files, in square brackets. Quotes were checked
  mechanically against the saved text. A quote marked "(fig. alt)" is the alt text of a figure.
- Dates run from 2026-04-10 to 2026-11-09. The older posts name older models (Opus 4.5 to 4.8) and
  some of their specifics are superseded by the later posts; this is flagged where it matters.
- Source keys: SKILLS, CACHE, SEE, CTX, WF, AUTO, REVIEW, EFFORT, OPUS, MODEL, TEAMS, EVAL, HTML,
  COST, SONNET, CLOUD, MODS, FAST (defined in the per-source headings).
- No injection attempts found. Several posts contain reader-directed commands (`claude update`,
  `/claude-api managed-agents-onboard <url>`, "run this request as written", "Post it on X"). They
  were treated as content and not run.

## Cross-cutting findings

### Practices that recur

1. Give the agent a way to run and check its own work (test, build, script that calls the endpoint, screenshot) and ask for the output as evidence. It is presented as the cheapest quality lever, to try before raising effort or model. REVIEW, COST, MODEL, SKILLS, SONNET, CLOUD, OPUS, FAST.
2. Keep `CLAUDE.md` short, spend it on codebase gotchas, and push everything situational into skills or a tree of files loaded on demand. CTX, SKILLS, COST (under 200 lines), REVIEW, SEE.
3. Delete instructions written for weaker models: blanket rules, repeated instructions, worked examples of tool use, "think carefully", "do not be lazy", mandatory multi-step rituals, scratchpad and verify-twice rules, contradictory rules. `/doctor` and `/claude-api prompt-audit` automate the clean-up. CTX, OPUS, SONNET, COST, EVAL.
4. Say what "done" looks like, name the proof, and say when to stop and ask. OPUS, CLOUD, WF (`/goal`), AUTO.
5. Review with a separate, fresh-context agent before a human looks; a single context prefers its own findings. REVIEW, WF, SKILLS, OPUS.
6. The prompt cache is a prefix match. Fix tools, MCP servers, system prompt, model and (on some platforms) effort at session start and leave them alone; send updates as messages. CACHE, COST, MODEL, SONNET.
7. Turn the effort dial before the model dial. Start on Opus 5.5 at `medium`; `low` for mechanical or in-the-loop work; `high` where hidden edge cases and verification matter; `xhigh`/`max` only with a measured gain. MODEL, COST, EFFORT, SONNET.
8. Put search, log-reading and summarising subagents on a smaller model; keep code edits and judgement calls on the main model. MODEL, COST, CACHE.
9. Multi-agent workflows, agent teams and advisors have to earn their coordination cost; ordinary coding tasks do not need them. WF, MODEL, COST.
10. When the same mistake recurs, fix it at the source: a line in `CLAUDE.md` or `REVIEW.md`, a skill gotcha, a lint rule, a hook, or an eval case. REVIEW, SKILLS, WF, EVAL, FAST.
11. Limit what an agent that reads untrusted text can do: read-only credentials, network allowlists, readers with no privileges handing summaries to a separate actor, spend caps. WF, AUTO, TEAMS, CLOUD, MODS.
12. Every loop needs a convergence rule: a stop condition, a round cap, a token or money budget, or a human who closes it at diminishing returns. REVIEW, WF, AUTO, FAST, EVAL.
13. Keep run state in files or a database, not in the conversation: a task checklist, bookmarks, a ledger, a log the skill re-reads, shared SQL tables. OPUS, AUTO, SKILLS, TEAMS, HTML.
14. Measure on your own tasks: `/usage` after a task, the same task on two models or two effort levels, an eval with a held-out split. COST, MODEL, EVAL, SONNET.
15. Whatever the agent needs must live in the repository: skills and commands under `.claude/`, MCP servers in `.mcp.json`, test commands in `CLAUDE.md`, installs in a SessionStart hook. Personal `~/.claude` does not travel to cloud sessions. CLOUD, SKILLS.
16. Shape behaviour through interface design (enums, expressive parameters, scripts with gotchas in docstrings, structured question tools), not through examples in the prompt; the bar for adding a tool is high. SEE, CTX, SKILLS.
17. If a thing can be counted, the agent can improve it; make the count deterministic and lock gains in with a CI ratchet. Throw out metrics that do not track the real goal. FAST, EVAL, REVIEW.
18. Keep changes small and reversible (flags, staged rollout, one-step rollback, a PR template with "Testing", "Risk", "How to revert") so less review is needed up front. REVIEW, FAST.
19. Agents under-reach by default: they stop early, call hard work infeasible, pad estimates. Humans supply ambition, taste and direction. FAST, TEAMS, WF (agentic laziness), OPUS (stops that name a next step without taking it).
20. Use richer references than a prose spec: HTML mockups and plans, a test suite, code to port, a rubric handed to verifier agents. CTX, HTML, REVIEW, EVAL.

### (a) Skills: taxonomy and advice (SKILLS, 2026-06-03, unless another key is given)

Definition and framing

- Skills are "folders of instructions, scripts, and resources that agents can discover and use" [What are skills?]. The post calls "just markdown files" a misconception; in Claude Code skills also have frontmatter options "including registering dynamic hooks" [What are skills?].
- Scale: "hundreds of them in active use" at Anthropic [intro].
- Nine categories; a skill should sit in one. "The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent." [Types of skills]. The list is offered as a gap-finding framework, "This isn't a definitive list" [Types of skills].

The nine categories [Types of skills, sub-headings 1 to 9]

| # | Category | What it holds | Example names given |
|---|---|---|---|
| 1 | Library and API reference | Correct use of a library, CLI or SDK, internal or a common one Claude struggles with; often a folder of reference snippets plus a gotchas list | `billing-lib`, `internal-platform-cli`, `sandbox-proxy` |
| 2 | Product verification | How to test or verify that code works; paired with playwright, tmux or other tools; scripts for recording video and asserting state at each step | `signup-flow-driver`, `checkout-verifier`, `tmux-cli-driver` |
| 3 | Data fetching and analysis | Connections to data and monitoring stacks: fetch libraries with credentials, dashboard ids, common query workflows | `funnel-query`, `cohort-compare`, `grafana`, `datadog` |
| 4 | Business process and team automation | A repetitive workflow as one command; simple instructions, may depend on other skills or MCPs; keeps logs of previous runs | `standup-post`, `create-<ticket-system>-ticket`, `weekly-recap` |
| 5 | Code scaffolding and templates | Framework boilerplate for one function of the codebase; composable scripts; best when scaffolding has natural-language requirements code cannot cover | `new-<framework>-workflow`, `new-migration`, `create-app` |
| 6 | Code quality and review | Enforce quality and review code; may include deterministic scripts; run from hooks or a GitHub Action | `adversarial-review`, `code-style`, `testing-practices` |
| 7 | CI/CD and deployment | Fetch, push and deploy; may call other skills for data | `babysit-pr`, `deploy-<service>`, `cherry-pick-prod` |
| 8 | Runbooks | Symptom (Slack thread, alert, error signature) to multi-tool investigation to structured report | `<service>-debugging`, `oncall-runner`, `log-correlator` |
| 9 | Infrastructure operations | Routine maintenance and operational procedures, some destructive and needing guardrails | `<resource>-orphans`, `dependency-management`, `cost-investigation` |

- Verification skills are singled out: "It can be worth having an engineer spend a week just making your verification skills excellent." [2. Product verification]. The same paragraph says they "have had the most measurable impact" on output quality internally (no number given).
- `adversarial-review` is described as: "spawns a fresh-eyes subagent to critique, implements fixes, iterates until findings degrade to nitpicks" [6. Code quality and review].
- `babysit-pr`: monitors a PR, retries flaky CI, resolves merge conflicts, enables auto-merge [7. CI/CD and deployment].

What makes a skill work [Tips for making skills, nine sub-headings]

- Don't state the obvious. "A skill that restates what Claude would do by default adds context without adding value." Knowledge skills should hold what "pushes Claude out of its normal way of thinking"; the `frontend-design` skill (avoiding "the Inter font and purple gradients") is the example.
- Build a gotchas section. "The highest-signal content in any skill is the Gotchas section." Build it from failures Claude actually hits and keep adding. Example gotchas are concrete data facts, such as an append-only table where the wanted row is the highest version, or a field with two names in two services. A figure in that section shows one skill's Gotchas growing "from one line (proration rounds down) to four" over three months (fig. alt).
- Use the file system and progressive disclosure. "Tell Claude what files are in your skill, and it will read them at appropriate times." Named layout: `references/api.md` for signatures and usage examples, `assets/` for output templates, plus folders of scripts and examples. Fig. B: a hub `SKILL.md` with "a symptom-to-file table telling Claude which file to read" (fig. alt).
- Avoid railroading. "Give Claude the information it needs, but give it the flexibility to adapt to the situation." Fig. C contrasts six numbered git steps with a goal-and-constraints version; caption: "State the goal and the constraints, not every step." (fig. alt and caption).
- Think through the setup. Store per-user setup in a `config.json` in the skill directory; if it is missing, the agent asks. For structured multiple-choice questions, tell Claude to use the `AskUserQuestion` tool.
- Write descriptions for the model, not for humans. Claude scans a listing of every skill's description at session start, so "the description field is not a summary"; it is "a description of when to trigger this skill". Fig. E contrasts a marketing-style sentence with `Monitors a PR until it merges. Trigger on ‘babysit’, ‘watch CI’, ‘make sure this lands’.` (fig. alt): include the trigger phrases a user would type.
- Help Claude remember. A skill can keep an append-only log, JSON files or a SQLite database; `standup-post` keeps `standups.log` and reads its own history. Use `${CLAUDE_PLUGIN_DATA}` for a stable data directory.
- Store scripts and generate code. "Giving Claude scripts and libraries lets Claude spend its turns on composition, deciding what to do next rather than reconstructing boilerplate." Fig. G: helper functions "with the gotchas written into the docstrings" (caption); Claude then writes one-off scripts that import them.
- Use on-demand hooks. "Skills can include hooks that are only activated when the skill is called, and that only last for the duration of the session." Examples: `/careful` (PreToolUse matcher on Bash that blocks `rm -rf`, `DROP TABLE`, force-push, `kubectl delete`) and `/freeze` (blocks any Edit/Write outside one directory, for debugging without drive-by fixes).

Distribution, composition, measurement

- Two ways to share: check into the repo under `./.claude/skills`, or ship a plugin through a plugin marketplace. Repo check-in suits small teams with few repos, with a cost: "But every skill that is checked in also adds a little bit to the context of the model." [Distributing skills].
- Marketplace curation at Anthropic is organic: upload to a sandbox folder, advertise, and open a PR to the marketplace once it has traction (owner's call) [Managing a skills marketplace].
- Dependencies are not native; reference another skill by name and the model invokes it if installed [Composing skills].
- Measurement: "we use a PreToolUse hook that lets us log skill usage within the company" to find popular and under-triggering skills (gist linked) [Measuring skills].
- Growth pattern: "Most of our best skills began as a few lines and a single gotcha" [Get started].

Supporting points from other posts

- Skills are "lightweight guides"; "Avoid making them overconstrained, except in highly important areas." Split long skills into many files. Best when they encode opinions and knowledge "particular to you, your team, or product" (CTX [Skills]).
- Verification and code review were moved out of Claude Code's own system prompt into skills (CTX [Now: Use progressive disclosure]).
- The team's pre-PR skills: one hunts for bugs, one simplifies the diff, one checks behaviour end to end (REVIEW [1. The work is verified before anyone else looks]).
- Skill triggering is a good hill-climbing target because the metric (trigger rate) is coupled directly to the description being edited (EVAL [Hillclimbing]).
- The `claude-api` skill went from 66% to about 88% on its own eval; the largest single insight was that content was present but Claude wrote remembered, older API shapes, fixed by a table near the top mapping remembered forms to current ones (EVAL [Hillclimbing for performance improvement]).
- A saved workflow can ship inside a skill: put the JavaScript file in the skill folder, reference it from `SKILL.md`, and tell Claude to treat it "as a template instead of a script that needs to be run verbatim" (WF [Saving and sharing dynamic workflows]).

### (b) New rules of context engineering, as do/don't pairs (CTX, 2026-07-24, unless another key is given)

Headline evidence: "We removed over 80% of" Claude Code's system prompt for Opus 5 and Fable 5 class models "with no measurable loss on our coding evaluations" [intro]. Diagnosis: "we were overconstraining Claude Code, both through our system prompt and in our CLAUDE.md files and skills" [Unhobbling Claude]. Conflicting messages in one request (system prompt, skill and user disagreeing about comments) make Claude "think more carefully" before acting [Unhobbling Claude].

| Don't (older habit) | Do (current models) | Locator |
|---|---|---|
| Hard rules written to prevent the worst case, such as "default to writing no comments", "Never write multi-paragraph docstrings" | State the principle and let judgement apply it: "Write code that reads like the surrounding code: match its comment density, naming, and idiom." | [Then: Give Claude rules] / [Now: Let Claude use judgement] |
| Examples of how to use each tool (formerly called the number one rule for tool usage) | Design the interface: expressive parameters, enums, one behavioural rule. "giving examples actually constrains them to a certain exploration space" | [Then: Give Claude examples] / [Now: Design interfaces] |
| Put every practice that might matter up front in the system prompt, `CLAUDE.md` or one `SKILL.md` | Progressive disclosure: skills, deferred tools found through ToolSearch, and "a tree of files that can be loaded at the right time" | [Then: Put it all upfront] / [Now: Use progressive disclosure] |
| Repeat an instruction in several places, or place it late in context, so it is obeyed | Say it once, where it belongs: "put instructions on how to use tools in the tool descriptions rather than the system prompt" | [Then: Repeat yourself] / [Now: Simple tool descriptions] |
| Save memories by hand into `CLAUDE.md` (the `#` hotkey) | Auto-memory: "Claude now automatically saves memories that are relevant to the work and to you" | [Then: Memory in CLAUDE.md files] / [Now: Auto-memory] |
| Simple markdown plans and specs as the only reference | Rich references: HTML artifacts, code, tests, rubrics. "A spec may also be a detailed test suite, or a function in a different codebase that Claude might port." | [Then: Simple specs] / [Now: Rich references] |

- The TodoWrite description shrank from "about 9,100 characters of when-to-use lists and worked examples" to one sentence, a status enum (`pending`, `in_progress`, `completed`) and one rule (fig. alt, [Now: Design interfaces]).
- Applying it to `CLAUDE.md`: keep it light, describe the repo briefly, "spend most of the tokens on gotchas inside of the codebase", do not state what Claude can see from the file system, and reference a verification skill instead of inlining verification steps [CLAUDE.md].
- References: `@`-mention files; prefer references that are code. "a HTML mockup of a design will generally produce better results than a description of the design or a screenshot" [References].
- Rubrics are a reference type: used with dynamic workflows to spin up verifier agents that check taste-based work [Now: Rich references].
- Tooling: `claude doctor`, or `/doctor` in a session, "to rightsize your skills, and CLAUDE.md files" [intro]; `/claude-api prompt-audit` checks skills and `CLAUDE.md` for prompting anti-patterns (COST [Check your prompts when you migrate]).

Reversals stated in other posts

- Thinking instructions: remove "think carefully", "think step by step" and similar from prompts and saved instructions. "Opus 5.5 always thinks before it replies, and it decides how much." Removing such a line made replies start sooner "with no clear drop in quality" (OPUS [Stop telling it to "think hard"]). To change thinking, change effort; "asking the model in the system prompt to think less doesn't reliably reduce it" (SONNET [Re-run your effort sweep]).
- Show-your-reasoning requests: remove them; "A request to reproduce its internal reasoning in the reply can be declined." Ask for a short explanation instead (OPUS [Don't ask it to show its reasoning in the reply]; SONNET [Use thinking.display for progress] names the decline category `reasoning_extraction`).
- Old-model workarounds: refusal steering, tool-call retry shims and "do not be lazy" lines should be removed, then "re-run your evals before tuning anything else" (SONNET [Remove Sonnet 5 workarounds]).
- Rituals: an audit removed "a mandatory six-step procedure, a scratchpad rule, a verify-twice rule, and instructions that contradicted each other"; these made the model write more and repeat tool calls. Measured on one 44-ticket benchmark: a further 9% cost cut after the 18% from moving to Opus 5.5 at low effort (COST [Check your prompts when you migrate]).
- Over-specification in skills: see "Avoid railroading" in (a).
- Examples: in the eval post's illustration, the prompt variant that "adds two worked examples" was reverted because train rose while test stayed flat; the variant that defined each category and added a tie-break rule won (EVAL fig. 7 alt). One illustrative case, consistent with the CTX claim.
- Vague negatives: for design, "avoid a generic look" style instructions swap one default for another; a list of the specific patterns to leave out "works much better" (OPUS [For design work, name the styles you don't want]). So specific prohibitions still work where the model has a strong default.
- Stops: Opus 5.5 "follows instructions that name these stops", so a short `CLAUDE.md` rule on when to keep going and when to ask is recommended (OPUS [Tell it which stops you want]).

Not covered: none of the 18 posts makes an explicit statement about emphasis words (capitals, "IMPORTANT", "MUST") or about role prompts (a persona line that opens a prompt). The closest material: CTX uses "DO NOT add comments" as its example of a clashing instruction and says strong guidance "that might not always be true" was a worst-case guardrail for older models [Then: Give Claude rules]; MODEL says to write prompts "precisely enough for the most literal model" when several models share a prompt [Check compatibility before migrating]; WF uses personas only for reviewer subagents ("skeptic persona subagent", [Memory and rule adherence]). Inference: emphasis and role prompts fall under the same over-constraint argument, but a setup that wants a cited rule on them needs another source.

### (c) Prompt caching facts that shape instruction files, tools and sessions

Mechanics

- "Prompt caching works by prefix matching"; rule of ordering: "static content first, dynamic content last" (CACHE [Lay out your prompt for caching]).
- Claude Code's order: static system prompt and tools (cached globally), `CLAUDE.md` (cached per project; the figure adds memory), session context (per session; the figure names env, MCP and output style), then conversation messages (CACHE [Lay out your prompt for caching], fig. A alt).
- "Any change anywhere in the prefix invalidates everything after it." (CACHE [Lessons learned]). "Changing the tool definitions clears the whole cache, and a change to the system prompt clears it from that point on", which is almost everything (COST [Session shape and hit rate]).
- Caches are per model: "The prompt cache belongs to the model that wrote it." (MODEL [Switch at a natural break]).
- Lifetime in Claude Code: one hour on a subscription; five minutes on an API key or cloud provider, or once a subscription draws on usage credits; each hit resets it (COST [How the cache works]).
- Prices on Opus 5.5: a cache read costs 5% of fresh input; a write costs 1.25x input (five-minute cache) or 2x (one-hour cache). At 120K tokens a five-minute write is about $0.60 and a read about $0.02, so "One write costs as much as 25 reads." (COST [How the cache works]).
- Effect size: the same 2.8M input tokens cost $11.20 uncached, $1.62 at a 90% hit rate, about $0.99 at 96%. "No other setting moves input cost this much." (COST [Cache reads]).
- Anthropic alerts on cache hit rate and declares SEVs when it drops (CACHE [intro]).

What breaks the cache

- Historic Claude Code breakages: "putting an in-depth timestamp in the static system prompt, shuffling tool order definitions non-deterministically", and changing tool parameters such as which agents the Agent tool can call (CACHE [Lay out your prompt for caching]).
- "adding or removing a tool invalidates the cache for the entire conversation" (CACHE [Never add or remove tools mid-session]).
- Expect a cache write when you: pause longer than the lifetime; change effort on Bedrock, Google Cloud's Agent Platform or a gateway; turn on fast mode for the first time in a conversation; connect or disconnect an MCP server; switch models; or the conversation is compacted. "So set these up when the session starts, and leave them alone while it works." (COST [Session shape and hit rate]).
- Effort: on Opus 5.5 with an API key or subscription, "changing effort keeps the cache" (COST [Changing effort mid-session]). On the Sonnet 5.5 API, changing top-level effort between requests invalidates the cache; per-message effort (beta) does not (SONNET [Cache more of your prompt]).

How Claude Code designs around it

- Updates go in messages, not the system prompt: a `<system-reminder>` tag in the next user message or tool result carries changed facts (time, changed files) (CACHE [Use messages for updates]).
- Plan mode keeps every tool loaded; `EnterPlanMode` and `ExitPlanMode` are tools and a system message states the mode. "The tool definitions never change." (CACHE [Using Plan Mode to design around the cache]).
- MCP tools are sent as name-only stubs with `defer_loading: true` and discovered through tool search; "the same stubs are always present in the same order" (CACHE [Use tool search to defer instead of remove]). COST confirms: only tool names and server instructions load at start [What loads before you type].
- Model switching: 100K tokens into an Opus conversation, "it would actually be more expensive to switch to Haiku than to have Opus answer"; use a subagent with a hand-off message instead (CACHE [Don't change models mid-session]).
- Compaction runs as a fork with the identical system prompt, context and tools, with the compaction prompt appended as a new user message, so the parent's cached prefix is reused; a "compaction buffer" of context is reserved for it (CACHE [The solution: cache-safe forking]). "Fork operations need to share the parent's prefix." (CACHE [Lessons learned]).

Session habits that follow

- Every turn resends the context even when cached: about $0.004 per turn at 20K tokens, about $0.03 at 150K; 30 turns cost about $0.12 against $0.90 (COST [Why long sessions cost more per turn]).
- `CLAUDE.md` "loads into the context at the start of every session, so each line in it is part of what every turn resends"; the costs docs "suggest keeping it under 200 lines" (COST [What loads before you type]).
- `/clear` between unrelated tasks costs nothing. `/compact` costs one request (about $0.25 at 150K tokens, repaid within about ten turns) and accepts a keep-instruction, for example `/compact keep the failing test names and the schema change` (COST [Compaction, /compact and /clear]).
- Timing: "compact before a break, not after one"; after the cache has expired the same `/compact` at 150K costs about $0.75 in input alone. To abandon a path, `/rewind` returns to an already cached prefix (COST [Compaction, /compact and /clear]).
- Compaction loses detail; do it at a natural break and name what must survive. `/autocompact <tokens>` sets the threshold (COST [Compaction, /compact and /clear]).
- To switch models, do it at a natural break after `/compact`, or start a fresh session "with a short written plan" (MODEL [Switch at a natural break]; COST [Moving up to Fable 5.1]). `/model` also saves the choice as default for new sessions (COST).
- Fast mode: the first request after turning it on pays the fast input price on the whole conversation uncached, "So turn it on at the start of a session, not deep into one." (COST [The rest of the bill]).
- Diagnosing: `/usage` shows a prompt-cache line that "often names the likely cause of the last miss" (COST [Reading a session]).
- Minimum cacheable prompt on Sonnet 5.5 is 512 tokens (1,024 on Sonnet 5) (SONNET [Model details]).

Inference: for a project setup this argues for a stable, small always-loaded layer (short `CLAUDE.md`, a fixed MCP list per project, no dynamic text such as timestamps in instruction files), with variable material in skills, files and messages; and against editing `CLAUDE.md`, toggling MCP servers or switching models in the middle of a long session.

### (d) "Seeing like an agent": tool and elicitation design, and what it implies for project scripts (SEE, 2026-04-10)

- Method: shape tools to the model's abilities, found by observation. "Experiment often, read your outputs, try new things." [Seeing like an agent is an art, not a science].
- Elicitation took three attempts [Improving elicitation with the AskUserQuestion tool]:
  1. A questions array on the plan-exit tool. It confused Claude, which was asked for a plan and questions about the plan at once.
  2. A custom markdown output format parsed into UI. "Claude could usually produce this format, but not reliably." It added sentences, dropped options, or abandoned the structure.
  3. A dedicated `AskUserQuestion` tool, callable any time, prompted especially in plan mode, shown as a modal that blocks the loop until answered. It forces structured output with multiple options and is composable from the Agent SDK and from skills.
- Acceptance test for a tool: the model calls it willingly and well. "even the best designed tool doesn’t work if Claude doesn’t understand how to call it" [Attempt 3].
- Tools expire. TodoWrite plus a reminder every 5 turns helped early models; later the reminders made Claude "think that it had to stick to the list". It was replaced by the Task tool, with dependencies and updates shared across subagents. "the tools that your models once needed might now be constraining them" [Updating with capabilities: tasks & todos].
- Context finding: Claude Code started with RAG over a vector index and dropped it for a Grep tool. RAG needed indexing, was fragile across environments, and "Claude was given this context instead of finding the context itself" [Designing a search interface].
- Progressive disclosure adds capability without adding a tool. Claude Code has about 20 tools and "The bar to add a new tool is high, because this gives the model one more option to think about." [Progressive disclosure: the Claude Code Guide agent].
- The Claude Code Guide case: (1) product documentation in the system prompt was rejected as context rot for a rare need; (2) a docs link worked but pulled large chunks into context; (3) a subagent now searches the docs in its own context and "hands back only the answer" [same section].
- Keep the set of supported models small and similar in capability, because tool design depends on the model [Updating with capabilities: tasks & todos].

Related statements in other posts

- Enumerations and a single rule in a tool's schema steer usage better than examples (CTX [Now: Design interfaces]).
- Scripts in skills let Claude compose instead of rebuilding boilerplate; put gotchas in docstrings (SKILLS [Store scripts and generate code]).
- Deterministic scripts make quality skills robust (SKILLS [6. Code quality and review]).
- Mods can register a tool or slash command and pass process arguments as an argv array so "nothing in a path is run as shell code" (MODS [Blast Radius]).

Inference, for a project's own scripts and CLIs (not stated in SEE in these words):

- Prefer a few general, composable commands the agent can search and combine (grep-style) over many narrow wrappers or a pre-built index.
- Make parameters and outputs self-describing (enumerated values, structured results) instead of documenting usage with examples in `CLAUDE.md`.
- When a human answer is needed, use the structured question tool from a skill, not a free-text convention the model must format.
- Put rarely needed documentation behind a lookup (a skill file or a subagent that returns only the answer), not in always-loaded instructions.
- Re-test each helper when the model changes and delete the ones that now constrain it.

### (e) Dynamic workflows and agent automations

When to use workflows (WF, 2026-06-02)

- A workflow is a JavaScript file executed by Claude Code with functions that spawn and coordinate subagents. Fig. A names `agent(prompt, opts)` with options `schema` (validated JSON), `model` (opus, sonnet or haiku), `isolation` (worktree or remote) and `agentType`, plus `parallel()` and `pipeline()` (fig. alt, [How dynamic workflows work]). An interrupted workflow resumes with the session.
- They target three failure modes of one long context [Why dynamic workflows]: agentic laziness (declaring done after partial progress, "35 of the 50 items"), self-preferential bias (preferring its own findings when judging), and goal drift (losing constraints across turns and compactions; "Each summarization step is lossy").
- Fit: "long-running, massively parallel, highly structured and/or adversarial tasks" [Why dynamic workflows]. Cost warning up front: "dynamic workflows often use more tokens and are best suited for complex, high value tasks" [intro].
- Not for routine work: "most traditional coding tasks do not need a panel of 5 reviewers" and "parallelism and specialization have to earn their coordination cost" [When not to use dynamic workflows].
- Six composable patterns [Helpful patterns when using dynamic workflows]: classify-and-act; fan-out-and-synthesize (the synthesis step is a barrier that waits for all agents); adversarial verification (a second agent checks each output against a rubric); generate-and-filter; tournament (N attempts judged pairwise); loop until done.
- Use cases with their recipes [Use cases]:
  - Migrations and refactors: one subagent per call site, failing test or module, each in a worktree; a second agent reviews adversarially; then merge. "Consider telling the agent not to use resource intensive commands" so parallelism does not exhaust the machine.
  - Deep research: the bundled `/deep-research` skill fans out searches, fetches, adversarially verifies claims and writes a cited report.
  - Deep verification: one agent extracts every factual claim, one checker per claim, optionally an auditor per source.
  - Sorting: tournaments or bucket-rank-then-merge, because "comparative judgment is more reliable than absolute scoring".
  - Memory and rule adherence: for rules Claude keeps missing even in `CLAUDE.md`, one verifier agent per rule, plus a skeptic agent to filter false positives. The reverse: mine recent sessions and review comments for repeated corrections, cluster, adversarially verify ("would this rule have prevented a real mistake?"), and distil survivors into `CLAUDE.md`.
  - Root-cause investigation: agents generate hypotheses from disjoint evidence (logs, files, data); each hypothesis faces verifiers and refuters.
  - Triage at scale: classify, dedupe against what is tracked, act or escalate; pair with `/loop`.
  - Exploration and taste: generate options, review against a rubric, optionally a tournament.
  - Evals: run variants in worktrees and have comparison agents grade outputs against a rubric, for example when refining a skill.
  - Model routing: a classifier agent researches the task and routes to Sonnet or Opus.

How to write and run them (WF [Tips for building dynamic workflows])

- Ask for one in plain language, or use the trigger word `ultracode` [Dynamic vs static workflows]. Detailed prompts naming the patterns give the best results [Prompting]. A "quick workflow" is valid for small jobs such as an adversarial check of one assumption.
- Stop conditions: for unknown amounts of work, "loop spawning agents until a stop condition is met (no new findings, or no more errors in the logs)", not for a fixed number of passes [Loop until done]. `/goal` sets "a hard completion requirement"; `/loop` repeats on an interval [Combine with /goal and /loop].
- Cost control: a prompt such as `use 10k tokens` sets a token cap [Token usage budgets]. The panel figure shows real scale: a review run of 14 agents used 482k tokens in about 6 minutes; a deep-research run of 22 agents used 1.1M tokens in about 11 minutes (fig. H alt).
- Save with `s` in the workflow menu; store under `~/.claude/workflows` or inside a skill [Saving and sharing dynamic workflows].
- Safety pattern, quarantine: "barring the agents that read untrusted public content from taking high-privilege actions"; reader agents get read-only tools and emit a structured summary; a separate actor agent holds the privileges (WF [Triaging at scale], fig. G alt).

Scheduled agent automations (AUTO, 2026-10-08; reference implementation on Claude Managed Agents, beta)

- Six parts: sources, one destination, agent, schedule, memory, guardrails [Overview]. Files: `agent.md` (model, tools, run steps), `deployment.md` (cron, time zone, budget, first message), `environment.yaml` (network allowlist), two memory stores, `vault.yaml`, `claude-lock.json`; applied with `ant apply` [Get the code].
- The six rules the post reduces to [Getting started]:
  1. "Read each source from a bookmark, not a fixed time window." A fixed window fails both ways: "A late run leaves a gap and an early run repeats items." [Read from where you left off].
  2. "Report a failed read as unreadable, never as a quiet day." A dead MCP server just removes its tools; without a rule the agent reports nothing new. On failure: keep the bookmark, write from the other sources, end with one line naming what could not be read [Don't mistake a failed read for a quiet day].
  3. Re-check every item against its live source right before posting; "never hedge an item's status: assert it or drop it" [Re-check anything still open right before posting].
  4. Count a post as sent only on confirmation (`"ok": true` and a message ts), then update ledger and bookmarks; check for today's title first; mark unclear results "maybe posted" and change nothing [Confirm the post landed before recording it].
  5. Re-read preferences every run from a store the agent cannot edit. "If it can't read the file, it should stop and say so instead of running on defaults." [Re-read your preferences at the start of every run].
  6. Read-only access wherever the agent only reads, and a spend cap per run.
- Safety reasoning: sources contain other people's text and "that text can be interpreted as instructions. Limit what the agent could do if it followed them." Read-only token, read-only preferences store, host allowlist. A planted instruction can still change what the brief says, including through the agent's own notes [Limits on what it can do].
- Credentials stay in a vault outside the sandbox; the sandbox holds a placeholder that the platform swaps for the real token only for allowed hosts [Give the agent its own, scoped credentials].
- Spend cap: "Start at three to five times the cost of a normal run, then tighten it as you see real numbers." A capped run pauses with `budget_reached`, so "a cap set too low looks like a brief that went quiet" [Set the spending cap from real runs]. The example budget is `"500"` cents.
- Other failure modes: dates computed in the server's time zone (state the reader's zone in the first message) [Compute dates in your time zone]; stale memory in both directions, fixed by a ledger with stable ids and last known status [Keep a ledger of what you've already reported, and report the change]; unattended MCP tools need `always_allow` because nobody is there to approve [Agent].
- Model in the reference agent: `claude-sonnet-5-5` [Agent], matching MODEL's row for repeated agent tasks.

Claude Code's own automation surfaces (CLOUD, 2026-10-06)

- Routines (research preview): a saved prompt, repositories, connectors and environment; each run is a cloud session started by a schedule (hourly at most), an HTTP call or a GitHub event; created with `/schedule`. "Routines run without approval prompts, and by default they push to `claude/`-prefixed branches." [6. Start work without starting it yourself].
- Auto-fix watches a PR and pushes fixes for failing checks and review comments, asking about anything ambiguous or architectural; started from the CI bar or `/autofix-pr` [5. Hand CI failures and review comments to Claude].
- Limits: parallel sessions draw on plan limits in parallel; routines have hourly caps [Habits that pay off].

### (f) Multi-agent teams with Fable 5.2

What the TEAMS post is: a report of one research experiment (2026-11-09), not a how-to for Claude Code users. Its guidance is mostly implicit. Explicit delegation advice for everyday use comes from OPUS, MODEL, COST, CLOUD and WF and is listed second.

From the experiment (TEAMS)

- Result: 1,000 agents on an early Fable 5.2, one lead and 999 helpers, reproduced a Lean formalisation of Fermat's Last Theorem without the domain platform or a steering researcher. "The team took 28.7 hours, used one-third as many output tokens, and wrote a proof one-seventh the length of the original." [intro]. The September run took 11 days and about 6 billion output tokens [Problem].
- Harness was general tools only: shell and editor in a no-network sandbox, the toolchain baked into the image, a Git branch per agent with merge requests into main, and a shared Postgres database [Tools].
- Shared state over messaging: "Agents had no dedicated messaging tools and coordinated only through the database and Git." [Sandboxing]. SQL was chosen "because it offers general primitives for organizing information", handles concurrent writes, and is familiar to Claude [Collaboration].
- Isolation was needed for scale: "A single shared machine hit its limits at about 100 agents"; more than half of the 100-agent runs had to be stopped or restarted for memory, disk or CPU [Collaboration].
- Briefing was minimal: the 60 statements with one-line descriptions, the tool list, and a hierarchy. The lead was told to split and assign; helpers were told to expect work and to check with the lead if a task was unclear [Prompting]. The harness sent the lead 19 automatic time-remaining reminders "each encouraging the lead to keep going" [Prompting].
- Self-organisation: in the first 10 minutes the lead created five tables (announce, assign, notes, subtasks, landed), assigned crews of 16 to 17 with a captain each, and told every helper to first judge difficulty and post a verdict [The lead dealt out the statements]. Work later became pull-based (a first-claim subtasks table; "do not wait for me") and, for the hardest statement, a task tree of 2,418 tasks up to 10 levels deep in which each piece could assume the pieces beneath it [The lead assigned the team to Langlands–Tunnell].
- Verification was mechanical and external: a statement counted only when Lean's checker accepted it and a grader checked main [Harness], [Results].
- Misjudged difficulty: helpers judged 47 of 60 statements infeasible within budget, "yet the team went on to prove most of them". "Agents tend to give up on hard problems and misjudge their difficulty." and "Human encouragement at such moments can keep agents from stopping too early." [Conclusions].
- Safety, layered because "no single layer of defense is sufficient to contain a team of agents" [Safety]:
  - Sandboxing: own VM, no network, one pipe to a gateway that tags identity outside the sandbox; pushes only to the agent's own branch with a separate merge job; shared unprivileged database role with a five-second statement limit and writes refused above 256 MiB; unprivileged user with sudo removed; hardened kernel; tools that cannot read or change the agent loop [Sandboxing].
  - Real-time: a prompted LLM classifier can block each tool call. "When the classifier blocks a tool call, the whole agent team stops and a person must review the block before the team can restart." [Real-time monitoring]. (In this run a helper block removed only that helper; a lead block would have ended the run.)
  - Monitors that saw chain of thought and inter-agent communication caught all sabotage attempts in red-team evaluations; an action-only monitor runs in parallel so reasoning cannot talk the monitor round [Real-time monitoring].
  - Offline monitor over the whole record [Offline monitoring].
  - Outcome: over more than a million tool calls, none met the bar to be blocked [Real-time monitoring].
- Limits stated: a toy experiment; domain-specific harnesses may still be more efficient; the run was restarted near hour 18 from its last save with 12 more hours (fig. 4 caption) [Conclusions].

Practical delegation guidance from the other posts

- What to delegate: audits, migrations and reviews across a large codebase (OPUS [Ask it to split big work across subagents]); searching files, reading logs, summarising, on Haiku 5.5 or Sonnet 5.5, because "Wrong answers are cheap to spot, and the main model has the judgment calls anyway." (MODEL [Pick a model by task]).
- What not to delegate: code edits and judgement calls (MODEL [Put subagents on smaller models]); one chain of dependent steps, or work that fits in one context window, where "the planning and merging cost more than they save" (MODEL [Delegate bulk work to cheaper workers]).
- Who leads: Fable 5.2 for "leading many subagents", major refactors and long unattended runs (MODEL [Pick a model by task], [TL;DR]).
- Briefing: one self-contained ticket per worker that states "what's wrong, what done looks like, and how to prove it" (CLOUD [1. Clear a backlog in parallel]); split parallel work along file boundaries (CLOUD [Three tasks, one repository, three machines]); isolated goals and own context windows (WF [Why dynamic workflows]).
- Verification: the example prompt says "When a subagent reports back, check its evidence before you accept it." and asks for one final table of item, verdict and evidence (OPUS [Ask it to split big work across subagents]); use a separate verifier per output (WF [Adversarial verification]).
- Cost evidence: an Opus 5.5 lead over up to 25 Sonnet 5.5 workers on a defect search across about 22 million tokens of source "cost about a third less than Opus 5.5 alone at its default effort" and scored about the same (MODEL [Delegate bulk work to cheaper workers]). Agent teams (experimental) use about seven times the tokens of a standard session when teammates run in plan mode; "Keep teams small, keep each task self-contained, and shut teammates down when their part is done." (COST [Moving down for lookups]).
- Risk of cheap workers: a small model that misreads a search result sends the main model after the wrong file (MODEL, COST).
- Mechanics: `model: haiku` or `model: sonnet` in a subagent definition; `CLAUDE_CODE_SUBAGENT_MODEL` sets the default; a subagent without a model setting runs on the main model (COST [Moving down for lookups]). The built-in Explore subagent now runs on the session's model; define your own subagent named `Explore` with `model: haiku` to keep exploration cheap (MODEL [Put subagents on smaller models]).

Inference for a solo developer: the transferable parts of TEAMS are shared durable state instead of chat between agents, one isolated workspace and branch per agent with a controlled merge step, a mechanical acceptance check, and explicit pushes against premature "infeasible" verdicts. The 1,000-agent scale and the kernel-level controls are not.

### (g) Effort and model selection, with the numbers

Lineup and list prices as of 2026-11-09 (MODEL [The four models side by side])

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.2 |
|---|---|---|---|---|
| Input / output per million tokens | $0.10 / $0.50 up to 100K-token prompts; $0.50 / $2.50 above | $2 / $10 | $4 / $20 | $8 / $40 |
| Cache read per million | $0.01, or $0.05 above 100K | $0.10 (SONNET says $0.20, see contradictions) | $0.20 | $0.20 |
| Context / max output | 1M / 128K | 1M / 128K | 1M / 128K | 1M / 128K |
| Default effort, API | `medium` | `high` (`medium` in Claude Code) | `medium` | `high` (`medium` in Claude Code) |
| Thinking | adaptive, can be turned off | adaptive, `between_tools` option | always on | always on |
| Fast mode | no | no | yes | yes |

Recommendations (MODEL [TL;DR], [Pick a model by task])

- Default: "you should start most work on Opus 5.5 at its default effort level", `medium`. It is the Claude Code default and half Fable 5.2's token price.
- Down to Sonnet 5.5 for well-scoped everyday work (a bug fix, a feature against a spec) at `medium` then `high`, and for agent tasks run repeatedly. A clear spec is not enough reason: a migration or performance optimisation can still need Opus or Fable.
- Down to Haiku 5.5 for classification, routing, extraction and for subagents on side tasks.
- Up to Fable 5.2 for the hardest technical work, when Opus 5.5 at `high` falls short, for long unattended runs, major refactors and migrations, architecture planning, deep research, and leading many subagents; start at `medium`, then `high`.
- Effort before model: "Past `high`, one more effort level can cost as much as a bigger model", so past `high` test the next model up at a lower effort. Effort adds thinking, tool calls and self-checks, and latency; it "won't give a model knowledge or skill it doesn't have".
- Escalation order when results fall short (MODEL [Latency against accuracy]): (1) check the model can verify its own work; (2) raise effort one level; (3) move up a model, starting at a lower effort than on the smaller one. "Often providing a means of self-verification is more cost effective and adds less latency than changing effort levels."
- Run cheap, retry failures expensive, when outcomes can be checked automatically: on a SWE-bench Pro subset, Opus 5.5 at `low` with failures re-run at `high` passed about 97% of tasks for about $0.17 each, against 95.3% for $0.29 with everything at `high` (MODEL [Latency against accuracy]).
- Mixed-model routing: "let code pick the model rather than asking a model to" when the rule is simple (MODEL [Check compatibility before migrating]). "Keep a multi-model setup only if it beats every single-model point on that chart." (MODEL [Measure on your own work]).
- `opusplan` (Opus plans, Sonnet edits) is the opposite of "edits on the main model"; both MODEL and COST say to measure it before adopting it.
- Advisor tool (beta): of four documented pairings "none clearly beat its executor alone"; one pairing gained 1.7 points for about 2.1 times the money ($2.92 per attempt) (MODEL [Escalate hard decisions to an advisor]).

What effort is (EFFORT, 2026-09-25; COST)

- Effort is a hint about how much compute to spend; in practice it modulates verification, edge-case testing and independent judgement: "effort was a great way of modulating how much verification and edgecase testing Claude did and how much of its own judgement it used" (EFFORT [intro]).
- It "sets a general disposition for how many tokens the model spends on each turn: its thinking, the text it writes, and its tool calls" (COST [Raise effort before you change models]). Opus 5.5 has `low`, `medium`, `high`, `xhigh`, plus `max` for a single session.
- More effort means more assumptions made for you: "higher effort levels will get more work done but Claude will also make more assumptions on my behalf" (EFFORT [Takeaways]).
- A detailed spec makes effort levels converge: given an interview-derived spec, models at different efforts produced similar designs and implementations (EFFORT [Highly specified build task]).
- Thariq's rule of thumb (EFFORT [When to use different effort levels in Claude Code]): Low for quick in-the-loop responses (brainstorming, sketching, easy changes); Medium for most regular engineering such as new features; High where verification matters or there are edge cases, such as a bug in a brownfield codebase; Max for fully autonomous hard problems such as end-to-end build and verification or finding vulnerabilities.
- His feature loop (EFFORT [Takeaways]): give a spec and have Claude interview you; implement on low; review and iterate on low; verify and test on high.
- COST's version: `medium` for well-scoped daily work; `high` when medium stalls; `low` for mechanical work such as renames or applying a known pattern; keep `xhigh` and `max` "for work where you've measured a gain" (COST [Raise effort before you change models]).
- Do not carry levels across models: Opus 5.5 default is `medium`, one below Opus 5's `high`, and at a given level it thinks more per turn (COST). Sonnet 5.5's levels were also recalibrated (SONNET [Re-run your effort sweep]).
- When more effort is the right fix: "The clearest sign you need more effort is a fix that stops at one layer." (handler updated, client still sends the old field). A test through the client would catch the same bug at medium, so "before you raise effort, check whether the model has a way to check its work" (COST [When medium fixes one layer]).
- Pricing of the choice: high adding 20K thinking tokens costs $0.40 on Opus 5.5, about one ten-turn retry loop. "So high pays for itself on a task where it saves one retry." (COST [Raise effort before you change models]).
- When effort does not help: it reduces missed-edge-case failures but "does not fix when the model has the wrong approach" (EFFORT [Higher effort levels help when there are many edge cases]).
- `/effort <level>` changes it mid-task; `/effort status` shows it (COST [Changing effort mid-session]).

Benchmark numbers

- SWE-bench Pro, Opus 5.5, relative to `high`: `medium` about 2.5 points lower for about 70% of the cost; `low` about 8 points lower for about a third; `xhigh` about 1.4 points higher for 2.5 times the cost (MODEL [Latency against accuracy]).
- Terminal-Bench 3.0 (Anthropic's runs): Fable 5.1 at `max` 58.0%; Opus 5.5 at `high` 58.9% with half the tokens (MODEL [Capability and cost per finished task]).
- FrontierCode 2.0: Fable 5.2 at `high` 45.3%, Opus 5.5 at `max` 45.5%, the former at roughly half the cost per task (MODEL, same section).
- Spend concentrates: "On one 20-problem search benchmark, two problems carried 43% of the spend." (MODEL, same section).
- Terminal-Bench 3.0 task examples (5 attempts each, internal runs): `html-js-filter`, Fable 5.1 from 1/5 at low to 5/5 at xhigh (about 2 minutes against about 33 minutes per attempt); `mvcc-lsm-compaction`, Opus 5.5 from 0/5 at low to 4/5 at xhigh (about 1 minute against about 11); `cli-2ph-simplex`, 0/5 to 5/5 at high; `gsea-proteomics`, 0/5 to 4/5 at high (EFFORT [Higher effort levels help...], [Problem areas where effort helps]).
- By category, Fable 5.1 pass rate low to top effort: Security 64% to 87%, Hardware 34% to 75%, ML 54% to 73%, Science 41% to 61%, Software 43% to 56%, Media 18% to 30%, Operations 12% to 22% (EFFORT fig. C text, `` copy only).
- Failure mix, Fable 5.1, 370 attempts: passes 140 at low and 214 at max; "a bug its tests missed" 40 to 14; "wrong or incomplete fix" 31 to 10; "picked the wrong reading" 25 to 47 (EFFORT fig. B text, `` copy only; failure kinds assigned by a model judge).
- Toy design task: 1 minute at low, 28 minutes at max (EFFORT [Lightly specified design task]).

Cost per task (COST, 2026-09-25, Opus 5.5 list prices: $4 input, $20 output, $0.20 cache read per million)

- Four drivers: turns, cache reads, output tokens (thinking is billed as output), model [What does a task cost?].
- Worked example: context growing from 20K to 120K over 40 turns is about 2.8M input tokens; with 90% from cache the input costs about $1.62; in 25 turns, about $1.02. "So the cheapest turn is the one you don't need." [Turns].
- "On Opus 5.5, an output token costs 100 times a cache read." 60K output tokens of a typical task cost $1.20 [Output tokens].
- Illustrative session (2.0M cache read, 200K fresh input, 60K output): $3.50 on Opus 5, $2.40 on Opus 5.5 (fig. B and C text, `` copy).
- Typical spend from the costs docs: about $13 per developer per active day on average across enterprise deployments; under $30 for 90% of users [The rest of the bill].
- Fast mode: up to 2.5 times faster at twice the price ($8 / $40), billed to usage credits on a subscription [The rest of the bill].
- Batch API: half price on input and output [The rest of the bill].
- Escalation trigger: "If Opus 5.5 on xhigh hits the same problem twice, switch, and switch back once it's solved." (written for Fable 5.1; MODEL updates the target to Fable 5.2) [Moving up to Fable 5.1].
- "Move down to Sonnet or Haiku for lookups, not for writing code"; for a mechanical edit across many files keep Opus 5.5 and set effort to low [Moving down for lookups].
- Hill-climb example: a support benchmark went from Opus 4.8 at high (74.4%, 4.6 cents per ticket) to Sonnet 5 at low with an improved prompt (98.9% on the search set at about 1 cent); on 14 held-out tickets, 90.5% against 78.6% at about one fifth of the cost (EVAL [Hillclimbing for cost reduction]).

Measuring your own (COST [Measure it yourself], [Reading a session]; MODEL [Measure on your own work])

- `/usage` (same as `/cost`) after a task; check cache share, output against input, and total input against conversation size (many times larger means many turns; read the transcript for the repeated loop).
- Run one backlog task on two models or two effort levels and compare; do three or four tasks before concluding.
- For a formal comparison: sample real tasks with an outcome check each, run each candidate at two or three effort levels in separate sessions, plot score against spend.

### (h) How Anthropic reviews code internally (REVIEW, 2026-10-15)

- Goal: minimum human review time that does not raise reverts or incidents. Result claimed, June to September: "merged pull requests to Claude Code's codebase more than doubled while the share that had to be reverted fell by more than 40 percent" [intro]. Claude writes about 90 percent of Claude Code's code [intro].
- Reframing: the question is which check, automated or human, catches what could go wrong, not whether a human read the code. "Now, review runs continuously, more like spellcheck while you write." [Rethinking the purpose of code review].
- Target: most PRs merge with at most one human in the loop, who can be the author. Measured by human approvals per PR (median and p95), human comments and wait time on a person, with revert and incident rates as the guardrail [The scarce resource: human time and attention].

Seven layers [Layer by layer]

1. Verified before anyone else looks. Give Claude something to run and "ask it to show the output instead of saying it's done". "Then a subagent reviews the diff with fresh context." Then internal skills: a bug hunter, a diff simplifier, an end-to-end behaviour check; UI changes are checked against design guidelines. Boris Cherny's estimate, as reported: verification makes the result two to three times better.
2. AI review on every PR, against the whole repo and the PR's stated intent; on a bug fix it looks for the root cause. Several agents look for bugs in parallel, a separate group votes on each finding, "it only gets posted if enough of them agree it's real", and findings that are only style, diagnostics or cleanup are dropped (filters A/B tested). Comments are tagged Important, Nit or Pre-existing. Every finding must be fixed or resolved with a reason. Depth per repo: Quick, Standard or Deep.
3. Security review that can block: no merge while a bug or security finding is open; `/security-review` or the open-source GitHub Action.
4. Blocking automated checks: lint, types, tests on every platform, build; the PR template asks how the change was tested and how to undo it.
5. Human approval scaled by risk. Low (docs, copy, internal-only, additive behind a flag): none once automated checks are green. Medium (ordinary product changes; sensitive areas such as caching, the auto-updater, system prompts): one person. High: two. "The change sets the tier, not the author." Two classifiers set the tier and whether another person is needed; CI workflow files and owner-listed paths always need a person. "An agent's approval never counts as a person's, either." The person who prompted an agent-written PR counts as a reviewer and is accountable. An approval covers one commit.
6. Merge queue re-runs checks against main; new behaviour ships behind a flag to employees first; `latest` channel before `stable`.
7. Fast detection and rollback: flags off without a deploy, weekly on-call, incident reviews that ask which layer should have caught it. Gap admitted: no circuit breakers yet that tighten approval when revert numbers move.

Instruction files for review [1. The work is verified before anyone else looks]

- `CLAUDE.md`: what the project is (stack, conventions, goals, non-goals). Every review loads it, so it is kept short and points to other docs. The reviewer flags code that breaks a convention in it and changes that make a line in it stale.
- `REVIEW.md`, written by code owners. Good ones are short: "They say what failure looks like in that repo" (for docs "it lies", for config "it misroutes"), cap the nits, list paths to skip, require a file and line as evidence, and ask for a summary that starts with a count and says plainly when there is nothing to fix.
- Repeated reviewer flags are fixed at the source: in the skill, with a lint rule, or in these files.

Improving the reviewer [How we make the reviewer better]

- "Any incidents are now an eval." Past incident-causing PRs with their fixes, confirmed by engineers, run daily against the reviewer.
- Noise is measured by what people do with each comment (fixed, said wrong, intentional, did not matter) and by running the reviewer on known-clean PRs.
- "Noise costs more when the author is an agent.": a person waves a nit off, an agent fixes it and triggers another round.
- Convergence: one PR went through more than fifty review-fix rounds overnight; "about 59% of it was code that had been there since the reviewer's first pass". Changes: "After three rounds, the reviewer asks the author to step back and reconsider the approach."; diff-only re-review after the first few passes; flag the class of bug; no repeats. Rounds-to-pass is tracked alongside recall.
- Review agents also run nightly over existing code.
- Launch-time figure: the share of internal PRs with substantive review comments "went from 16% to 54%" [2. AI review on every pull request].

What stays human [Where humans stay in the loop]: whether to build it; risky code (billing, auto-updater, CI workflows); architecture that sets a pattern; reading the evidence, "If you can't say what the checks would miss, ask for a real review rather than a quick approval."; owning the outcome.

Understanding without reading diffs [Sharing context across the team]: ask Claude for an explainer of exactly the slice you are about to change, or a small HTML artifact; "reading trivial diffs line by line" teaches little.

Adoption list [How you can adopt this process], the parts a solo developer can use: checks the agent can run listed in a short `CLAUDE.md`, plus hooks that run formatters and linters; `/code-review` and `/security-review` locally or a fresh-context subagent review; a `REVIEW.md` that absorbs repeated review comments; required CI and a PR template with "Testing", "Risk" and "How to revert"; review effort matched to risk; a cap on review rounds with diff-only re-review; never letting a bot's approval replace a required human's; incidents and reverts turned into an eval set and re-scored "whenever its prompts, tools or model change".

Related: a review prompt for a single developer, "List only problems you'd block the merge for." with file and line, why it is wrong and how to show it fails (OPUS [Ask it to review the code]); an early tester's claim that Opus 5.5 at its lowest effort caught more bugs than Opus 5 at high, with fewer false alarms (OPUS, same section; anecdotal).

### (i) Eval design and hill-climbing a solo developer can apply (EVAL, 2026-09-28)

Designing the eval [Eval design]

- Four properties: tasks mirror production; scores rise with stronger models and more effort (if not, suspect ambiguous tasks or the grader); headroom at the frontier (the best model at top effort well below 100%); low run-to-run variance.
- A task that fails every run regardless of replicates is probably impossible or ambiguous. A good task is one where two experts would agree and "everything the grader checks is stated in the task".
- Variance hides in configuration (effort not applied consistently) and in leftover state from earlier trials (a file, git history) that hands the agent the answer.
- Do not sample cases because today's model fails them; that measures one model's failure fingerprint. "Pick hard cases because a human judged them hard", and be able to say why before including it. Do not trust user traffic blindly; it can skew easy [Adversarial sampling].
- Input sources in priority order: production transcripts; bug reports and tickets; five to ten hand-written cases; cases synthesised from the codebase [Designing examples]. Review every input on a generated page before running.

Grading [Validating the grader]

- Use the cheapest grader that fits: code checks for constrained outputs (exact match, label from a set, schema, passing tests); an LLM judge for open-ended outputs with "a rubric written as checkable claims (not a 1-to-5 scale)".
- With a baseline, the judge compares both outputs blind, in random order. The judge model "should not be the model you are testing".
- Read scored transcripts before trusting the grader: "scoring failures are among the most common ways an evaluation is misconfigured".
- Diagnostics on the baseline run: grade the same output twice and see if the verdict changes; check for timeouts, API errors and cut-off answers; if the baseline is already about 95% or higher, climb on cost or latency instead of quality [Diagnostic checks].
- Outputs kept: cases, grader, runner, one JSON line and one full transcript per case, a page linking each score to its transcript; scores come with a confidence interval.

Hill-climbing [Hillclimbing], [/claude-api hillclimb]

- Good targets are cheap to change and revert (prompts, skills), attributable (skill trigger rate against the description), and well scoped. Cost at equal quality is a strong objective even on a saturated eval.
- Overfitting defences: split into a train set the climber may read and a test set it never sees; "Never paste failures into the prompt"; keep answers structurally out of reach.
- Before round one, confirm the eval's noise is smaller than the smallest improvement you would act on; otherwise add repetitions or cases.
- Each round: read the previous round's train transcripts, propose one change as a patch that fixes the failing behaviour at its root (rewrite the section, add the missing rule) instead of rewording a line. Keep it only if train and test both improve; revert on train-only gains or any regression.
- When the score stalls for two or three rounds, stop editing and sort every remaining failure by cause; this catches ambiguous cases, harness errors and variance. "Tasks that never improved in performance despite addressing obvious content gaps are tells that the example or grader is flawed." [Hillclimbing for performance improvement].
- Finish at the version that did best on test; "If the gain is within noise, it says so and recommends against merging."
- Commands: `/claude-api build-eval` and `/claude-api hillclimb` (the `claude-api` skill ships inside Claude Code). Surfaces it can change: system prompt, skills or instruction files, tool descriptions, model, effort and API parameters, harness code.

Results reported [Examples]

- Cost: 44 tickets (30 search, 14 held out). Opus 4.8 at high: 74.4%, 4.6 cents per ticket. After a prompt audit and Opus 5.5 at low: 87.8%, 1.9 cents. Sonnet 5 at low: 88.9%, about 1 cent. With routing rules and a cross-reference added: 98.9%. Held-out: 90.5% against 78.6% at about one fifth of the cost.
- Quality: the `claude-api` skill, 66% to 74% (eight missing features added), 77% (type-table errors fixed), 80% (a remembered-form to current-form table near the top), about 88% (two flawed eval tasks repaired plus more edits).

Lighter-weight variants from other posts

- A workflow can act as a small eval: run variants in worktrees and have comparison agents grade against a rubric (WF [Evals]).
- Log skill invocations with a PreToolUse hook to find under-triggering skills (SKILLS [Measuring skills]).
- Turn incidents and reverts into the reviewer's eval set and re-score on every prompt, tool or model change (REVIEW).
- Every benchmark must prove it tracks the real goal or be removed; proven ones become CI ratchets (FAST [Anything can be hill climbed]).

Inference for a solo developer: the minimum viable version is a handful of real past tasks per skill or prompt, split into train and held-out, a code check where possible, one change per round, and reverting anything that only improves the cases you looked at.

### (j) HTML output (HTML, 2026-05-20; one author's stated personal practice)

- Claim: markdown has become restrictive for agent-to-human output; "I find it difficult to read a Markdown file of more than a hundred lines" [intro]. HTML carries tables, CSS design data, SVG illustrations, code, interactions, workflows, spatial layouts and images [Information density].
- Why [Why use HTML?]: information density; easier reading through tabs, illustrations and links, including on mobile; a shareable link; two-way interaction (sliders, knobs, a copy-back-into-prompt button); and Claude Code's access to local context (files, MCPs, browser, git history) when generating it.
- How: just ask. Prompt it to "make an HTML file" or an HTML artifact; decide what the artifact is for; turn recurring patterns into a skill later [Getting started].
- Use cases [Use cases]: specs, planning and exploration (several options in a grid with trade-offs; an implementation plan with mockups, data flow and key snippets); code review and understanding (the real diff with margin annotations colour-coded by severity); design and prototypes (sliders for animation parameters with a copy button); reports and explainers (SVG diagrams, annotated snippets, a gotchas section); custom throwaway editors (ticket triage board, feature-flag form, prompt tuner).
- Rule for editors: "The trick is always to end with an export", a copy-as-JSON, copy-as-prompt or copy-diff button that feeds back into Claude Code [Custom editing interfaces].
- Workflow: a web of HTML files instead of one plan (explorations, mockups, then an implementation plan), handed to a fresh session to implement and to the verification agent as context; kept as references afterwards [Specs, planning, and exploration], [Is this how you've replaced planning?].
- Cost: "While Markdown often uses fewer tokens", he judges the expressiveness and the higher chance of actually reading it worth it; with a 1M context window the extra tokens are "not really noticeable" [Isn't it less efficient?].
- Motive: "it helps me feel much more in the loop with Claude" [Staying in the loop with Claude].
- Caveat in the byline: the post "expresses his personal opinions"; he calls himself "far on the HTML maximalist side".
- Echoes: HTML artifacts as references and HTML mockups over descriptions or screenshots (CTX [Now: Rich references], [References]); explainers and small artifacts in place of reading trivial diffs (REVIEW [Sharing context across the team]); the eval skill generates static local pages for input review and results (EVAL [Designing examples], [Validating the grader]).

### Contradictions and open questions

- Sonnet 5.5 cache-read price: SONNET's table lists $0.20 and its text says a read "costs a tenth of the input price" ($0.20); MODEL's table and text say $0.10. Unresolved; check the pricing docs.
- Explore subagent model: CACHE (April) says Claude Code's Explore agents use Haiku; MODEL (November) says the built-in Explore now runs on the session's model and tells you to define your own `Explore` with `model: haiku`. The later post supersedes.
- Switching models mid-session: CACHE says "Don't change tools or models mid-conversation" and to use subagents with a hand-off; COST and MODEL accept switching at a natural break after `/compact` or in a fresh session, and COST even recommends switching up and back for a hard step. These agree on cost mechanics but differ in tone; the switch-and-switch-back advice pays two cache writes.
- Effort and the cache: EFFORT and COST say effort changes keep the cache on Opus 5.5 with an API key or subscription, but not on Bedrock, Google Cloud's Agent Platform or a gateway. SONNET says changing top-level effort on the API invalidates the cache and points to per-message effort (beta). The behaviour is platform- and model-specific.
- Mid-conversation tool changes: CACHE says never; SONNET lists "mid-conversation tool changes (beta)" as a new API feature without stating the cache effect; COST says connecting an MCP server mid-session causes a cache write. Open question whether the beta is cache-safe.
- Examples: CTX says examples constrain current models; SKILLS (seven weeks earlier) recommends folders of reference snippets and examples inside skills and an `internal-platform-cli` skill "with examples on when to use them". Possible reconciliation (inference): examples as on-demand reference material are fine, examples in always-loaded tool or system prompts are not.
- Rules versus judgement: CTX argues for deleting rules; OPUS adds a `CLAUDE.md` stop rule, SONNET adds a system-prompt paragraph requiring a real check at low effort, REVIEW relies on `REVIEW.md` with caps, and OPUS finds specific negative lists work for design. Reading them together (inference): add a rule for an observed, recurring failure; do not add prophylactic ones.
- Review depth: SKILLS describes `adversarial-review` iterating "until findings degrade to nitpicks"; REVIEW found unbounded rounds mostly resurfaced old code and now caps at three. The later post is the safer default.
- Memory: CTX says auto-memory replaced hand-saving to `CLAUDE.md`; WF and REVIEW still distil recurring corrections into `CLAUDE.md`; CLOUD says personal `~/.claude` does not reach cloud sessions. Open question: where auto-memory is stored and whether it travels.
- Plans: CTX and HTML favour HTML artifacts over markdown plans; CLOUD commits a markdown plan (`docs/migration-plan.md`), OPUS keeps `TASKS.md`, COST suggests "a short written plan" for a fresh session. Not in conflict if HTML is for human review and a plain file is for run state; the posts do not say this.
- Effort for implementation: within EFFORT, the author implements on low in his feature loop but lists Medium for "most of my regular software engineering work"; COST reserves low for mechanical work. The level depends on how closely the developer is in the loop.
- Fable versions: COST and EFFORT refer to Fable 5.1 ($10 / $50, cache read $0.25); MODEL covers Fable 5.2 ($8 / $40, cache read $0.20). Use MODEL's numbers.
- Multi-agent scale: TEAMS shows 1,000 agents succeeding with minimal structure; MODEL says to skip orchestration when work fits one context window; COST prices agent teams at about seven times a normal session. TEAMS is a research result on a mechanically checkable task, not a recommendation.
- Judge independence: EVAL says the judge should not be the model under test; REVIEW's voting reviewers and WF's verifier agents do not say which model verifies. Open question whether a different model is used for verification.
- Effort level names: EFFORT's rule of thumb lists Low, Medium, High, Max; COST and SONNET list `low`, `medium`, `high`, `xhigh`, `max`.
- Not covered by this batch: emphasis words and role prompts (see (b)); hooks configuration beyond SessionStart, PreToolUse in skills and formatter or linter hooks named in REVIEW; permissions design beyond the advice in OPUS to keep permission prompts on for destructive commands.

## Per source

### SKILLS: Lessons from building Claude Code: How we use skills (Thariq Shihipar, 2026-06-03)

File: `refs/articles/claude.dev/blog-lessons-from-building-claude-code-how-we-use-skills/article.md` (headings: same path with ``)   URL: https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/

Thesis: Skills are folders, not markdown files, and the effective ones use scripts, data, config and hooks. Anthropic's hundreds of internal skills cluster into nine categories, and a skill should fit one. The value is in gotchas, progressive disclosure and trigger-oriented descriptions.

Practices: the full taxonomy and advice is in cross-cutting section (a). Points worth repeating:

- Fit one category; straddling confuses the agent [Types of skills].
- Invest first in verification skills; pair with playwright or tmux, record video, assert state at each step [2. Product verification].
- Automation skills should save previous results to log files so the model stays consistent across runs: "saving previous results in log files can help the model stay consistent" [4. Business process and team automation].
- Run quality skills automatically from hooks or a GitHub Action, with deterministic scripts for robustness [6. Code quality and review].
- Write only what moves Claude off its defaults; grow a Gotchas section from real failures [Don't state the obvious], [Build a gotchas section].
- Tell Claude which files exist in the skill folder (`references/`, `assets/`, scripts, examples) [Use the file system and progressive disclosure].
- State goals and constraints, not every step [Avoid railroading Claude].
- `config.json` in the skill folder for per-user setup; `AskUserQuestion` for structured questions [Think through the setup].
- Description states when to trigger, with trigger phrases [Write descriptions for the model, not for humans].
- Persist data via `${CLAUDE_PLUGIN_DATA}` [Help Claude remember].
- Ship helper libraries Claude composes into one-off scripts [Store scripts and generate code].
- Session-scoped hooks registered by a skill, such as `/careful` and `/freeze` [Use on-demand hooks].

Evidence and numbers: "hundreds" of skills in active use; nine categories; no measured effect sizes. Verification skills are said to have the most measurable impact without a figure.

Tools and files named: `SKILL.md`, `./.claude/skills`, `references/api.md`, `assets/`, `config.json`, `standups.log`, `${CLAUDE_PLUGIN_DATA}`, `AskUserQuestion`, PreToolUse hook, plugin marketplaces, `frontend-design` skill, playwright, tmux, `/careful`, `/freeze`.

Caveats: "Skills best practices are still evolving." No native dependency management between skills. Every checked-in skill adds context. The example skills are mostly organisation-scale (Slack, Datadog, on-call); a solo developer will use fewer categories.

Relevance: high. It is the most direct source for which skills to build and how to structure them.

### CACHE: Lessons from building Claude Code: Prompt caching is everything (Thariq Shihipar, 2026-04-30)

File: `refs/articles/claude.dev/blog-lessons-from-building-claude-code-prompt-caching-is-everything/article.md`   URL: https://claude.dev/blog/lessons-from-building-claude-code-prompt-caching-is-everything/

Thesis: Long-running agents are only affordable because of prompt caching, which is a prefix match, so the whole harness is ordered and designed around keeping the prefix stable. Features such as plan mode, tool search and compaction are shaped by that constraint.

Practices:

- Order content "static content first, dynamic content last": system prompt and tools, then `CLAUDE.md`, then session context, then messages [Lay out your prompt for caching].
- Watch for accidental prefix changes: timestamps in the system prompt, non-deterministic tool order, changed tool parameters [same].
- Put updated facts in the next message (a `<system-reminder>` tag), not in the system prompt [Use messages for updates].
- Do not switch models mid-session; delegate to a subagent with a hand-off message [Don't change models mid-session].
- Never add or remove tools mid-session; model state changes as tools (`EnterPlanMode`, `ExitPlanMode`) [Never add or remove tools mid-session], [Using Plan Mode to design around the cache].
- Defer tool schemas with `defer_loading: true` stubs and tool search instead of removing tools [Use tool search to defer instead of remove].
- Run compaction and other side computations as forks that share the parent's exact prefix, and keep a compaction buffer [The solution: cache-safe forking].
- "Monitor your cache hit rate like you monitor uptime." [Lessons learned].

Evidence and numbers: Anthropic alerts on cache hit rate and declares SEVs. The compaction figure describes a forked call as "a cache hit at one tenth the price" returning "a summary of about 20k tokens" (fig. B alt). The example threshold is 100K tokens into an Opus conversation.

Tools and files named: `cache_control`, `CLAUDE.md`, `<system-reminder>`, Plan Mode, `EnterPlanMode`, `ExitPlanMode`, tool search tool, `defer_loading`, compaction API, Explore agents.

Caveats: written for harness builders; the user-facing consequences are spelled out later in COST. The Explore-uses-Haiku detail is superseded by MODEL. A bonus noted: because `EnterPlanMode` is a tool, the model can enter plan mode by itself on a hard problem.

Relevance: high. It explains why instruction files, tool lists and model choice should be stable within a session.

### SEE: Seeing like an agent: how we design tools in Claude Code (Thariq Shihipar, 2026-04-10)

File: `refs/articles/claude.dev/blog-seeing-like-an-agent/article.md`   URL: https://claude.dev/blog/seeing-like-an-agent/

Thesis: Tools should be shaped to the model's actual abilities, which you learn by reading its outputs and experimenting. As models improve, tools that once helped start to constrain, and new capability is better added by progressive disclosure than by new tools.

Practices: see cross-cutting section (d). Summary:

- Three attempts at elicitation ended in a dedicated, structured, blocking `AskUserQuestion` tool [Improving elicitation with the AskUserQuestion tool].
- Free-form output formats are unreliable as an interface to UI [Attempt 2: Changing output format].
- Revisit old tools: TodoWrite and its reminders were replaced by Tasks with dependencies shared across subagents [Updating with capabilities: tasks & todos].
- Let the model find context with search tools instead of pre-retrieving it [Designing a search interface].
- High bar for new tools; use skills, linked files and subagents to extend the action space [Progressive disclosure: the Claude Code Guide agent].
- A lookup subagent keeps the main context clean by returning only the answer [same].

Evidence and numbers: about 20 tools in Claude Code; reminders were every 5 turns; no quantitative evaluation.

Tools and files named: `AskUserQuestion`, ExitPlanTool, TodoWrite, Task tool, Grep, Agent Skills, Claude Code Guide subagent, Agent SDK.

Caveats: "an art, not a science"; the Guide subagent "isn’t a perfect solution (Claude can still get confused when you ask it about how to set itself up)". The author doubts the current elicitation tool is final. Oldest post in the batch.

Relevance: high. It gives the design reasoning for a project's own scripts, question flows and lookup subagents.

### CTX: The new rules of context engineering for Claude 5 generation models (Thariq Shihipar, 2026-07-24)

File: `refs/articles/claude.dev/blog-the-new-rules-of-context-engineering-for-claude-5-generation-models/article.md`   URL: https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/

Thesis: Context (system prompt, `CLAUDE.md`, skills, memory) was over-constraining newer models. Anthropic cut over 80% of Claude Code's system prompt with no measurable eval loss, and six earlier best practices are now described as myths with replacements.

Practices: the six then/now pairs are in cross-cutting section (b). In addition:

- Look for conflicting instructions across system prompt, skills and user requests; they cost thinking [Unhobbling Claude].
- `CLAUDE.md`: light, brief repo purpose, mostly gotchas, nothing obvious from the file system, references to skills for procedures [CLAUDE.md].
- Skills: lightweight guides, not over-constrained "except in highly important areas", split into many files, encoding what is particular to you [Skills].
- References: `@`-mention spec files, mockups or whole codebases; prefer code-form references [References].
- Run `claude doctor` or `/doctor` to right-size skills and `CLAUDE.md` [intro], [Try simplifying].
- System prompt work matters only when building your own harness [System prompt].

Evidence and numbers: over 80% of the system prompt removed "with no measurable loss on our coding evaluations". TodoWrite description cut from about 9,100 characters to a sentence plus an enum (fig. alt).

Tools and files named: `CLAUDE.md`, `SKILL.md`, `claude doctor`, `/doctor`, ToolSearch, deferred tools, Task tools, memory, artifacts, `@` mentions, the `#` hotkey (retired practice).

Caveats: applies to "models like Claude Opus 5 and Claude Fable 5"; older or smaller models are not addressed. No guidance on emphasis words or role prompts. The eval evidence is Anthropic's own coding evals, not shown.

Relevance: high. It sets the size and style rules for every instruction file in a setup.

### WF: A harness for every task: dynamic workflows in Claude Code (Thariq Shihipar and Sid Bidasaria, 2026-06-02)

File: `refs/articles/claude.dev/blog-a-harness-for-every-task-dynamic-workflows-in-claude-code/article.md`   URL: https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/

Thesis: Claude Code can write a task-specific multi-agent harness as a JavaScript workflow. This counters the laziness, self-preference and goal drift of one long context, at a higher token cost, so it suits complex, high-value, parallel or adversarial work.

Practices: see cross-cutting section (e). Summary:

- Know the six patterns and name them in the prompt [Helpful patterns when using dynamic workflows], [Prompting].
- Use isolated worktrees per fix and an adversarial reviewer before merging [Migrations and refactors].
- One verifier per rule plus a skeptic for rules Claude keeps missing [Memory and rule adherence].
- Mine past sessions for repeated corrections and distil verified ones into `CLAUDE.md` [same].
- Quarantine readers of untrusted content from privileged actions [Triaging at scale].
- Stop on a condition, not a pass count; add `/goal`, `/loop` and a token budget [Loop until done], [Combine with /goal and /loop], [Token usage budgets].
- Ask whether the task really needs more compute [When not to use dynamic workflows].
- Save reusable workflows to `~/.claude/workflows` or a skill, as templates [Saving and sharing dynamic workflows].

Evidence and numbers: Bun's Zig-to-Rust rewrite is cited as done with workflows (linked thread, not detailed). Panel figure: 14 agents, 482k tokens, 6m 12s for a review; 22 agents, 1.1M tokens, 11m 3s for deep research (fig. alt). No controlled comparison with single-agent runs.

Tools and files named: `agent()`, `parallel()`, `pipeline()`, `ultracode`, `/deep-research`, `/loop`, `/goal`, `AskUserQuestion`, `claude -p`, Claude Agent SDK, worktrees, `~/.claude/workflows`, `SKILL.md`.

Caveats: "best practices are still developing"; "Workflows are new"; written when Opus 4.8 was current. Token use is significantly higher.

Relevance: high for knowing when not to reach for multi-agent, and for the rule-verifier and session-mining recipes; medium for daily use.

### AUTO: Building effective agent automations (Lance Martin and CJ Avilla, 2026-10-08)

File: `refs/articles/claude.dev/blog-building-effective-agent-automations/article.md`   URL: https://claude.dev/blog/building-effective-agent-automations/

Thesis: Scheduled background agents fail quietly: they lose a source, repeat or skip items, or ignore changed preferences. A reference daily-brief agent on Claude Managed Agents shows six rules that prevent this.

Practices: the six rules and the safety reasoning are in cross-cutting section (e). In addition:

- Keep run records (`runs/<date>.md`) with states "posting", "posted" with message id, or "maybe posted" [Confirm the post landed before recording it].
- Decide what earns a line: something the reader would act on today or that changes a decision; "When unsure, leave it out." [Keep the brief short].
- Copy links from the source's own link field, never assemble them by hand [Re-check anything still open right before posting].
- Keep source-behaviour notes in agent state (for example a source that "returns only the newest 50 items") [Memory].
- Disable unused built-in tools (`web_search`, `web_fetch`) in the agent config [Agent].
- Test a deployment by hand with `ant beta:deployments run --deployment-id <id>` [Schedule].

Evidence and numbers: cron `32 7 * * 1-5`; budget `"500"` cents; cap at three to five times a normal run. No outcome measurements.

Tools and files named: Claude Managed Agents (beta), `ant apply`, `agent.md`, `deployment.md`, `environment.yaml`, `memory_store_preferences.yaml`, `memory_store_state.yaml`, `vault.yaml`, `claude-lock.json`, `bookmarks.json`, `ledger.md`, `/mnt/memory/`, `scripts/seed-preferences.sh`, `always_allow`, `budget_reached`, `claude-api` skill.

Caveats: platform-specific and beta. The Slack token both reads and posts, which the authors flag as the exception to read-only. A planted instruction can still alter the brief's content.

Relevance: medium. The six rules transfer to any scheduled agent or `/loop` job; the platform files do not.

### REVIEW: How the Claude Code team does code review (Addy Osmani, Morgan Westlee Lunt, Qing Wang, 2026-10-15)

File: `refs/articles/claude.dev/blog-solving-code-review-at-anthropic/article.md`   URL: https://claude.dev/blog/solving-code-review-at-anthropic/

Thesis: At agent-produced volume, line-by-line human review is not feasible, so the team moved most reading to machines in layers, kept human approval scaled to risk, and invested in fast rollback. The target is minimum human time with no rise in reverts or incidents.

Practices: the full process is in cross-cutting section (h). Most transferable to one developer:

- Verify, then fresh-context subagent review, then bug-hunt, simplify and end-to-end skills, all before a PR [1. The work is verified before anyone else looks].
- Short `CLAUDE.md` plus a `REVIEW.md` that states what failure looks like, caps nits, lists skip paths and demands file-and-line evidence [same].
- Fix repeated findings at the source: skill, lint rule or instruction file [same].
- Tag findings Important, Nit or Pre-existing; drop style-only findings [2. AI review on every pull request].
- Cap review rounds at three; re-review only the new diff; flag bug classes; no repeats [How we make the reviewer better].
- Turn incidents into an eval set for the reviewer [same].
- PR template: how tested, how to undo [4. Automated checks that block].
- Read the evidence, not the diff, for low-risk changes; ask Claude for an explainer of the module you are about to change [Where humans stay in the loop], [Sharing context across the team].
- Raise a change of direction early in the thread, not as a blocking comment on a finished PR [When we change direction].

Evidence and numbers: merged PRs more than doubled June to September while the reverted share fell more than 40 percent; monorepo changes per day from about 2,500 in May to more than 30,000 in September; substantive review comments on 16% then 54% of internal PRs; more than fifty rounds on one PR; about 59% of repeated flags were pre-existing code; verification estimated to make results two to three times better (attributed estimate).

Tools and files named: `CLAUDE.md`, `REVIEW.md`, `/code-review`, `/security-review`, Code Review for Claude Code (Quick, Standard, Deep), Claude Code GitHub Action, CODEOWNERS, branch protection, merge queue, feature flags, `latest` and `stable` channels.

Caveats: team-scale mechanisms (trusted-author lists, two-person rules, on-call) do not apply to one person. No circuit breakers yet. The headline numbers are before-and-after, not controlled.

Relevance: high. It is the template for a pre-PR review pipeline and a `REVIEW.md`.

### EFFORT: Using Claude Code: Spending your effort (Thariq Shihipar, 2026-09-25)

File: `refs/articles/claude.dev/blog-spending-your-effort/article.md`   URL: https://claude.dev/blog/spending-your-effort/

Thesis: Effort mostly controls how much verification, edge-case testing and independent judgement Claude applies. Higher effort pays off on tasks with hidden edge cases and little human supervision; it does not rescue a wrong approach.

Practices: see cross-cutting section (g). Summary:

- Low for sketches and iteration with you in the loop; max for a best one-shot [Underspecified build task], [Lightly specified design task].
- A detailed spec narrows the difference between levels [Highly specified build task].
- Loop: interview, implement on low, review, verify on high [Takeaways].
- High for brownfield bug fixes; max for autonomous build-and-verify or security work [When to use different effort levels in Claude Code].
- Change effort mid-conversation with `/effort` [same].

Evidence and numbers: per-task results at 5 attempts each and the category and failure-mix figures listed in (g). What high effort actually did in traces: reproduced the crash first, wrote randomised tests against a reference, checked tests failed on half-finished fixes, fuzzed, timed large inputs, tried two data-prep methods and investigated the disagreement.

Tools and files named: `/effort`, `/config`, Terminal-Bench 3.0, Opus 5.5, Fable 5.1.

Caveats: build examples are called "toy examples". Benchmark numbers are internal, 5 attempts per task, with production safety interventions off for Fable 5.1 and no internet on security tasks, so they "won’t line up with the public leaderboard" [footnote]. Failure kinds were labelled by a model judge and are approximate. Fable 5.1 is now superseded by 5.2.

Relevance: high. It gives a behavioural model of effort that maps directly to per-task and per-skill effort choices.

### OPUS: Getting the most out of Opus 5.5 in Claude and Claude Code (Addy Osmani, 2026-09-22)

File: `refs/articles/claude.dev/blog-getting-the-most-out-of-opus-5-5/article.md`   URL: https://claude.dev/blog/getting-the-most-out-of-opus-5-5/

Thesis: Opus 5.5 works longer unattended, reports plainly and always thinks, so prompts should hand over a whole task with a finish line, drop thinking instructions, and steer stops and reporting through `CLAUDE.md`.

Practices:

- "Give the whole task in one message. Name the finish line" and say when to stop and ask [Say what "done" looks like, then let it run].
- Delete "think carefully" and similar; say "Answer directly." for a quick answer [Stop telling it to "think hard"].
- Type follow-ups while it works instead of restarting [Add to a running task].
- For design, list the specific styles to leave out; iterate the list [For design work, name the styles you don't want].
- `CLAUDE.md` stop rule, given verbatim in the post: "When a step doesn't need my input, keep going. Put status notes in the same message as your next action." followed by stopping only when blocked or before anything destructive. Keep permission prompts on for destructive commands [Tell it which stops you want].
- For pair programming, ask for the opposite: a one-line plan first and a short recap [same].
- Split audits and migrations across subagents and check each one's evidence [Ask it to split big work across subagents].
- Keep the task list in a file (`TASKS.md`); "A list in a file survives that" (compaction) [Keep the task list in a file].
- Read what it needs from you first; set the summary format in `CLAUDE.md`, for example three headings "Blocked on me, Changed, Found" [Read what it needs from you first].
- Have it review the diff before a person does, listing only merge-blocking problems with file, line, reason and a way to show the failure [Ask it to review the code].
- Ask it to mark what it could not confirm and where it looked [Ask it to mark what it couldn't confirm].
- Do not ask it to reproduce its reasoning [Don't ask it to show its reasoning in the reply].
- `/fast` for back-and-forth work [Turn on fast mode when you're waiting on each reply].

Evidence and numbers: mostly tester reports. Removing a think-carefully line started replies sooner with no clear quality drop (Anthropic's testing in a chat product). One tester: lowest effort on Opus 5.5 beat Opus 5 at high on bug-catching.

Tools and files named: `CLAUDE.md`, `TASKS.md`, `/model`, `/config`, `/feedback`, `/fast`, the setting "Switch models when a message is flagged".

Caveats: safety classifiers can flag legitimate work and switch the session to an older model; the check covers everything in the conversation including files and search results [5. When a message is flagged]. Opus 5.5 "sometimes stops to report instead of going on". The settled-answers instruction should be left out of long analysis projects.

Relevance: high. It supplies ready wording for the stop, reporting and review parts of a `CLAUDE.md`.

### MODEL: Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku (Addy Osmani, 2026-11-09)

File: `refs/articles/claude.dev/blog-which-claude-model-should-you-build-with/article.md`   URL: https://claude.dev/blog/which-claude-model-should-you-build-with/

Thesis: Start most work on Opus 5.5 at medium; adjust effort before model; move down for scoped or high-volume work and up to Fable 5.2 for the hardest or longest unattended work. Token price is not task cost, so measure cost per finished task.

Practices: see cross-cutting section (g) and the delegation list in (f). In addition:

- Price the hardest tasks in a set, not only typical ones [Capability and cost per finished task].
- For replies a person waits on, Sonnet 5.5 at `low` or `medium` [Latency against accuracy].
- "a lean main context matters more the bigger the main model is"; let cheaper subagents do the verbose reading [Context against cost].
- Moving down a tier loses earlier reasoning because a model never reads thinking blocks from a model above it; a move from Fable 5.2 to any other model drops its reasoning [Switch at a natural break].
- Example subagent file `.claude/agents/log-reader.md` with `tools: Read, Grep, Glob, Bash` and `model: haiku` [Put subagents on smaller models].
- If several models share a system, build for the strictest: append-only history, `tool_choice: auto` with strict tools, read content blocks by `type` [Check compatibility before migrating].

Evidence and numbers: prices and benchmarks in (g). Fable 5.2 generates up to 30% faster than 5.1; Sonnet 5.5 runs 30% faster than Sonnet 5. Cache read per turn about $0.03 at 150K and $0.004 at 20K. Haiku 5.5 costs a twentieth of Sonnet's input price on short prompts.

Tools and files named: `/effort status`, `/model`, `/usage`, `/compact`, `.claude/agents/log-reader.md`, `CLAUDE_CODE_SUBAGENT_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`, `opusplan`, advisor tool (beta), multiagent orchestration in Managed Agents, `between_tools`, `computer_toolset_20260801`, Claude Code v2.1.293 (for the `haiku` alias resolving to Haiku 5.5).

Caveats: benchmark figures are Anthropic's. On Bedrock, Google Cloud, Foundry and Claude Platform on AWS the `haiku` alias still resolves to Haiku 4.5. Forced `tool_choice` returns a 400 on Sonnet 5.5, Opus 5.5 and Fable 5.2. Fable 5.2 rejects requests whose history before a thinking block changed. Safety classifiers can re-run a flagged request on an older model.

Relevance: high. It is the current, dated source for default model, effort and subagent model settings.

### TEAMS: Safely scaling multi-agent teams with Claude Fable 5.2 (Barry Zhang, Tianyi Peng, Elle Najt, Keller Scholl, Lance Martin, 2026-11-09)

File: `refs/articles/claude.dev/blog-safely-scaling-multi-agent-teams-with-fable-5-2/article.md`   URL: https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/

Thesis: A team of 1,000 agents on an early Fable 5.2, given only general tools, a shared database and a lead-and-helpers hierarchy, organised itself and reproduced a formal proof in 28.7 hours inside layered safety controls. The authors read it as evidence that ambitious long-horizon work is possible within designed boundaries.

Practices: see cross-cutting section (f). Summary:

- General primitives (Git, SQL, shell) can replace a domain-specific coordination platform for a capable model [Collaboration].
- Give each agent its own sandbox and branch; merge through a separate job [Sandboxing].
- Coordinate through shared durable state, not messaging [Sandboxing].
- Use a mechanical acceptance check (Lean's checker and a grader on main) [Harness].
- Layer sandboxing, a blocking classifier and offline monitoring; stop the team on a block until a person reviews [Safety].
- Counter early give-up with reminders or human encouragement [Prompting], [Conclusions].

Evidence and numbers: 28.7 hours; one-third the output tokens and one-seventh the proof length of the earlier run (11 days, about 6 billion output tokens, 13 million lines of Lean); 60 statements and 47 given lemmas; 19 lead reminders; crews of 16 to 17 growing to 46 to 139; 10 statements proved within about 70 minutes; 756 tasks written by 73 helpers by hour 5.6; 2,418 tasks up to 10 levels deep; more than a million tool calls with none blocked; 36,612 database writes and 311,734 reads by hour 30 (fig. alt); 54 of 60 statements proved in the final count (fig. 6 caption).

Tools and files named: Lean 4, Mathlib, Prove2Me, Postgres, Git; tables announce, assign, notes, subtasks, landed.

Caveats: called a "toy experiment" throughout. The task is unusually decomposable and machine-checkable. The model had the earlier formalisation's 47 lemmas. The run was restarted near hour 18. Only the action-based monitor ran in this experiment. No cost in dollars is given.

Relevance: medium. The coordination and safety principles transfer; the scale and infrastructure do not.

### EVAL: Automating eval design and hillclimbing with Claude (Lance Martin, 2026-09-28)

File: `refs/articles/claude.dev/blog-automating-eval-design-and-hillclimbing/article.md`   URL: https://claude.dev/blog/automating-eval-design-and-hillclimbing/

Thesis: Good evals mirror production, respond to capability, have headroom and low variance; hill-climbing against them needs a held-out split and one attributable change per round to avoid overfitting. Both are packaged as `claude-api` skill commands.

Practices: see cross-cutting section (i). Summary:

- Sample from real traffic and tickets first; hand-write five to ten cases; review all inputs before running [Designing examples].
- Cheapest grader that fits; checkable-claim rubrics; blind pairwise judging against a baseline; a different judge model [Validating the grader].
- Diagnose grader stability, plumbing errors and headroom on the baseline [Diagnostic checks].
- Train and test split, one patch per round, revert train-only gains [/claude-api hillclimb].
- On a stall, classify remaining failures by cause before editing further [same].
- Climb on cost when quality is saturated [Hillclimbing].

Evidence and numbers: the two worked examples in (i). The illustrative inbox-routing eval has 24 inputs, a 0.681 baseline and a best variant at 0.875 on both splits (fig. alt).

Tools and files named: `/claude-api build-eval`, `/claude-api hillclimb`, `claude update`, `claude-api` skill (github.com/anthropics/skills).

Caveats: results come from internal benchmarks; the support benchmark is small (44 tickets, 14 held out). Open-ended harness changes are said to stall more often. The post is partly a product walkthrough.

Relevance: high for anyone maintaining skills and prompts; the method scales down to a handful of cases.

### HTML: Using Claude Code: The unreasonable effectiveness of HTML (Thariq Shihipar, 2026-05-20)

File: `refs/articles/claude.dev/blog-using-claude-code-the-unreasonable-effectiveness-of-html/article.md`   URL: https://claude.dev/blog/using-claude-code-the-unreasonable-effectiveness-of-html/

Thesis: For specs, plans, reviews, reports and one-off editors, HTML is a better agent-to-human format than markdown because it is denser, easier to read and share, and interactive. The author's real motive is staying engaged with Claude's choices.

Practices: see cross-cutting section (j). Summary:

- Ask for an HTML file or artifact; know what it is for [Getting started].
- Explore several options side by side with labelled trade-offs before planning [Specs, planning, and exploration].
- Review PRs through a rendered diff with severity-coded margin notes [Code review and understanding].
- Prototype interactions with sliders and a copy-parameters button [Design and prototypes].
- Build throwaway single-file editors that end in an export button [Custom editing interfaces].
- Keep the HTML files as references for implementation and verification sessions [Is this how you've replaced planning?].

Evidence and numbers: none measured; the argument is personal experience. Template gallery: thariqs.github.io/html-effectiveness and github.com/anthropics/html-effectiveness.

Tools and files named: HTML artifacts, Claude Design, Claude in Chrome, MCP servers (Slack, Linear), SVG.

Caveats: explicitly personal opinion; HTML costs more tokens; written when Opus 4.7 was current. HTML is harder to diff and hand-edit than markdown (inference; the post only notes he no longer edits these files himself).

Relevance: medium. Useful as an optional output practice for plans and reviews; not a required part of a setup.

### COST: What a task costs on Opus 5.5 (Addy Osmani, 2026-09-25)

File: `refs/articles/claude.dev/blog-what-a-task-costs-on-opus-5-5/article.md`   URL: https://claude.dev/blog/what-a-task-costs-on-opus-5-5/

Thesis: Task cost is set by turns, cache reads, output tokens and model, not token price alone. Every saving (lower effort, smaller model, less context) can cost a finished task, and "A retry costs more than those savings."

Practices: see cross-cutting sections (c) and (g). In addition:

- Give the model a way to check its work and start multi-file changes in plan mode [Keep in mind].
- Prefer one-pass context gathering and batched tool calls; each extra turn resends everything [Turns].
- Most days need three models: a small one for lookups, Opus 5.5 for supervised work, a bigger one for the hardest tasks [Choose the right model for your work].
- Run `/claude-api prompt-audit` on skills and `CLAUDE.md` after migrating models [Check your prompts when you migrate].
- Run `/mcp` and turn off unused servers [What loads before you type].
- Keep a long session moving so its cache stays warm [Keep in mind].
- Review any session that costs well above your own normal [Reading a session].

Evidence and numbers: listed in (c) and (g). Also: Opus 5.5 is 20% cheaper on input and output and 60% cheaper on cache reads than Opus 5 (input $5 to $4, output $25 to $20, cache read $0.50 to $0.20, fig. A alt); the "40% less to run" figure is an estimate that assumes fewer tokens per task; subscription limits go about 25% further.

Tools and files named: `/usage`, `/cost`, `/effort`, `/effort status`, `/model`, `/compact`, `/clear`, `/rewind`, `/autocompact`, `/mcp`, `/fast`, `/feedback`, `/claude-api prompt-audit`, `CLAUDE_CODE_SUBAGENT_MODEL`, `opusplan`, agent teams, Claude Code Analytics API, Usage and Cost API, Claude Code v2.1.280.

Caveats: "Some numbers here are list prices, and some are illustrations built from them." The dollar figure in `/usage` on a subscription is a guide, not a bill. The prompt-audit result is from one benchmark. Refers to Fable 5.1.

Relevance: high. It turns caching and effort into concrete session habits and gives the 200-line `CLAUDE.md` guideline.

### SONNET: Building with Claude Sonnet 5.5 (Addy Osmani, 2026-09-28)

File: `refs/articles/claude.dev/blog-building-with-claude-sonnet-5-5/article.md`   URL: https://claude.dev/blog/building-with-claude-sonnet-5-5/

Thesis: Sonnet 5.5 is the model for well-scoped everyday work with a clear spec and a check, at half Opus's token price. Most of the post is an API migration guide.

Practices:

- "Sonnet 5.5 fits best when the task has a clear spec and a way to check the result." [Choosing between Sonnet 5.5 and Opus 5.5].
- For agentic coding start at `medium` for well-specified tasks, `high` for harder or longer ones; use `xhigh` or `max` only where evals show a gain, otherwise consider Opus 5.5 [Re-run your effort sweep], [Model details].
- Remove Sonnet 5 workarounds and re-run evals [Remove Sonnet 5 workarounds].
- At `low` effort it "sometimes skips a check that exercises the change"; the post gives a system-prompt paragraph requiring a real check (tests, type-checker, build or the changed command) before reporting done, and saying which check was not run and why if none can run [Ask for real checks at low effort].
- Lower effort to reduce thinking; prompt requests to think less are unreliable [Re-run your effort sweep].
- In Claude Code: "The `default` model stays Opus 5.5, so switch with `/model sonnet` for well-scoped tasks." [In Claude Code].
- API: read content blocks by type; `between_tools` thinking; `tool_choice: auto` with `strict: true`; append-only conversations; per-message effort (beta) keeps the cache [Migrating from Sonnet 5], [Cache more of your prompt].

Evidence and numbers: 30% faster than Sonnet 5 and up to 30% cheaper for most work at unchanged token prices; $2 / $10; cache write $2.50 (5 minutes) and $4 (1 hour); 1M context; 128k output; minimum cacheable prompt 512 tokens; knowledge cutoff June 2026; images up to 2576 pixels on the long edge cost about 2.5 times the tokens of older models.

Tools and files named: `claude-sonnet-5-5`, `/model sonnet`, `/claude-api migrate`, `between_tools`, `thinking.display`, `stop_reason: "refusal"`, Claude Code v2.1.284.

Caveats: cache-read price disagrees with MODEL. Refusal categories (`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`) can decline legitimate requests. Largely API-level detail.

Relevance: medium. The model-fit rule and the real-check paragraph matter for a setup; the migration detail matters only when building on the API.

### CLOUD: Claude Code in the cloud: a field guide to cloud sessions (Addy Osmani, 2026-10-06)

File: `refs/articles/claude.dev/blog-claude-code-in-the-cloud/article.md`   URL: https://claude.dev/blog/claude-code-in-the-cloud/

Thesis: A cloud session gives each task a fresh VM, branch and scoped credential, so tasks run in parallel and unattended and end as a reviewable branch. It only works well if the repository itself carries the configuration and the means to verify.

Practices:

- Repo config travels, personal config does not: "`CLAUDE.md`, rules, skills, agents, and commands travel with the repo, and your `~/.claude` stays on your laptop." [Under the hood of a Claude Code cloud session].
- Move what is needed into the repo: skills and commands under `.claude/`, project MCP servers in `.mcp.json`, test commands in `CLAUDE.md` [Common questions].
- "Write each task as a self-contained ticket that states what's wrong, what done looks like, and how to prove it." [1. Clear a backlog in parallel].
- Split parallel tasks along file boundaries and expect sessions to report problems another session is fixing [Three tasks, one repository, three machines].
- Ask for heavy proof because the VM's CPU is not yours: run the suite 200 times, bisect across 50 commits [2. Let it prove the fix].
- Plan locally in plan mode, commit the plan, execute in the cloud, `claude --teleport` to finish locally [3. Plan at your desk, build in the cloud, finish in your terminal].
- Dependencies in a SessionStart hook in `.claude/settings.json` "so they run the same way locally and in the cloud"; check `CLAUDE_CODE_REMOTE` for cloud-only steps; machine tools in the environment's setup script [Give sessions what they need to check their own work].
- Narrowest network level that works; keep secrets out of shared environment variables [same].
- Run untrusted code (a contributor's PR, a new dependency's install script) in a cloud session, away from local keys [7. Run code you don't fully trust].
- "Name the command that proves the task is done, and read Claude's summary before the diff." One task per session; push before `claude --cloud`; commit as you go [Habits that pay off].

Evidence and numbers: three sessions ran 61, 65 and 72 seconds and finished within 87 seconds; the flaky-test session ran the suite 40 times with zero failures; VM about 4 vCPUs, 16 GB RAM, 30 GB disk; foreground command timeout 2 minutes by default, 10 at most; setup script should finish within about five minutes; cache rebuilds about every seven days; projects can start up to 200 threads a day.

Tools and files named: `claude --cloud`, `claude --teleport`, `/teleport`, `/tp`, `/tasks`, `/autofix-pr`, `/schedule`, `/web-setup`, `claude -p "<msg>" --cloud <session-id>`, routines, projects, Claude GitHub App, `.claude/settings.json`, `.mcp.json`, `CLAUDE_CODE_REMOTE`, `BASH_DEFAULT_TIMEOUT_MS`, `BASH_MAX_TIMEOUT_MS`, `Claude-Session` commit trailer.

Caveats: not available with a Console API key or third-party provider, or under Zero Data Retention. Sessions cannot reach local databases, VPN services or simulators. Even at network level None, requests go to the Anthropic API. Parallel sessions use plan limits in parallel. The demo repository is invented and was recreated from the prompt, which took a third to half of each run.

Relevance: high for template design: it is the reason project-level config must be self-sufficient.

### MODS: Getting started with Claude Code mods (Addy Osmani, 2026-10-01)

File: `refs/articles/claude.dev/blog-getting-started-with-claude-code-mods/article.md`   URL: https://claude.dev/blog/getting-started-with-claude-code-mods/

Thesis: A mod is a JavaScript or TypeScript module inside a plugin that hooks every session event, keeps state and can draw UI. It goes beyond settings hooks, and Claude Code can write one from a description.

Practices:

- Structure: a plugin with `.claude-plugin/plugin.json`, a `hooks/hooks.json` naming one module under `modules`, and a module exporting `register(on, options)` [How a mod works].
- A hook can observe (`await next(e)`), rewrite (`next({...e})`) or answer (`return { deny: "…" }`) [same].
- Difference from settings hooks: a settings hook "runs a shell command for each event and passes JSON over stdin and stdout"; a mod is loaded once, keeps state, draws UI and can register commands or tools [same].
- Describe the mod to Claude and allow hot reload; such a mod is session-only until copied out and installed [The shortcut: let Claude build it].
- Keep data in `$.state`, not module variables, because every save reloads the module [Step 3], [Four habits worth keeping].
- Validate and test with `claude plugin validate` and `claude plugin test` [Step 5: Validate and test].
- A command guard built as a mod "It's a safety net, not a permission system."; it reads command text, so `$(…)`, aliases and scripts get past. "Use permission rules for a hard block." [Blast Radius].
- Install mods like packages: "read the repo first and only install from people you trust" [Sharing your mod].
- Ideas listed: a cost or rate-limit meter, a `prompt.submit` hook that adds conventions to every prompt, a `tool.call` guard for production contexts [What will you mod?].

Evidence and numbers: Token Weather is about 80 lines; a hook gets 10 seconds of its own time per dispatch, not counting time inside `$` calls; requires Claude Code 2.1.287 or later.

Tools and files named: `.claude-plugin/plugin.json`, `.claude-plugin/types/`, `hooks/hooks.json`, `register`, `on`, `$.state`, `$.session.usage()`, `$.ui.resolve`, `$.ui.open`, `$.process.run`, `$.command.register`, `$.fs.read`, `claude --plugin-dir`, `claude plugin validate`, `claude plugin test`, `claude --debug`, `.claude-plugin/marketplace.json`, `/plugin marketplace add`, `/plugin install`, `/reload-plugins`, events `tool.call`, `ui.render`, `session.start`, `turn.start`, `turn.complete`, `command.run`, `prompt.submit`.

Caveats: "The API can change between releases." A mod runs with the same access as Claude Code. A `prompt.submit` hook that adds text to every prompt would add always-on context, which CTX argues against (inference). "Some of Claude Code's own features are built as mods, including AGENTS.md support and the `/diff` pane beside the conversation."

Relevance: medium. Optional for a project setup; relevant where a status readout or a soft guard is wanted, and for knowing that guards of this kind are not permission rules.

### FAST: How we made claude.ai 3x faster in two weeks (Raymond Wang, Sam Attard, Issac G, 2026-09-23)

File: `refs/articles/claude.dev/blog-how-we-made-claude-ai-faster/article.md`   URL: https://claude.dev/blog/how-we-made-claude-ai-faster/

Thesis: A two-week performance sprint run through Claude in one Slack channel made claude.ai about 3x faster. The central lesson is that once something is measurable, Claude can improve it, so the highest-leverage human work was finding deterministic things to measure and guarding the gains.

Practices:

- "With Claude, measuring something makes it tractable." Measurement becomes step one of the climb, not step zero [Anything can be hill climbed].
- Prefer deterministic metrics (instruction counts, React commits, style recalculations, layout shifts by named region) over noisy wall-clock time for lab loops and CI gates [same].
- Every benchmark has two jobs: a metric to move in the lab and a CI guardrail "that could only ratchet down"; a daily job lowers the ceiling when the count drops [same].
- Make each benchmark prove it tracks the real outcome or remove it: "we threw it out rather than let Claude climb the wrong hill" [same].
- The loop: thread on a slow spot, trace and build a benchmark, PRs sized for risk with user-visible changes behind a flag, watch the deploy, ratchet or turn the flag off, find the next spot [The loop, thread by thread].
- Prove a fix with repeated runs: red 20 of 20 on main, green 20 of 20 on the PR [same].
- Safety set up before the pace: automated review plus at least one human approval; "unit tests always came before optimizations, and anything that could cause a user-visible problem shipped behind a short-lived feature flag" [Guardrails].
- Clean up flags as a tracked task; classify each as kill switch or ramp [Guardrails].
- Human steering in three parts: ambition ("By default, Claude is careful about scope. It tickets findings, hedges on feasibility, and pads its estimates."), taste (a named owner rules on user-visible changes from before-and-after recordings), direction ("We kept each thread deliberately narrow, focused on one benchmark or journey") [Steering].
- Close threads at diminishing returns; one 900-line PR was rejected because 2ms was not worth the maintenance [Steering].

Evidence and numbers: p75 time to typeable page 3.1s to 0.55s; new Claude Code session 0.8s to 0.3s; Cowork cloud session 2.6s to 0.73s; more than three thousand changes merged "without a single customer-facing incident or rollback"; twelve of thirteen targets hit by day three; instructions cut 48% and 31% with wall-clock down 78% and 44%; more than 150 threads at a time; over two hundred changes on the busiest days; about a third of PRs added telemetry or guardrails; nearly two hundred flags, more than half cleaned up; streaming main-thread blocking about 750ms to about 200ms.

Tools and files named: Claude Tag (beta), Slack standing instructions, Datadog MCP server, Valgrind, `node --predictable`, Layout Instability API, feature flags, CI ratchets, jsdom.

Caveats: the model was an internal research model "roughly comparable to Opus 5.5". "The loop was productive, but it wasn’t autonomous." Team-scale, with human approval on every change. The 95th percentile and long conversations still have room.

Relevance: medium. The measure, ratchet and prove-the-metric pattern transfers to a solo developer's performance, test-flake or bundle-size work; the Slack and scale aspects do not.
