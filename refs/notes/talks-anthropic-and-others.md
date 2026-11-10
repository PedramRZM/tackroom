# Talks and podcasts: Anthropic (Code with Claude 2026) and other agentic-coding practitioners

Sources read: 35 transcripts in full (33 caption transcripts saved with `tools/refs video`, 2 third-party transcripts saved with `tools/refs article`), plus 17 Code with Claude session-page abstracts (title, speaker, date, one paragraph each). Written 2026-11-10/11.

Could not be read or fetched:
- No English captions on any mirror (retried two to four times): SF opening keynote (GMIWm5y90xA), A conversation with Dario Amodei and Daniela Amodei (7xco5Qd2Oo8), What's new in Claude Code SF and London (IMZa42k6L6M, sRvUXLquiRg), Beyond the basics (tuY2ChJIx48) and Stop babysitting your agents (wI0ptqCSL0I) (both replaced by third-party transcripts, see their entries), Spotify's London talk (zFslvuvYifQ; replaced by the Claude-channel interview with the same speaker), Datadog (EdmuYPBt_EM), GitHub (y5TmF_6o6xk), Warp (uGroRwlC9y4), "Embrace long-running tasks with Opus 4.8" (5HVPeux24WU), Cat Wu with Peter Yang (jmHBMtpR36M).
- No recording published: Netflix maturity ladder, Coherence at Claude Code speed, Measure twice cut once, Rearchitecting your workflows (SF), How we Claude Code (SF, Thariq Shihipar's own version), The last mile is the spec and Rewriting Bun in Rust (Tokyo Extended). The Tokyo day exists only as one 8 h 46 min stream (GiqyYQdYoIY), not fetched.
- Session pages: 22 of 39 could not be saved because the page text is under the tool's 600-character minimum; their abstracts add nothing beyond title, speaker and date.
- AI Native DevCon New York, November 2026: only a recap and sub-minute clips were on the channel on 2026-11-10; no full talks. One talk from a Tessl event that mentions Opus 5 (Baz) was read; a third-party upload titled "AI Native Dev NYC" turned out to be the 2025 event.
- Not fetched, to stay within what could be read in full: Lenny's Podcast and Pragmatic Engineer interviews with Boris Cherny and the Y Combinator Lightcone episode (all February to March 2026, superseded here by his later YC and @Scale appearances), Latent Space with Thariq Shihipar, Dwarkesh Patel with Dario Amodei, Vercel Ship 2026. Andrej Karpathy's two talks are already in `refs/videos` under the `people-karpathy` collection saved by another reader and were not re-read here.

Source keys used below: Fung (Running an AI-native engineering org), MemDream, Playbook, HowWe, LiveCoding, Proactive, TeamUses (How the Claude Code team uses Claude Code), Year (Reflecting on a year), VerifyLoops, AutoMode, Keynote (London), ToolSkill, Thinking, Cursor, Model, Remember, Taste, Spotify, OldPrompts (Lance Martin), Osmani, Voss, CodexHarness, NoVibes, YC80 (Cherny at YC), ThariqLoops, FableGuide, Ralph, Scale (Cherny at @Scale), RPIwrong (Horthy 2026), Baz, Krier, CodexCloud, Sandboxes, Babysit, Beyond.

Dating matters: May 2026 sources describe Opus 4.7; Scale (June) describes Opus 4.8 and Fable; YC80 describes Opus 5; OldPrompts describes Opus 5.5. NoVibes (November 2025) and Ralph (January 2026) predate all of them.

## Cross-cutting findings

1. Agent-run verification is the precondition for everything else, and it means running the product, not only tests, lint and types. (Year `[01:00]`, Babysit `[07:23]`, VerifyLoops `[00:00]`, YC80 `[19:32]`, Keynote `[42:04]`, Osmani `[04:18]`, Fung `[11:20]`, Spotify `[11:22]`)
2. Put the verification procedure in one project skill, created by walking Claude through the checks once, and tell the skill to update itself when it hits a blocker. (Babysit `[14:58]`-`[21:08]`, VerifyLoops `[01:01]`, Year `[02:02]`)
3. Work comes back with evidence a human can check quickly: before/after screenshots, a recorded run, measured scores, a test that fails before and passes after. (LiveCoding `[03:05]`, HowWe `[27:14]`, Osmani `[07:22]`, Cursor `[06:19]`, Babysit `[12:58]`, VerifyLoops `[02:02]`)
4. Checks should be measurable and should push off the happy path; unblock them with a login identity and state-seeding scripts. (VerifyLoops `[01:01]`, HowWe `[21:44]`, Babysit `[13:29]`-`[14:14]`)
5. Write corrections into CLAUDE.md or a skill instead of repeating them, but only for failures seen more than once, and prune the whole set when the model changes. (Year `[00:00]`, LiveCoding `[08:21]`, YC80 `[06:15]`-`[08:18]`)
6. Keep always-loaded text to what every task needs; move the rest to skills loaded on demand. (ToolSkill `[21:47]`, Beyond `[18:11]`, Year `[16:16]`, ThariqLoops `[34:45]`)
7. Prefer explanation to prohibition: give reasons, context and both sides of a trade-off; drop examples, shouted rules and patches written for older models. (Playbook `[15:40]`, `[21:51]`; ThariqLoops `[34:45]`; FableGuide `[06:19]`; OldPrompts `[01:15]`)
8. Brief by outcome: the task, guardrails and exit criteria, not an ordered list of steps. (YC80 `[14:25]`, TeamUses `[01:00]`, HowWe `[06:28]`)
9. Before a long run, remove unknowns: interview, blind-spot pass, cheap prototypes or HTML variants, reference code, and implementation notes during the run. (FableGuide `[10:26]`-`[13:28]`, HowWe `[04:24]`-`[09:29]`, ThariqLoops `[09:10]`-`[17:23]`, RPIwrong `[14:17]`)
10. The author must not grade its own work: use a separate context, or a separate model, for review and for permission decisions. (ThariqLoops `[29:39]`, TeamUses `[11:16]`, AutoMode `[00:00]`, Proactive `[11:38]`, Taste `[27:57]`, ToolSkill `[36:04]`)
11. Subagents are for context isolation, parallel search and a fresh reviewer, not for role-play; fold other work back into the main agent. (NoVibes `[06:31]`, ToolSkill `[35:02]`-`[40:09]`, Beyond `[33:26]`)
12. For your own tooling use a CLI plus a short skill; keep MCP for third-party connectors and watch the context cost of tool definitions. (Beyond `[24:34]`-`[25:39]`, ToolSkill `[31:59]`, NoVibes `[05:30]`, CodexHarness `[07:23]`)
13. Unattended runs use auto mode with a configured trust boundary plus hard deny rules, introduced narrowly and widened after watching denials. (AutoMode `[03:06]`-`[05:10]`, Year `[07:07]`, Scale `[36:35]`, Beyond `[44:18]`)
14. Move unattended work off the laptop into an isolated environment with only the access the task needs. (Babysit `[02:06]`, Proactive `[02:27]`, TeamUses `[07:08]`, Sandboxes `[04:18]`, CodexCloud `[03:29]`, OldPrompts `[20:39]`)
15. Step up in order: interactive prompt, then `/loop` on a session, then a routine; good first chores are PR babysitting, docs sync, feedback triage, dead code, flaky or useless tests. (Babysit `[33:35]`-`[35:43]`, Scale `[31:30]`, YC80 `[27:43]`, Proactive `[07:33]`, Year `[04:04]`)
16. Extend trust gradually: recommendation first, action later; merge automatically only what is easy to verify. (Proactive `[19:49]`, Year `[05:07]`, LiveCoding `[14:42]`, AutoMode `[05:10]`)
17. Human attention, not compute, limits parallel sessions: four to five at once, one task in focus, with agent view, naming and colours to cut switching cost. (Babysit `[26:56]`, ThariqLoops `[31:41]`, Beyond `[39:48]`, Spotify `[03:14]`)
18. Protect the prompt cache: stable content first, volatile content last, append-only history, no changing values near the top. (Model `[19:37]`, OldPrompts `[05:20]`, Beyond `[19:59]`-`[21:30]`)
19. Decide model, effort and prompt changes with a small private eval, read the transcripts, and hill-climb with a held-out split. (Model `[03:20]`, `[12:30]`; OldPrompts `[13:30]`; ToolSkill `[10:31]`; Taste `[20:51]`; Playbook `[03:28]`)
20. A consistent codebase, strong tests and an identical starting setup make agents more reliable than extra instructions do. (Spotify `[19:30]`, Cursor `[05:17]`, Baz `[08:19]`, LiveCoding `[08:21]`)

### (a) What Anthropic's own engineers say they do day to day

1. Run in auto mode by default. Cherny uses it "for everything" (Year `[07:07]`); Wu says "most of us are running in auto mode" (Keynote `[32:42]`); Sumner uses it at Bun (LiveCoding `[22:05]`); Hollman and Doko tell audiences to use it (Beyond `[44:18]`, HowWe `[07:29]`).
2. Cherny no longer uses plan mode; he starts a session and moves to the next one (Year `[06:07]`-`[07:07]`).
3. Cherny runs hundreds of agents every night (LiveCoding `[10:25]`) and does most of his coding from his phone through remote control and voice (Year `[14:14]`, Scale `[02:09]`).
4. About 30% of Cherny's code on an average day comes from loops (Scale `[11:12]`); "A lot of my code these days is written by routines" (Keynote `[42:04]`). His own maintenance loops: architecture, flaky tests, useless tests, duplicated abstractions (Scale `[31:30]`); the team runs 20 to 30 one-sentence routines a day (YC80 `[28:43]`-`[29:45]`).
5. When Claude makes a mistake, tell it to write the lesson into CLAUDE.md or a skill (Year `[00:00]`, LiveCoding `[09:24]`).
6. One team-wide verification skill that documents itself (Babysit `[15:14]`); a desktop-development skill that drives the app with computer use (Year `[02:02]`); PRs arrive with screenshots (TeamUses `[17:20]`) and front-end changes with recorded verification runs (HowWe `[27:14]`).
7. Claude Code Review runs on every PR; the human question is whether the PR should exist, plus legal, security-boundary and taste review (Scale `[25:24]`-`[26:26]`, Fung `[13:23]`-`[14:24]`, TeamUses `[09:09]`).
8. Routines in use: docs updated daily and incoming feedback posted to Slack every six hours (Babysit `[35:59]`); a per-feature routine that fixes incoming tickets and one that picks up bug reports unanswered for five hours (Year `[04:04]`-`[05:07]`); weekly docs sync against merged PRs (Proactive `[07:33]`).
9. `/loop` to babysit open PRs through review comments, conflicts and CI (Babysit `[34:36]`, Beyond `[43:47]`); autofix does the same on the PR (Keynote `[35:47]`, `[44:08]`).
10. One focused interactive session plus background sessions: Shihipar keeps one active Claude Code session and runs the rest in Claude Tag (ThariqLoops `[18:26]`-`[19:27]`); another engineer does "70 to 80%" of work in Claude Tag (TeamUses `[01:00]`).
11. Parallel-session mechanics: Hollman keeps long-lived worktrees that track main, each with a persistent agent, and colours and names sessions (Beyond `[39:48]`-`[41:55]`); Bidasaria caps himself at four to five sessions and uses agent view (Babysit `[26:56]`-`[30:28]`); Cherny moved from six terminal tabs to one agent view plus the desktop app's worktrees (Year `[14:14]`).
12. Effort set to xhigh and left there on Opus 4.7 (ToolSkill `[17:42]`, HowWe `[07:29]`). Cherny uses the top model for everything (Scale `[19:19]`).
13. Plans, specs, PR explainers and incident reports are shared as HTML artifacts (ThariqLoops `[14:19]`, HowWe `[10:29]`, TeamUses `[06:08]`).
14. Meeting notes go straight to Claude to pull out quick PRs (Beyond `[14:22]`); stand-up became a skill, and later a Cowork task that asks each engineer for status in Slack (Fung `[21:33]`, Scale `[13:15]`).
15. Technical debates are settled by generating the alternatives as PRs (Fung `[09:18]`); discussion happens on a PR or prototype instead of a design doc (Fung `[10:19]`).
16. The Claude Code system prompt is ablated line by line for each new model (YC80 `[05:14]`).
17. New team members use the explanatory output style to learn the codebase while Claude works (Scale `[39:37]`).
18. At Bun, a bot reproduces every new issue and may open a PR only with a test that fails before and passes after; CodeRabbit and Claude Code Review then argue with the author bot (LiveCoding `[02:02]`-`[05:10]`).

### (b) Primitives for long-running and unattended work, with the guidance given

- `/goal`: keeps the agent from stopping until an exit condition holds and tells it to fill gaps instead of asking. Use when spec work is done and there is a checkable signal such as latency or a rendered design matching a Figma file (ThariqLoops `[01:02]`-`[04:06]`). With Opus 5 Cherny calls it helpful but not required (YC80 `[22:38]`). Codex has the same concept (CodexHarness `[05:19]`).
- Task budgets and effort: an upper bound in tokens before the agent checks in (Thinking `[08:28]`); effort guidance differs by date, see (d).
- `/loop`: runs a prompt at an interval in a live session (a local cron; Claude can cancel it). Needs CLAUDE.md and tools set up so the prompt can be one line. Typical: `/loop 10 minutes` to babysit PRs (Babysit `[34:36]`-`[34:54]`, Beyond `[43:19]`, YC80 `[27:43]`).
- Routines: the same idea on Anthropic's infrastructure, triggered by schedule, GitHub event or webhook; created with `/schedule`. Decide trigger, context (repos, connectors) and how you keep it honest; pair a generating routine with a reviewing one; render or run the output; start with recommendations before actions (Proactive `[04:30]`-`[12:38]`, `[19:49]`; Babysit `[35:06]`; Keynote `[43:05]`). For repetitive work that shares no context but may share memory (YC80 `[27:43]`).
- Dynamic workflows: say "use a workflow"; Claude writes a script that fans out subagents, verifies or filters, and merges. Use for one large task split into chunks, for work judged against a rubric, and when a result needs more compute. The script is a JS file that can live in a skill; deterministic loops guarantee no item is skipped (YC80 `[24:39]`-`[26:43]`, ThariqLoops `[27:34]`-`[30:40]`, TeamUses `[10:11]`-`[13:16]`, Scale `[27:26]`-`[33:32]`).
- Auto mode: a classifier that sees your messages and the tool calls, plus a probe on tool results, after your deny/ask/allow rules. Describe your environment so internal systems are not treated as external; use permission deny rules for hard limits; review production changes yourself (AutoMode, whole video). Hollman's rough cost figure is 30 to 40% more tokens, which she flags as uncertain (Beyond `[44:51]`).
- Remote and sandboxed execution: Claude Code on the web is listed as a prerequisite (Babysit `[02:06]`); setting up the container environment is the painful part (TeamUses `[07:08]`). Outside Anthropic: least privilege and one fresh environment per run (Sandboxes `[04:18]`-`[10:24]`), an onboarding agent and dev CLI so agents can start and wait for services (Cursor `[02:16]`-`[04:17]`), a generated startup skill and script (CodexCloud `[03:29]`). For runs of days: recoverable append-only session log and keys held in a vault the agent cannot read (OldPrompts `[20:39]`-`[21:39]`). Sandboxes can be escaped (Sandboxes `[12:27]`).
- Agent teams and many sessions: enabled in practice by auto mode (Beyond `[44:51]`); agents can message each other (Beyond `[41:55]`); agent view, desktop sidebar and remote control manage attention (Babysit `[27:17]`-`[32:06]`). Counter-guidance: fewer subagents than before (ToolSkill `[40:09]`), context hygiene before orchestration (Model `[20:38]`).
- Memory: files in a directory the agent reads and greps, with read-only shared stores and read-write working stores, version history and an index file (MemDream `[05:16]`-`[08:20]`, Remember `[20:01]`). In Claude Code terms Hollman calls memory "low quality, low cost" and short-lived, distinct from reviewed skills (Beyond `[36:39]`).
- Dreaming: a scheduled out-of-band pass over recent transcripts that deduplicates, removes stale entries, adds cross-session patterns and writes to a cloned store with a diff for review. Managed Agents only, research preview from 2026-05-06 (MemDream `[11:22]`-`[22:37]`, Remember `[13:39]`-`[21:02]`). Inference: the same pattern can be built as a routine over session logs in any harness.

### (c) Advice on CLAUDE.md, skills, hooks, subagents and verification

- CLAUDE.md: called "the single highest leverage thing" in May 2026 (Babysit `[01:31]`). Contents that earn their place: the one build-and-run command, how to run and write tests and where they go, known pitfalls, a folder overview (LiveCoding `[08:21]`-`[09:24]`). Keep only what is needed "regardless of the task" (ToolSkill `[21:47]`). Shihipar thinks most are too long (ThariqLoops `[34:45]`); Cherny says delete it periodically and re-add only on repeated failure (YC80 `[06:15]`-`[08:18]`). It sits in the per-project cache layer, after system instructions and tools (OldPrompts `[06:22]`). Inference: editing it invalidates less cache than changing tools or the system prompt. Plugins are deliberately not allowed to add one (Beyond `[34:47]`).
- Skills: a folder with a markdown file and an always-loaded one-line description; the description needs enough text to trigger, up to 300 to 400 tokens (Beyond `[28:09]`-`[29:44]`). Use for knowledge needed some of the time (ToolSkill `[22:49]`). Do the work by hand first, then ask Claude to turn it into a skill (ThariqLoops `[06:08]`, OldPrompts `[28:47]`, Babysit `[20:38]`). A skill can carry scripts or a workflow file (ThariqLoops `[25:33]`, `[28:37]`). Skills can be hill-climbed against an eval, with a train/test split to limit overfitting (OldPrompts `[14:30]`-`[15:33]`). Split long procedural prompts: under 40 instructions each worked better than one of 85 (RPIwrong `[13:16]`). Capacity for many rules is much higher than in 2025, but adherence still has to be checked (Voss `[07:22]`, `[20:36]`).
- Hooks: cost no context unless they return text; best used as nudges that scale with model ability ("red squigglies"), for example a reminder on generated files or a linter after edits (Beyond `[13:17]`-`[14:17]`, `[30:30]`-`[32:25]`). Anthropic runs hooks on edits that inspect diffs during review (Osmani `[06:21]`). Unconditional context can be injected from a SessionStart hook when really needed (Beyond `[36:00]`). Cherny lists hooks among things to delete and re-test every six months (YC80 `[06:15]`).
- Subagents: system prompt in a separate context, one description line in the parent (Beyond `[33:26]`-`[34:34]`). Two good uses: parallel exploration and an independent reviewer (ToolSkill `[35:02]`-`[37:05]`). Risks: lossy hand-offs and scattered logs (ToolSkill `[38:07]`). For reviewers: instruct them to assume problems exist and hunt for them, ask for reasons before a score, and prefer binary or pairwise judgments (Taste `[28:57]`, `[35:03]`; OldPrompts `[29:49]`-`[31:52]`).
- Verification: mirror what a person does (build, run, inspect UI, logs and data, tests) (Babysit `[07:23]`); four parts for UI work: run, drive a browser, prove with screenshots, unblock with identity and seeded state (Babysit `[12:14]`-`[14:14]`); make failure output readable to the agent (LiveCoding `[09:24]`); expose state so checks do not scrape the DOM (HowWe `[16:39]`-`[17:40]`); lean on end-to-end, property-based and visual tests (Osmani `[09:23]`); fix root causes instead of retrying CI (Keynote `[44:08]`); beware agents faking tests (Krier `[11:27]`) and evals contaminated by git history (Model `[12:30]`).

### (d) Where these sources contradict older advice

- Plan mode before every task: Cherny dropped it for Opus 4.6 and later (Year `[06:07]`). What replaced it is unknown-hunting and short design artefacts, not nothing (FableGuide `[08:22]`, RPIwrong `[14:17]`).
- Heavy prompt and context engineering: "minimal possible system prompt, the minimal possible tools" (Year `[16:16]`); Claude Code's own prompt cut by 80% (YC80 `[03:12]`).
- Many examples and MUST/NEVER rules: examples now constrain, bans over-constrain, reasons work better (FableGuide `[06:19]`, ThariqLoops `[34:45]`, Playbook `[15:40]`).
- "think step-by-step", "double-check your work", "be maximally thorough": remove; they cost tokens and can hurt (OldPrompts `[01:15]`-`[02:16]`).
- The claim that models follow only about 150 to 200 instructions: true for 2025 models, roughly ten times higher in 2026 on a proxy task (Voss `[05:21]`-`[07:22]`); Horthy himself calls his figure dated (RPIwrong `[07:12]`).
- Scaffolding around the model (to-do tool, LLM judge on PRs, fixed planning step): added for weaker models and since removed (TeamUses `[03:04]`, Spotify `[09:20]`, Keynote `[18:24]`).
- A human approving each action is the safe mode: Anthropic now argues the classifier is safer because of approval fatigue (Year `[07:07]`, Scale `[36:35]`, AutoMode `[00:00]`).
- Fresh context every iteration and avoid compaction at all costs (Ralph `[09:14]`): 2026 models are said to run for days on one task with a verifier (YC80 `[01:10]`), and the stated design is to keep a recoverable full log (OldPrompts `[57:13]`). Horthy relaxed his own 40% limit (RPIwrong `[25:30]`).
- The advice that you can stop reading the code: Horthy reversed after six months (RPIwrong `[09:12]`).
- Review long plans carefully: Horthy now reviews a 200-line design and a two-page outline instead (RPIwrong `[08:12]`, `[14:17]`); Anthropic prefers HTML over markdown beyond about 200 lines (HowWe `[10:29]`).
- Role-named subagents: rejected (NoVibes `[06:31]`); fewer subagents overall (ToolSkill `[40:09]`).
- MCP as the default integration: CLI plus skill first (Beyond `[24:34]`, ToolSkill `[31:59]`).
- A smaller model is the cheap and fast choice: a stronger model at lower effort often finishes in fewer turns and tokens (Model `[14:31]`, `[16:34]`; OldPrompts `[17:35]`, `[39:59]`).
- Roadmaps and design docs first: just-in-time planning and PRs as the discussion (Fung `[08:18]`-`[10:19]`).
- Retry flaky CI: fix the root cause (Keynote `[44:08]`).

### Contradictions and open questions

- Effort for coding: default xhigh (Thinking `[22:46]`, May 2026, Opus 4.7) against "try stronger model low effort" first (OldPrompts `[39:59]`, later 2026, Opus 5.5). Both say to measure; neither gives a coding-specific eval result.
- Reading the code: "please read it" for production code (RPIwrong `[10:13]`) against Cherny no longer looking for bugs after Claude Code Review (Scale `[26:26]`) and Osmani's "checking on the agent's evidence" (Osmani `[07:22]`). The Anthropic position depends on a costly automated review that a solo developer may not run.
- How long instructions may be: capacity is high (Voss), Anthropic staff still say shorter is better for behaviour and cost (ThariqLoops, YC80, ToolSkill, Beyond), and one vendor's telemetry shows instruction-file use dropping after a model release (Baz `[14:30]`). Not reconciled by any measurement on real coding tasks.
- CLAUDE.md: "single highest leverage thing" (Babysit, May 2026) against "every 6 months delete your Claude MD" (YC80, later 2026). Compatible only if the file is small and re-earned.
- Hooks: zero-overhead nudges to invest in (Beyond) against "Delete your hooks" (YC80). Inference: instruction-like hooks age with the model; deterministic guards and checks do not, but no source states this.
- Memory volume: "more information actually really does help future sessions" (Remember `[21:02]`) against context minimalism (Year `[16:16]`). They concern different layers (stored for retrieval against loaded up front), but neither source draws that line.
- Scale of parallelism: thousands of agents and nightly fleets (Cherny) against a four-to-five session attention limit (Babysit), "a little mid on agent swarms" (RPIwrong `[10:13]`) and "too much time" on orchestration (Model `[20:38]`).
- Prompt injection: Cherny says they "cannot demonstrate prompt injection anymore" with three layers (YC80 `[03:12]`) and cites about 1% success at 100 attempts (Scale `[38:36]`); the auto mode explainer still tells users to review high-stakes actions (AutoMode `[05:10]`) and Brennan cites a sandbox escape (Sandboxes `[12:27]`). Vendor claims, not independently measured here.
- Open: nearly all numbers are self-reported by vendors (PR counts, token counts, percentages of AI-written code). No source measures these practices for a solo developer or a small repository.
- Open: the "What's new in Claude Code" sessions and both SF keynote and Amodei conversation could not be transcribed, so feature-level details (agent view, autofix, artifacts, mods) rest on mentions in other talks.

## Per source

Captions are auto-generated unless stated, so product and people names are often garbled
("cloud code", "quad code", "cloud MD" = Claude Code, CLAUDE.md). Quotes are copied verbatim from the
saved transcript, including caption errors.

### Running an AI-native engineering org (Fiona Fung, Anthropic, manager of the Claude Code and Cowork team; Code with Claude SF, 2026-05-06)
File: refs/videos/igO8iyca2_g/transcript.md   URL: https://www.youtube.com/watch?v=igO8iyca2_g
Thesis: Coding throughput is no longer the bottleneck on the Claude Code team; the bottleneck moved to verification, review, cross-functional partners and security, so team norms built around expensive engineering time (roadmaps, design docs, stand-ups, review rules) have to be rewritten and old processes deliberately killed.
Practices:
- Name the new bottlenecks explicitly: "verification, review, cross-functional partners, security" `[05:16]`; ask "Is this code correct? Who reviews this code?" and how it is maintained `[05:16]`.
- Planning shrinks and moves late ("JIT planning"): a six-month roadmap "was pretty good for three months" `[08:18]`. Design-doc-before-code is reduced; "instead of a doc, a PR" `[10:19]`, and product reviews are replaced by prototypes dogfooded internally `[10:19]`.
- Technical debates are settled with code: she generated three alternative PRs for an API refactor so the team could compare implementation and caller impact `[09:18]`. Caveat she adds: this needs team culture so that "the last person who check in wins" does not happen `[10:19]`.
- Double down on verification and "shift left": automation that catches bugs before a human or a user does `[11:20]`. Non-engineers (designers, PMs) also ship code, so everyone needs confidence that a change does not break things `[11:20]`-`[12:21]`.
- Code review split: Claude Code Review handles "styling and lint and PR feedback requests", catches some bugs, adds tests and "babysits" PRs `[13:23]`-`[14:24]`; humans are still required for legal review, trust boundaries and security-sensitive code, and product sense/taste `[14:24]`. "It's all about trust but verify." `[14:24]`
- Replace "who made this change?" with the real question (who regressed it, who is the expert, what is the context) and automate that lookup `[12:21]`.
- Morning ritual moved from a manual desktop session (summarise the customer-feedback channel) to a routine `[12:21]`-`[13:23]`.
- Source of truth: "the code is the source of truth" on Claude Code; she answers customer questions by asking Claude Code against a local checkout `[19:31]`. Teams with good specs should check them into the repo and have Claude verify code against the spec `[19:31]`-`[20:32]`.
- Three team principles: every team member (including non-engineers) uses Claude Code; "Claudify everything you can"; "explicit permission to kill old processes" `[20:32]`-`[21:33]`. Example: stand-up, then a spreadsheet, then a stand-up skill/script run by Claude `[21:33]`.
- Principles are re-checked every few months; pods choose their own triage, planning, on-call and what to automate first `[20:32]`, `[22:33]`.
Evidence and numbers: "I don't think I've seen a non-cloud-assisted commit probably in the last 4 months or so." `[24:34]`. Metrics she watches: onboarding ramp-up time, PR cycle time, share of Claude-assisted commits, plus quality/reliability; no figures given ("I can't go into the explicit numbers") `[23:33]`-`[25:37]`. Warns that PR cycle time can expose CI/build infrastructure that cannot keep up `[24:34]`.
Tools and files named: Claude Code, Cowork ("Cowie" in captions), routines, Claude Code Review, a stand-up skill.
Caveats: open questions she lists herself: how far to push fully automated review, and that the trust/verify balance changes with each model `[25:37]`-`[26:38]`.
Relevance: medium. Org-level, but the points on verification as the bottleneck, code as source of truth and killing old processes apply directly to a solo setup.

### Memory and dreaming for self-learning agents (Mahesh Murag, Anthropic platform PM; Code with Claude SF, 2026-05-06)
File: refs/videos/RtywqDFBYnQ/transcript.md   URL: https://www.youtube.com/watch?v=RtywqDFBYnQ
Thesis: Memory is the next agent primitive after MCP and skills. Anthropic models it as a file system the agent manages with bash and grep, and adds "dreaming": an out-of-band batch job that reads recent session transcripts and rewrites the memory store.
Practices:
- Memory is files in a hierarchy that Claude edits with ordinary tools; Opus 4.7 is described as state of the art at file-system memory (what to store, how to split files) `[05:16]`. CLAUDE.md is called "a pretty constrained early version of memory" `[04:15]`; skills are framed as "procedural memory" `[09:21]`.
- Scope memory stores by permission: read-only org-wide store (runbooks, best practices, owners) plus a read-write working store per team/task `[07:19]`, `[17:33]`-`[18:34]`.
- Many agents writing the same store need optimistic concurrency (content hash precondition) `[07:19]`, version history and attribution (which agent, session, time) `[08:20]`.
- Dreaming: a batch, asynchronous job run on a cron or when agents finish; it reads recent transcripts, finds repeated mistakes (for example failed tool calls) and working strategies, and outputs a diff you can apply or review first `[11:22]`-`[12:23]`.
- Design reason: keep objectives separate. Dreaming lets them "separate the memory quality objective from the task completion" objective `[14:29]`, adds no latency to the task, and sees patterns across sessions that one agent cannot `[13:28]`.
- What the dream produced in the demo: a cross-session pattern note, deduplication of five identical entries into one, removal of a stale entry, and a verification note marking a memory as confirmed `[21:35]`-`[22:37]`.
Evidence and numbers: Rakuten reported first-pass mistakes down 90% with memory `[03:15]`; Harvey saw a "six times increase in the task completion rate" on one legal scenario with dreaming `[11:22]`. Both are vendor-reported customer anecdotes.
Tools and files named: Claude Managed Agents memory (public beta), dreaming (research preview, launched 2026-05-06), memory tool, CLAUDE.md, skills, MCP.
Caveats: this is the Managed Agents API, not Claude Code. Limits seen before dreaming: sessions missed learnings from other sessions, and stores went stale or duplicated `[10:21]`.
Relevance: medium. The file-based memory design and the pattern of a separate consolidation pass over transcripts can be copied in any harness with a scheduled job.

### The prompting playbook (Margot van Laar, Anthropic applied AI; Code with Claude London, 2026-05-19)
File: refs/videos/G2B0YWuJUgI/transcript.md   URL: https://www.youtube.com/watch?v=G2B0YWuJUgI
Thesis: Maintain prompts like code: start from an eval set, clean up structure, then fix one failure mode at a time. Many failures after a model migration come from old defensive patches that newer, more literal models now over-apply.
Practices:
- An eval set needs three kinds of case: a control case that should always pass, edge cases that failed before, and cases where the model must hand off to a human or refuse `[03:28]`-`[04:28]`.
- Hygiene first: separate role, guidelines, policy, tone and data with XML tags; remove pasted junk (web-page debris) and false statements such as telling the bot it is human `[08:32]`-`[09:34]`. Rule of thumb: "if you're reading a prompt and you can't tell guidelines from policy from data, most likely the model isn't able to either" `[10:34]`.
- Output contract: define the format, and enforce it in the harness (stop sequence, structured outputs) instead of only in prose `[11:34]`-`[12:35]`.
- Remove stale patches: "Never give a customer the wrong plan details" made the model withhold data it had. Newer models follow instructions more closely, so such lines "have now become redundant and are actually being overfitted to" `[15:40]`. Keep defensive prompt changes in version control with the reason, so they can be reverted `[16:40]`.
- "instructions don't add capability" `[19:50]`: an instruction marked critical to always calculate correctly did nothing; a calculation tool fixed it `[18:44]`-`[19:50]`.
- State both sides of a trade-off. Telling the model only that escalation costs $8 made it never escalate; adding the cost of a wrong answer fixed it `[20:51]`-`[21:51]`.
- For a new agent, compare prompt, model and harness together. A generate, evaluate, repair loop of three small prompts solved all cases with fewer tokens and lower latency than Sonnet 4.6 with one longer prompt; Opus 4.7 with adaptive thinking also passed at about triple the tokens and latency `[27:03]`-`[31:16]`.
- Summary list includes "avoiding long ban lists" `[32:19]`.
Evidence and numbers: toy evals (5 cases, 5 trials), run live; she notes run-to-run variance `[10:34]`.
Tools and files named: XML tags, stop sequences, structured outputs, adaptive thinking, Sonnet 4.6, Opus 4.7, LLM judge vs Python grader.
Caveats: customer-support and scheduling examples, not coding. Inference: the same rules apply to CLAUDE.md and skill text (remove shouted patches, give reasons and both sides of trade-offs, prefer a tool or hook over an instruction).
Relevance: high for how to write instructions and how to test them.

### How we Claude Code (Arnaud Doko, Anthropic applied AI, presenting Thariq Shihipar's SF workshop; Code with Claude London Extended, 2026-05-20)
File: refs/videos/IlqJqcl8ONE/transcript.md   URL: https://www.youtube.com/watch?v=IlqJqcl8ONE
Thesis: As agents run longer, front-load human effort into the spec and build verification into the artifact. Three steps: let Claude interview you, review plans as HTML instead of long markdown, and make the app expose state so an agent can verify it and record evidence. Speaker names in captions are "Arno" and "Tariq"; spellings taken from the session page.
Practices:
- Resist constraining capable models (he cites Sutton's bitter lesson) `[03:24]`-`[04:24]`. Claude "is likely better at extracting what you want" than you are at specifying it `[04:24]`.
- Interview step: the prompt names the domains you care about without fixing the outcome, and explicitly asks Claude to use the AskUserQuestion tool ("ask user question tool"); Claude then writes the spec `[06:28]`-`[09:29]`. Bad prompts he sees: "Make it better" and "make no mistakes" `[06:28]`.
- Settings he recommends: auto mode ("If you're not using auto mode, you need to be using auto mode") `[07:29]`, effort xhigh ("Our recommendation is X high") `[07:29]`, `/effort`, `/fast`, shift+tab to cycle into auto `[08:29]`.
- HTML instead of markdown for specs and plans: markdown over about 200 lines does not get read by you or colleagues `[10:29]`. Ask for several design directions as HTML and compare them; give feedback with screenshots `[10:29]`-`[11:31]`. He says HTML specs are not less token-efficient overall because you iterate less `[30:20]`-`[31:20]`.
- Verification built into the artifact: components publish state to the DOM as data attributes (a "DOM contract"), each component has schemas, fixtures, known states and invariants, and probes push off the happy path `[16:39]`-`[18:40]`, `[21:44]`.
- Three surfaces for the same checks: a human-readable dashboard, agent-driven through Playwright MCP in the browser, and headless (`bun verify`, captions: "run bun verify") for CI `[16:39]`, `[29:17]`.
- Record the verification run as video clips and share them as evidence; "the cloud code team uh records basically all the code changes that they do like this", at least front-end changes `[27:14]`.
Evidence and numbers: none measured.
Tools and files named: AskUserQuestion tool, auto mode, `/effort`, `/fast`, `/goal` (mentioned `[26:13]`), Playwright MCP, Storybook fixtures, Testing Library, Opus 4.7 (recommended over Sonnet here for vision) `[30:20]`, blog post "The Unreasonable Effectiveness of HTML files" (Thariq).
Caveats: the demo repo was a week and a half old; the retention and exact internal tooling for recordings were not described `[28:16]`.
Relevance: high. A concrete recipe for spec interview, plan review and agent-driven UI verification with evidence.

### Live coding session with Boris Cherny and Jarred Sumner (Anthropic; Code with Claude SF, 2026-05-06)
File: refs/videos/DlTCu_pNDHE/transcript.md   URL: https://www.youtube.com/watch?v=DlTCu_pNDHE
Thesis: Bun runs a closed loop: a bot reproduces every new GitHub issue, opens a PR with a test that fails before and passes after, and automated reviewers argue with it until comments are resolved. The remaining bottleneck is human confidence to merge, so the work is in making proof of correctness cheap.
Practices:
- Every new issue triggers a Claude bot ("Robo Bun"/"Robun" in captions) that tries to reproduce it and opens a PR `[02:02]`.
- Hard gate: the PR must include a test that fails on the previous build and passes on the branch; "the bot actually can't submit a PR without that uh being the case" `[03:05]`.
- Two automated reviewers with different jobs: CodeRabbit for style and CLAUDE.md conformance, Claude Code Review for subtle bugs needing full context; the author bot replies, fixes and marks comments resolved (one PR had about 100 comments) `[04:10]`-`[05:10]`, `[21:00]`. Sumner's estimate of Claude Code Review noise: "maybe like 10% of the time it's wrong" `[14:42]`.
- CLAUDE.md content for Bun: the single build-and-run command (so a stale debug build is never tested), how to run and write tests and where to put them, known pitfalls, a folder overview and dependencies `[08:21]`-`[09:24]`. Rule: "every time that you find yourself repeating something it should probably go in cloud MD" `[08:21]`. Cherny: after a mistake repeats once or twice, tell Claude to add it to CLAUDE.md ("compound engineering") `[09:24]`.
- Make failure output agent-readable: print the error message before less informative assertions `[09:24]`.
- Let the agent do the full loop: write, test, read CI errors and build logs, monitor CI `[10:25]`.
- Auto mode for permissions; before it Sumner used `--dangerously-skip-permissions` ("I think I'm not supposed to recommend that") `[22:05]`. Cherny: with auto mode he lets Claude run "for hours and hours", "almost every night" `[29:16]`.
- Hill climbing: give the model a metric and a way to measure it and let it iterate in auto mode (the image library was prompted as "make it faster than sharp") `[18:53]`-`[19:53]`.
- PR monitoring: the session ran commands, then slept 20 minutes and woke up to re-check (Cherny guesses a loop) `[23:08]`-`[24:09]`.
- "PRs become suggestions": not merging an agent PR costs nothing socially, which raises the merge bar `[27:14]`.
Evidence and numbers: the bot is a bigger contributor to main over three months than Sumner `[03:05]`; three to four PRs from one prompt each in about 30 minutes on stage `[24:09]`, `[29:16]`; Cherny: "every night I I'm I'm running like hundreds of agents every single night" `[10:25]`; HTTP/3 server, image API and a Rust rewrite attempt in two weeks `[18:53]`.
Tools and files named: CLAUDE.md, Claude Code Review, CodeRabbit, auto mode, no-flicker renderer (env var heard as "quad code, no flicker equals 1"; exact name not verifiable from captions) `[23:08]`, Discord/Slack @-mention bot.
Caveats: Sumner does not let the bot auto-merge or act on every feature request (taste) `[25:13]`-`[27:14]`; works best because Bun is a CLI/systems codebase where repro and tests are cheap `[06:15]`; he says this was not possible three to six months earlier `[21:00]`. Open problems: communicating "sufficient proof", easy rollback, CI capacity `[16:48]`-`[17:49]`.
Relevance: high. The fail-before/pass-after gate, reviewer-vs-author loop and CLAUDE.md contents are directly reusable.

### Build a proactive agent workflow with Claude Code (Maya Nielan, Anthropic applied AI; Code with Claude London, 2026-05-19)
File: refs/videos/eSP7PLTXNy8/transcript.md   URL: https://www.youtube.com/watch?v=eSP7PLTXNy8
Thesis: Routines turn Claude Code from a tool that waits for a prompt into a teammate that reacts: a remote session defined by a prompt, repos, connectors and a trigger, running on Anthropic's infrastructure.
Practices:
- Create one from the terminal with `/schedule` plus a plain-language request; Claude asks follow-ups (time, notification) and writes the routine instructions `[07:33]`.
- Three decisions for any routine: trigger, context, and how you steer it to "keep it honest" `[08:34]`.
- Triggers: schedule, native GitHub events (for example issue opened, labelled PR merged), or a POST to a webhook with the payload as context `[05:31]`, `[09:34]`, `[15:43]`.
- Context is the ceiling: repos (source plus docs), connectors (Drive, Slack, monitoring) `[10:36]`-`[11:38]`.
- Quality: (1) agent-on-agent review, one routine creates the PR and a second routine triggered by PR creation comments on it (generator/critic) `[11:38]`; (2) open the live session on the web and steer, stop or resume it `[12:38]`, `[17:47]`; (3) verify output, for docs by rendering the changed page `[12:38]`.
- Graduated trust for a deploy verifier: first only an investigation and a go/no-go recommendation; allow automatic rollback only after watching it be right `[19:49]`.
- Example routines: weekly docs sync against merged PRs, docs-gap triage on new issues, deploy verifier on CD webhook, on-call investigator, weekly backlog triage `[07:33]`, `[15:43]`, `[17:47]`-`[20:50]`.
Evidence and numbers: "weekly PRs for Claude Code have gone up 200% since the beginning of the new year" `[06:31]`; one engineer maintains docs for Claude Code and the Agent SDK with these routines `[06:31]`.
Tools and files named: routines, `/schedule`, Claude Code on the web, GitHub and Slack connectors, webhooks.
Caveats: local cron was rejected because sessions die with the laptop and headless runs are hard to watch or resume `[02:27]`-`[03:29]`.
Relevance: high for unattended work: trigger/context/steering checklist and the graduated-trust pattern.

### How the Claude Code team uses Claude Code (Anthropic Claude Code engineers; Claude channel, 2026, exact date not in the file; after Claude Tag shipped)
File: refs/videos/S-sYlFiGFv8/transcript.md   URL: https://www.youtube.com/watch?v=S-sYlFiGFv8
Thesis: A round-table of Claude Code engineers (captions name "Sid" and "Robert"; a third speaker designed the AskUserQuestion tool, probably Thariq Shihipar, not named). Their work has moved from supervising transcripts and tool calls to handing goals to a Slack-native agent (Claude Tag), with loops, routines, workflows and verification as the supporting primitives. Harness features are scaffolding for the current model and get deleted as models improve.
Practices:
- Delegate goals, not steps: "I have a goal and I'd like to achieve this goal" replaces caring about "each individual tool call" `[01:00]`. One engineer does "70 to 80%" of work in Claude Tag and opens the TUI or desktop app for the rest, to refine or micromanage `[01:00]`.
- Harness features have a shelf life. The to-do list was added when Sonnet 3.5 would do three of five tasks and "give up"; a year later "you don't really need the to do list anymore" `[03:04]`. Features exist "to cover for some of the failure modes" of the current model and are removed later `[04:04]`.
- AskUserQuestion: hard to get the model to call well at first; now the designer mostly has Claude create an HTML artifact that asks the questions with diagrams and mock-ups `[05:06]`-`[06:08]`.
- Loop journey: laptop sessions, then remote dev boxes, then Claude Code on the web (hosted containers), then routines. Setting up the container dev environment is "a bit of a pain" but gave "10x my productivity" `[07:08]`. Example routine: every day read incoming feedback, bucket by importance, fix the ones it has high confidence in `[08:08]`.
- Code review: Claude handles nit-picks autonomously and directs humans to the bigger picture (why an API or service boundary is shaped as it is) `[09:09]`-`[10:11]`.
- Workflows grew out of code review: fan out to find candidate bugs, then for each bug an adversarial review from three perspectives to check it is real, then coalesce ("MapReduce") `[10:11]`-`[12:16]`. Because Claude writes code to orchestrate subagents, a for loop "it's not going to skip one of the items" `[13:16]`. Claude designs the fan-out topology itself `[11:16]`-`[12:16]`.
- Make the dev loop easy for the agent: Claude must be able to do everything a human does to build and test end to end `[14:17]`.
- Verification on their PRs: Claude tests the change and sends screenshots; one engineer had Claude record itself using the TUI, then still cloned and tried it himself as a sanity check `[17:20]`-`[18:20]`.
- Ask for outcomes at a higher level ("improve the funnel") and give your own idea as one example instead of the instruction `[16:19]`-`[17:20]`.
Evidence and numbers: self-reported shares of work only.
Tools and files named: Claude Tag (Slack agent), TUI, desktop app, Claude Code on the web, routines, loops, workflows, auto mode, memory, artifacts, AskUserQuestion.
Caveats: the model "fundamentally shifts underneath you every two months" `[02:03]`, so any fixed setup decays.
Relevance: high. First-hand description of daily practice and of which harness features they consider temporary.

### Reflecting on a year of Claude Code (Anthropic; Claude channel, 2026, around the one-year mark; speakers not named in captions, by content Boris Cherny, Cat Wu and a third team member)
File: refs/videos/Hth_tLaC2j8/transcript.md   URL: https://www.youtube.com/watch?v=Hth_tLaC2j8
Thesis: The two ideas that matter most are compounding corrections into CLAUDE.md or skills and giving the agent a way to run the thing it built. With Opus 4.6/4.7-era models the speakers dropped plan mode for auto mode and call themselves context minimalists.
Practices:
- Corrections compound: "I don't tell Claude to do it differently, I tell it to write it to the CLAUDE.md," or make a skill `[00:00]`-`[01:00]`.
- Verification is not unit tests, lint or type check (those "were already automated"); it is "can the agent run the thing?" `[01:00]`. Examples: Claude testing its own CLI in bash; loops for iOS simulator, Android simulator and desktop computer use `[01:00]`-`[02:02]`.
- A "desktop development skill" teaches Claude to run the local desktop app and click through new UX with computer use, including edge cases; when it hits an environment problem it reads Slack to see if staging is down, and after debugging the speaker tells it to update the skill `[02:02]`-`[03:03]`.
- Routines in use: one listens for every ticket about a feature (voice mode), puts up a fix and pings the owner; another picks up bug reports not answered in five hours, and the owner merges "the ones that are easy to verify" `[04:04]`-`[05:07]`. Routines do code review and babysit PRs (review comments, CI, rebase) `[06:07]`.
- Plan mode dropped: go-to features "used to be" plan mode; "I don't use that anymore", auto mode instead, because newer models "don't actually need like a planning step anymore" (needed for Opus 4 to about 4.5) `[06:07]`-`[07:07]`. Caveat in the same breath: "some people still use it. They like to have that artifact." `[07:07]`
- Auto mode rationale: people accept about 99% of prompts and stop reading, so a classifier is "more safe than reading every single permission prompt" `[07:07]`-`[08:09]`. It was validated on thousands of transcripts plus red-team prompt-injection attempts turned into evals `[09:10]`.
- Loop/routine as the next abstraction: "I talk to loop or I talk to a routine and it prompts Claude for me" `[10:11]`.
- Managing many agents: previously six terminal tabs with six checkouts; now one tab with agent view, the desktop app creating worktrees, and "probably half my engineering now I do on my phone" through remote control and voice `[14:14]`-`[15:16]`.
- Context minimalism: "You give it the minimal possible system prompt, the minimal possible tools, and then you let the model figure it out", plus a way to pull context in `[16:16]`. Second speaker: "tell the model only what it needs to know"; too much context is micromanaging; the harness prompt is being made leaner `[16:16]`.
Evidence and numbers: none measured; "tree of like thousands of agents" is a self-description `[00:00]`.
Tools and files named: CLAUDE.md, skills, routines, loop, auto mode, plan mode, agent view, desktop app worktrees, remote control, voice mode, Agent SDK, Cowork.
Caveats: this contradicts the long-standing advice to always plan first and to engineer context heavily; the speakers tie each technique to a model generation (prompt engineering for Sonnet 3.5, context engineering for Opus 4) `[16:16]`.
Relevance: high. The clearest statement of what Anthropic's own leads stopped doing.

### Building verification loops in Claude Code (Anthropic explainer; Claude channel, 2026, date not in the file)
File: refs/videos/mQZB0l-rhxE/transcript.md   URL: https://www.youtube.com/watch?v=mQZB0l-rhxE
Thesis: Tests, type checks and linters do not prove a change does what you meant; codify the manual check you do afterwards so Claude runs it.
Practices:
- Start with the bundled verify skill: on first use it runs the app, checks the change in the app, then "saves the steps that worked as a skill in your project"; treat that as a starting point and extend it `[01:01]`.
- In the skill say "when Claude should run it, what to do when a check fails, and what proves each check passed" `[01:01]`. "The more measurable a check is, the easier it is for Claude to tell whether it's passed or not." `[01:01]`
- Example measurable check: layout shift via a performance trace through Chrome DevTools MCP (Core Web Vitals) `[01:01]`; result returned with screenshots and scores `[02:02]`.
- Trigger for adding a check: whenever you catch yourself checking by hand and telling Claude what to fix; candidates are a performance budget, an accessibility checklist, design-system rules `[02:02]`.
Tools and files named: verify skill, Chrome DevTools MCP, browser, terminal, iOS simulator.
Relevance: high. Short, but it is the official recipe for a project verify skill.

### How auto mode works with Claude Code (Anthropic explainer; Claude channel, 2026, "a few months" after auto mode launched)
File: refs/videos/b8SV4U6fEIc/transcript.md   URL: https://www.youtube.com/watch?v=b8SV4U6fEIc
Thesis: Auto mode replaces per-action approval with a separate classifier plus an injection probe, inside a trust boundary you configure.
Practices:
- The classifier sees your messages and Claude's tool calls, not Claude's reasoning, replies or tool output, and checks actions against your intent, looking for anything "irreversible or destructive" beyond what you asked `[01:05]`. On denial Claude tries a safer route (push to a new branch instead of force-pushing main); repeated denials pause for you `[01:05]`.
- A server-side probe scans every tool result for injected instructions and flags suspicious content before it enters context; an attack must pass both layers `[02:06]`.
- Order of evaluation: your deny, ask and allow rules first, then a tier check. Read-only or recoverable actions (search, edits in the project) skip the classifier; shell commands, web fetches and anything leaving the environment go through it `[02:06]`-`[03:06]`.
- Configure the boundary: by default only the working directory and git remotes count as internal. Describe your GitHub org, buckets and internal services in the `environment` field (managed settings for admins, user settings for additions); setting it replaces the built-ins unless you add the default string `[03:06]`-`[04:07]`.
- `allow`, soft deny and hard deny in that config are guidance to the classifier, "not hard rules". For hard limits use permission deny rules, and ask rules to force a prompt even in auto mode; broad allow rules that grant arbitrary code execution still go to the classifier `[04:07]`.
- Rollout: "start narrow. Watch what gets denied and then widen"; review production-infrastructure changes yourself or build your own evals `[05:10]`.
Evidence and numbers: "97% of permission prompts in Claude Code get approved" `[00:00]`; with probes and auto mode "the attack success rate in our evaluations dropped to zero" `[02:06]` (Anthropic's own evaluation; no sample size given).
Relevance: high. Exact layering of permission rules, classifier and probe for unattended runs.

### Code with Claude London 2026: Opening keynote (Boris Cherny, "Lisa" of research PM, Angela Jiang, "Caitlyn", Cat Wu; 2026-05-19)
File: refs/videos/6amLO7I9xdg/transcript.md   URL: https://www.youtube.com/watch?v=6amLO7I9xdg
Thesis: Model capability is exponential while adoption is linear; the product answer is primitives that let Claude run asynchronously and prompt itself (routines, autofix, code review, security scans) with verification as the enabler.
Practices:
- Build for the next model: "the scaffolding that used to help can hold Claude back"; more capable models get further with general primitives such as a file system and a sandbox `[18:24]`. Keep making harder evals; a task that starts passing is the signal to ship `[19:25]`.
- Advisor strategy on the API: a smaller executor (Haiku or Sonnet) asks a larger model for advice through a tool; Sonnet with an Opus advisor did better and cheaper than Sonnet alone in their test `[21:27]`-`[22:29]`.
- Cat Wu's before/after: a year ago she read every edit and permission prompt; now "most of us are running in auto mode" and check in after Claude has tested, verified and opened a PR `[32:42]`.
- Feature list tied to bottlenecks: Code Review (a team of agents), remote control and mobile, autofix (fixes flaky CI, review comments, merge conflicts so the PR stays green), routines (schedule, webhook, API), Claude Security (overnight scan ranked by severity) `[34:44]`-`[36:50]`.
- Cherny: "A lot of my code these days is written by routines"; "Routines are a higher order prompt." `[42:04]`-`[43:05]`. Routines can run locally or on remote compute `[43:05]`.
- Async needs verification: "If cla can check its work, you can just let it run while you work on something else" `[42:04]`. Demo: Claude drives the dashboard in a browser, sees a modal close before the success toast, traces a race condition, fixes and re-verifies `[40:52]`.
- On flaky CI, the demo routine retried the job; in the Claude Code codebase "we tell it to fix the root cause instead, not just retry" `[44:08]`.
Evidence and numbers: Spotify's background agent merges "over a thousand PRs a month" and cuts migration time "by over 90%" `[05:03]`; average Claude Code developer runs it "over 20 hours a week" `[09:15]`; "200% increase in the number of PRs per engineer" at Anthropic `[34:44]`; Mercado Libre: 23,000 engineers, over 500,000 PRs reviewed, target of 90% autonomous coding by Q3 `[37:50]`-`[38:51]`; Rakuten: three times more production tasks resolved with Opus 4.7 `[15:20]`. All vendor-reported.
Tools and files named: Opus 4.7, Mythos preview, agent view, desktop app, routines, autofix, Code Review, Claude Security, remote control, Managed Agents (outcomes, dreaming, multi-agent orchestration, self-hosted sandboxes, MCP tunnels), advisor tool.
Caveats: keynote; model limits admitted: verbal tics and "sometimes does more than you asked for" `[16:21]`.
Relevance: medium. Useful as the map of primitives and for the rule to fix the root cause instead of retrying.

### Tool, skill, or subagent? Decomposing an agent that outgrew its prompt (Will Steuk, Anthropic applied AI; Code with Claude London Extended, 2026-05-20)
File: refs/videos/mWvtOHlZM-I/transcript.md   URL: https://www.youtube.com/watch?v=mWvtOHlZM-I
Thesis: An agent that accreted a 400-line system prompt, 12 tools and three wrapped subagents regressed. The fix was a 15-line prompt, business logic moved to skills, tools collapsed to bash/read/write, and one subagent kept for a job that needs a clean context.
Practices:
- System prompt: "Leave the system prompt only for the information that Claude needs in its mind, regardless of the task" `[21:47]`; skills hold what is needed "some of the time, not all of the time" `[22:49]`. The prompt went from about 400 lines to about 50 and finally 15 `[24:51]`, `[41:10]`.
- Failure causes found by eval triage: the model reasoning where it lacked a tool, output-structure mismatches between subagent and orchestrator, and two contradictory policies far apart in the long prompt (the model used a 1.35 multiplier instead of the retrieved 3.1) `[08:29]`-`[09:30]`, `[18:45]`-`[19:46]`. "this isn't a model problem", it is a context problem `[09:30]`.
- Tools: start from human-like primitives (file system, code execution, web search, sometimes a to-do list), remove what is not needed, add custom tools only when needed `[26:53]`-`[30:58]`. Giving bash so Claude writes a script beats loading a CSV into context `[27:53]`.
- MCP last: "We don't run to MCP"; use local custom tools first and publish an MCP server only when several clients need the same governed tools `[31:59]`. MCP "can cause some context issues"; CLIs or API calls from code are an alternative `[33:00]`.
- Subagents have two good uses: parallelism ("throw a lot of Claude at a problem": research, codebase exploration) and "a fresh mind" (review by an instance without the author's context; a forecast kept away from the customer conversation) `[35:02]`-`[37:05]`. Otherwise fold the work back into the main agent: "you just don't need as many sub-agents" `[40:09]`.
- Subagent risks: orchestrator-to-subagent communication loses information, and logs across agents are hard to collect `[38:07]`.
- Method: run evals, have Claude Code triage failures into themes, change one thing, rerun ("hill climbing"); keep evals updated as capability grows `[10:31]`, `[18:45]`, `[43:13]`. Graders: deterministic (turn count, latency, tokens) plus LLM judge for tone and quality `[05:26]`-`[06:28]`.
- Presenter's Claude Code setting: Opus 4.7 with effort "extra high", "and I forget about it" `[17:42]`.
Evidence and numbers: eval pass rate 83% nominal (62% on the live run, 7 of 12) to about 92% after `[17:42]`, `[42:11]`; one task dropped from over 200,000 tokens after switching to code execution `[34:01]`. Workshop repo with 12 tasks, not a production measurement.
Tools and files named: Claude Managed Agents, callable agents, skills, bash/read/write, MCP, `uv run evals --agent before` (as heard).
Caveats: he notes results can regress in other cases `[35:02]`.
Relevance: high. A direct decision rule for prompt vs skill vs tool vs subagent, from Anthropic staff.

### The thinking lever (Matt Bleifer, Anthropic research PM; Code with Claude SF, 2026-05-06)
File: refs/videos/OXJO4LldSnc/transcript.md   URL: https://www.youtube.com/watch?v=OXJO4LldSnc
Thesis: Test-time compute is a second axis of capability. Control it with the effort setting and task budgets, not with a thinking on/off toggle; adaptive thinking lets Claude interleave thinking, tool calls and text freely.
Practices:
- Default recommendation for coding: "go with extra high" `[22:46]`. xhigh was introduced with Opus 4.7, is "the best setting for most coding and agentic use cases" and the default in Claude Code and Claude.ai for Opus 4.7 `[18:40]`.
- Other levels: max for the hardest tasks but with diminishing returns; high to balance tokens and intelligence; medium for cost-sensitive work; low for short-scope and latency-sensitive tasks `[17:39]`-`[18:40]`.
- Low effort takes shortcuts: "you may catch it taking unexpected shortcuts", so read transcripts at each level `[15:36]`.
- Thinking toggles are "a poor proxy for an effort dial": they switch a capability off instead of saying how hard to work `[13:34]`. Enable thinking whenever possible and modulate with effort or budgets `[21:43]`.
- Task budgets: an upper bound in tokens (later time or cost) before Claude stops and checks in, for example 100,000 tokens `[08:28]`.
- Small model or low effort on a big model: "use small models for a fast time to first token, use bigger models at lower effort for a fast time to last token" `[20:43]`. Small models for bulk classification, extraction, basic summarisation `[20:43]`.
- Where possible plot your own eval score against tokens, time or cost per effort level and per model `[14:35]`, `[21:43]`.
Evidence and numbers: one demo prompt on Opus 4.7: low about 50 s and 4,600 output tokens; high about 2x both; max about 10x both, with visibly better output each step `[02:19]`-`[04:21]`. Opus 4.7 low used about the same output tokens as Haiku 4.5 max with a better result `[19:42]`. Adaptive thinking is used for all Anthropic benchmarks since Opus 4.6 `[12:32]`.
Tools and files named: effort levels (low, medium, high, xhigh, max), task budgets, adaptive thinking, interleaved thinking.
Relevance: high for setting effort per task type and per subagent.

### Giving coding agents their own computers: How Cursor built cloud agents (Alexi Robbins, Cursor; Code with Claude SF, 2026-05-06)
File: refs/videos/BbYSGxtsMic/transcript.md   URL: https://www.youtube.com/watch?v=BbYSGxtsMic
Thesis: The bottleneck is no longer model intelligence but humans giving agents tools, context and ambitious tasks. Cursor onboards agents like new hires (a computer, a working dev environment, docs), then has agents report and fix their own friction ("agent experience").
Practices:
- An onboarding agent explores the repo "not to make a change but to figure out how to run it", working out services, environment variables and permissions with the developer, and returns a demo `[02:16]`-`[03:17]`.
- Agent dev-experience tooling: a dev CLI to start services, wait for readiness, check status, create test accounts and sign in to third-party services, because agents were "spending a lot of time sleeping" `[03:17]`-`[04:17]`.
- Principles: give agents eyes (anything you can see, including app state you changed and other agents' chats) `[04:17]`-`[05:17]`; give them tools to do what you can do, within security constraints `[05:17]`; keep code and instructions high quality because "agents are auto regressive" `[05:17]`.
- Computer-use demos: the agent records a video of the feature working, which is both its end-to-end test and "a really high bandwidth method of reviewing the work of the agent before you get into code" `[06:19]`.
- When an agent fails, stop and fix the cause, because failure modes are "multiplied out across your whole team" `[08:21]`-`[09:23]`.
- Self-improvement loop: every cloud agent gets a skill (captions: "WCF skill", "work on the factory"; acronym unclear) telling it to report anything "annoying, broken, or confusing" instead of grinding through `[11:26]`. Reports go to a system of record; a manager agent categorises and dedupes them into technical problems, permission gaps and "ignorance" needing a human answer `[10:24]`.
- Fixes to flaky dev-environment problems are validated by launching many more cloud agents with the change, an eval set for the fix, before a human reviews the PR `[12:27]`.
Evidence and numbers: none.
Tools and files named: cursor.com/onboard, cloud agents, computer use.
Caveats: vendor talk; cloud isolation framed as what makes autonomy safe (no access to your local environment variables) `[08:21]`.
Relevance: high. The skill that reports friction and the dev CLI for waiting on services are cheap to copy.

### Picking the right model (Lucas Smedley, Anthropic applied AI; Code with Claude London, 2026-05-19)
File: refs/videos/P0uMXS6emHA/transcript.md   URL: https://www.youtube.com/watch?v=P0uMXS6emHA
Thesis: Choose model and settings with a small private eval, optimise for cost per successful outcome, and shift the cost/quality curve with prompt caching and clean tool output.
Practices:
- "the right model is not the model that is cheapest per token"; it is "cheapest per successful outcome" `[24:42]`.
- Grade the working, not only the answer: outcome graders plus checks on steps (the right tool called, the right argument) `[06:24]`-`[07:24]`.
- Eval gotchas: run each task several times (variance means an ill-defined task) `[08:25]`; separate infrastructure failures (API or tool errors) from model failures `[09:26]`; keep the set representative by feeding production failures back `[10:27]`.
- Read transcripts. Example: a coding eval looked great until transcripts showed Claude reading git history from earlier trials and "extracting the answer from there" `[12:30]`.
- Re-tune prompts per model: one tool was "drastically under-triggered" on Opus 4.5 and "drastically over-triggered" on Opus 4.6 with the same prompt `[11:30]`. Feed the new model's prompting guide to Claude and ask it to update your prompts `[10:27]`.
- Bigger models can be faster and cheaper overall because they need fewer turns `[14:31]`, `[16:34]`.
- Prompt caching: cached input costs one tenth; aim for an 80 to 90% cache hit rate; keep the message array append-only and avoid dynamic values such as a timestamp in the system prompt `[18:36]`-`[20:38]`.
- Context hygiene beats elaborate orchestration: "people spend too much time thinking about these like super complex multi-agent orchestration systems" `[20:38]`. Clean tool responses (markdown instead of JSON, short dates, add day of week) `[21:40]`.
Evidence and numbers: tool-response clean-up cut tokens 66.4% `[21:40]`; deduplicating search results cut input tokens 77% and cost 65% while accuracy rose 9% `[22:40]`; internal code-fix pipeline: Haiku 4.5 without thinking 92%, with thinking 100%, Sonnet and Opus 100% in less time `[13:30]`-`[14:31]`.
Tools and files named: tau-bench (captions: "Tao bench"), LangSmith, Braintrust, a model-sweep skill in the workshop repo.
Relevance: medium to high. Supports per-task model choice and lean tool output; the append-only caching rule matters for hooks that inject context.

### Agents that remember (Kevin Chen, Anthropic; Code with Claude London Extended, 2026-05-20)
File: refs/videos/geUv4CjPpxI/transcript.md   URL: https://www.youtube.com/watch?v=geUv4CjPpxI
Thesis: Workshop version of the memory and dreaming talk for Managed Agents: mount a memory store as a file system, then run dreaming so the store does not grow unbounded, stale and duplicated.
Practices:
- Memory store is mounted in the session container; the agent checks it first, greps for keywords, and writes files such as `sessions.md` `[06:29]`, `[09:33]`-`[11:37]`. Each mount takes a prompt saying what to remember and an access mode (read-write default, or read-only) `[08:31]`.
- Without consolidation agents "start just kind of dumping information" every task `[13:39]`.
- Dreaming is non-destructive: it clones the input store to an output store and shows a diff for human review `[18:58]`, `[20:01]`-`[21:02]`. One subagent per input session so the pass is exhaustive `[22:03]`.
- What the dream added: an index file of slugs pointing to memory files, so a later agent reads the index instead of doing a wide grep; extra detail and metadata on existing files `[20:01]`.
- Their finding: "more information actually really does help future sessions", since the writing agent cannot predict what will be needed; dreaming can prune later `[21:02]`.
Evidence and numbers: dreaming expected to hit about a 95% prompt-cache rate `[26:13]`; up to about 100 sessions per dream `[15:43]`.
Relevance: medium. Inference: an index file plus periodic consolidation is the part worth copying for a file-based memory in a coding repo. Note the tension with the "context minimalist" stance in "Reflecting on a year of Claude Code": that concerns what is loaded up front, this concerns what is stored for retrieval.

### Evals for taste: Hill-climbing a slide-generation agent (Jiri De Jonghe, Anthropic; Code with Claude London Extended, 2026-05-20)
File: refs/videos/v9FTCvkV_a0/transcript.md   URL: https://www.youtube.com/watch?v=v9FTCvkV_a0
Thesis: Build your own evals with code graders for what is countable and model judges for what is not, then loop: find failures, change the prompt or model, rerun, and recalibrate the graders themselves.
Practices:
- Grader types: code-based (fast, cheap, deterministic, brittle), model-based (rubric, pairwise comparison, multi-judge majority), human (best, slowest) `[08:36]`-`[12:41]`. Drop any grader that gives no actionable information `[17:47]`.
- Judges need anchors and reasons first: an unanchored 0 to 5 rubric gave 5 for images to a deck with no image `[33:02]`-`[34:03]`. Ask for pros and cons before the score, because a model that outputs the number first "will do anything it can to argue why it should be a four" `[35:03]`-`[36:04]`.
- QA loop as a general pattern: a second agent criticises, the first fixes, repeat. Prompt wording used: "Approach QA as a bug hunt, not a confirmation step" and assume there are problems; require at least one fix-and-verify cycle with rendered images `[27:57]`-`[28:57]`.
- Evals are "a living artifact"; when scores saturate or disagree with your eye, fix the grader `[20:51]`, `[24:54]`.
- Try a stronger model with the bare prompt before adding rules: Opus 4.7 with the original one-line prompt beat the heavily prompted Sonnet 4.6 and used no emojis unprompted `[31:00]`-`[33:02]`.
Evidence and numbers: workshop scores only.
Relevance: medium. The judge-calibration points (anchors, reasons before score, adversarial QA wording) apply to reviewer subagents.

### How Spotify runs agents across 20M+ lines of code (Niklas Gustavsson, Spotify, interviewed by an Anthropic host who is not named in captions; Claude channel, 2026)
File: refs/videos/9DHZLw5653E/transcript.md   URL: https://www.youtube.com/watch?v=9DHZLw5653E
Thesis: Spotify's background agent ("Honk") works because of earlier investment in fleet-wide automation, test automation and standardisation; the same engineering practices that helped humans help agents.
Practices:
- Personal setup: 5 to 10 tmux tabs, each a Claude session paired with a terminal pane for git diff, across a set of worktrees `[03:14]`.
- Monorepo of more than 20 million lines works well; Claude uses other code in the repo as a model for the problem `[04:15]`. Consistency matters: if patterns "look in 10 different ways claude is going to be more confused" `[19:30]`.
- Honk architecture: Agent SDK in a Kubernetes pod with tools; the key tool lets it run verification (CI builds on Linux and macOS, sometimes the iOS simulator) `[10:20]`-`[11:22]`.
- The LLM judge was removed: it took PR success from roughly 20-30% to 80% in early versions, but after Opus 4.5 "we don't didn't need judge anymore" `[09:20]`-`[10:20]`.
- Auto-merge required stronger tests: teams were told they "might not no longer be in the loop", so test automation had to carry the checking `[12:23]`-`[13:24]`.
- Host's framing: to go faster, encode quality practices "in a skill or in a quad MD or in some set of MCPS" so Claude can run them `[13:24]`.
Evidence and numbers: codebase grew about seven times faster than headcount `[05:16]`; about 4,500 production deployments a day `[14:25]`; 2,900 engineers `[16:25]`; "75% plus improvement in PR frequency" attributed to AI tooling and about 73% of PRs AI-authored `[16:25]`; quality metrics "neutral" `[14:25]`. Self-reported.
Tools and files named: Honk, fleet management, Claude Agent SDK, tmux, worktrees, Figma-to-UI with simulator.
Caveats: the Code with Claude London talk by the same speaker (zFslvuvYifQ) had no captions available; this interview was read instead.
Relevance: medium. Supports putting tests and consistent patterns first, and is a dated example of scaffolding (the judge) being removed.

### Your Old Prompts Are Making Claude Worse (Lance Martin, Anthropic; AI Engineer channel, second half of 2026: refers to Opus 5.5, Sonnet 5, Haiku 5.5 and Fable as current)
File: refs/videos/ys6YQ2yfBpM/transcript.md   URL: https://www.youtube.com/watch?v=ys6YQ2yfBpM
Thesis: Most applications sit inside the cost/quality frontier because of small misconfigurations: prompts carrying debt from older models, a broken prompt cache, wrong effort, and weak evals. Fix those, then let Claude hill-climb on a well-built eval.
Practices:
- "prompts accumulate debt just like code" `[01:15]`. Patterns he says frontier models no longer need: "think step-by-step", verification rituals ("double-check your work"), thoroughness boosters ("be maximally thorough"), scratch pads telling the agent how to think `[01:15]`. They raise cost and can lower performance `[02:16]`.
- Contradictory rules: older models ignored one of the two; "with frontier models, they'll often get confused by contradictory rules" `[02:16]`.
- Claude Code ships skills that audit prompts, skills and tools in the working directory for these anti-patterns and remove them. Heard as "checkup prompt audit" (for your Claude Code configuration) and "Claude API prompt audit" (for code that calls the API); exact command spelling not verifiable from captions `[02:16]`-`[03:16]`. The audit has model-specific caveats (smaller models may still need more guidance) `[50:09]`. He places the turning point at roughly Opus 4.5, hedged as "a little bit squishy" `[49:08]`-`[50:09]`.
- Prompt cache: strict prefix match, a single changed byte in the prefix "will invalidate the cache" `[05:20]`-`[06:22]`. Order prompts from global (system instructions, tools) to per-project (CLAUDE.md, memory) to per-session state to per-turn messages `[06:22]`. Claude Code tracks cache hit rate "very very religiously" `[06:22]`.
- Eval design checks: score rises with model size and with thinking, headroom exists at the frontier, run-to-run variance is low `[09:25]`. Ambiguous tasks create fake headroom that burns tokens `[10:26]`.
- Hill-climb skill (heard as "Claude API hill climb"): splits the eval into train and test, reflects only on train failures, reports both each round; train up with test flat signals overfitting `[13:30]`-`[14:30]`. If stuck for several rounds it clusters remaining failures to find ambiguous cases or bad graders `[36:57]`. "It's not guaranteed to converge at all." `[35:57]`
- Best surfaces to hill-climb: prompts and skills (small, tightly coupled to behaviour) but they overfit easily; harness code is harder to interpret `[26:46]`-`[27:46]`.
- Graders: prefer deterministic checks; otherwise a rubric a human could apply, binary instead of 0-5 or 1-10 scales ("That's extremely noisy"), agreement across several models, replicates, pairwise comparison for ambiguous quality; grade with smaller, cheaper models `[29:49]`-`[31:52]`, `[33:53]`.
- Effort guidance without an eval: "try stronger model low effort in general", then dial up; starting at max is "extremely token" hungry `[39:59]`-`[41:02]`. Effort is a suggestion of how hard to think, "not a hard cap" `[51:10]`. On frontier coding problems xhigh or max can use far more tokens than medium or low "without much difference in actual outcome" `[52:11]`.
- Turning a repeated procedure into a skill: do the workflow once, then tell Claude "turn this into a skill" `[28:47]`.
- Long-running design: keep the session log as an append-only object separate from harness and sandbox so either can die and be recovered; secrets stay in vaults the agent can reference but not read `[20:39]`-`[21:39]`. Compaction should not destroy context: keep the full log queryable `[57:13]`-`[58:14]`.
- Eval set composition: do not sample cases only from one model's failures; choose cases hard "from first principles" and from production data `[32:53]`.
Evidence and numbers: synthetic 50-ticket eval: migrating Opus 4.8 to Opus 5.5 with anti-patterns injected, then running the audit, improved both cost and score (chart, no figures spoken) `[03:16]`-`[04:19]`; cache fixes cut cost "by up to 72%" on internal benchmark harnesses `[07:23]`; the Claude API skill started at 66% on his docs eval before hill climbing `[14:30]`; a cost-reduction climb reached "a 90% reduction in cost" with better score `[17:35]`.
Tools and files named: prompt audit, cache diagnostics, build eval and hill climb skills (bundled with Claude Code, open source), Claude Managed Agents, vaults, METR task-duration charts.
Caveats: this conflicts with the May 2026 Code with Claude advice to default to xhigh for coding (see "The thinking lever"); the two talks are months and two model generations apart. He says overfitting is the main practical risk and a human must audit the loop `[13:30]`.
Relevance: high. The most direct source on which older prompting habits to delete, and on how to hill-climb skills safely.

### How Anthropic Merges 30,000 Code Changes a Day (Manish Kapur, Sonar, with Addy Osmani, Anthropic; AI Engineer channel, second half of 2026)
File: refs/videos/AnsXWH2_EBU/transcript.md   URL: https://www.youtube.com/watch?v=AnsXWH2_EBU
Thesis: Code generation is cheap; confidence is scarce. Anthropic's answer, per Osmani, is Claude doing the first-pass review with real end-to-end checks, hooks on edits, codified taste in shared instruction files, and humans checking the agent's evidence.
Practices (Osmani's statements only):
- Give agents a way to verify: checks (tests, benchmarks, specs) are where to spend time; with them in place quality of outcomes can improve "two to three" times `[04:18]`-`[05:19]`.
- Review flow: Claude does a first-pass review and must "actually try the experience out similar to a real user": end-to-end tasks, checking in a browser, running tools and linting `[06:21]`.
- "we have hooks that will then go and run on any edits. They will study the diffs" to correct the PR quickly `[06:21]`.
- Codify best practice and taste in the team's shared "Claude.md, agents.md, anywhere where the agent can then consult during code review" `[07:22]`.
- "people are responsible for checking on the agent's evidence": videos of the UI being clicked, screenshots for mobile or desktop `[07:22]`.
- Tests they lean on: "end-to-end tests, property tests, any visual verification tests" `[09:23]`.
- Label agent-written code in the PR, and keep a named human owner who is on the hook `[15:27]`-`[16:27]`.
- Definitions: a software factory is "loops at scale"; lights-on keeps human judgment and taste in the loop, dark pulls humans in only for exceptions `[02:16]`-`[03:17]`. Prediction: "light factories with some dark corners" by end of 2027 `[14:27]`.
- Enterprise concerns: control, permissions, sandbox `[13:26]`.
Evidence and numbers: Anthropic merged about 2,500 changes a day in May and about 30,000 a day at the time of the talk (stated by the host from an Anthropic post and confirmed in part by Osmani) `[05:19]`-`[06:21]`; CircleCI: throughput up about 59% while three in ten merge attempts fail (host's slide) `[01:15]`-`[02:16]`. Sonar survey figures are vendor data.
Caveats: co-presented by a vendor; Sonar's layered-verification pitch is the host's, not Anthropic's.
Relevance: high for the review and evidence model; short.

### How long can your skills be before your agent forgets what you told it? (Laurie Voss, Arize AI; AI Engineer channel, mid-2026)
File: refs/videos/XzJD1bvXKjs/transcript.md   URL: https://www.youtube.com/watch?v=XzJD1bvXKjs
Thesis: The "about 200 instructions" ceiling came from the 2025 IFScale benchmark and was real for 2025 models. Rerun on 2026 frontier models, the ceiling is roughly ten times higher, but models now fail in different, harder-to-detect ways.
Practices and findings:
- Replication: GPT-4.1, Claude Sonnet 4 and Gemini 2.5 Pro started failing around 200 to 300 rules and lost 30 to 50% by 500 `[05:21]`.
- 2026 models (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, DeepSeek V4 Pro) all scored 100% on the original 500-rule test; the boundary is "closer to 2,000" and up to 5,000 for the best `[06:22]`-`[07:22]`.
- Failure modes differ by model: DeepSeek forgets from about 750 rules; Claude refused at the API level when random word lists tripped its safety classifier; Gemini spent its whole budget thinking and returned almost nothing; GPT-5.5 started the report and then stopped, saying the task was pointless, which "looks like a real answer" `[09:24]`-`[13:27]`, `[17:30]`.
- Her workflow conclusions: skills files no longer need to be kept under 200 instructions and sharded into sub-skills; 100 to 300 specific rules can sit in one prompt; the constraint is now cost and latency, and verification of whether rules were followed `[14:27]`-`[15:28]`, `[20:36]`.
- Rule: assumptions about prompt length made more than about six months ago are probably wrong `[08:23]`.
Evidence and numbers: 2,300 calls across seven models for $29 `[18:33]`. Cited follow-ups: Chroma's context-rot work (accuracy on long inputs can fall 30 to 50% before the window limit) and a 46-model paper showing rewording or reordering the same instructions changes compliance `[16:28]`, `[19:34]`.
Caveats (hers): the task is a proxy (include exact keywords in a report); it measures a ceiling on tracking, not reasoning over conflicting rules; real instructions will do worse `[03:20]`-`[04:20]`, `[16:28]`. The speaker works for an eval vendor.
Relevance: high. Measured counter-evidence to the rule of keeping instruction files tiny, with clear limits. It does not contradict Anthropic's advice to keep always-loaded prompts short: that advice is about relevance and conflicts, this is about capacity.

### Building on the Codex Harness (Dominik Kundel, OpenAI; AI Engineer channel, 2026)
File: refs/videos/9WiBJRO84yY/transcript.md   URL: https://www.youtube.com/watch?v=9WiBJRO84yY
Thesis: The Codex app server is an open-source JSON-RPC protocol around the Codex harness; build clients on it instead of writing your own agent loop.
Practices:
- Customise by appending developer instructions, not by replacing the base system prompt, so you keep OpenAI's per-model tuning and stay "in distribution" `[06:22]`-`[07:23]`, `[16:41]`.
- Add tools as deferred so they are found through tool search instead of "polluting the overall context window" `[07:23]`, `[16:41]`.
- Per-thread configuration includes model, provider and sandbox (network connections, writable files) `[08:24]`.
- `codex exec` for non-interactive scripting and CI (for example auto-fixing a PR); the app server when you need many threads, an eval harness or goal mode `[14:40]`-`[15:40]`.
- Ship your own pinned version of the harness with your app; the protocol changes between versions `[09:24]`, `[15:40]`.
Tools and files named: Codex app server, Codex CLI, `codex exec`, goal mode ("slash goal"), tool search, Agent Client Protocol (ACP), a Codex plugin for Claude Code used for review or hand-off `[02:15]`.
Relevance: medium. Confirms the same primitives (goal, deferred tools, sandbox config, append-don't-replace prompts) exist on the Codex side.

### No Vibes Allowed: Solving Hard Problems in Complex Codebases (Dex Horthy, HumanLayer; AI Engineer Code Summit, about November 2025)
File: refs/videos/rmvDxxNubIg/transcript.md   URL: https://www.youtube.com/watch?v=rmvDxxNubIg
Thesis: In brownfield code the lever is context management: keep the window in the "smart zone" through frequent intentional compaction, organised as research, plan, implement, with the human reading research and plans because errors there multiply.
Practices:
- Start a fresh context when off track; do not keep correcting, because a history of mistakes and scolding biases the next step `[02:25]`-`[05:30]`.
- Intentional compaction: have the agent write its state to a markdown file (what we are doing, exact files and line numbers) and start a new session from it `[03:25]`-`[04:28]`.
- "Dumb zone": with about 168,000 usable tokens, diminishing returns start "around the 40% line", depending on the task; many MCP servers put all work in the dumb zone `[05:30]`.
- Subagents "are not for anthropomorphizing roles. They are for controlling context": fork a search, return a succinct pointer `[06:31]`.
- Research (objective map of how the system works), plan (exact steps, file names, code snippets, how to test after each change), implement with low context `[07:31]`.
- Leverage ordering: "a bad line of code is a bad line of code", a bad plan line can be a hundred bad lines, a bad research line sends everything the wrong way, so review effort goes upstream `[16:42]`.
- Static onboarding docs go stale ("the amount of lies"); prefer on-demand research generated from code, with progressive disclosure for per-directory context `[11:34]`-`[14:39]`.
- Scale the process to the task: button colour needs none of it; multi-repo features need all of it `[17:42]`.
- Plans and agent threads attached to PRs keep the team's "mental alignment" `[14:39]`-`[15:39]`.
Evidence and numbers: self-reported: 35,000 lines to BAML in seven hours, estimated at one to two weeks of work; a failure case removing Hadoop from parquet-java `[08:32]`-`[09:32]`. Cites a Stanford survey of 100,000 developers on rework `[00:23]`.
Caveats: late-2025 models and a 200k window. Several 2026 sources in this file dispute parts of it: Anthropic leads say plan mode is no longer needed, and Voss measures a much higher instruction ceiling. See also Horthy's own 2026 revision below (RPIwrong).
Relevance: high as the baseline that newer advice modifies; the subagents-for-context and review-upstream points are still echoed by Anthropic.

### Boris Cherny: We Cut 80% of Claude Code's Prompt (Boris Cherny, Anthropic, on stage at a Y Combinator event; 2026, the day after Opus 5 shipped; exact date not in the file)
File: refs/videos/qyPCVqFUyDo/transcript.md   URL: https://www.youtube.com/watch?v=qyPCVqFUyDo
Thesis: Each model generation makes earlier scaffolding obsolete. Anthropic ablates the Claude Code system prompt per model and deleted over 80% of it for Opus 5; users should do the same to their own CLAUDE.md, skills and hooks, and add instructions back only on repeated observed failure. The skill that matters is giving a hard task plus a way to verify.
Practices:
- Ablation method: "you delete the entire system prompt and then you bring it back line by line to figure out what is the impact of each individual line" `[05:14]`; same for tools, which are unshipped regularly `[06:15]`.
- For users: "every 6 months delete your Claude MD. Delete your skills. Delete your hooks. See what the model does" `[06:15]`.
- Rebuild order: delete, use, watch where it fails, and "only when you see it repeatedly stumble on the same thing" add it back, because the model reads the instruction on every use `[07:17]`-`[08:18]`.
- Experiment switches: a `--system-prompt` flag to replace the prompt, and an undocumented "simple mode" environment variable (heard as "Claude Code simple equals one") that removes all system and tool prompts; the model is "a little bit more intelligent without these prompts", but the product prompts make it behave as users expect `[04:14]`-`[05:14]`.
- Task framing: do not over-specify steps ("You must do like one, then two, then three"); "describe the task", "the guardrails" and "the exit criteria", then let it run `[14:25]`-`[15:26]`. Give tasks slightly harder than you think it can do `[14:25]`.
- Verification is "the single most important thing that people do not get right" `[19:32]`. Example prompt for a native rewrite: run the Electron app in a macOS VM, screenshot it, compare pixel by pixel with the Swift version, "don't stop until you're done"; running over two weeks `[20:35]`-`[21:38]`.
- With Opus 5 he says `/goal` and `/loop` are not required to keep it going ("These help"), only the task and a way to verify `[01:10]`, `[22:38]`.
- Fixing failures: better prompting, a skill, or an MCP server when context is missing `[23:39]`.
- Dynamic workflows: say "use a workflow"; Claude orchestrates agents in sequence and in parallel (fan out, verify or summarise, fan out again) inside a sandbox; he calls it a new form of test-time compute `[24:39]`-`[26:43]`.
- Loop is "a cron job that's running locally"; a routine is the same in the cloud. Use them for repetitive tasks that do not share context but may share memory `[27:43]`.
- Maintenance routines Anthropic runs daily, each a one-sentence prompt: clean up dead code, remove fully shipped experiments, add tests where coverage is missing, delete useless tests, and unify near-duplicate abstractions ("abstraction police"); 20 to 30 routines per day across codebases `[27:43]`-`[29:45]`.
- Evals outlive the harness but only by "one, two, three model generations" before saturating `[09:19]`.
- Security claim: aligned model plus a prompt-injection classifier on all traffic plus the auto mode classifier; "we just cannot demonstrate prompt injection anymore" `[02:11]`-`[03:12]`.
Evidence and numbers: Bun rewritten from Zig to Rust by one prompt with steering via a dynamic workflow that "ran for 11 days", now in production, estimated at over a year of human work `[16:27]`-`[17:30]`; "hundreds of agents running every day, sometimes thousands" for maintenance `[29:45]`.
Tools and files named: Opus 5, Fable, auto mode, `/goal`, `/loop`, routines, dynamic workflows, Claude Tag, `--system-prompt`, CLAUDE.md, skills, hooks, MCP.
Caveats: "coding is solved for the kind of coding that I do. It's not solved for everyone": deep systems code, distributed systems and pixel-level UI verification still struggle `[30:45]`. The no-prompt-injection claim is his statement, not a measurement in this file; treat as vendor claim. Inference: "delete your hooks" fits instruction-like hooks; he also says most remaining harness code is "safety and permissions and static analysis" `[06:15]`, so deterministic guard hooks are a different category.
Relevance: high. The strongest statement that setups should be pruned and re-earned per model, with a procedure.

### How I Plan, Build, and Run Loops with Claude Code (Thariq Shihipar, Anthropic, interviewed by Peter Yang; 2026, date not in the file; after the 80% prompt cut)
File: refs/videos/aVO6E181cNU/transcript.md   URL: https://www.youtube.com/watch?v=aVO6E181cNU
Thesis: `/loop`, `/goal` and workflows are three ways to keep an agent working; which one fits depends on how checkable the result is. Planning is not one document but an iterative removal of unknowns through explainers, prototypes and implementation notes.
Practices:
- `/goal` "helps the agent remind itself what its exit condition is" and only lets it stop when met; it signals that spec and exploration are done, so "power through" and fill gaps instead of stopping to ask `[01:02]`-`[02:02]`.
- Choosing the primitive: a deterministic signal (latency, a rendered design matching a Figma file through the Figma MCP) suits `/goal`; a "squishy" target (matching a screenshot) suits a workflow with a rubric and a verification agent `[03:04]`-`[04:06]`.
- Workflows: the main agent coordinates, a subagent per item does the work, and a separate agent verifies against a rubric, because of "self-referential bias": a model is more lenient on its own output `[27:34]`-`[30:40]`. A workflow "is just a JS file" and can be saved inside a skill for reuse `[28:37]`.
- Do not write a skill first: "really figure out what I want before I turn it into a skill" and learn the edge cases `[06:08]`. Sometimes the right shape is a repo of scripts (a workspace), with the skill describing how to set it up; more scripts means less done from scratch `[25:33]`.
- Planning as finding unknowns: ask for an explainer of a dependency including "ways things can go wrong" before building on it `[10:11]`-`[11:12]`; ask for an HTML artifact with design variations and give a reference site `[09:10]`; make the cheapest prototype first (HTML before React) `[17:23]`.
- Ask the agent to "keep implementation notes as it goes" so surprises are recorded and you can re-spec `[16:22]`-`[17:23]`.
- Failure mode: people "glaze over" plans; the prompt box becomes "a lazy button" and you pay later `[12:15]`-`[13:16]`.
- Focus: one active Claude Code session for the task he is concentrating on, background and multiplayer work in Claude Tag sessions (babysit a PR, fix tests, tag a reviewer) `[18:26]`-`[19:27]`. The team invested in making the dev environment run remotely `[18:26]`.
- Instruction length: "I feel like cloud. MBS are probably too long right now"; "probably a lot of skills are too long" `[34:45]`-`[35:46]`. Examples constrain newer models and "never" rules over-constrain; "if you give it the reason" it works better than the bare prohibition `[34:45]`.
- Clean-up: the `/simplify` skill ("simplify which Boris put out") `[32:42]`.
Evidence and numbers: system prompt cut by 80% `[33:44]`; no measurements.
Tools and files named: `/loop`, `/goal`, workflows, artifacts (Team and Enterprise at the time), Claude Tag, frontend-design plugin, Figma MCP, Remotion, Whisper.
Caveats: an interview with a sponsor read in the middle (ignored). His demo is video editing, not production code.
Relevance: high. Clear selection rule between goal, loop and workflow, and guidance on when to create a skill.

### Field Guide to Fable (Thariq Shihipar, Anthropic; AI Engineer conference, 2026, the day Fable was re-released)
File: refs/videos/9fubhllmsBU/transcript.md   URL: https://www.youtube.com/watch?v=9fubhllmsBU
Thesis: With a model that covers far more ground per prompt, the limit is the user's ability to find their own unknowns before and during the run. He lists six techniques, and describes how system-prompt best practice has reversed.
Practices:
- System prompt history: Sonnet 3.5 era, small prompt, few tools, many examples; then larger prompts, many examples and tools; now a smaller prompt because "The examples tend to constrain it", and "context and not just constraints" instead of "Do not do this" `[05:19]`-`[06:19]`.
- Six techniques for unknowns: (1) a "blind spot pass" ("help me figure out my relevant unknown unknowns and help me prompt better"), pointing it at the module, git history or Slack `[10:26]`; (2) brainstorms and prototypes, for example an HTML page with four different designs to react to `[11:26]`; (3) an interview, with context such as "prioritize questions that would change the architecture" `[12:28]`; (4) references: give existing code or an HTML mock-up as the map `[12:28]`-`[13:28]`; (5) implementation notes: when it hits an unknown, "ask it to log it" `[13:28]`; (6) have it quiz you afterwards so you can stand behind the PR `[13:28]`.
- AskUserQuestion progression: barely callable on Opus 4, could run a 40-question spec interview by Opus 4.5, and with Opus 4.8 and Fable builds an HTML report with the questions embedded `[06:19]`-`[07:21]`.
- Capability overhang example: a chat model cannot list Pokemon ending in "aw", Claude Code can because it writes a script `[03:16]`-`[04:16]`.
Evidence and numbers: none.
Tools and files named: Fable, Claude Tag, AskUserQuestion, plan mode, HTML reports.
Relevance: high. A compact checklist for pre-flight and in-flight spec work.

### The Ralph Wiggum Loop from 1st principles (Geoffrey Huntley; own channel, about January 2026, Sonnet 4.5 era)
File: refs/videos/4Nna09dG_c0/transcript.md   URL: https://www.youtube.com/watch?v=4Nna09dG_c0
Thesis: Ralph is a bash loop that starts a fresh context each iteration, feeds it the same prompt plus a spec index and an implementation plan, and lets the model pick one task per loop. Its purpose is to avoid context rot and compaction; captions render his malloc metaphor for the context array as "malicking".
Practices:
- Fresh context per iteration; "Compaction is the is the devil" `[09:14]`-`[10:14]`. He says Anthropic's Ralph plugin is "not it" because it keeps one session going until compaction, which is lossy and can drop the "pin" `[03:03]`, `[12:18]`.
- The "pin": a specs README that is a lookup table linking each spec with many synonyms, so the search tool hits it and the model does not invent existing functionality `[12:18]`-`[13:19]`, `[23:34]`-`[24:35]`.
- Specs are generated in a conversation ("you can interview me"), then reviewed and edited by hand; the planning conversation and the build loop run in separate sessions `[08:10]`-`[09:14]`, `[13:19]`, `[29:23]`.
- Implementation plan as bullet points that cite the spec and source locations to change `[22:27]`.
- Loop prompt (`prompt.md`): study the specs README, study the implementation plan, "pick the most important thing to do", write property-based or unit tests as the model judges best, run tests, commit when they pass, and update the plan when the task is done (he forgot this line at first) `[29:23]`-`[33:56]`. One goal per loop keeps context small `[30:27]`.
- Run attended first, watch, adjust the prompt or specs, then unattended: "low control with high oversight" `[30:27]`, `[33:56]`-`[34:58]`.
- The engineer's job is "engineering back pressure" (tests, checks) to keep the generator on the rails `[18:49]`.
- Command as spoken: a `while true` loop piping `prompt.md` into `claude` with `--dangerously-skip-permissions` `[32:52]`-`[33:56]`.
Evidence and numbers: cost claim of 10.42 US dollars an hour (captions print it as "$1042 US an hour") from Sonnet 4.5 API pricing over 24 hours `[01:01]`-`[02:02]`; his own estimate.
Caveats: he deploys with no CI and no code review on a personal project with sudo on NixOS `[32:52]`; not transferable as-is. Later Anthropic sources in this file say newer models keep going without such scaffolding (Cherny, YC talk) and that the full session log should be kept instead of discarded (Martin).
Relevance: medium to high. The original description of fresh-context loops, spec index and one-task-per-iteration; dated but the structure survives in `/loop` and routines.

### Fireside Chat with Boris Cherny at @Scale (Meta's conference; June 2026 per search listing, after Code with Claude Tokyo)
File: refs/videos/Z47vatpsGPI/transcript.md   URL: https://www.youtube.com/watch?v=Z47vatpsGPI
Thesis: Coding stopped being the bottleneck; Anthropic removes the next bottleneck each time with a Claude-powered product (code review, security review, CI optimisation, maintenance loops). Loops are the next abstraction step after agents.
Practices:
- Abstraction ladder: source code is a statement, an agent writing code is a function, "loops are like a higher order function" `[09:12]`. About 30% of his code is written by loops on an average day; 100% on some days "but it it doesn't totally click yet" `[11:12]`.
- Loop examples: one agent looping over all code reviews; one reading user feedback every 5 or 10 minutes and opening fix PRs `[10:12]`.
- Maintenance loops he runs: improve architecture, find and fix flaky tests, delete useless tests, unify duplicated abstractions; he reviews the resulting PRs, not the process `[31:30]`-`[32:31]`.
- "use a workflow" as the phrase that adds test-time compute when a result is not good enough `[32:31]`. Example: one prompt asking for a workflow to analyse real CI timings produced four PRs that cut CI time by 50% in a few hours and a few million tokens `[27:26]`-`[28:27]`.
- Claude Code Review runs on every Anthropic PR and uses many tokens by design; he puts bug catch at "98, 99%" and reviews only whether the PR should exist `[25:24]`-`[26:26]`. Claude Security scans all codebases weekly and fixes issues autonomously `[26:26]`-`[27:26]`.
- Auto mode origin: security staff saw that prompt fatigue made the human in the loop harmful; routing prompts to a model was "more secure" than both dangerous mode and manual approval and unblocked runs of hours or days `[36:35]`-`[38:36]`.
- Staying in the loop: new engineers are told to use the explanatory output style (heard as "exploratory", via `/config`), and a learning output style exists for non-coders that walks through steps instead of doing them `[39:37]`.
- Model choice: he uses the top model for everything and argues for optimising return before cost; cost levers when needed are advisor models, a default lower model with call-outs, effort level, per-seat and per-department budgets `[04:10]`-`[05:10]`, `[19:19]`-`[20:20]`.
- Collaboration today: connect Claude Code to Slack or Teams by MCP `[21:21]`.
- Planning horizon: weekly or monthly, no one-year plan `[29:28]`.
Evidence and numbers: 1.7 thousand PRs, 400,000 lines added and 250,000 deleted this year, 8 billion tokens since March `[01:07]`-`[02:09]`; all his code written by Claude Code since Opus 4.5 in November 2025 `[02:09]`; "8x increase in code per engineer since the beginning of this year" at Anthropic `[06:10]`; 80 to 90% of Anthropic code written by Claude Code `[18:18]`; prompt-injection success "around 1%" at 100 attempts per system cards `[38:36]`. Self-reported.
Tools and files named: loops, routines, dynamic workflows, Claude Code Review, Claude Security, auto mode, output styles, Cowork, advisor models, Fable, Opus 4.8.
Caveats: he names what Fable still does worse than him: product ideas and distributed-system design `[34:34]`-`[35:34]`. The 98 to 99% figure is an estimate in conversation.
Relevance: high for what the head of Claude Code does daily and which loops he trusts unattended.

### Everything We Got Wrong About Research-Plan-Implement (Dex Horthy, HumanLayer; AAIF Live, early 2026, before AI Engineer Miami; Opus 4.5 era)
File: refs/videos/YwZR6tc7qYg/transcript.md   URL: https://www.youtube.com/watch?v=YwZR6tc7qYg
Thesis: A public correction of his own 2025 method. Research-plan-implement worked for experts and failed for their teams because a monolithic planning prompt skipped steps, research was contaminated by the ticket, and reviewing long plans gave no leverage. The replacement splits the work into smaller prompts joined by real control flow and moves review to short design and outline documents plus the code itself.
Practices:
- Reversal on code reading: "We tried not reading the code for like 6 months. Uh it did not end well. We had to rip out and replace large parts of that system." `[09:12]` New advice: "don't read the plans. Please, read the code", because a 1,000-line plan is about as much to review as 1,000 lines of code and the code still differs `[08:12]`.
- Instruction budget: their planning prompt had "85 or more instructions"; with CLAUDE.md, system prompt, tools and MCP on top, steps were silently skipped unless the user typed "magic words" `[05:10]`-`[07:12]`. He cites the 150 to 200 instruction figure and adds it is "probably a little bit higher now" `[07:12]`.
- "don't use prompts for control flow if you can use control flow for control flow" `[14:17]`: split into separate prompts each under 40 instructions `[13:16]`.
- Research hygiene: one context turns the ticket into questions; a fresh context that never sees the ticket answers them, so research stays factual ("if you tell the model what you're building, then you get opinions") `[04:10]`-`[05:10]`, `[11:14]`.
- Design discussion document, about 200 lines: current state, desired end state, patterns to follow, resolved decisions, open questions. Use it to catch the agent copying a bad existing pattern `[14:17]`-`[16:19]`.
- Structure outline, about two pages: phases, order, and how each is tested; like C header files (signatures and new types) `[16:19]`-`[17:19]`.
- Force vertical slices: models default to "horizontal plans" (all database, then all services, then API, then front end) with nothing testable until 1,200 lines in; require checkpoints that can be verified `[17:19]`-`[18:19]`.
- The detailed plan becomes "a tactical doc" for the agent that he only spot-checks `[19:20]`. Peers review the short design and outline before code exists `[19:20]`-`[20:22]`.
- Full sequence: questions, research, design, structure, plan, worktree, implement, PR `[13:16]`, `[21:22]`.
- Context budget: experienced users go to 60%; beginners should aim under 40%. They do not use built-in compaction because state lives in the documents `[25:30]`.
- Aim for 2 to 3x with near-human quality instead of 10x, since speed is worthless if you "throw it all away in 6 months" `[10:13]`.
Evidence and numbers: about half of users got plans written without the question step unless prompted with the exact phrase `[06:11]`; experience with "thousands of engineers" (unquantified) `[03:10]`.
Caveats: he sells an IDE implementing this. He states he is "a little mid on agent swarms" `[10:13]`, which conflicts with Anthropic's workflow and routine advocacy later in 2026. His "read the code" position conflicts with Cherny's "I'm not looking for bugs anymore" (@Scale).
Relevance: high. Concrete lessons on splitting skills, on instruction counts per prompt and on where human review pays off.

### The Hidden 50% Drop in AI Agents Following Your Rules ("Guy", co-founder and CEO of Baz, at a Tessl / AI Native Dev event; autumn 2026, mentions Opus 5 models as released)
File: refs/videos/R1j6HtykHNE/transcript.md   URL: https://www.youtube.com/watch?v=R1j6HtykHNE
Thesis: Telemetry from a code-review vendor's customers suggests that how often agents consult static instruction files changes abruptly with model releases, and that stale or forgotten rule files keep steering agents.
Findings and practices:
- After one model release, usage of static instruction files across their customer base fell by "almost a 50%" `[13:28]`-`[14:30]`. He says the change "was completely invisible to you" `[14:30]`.
- Review comments that used the team's own guidelines were accepted more often; he calls it correlation, and notes their harness forces guideline use, which a stock harness does not `[15:34]`-`[16:36]`.
- Stale files: instruction files not updated in "six, 12, 18 weeks" are still treated as truth by every downstream agent `[17:38]`. A leftover CodeRabbit rule file from an old trial overrode CLAUDE.md and newer skills in their data `[18:39]`.
- "The number one factor that drives a consistent outcome is setup": an identical starting state for a task predicts consistency better than instructions, skills or shared memory `[08:19]`.
- What replaced agile rituals in the teams they see: human-written specs or plan files, verification at the PR choke point, and merge queues `[19:45]`-`[21:47]`.
- Long-horizon tasks adhere to instruction files more consistently than short ones (more turns in which to land on the right file) `[27:01]`-`[28:01]`.
Evidence and numbers: charts described verbally; no sample sizes, model names or dates given for the regression. Proprietary vendor data.
Caveats: the speaker says the data "is supposed to be confusing"; his claims about how vendors load AGENTS.md and skills are observations, not documented behaviour. Captions give the speaker only as "Guy".
Relevance: medium to high. Supports auditing for stale or duplicate rule files across tools, and re-checking adherence after each model change.

### From Prompts to AGENTS.md: What Survives Across Thousands of Runs (Thomas Krier; AI Native DevCon New York, autumn 2025 by content: GPT-5 Codex, Opus 4.1)
File: refs/videos/aMwuPa6BnaM/transcript.md   URL: https://www.youtube.com/watch?v=aMwuPa6BnaM
Thesis: Experience report from a data team running many Codex and Claude Code agents in tmux, with small experiments on whether AGENTS.md rules help.
Practices: share one rule file between tools (reference AGENTS.md from CLAUDE.md, or symlink) `[06:21]`; after a session ask the agent for lessons learned and "five suggestions" for rule changes, then approve selectively `[08:24]`-`[09:25]`; top testing rule, as captioned: "No fa fake, no mock, no stop" (no fakes, mocks or stubs), because agents fake tests to finish `[11:27]`; summarise context yourself and hand it to a new agent instead of trusting opaque auto-compaction `[12:29]`; an "arena" round where agents see each other's solutions and refine `[16:32]`-`[18:34]`.
Evidence and numbers: in a 20-agent experiment, adding an AGENTS.md raised solution scores but also raised token use `[15:31]`-`[16:32]`. Small and informal.
Relevance: low to medium. This is the 2025 New York event, not the 2026 one; kept for the lessons-learned ritual and the tokens-up finding.

### Codex Has Left The Laptop (Dominik Kundel, OpenAI; DevDay 2026)
File: refs/videos/XkKdbPhIvbY/transcript.md   URL: https://www.youtube.com/watch?v=XkKdbPhIvbY
Thesis: OpenAI's equivalent of the Anthropic direction: move agent work to managed cloud environments, add a personal always-on agent ("dot"), a shared-thread agent in Slack and Teams, and shared plan documents ("Space").
Practices:
- Cloud environment setup is done by the agent: it inspects repos and dependencies and writes "a startup skill that teaches the agent how to use the environment" plus an install or startup script; file-system snapshots speed up later tasks `[03:29]`-`[05:33]`, `[09:36]`.
- Private resources are reached through a VPN (Tailscale) or OIDC instead of public exposure; network access and stored keys are configured per environment, with personal values kept in a vault that is not shared with the team `[07:35]`-`[10:36]`.
- Plans live in a shared document that the agent and the team both edit, with a task tracker the agent updates while implementing `[12:38]`-`[13:39]`.
- Personal agent for ongoing responsibilities (watching channels, triaging PRs, spawning cloud tasks); the shared agent reaches only shared environments `[14:40]`-`[16:42]`.
- The CLI gained an agent view for parallel tasks and a voice mode `[17:44]`.
Tools and files named: Codex Cloud, dots, Space, code review tab, agent view, Figma plugin.
Relevance: medium. Shows convergence across vendors on environment-setup skills, agent views and proactive agents; useful for a harness-neutral setup.

### Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents (Robert Brennan, OpenHands; AI Engineer channel, 2026)
File: refs/videos/iH_wV8BbS24/transcript.md   URL: https://www.youtube.com/watch?v=iH_wV8BbS24
Thesis: Unattended agents need least privilege. Four isolation options with trade-offs: local Docker, CI runners, a dedicated VM, ephemeral pods.
Practices:
- A local agent with permission prompts skipped can reach the whole file system, anything sensitive held in the shell environment or home directory, and any production system the user is logged in to `[04:18]`.
- Least privilege: give the agent only the repo and the few keys the task needs, to limit the "blast radius of a prompt injection attack" or of a confused agent `[04:18]`-`[05:19]`.
- Local Docker container per conversation: ephemeral, mount only the repo, ports and selected values; does not scale and cannot react to events `[05:19]`-`[06:20]`.
- GitHub Actions: isolated, scheduled or PR-triggered; only GitHub events, and vendor lock-in `[06:20]`-`[07:20]`.
- Dedicated VM or Mac mini: persistent and can receive webhooks, but co-located agents share access (a review agent can reach the incident bot's access and memory) `[08:21]`-`[09:23]`.
- Ephemeral pod per session (Kubernetes): fresh state each run, scale, schedule and webhook triggers `[09:23]`-`[10:24]`.
- Sandboxing "is not a panacea": container escapes exist, and he cites a Mythos test instance escaping its sandbox `[12:27]`.
Relevance: medium. A neutral checklist for deciding where unattended runs execute; the solo-developer options are the first two.

### Stop babysitting your agents (Sid Bidasaria, Anthropic, founding engineer of Claude Code; Code with Claude London, 2026-05-19)
File: refs/articles/sozai.app/transcript-stop-babysitting-agents-index-md/article.md   URL: https://sozai.app/transcript/stop-babysitting-agents/ (video: https://www.youtube.com/watch?v=wI0ptqCSL0I)
Source note: the official video had no captions on any mirror. This is a third-party machine transcript with timestamps (SozAI); it spells the speaker "Boudesaria" and the product "Cloud Code". Its summary block on top is machine-written and was not used. Quotes are verbatim from that file, so wording may differ slightly from the audio.
Thesis: Three layers stacked in order: verification (Claude checks its own work in a loop), then parallel sessions you can trust, then background loops that take your keyboard out of the path. The question to keep asking: "what does an agent need from your code base that a human takes for granted?" `[04:23]`
Practices:
- Prerequisites ("table stakes"): a high-quality CLAUDE.md, "the single highest leverage thing that you can do" `[01:31]`; connect the tools you use daily (Slack, Asana, Linear, Datadog, BigQuery), rule of thumb "if a tool is useful for you in your day-to-day life, it will also be useful" for Claude `[01:45]`; set up the remote environment on Claude Code on the web `[02:06]`.
- Model verification on how a human checks work: build and type-check, run the executable, check side effects (browser UI, logs, database state), run and add unit tests, deploy to staging `[07:23]`-`[08:30]`.
- A loop is "an autonomous circuit that you can complete" so Claude can hill-climb to a success criterion: write, check, debug, repeat `[09:31]`-`[10:16]`. "wherever possible, our goal now is to get Claude into a loop" `[11:11]`.
- Four parts of a front-end verification loop: (1) run the app (dev server); (2) use it through a browser tool (Claude in Chrome via `/chrome`, or Playwright); (3) prove it, with a screenshot before and after the fix; (4) unblock it: give Claude a login identity and scripts that seed state, kept dynamic instead of prescriptive `[12:14]`-`[14:14]`.
- Package the loop as a skill and make it self-improving: instruct the skill to update itself whenever Claude hits a blocker. The Claude Code team has one verification skill, and "the skill is explicitly told to keep documenting itself" `[14:58]`-`[15:29]`
- How to create it: walk Claude through the checks by hand once (start server, drive the browser, change a setting), then say "take everything we learned and put it into a skill file" `[20:38]`-`[21:08]`; he estimates five to ten minutes `[22:25]`. In the demo the new feature run then hit lint errors, fixed them and re-verified `[24:00]`-`[24:38]`.
- Attention is the limit on parallel work: more than four to five open sessions "simultaneously takes a big load on my brain" `[26:56]`-`[27:11]`. Aids: desktop app sidebar across local and cloud sessions; `claude agents` (agent view) sorted by how much attention each session needs; rename, pin and colour sessions; Claude Code on the web; `/remote-control` with phone notifications `[27:17]`-`[32:06]`. His earlier setup was tmux with four panes, one worktree each `[29:08]`.
- Background work: `/loop 10 minutes` plus "babysit my open PRs" wakes the session every 10 minutes; it works "if you have your Cloud MDs and your tools defined and set up correctly" `[34:36]`-`[34:54]`. Routines are `/loop` running remotely in the same containers as Claude Code on the web, with time or event triggers `[35:06]`-`[35:43]`.
- Candidate chores for loops and routines: PR babysitting (review comments, merge conflicts, CI failures), updating docs, triage, monitoring feedback, keeping CI green `[33:35]`-`[34:20]`. Team examples: a routine updates the docs every day; another reads incoming issues and feedback and posts to Slack every six hours `[35:59]`-`[36:10]`.
Evidence and numbers: about half the audience had done the first two prerequisites `[02:41]`; no measurements.
Tools and files named: CLAUDE.md, skills, Claude in Chrome MCP (`/chrome`), Playwright, auto mode, desktop app, `claude agents`, Claude Code on the web, `/remote-control`, `/loop`, routines.
Caveats: third-party transcript; the SF version of this talk ("Rearchitecting your workflows with Claude Code") has no recording.
Relevance: high. The clearest ordered recipe in this set: verification skill first, then parallelism, then loops.

### Beyond the basics with Claude Code (Daisy Hollman, Anthropic Claude Code team; Code with Claude London, 2026-05-19)
File: refs/articles/sozai.app/transcript-beyond-basics-claude-code-index-md/article.md   URL: https://sozai.app/transcript/beyond-basics-claude-code/ (video: https://www.youtube.com/watch?v=tuY2ChJIx48)
Source note: third-party machine transcript (SozAI); the official video had no captions on any mirror. Roughly the first 16 minutes of this file are scrambled: segments repeat and interleave, so locators before `[16:45]` are approximate. From `[16:45]` on it reads in order. Speaker spelled "Holman"; "Quad"/"Cloud" = Claude.
Thesis: Customising an agent for real software engineering means giving it access, knowledge and tooling, all through a context window that is not growing. Judge every customisation primitive by what it costs when not used and by what happens with thousands of them; hooks are the only one with zero context cost.
Practices:
- Thesis sentence, split across two segments of the scrambled part: "if Claude can't do everything you can do, it can't do your" `[03:52]` then "job with you" `[07:23]`. Exercise: do a full day without leaving Claude Code and write down every time you alt-tab to another tool to copy something in; connect each of those `[15:08]`-`[15:47]`.
- Give Claude the "why": decisions live in chat threads, design docs, runbooks and meeting notes, not in source. She feeds meeting notes to Claude and asks for low-hanging fruit, getting two or three "PRs per meeting" `[14:22]`-`[14:40]`. CI: "You should not be fixing CI failures yourself at this point in time." `[13:04]`
- Two kinds of tools: those that "compensate for a lack of intelligence" and those that "scale with intelligence". Hooks that nudge are the second kind, "the red squigglies for your agent" `[13:17]`, `[14:53]`. Example: a hook reminding Claude that a file is generated, instead of blocking the edit `[13:49]`-`[14:17]`. Forcing a fixed order of work does not scale with intelligence `[15:31]`.
- Context budget: windows are about 1 million tokens (Opus 4.7) and "aren't really growing" `[16:45]`; treat it like running "NPM on an Arduino" and "Don't pay for what you don't use" `[18:11]`-`[18:56]`.
- Prompt cache constraint: changing something early in the prompt makes everything after it uncached, "which cost 10 times as much"; you cannot evict a tool definition without invalidating the cache. Put "stable shared stuff at the very front and volatile per task information closer to the end" `[19:59]`-`[21:30]`.
- MCP: designed for chatbots without a shell. If you already have a CLI, "it doesn't make a whole lot of sense to wrap that CLI in MCP" unless it ships to non-technical customers; a skill that explains the CLI is easier `[24:34]`-`[24:53]`. Still use other vendors' MCP servers (Slack, email) `[25:10]`. Scaling: "even 20 servers with 15 tools each" fills much of the window; tool search lazy-loads schemas, but generic tools still need full definitions and shorter descriptions trigger less `[25:39]`-`[27:07]`.
- Skills: "a lazy system prompt", a folder with a markdown file and a one-line description that is always loaded `[28:09]`-`[28:43]`. Reliable triggering can still take a paragraph of description, "something like 300, 400 tokens", and trimming the description reduces triggering `[29:21]`-`[29:44]`. No sub-skill hierarchy yet (announced as coming) `[29:44]`-`[30:07]`. Because they are easy to create, control skill quality in a shared repo `[29:02]`.
- Hooks: "an actual zero overhead abstraction": a script runs on an event outside the context window and decides whether to insert text; a JavaScript type-check hook costs nothing while you write Rust, unlike a JavaScript skill description `[30:30]`-`[32:25]`. Limits: matching on words or regexes; using subagents to decide gets expensive `[32:43]`-`[33:01]`.
- Subagents: their system prompt lives in a separate context; the parent pays for the call, the result, and a one-line description per agent `[33:26]`-`[34:34]`.
- Why plugins cannot ship a CLAUDE.md: it is "an extremely expensive abstraction, but it looks super cheap"; the deliberate workaround is returning text from a SessionStart hook, which makes the unconditional cost explicit `[34:47]`-`[36:00]`.
- Memory is "low quality, low cost" and short-lived; plugins and skills are context-engineering artefacts that are "iterated on" and "evaluated", not made on the fly `[36:16]`-`[36:56]`.
- Her setup: several long-lived worktrees that all track upstream main, each with a persistent agent that keeps its identity, so dependency installs are not repeated `[40:33]`-`[41:55]`; `/color` and rename for fast context switching `[39:48]`-`[40:17]`.
- `/loop` runs a prompt at a fixed interval and Claude can turn it off when no longer relevant (internally a cron tool); for PRs, leave it for a day and a half and "it will fix all of the CI bugs" `[43:19]`-`[44:05]`.
- Auto mode "is what makes Loop usable", agent teams usable and overnight work usable; she gives a cost of "30 to 40% more" tokens and immediately says "don't quote me on that" `[44:18]`-`[45:07]`.
- Agents can message each other (SendMessage tool), with constraints being relaxed `[41:55]`-`[43:03]`. Remote control for a "30-second check-in after dinner" on overnight agents `[46:05]`-`[46:22]`.
- Three take-homes: give it access, mind the context window, pick abstractions that scale `[46:22]`-`[46:46]`.
Evidence and numbers: some companies have tens or "hundreds of thousands of skills" in a monorepo and hit a scaling boundary `[22:01]`-`[22:16]`; the engineer who built agent view went through "like a thousand PRs in the past month" with it `[45:53]`. Anecdotal.
Tools and files named: plugins, MCP, tool search, skills, hooks (SessionStart), subagents, agent teams, SendMessage, worktrees, `/color`, `/loop`, auto mode, `claude agents`, remote control.
Caveats: transcript quality as noted. Her framing targets very large monorepos; for a solo developer the per-description costs are small. Inference: the ordering still holds: prefer a hook when a check can be decided by a script, a skill when Claude must choose, an always-loaded file only for what every task needs.
Relevance: high. The best source here on the context cost of each primitive and on hooks as nudges.

