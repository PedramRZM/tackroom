# AI Native DevCon London (June 2026), batch 1: skills, context, memory and agent enablement

Sources read: 13 of 13, each in full (10 full talks, 3 short compilation videos). None unreadable.
All are YouTube caption transcripts with no speaker labels; names, products and commands are often
garbled and I flag the spellings I am unsure of. Upload dates are not in the metadata: the talks
were given in June 2026; the three compilations say they were cut afterwards (they advertise a
November 2026 event). Notes written 2026-11-10.

Source keys used below:

| Key | Speaker, talk | Video id |
| --- | --- | --- |
| GP | Guy Podjarny (Tessl CEO), Skills are the new Code | KpfnldjO3Iw |
| JG | John Groetzinger (Cisco), Skills Everywhere | 78KQVxMTAQ4 |
| JM | James Moss (Tessl), Using skills to pay the bills | 6VRKZQ3pmoU |
| LT | Liran Tal (Snyk), Your AI Agent Installed Malware Because a SKILL.md Told It To | oJGX8GYLWxg |
| PD | Patrick Debois (Tessl), The Rise of Agent Enablement | I9RWrW32QEw |
| LM | Lamis Mukta (Anthropic), Learning while you sleep: Beyond memory to dreaming | tTcxVv8HHNw |
| CQ | Peter Wilson and Davide Eynard (Mozilla.ai), cq, Stack Overflow for Agents | AHIY1XccX_E |
| EM | Edouard Maleix (freelance), How AI-First Dev Teams Build Collective Intelligence | -sYhcsy5OwI |
| RO | Robert Overweg, One Brain, No Filtering | rmxRlpi7xN4 |
| EB | Emma Burrows (Rezonant), How PMs can set up a product brain | M6Nhl4zR0uk |
| C1 | Compilation: Cisco and Stanford on Why Skills Are the New Code | PabKgxoegGg |
| C2 | Compilation: Your Coding Agent Deletes Its Memory After 30 Days | Xn7gXeNtoZI |
| C3 | Compilation: Anthropic, OpenAI and Thoughtworks on Context Engineering | wBBCJinOes4 |

Bias to keep in mind: GP, JM and PD work for Tessl (a skills registry and eval vendor), LT for Snyk
(a scanner vendor), LM for Anthropic, EB and CQ present their own products. The conference is run
by Tessl's media arm. Claims that happen to require the speaker's product are marked where relevant.

## Cross-cutting findings

### Recurring practices

1. Treat a skill as software, not a document: lint it, evaluate it, scan it, version it, track where it is installed, and watch how it behaves in real sessions. (GP [17:25], JM [24:44], JG [28:39], PD [19:41])
2. An eval is the gate for every skill change. Define the minimum the skill must always do well, and add an eval whenever a new topic is added. (JG [06:10], [12:17]; GP [20:31]; JM [23:44])
3. Build eval scenarios from things that really happened (an old pull request, a production trace, a captured incident), not invented tasks. (GP [21:32]; JG [15:22]; EM [23:48])
4. Prove a skill's usefulness by running the same task with and without it and looking at the delta; delete what shows no benefit. (EM [23:48], [31:05]; JM [23:44]; supported by the Stanford number in C1 [08:19])
5. Keep everything that shapes agent behaviour in the repository, not in a home directory: it then appears in diffs, review and CI. (JM [13:24]-[14:25], including a second-hand Boris Cherny quote; LT [15:25] on skills scattered across project and user directories)
6. Write small, single-purpose skills with their own descriptions and bundle related ones as a plugin, instead of one large skill with a keyword-stuffed description. (JM [10:20]-[13:24]; GP [05:07] on composition)
7. Keep always-loaded rules small; put procedures in skills that load on demand; leave reference material as plain docs the agent can search. (GP [04:07]-[05:07]; LM [03:05]-[06:15])
8. The skill listing itself costs context and can be truncated, so every installed skill has a price even when unused. (JM [06:11]-[07:13])
9. When something must happen, enforce it in deterministic harness code (a hook, a pre-commit gate) instead of hoping the model loads the skill. (GP [07:11]-[08:11]; C3 Böckeler [06:08]; CQ [21:40] reports trigger trouble without hooks)
10. Context is the durable asset; models and harnesses change. Keep skills portable across agents. (JG [02:06], [25:37]; JM [20:38]; LM [12:25])
11. Do not edit or fork a third-party skill in place. Write a first-party skill that invokes it and adds local conventions. (JM [12:24]-[13:24]; PD [19:41] on forks)
12. Keep one source of truth and generate other formats from it with a deterministic script, not an LLM. (JG [20:28]-[22:30])
13. Third-party skills are untrusted executable packages: inventory them, scan them with a purpose-built (not regex) scanner, re-scan on every update, pin versions and wait a few days before taking new releases. (LT [30:43]-[31:44]; JM [16:29]-[19:37]; GP [24:35]-[26:38]; PD [24:52])
14. A human clicking approve is a weak security boundary (approval fatigue, confused deputy). Remove one leg of private data, untrusted content and outbound communication instead. (LT [08:17]-[11:20], [18:27], [20:29])
15. Run agent tasks and judges in a sandbox where file and network access are controlled. (EM [20:44]-[21:46]; LT [03:04] notes the skill format itself carries no sandbox or permission data)
16. Store memory as plain markdown files the agent searches with ordinary file tools; version it and record which session produced each change. (LM [07:17]-[10:23]; RO [10:19]; EB [07:11])
17. Capture a lesson at the moment of correction, keep its origin attached, and promote it to shared guidance only when it recurs. (EM [09:23], [29:03]; CQ [11:22]-[12:23]; LM [22:39])
18. Consolidate memory out of band: a separate job reads transcripts plus the memory store and proposes changes for a human to accept. (LM [17:31]-[23:42]; EB [06:08] organisational agent)
19. When the agent gets something wrong, fix the system that produced the mistake so it does not recur, instead of only fixing the output. (PD [04:13], [08:21]; EM [11:27]; CQ [20:40])
20. Good context lets cheaper models do routine work; evals are how you find out. (JG [01:03]-[03:06]; GP [21:32]; RO [21:31])

### (a) What makes a skill good or bad

Structure
- A skill is a package, not only `SKILL.md`: rules (more markdown files), scripts, scaffolding, examples and example evals travel with it (JG [06:10], [18:24]). LT makes the same point as a warning: assets, references and installed packages are where payloads hide (LT [03:04], [27:36]).
- Progressive disclosure: only a short front matter is read before load, so depth in the body is cheap (LM [06:15]). Tessl's reviewer checks a skill against Anthropic's best practices: "Does it have proper progressive disclosure?" (GP [18:30]), plus concision and whether it declares its activation well.
- Single responsibility and decomposition. "Don't write monolithic skills" (JM [10:20]). Example: one skill breaks a Figma design into components and hands off to separate skills for low-level components, mid-level forms and pages; a human can still invoke just the low-level one (JM [11:20]-[12:24]).
- Skills fit procedures where you hold an opinion about the end-to-end process (LM [05:12]: "processes where you have like a procedural workflow"). GP's content types are policies and practices, product or API specs, and workflows (GP [03:06]-[04:07]).
- Safety boundaries belong in the text. GP calls skills that push an action with no limits negligent: "there should be a line there like do not drop the table" (GP [12:19]). Never have a skill route secrets through anything logged (GP [12:19]; LT [24:34]).
- Bad: a skill that restates what the model already does. In the Stanford study quoted in C1, "we see 55% following the instructions of the skill, even when the skill is not present" (C1 [08:19]).

Description and activation
- Name and description of every installed skill are injected at the start of every context window; there is a budget, "often expressed as a percentage of the context window" (JM [06:11]), and past it "Most agents will truncate that description" (JM [07:13]), so the skill silently stops triggering.
- Smaller skills get specific descriptions and activate more reliably than a large skill with many keywords (JM [11:20]).
- Triggering is unreliable even for careful authors: the cq team reports "a lot of issues on trying to get the skill trigger at the right time" (CQ [21:40]). EM lists activation (did the skill load in time) as its own eval dimension (EM [20:44]).
- Where loading must not be left to the model, GP cites Intercom: they "block GitHub pull request creation unless the relevant skill was loaded" (GP [07:11]).

Size
- No speaker gives a line or token limit. The concrete checks named are a line-count check and front matter validation in Tessl's `skill review` (JM [15:28]) and concision in the best-practice review (GP [18:30]).

Scripts
- Use tools and scripts for what can be done cheaper, faster and more deterministically than by the model (GP [02:03]-[03:06]). JG: have the agent write a deterministic script for mechanical conversions; "Don't have an LLM, just update confluence" (JG [21:30]).
- Shape data for agent editing: store eval datasets as JSONL so each case is one line and edits are precise. "Everyone needs to be using JSON, L instead of JSON." (JG [16:23])

Evaluation
- Static review first (lint for fields and format, best-practice review, optional LLM judge), cheap enough to run locally and in CI and fail the build (GP [17:25]-[19:30]; JM [14:25]-[15:28]).
- Then evals: run an agent on a task in a defined environment and judge the result. Levels: single-skill evals; project evals with all installed skills; larger model-comparison suites (GP [20:31]-[22:33]). Regression runs can use cheap models: "even with cheap open models, just to know that you're not regressing" (GP [21:32]).
- "Define the bare minimum that you expect this skill to always help with and always do it well." (JG [06:10]) and "So new topic means new eval, right?" (JG [12:17]).
- Scenario quality matters more than count; some scenarios "are just a waste of time in tokens" (GP [22:33]).
- Calibrate the judge by hand first: "before you run an LLM judge, you you are the judge" (EM [22:48]). EM's first run scored near 1.0 with lazy criteria and he treats that as a warning, not a win.
- For agent evals JG checks more than the answer: tools called, parameters, token spend and latency against a stored baseline (JG [17:23]).
- Evals also answer "Do you even need this skill?" after a model upgrade (JM [23:44]).

Versioning
- Semantic versions as a trust signal: 0.0.x while only the author uses it, 0.x while a few people give feedback, 1.0 once it works first time for many (JG [24:34]). "start with version zero zero, share it with a few, get some feedback" (JG [24:34]).
- Versions let you say which release introduced a problem and whether the fix worked (GP [25:36]). Pinning stops silent drift and makes rollback possible (JM [16:29]).
- Skills rot as models, APIs and infrastructure change: "it rots and it becomes less effective and eventually harmful" (GP [15:23]); "having an outdated skill can often be just as bad as having no skill at all" (JM [06:11]). PD: re-test skills when the model changes, as you would when an external API changes (PD [19:41]).

Distribution
- Simplest version that works today: one git repository of skills the agent can read, and "it can just grep for the skills that it needs" (JG [27:38]). Cisco teams each keep one skills repo, separate from project repos (JG [27:38]).
- Registry or package manager for pinned versions, update notices, diffs, rollback, discovery and policy enforcement (JM [16:29]-[18:36]; GP [25:36]-[26:38]). Named options: Tessl registry, Microsoft's APM (JM [29:51]), the `skills` npx command (caption: NP Skills, JM [15:28]).
- Do not tie skills to one agent's directory layout; JM points at the many per-agent paths in the skills repo and the shared agents-directory pattern (JM [19:37]-[20:38]).
- Open problem: there is no standard way to declare a dependency between skills in different packages; JM suggests peer-dependency-like metadata or letting the agent read the reference (JM [30:54]).

Ownership
- A shared skills repo without quality signals collapses: duplicates pile up ("There are seven over here. Which one should I choose?", GP [14:22]), PRs stall because the owner cannot tell if a change helps, and people return to private copies (GP [13:22]-[15:23]).
- Treat a shared skill like a shared library: anyone may open a PR, the evals decide (JG [28:39]: "We treat it just like we would a shared library.").
- Every shared component needs a named owner, maintainer and budget (PD [18:40]-[20:44]); avoid single-person ownership and bus factor (JM [21:41], [24:44]).

Authoring
- JG: do not hand-write skills. "The skill is not for you. The skills for your agent." (JG [09:14]). Work the task through with one agent, then have it distil the session into a skill; a small model can write the skill it will use itself (JG [10:15], [18:24]-[19:26]). Human effort goes into the eval.
- EM disagrees on sequencing: do the curation by hand before delegating it (EM [31:05]).

### (b) How skills, rules/AGENTS.md, MCP and memory are divided

- Rules files (CLAUDE.md, AGENTS.md; the captions garble both): always in context, so small. "you've got rules that always get shoved into the context window" (GP [04:07]). LM: a short file of codebase orientation, organisation facts and user preferences was unreasonably effective, and the failure mode is the file growing long (LM [03:05]-[04:07]).
- Skills: loaded on demand by user invocation or model choice; reusable like libraries. "If you think you're going to do it more times, you turn it into a skill." (GP [10:16]). One-off needs stay as prompts. Best for opinionated procedures (LM [05:12]).
- Passive docs: architecture notes and similar files that sit in the repo and are found by search when needed (GP [05:07]).
- Tools (CLI, MCP, network APIs): the action layer. GP lists CLI first and frames tools as the cheaper, faster, less error-prone path for work that does not need model intelligence (GP [02:03]-[03:06]); many skills exist only to explain how to use a tool (GP [05:07]). MCP gets little direct discussion in this batch. Where it appears it is a connector: cq ships a skill that carries the protocol (when to query, validate, propose) plus an MCP server that performs query, propose, confirm and flag (CQ [12:23]); RO and EB use MCP or API connectors to pull meeting notes and tickets in (RO [16:28]; EB [19:31]).
- Harness and hooks: deterministic code around the model for things that must always happen, such as blocking PR creation without the skill or blocking commits under a coverage bar (GP [06:08]-[08:11]). Böckeler's split in C3: guides feed forward, sensors feed back, and each can be computational (static analysis, codemods) or inferential (a review agent) (C3 [05:06]-[07:12]).
- Memory: files the agent itself reads and writes during work, separate from human-curated rules. Tiered by scope and permission: curated organisation-wide context read-only for agents, a per-agent scratchpad writable (LM [11:25]-[12:25]). EM has the same scoping for diaries (team, personal, repository, project) (EM [08:19]).
- The flow between layers, as EM runs it: raw entries accumulate, curated packs are rendered to markdown, and "those rendered facts, they are just skills" in the end (EM [30:04]-[31:05]; caption has facts for packs). Inference: memory is the intake, skills and rules are where proven lessons graduate to.
- Human-facing docs: keep a `README.md` for people next to the `SKILL.md` for the agent, generated together; in JG's experience they overlap about 80% (JG [20:28], [25:37]).
- Critique of leaning on rules plus built-in memory alone: it is local to one machine and "all of that stuff then also has to get loaded into the context" (CQ [08:17]); built-in memory wrote duplicates and ignored them (CQ [09:20]).

### (c) Supply-chain and injection risks of third-party skills, and controls

Risks described
- The format has no security model. A `SKILL.md` carries "no sandboxing information. There's no permission here." (LT [03:04]); the Agent Skills spec's guidance amounts to read before enabling and do not trust third parties, with "There's like no signing, no log file" (LT [05:10]; log file is the caption's rendering of lockfile). Trusting a folder is the only boundary: "that is the security boundary" (LT [05:10]).
- Prevalence on ClawHub (captions: CLO hub, club, glob), scanned around 5-6 February 2026 over about 4,000 skills: LT says "up to like 34% or something like that" had some security issue (LT [12:21]) and 7% leaked credentials (LT [26:35]). GP says over 30% malicious (GP [12:19]); JM says 20% (JM [19:37]). See contradictions.
- Malware via prerequisite: a skill posing as a Google integration carried an important-note section telling the agent to download a core component from a link; the archive was password-protected so platform scanners could not open it, and the password was in the skill. The agent relays the request, the human approves, "You say yes and malware goes in." (LT [20:29]; the whole demo runs [19:29]-[22:34]). LT calls this a confused deputy and says hundreds installed it.
- Invisible instructions: Unicode control characters (the Trojan Source technique) hid a shell command in a harmless-looking testing skill; Gemini CLI in YOLO mode executed it on activation. Human review is bypassed: "that even you as a human review just completely bypass here" (LT [24:34]).
- Natural-language exfiltration: a deployment skill told the agent to upload the env file to a public paste service as a deploy step. It worked on some runs and was refused on another; "attackers will be very, very mindful and trying as many times as they want" (LT [26:35]).
- Poisoned content at run time: an email asking for a config file was obeyed by an OpenClaw agent with inbox access (LT [16:25]-[18:27]). The general pattern is private data plus untrusted content plus outbound communication (LT attributes it to Simon Willison, caption: Simon Wilson; Snyk's term is toxic flows); "all even two of those are pretty bad to combine" (LT [09:18]). Ordinary coding example: an agent with a local env file asked to read a public GitHub issue (LT [10:19]).
- Secrets in context: a skill that collects card details leaves them in logs, memory files and any proxy or judge model (LT [24:34]-[25:35]).
- Fake security tooling: a skill named as a scanner was itself malware, with the payload in test fixtures (LT [26:35]-[27:36]). Typosquatting and lookalike names (LT [14:25]); forks with the same name but different content (JM [16:29]).
- Persistence through agent config: the npm attack JM calls mini Shai-Hulud (caption: mini Shiloh tech) "added a global clawed code hook to your machine" to keep itself installed (JM [18:36]).
- Memory poisoning: memories can be "maliciously injected by someone trying to prompt inject your agents to write bad things to memory" (LM [09:22]). Shared knowledge stores carry the same risk plus personal data leakage (CQ [14:26]-[15:28]).
- Negligent first-party skills: no malicious intent, but no stated limits either (GP [12:19]).

Controls recommended
- Keep an inventory: know which skills are installed, where, and at which version. "have an inventory of all of them" (LT [31:44]); GP and JM make the same governance point (GP [13:22]; JM [08:14]).
- Scan with a tool built for skills that analyses intent, and re-scan on every update. Regex scanners fail: a legitimate one missed the malicious deployment skill and flagged itself; "pattern matching just doesn't work" (LT [28:40]). Named tool: Snyk Agent Scan, with a nine-category risk taxonomy, integrated into registries including Tessl's (LT [29:42]-[30:43]). Vendor claim, no precision or recall figures given.
- Pin versions and install through something that records what was installed (GP [25:36]; JM [16:29]).
- Minimum release age: refuse packages newer than a few days. Tessl says this is why the npm attack did not reach them (JM [18:36]-[19:37]). ClawHub added a supply-side version: the publishing account must be about seven days old with other contributions (LT [15:25]).
- Allowlist: all first-party skills, a small approved set of third-party ones, a defined process for bringing a new external skill in (JM [17:33]; PD [24:52]).
- No global agent state: skills, hooks and settings live in the repo (JM [13:24]-[14:25], [18:36]).
- Do not rely on deny lists for shell commands; agents work around them (LT [11:20]). Do not rely on approval prompts; LT names "acceptance fatigue" (LT [18:27]).
- Sandbox with explicit file and network policy (EM [21:46]); limit blast radius for agents as you would for users (PD [08:21]).
- For knowledge shared between agents: human review before anything becomes visible to others, PII and guardrail checks on submission, short-lived API keys delegated to the agent that cannot perform control-plane operations, optional signing of entries, and an instruction to validate retrieved advice before acting on it (CQ [11:22]-[12:23], [16:29]-[17:30]).
- For memory: version every change, record who and which session wrote it, and keep curated tiers read-only to agents (LM [10:23]-[12:25]).
- Quick vetting habit: before adopting an outside skill, have the agent compare it with what the repo already has; RO's check took a minute and concluded "nothing you don't already have" (RO [10:19]). Inference: this is a usefulness check, not a security check.

### (d) Memory, dreaming and team-shared learning in practice

What the speakers mean
- Memory (LM): markdown files in a directory that the agent decides when to read, write and update during a session (in band). Current best practice at Anthropic is "modeling these memory systems just as file systems" (LM [07:17]) searched with bash and grep, with an index so files can grow. Autonomy on writes: "give agents autonomy when they're writing to memories" (LM [08:18]).
- Production guardrails for memory (LM [10:23]-[13:26]): versions with rollback and provenance; optimistic concurrency by hashing before drafting and again before writing ("If those two things do not match, then the agent cannot write it", LM [11:25]); permissions by tier; portability across products.
- Limits of in-band memory (LM [15:27]-[16:29]): the agent splits effort between the task and its future self ("how much capacity should an agent put into helping future versions of itself"), and it cannot see patterns across sessions or across other agents.
- Dreaming (LM [17:31]-[23:42]): "a process that runs in batch and asynchronously with its own allocated resources" (LM [18:32]). Input is the current memory store plus a chosen set of session transcripts, including tool calls and metadata. An orchestrator fans out subagents over the transcripts, collects patterns, and proposes specific edits, each with the transcripts where the pattern occurred and "some stats on like how prevalent this issue is" (LM [22:39]). A person accepts or rejects. It also prunes: "consolidate your memory and cut things that are no longer relevant" (LM [25:48]). You can steer what counts as worth remembering. Offered as the memory and dreaming API in Claude Managed Agents (LM [27:53]).
- Diary (EM): every agent has its own identity (a GitHub App bot, signed commits, its own permissions) and writes entries during work; commits reference the entry that explains them (EM [07:18]-[09:23]). "if the work or decision matters, you need to land it somewhere before it disappears" (EM [09:23]). Entries link to the review comment that caught the mistake and to the fix (EM [13:29]-[14:31]).
- Packs (EM [15:33]-[18:40]): after passive accumulation, a person (later an agent) groups related entries, renders them to markdown within a token budget with each section pointing at its source entry, human and agent, and ships that as a skill.
- Knowledge units (CQ [10:21]-[12:23]): a small JSON record (domains, the insight, the action to take, languages, frameworks, an optional pattern). The agent queries before a task, proposes when it solves something non-obvious, confirms or flags entries it used (building a confidence score), and can be asked to reflect over a whole session at the end. Stored in local SQLite by default, optionally a team server with human review, optionally a public commons.
- Team wiki (RO, EB): a git repository of markdown fed by scheduled ingestion. EB's layout is `inputs` (a daily queue, with a manual folder), `sources` (raw data, trimmed) and `wiki` (customer insight, features, product principles, technical context), with a separate organisational agent that restructures the wiki as it ages (EB [06:08]-[07:11]). RO keeps a private vault and promotes a small number of wikis (10 to 15) to the wider team (RO [08:14], [26:45]).
- Transcripts as raw material: Brian Douglas (C2 [07:12]) says Claude Code and Codex keep session files locally for 30 days and then delete them, and argues for mining them for skills, docs and context.

A lightweight single-repo version (Inference throughout; each step names the source practice it borrows)
1. A `lessons/` directory of short markdown entries, one per correction: date, commit or session reference, what went wrong, what fixed it, scope tags (language, framework, area). Borrowed from EM's entries and the cq knowledge-unit fields.
2. Have the agent write the entry at the moment you correct it, and reference the entry from the commit that fixes the problem (EM [09:23]).
3. A reflect step at session end that proposes entries you approve or edit (CQ [12:23]), since in-band writing competes with the task (LM [15:27]).
4. A query step at task start: grep `lessons/` by tag before working (CQ [11:22]; LM [07:17]). No vector store until the corpus is large (RO [10:19]).
5. Git supplies versioning, rollback and provenance (LM [10:23]). A solo developer does not need the hashing scheme unless several agents write at once.
6. Promote only on recurrence: "if there is no recurrence, you don't care" (EM [29:03]). When a theme repeats, render the entries into a skill or a rule line, keeping links back to the entries (EM [17:39]-[18:40]).
7. A weekly out-of-band dream run: give a fresh agent the lessons, rules, skills and the week's transcripts; ask for proposed additions, merges and deletions with the evidence and a count of occurrences; review the diff yourself (LM [18:32]-[23:42]). Ask it to check for duplicates by intent, not by file name or bytes (CQ [08:17]-[09:20]).
8. Test a promoted lesson by replaying the original incident with and without it (EM [23:48]); retire it when it stops helping (EM [31:05]).
9. Keep curated files read-only to the agent in normal sessions and give it a scratch area (LM [12:25]).
10. Preserve transcripts past the harness's retention window if you want step 7 to see them (C2 [07:12]). Inference, not from a source: in Claude Code this is likely the `cleanupPeriodDays` setting; verify against current docs.

### (e) Every measured result or number given

Measured or counted by the speaker's own organisation
- About 2 million skills on public GitHub, up from roughly zero at the start of 2026 (GP [11:18]: "there are about 2 million skills on GitHub"); JM adds the repo count: "2 million plus skills across GitHub, across 44,000 repos" (JM [03:05]). Method not described.
- ClawHub scan, early February 2026, about 4,000 skills: up to about 34% with some security issue, glossed as 1 in 3 (LT [12:21]); 7% leaking credentials (LT [26:35]). An earlier passage reads 1 in 7 and 30% in the same breath and is too garbled to use (LT [02:03]).
- Skills on Vercel's skills.sh registry passed half a million within a few months; npm took about ten years to reach 1 million packages (LT [13:24]; the years are garbled).
- Daily skill publication on ClawHub went from tens to hundreds, about tenfold (LT [15:25]-[16:25]).
- The fake Google skill was installed hundreds of times (LT [19:29]).
- Stanford study (C1 [06:18]-[08:19]; narrator names Rob Willoughby and Simon Obstbaum, spellings unverified): 500 skills, 1,000 synthetic tasks anchored on the skills, 19 model and harness combinations. Instruction-following was 55% with the skill absent. The with-skill figure is unreadable in the captions (the text reads 1,993%). The full talk is not in this batch.
- EM's pack eval on the missed-Go-SDK incident: without the pack the agent failed (caption: fail at 67, meaning unclear); "with the pack it was always passing" (EM [24:51]). He presents it as a single case.
- EM's first fidelity eval: three binary criteria, composite score near 1, which he attributes to lazy criteria (EM [22:48]).
- About 95% of one of EM's open-source PRs was written by Claude Code (EM [06:17]).
- Tessl's LLM-judge review scored JM's deliberately bad money-making skill 20% (JM [15:28]).
- Cisco: over 1,000 users on the new platform within weeks of release (JG [05:09]); 8 specialist agents with 10 more planned that quarter (JG [13:20]); 8 teams produced consistent eval datasets within a week using one shared skill, rolled out to one team on day one, another on day two, everyone on day three (JG [19:26]); README and skill about 80% similar (JG [25:37]); an Opus prompt fanning out to 15 subagents as the cost problem (JG [01:03], clean wording in C1 [05:14]); the KB-to-skill platform followed two years of work by two engineers (JG [08:12]).
- RO: almost 1,200 markdown files handled without RAG (RO [10:19]; later he says almost 1,500, [27:47]); one minute to vet an outside skill (RO [10:19]); about a month to build the setup, and seconds to minutes to rebuild from a script (RO [25:41]); 80% of content kept to leadership, 10 to 15 wikis promoted (RO [26:45]); half a million data points on art directors' preferences (RO [26:45]).
- cq: a demo failed because the local model's default context was 4K tokens and the fetched page overflowed it (CQ [04:07]); a 0.8-billion-parameter local model answered correctly once given a directory-browse and file-read tool, after several attempts (CQ [05:07]-[06:10]); agents kept writing GitHub Actions two major versions out of date until the lesson was stored (CQ [22:41]).
- Lopopolo (C3 [03:02]-[04:03]): about three concurrent sessions is his personal limit; tasks run 6, 12 or 36 hours with auto-compaction.
- Böckeler (C3 [06:08]-[07:12]): recalls Amazon's claim of 400 or 500 developer-years saved on Java upgrades, mostly codemods exposed to AI. Second-hand and approximate.
- Douglas (C2 [07:12]): session files deleted after 30 days; a 200 dollar monthly plan; 10 parallel agents in separate VMs.

Quoted from others, or thresholds
- OpenClaw skills malicious: over 30% (GP [12:19]) versus 20% (JM [19:37], attributing it to GP).
- A unicorn with over 1,000 developers ended up with seven code review skills in its shared repo (GP [13:22]-[14:22]).
- Minimum release age of a few days (JM [18:36]); ClawHub publisher account age about seven days (LT [15:25]).
- Skills can go stale in as little as two weeks (GP [15:23]); rhetorical, not measured.
- Viral claims JM cites as examples of unmeasured hype, not as findings: a skill cutting tokens 60 to 80%; rules lifting coding accuracy from 65% to 94%; 20,000 tokens added to every prompt; a prompt killing 90% of production bugs (JM [21:41]-[22:41]).

No numbers at all: LM reports better accuracy on repeat tasks and lower token cost from memory, with no figures (LM [13:26]-[14:26]). PD and EB give none.

### Contradictions and open questions

- Share of bad skills on OpenClaw's hub. GP: over 30% malicious. JM, citing GP the same day: 20%. LT, whose team ran the scan: up to about 34% with some kind of security issue, which is broader than malicious. Use LT's wording; treat the others as loose retellings.
- Who writes and reads skills. JG: do not hand-write them and "If your engineers are reviewing text diffs on a skill, you are wasting a lot of time." (JG [11:16]); judge by evals. LT opens by shaming the audience for not reading the skills they install. EM: master the workflow by hand first: "every workflow before we should lend it to an LLM, we need to master it as human" (EM [31:05]). Inference: JG is speaking of first-party skills covered by evals, LT of third-party ones; they are compatible, but JG's position depends entirely on the evals existing.
- Is agent-written memory reliable. LM: autonomy works really well. CQ: Claude admitted "I've been writing the same memory tons of times in different places and also just ignoring it" (CQ [09:20]). JG: agent-built memories drift from the source documents until "the memories drift from the content" and trust is lost (JG [10:15]). LM's own guardrail list and dreaming are partly an answer to this.
- Retrieval. RO: vectors and RAG were not needed at about 1,200 files. LM: files plus grep plus an index. CQ expects to need semantic search as the store grows (CQ [29:53]-[30:55]). RO added a vector layer anyway and says it pays off only at larger scale (RO [19:30]).
- Registry or plain git. JM (vendor) argues a registry is needed; JG, a Tessl customer, also says a single repo and grep is a workable start. For one developer the registry benefits that remain are pinning and release-age delay.
- Global versus repo-local. JM and the Boris Cherny quote ban setup outside the repo. LM and EM both keep a personal tier (preferences, private diary). Open for a solo developer who works across many repos: what, if anything, should stay global.
- Hooks for activation. GP holds up hook-enforced skill loading as the model. The cq team chose not to use hooks because the right moment is task start, not every call, and then struggled with triggering (CQ [21:40]).
- Value of approval prompts. LT argues they fail as a security control. CQ, LM and EB all rely on a human accepting proposed knowledge or plans. Inference: different jobs. Review of a proposed diff at rest is not the same as a mid-task permission prompt.
- Eval analogy. GP maps single-skill evals to unit tests; JM maps skill review to lint and unit tests and evals to end-to-end tests. Cosmetic, but it changes where people expect to pay token cost.
- Speaker name. The C2 narrator calls the diary speaker Alex; the talk title says Edouard Maleix.
- Not answered anywhere: the actual skill-listing budget for each harness, a recommended maximum skill length, how to declare cross-package skill dependencies, and any quantified benefit of memory or dreaming.

## Per source

### Skills are the new Code (Guy Podjarny, Tessl, June 2026)
File: refs/videos/KpfnldjO3Iw/transcript.md   URL: https://www.youtube.com/watch?v=KpfnldjO3Iw
Thesis: Agent development has a layered stack (models, tools, context, harnesses, factory lines) and context is the part developers now program. Skills are multiplying faster than teams can govern them, and the fix is to apply the five standard software quality tools to them.
Practices:
- Sort context by load mode: always-on rules, on-demand skills, passive docs; and by content: policies and practices, product or API specs, workflows [03:06]-[05:07].
- Use tools (CLI, MCP, API) where intelligence is not needed; grep and FFmpeg are his examples of cheaper and less error-prone than the model [02:03]-[03:06].
- Use harness hooks for control: Intercom blocks PR creation unless the skill was loaded [07:11]; an OpenAI team's harness uses "not allowing a commit unless a certain test coverage has been included" [08:11].
- Static analysis for skills: lint for fields and format, review against Anthropic's best practices (progressive disclosure, concision, activation), security scan, then an agentic review of substance [17:25]-[19:30].
- Evals at three levels: single skill, project with all skills installed (helps you delete things), and model-comparison suites [20:31]-[22:33]. Seed project evals from history: "take an old pull request and I can convert or extract a scenario out of that" [21:32].
- Dependency management: registry, versions, a record of what is installed, quality and security bars on install and publish, cross-agent packaging [25:36]-[26:38].
- Observability: monitor coding-agent sessions to extract eval scenarios and find missing or removable skills [26:38]-[27:39].
- Turn maintenance into optimisation: mine agent logs, PRs and production logs for skill changes, including deletions [16:23].
- Humans should "leave the SDLC to the agents" and work a context lifecycle: generate, evaluate, optimise, distribute, consume securely, observe [27:39].
Evidence and numbers: about 2 million public skills [11:18]; over 30% of OpenClaw-ecosystem skills malicious [12:19]; the seven-code-review-skills story from a company with over 1,000 developers [13:22]-[14:22].
Tools and files named: CLAUDE.md, AGENTS.md (both garbled), an architecture doc, Claude Code, a Tessl lint command (name garbled in the captions), Tessl review, Tessl eval, Tessl registry, Snyk, Datadog, Linear, Jira, GLM and Opus model names (versions garbled), Tessl agent (early access).
Caveats: keynote by the vendor's CEO; every remedy maps to a Tessl feature. He says quality scores are imperfect and dynamic security testing of skills is nascent [23:34]-[24:35]. Terms such as harness are admitted to be unstable [09:14].
Relevance: high. It is the clearest statement of the rules, skills, docs, tools and hooks split and of the review-then-eval pipeline.

### Skills Everywhere (John Groetzinger, Cisco, June 2026)
File: refs/videos/78KQVxMTAQ4/transcript.md   URL: https://www.youtube.com/watch?v=78KQVxMTAQ4
Thesis: Better context, not a better model, is what most work needs, and skills are the portable form of it. Maintain context once, guard it with evals, and generate every other representation from that source.
Practices:
- Default to a mid-tier model and escalate only for complex planning: "I largely used the medium tier model" [02:06]. Subagent fan-out on the top model was the cost driver that forced limits [01:03]-[02:06].
- Use skills to correct stale training defaults. His repository-standard skill stops agents emitting `requirements.txt` and pip when the team standard is uv [06:10].
- Ask "is this a skill?" before answering a repeated question in chat: the cultural default he pushes is "asking first, is this a skill?" [22:30].
- Pipeline for skills derived from docs: a doc change triggers an LLM that classifies it minor, moderate or major, updates the skill and runs evals. Minor plus passing evals releases automatically; major changes and new topics go to a human [11:16]-[12:17].
- Only curated, actively maintained docs are converted; pointing an agent at the whole knowledge base produced hallucinations from stale articles [08:12].
- Eval design: one shared dataset schema, datasets stored in the repo next to the code, JSONL format, the same script running against local, dev and staging endpoints, checks on tool calls, parameters, tokens and latency against a baseline [15:22]-[17:23].
- Pull eval cases from production traces, and rerun the full set after every prompt or tool change: "What else did that break to fix this one thing?" [15:22].
- Ship the practice as a skill instead of a meeting: his eval-framework plugin (skill file, example scripts, example evals) let every team's agent build evals the same way [18:24]-[20:28].
- Pair `SKILL.md` with `README.md` in one git repo and sync the README to the wiki with a deterministic script [20:28]-[22:30].
- Semantic versioning as a maturity signal; use it yourself first, then a few people, then 1.0 [24:34].
- Discovery at small scale: put skills in one repo and let the agent grep [27:38].
- Start with one workflow you keep explaining [23:32].
Evidence and numbers: see (e). All anecdotal by his own account [07:11].
Tools and files named: SKILL.md (caption: skill that empty, skill.md), README.md, JSONL, uv, LangChain, LangGraph, LangSmith, Claude Code, GitHub Copilot CLI, Tessl registry, Confluence, Jira, GitHub Actions, Sonnet, Opus, Haiku.
Caveats: he says these are patterns tried under deadline pressure, not case studies [07:11]. His advice not to read skill diffs holds only when evals cover what you care about. Agent-built memories drifting from source content is the failure he spent two years on [10:15]-[11:16].
Relevance: high. Concrete eval mechanics, versioning rule and single-source pipeline, all usable by one person.

### Using skills to pay the bills (James Moss, Tessl, June 2026)
File: refs/videos/6VRKZQ3pmoU/transcript.md   URL: https://www.youtube.com/watch?v=6VRKZQ3pmoU
Thesis: Skills sprawl in five ways (overlap, drift, no activation, staleness, overloading), and the remedies are the ones packaging ecosystems already learned. Skills are the durable asset and the agent only the runtime.
Practices:
- Five failure modes, with overloading the least known: too many skills in one repo exhausts the listing budget and descriptions get truncated [05:11]-[07:13].
- Context is the lever you control: "an agent is a function of the model, the harness and the context" [09:17].
- Decompose into small skills grouped as a plugin; an entry skill can call the others [10:20]-[12:24].
- Extend, do not edit, vendored third-party skills: "Write your own first party skill that invokes that skill." [13:24].
- No global skills: "Skills that affect output should be version controlled alongside the thing that they're acting on." [14:25]. He relays Boris Cherny, via a colleague: "All agent workflow improvements, hooks, skills, etc. must be checked into the repo for everyone." [14:25].
- Run automated skill review locally after edits and in CI as a gate; it checks validity, line count and front matter, with an LLM judge on top [14:25]-[15:28].
- Registry benefits: "Everyone's pulling the same version of the skill, the same pin version." [16:29], plus update notices, diffs, rollback and discovery.
- Registry as policy point: approved skills only, security scan must pass, minimum release age [17:33]-[18:36].
- Keep skills agent-neutral: "Skills are effectively your durable asset. The agent is just the runtime." [20:38].
- Make contribution safe with CI checks so people dare to change shared skills [21:41].
- Treat any claimed improvement as an experiment to be written down and measured; evals let you vary model, harness or context and see the effect [22:41]-[23:44].
Evidence and numbers: see (e). The npm incident and the release-age defence are first-hand [18:36]-[19:37].
Tools and files named: Tessl skills inventory (private beta), Tessl registry, `skill review`, Snyk scans, Claude marketplaces, the npx skills command (garbled), Microsoft APM, Matt Pocock's grill-me skill and its successor grill-with-docs, the agents-directory convention.
Caveats: vendor talk. He has no good answer for sharing skills with non-technical staff [28:48]-[29:51] or for cross-package skill dependencies [30:54]. Plugins versus single skills: it depends [27:47].
Relevance: high. The repo-only rule, the description budget and the extend-not-edit rule apply directly to a solo setup.

### Your AI Agent Installed Malware Because a SKILL.md Told It To (Liran Tal, Snyk, June 2026)
File: refs/videos/oJGX8GYLWxg/transcript.md   URL: https://www.youtube.com/watch?v=oJGX8GYLWxg
Thesis: Skill ecosystems are repeating the early npm supply-chain story at higher speed and with a worse twist: the payload is natural language executed by a privileged agent. Reading the file and approving prompts are not adequate defences.
Practices:
- Treat a skill as a package with scripts, assets and references, and review all of it on every update, not only the markdown and not only at install [03:04]-[04:07].
- Assume the folder-trust prompt is the only boundary the harness gives you [05:10].
- Map your own exposure against the three-part pattern (private data, untrusted content, outbound channel) and remove a leg [08:17]-[11:20].
- Do not count on command deny lists; agents route around them to reach the goal [11:20].
- Do not count on human approval; repeated prompts lead to blanket acceptance, and the agent can end up socially engineering its user [18:27], [20:29].
- Hidden Unicode makes visual review unreliable [22:34]-[24:34].
- Never pass secrets or card data through an agent's context; they persist in logs, memory files and intermediaries [24:34]-[25:35].
- Use an intent-based scanner, keep an inventory, and re-scan when skills are upgraded or passed around the team [29:42]-[31:44].
Evidence and numbers: ClawHub scan figures, registry growth, 7% credential leaks, hundreds of installs of the fake skill; see (e). Demonstrations: poisoned email on OpenClaw, fake prerequisite malware, invisible-character command on Gemini CLI in YOLO mode, env-file exfiltration by a deployment skill (succeeded on some runs, refused on one), a malicious scanner skill, a regex scanner that missed the attack and flagged itself.
Tools and files named: SKILL.md, the Agent Skills spec, ClawHub, skills.sh (Vercel), Tessl registry, OpenClaw, Gemini CLI with the yes flag, Claude Code, Snyk Agent Scan, Skill Defender (legitimate regex scanner), a malicious skill named skill guard (spelling as heard), Telegram, Gmail, env files.
Caveats: vendor talk; detection quality is asserted, not shown. Several figures are garbled in the captions. The exfiltration demo was non-deterministic. He leaves the role of the human in the loop as an open question [18:27]-[19:29].
Relevance: high. It defines the threat model for installing any outside skill and for running agents with broad permissions.

### The Rise of Agent Enablement (Patrick Debois, Tessl, June 2026)
File: refs/videos/I9RWrW32QEw/transcript.md   URL: https://www.youtube.com/watch?v=I9RWrW32QEw
Thesis: Scaling agentic coding is an enablement problem with the same shape as DevOps and platform teams: what is good practice for people is good for agents, and someone has to own the shared layer.
Practices:
- Do not just patch the agent's output; spend the effort on "improving the system that builds the code" [04:13]. After each task: "Think about not repeating this again." [08:21].
- Vague goals are the fastest way to burn tokens; small tasks and clear goals [06:17], [10:22].
- Measure agent efficiency by turns: "how many turns does an agent need to do to do the right thing?" [11:24]. Add rework to velocity metrics [12:25].
- Hold an agent retrospective (how did our agents work) and feed it into the next cycle [11:24].
- Make agent quality part of the definition of done [10:22]-[11:24].
- Shared skills need an owner, a maintainer and a budget; re-test them when the model changes [18:40]-[20:44].
- Governance before automation: approved skills, mandated scans, an intake process for external skills [24:52]; his barrel image says the lowest stave sets the level [27:00].
Evidence and numbers: none measured. Tessl itself has five or six harnesses in progress [07:19].
Tools and files named: CLAUDE.md, registries for skills and MCP, gateways, his own agent that distils social posts into patterns while trying to discount vendor content and repeated citations of one article [29:04].
Caveats: a new talk written days before; he says "Unfortunately, there is no playbook." [25:56] and that the KPI advice is still vague [24:52].
Relevance: medium. Mostly organisational, but the turns metric, agent retro and fix-the-system habit transfer to one person.

### Learning while you sleep: Beyond memory to dreaming (Lamis Mukta, Anthropic, June 2026)
File: refs/videos/tTcxVv8HHNw/transcript.md   URL: https://www.youtube.com/watch?v=tTcxVv8HHNw
Thesis: Context engineering moved in a year from CLAUDE.md to memory tools to skills to file-system memory. In-session memory is necessary but limited; a separate batch process that reviews transcripts and curates memory closes the learning loop.
Practices:
- Start simple: "do the simple thing that works" [03:05]. A short instruction file and skills go a long way before any memory system [24:42].
- Model memory as a directory of markdown searched with normal file tools; do not design special memory tools [07:17].
- Let the agent decide what to write, but add guardrails once several agents or long-running work are involved: versioning with provenance, hash-checked writes, tiered permissions, portability [10:23]-[13:26].
- Know the two limits of in-session memory: divided effort and no cross-session view [15:27]-[16:29].
- Run dreaming as a separate job with its own budget over selected transcripts and the memory store; inspect tool calls and metadata, not only messages [18:32]-[20:33].
- Require evidence with each proposed memory change (the transcripts, prevalence) and keep a human accept or reject step [22:39]-[23:42].
- Prune stale memory in the same pass [25:48].
- Scope dreaming to transcripts that share the permission level of the target memory store [28:55]-[29:57].
- Move the parts that should be deterministic (hashing, versioning) into the harness [30:59].
Evidence and numbers: none. Benefits (better second attempts, fewer tokens) are stated qualitatively [13:26]-[14:26].
Tools and files named: CLAUDE.md, memory tool, skills, bash, grep, Claude Code, Claude Managed Agents memory and dreaming API.
Caveats: she calls the area open research [26:52]. The audience question about reinventing databases is conceded in part [30:59]. Product pointer only given when asked.
Relevance: high. It is the first-party description of file memory and dreaming, and both scale down to one repo.

### cq, Stack Overflow for Agents (Peter Wilson and Davide Eynard, Mozilla.ai, June 2026)
File: refs/videos/AHIY1XccX_E/transcript.md   URL: https://www.youtube.com/watch?v=AHIY1XccX_E
Thesis: Agents keep rediscovering the same fixes because the lesson dies with the session and built-in rules and memory are local and unreliable. cq stores each lesson as a small structured unit that agents query before a task and that can be shared from one machine to a team to a public commons.
Practices:
- Query before starting: "before you start working on a new task, you should come query CQ for that domain" [11:22].
- Treat retrieved knowledge as a hint: "validate this thing first, don't just blindly use it" [12:23]; confirm what worked and flag what did not.
- Trigger a reflect pass at the end of a session to harvest lessons the agent did not record [12:23].
- Three tiers with rising review: local store with no review, team server with human approval, public commons by nomination [13:26]-[14:26].
- Generalise lessons away from the specific project unless it is an open-source tool [28:52].
- Private by default; sharing is opt-in [21:40].
- Audit agent memory for duplicates by meaning; a byte or file-name comparison reports nothing [08:17]-[09:20].
- When an agent is stuck on tool configuration, tell it to read the current official docs; this is what fixed the MCP config path [18:32]-[19:36].
Evidence and numbers: worked example with the Joplin MCP server (wrong config path, lesson stored, next fresh session used the right path first time) [18:32]-[20:40]; small-model context examples [04:07]-[06:10]; GitHub Actions version drift [22:41].
Tools and files named: cq (plugin with skill plus MCP server), cq exchange (hosted), local SQLite store (they say "you get like a little SQLite database locally" [13:26]), Docker server, any-agent, Joplin, Claude Code, CLAUDE.md, AGENTS.md, STRIDE threat model, JWT and short-lived API keys.
Caveats: they say they fixed it only for a narrow personal case [17:30]. Skill triggering was a fight and they chose not to use hooks [21:40]. Retrieval is basic and semantic search is an open PR [29:53]. Risks of a shared store (poisoning, PII, spoofing) are acknowledged and only partly mitigated [14:26]-[17:30]. Built from late February to May 2026, so young.
Relevance: high for the pattern (query, propose, confirm, flag, reflect), medium for the product.

### How AI-First Dev Teams Build Collective Intelligence (Edouard Maleix, June 2026)
File: refs/videos/-sYhcsy5OwI/transcript.md   URL: https://www.youtube.com/watch?v=-sYhcsy5OwI
Thesis: Corrections evaporate when a session ends and piled-up rules cannot be traced or tested. Give agents an identity, have them log attributed diary entries, curate recurring entries into evaluated packs, and let packs that stop helping die.
Practices:
- Give the agent its own identity (bot account, signed commits, own permissions) instead of committing as you [07:18].
- Link each agent commit to a diary entry holding the reasoning [09:23].
- Capture the incident when it happens; his running example is an agent that regenerates the OpenAPI spec and TypeScript SDK but forgets the Go SDK three days running [10:24]-[11:27]. CI would catch it; the aim is to save iterations.
- Accumulate passively, then curate: map scopes, slice by incident type, follow links, fall back to raw search [14:31]-[15:33].
- Render a pack to markdown within a token budget, keeping source entry, human and agent on every section, so the rule reads as "that's how you do things, because we got bitten somewhere" [18:40].
- Evaluate packs on fidelity to entries, usefulness and activation [19:40]-[20:44].
- Run evals in a sandbox with explicit file and network policy [20:44]-[21:46].
- Usefulness test is a replay of the captured incident with and without the pack [23:48].
- Do not consolidate one-offs; act on recurrence [29:03]. Retire packs that regular evals show no longer help: "then it dies" [31:05].
- Curate by hand first, delegate later [31:05].
Evidence and numbers: the Go SDK replay (failed without, "with the pack it was always passing" [24:51]); a near-perfect first fidelity score he distrusts [22:48]. Single case.
Tools and files named: Claude Code, GitHub App bot identity, GPG-signed commits, OpenAPI spec, TypeScript and Go SDKs, a sandbox compared to Codex's, his open-source repository (name not captured in captions). He mentions the term compound engineering [18:40].
Caveats: he stresses it is experimental. The four entry categories are on a slide and not spoken, apart from episodic [13:29]. The problem statement itself: with piled-up rules "you barely can barely say when it's getting used" [02:03]. The autonomous task-claiming section at the end is speculative [24:51]-[27:01].
Relevance: high. The lesson-to-pack-to-skill loop with incident replay is the most concrete self-improvement procedure in the batch.

### One Brain, No Filtering (Robert Overweg, June 2026)
File: refs/videos/rmxRlpi7xN4/transcript.md   URL: https://www.youtube.com/watch?v=rmxRlpi7xN4
Thesis: A small startup put research, meeting transcripts and client material into git-backed markdown vaults that an always-on agent queries in natural language. It works with little structure, but it was painful to build and keep running.
Practices:
- Stack: OpenClaw in a sandbox, a GitHub repo as the store, Obsidian for local browsing, Telegram as the interface [05:08].
- A scheduled job follows chosen accounts and keywords and sends a morning digest; only items he judges important are promoted to the vault, and fewer still become team wikis [07:11]-[08:14].
- Before adopting an outside skill, ask the agent whether it adds anything over existing skills and task files [09:18]-[10:19].
- Plain files were enough at this scale; vector and graph layers were added later and are "not really needed" yet [10:19], [19:30].
- Keep knowledge where you control it: "keep it as much as possible on, like, our own, our own stack" [17:28].
- Separate instances and stores per audience so data does not leak across people, teams and clients [18:28], [28:48].
- Use a cheap model for routine lookups to control spend [21:31].
- Roll out to one person first: "start small, let one person suffer through it first" [21:31].
Evidence and numbers: see (e).
Tools and files named: OpenClaw, Obsidian, GitHub, Telegram, Granola, Omi (recording device), G-Brain (attributed to Garry Tan; caption: Gary Tan), ZeroEntropy, Neo4j (considered), Hermes (not tried), Codex, Haiku. The outside skill pack is attributed to a Google engineer whose name the captions render as Adios Marni; probably Addy Osmani, unverified.
Caveats: Obsidian and git merge conflicts, broken scripts and scheduled jobs, upstream updates breaking half the setup; adding features "becomes a full time job" [19:30]. Permissions for shared client data unsolved [24:36]. No broad tool comparison was done [27:47].
Relevance: medium. Useful evidence that plain markdown plus an agent scales to over a thousand files, and an honest maintenance-cost warning.

### How PMs can set up a product brain (Emma Burrows, Rezonant, June 2026)
File: refs/videos/M6Nhl4zR0uk/transcript.md   URL: https://www.youtube.com/watch?v=M6Nhl4zR0uk
Thesis: Product work is the next bottleneck; a git-backed product wiki kept current by ingestion agents lets an agent triage tickets and route them to a fix or a spec with a human decision in between.
Practices:
- Repo layout: `inputs` (daily queue plus a manual folder), `sources` (raw data, not all kept: "We don't keep all the raw data because sometimes it can overwhelm the agent." [07:11]), `wiki` (customer insight, features, product principles, technical context).
- Three agent roles: one runs workflows, one ingests and restructures inputs, one reorganises the wiki as it ages [06:08].
- Triage rule shown in the demo: a small, well-specified ticket gets options and, once the human picks, goes to a coding agent and a PR; a ticket that overlaps other work gets a recommendation to write a PRD first, "it has not recommended that this goes straight to agent coding" [13:21].
- Feed each outcome back into the input queue so the wiki learns [14:22].
- Keep product documents in git, not in a document suite, so coding agents can read them [19:31].
- Anonymise customer data before it reaches the repo [17:30]. PRs are still reviewed by a person [26:42].
Evidence and numbers: none; a demo, partly pre-run.
Tools and files named: Rezonant, Linear, Granola, Slack, GitHub, MCP connectors, OpenClaw (as a comparison).
Caveats: product pitch; setup per company is still hand-tuned ("an art", [25:42]). Observation worth keeping: "a ticket is basically a full feature now" [21:35].
Relevance: low to medium. The inputs, sources, wiki layout and the fix-or-spec triage rule are the reusable parts.

### Compilation: Cisco and Stanford on Why Skills Are the New Code (AI Native Dev, after June 2026)
File: refs/videos/PabKgxoegGg/transcript.md   URL: https://www.youtube.com/watch?v=PabKgxoegGg
Thesis: Excerpts of GP, JM and JG (already covered, with cleaner captions) plus a Stanford segment not otherwise in this batch.
Practices: the only new material is the Stanford study design, "we've got 500 skills. We have 1000 tasks." [07:19] across 19 model and harness combinations, with tasks sized like well-scoped tickets, and its finding that much skill content is already in the model's weights, so skills should carry what the model cannot know [08:19].
Evidence and numbers: 55% instruction-following with no skill loaded [08:19]; the with-skill number is unreadable.
Caveats: the Stanford passage is badly garbled; speaker names unverified. Worth fetching the full talk.
Relevance: medium, for the single strongest quantitative finding about skill value.

### Compilation: Your Coding Agent Deletes Its Memory After 30 Days (AI Native Dev, after June 2026)
File: refs/videos/Xn7gXeNtoZI/transcript.md   URL: https://www.youtube.com/watch?v=Xn7gXeNtoZI
Thesis: Excerpts of CQ, RO and EM (covered above) plus Brian Douglas of Paper Compute on session transcripts as wasted value.
Practices: Douglas says the harness keeps sessions locally and "after 30 days is deleted" [07:12]; "we're just renting the tokens and then we get no output from it" [07:12]. He runs cleanup and documentation agents in separate VMs, records every session, and uses the recordings to generate skills, docs and context [08:12].
Caveats: short clip; product names garbled; the narrator calls EM Alex.
Relevance: low to medium. One actionable point: keep transcripts if you intend to mine them.

### Compilation: Anthropic, OpenAI and Thoughtworks on Context Engineering (AI Native Dev, after June 2026)
File: refs/videos/wBBCJinOes4/transcript.md   URL: https://www.youtube.com/watch?v=wBBCJinOes4
Thesis: Excerpts of LM and GP (covered above) plus Ryan Lopopolo (OpenAI) and Birgitta Böckeler (Thoughtworks), whose full talks are outside this batch.
Practices:
- Lopopolo: the remaining limits are human time, human and model attention, and the context window. "I max out probably at three concurrent sessions on my laptop." [03:02]; more throughput requires removing your synchronous attention. Conflicting or overbearing requirements in one task degrade results [04:03].
- Lopopolo: with auto-compaction, "I can let a task go for six, 12, 36 hours and still get good results" [04:03], but you must structure and resurface context because "context windows are continually being emptied and filled" [05:06].
- Böckeler: a harness has guides (feed forward) and sensors (feed back); each is either computational (static analysis, codemods such as OpenRewrite) or inferential, where "a review agent is an LLM judging the work of another LLM" [06:08]. Use sensors to trigger self-correction before a human looks.
Evidence and numbers: three sessions; 6 to 36 hour tasks; the recalled Amazon Java-upgrade claim [07:12].
Caveats: clips only.
Relevance: medium. The guides and sensors vocabulary and the compaction warning inform hook and loop design.
