# Anthropic claude.com articles and guide chapters: using and extending Claude Code, skills and agents

Sources read: 60 of 60, each in full (52 articles and 8 guide files from claude.com). None was unreadable. Three saved files are incomplete or degraded, which limits what can be quoted from them:

- `resources-articles-maximizing-the-value-of-your-claude-code-sessions` (fetched via jina): the closing "Where to look first" ranked list is an image and is missing from the text.
- `resources-articles-subagents-in-claude-code`: every code example (agent file, CLAUDE.md policy, skill, hook script) is missing from the saved text; the prose around them is intact.
- `resources-articles-beyond-permission-prompts-...`: the saved page is an unpolished draft with placeholders such as "\[XXX\]".

Several `meta.json` author fields name a quoted customer, not the writer; bylines below come from the article text.

Source keys and dates (newest guidance wins where they conflict):

| Key | Article | Date |
|---|---|---|
| TokenSaving | Token-saving updates on the Anthropic API | 2025-03-13 |
| Memory | Bringing memory to teams | 2025-09-11 |
| AgentSDK | Building agents with the Claude Agent SDK | 2025-09-29 |
| CtxMgmt | Managing context on the Claude Developer Platform | 2025-09-29 |
| Sandbox | Beyond permission prompts | 2025-10-08 |
| Plugins | Customize Claude Code with plugins | 2025-10-09 |
| SkillsLaunch | Introducing Agent Skills | 2025-10-16 |
| Web | Claude Code on the web | 2025-10-20 |
| PromptBP | Prompt engineering best practices | 2025-11-10 |
| Frontend | Improving frontend design through Skills | 2025-11-12 |
| CreateSkills | How to create Skills | 2025-11-19 |
| ClaudeMd | Using CLAUDE.md files | 2025-11-25 |
| Hooks | How to configure hooks | 2025-12-11 |
| SkillsMCP | Extending Claude's capabilities with skills and MCP | 2025-12-19 |
| AgentsSkills | Building agents with Skills | 2026-01-22 |
| MultiAgent | When to use multi-agent systems | 2026-01-23 |
| Guide | Complete guide to building Skills (chapters: Fundamentals, Planning, Testing, Patterns, Resources, Distribution) | 2026-01-26 |
| SkillCreator | Improving skill-creator | 2026-03-03 |
| WfPatterns | Common workflow patterns for AI agents | 2026-03-05 |
| SkillsExplained | Skills explained | 2026-03-05 |
| 1M-GA | 1M context generally available | 2026-03-13 |
| AutoLaunch | Auto mode for Claude Code | 2026-03-24 |
| Harness | Agent harness design: 3 patterns | 2026-04-02 |
| Subagents | How and when to use subagents in Claude Code | 2026-04-07 |
| Advisor | The advisor strategy | 2026-04-09 |
| CoordPatterns | Multi-agent coordination patterns | 2026-04-10 |
| Routines | Introducing routines in Claude Code | 2026-04-14 |
| Desktop | Redesigning Claude Code on desktop | 2026-04-14 |
| Sessions1M | Session management and 1M context | 2026-04-15 |
| Opus47 | Best practices for Opus 4.7 with Claude Code | 2026-04-16 |
| MAMemory | Memory for Claude Managed Agents | 2026-04-23 |
| Onboarding | Onboarding Claude Code like a new developer | 2026-04-28 |
| APISkill | Claude API skill | 2026-04-29 |
| AgentView | Agent view in Claude Code | 2026-05-11 |
| LargeCode | How Claude Code works in large codebases | 2026-05-14 |
| DynWf | Introducing dynamic workflows | 2026-05-28 |
| Steering | Steering Claude Code | 2026-06-18 |
| Artifacts | Claude Code now supports artifacts | 2026-06-18 |
| Loops | Loop engineering: getting started with loops | 2026-06-30 |
| FableGuide | A field guide to Claude Fable 5 | 2026-07-06 |
| Effort | Effort level and model selection | 2026-07-07 |
| VerifyLoops | Building verification loops with skills | 2026-07-22 |
| Models | Claude models explained | 2026-07-24 |
| Cost | Cost visibility and control | 2026-08-04 |
| SelfHost | Self-hosted environments | 2026-08-06 |
| AutoDefault | Auto mode is now the default | 2026-08-07 |
| AutoProd | Running auto mode in production | 2026-08-07 |
| SessionValue | Maximizing the value of your Claude Code sessions | 2026-08-14 |
| Opus55 | Opus 5.5 and longer, context-heavy sessions | 2026-09-24 |
| PluginPortal | Build plugins for Claude | 2026-09-25 |
| Mods | Customize Claude Code with mods | 2026-10-01 |
| Fold | When to fold subagents into your main agent loop | 2026-10-22 |

## Cross-cutting findings

### Recurring practices

1. Start with the simplest structure (one agent, one turn-based loop) and add agents, workflows or loops only when a measured limit appears. (MultiAgent, WfPatterns, CoordPatterns, Loops, Fold, Subagents)
2. Always-loaded context is paid for on every turn and dilutes adherence, so keep CLAUDE.md small and move procedures to skills and scoped constraints to path-scoped rules. (Steering, SessionValue, LargeCode, Harness, Frontend, Opus55)
3. Anything that must always or never happen is enforced by code (hooks, permissions, scripts), not by an instruction. (Steering, LargeCode, Hooks, Guide Patterns, WfPatterns)
4. Give Claude a way to see, measure and interact with its result, and turn each recurring manual check into a verification skill; quantitative checks work best. (VerifyLoops, Loops, AgentSDK, AutoProd)
5. Review with a second agent in fresh context, and give any verifier explicit criteria, or it rubber-stamps. (Loops, Subagents, MultiAgent, CoordPatterns, DynWf)
6. Every loop needs a stated stop condition and a cap on iterations or turns. (Loops, WfPatterns, CoordPatterns, MultiAgent)
7. Split work by context, not by role; use a subagent when only the conclusion is needed, not the intermediate output. (MultiAgent, Fold, Sessions1M, SessionValue, Steering)
8. A skill's or subagent's description decides whether it is used: state what it does and when to use it, with boundaries, and test both should-trigger and should-not-trigger prompts. (CreateSkills, Guide Planning, Guide Testing, SkillCreator, Subagents)
9. Build skills and CLAUDE.md entries from real repeated work, not speculation. (CreateSkills, VerifyLoops, Guide Testing, SkillsExplained, ClaudeMd)
10. New task, new session; rewind instead of correcting; compact proactively with a hint, and before a break. (Sessions1M, SessionValue, Opus55, ClaudeMd)
11. Choose model and effort at session start, stay on defaults, and change one only after asking whether Claude lacked knowledge or lacked effort. (Effort, SessionValue, Opus55, Harness, Models)
12. Put the whole task in the first turn: intent, constraints, acceptance criteria, file locations; surface unknowns before implementation. (Opus47, FableGuide, SessionValue)
13. Write instructions as explicit statements with the reason and a positive example, not capitalised prohibitions. (PromptBP, Steering, Opus47)
14. Configuration ages: instructions, skills and hooks written for an older model become overhead or a constraint, so review on a schedule and after model releases. (LargeCode, Harness, Fold, SkillCreator)
15. Work with fewer prompts through auto mode plus explicit deny rules and sandboxing, and step out for production infrastructure and outward-facing actions. (AutoDefault, AutoProd, Sandbox, Harness)
16. When a result misses, fix the system (skill, rule, hook, CLAUDE.md), not only the instance. (Loops, AgentSDK, LargeCode, Onboarding)
17. Put deterministic or boilerplate work in scripts that a skill runs: cheaper and more reliable than re-deriving it. (Loops, Frontend, AgentsSkills, Guide Patterns, SkillsLaunch)
18. Navigation is agentic search over the live repo; help it with a map, scoped commands, ignore rules and LSP, not an index. (LargeCode, AgentSDK, ClaudeMd)

### (a) What goes where: CLAUDE.md, rules, skills, hooks, subagents, MCP

Steering (2026-06-18) names "seven methods for instructing Claude's behavior: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt", and says each controls when an instruction loads, whether it survives compaction, and "How much authority it carries." MCP is not in that list; its criteria come from SkillsMCP, SkillsExplained and LargeCode.

| Mechanism | Anthropic's criterion for using it | When it loads | After compaction | Context cost |
|---|---|---|---|---|
| CLAUDE.md, root | "facts Claude should hold all the time: build commands, monorepo layout, team conventions" (Steering, "When to use each method") | Session start, whole session | Re-read | High: "Every line costs tokens whether relevant or not" |
| CLAUDE.md, subdirectory | "Conventions specific to a subdirectory" (Steering table) | When Claude reads a file under that directory | "Lost until that subdirectory is touched again" | Low |
| Rules, `.claude/rules/` | "Specific constraints or conventions (e.g., all API handlers must validate input with Zod)"; with `paths:` when the constraint is file-specific or cross-cutting (Steering) | Session start if unscoped; on matching file reads if path-scoped | "Re-injected on compaction" | Medium; "Always-on unless path-scoped" |
| Skills, `.claude/skills/` | "Procedural workflows (deploy or release checklists)"; anything explaining how to do something (Steering; SkillsMCP) | Name and description at start; body when invoked | Re-injected "up to a shared budget; oldest dropped first" | Low |
| Subagents, `.claude/agents/` | Parallel work or side tasks that "should run in isolation and return only a summary (deep search, log analysis, dependency audit)" (Steering table) | Name, description, tool list at start; body only in the child | Only the final message returns | Low in the parent |
| Hooks, `settings.json` | "Deterministic automation: run linters, post to Slack on completion, block commands, back up chat history on PreCompact" (Steering table) | On lifecycle events | "Bypass compaction entirely" | Low |
| Output styles | "Significant role changes (code assistant to general assistant)"; replaces default coding instructions unless `keep-coding-instructions: true` (Steering) | Session start, system prompt | Never compacted | High |
| Append system prompt | "Tone, response length, formatting preferences"; per invocation (Steering table) | Session start, CLI flag | Never compacted | Moderate |
| MCP server | "If you need Claude to *access* something, that's MCP" (SkillsMCP); live data, actions in external systems | "Always available once configured" (LargeCode table); definitions "loaded upfront" (SkillsMCP, 2025-12) unless tool search or `/mcp` toggling is used (Fold, SessionValue) | n/a | Upfront tool definitions |

The five relocation tests (Steering, "When to use each method"), quoted by their headings:

- ""Every time X, always do Y" in CLAUDE.md": use a hook, because "The model choosing to run a formatter is different from the formatter running automatically."
- "“Never do this” in CLAUDE.md": "A real guardrail needs to be deterministic, and the enforcement methods are hooks and permissions." The stated reason is that under pressure, in a long session, an ambiguous situation, or a prompt injection, "the model can fail to follow a prompted rule."
- "A 30-line procedure in CLAUDE.md": "Procedures belong in skills."
- "An API-specific rule without paths": "An unscoped rule is mechanically identical to putting the content in CLAUDE.md: always loaded, always costing tokens."
- "Writing personal preferences to a project-level CLAUDE.md file": use the user-level counterpart; project files are for preferences "team-wide but specific to a given codebase."

Pairwise criteria:

- Path-scoped rule versus nested CLAUDE.md: a rule "when the instruction regards a cross-cutting concern or file that appears in multiple (but not all) corners of the codebase" (Steering, "Rules"). A nested CLAUDE.md fits one directory's conventions and its scoped test and lint commands (Steering; LargeCode).
- Skill versus subagent: a subagent when intermediate results would clutter the main conversation; "Use a skill when you want the procedure to play out inside the main thread so you can see and steer each step." (Steering, "Subagents"). Also: "Use Skills to teach expertise that any agent can apply; use subagents when you need independent task execution with specific tool permissions and context isolation." (SkillsExplained)
- Skill versus MCP: "If you're explaining *how* to do something, that's a skill. If you need Claude to *access* something, that's MCP." (SkillsMCP). MCP instructions stay generic to the server; process and multi-server sequencing go in the skill (SkillsMCP, "Where skills and MCP may overlap").
- Skill versus CLAUDE.md: CLAUDE.md is "always loaded and shapes every interaction"; a skill is "the right place for workflows that should be available but not applied to every prompt." (Subagents, "Skills")
- Prompt versus skill: "If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill." (SkillsExplained)
- Hook versus mod: "hooks can't rewrite events, draw new UI, or replace features. Mods can." (Mods, 2026-10-01; postdates Steering)
- Common misplacements (LargeCode table, "Common confusion"): CLAUDE.md "Using it for reusable expertise that belongs in a skill"; hooks "Using prompts for things that should run automatically"; MCP "Building MCP connections before the basics are working"; subagents "Running exploration and editing in the same session".
- Build order for a harness: CLAUDE.md, hooks, skills, plugins, MCP, "each layer builds on what came before", with LSP and subagents added on top (LargeCode, "The harness matters as much as the model").
- Packaging: skills, subagents, hooks and output styles can be bundled as a plugin (Steering, closing; PluginPortal).

### (b) How to write CLAUDE.md

- Length: "Keep CLAUDE.md under 200 lines, give it an owner, and review changes to it like code." (Steering, "CLAUDE.md files"). Why: every line "consumes tokens and dilutes adherence to the instructions that actually matter." (same)
- Role: "an overview of your codebase, or as an index pointing to other files" (Steering); "the ‘lay of the land,’ not the expertise itself" (Onboarding); the root file "should be pointers and critical gotchas only; everything else drifts into noise." (LargeCode)
- Include: "Build commands, directory layout, monorepo structure, coding conventions, and team norms" (Steering); "exact build and test commands" (VerifyLoops); "the two or three commands you run all day ..., quiet flags included" (SessionValue); a project summary, directory tree, main dependencies and "any non-standard organizational choices" (ClaudeMd); custom tools with usage examples and MCP usage limits (ClaudeMd); "project-specific warnings" (ClaudeMd); the policy for when to delegate to which subagent, e.g. "Code reviews should always use read-only subagents" (Subagents); optionally a "Compact instructions" section saying what `/compact` should keep (SessionValue).
- Exclude: procedures (Steering's example is "A 30-line procedure in CLAUDE.md"; these go to skills), always/never automation (to hooks and permissions), path-specific rules (to scoped rules), personal preferences (to user-level files) (Steering); "reusable expertise that belongs in a skill" (LargeCode); "generic guidance that doesn't apply to your project" (ClaudeMd); "sensitive information, API keys, credentials, database connection strings, or detailed security vulnerability information" (ClaudeMd).
- Style: "being explicit, explaining the why behind constraints, and showing examples." (Steering). "There is no required format"; keep it "concise and human-readable" (ClaudeMd).
- Admission test: "Each addition should solve a real problem you have encountered, not theoretical concerns about what Claude might need." (ClaudeMd). "It's tempting to create a comprehensive CLAUDE.md right away. Resist that urge." (ClaudeMd)
- Starting and maintaining: run `/init`, treat the result as "a starting point, not a finished product", prune and add what Claude could not infer (ClaudeMd); add repeated instructions with the `#` key (ClaudeMd); a stop hook can "propose CLAUDE.md updates while the context is fresh" (LargeCode); when effort is being raised for a task that should not need it, "the fix is often upstream, in your context, your CLAUDE.md, or how the task is scoped" (Effort).
- Review cadence: "a meaningful configuration review every three to six months", and after major model releases, because "instructions written for your current model can work against a future one." (LargeCode)
- Layering: subdirectory CLAUDE.md files load on demand and hold local conventions and per-directory test and lint commands; start sessions in the relevant subdirectory, since Claude walks up the tree and loads parents (LargeCode; Steering). After compaction a subdirectory file is gone until that directory is touched again (Steering).
- Position in the request: tool definitions, then system prompt, then the conversation "with `CLAUDE.md` at the front of it" (SessionValue). Check what is loaded with `/context` in a fresh session (SessionValue).

### (c) Designing, testing and iterating skills

Structure

- A folder with required `SKILL.md` and optional `scripts/`, `references/`, `assets/` (Guide Fundamentals). Folder and `name` in kebab-case and matching; file named exactly `SKILL.md`; no `README.md` inside the folder (Guide Planning). In Claude Code, project skills live in `.claude/skills/<name>/SKILL.md` (Steering; VerifyLoops) and user skills in `~/.claude/skills` (SkillsLaunch). "A skill is a directory, not a single file"; `.claude/commands/` is called "legacy" (Subagents).
- Frontmatter: required `name` and `description`; optional `license`, `compatibility`, `metadata`, `allowed-tools` (Guide Planning; Guide Resources). No XML angle brackets, because "Frontmatter appears in Claude's system prompt. Malicious content could inject instructions." (Guide Planning)
- Body template: instructions as numbered steps with commands and expected output, then examples, then troubleshooting (Guide Planning). Include success criteria "so Claude can self-check" (CreateSkills).
- Granularity: "Aim for single-purpose skills." (CreateSkills). The skill should "work well alongside others, not assume it's the only capability available." (Guide Fundamentals)

Description writing

- "the name and description are the only parts of the SKILL.md file that influence triggering" (CreateSkills; link markup removed).
- Formula: "[What it does] + [When to use it] + [Key capabilities]"; the description "MUST include BOTH" what and when; "Under 1024 characters" (Guide Planning).
- Write it "from Claude's perspective, focusing on triggers, capabilities, and use cases" and include boundaries, e.g. "Not for simple PDF viewing or basic conversions." (CreateSkills). For over-triggering add negative triggers such as "Do NOT use for simple data exploration (use data-viz skill instead)" (Guide Patterns).
- Trigger conditions over capability labels: ""Reviews code for security issues before commits" routes better than "security expert."" (Subagents, about subagent descriptions; the same field logic).
- Balance: "too broad and you get false triggers, too narrow and it never fires" (SkillCreator). Debug by asking "When would you use the \[skill name\] skill?" (Guide Patterns).

Progressive disclosure

- Three levels: frontmatter always loaded, body when relevant, linked files on demand (Guide Fundamentals). Sizes given: metadata about 50 tokens (AgentsSkills) or about 100 tokens (SkillsExplained); body "\<5k tokens" (SkillsExplained), "Keep SKILL.md under 5,000 words" (Guide Patterns).
- "menu" approach: SKILL.md describes what is available and points by relative path to separate files (CreateSkills). "reference do not embed": skills point into a documentation knowledge base instead of duplicating it (Onboarding).
- Too many skills is its own failure: "Evaluate if you have more than 20 - 50 skills enabled simultaneously" (Guide Patterns). Path-scope a skill so it never auto-loads elsewhere in a monorepo (LargeCode). Invoked skills share a re-injection budget after compaction, "oldest dropped first" (Steering).

Scripts

- Code is for "tasks where traditional programming is more reliable than token generation." (SkillsLaunch). "Code is deterministic; language interpretation isn't." (Guide Patterns). "Running a script is cheaper than reasoning through the steps." (Loops)
- Save the script Claude keeps rewriting into the skill and reference it from the doc (AgentsSkills). Scripts for boilerplate "minimize token usage while increasing reliability" (Frontend).

When to create one and how to get the first version

- "Have I done this task at least five times? Will I do it at least ten more times?"; "Don't write skills speculatively." (CreateSkills)
- "iterate on a single challenging task until Claude succeeds, then extract the winning approach into a skill." (Guide Testing)
- Start from "2-3 concrete use cases" with trigger, steps and result (Guide Planning). Use skill-creator and let it interview you (VerifyLoops; Guide Testing).
- For generic output: "identify convergent defaults, provide concrete alternatives, structure guidance at the right altitude" (Frontend).

Evaluation with skill-creator (SkillCreator, 2026-03-03; supersedes the Guide Testing note that it "does not execute automated test suites")

- Evals: test prompts plus files, a description of what good looks like, pass or fail.
- Benchmark mode "tracks eval pass rate, elapsed time, and token usage"; run after model updates and after edits.
- Evals run in parallel agents, "each in a clean context"; comparator agents "judge outputs without knowing which is which" for version A versus B or skill versus no skill.
- Description tuning against sample prompts to cut false positives and negatives.
- Two skill types: "Capability uplift" skills may be outgrown ("Evals tell you when that's happened"); "Encoded preference" skills are durable but must stay faithful to the real workflow.
- Library hygiene: `/skill-creator` to "trim, deduplicate, and restructure" and `/skill-doctor` to see cost and usage and "delete dead weight" (Fold, 2026-10-22).

Manual test plan (Guide Planning, Guide Testing, CreateSkills)

- Triggering: obvious prompts, paraphrased prompts, and unrelated prompts that must not trigger; target "Skill triggers on 90% of relevant queries" over "10-20 test queries".
- Functional: Given/When/Then cases; "Run the same request 3-5 times" for consistency; normal, edge and out-of-scope cases.
- Baseline: same task with and without the skill, comparing tool calls, failed calls and tokens.
- Embedded checks: after appending a check to a skill, invoke it "on a fresh task" and confirm the step ran (VerifyLoops).

Common failure modes and fixes

- Never triggers: description too generic or lacking the phrases users say; revise it (Guide Patterns). "If skills don't activate, broaden your description and add use cases." (CreateSkills)
- Triggers too often: negative triggers, narrower scope (Guide Patterns).
- Instructions not followed: too verbose, buried, or ambiguous; put critical items at the top, replace vague lines with explicit checks, or move the check into a script (Guide Patterns).
- Slow or degraded: SKILL.md too large, everything inline, too many skills enabled (Guide Patterns).
- Conflicts with MCP server instructions (JSON versus markdown tables): "Claude has to guess which one is right." (SkillsMCP)
- Upload and format errors: wrong file name, missing `---`, name with spaces or capitals (Guide Patterns).
- Stale skills: a capability-uplift skill the model no longer needs, or a skill built to compensate for a past model limit, "become overhead once those limitations no longer exist." (SkillCreator; LargeCode)
- Security: skills execute code; "stick to trusted sources" (SkillsLaunch).

The verification-loop skill pattern (VerifyLoops 2026-07-22; Loops 2026-06-30)

- What it is: "an iterative process where Claude checks and attempts to fix the work." Claude already uses deterministic signals (type checkers, linters, tests, runtime errors); "Whatever Claude can't infer becomes the steps you take to manually check a feature", and those steps are what to encode. (VerifyLoops, intro)
- Try built-ins first: `/verify` ("builds, runs, and observes the changes in your application"), the toolchain with exact commands in CLAUDE.md, Code Review, GitHub Actions invoking a verification skill, spec validation against a markdown spec. (VerifyLoops, "Built-in verification loops")
- Trigger to write one: "the same small corrections every time Claude implements a new feature". Write it "in plain English, the way you'd hand it to a new teammate on day one." Project-specific deterministic rules count ("Reject any migration that drops a column without a backfill step"). (VerifyLoops, "Writing verification loops")
- Minimal shape (`verify-log-hygiene`): `name`; `description` stating the check and its trigger condition; `allowed-tools: [Read, Edit, Grep]`; body: read the relevant part of the current diff, state the pass condition per item, "Report each violation with file:line, then fix it". (VerifyLoops, "Make it a skill")
- End-to-end shape (`verify-frontend-change`): do not report a UI change complete from the edit alone; start the dev server and open the page, interact with the change and screenshot before and after, require "zero new errors or warnings" in the console, run a performance trace; "If any step fails, fix the issue and rerun from step 1". (Loops, "Turn-based loops")
- Design rule: include tools that let Claude see, measure or interact with the result; "The more quantitative the checks are, the easier it is for Claude to self-verify." (Loops)
- Where it runs, four placements (VerifyLoops, "Match the check to where it runs"):
  - Standalone: invoked deliberately for cross-cutting checks that do not apply every time. "The signal that you've outgrown standalone is when you're running it after every change."
  - Embedded: one line appended to the producing skill, e.g. "run eslint on it and address any errors before reporting completion." Only for skills you can edit; plugin-managed and built-in skills are overwritten on update, "for those, chain instead."
  - Chained: a wrapper skill calls one skill then another, e.g. "Run /simplify on the current diff first. When /simplify finishes, invoke /verify-no-public-api-changes." Chaining "trades flexibility for automation".
  - On every PR: the same skills run in CI; "Hold off on PR-wide gates while the chain is still in flux".
- The Claude Code team's chain: `/code-review`, then `/simplify`, then a `/verify` skill, then a custom `/design` skill that checks a `DESIGN.md` when UI changed. (VerifyLoops, "Chained")
- Six steps: pick the most frequent manual follow-up of the week; try `/verify`; write the procedure in plain English; hand it to skill-creator or drop the file in `.claude/skills/`; invoke on a new task and confirm the check ran; then try chaining. (VerifyLoops, closing list)
- Cost and limits: "Chained verification loops can increase token spend". Neither article gives a retry cap for the fix loop inside a verification skill; caps are given for `/goal` ("stop after 5 tries") and for generator-verifier loops ("A maximum iteration limit with a fallback strategy") (Loops; CoordPatterns). Inference: a verification skill should state its own cap.
- Verifier pitfalls from the multi-agent articles apply: the "early victory problem" (runs one or two tests and declares success) and rubber-stamping without criteria; fix with concrete criteria, the full suite, and negative tests. (MultiAgent; CoordPatterns)

### (d) Hooks: recommended uses and configuration

- Purpose: "anything that should happen deterministically" (Steering). Three problem classes: remove repeated manual steps, enforce project rules every time, inject dynamic context (Hooks).
- Recommended uses, by event: `PostToolUse` on `Write|Edit` to format and lint (Hooks; Steering; LargeCode); `PreToolUse` to block dangerous commands, with "exit code 2 to deny it" (Steering; Hooks); `Stop` to gate on tests, returning `decision: "block"` with a reason and guarding with `stop_hook_active` to avoid infinite loops (Subagents); `Stop` to reflect on the session and propose CLAUDE.md updates (LargeCode); `SessionStart` to inject git status or team context (Hooks; LargeCode); `PreCompact` to back up the transcript (Hooks; Steering); completion notifications (Opus47; Steering); rewriting noisy commands so only relevant lines return (SessionValue).
- First hook: "The PostToolUse formatter hook is a good first choice" (Hooks). Order of adoption for automation: conversation and CLAUDE.md first, "hooks come later, as workflows mature." (Subagents)
- Types: "command, HTTP, mcp\_tool, prompt, and agent"; all trigger deterministically, but prompt and agent hooks "use Claude’s judgment rather than a set of rules to determine the output." (Steering)
- Where: project `.claude/settings.json`, user `~/.claude/settings.json`, local `.claude/settings.local.json` (Hooks); also managed policy settings and skill or agent frontmatter (Steering).
- Mechanics (Hooks, 2025-12): JSON on stdin (`tool_name`, `tool_input`, `transcript_path`, `cwd`, `permission_mode`); exit 0 success, "Exit code 2 means a blocking error: stderr becomes the error message and the action gets prevented"; JSON output fields `decision`, `reason`, `continue`, `updatedInput`; matchers are case-sensitive, support `Write|Edit` and `Bash(npm test*)`, and apply only to `PreToolUse`, `PostToolUse`, `PermissionRequest`; 60-second default timeout; matching hooks run in parallel; `CLAUDE_PROJECT_DIR` for paths.
- Visibility: hook output mostly does not enter context; a blocking hook's stderr does. A backup written by a `PreCompact` hook is unknown to Claude unless returned (Steering).
- Safety: hooks run with user permissions; edits to hook config need review in `/hooks`; validate stdin, quote variables, use absolute paths, avoid sensitive files (Hooks).
- Ageing: a hook built around a tooling gap becomes redundant when the product closes it (the Perforce `p4 edit` example) (LargeCode).
- Auto-approval hooks (`PermissionRequest`) were suggested in 2025-12 to cut prompt fatigue (Hooks). Inference: auto mode (default from 2026-08) now covers that need, and Nuro shelved its own approval hook when auto mode shipped (AutoProd).

### (e) Subagents and multi-agent patterns

When to use

- Claude Code signals: research needing dozens of file reads; independent tasks; fresh perspective; verification before committing; "exploring ten or more files, or involves three or more independent pieces of work" (Subagents).
- The context test: "*will I need this tool output again, or just the conclusion?*" (Sessions1M). Good for noisy jobs such as log analysis (SessionValue; Steering).
- General conditions: context pollution, parallelisable work, specialisation of tools or prompts (MultiAgent). Restated in 2026-10 as: measurable degradation from context bloat; parallel tasks with disposable fresh contexts; tool-selection trouble or conflicting system-prompt instructions (Fold).
- Tool restriction: a read-only reviewer with Read, Grep and Glob "but not Write or Edit" (SkillsExplained); exploration split from editing, with findings written to a file (LargeCode).

When not to, and when to fold back

- "Sequential, dependent work", "Same-file edits", "Small tasks", "Too many specialist agents" ("Most teams settle on a handful of well-scoped agents") (Subagents). "For a small job it's just overhead." (SessionValue)
- Do not split by role: in a planner/implementer/tester/reviewer experiment "the subagents spent more tokens on coordination than on actual work" (MultiAgent).
- Fold a subagent into the main loop as a skill plus tools unless one of the three conditions holds; "keep it as a subagent only if the folded version scores worse" on an eval (Fold). Shared context "leads to richer outputs and better insights than a set of summaries handed back by subagents" (Fold).
- Newer models delegate less on their own: Opus 4.7 "spawns fewer subagents by default"; ask explicitly when fan-out is wanted (Opus47).

Coordination patterns (CoordPatterns)

- Generator-verifier (needs explicit criteria and an iteration cap); orchestrator-subagent (Claude Code's own pattern; the default starting point); agent teams (persistent workers, independent partitions); message bus (event-driven); shared state (needs termination conditions). "For most use cases, we recommend starting with orchestrator-subagent."
- Workflow shapes: sequential, parallel, evaluator-optimizer; "Design your aggregation strategy before implementing parallel agents." (WfPatterns)
- Verification subagent: give it the artifact, success criteria and tools; it needs no build history (MultiAgent). Dynamic workflows add independent attempts and "adversarial agents working to break the result" (DynWf).
- Briefing: scope clearly, ask for parallel execution, specify the return format, ask for no prior discussion when an unbiased view matters (Subagents).

Costs

- "multi-agent implementations typically use 3-10x more tokens than single-agent approaches for equivalent tasks"; "The primary benefit of parallelization is thoroughness, not speed." (MultiAgent)
- A subagent re-reads what the parent already had and pays for its own turns; the parent gets only what the child chose to report (SessionValue). "Each call still hands back a lossy summary" and "Every call is a nested model loop that adds latency" (Fold).
- Cost controls: give recurring noisy jobs a subagent definition with "model: haiku (or sonnet)", otherwise it runs on the main session's model (SessionValue); Sonnet suits "high-volume sub-agents" (Models); forked subagents start from the parent's cache (Opus55).
- Mechanics: `.claude/agents/` and `~/.claude/agents/`, frontmatter name, description, optional model and tools; nesting "up to five levels deep"; only the final message returns (Steering; Subagents). Subagents can use skills (SkillsExplained).

### (f) The four loop types; /goal, /loop, /schedule, routines, dynamic workflows

Definition: "loops as agents repeating cycles of work until a stop condition is met" (Loops).

| Loop | Trigger | Stop condition | Best for | Usage control | You hand off | Primitive |
|---|---|---|---|---|---|---|
| Turn-based | A user prompt | "Claude judges it has completed the task or needs additional context." | Shorter, irregular tasks | Specific prompts; verification skills to cut turns | The check | Custom verification skills |
| Goal-based | A manual prompt in real time | "Goal achieved OR maximum number of turns reached." | "Tasks that have verifiable exit criteria." | Specific completion criteria and "explicit turn caps" | The stop condition | `/goal` |
| Time-based | A time interval | "You cancel it, or the work completes (the PR merges, the queue is empty)." | Recurring work; watching external systems | "Set longer intervals or react based on events rather than time." | The trigger | `/loop`, `/schedule` |
| Proactive | "An event or schedule, with no human in real time." | Each task exits when its goal is met; the routine runs until turned off | "Recurring streams of well-defined work" | Smaller models for routine runs, "the most capable model for judgment calls" | The prompt | All of the above plus dynamic workflows |

(All cells from Loops, sections named after each loop and the "Getting started" table.)

- `/goal`: an evaluator model checks the condition each time Claude tries to stop. Use deterministic criteria (tests passed, a score threshold) and a cap, e.g. `/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.` `/goal` with no arguments shows turns and tokens so far. (Loops)
- `/loop`: re-runs a prompt on an interval on your machine, e.g. `/loop 5m check my PR, address review comments, and fix failing CI`. It "fires as a full turn in the session you set it up in, carrying that whole conversation with it every time"; start it from a fresh session in another terminal. (Loops; SessionValue)
- `/schedule` and routines: a routine is a saved prompt, repo and connectors that runs in the cloud on a schedule, an API call, or a GitHub event; `/schedule` tasks are scheduled routines. Daily caps at launch: Pro 5, Max 15, Team and Enterprise 25, drawing on normal usage limits. (Routines; Loops)
- Dynamic workflows: Claude writes an orchestration script running "tens to hundreds of parallel subagents", with verification and adversarial review, saving progress so an interrupted job resumes. Start by asking, or with `ultracode` in the effort menu. Fits codebase-wide audits, large migrations and work to be "checked twice". (DynWf)
- Composition for unattended work: `/schedule` for the trigger, `/goal` for done, skills for how to verify, a workflow for fan-out, auto mode to avoid permission stops. (Loops, "Proactive loops")
- Stop conditions elsewhere in the batch: "Define maximum iteration counts and specific quality thresholds" (WfPatterns); a maximum iteration limit "with a fallback strategy (escalate to a human, return the best attempt with caveats)" (CoordPatterns); for shared-state systems "a time budget, a convergence threshold (no new findings for N cycles), or a designated agent" (CoordPatterns); a `Stop` hook needs the `stop_hook_active` guard (Subagents); auto mode falls back to manual after "three blocks in a row, or twenty across a session" (AutoDefault).
- Token management (Loops, "Managing token usage"): right primitive and model; clear success and stop criteria; "Pilot before a large run: Dynamic workflows can spawn hundreds of agents"; scripts for deterministic work; do not run routines more often than the watched thing changes; review with `/usage`, `/goal`, `/workflows`. Workflows "can consume substantially more tokens than a typical Claude Code session" and ask for confirmation the first time (DynWf).
- Quality in loops: clean codebase, verification skills, reachable docs, a second agent for review; "don’t stop at fixing the individual issue, try to encode it to improve the system for all future iterations." (Loops)
- Suitable unattended tasks have "a clear, measurable signal an agent can iterate against on its own" (AutoProd).

### (g) Permissions, auto mode and sandboxing

- Why not manual prompts: "users approve 97% of permission prompts"; testers caught a planted dangerous command 13.6% of the time, falling to about 5% after 50 or more prompts, against 89% for auto mode (AutoDefault).
- Auto mode: a classifier reviews each tool call for actions that are "irreversible, destructive, or aimed outside your environment"; default for new Pro, Max and Team sessions from 2026-08-14; classifier tokens not charged on those plans (AutoDefault). Switch with Shift+Tab.
- Interaction with rules: "Permission rules still fire before the classifier in auto mode", except allow rules broad enough for arbitrary code execution such as `Bash(python:*)`, which are set aside while in auto mode (AutoDefault). Consequence drawn here (inference): interpreter-wide allow rules buy nothing under auto mode; explicit deny rules still matter.
- Guardrails teams keep under auto mode: deny "the most dangerous commands, like recursive deletes, outright in their settings" (AutoProd); configure it "not to approve actions that communicate with other people, like sending Slack messages or emails" (AutoProd); customisable hard denies, with exfiltration never approved (AutoDefault); the classifier checks push destinations and git status before destructive git commands (AutoDefault).
- When to step out: "For high-stakes changes to production infrastructure, we still recommend reviewing Claude's actions yourself." (AutoDefault). One engineer "switches to accept edits and verifies each tool call by hand" for Terraform, AWS and live POST calls, and another reviews PR comments made on his behalf in interactive mode (AutoProd). Auto mode "should only be used for tasks where users trust the general direction." (Harness)
- Bypass: `--dangerously-skip-permissions` "should not be used outside of isolated environments." (AutoLaunch). Even so, 25% of interactive sessions started in bypass mode as of mid-2026 (AutoDefault).
- Sandboxing: `claude --sandbox` isolates bash with OS primitives (bubblewrap, seatbelt); "effective sandboxing requires *both* filesystem and network isolation"; write access limited to the working directory, network through an allowlisting proxy; applies to spawned subprocesses (Sandbox, 2025-10). Cloud sessions run in isolated sandboxes with credentials kept outside (Sandbox; Web).
- Deterministic layer: "the enforcement methods are hooks and permissions"; managed settings are the only organisation-wide enforcement (Steering). Commit `permissions.deny` in `.claude/settings.json` so exclusions are version-controlled (LargeCode). Promote hard-to-reverse actions to dedicated, confirmable tools: "Reversibility is often a good criterion" (Harness).
- Prompt injection: tool results are screened and a warning added to context; 0 of 720 indirect-injection attempts succeeded against Fable 5, Opus 5 and Sonnet 5 in auto mode in a third-party test (AutoDefault). Instructions alone can be defeated by injection (Steering).
- Supply-chain cautions: mods "aren’t sandboxed" and run with full access (Mods); skills execute code, so use trusted sources (SkillsLaunch); hooks run with user permissions (Hooks).
- Residual risk is stated: auto mode "does not eliminate risk" (AutoDefault); "Ultimately, you’re still responsible for what happens." (AutoProd)

### (h) Context and session management, effort, model selection, advisor

- 1M context is the default window in Claude Code on the plans named in 1M-GA ("Claude Code has a context window of one million tokens", Sessions1M), but "model performance degrades as context grows" (context rot) and the rule is "when you start a new task, you should also start a new session." (Sessions1M)
- Five moves after any turn: continue, `/rewind` (Esc Esc), `/clear`, compact, subagent (Sessions1M). Table: still relevant, continue; wrong path, rewind; bloated mid-task, `/compact <hint>`; new task, `/clear`; noisy next step, subagent (Sessions1M, "Putting it together").
- Rewind beats correcting and beats compacting for a bad tangent: it keeps the cached prefix and "costs nothing" (Sessions1M; SessionValue).
- Compaction: lossy; steer it (`/compact focus on the auth refactor, drop the test debugging`); bad autocompacts happen "when the model can’t predict the direction your work is going" and the model "is at its least intelligent point when compacting", so compact proactively and state what comes next (Sessions1M). "Compact before you step away rather than after" because the cache expires (Opus55; SessionValue). `/autocompact 200k` restores the earlier threshold on 1M models (SessionValue).
- Clearing and handoff: with `/clear` "*you* write down what matters" (goal, constraint, files, approaches ruled out) (Sessions1M); `/rename` first to find the session later (SessionValue); "summarize from here" produces a handoff message (Sessions1M); for implementation after planning, "I make a new session and pass any artifacts to the prompt", e.g. a spec file and a prototype, and keep an `implementation-notes.md` with deviations (FableGuide). Plans and to-do lists "don't persist across sessions"; written context does (Onboarding).
- What fills context: tool definitions, system prompt, CLAUDE.md, then tool results that are re-sent every turn. Reduce with @-mentions, specific prompts, quiet flags, `/mcp` off for unused servers, and `/context` to inspect (SessionValue).
- Cache discipline: `/model`, `/effort`, fast mode, `/compact` and idle time break the cache; cheap moments to switch are session start or right after `/clear` (SessionValue). "Avoid switching models during a session ... If you need a cheaper model, use a subagent." (Harness). For Opus 5.5 and Fable 5.1 effort can now change "without resetting your cache" (Opus55). Check cached-read share with `/usage` (Opus55).
- Effort: controls thinking, files read, verification and how far Claude goes before checking in; "for most tasks you should use the model’s default effort level"; treat it as "a general preference" not a per-task dial (Effort). For Opus 4.7 the levels were `low`, `medium`, `high`, `xhigh` (default), `max` ("more prone to overthinking") (Opus47). `ultracode` sets xhigh and lets Claude decide when to use a workflow (DynWf).
- Diagnostic: "did it not *try* hard enough, or did it not *know* enough?" Larger model for subtle bugs, unfamiliar domains, architecture; higher effort if it skipped a file or did not run the tests; first check context and scoping (Effort).
- Model selection: "start with the most intelligent generally available model and use effort level to dial in performance and cost" (Models). Family: "Fable for the hardest problems", Opus "for long-horizon work and coding", Sonnet "for everyday work and analysis", Haiku "for high-volume and routine tasks" (Cost, list items). Opus versus Fable: move to Fable when evals show Opus struggling (Models). Smaller models want "specific instructions directing execution" (Effort). Drop down when work "has been routine for a while" (Effort), at a session boundary (SessionValue).
- Advisor strategy: a cheaper executor consults a stronger model for "a plan, a correction, or a stop signal"; Claude Platform API tool `advisor_20260301` with `max_uses` (Advisor). Results: Sonnet 4.6 plus Opus 4.6 advisor, "a 2.7 percentage point increase" on SWE-bench Multilingual at 11.9% lower cost per task (Advisor); Sonnet 5 with a Fable 5 advisor "within 10% of Fable 5’s score at 63% of the price" (Models). No article in this batch documents an advisor setting inside Claude Code.
- First-turn discipline: "Every user turn adds reasoning overhead. Batch your questions" (Opus47).

### (i) Large-codebase and onboarding practices

- Navigation is agentic search on the live tree, with no index to go stale; it "works best when Claude has enough starting context to know where to look." (LargeCode). Start with agentic search and add semantic search only if needed (AgentSDK).
- Lean, layered CLAUDE.md: root for pointers and gotchas, subdirectories for local conventions; start sessions in the relevant subdirectory (LargeCode).
- Scope test and lint commands per subdirectory; full-suite runs for a one-service change cause "timeouts and wastes context on irrelevant output." (LargeCode)
- Exclude generated files, build artefacts and third-party code with ignore files and committed `permissions.deny` (LargeCode).
- Codebase map: a root markdown file with one line per top-level folder when the structure is not self-explanatory (LargeCode); a tree and architecture summary in CLAUDE.md (ClaudeMd).
- LSP via a code intelligence plugin so Claude "searches by symbol, not by string" (LargeCode).
- Split exploration from editing with a read-only subagent that writes findings to a file (LargeCode); research before implementing (Subagents).
- Onboard like a trainee: "explaining enough to achieve a successful limited project and produce improved context for the next iteration" (Onboarding). "context is just another artifact to maintain and grow"; version it (Onboarding).
- Skills as the expertise layer, pointing into docs ("reference do not embed"); a `debugging` skill that forces root-cause analysis before any fix; a `version-control` skill for commit and PR conventions (Onboarding).
- MCP where real data is needed (test results, exception reports), and only after the basics work (Onboarding; LargeCode).
- Ownership: one DRI for settings, permissions policy and CLAUDE.md conventions; review every three to six months (LargeCode). For a solo developer the DRI is the developer; the cadence still applies (inference).
- Keep the codebase clean, since "Claude follows patterns and conventions that already exist in your codebase" (Loops); point Claude at source code as the best reference (FableGuide).
- Find unknowns before building: blind spot pass, prototypes, an interview "one question at a time", an implementation plan that leads with the decisions likely to change, and a post-change quiz (FableGuide).

### (j) Explicit statements that older advice no longer applies

- Harness assumptions go stale: "agent harnesses encode assumptions about what Claude can’t do on its own, but those assumptions grow stale as Claude gets more capable." Context resets added for Sonnet 4.5's "context anxiety" became "dead weight" with Opus 4.5. (Harness, 2026-04-02)
- Project instructions: "instructions written for your current model can work against a future one"; a rule to split every refactor into single-file changes "would prevent a newer one from making coordinated cross-file edits it handles well." Compensating skills and hooks "become overhead once those limitations no longer exist." (LargeCode, 2026-05-14)
- Architectures: much router/planner/specialist structure "was doing work the model no longer needed done for it"; "starting with Opus 4.5, models became capable of managing far more in a single loop than most teams expected"; recent models "check their work as they go, which makes some harness elements redundant." A tool, `/claude-api prompt-audit`, exists to "flag instructions written for older models". (Fold, 2026-10-22)
- System prompt size: Anthropic "reduced Claude Code’s system prompt for more advanced models by over 80%" (Fold).
- Prompt techniques: "XML tags and heavy role prompting are less necessary with modern models."; extended thinking "is generally preferable to manual chain of thought prompting"; prompting is moving to "less scaffolding, more curation." (PromptBP)
- Thinking controls: "Extended Thinking with a fixed thinking budget is not supported in Opus 4.7." (Opus47); "You cannot turn off thinking on Opus 5.5, and Fable 5.1" (Fold); `MAX_THINKING_TOKENS=0` works "except on Fable 5" (SessionValue).
- Model behaviour shifts to re-tune for: Opus 4.7 is less verbose, calls tools less and spawns fewer subagents by default; "we recommend experimenting with effort rather than just porting over an old setting." (Opus47)
- Skills: "Capability uplift skills may become less necessary as models improve"; over time "a natural-language description of *what* the skill should do may be enough" (SkillCreator).
- Multi-agent thresholds: "These thresholds will shift as models improve. Current limits represent practical guidelines, not fundamental constraints." (MultiAgent)
- Permissions: per-action manual approval is no longer the default on Pro, Max and Team; Anthropic reports auto mode "matched or outperformed manual review" on every measure it tested (AutoDefault).
- Commands: `.claude/commands/` is the "legacy" single-file format; skills replace it (Subagents).
- Unknowns now bound quality: Fable "is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns." (FableGuide)

### Contradictions and open questions

- Context clearing with 1M. 1M-GA (2026-03) says summarisation and context clearing "are no longer needed"; Sessions1M (2026-04) and SessionValue (2026-08) say to start a new session per task and `/clear` between tasks because of context rot and cost. The later, Claude Code specific articles should win.
- Effort tuning. Opus47 (2026-04) says you can "toggle between effort levels during the same task"; Effort (2026-07) says treat effort as a general preference; SessionValue (2026-08) says changing it mid-conversation breaks the cache; Opus55 (2026-09) says for Opus 5.5 and Fable 5.1 it no longer resets the cache. Net: default effort, change at session boundaries unless on the newest models.
- Pipelines of subagents. Subagents (2026-04) lists "Pipeline workflows" (design, implement, test) as a use; MultiAgent (2026-01) lists "Sequential phases of the same work" as a problematic boundary, and Fold (2026-10) argues against role-shaped structure. Subagents' own "When shouldn’t you" section also warns against sequential dependent relays.
- Separate verifier or not. MultiAgent says capable orchestrators "are increasingly able to evaluate subagent work directly without a separate verification step"; Loops, Subagents and DynWf recommend a fresh-context reviewer; AgentSDK calls LLM-as-judge "generally not a very robust method". Common ground: deterministic checks first, explicit criteria for any model reviewer.
- Workflows in CLAUDE.md. ClaudeMd (2025-11) puts standard workflows and custom commands in CLAUDE.md and `.claude/commands/`; Steering (2026-06) moves procedures to skills.
- Emphatic wording. PromptBP and Opus47 favour reasons and positive examples over "NEVER"; yet Anthropic's own example skills and guide use "CRITICAL", "MUST", "Never report..." (CreateSkills, Guide Patterns, Loops), and a practitioner's skill description uses "ALWAYS load when..." (Onboarding). No source in this batch measures the difference on current models.
- Tool-count thresholds differ: "often 20+" (MultiAgent), "15-20+" (MultiAgent, another section), "30-50 tool definitions" (Fold); skills "20 - 50" enabled (Guide Patterns).
- Skill metadata size differs: about 50 tokens (AgentsSkills) versus about 100 (SkillsExplained); SKILL.md "\~500 tokens" (AgentsSkills) versus under 5,000 words (Guide Patterns).
- Where CLAUDE.md sits: "part of Claude's system prompt" (ClaudeMd) versus at the front of the conversation after the system prompt (SessionValue).
- `allowed-tools` syntax differs between the Guide (space-separated string) and VerifyLoops (YAML list).
- Model choice direction: Models recommends starting with the most intelligent model, and notes the docs also cover starting cheap and moving up; Cost stresses matching model to task. Both agree on evals as the arbiter.
- Not covered in this batch: `AGENTS.md` is never mentioned, so cross-harness instruction files have no support here beyond the Agent Skills open standard and the `compatibility` field; no article explains how sandboxing and auto mode should be combined; no advisor configuration for Claude Code; no retry cap for verification skills; the saved Subagents article lacks its example files; mods are too new to appear in the decision framework.

## Per source

Listed in batch order (`refs/sources/batches/anthropic-claude-com-practice.txt`). Dates are from each
item's `meta.json`. Quotes are verbatim from the saved `article.md` (markdown emphasis and link
markup dropped); the locator in brackets is the section heading. A quote inside a "Caveats" line
that compares with another article comes from that other article's saved file, which is named
beside it. Every quote was checked by script against the saved files after writing. Where
`meta.json` gives an "author" that is really a quoted customer, the entry says "Anthropic" instead.

### 1M context is now generally available for Opus 4.6 and Sonnet 4.6 (Anthropic, 2026-03-13)
File: refs/articles/claude.com/resources-articles-1m-context-ga/article.md   URL: https://claude.com/resources/articles/1m-context-ga
Thesis: The 1M window became standard-priced for Opus 4.6 and Sonnet 4.6 and the default in Claude Code on Max, Ultra, Team and Enterprise with Opus 4.6. The claim is that summarisation and clearing work is "no longer needed" at this size.
Practices:
- Pricing has no long-context multiplier: "a 900K-token request is billed at the same per-token rate as a 9K one." (intro)
- Claude Code effect: sessions "can use the full 1M context window automatically, meaning fewer compactions and more of the conversation kept intact." (intro)
Evidence and numbers: $5/$25 per million tokens Opus 4.6, $3/$15 Sonnet 4.6; Opus 4.6 "scores 78.3% on MRCR v2"; 600 images or PDF pages per request (up from 100); one customer quote reports "a 15% decrease in compaction events"; another raised its window from 200k to 500k and "it actually uses fewer tokens overall" (customer quotes, unattributed in the saved text).
Tools and files named: none specific to Claude Code configuration.
Caveats: Launch post. Its claim that "lossy summarization, and context clearing ... are no longer needed" ("Long context that holds up") is contradicted one month later by the session-management article (2026-04-15), which says that even with 1M "context rot may occur" and advises a new session per task, and by the session-value article (2026-08-14), which advises `/clear` between tasks. Model names are superseded (Opus 4.7, Fable 5, Opus 5.5 follow).
Relevance: medium. Establishes that 1M is the default window; the claim that clearing is no longer needed should not be designed around.

### A field guide to Claude Fable 5: Finding your unknowns (Thariq Shihipar, Anthropic, 2026-07-06)
File: refs/articles/claude.com/resources-articles-a-field-guide-to-claude-fable-finding-your-unknowns/article.md   URL: https://claude.com/resources/articles/a-field-guide-to-claude-fable-finding-your-unknowns
Thesis: With Fable, output quality is limited by how well the human clarifies "unknowns" (the gap between the prompt/skills/context and the real codebase). The author uses a set of cheap pre-, mid- and post-implementation patterns to surface them.
Practices:
- Framing: "Claude Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns." (intro)
- Balance specificity: "If you are too specific, Claude will follow your instructions even when a pivot may be more appropriate"; too vague and it falls back on industry defaults. ("Help Claude help you")
- Blind spot pass: ask literally for a "blind spot pass" and "unknown unknowns", stating who you are and what you know. ("Blind Spot Pass")
- Brainstorm and prototype first for see-it-to-know-it criteria, e.g. "an HTML page with 4 wildly different design directions", or a single HTML mock with fake data before touching the app. ("Brainstorms and prototypes")
- Interview: "Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture." ("Interviews")
- References: "the absolute best reference is *source code*"; point at a folder, even in another language, rather than a screenshot. ("References")
- Implementation plan that leads with what is likely to change (data models, type interfaces, UX flows) and buries mechanical refactoring. ("Implementation Plans")
- New session for implementation: "I make a new session and pass any artifacts to the prompt", e.g. a spec file and a prototype. ("Implementation notes")
- Ask for a temporary `implementation-notes.md` with a "Deviations" section: on an edge case, "pick the conservative option, log it under 'Deviations', and keep going." ("Implementation notes")
- Post-implementation quiz: an HTML report plus a quiz; "I only merge after I pass the quiz perfectly." ("Quizzes")
Evidence and numbers: none measured; anecdote that the Fable launch video was edited end to end with Claude Code.
Tools and files named: `implementation-notes.md` (or `.html`), HTML plans and reports, Remotion, Whisper, ffmpeg.
Caveats: One person's workflow. The author says "just planning ahead isn’t always enough": unknowns also appear deep in implementation. (intro)
Relevance: high. Directly usable as plan/interview/handoff/quiz commands and as a rule to pick the conservative option and log deviations.

### A guide to cost visibility and control in Claude (Anthropic, 2026-08-04)
File: refs/articles/claude.com/resources-articles-a-guide-to-cost-visibility-and-control-in-claude/article.md   URL: https://claude.com/resources/articles/a-guide-to-cost-visibility-and-control-in-claude
Thesis: Measure cost per outcome, not tokens, and match the model to whether work is hard or merely large. Mostly enterprise admin controls.
Practices:
- Model family as of 2026-08: "Fable for the hardest problems; Opus for long-horizon work and coding; Sonnet for everyday work and analysis; Haiku for high-volume and routine tasks." ("Useful ways to think about cost", list reflowed)
- Under-sizing costs more: a cheaper model on complex reasoning "burns tokens on retries and needs more human correction." (same section)
- API levers: prompt caching ("can cost 10% of the normal input rate on cache hits"), batch at half price, effort parameter, advisor strategy. ("Controls for building on the API")
Relevance: low for a solo setup; the four-tier model description and the retries argument are the usable parts.

### Agent view in Claude Code (Anthropic, 2026-05-11)
File: refs/articles/claude.com/resources-articles-agent-view-in-claude-code/article.md   URL: https://claude.com/resources/articles/agent-view-in-claude-code
Thesis: One CLI screen lists every Claude Code session with whether it is waiting, working or done.
Practices:
- Open with the left arrow from any session or `claude agents`; peek and answer inline; Enter attaches. ("How it works")
- `/bg` sends an existing session to the background; `claude --bg [task]` starts one there. ("Background anything")
- Looping jobs ("PR babysitters, dashboard updaters") show their next run time in the list. ("How developers are using agent view")
Tools and files named: `claude agents`, `/bg`, `claude --bg`.
Caveats: Research Preview at publication; opt in by running `claude agents`.
Relevance: medium. It is the control surface for parallel and looping sessions; no configuration to design.

### Claude Code now supports artifacts (Anthropic, 2026-06-18)
File: refs/articles/claude.com/resources-articles-artifacts-in-claude-code/article.md   URL: https://claude.com/resources/articles/artifacts-in-claude-code
Thesis: A session can publish a live web page (PR walkthrough, incident page, dashboard) built from session context, republished in place at one link.
Practices: example prompt for engineers: "Make an artifact walking through this PR — the diff, the reasoning, and what I tested." ("Getting started")
Caveats: beta for Team and Enterprise orgs only; artifacts "cannot be made public".
Relevance: low for a solo developer on a personal plan (availability); the PR-walkthrough idea overlaps with the Fable field guide's HTML reports.

### Auto mode is now the default in Claude Code for Pro, Max, Ultra, and Team plans (Conner Phillippi et al., Anthropic, 2026-08-07; update note dated 2026-10-22)
File: refs/articles/claude.com/resources-articles-auto-mode-default-in-claude-code/article.md   URL: https://claude.com/resources/articles/auto-mode-default-in-claude-code
Thesis: Auto mode replaces per-action prompts with a classifier aimed at actions that are "irreversible, destructive, or aimed outside your environment", and Anthropic's tests found it matched or beat a human clicking through prompts. From 2026-08-14 new sessions on Pro, Max and Team start in auto mode. (`meta.json` lists "Kai Zhou" as author; he is a quoted Nuro engineer. The byline in the text is Conner Phillippi.)
Practices:
- Fallback thresholds: if Claude cannot make progress, "three blocks in a row, or twenty across a session—Claude Code falls back to manual approvals." (intro)
- Permission rules still run first, with one exception: "allow rules broad enough to grant arbitrary code execution (e.g. python:\*)" are "set aside while in auto mode"; settings files are not modified. ("Comparing manual review to auto mode")
- Hard denies: data exfiltration "sits in a category the classifier is designed to never approve"; hard-deny rules are "customizable via settings". ("Making auto mode even safer")
- The classifier checks whether a push or PR destination "is public, private, or trusted", and sees `git status` before commands such as `git reset --hard`. (same section)
- Tool results are screened by an API-side probe for injection; on a hit "a warning is added to Claude's context". (same section)
- Switch modes with Shift+Tab (CLI) or the mode dropdown (desktop); admins pin `defaultMode` or set `disableAutoMode` in managed settings. ("Getting started")
- Residual-risk advice: "For high-stakes changes to production infrastructure, we still recommend reviewing Claude's actions yourself." ("Getting started")
Evidence and numbers: users approve 97% of permission prompts but reject 39% of plans; 49.5% of active CLI users have a Bash allow-rule (5% allow any shell command, 43% have interpreter rules such as `Bash(python:*)` or `Bash(node:*)`); 62% have used `bypassPermissions` or "don't ask again" on Bash; 25% of interactive sessions start in bypass mode. Controlled study, 1,053 paid testers: humans caught the dangerous command 13.6% of the time, auto mode blocked 89%; human catch rate fell from about 17% early to about 5% after 50+ prompts. Flagged production sessions at severity 7+: 6.3% (manual) versus 2.4% (auto) contained unrequested harm. Apollo Research red-team: classifier miss rate fell from 12% to 7% on synthetic adversarial attacks. Trajectory Labs: 0 of 720 indirect-injection attempts succeeded against Fable 5, Opus 5 or Sonnet 5 in auto mode; 0.09% average in `bypassPermissions`. Auto mode users "ship about 25% more PRs". Classifier overhead tokens no longer charged on Pro, Max, Ultra and Team.
Tools and files named: auto mode, `bypassPermissions`, `defaultMode`, `disableAutoMode`, managed settings, `Bash(python:*)`, Shift+Tab; Claude Code v2.1.205 was the tested version.
Caveats: Vendor's own evaluation; the 7% miss rate is on synthetic attacks and "should not be taken as the miss rate on real traffic". The study used a test environment, not participants' own code. Auto mode "does not eliminate risk". Enterprise and API remained opt-in at publication.
Relevance: high. Sets the baseline permission mode for the setup and says which allow-rules are pointless or ignored under it.

### Running auto mode in production (Molly Vorwerck, Anthropic, 2026-08-07)
File: refs/articles/claude.com/resources-articles-auto-mode-in-production/article.md   URL: https://claude.com/resources/articles/auto-mode-in-production
Thesis: Three companies run auto mode as their daily default, inside explicit deny rules and other guardrails, and step out of it for production infrastructure and for actions that speak to other people.
Practices:
- Guardrails under auto mode at Nuro: engineers "deny the most dangerous commands, like recursive deletes, outright in their settings." ("Powering longer running autonomous agents at Nuro")
- Long unattended runs work for tasks with a measurable signal: "the metric itself tells the agent whether it’s improving or regressing." (same section)
- Step out for sensitive work: with Terraform, AWS or live POST calls, a Gusto engineer "switches to accept edits and verifies each tool call by hand." ("Shipping PRs faster and safer at Gusto")
- Two teams configured auto mode "not to approve actions that communicate with other people, like sending Slack messages or emails." ("Accelerating the software development lifecycle (SDLC) at Garner Health")
- Garner's lifecycle is a plugin of skills: pick up a task, explore, commit context files to the repo, run "antagonistic research" on its own assumptions, then implement. (same section)
- Review of outward-facing output stays manual: Kai Zhou switches to interactive mode when Claude Code reviews a PR on his behalf. (Nuro section)
Evidence and numbers: "Claude works 9x longer between interruptions than under the previous default"; one engineer's 2,425 sessions since December; about 10% of Gusto transcripts since mid-May 2026 include a denial; a 10 p.m. to 5 a.m. run that produced three PRs.
Tools and files named: auto mode, accept edits mode, settings deny rules, skills plugin, MCP proxy with tool guards (Gusto).
Caveats: Customer testimonials. "Ultimately, you’re still responsible for what happens." Before auto mode shipped, Nuro prototyped a hook sending each action to a small model, then shelved it.
Relevance: high. Gives the concrete shape of a setup with fewer prompts: auto mode plus explicit denies, plus a rule against unapproved outbound messages.

### Auto mode for Claude Code (Anthropic, 2026-03-24; update note 2026-07-10)
File: refs/articles/claude.com/resources-articles-auto-mode/article.md   URL: https://claude.com/resources/articles/auto-mode
Thesis: Launch note for auto mode as a research preview: a classifier reviews each tool call as a middle path between default prompts and `--dangerously-skip-permissions`.
Practices:
- `--dangerously-skip-permissions` "should not be used outside of isolated environments." ("How it works")
- At launch: enable with `claude --enable-auto-mode`, cycle with Shift+Tab; admins disable with `"disableAutoMode": "disable"`. ("Getting started")
Caveats: Superseded by the 2026-08-07 posts (now default, GA since 2026-07-10 per its own update line). At launch Anthropic still said "we continue to recommend using it in isolated environments" ("What to expect"); the August post narrows this to reviewing high-stakes production changes yourself.
Relevance: medium, mostly historical.

### Prompt engineering best practices for 2026 (Anthropic, 2025-11-10; later edited, since it links to a "Claude 5 generation" post and to the 2026-06 steering article)
File: refs/articles/claude.com/resources-articles-best-practices-for-prompt-engineering/article.md   URL: https://claude.com/resources/articles/best-practices-for-prompt-engineering
Thesis: Clear, explicit, motivated instructions do most of the work; advanced techniques are added only when they fix a specific problem. Several formerly standard techniques are described as less necessary.
Practices:
- Explain why instead of shouting: "NEVER use bullet points" is given as the less effective form; a reasoned preference lets the model "make better decisions about related formatting choices." ("Provide context and motivation")
- Examples are followed closely: "Claude 4.x and similar advanced models pay very close attention to details in examples." Start with one example. ("Use examples")
- Permit uncertainty: "If the data is insufficient to draw conclusions, say so rather than speculating." ("Give permission to Claude to express uncertainty")
- Format control: "Tell the AI what TO do instead of what NOT to do", and match the prompt's own formatting to the output wanted. ("Control the output format")
- Be explicit about action versus advice: say "Change this function" rather than "Can you suggest changes?" ("Troubleshooting common prompt issues")
- Task splitting still helps "not because of context limitations" but for focus; put the most critical details at the beginning or end of long context. ("Working with long content")
- Persistent instructions belong elsewhere: "move them into CLAUDE.md files, skills, or other steering methods". ("Final words of advice", link text)
Evidence and numbers: none.
Tools and files named: extended thinking, prefill (API), XML tags.
Caveats, and explicit statements that older advice no longer applies: "XML tags and heavy role prompting are less necessary with modern models." ("Common mistakes to avoid"); "Longer, more complex prompts are NOT always better." (same); extended thinking "is generally preferable to manual chain of thought prompting" ("Chain of thought prompting"). The intro says prompting is converging with context engineering: "less scaffolding, more curation." The article itself still uses a "DO NOT use ordered lists" example and the "go beyond the basics" request, written for Claude 4.x; the Opus 4.7 and Fable posts later describe models that need less of this. Fixed thinking budgets are tied to older behaviour (see the Opus 4.7 post: a fixed thinking budget "is not supported").
Relevance: medium. The rules to explain why, state the positive form and start with one example apply to writing CLAUDE.md, rules and skills.

### Best practices for using Claude Opus 4.7 with Claude Code (Anthropic, 2026-04-16)
File: refs/articles/claude.com/resources-articles-best-practices-for-using-claude-opus-4-7-with-claude-code/article.md   URL: https://claude.com/resources/articles/best-practices-for-using-claude-opus-4-7-with-claude-code
Thesis: Opus 4.7 reasons more after each user turn and delegates less by default, so the efficient pattern is a fully specified first turn, few interruptions, and effort left at the new default `xhigh`.
Practices:
- Treat it "more like a capable engineer you’re delegating to than a pair programmer you’re guiding line by line". ("Structuring interactive coding sessions")
- First turn should carry "intent, constraints, acceptance criteria, and relevant file locations"; drip-fed ambiguous prompts reduce token efficiency and sometimes quality. (same section)
- "Every user turn adds reasoning overhead. Batch your questions". (same section)
- Completion notifications: ask Claude to play a sound when done "and it can create its own hook-based notifications." (same section)
- Effort levels: `low`/`medium` for cost- or latency-sensitive, tightly scoped work; `high` "if you’re running concurrent sessions or want to spend less"; `xhigh` default and recommended; `max` "shows diminishing returns and is more prone to overthinking". ("Recommended effort settings for Opus 4.7")
- Do not port an old effort setting: "we recommend experimenting with effort rather than just porting over an old setting." (same section)
- Fewer subagents by default; if fan-out is wanted, say so. Suggested text: "Do not spawn a subagent for work you can complete directly in a single response". ("Behavior changes worth knowing")
- Fewer tool calls and more reasoning by default; to get more searching or reading, describe "when and why the tool should be used." (same section)
- Style steering: "positive examples of the voice you want work better than negative “Don’t do this” instructions." (same section)
Evidence and numbers: none measured; an updated tokenizer and more thinking at high effort raise token use relative to Opus 4.6.
Tools and files named: effort levels `low`, `medium`, `high`, `xhigh`, `max`; adaptive thinking; auto mode; Shift+Tab; hooks for notifications.
Caveats, and explicit statements that older advice no longer applies: "Extended Thinking with a fixed thinking budget is not supported in Opus 4.7." Prompts and harnesses "carefully tuned ... for the older model" may need changes (paraphrase of "Behavior changes worth knowing"). Superseded in part: the 2026-07-07 effort article says to stay on each model's default effort and treat effort as a general preference, and newer models (Opus 4.8, Opus 5, Opus 5.5, Fable 5) follow.
Relevance: high for the first-turn/acceptance-criteria and effort guidance; model-specific defaults are dated.

### Beyond permission prompts: making Claude Code more secure and autonomous (Anthropic, 2025-10-08)
File: refs/articles/claude.com/resources-articles-beyond-permission-prompts-making-claude-code-more-secure-and/article.md   URL: https://claude.com/resources/articles/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
Thesis: OS-level sandboxing of the bash tool (filesystem plus network isolation) lets Claude run with fewer prompts while containing a successful prompt injection.
Practices:
- Both halves are required: "effective sandboxing requires *both* filesystem and network isolation." Without network isolation, key files can be exfiltrated; without filesystem isolation the sandbox can be escaped. ("Sandboxing: a safer and more autonomous approach")
- Sandboxed bash allows read/write in the current working directory and blocks modification outside it; network goes through a proxy that enforces a domain allowlist and asks about new domains. ("Sandboxed bash tool")
- Restrictions apply to "any scripts, programs, or subprocesses that are spawned by the command." (same section)
- Start with `claude --sandbox`. ("Getting started")
- Claude Code on the web keeps git credentials outside the sandbox; a proxy checks "it is only pushing to the configured branch". ("Claude Code on the web")
Evidence and numbers: none in this saved version.
Tools and files named: `claude --sandbox`, Linux bubblewrap, macOS seatbelt, sandbox runtime (open source), Claude Code on the web.
Caveats: The saved page is visibly an unpolished draft ("\[Github link?\]", "\[XXX\]", merged words), and its FAQ is generic filler. It is the oldest permissions source in the batch; "approval fatigue" is the motivation later quantified in the 2026-08 auto mode post. It predates auto mode. Inference: sandboxing and auto mode are complementary layers, but no article in this batch states how to combine them.
Relevance: high. Sandboxing is the OS-enforced layer under any fewer-prompts configuration.

### Build plugins for Claude with the directory submission portal (Anthropic, 2026-09-25)
File: refs/articles/claude.com/resources-articles-build-plugins-for-claude/article.md   URL: https://claude.com/resources/articles/build-plugins-for-claude
Thesis: Plugins are now "the main way to build third-party extensions for Claude"; a portal handles submission, safety scan and analytics.
Practices: a plugin bundle combines MCP servers and skills in a GitHub repo; "In Claude Code, plugins can also include LSPs, commands, hooks, and agents." ("Submit and track plugins in the directory submission portal")
Tools and files named: Claude directory, MCP 2.0 (spec dated 2026-07-28, "stateless core"), MCP Apps, Enterprise Managed Auth.
Relevance: low. Confirms the plugin as the packaging unit if the template is ever distributed.

### Building agents: When to fold subagents into your main agent loop (Anthropic Applied AI; `meta.json` author "Diane Sarkis"; 2026-10-22)
File: refs/articles/claude.com/resources-articles-building-agents-when-to-fold-subagents-into-your-main-agent-l/article.md   URL: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
Thesis: For agents built on the Claude Platform, a single agent loop with skills (progressively disclosed context) and tool search (progressively disclosed tools) frequently beats a router/planner/specialist-subagent design on quality, cost and latency. Subagents are kept only where a measured condition holds. This is the newest architecture statement in the batch.
Practices:
- Keep a subagent only when one of three conditions holds: a single loop "hits measurable performance degradation from context bloat"; tasks need parallel fresh context windows "that can be discarded once the task is done"; or the agent "struggles to select appropriate tools or there are conflicting instructions in the system prompt." (intro)
- Why fold: "An agent that has seen the result of each earlier step can connect them", giving better output than "a set of summaries handed back by subagents." ("Using an agent loop with progressive disclosure")
- If you do go multi-agent, start with the simplest pattern and split by context, not problem type: "give each subagent a piece of work that needs little from the rest of the system and have it hand back a compact result". Good candidates: independent research paths, components with clean interfaces, black-box verification. (same section)
- Split by problem type and agents play a "telephone game", "with each handoff degrading fidelity." (same section)
- Target single-loop design: one model and one context window, "with limits (turn and cost budgets, write gates) set in the harness"; the model writes its plan on the first turn and revises it; "A goal or verifier check can optionally run after the answer." ("How to fold subagents into the main agent loop")
- Where things move: "Ordering and domain procedure move into skills"; "Hard limits (validation, approval gates)" and mid-conversation lookups move into tools; code still loads anything "cheap and almost always relevant". (same section)
- Evals first: "Even a set of 10 golden examples is enough to start." Fold one subagent at a time, compare, and look at "which tasks flipped", not only the score; run each task more than once, since one regression "only showed up in one run out of two." ("Task-completion evals", "Folding subagents into the main agent via skills and tools")
- Subagent-as-tool is the intermediate step; a full handoff only "when it needs to talk to the user directly." Remaining costs: "Each call still hands back a lossy summary" and "Every call is a nested model loop that adds latency". ("Subagents called as tools")
- Tools: group by user intent, not one per API, "because once you exceed 30-50 tool definitions in the system prompt, tool choice tends to degrade." Use tool search with deferred loading; preconditions live inside tools and return a readable instruction or refusal. ("MCP tools")
- Skills hold "the steps, rules, and judgment calls a specialist subagent's prompt used to hold." Knowledge bases sit behind a lookup tool or as reference files in a skill; avoid code that retrieves and pastes context into prompts. ("Skills", "Knowledge bases")
- Library maintenance: `/skill-creator` to author and "audit existing ones to trim, deduplicate, and restructure"; `/skill-doctor` to "see what each skill in your library costs and how often it’s actually used, and delete dead weight." ("Skills")
- `/claude-api prompt-audit` "can flag instructions written for older models in your prompts, skills, and tool descriptions and propose fixes as a diff." Others: `/claude-api build-eval`, `/claude-api hillclimb`, `/claude-api cost-optimize`. ("Tools to accelerate this work")
Evidence and numbers: one customer saw "a roughly 2x faster runtime" with a single loop; Anthropic "reduced Claude Code’s system prompt for more advanced models by over 80%"; tool choice degrades past 30-50 definitions; a dozen specialist subagents hurt one company's brand consistency and latency.
Tools and files named: `anthropics/single-agent-loop-kit`, tool search, task budgets, `/skill-creator`, `/skill-doctor`, `/claude-api build-eval|prompt-audit|hillclimb|cost-optimize`.
Caveats, and explicit statements that older advice no longer applies: "starting with Opus 4.5, models became capable of managing far more in a single loop than most teams expected"; recent models "narrate their progress and check their work as they go, which makes some harness elements redundant"; proposed structures were often "doing work the model no longer needed done for it"; "You cannot turn off thinking on Opus 5.5, and Fable 5.1". The article is about enterprise agents on the Claude Platform, not Claude Code project setups; applying it to Claude Code subagents is an inference. Guidance is framed as provisional: "measure, change one thing at a time, and keep what holds up."
Relevance: high. Sets the default: skills and tools first, subagents only for the three stated conditions.

### Building agents with Skills: Equipping agents for specialized work (Anthropic; acknowledgments Barry Zhang, Mahesh Murag, Keith Lazuka, Ryan Whitehead; 2026-01-22)
File: refs/articles/claude.com/resources-articles-building-agents-with-skills-equipping-agents-for-specialized/article.md   URL: https://claude.com/resources/articles/building-agents-with-skills-equipping-agents-for-specialized-work
Thesis: Anthropic "stopped building specialized agents and started building skills instead": one general agent with bash and a filesystem, MCP for connectivity, and skills for domain expertise.
Practices:
- Three-tier progressive disclosure with token figures: "metadata uses \~50 tokens, full SKILL.md files \~500 tokens, and reference files 2,000+ tokens and only when specifically needed." ("Progressive disclosure")
- Save repeated scripts into the skill: "we kept seeing Claude write the same script ... So we asked Claude to save it as a tool for itself"; the skill's doc then just says to use `./apply_template.py`. ("Skills can include scripts as tools")
- Code versus tool definitions: code "is self-documenting, modifiable, and doesn't need to be in context at all times." (same section)
- Layering: "the loop reasons, the runtime executes, MCP connects, and skills guide." ("The complete architecture")
Evidence and numbers: skill sizes seen in practice: about 100 lines (simple), about 800 (intermediate), 2,500+ (complex); first skill "in under 30 minutes" with skill-creator.
Tools and files named: `SKILL.md`, `references/`, skill-creator, `anthropics/skills`, frontend-design plugin, agentskills.io (open standard).
Caveats: The "\~500 tokens" SKILL.md figure is far below the "under 5,000 words" limit in the skills guide (2026-01-26); treat it as illustrative. Promotional sections on verticals.
Relevance: medium-high. States the skills-over-specialist-agents position and the script-in-skill pattern.

### Building agents with the Claude Agent SDK (Thariq Shihipar et al., Anthropic, 2025-09-29)
File: refs/articles/claude.com/resources-articles-building-agents-with-the-claude-agent-sdk/article.md   URL: https://claude.com/resources/articles/building-agents-with-the-claude-agent-sdk
Thesis: Give the agent a computer and design around the loop "gather context -> take action -> verify work -> repeat". Verification needs concrete feedback mechanisms.
Practices:
- Folder structure is context engineering: "the folder and file structure of an agent becomes a form of context engineering." ("Agentic search and the file system")
- Search: "we suggest starting with agentic search, and only adding semantic search if you need faster results or more variations." ("Semantic search")
- Subagents for two reasons: parallelisation and context isolation; they "only send relevant information back to the orchestrator". ("Subagents")
- Verification ranked: rules first: "The best form of feedback is providing clearly defined rules for an output, then explaining which rules failed and why." Prefer TypeScript plus lint over plain JavaScript for the extra feedback layers. ("Defining rules")
- Visual feedback via screenshots, automated with the Playwright MCP server, at different viewport sizes. ("Visual feedback")
- LLM-as-judge is last resort: "This is generally not a very robust method, and can have heavy latency tradeoffs". ("LLM as a judge")
- Improving an agent: read failures and ask whether it has the right tools; if it fails repeatedly, "add a formal rule in your tool calls to identify and fix the failure". ("Testing and improving your agent")
Evidence and numbers: none.
Tools and files named: Claude Agent SDK (renamed from Claude Code SDK), `/compact`, Playwright MCP, `grep`, `tail`.
Caveats: Oldest architecture post in the batch (2025-09). Its subagent enthusiasm is tempered by the 2026-10-22 fold-in article, to which the saved page now links. The LLM-judge caution conflicts in tone with later posts: the loops article (2026-06-30) recommends "a second agent for code reviews" and `/goal` relies on an evaluator model; the workflow-patterns post (2026-03-05) keeps the caution by preferring deterministic tools where they exist.
Relevance: medium. The ranking (deterministic rules, then visual feedback, then an LLM judge) is the durable part.

### When to use multi-agent systems (and when not to) (Cara Phillips et al., Anthropic, 2026-01-23)
File: refs/articles/claude.com/resources-articles-building-multi-agent-systems-when-and-how-to-use-them/article.md   URL: https://claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them
Thesis: Start with a single agent. Multiple agents pay off in three situations only (context pollution, parallelisable work, specialisation), and work must be split by context boundaries, not by role.
Practices:
- The three situations: "when context pollution degrades performance, when tasks can run in parallel, and when specialization improves tool selection or task focus." Otherwise "the coordination costs typically exceed the benefits." (intro)
- Context isolation fits when a subtask produces "more than 1000 tokens" mostly irrelevant to the main task, has clear extraction criteria, or is a lookup needing filtering. ("Context protection")
- Parallel agents buy coverage, not speed: "The primary benefit of parallelization is thoroughness, not speed." ("Parallelization")
- Tool-count signals: "An agent with too many tools (often 20+) struggles to select the appropriate one"; try the Tool Search Tool first, which "can reduce token usage by up to 85%". ("Tool set specialization", "Outgrowing single-agent architectures")
- Context-centric decomposition: "an agent handling a feature should also handle its tests, because it already possesses the necessary context." ("Context-centric decomposition")
- Bad boundaries: "Sequential phases of the same work. Planning, implementation, and testing of the same feature share too much context"; tightly coupled components; shared state. Good boundaries: independent research paths, clean-interface components, black-box verification. (same section)
- Verification subagent is the one pattern that works across domains because it "can blackbox-test a system without needing the full history of how it was built." Give it the artifact, clear success criteria and tools. ("The verification subagent pattern")
- "The early victory problem": the verifier "runs one or two tests, observes them pass, and declares success." Mitigate with concrete criteria ("Run the full test suite and report all failures"), multiple scenarios, negative tests, and an explicit must-run instruction. ("The early victory problem")
- Example loop caps retries: `max_attempts: int = 3`, feeding the verifier's issues back into the requirements. ("Implementating a multi-agent system" [sic])
Evidence and numbers: "multi-agent implementations typically use 3-10x more tokens than single-agent approaches for equivalent tasks"; in a role-split experiment (planner, implementer, tester, reviewer) "the subagents spent more tokens on coordination than on actual work"; teams spent months on multi-agent designs "only to discover that improved prompting on a single agent achieved equivalent results."
Tools and files named: Tool Search Tool, compaction, `claude-sonnet-4-5` in code samples (dated).
Caveats: "These thresholds will shift as models improve." It also says capable orchestrators "(like Claude Opus 4.5) are increasingly able to evaluate subagent work directly without a separate verification step", which is in tension with later Claude Code advice to use a fresh-context reviewer. The article calls its capitalised "You MUST run the complete test suite before marking as passed" instruction "essential", whereas the 2025-11 prompt article presents a bare "NEVER ..." rule as less effective than one that explains why; the two are not reconciled. The 20+ tool threshold differs from 30-50 in the 2026-10-22 article.
Relevance: high. It rules out the planner/implementer/tester/reviewer role pipeline and keeps the black-box verifier.

### Building verification loops in Claude Code with skills (Delba de Oliveira, Claude Code team, 2026-07-22)
File: refs/articles/claude.com/resources-articles-building-verification-loops-in-claude-code-with-skills/article.md   URL: https://claude.com/resources/articles/building-verification-loops-in-claude-code-with-skills
Thesis: Whatever Claude cannot infer from type checkers, linters, tests and runtime errors becomes a manual check; write each recurring manual check down as a skill and choose where it runs (standalone, embedded, chained, on every PR).
Practices:
- Definition: "a verification loop is an iterative process where Claude checks and attempts to fix the work." (intro)
- Built-ins to try first: the `/verify` skill ("builds, runs, and observes the changes in your application"), the toolchain, Code Review (research preview), GitHub Actions invoking a verification skill, spec validation against a markdown spec, rubrics in Managed Agents. ("Built-in verification loops")
- CLAUDE.md: "list your exact build and test commands in CLAUDE.md so Claude doesn't have to infer them." (same section)
- Trigger for writing one: "you find yourself making the same small corrections every time Claude implements a new feature". Write it "in plain English, the way you'd hand it to a new teammate on day one." ("Writing verification loops")
- Deterministic project rules qualify: "Reject any migration that drops a column without a backfill step" is given as a rule "no generic linter will catch". (same section, Pro tip)
- Create via the skill-creator plugin with an interview: `/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.` Or hand-write `.claude/skills/<name>/SKILL.md`. ("Make it a skill")
- Minimal verification skill shape (the `verify-log-hygiene` example): frontmatter `name`, a `description` saying what it checks and "Use when the diff touches error handling or logging", `allowed-tools: [Read, Edit, Grep]`; body: read the diff's relevant paths, state the pass condition, "Report each violation with file:line, then fix it". (same section)
- Standalone: invoked deliberately for cross-cutting checks that do not apply every time (pre-commit security scan, pre-PR accessibility audit, licence headers). "The signal that you've outgrown standalone is when you're running it after every change." ("Standalone")
- Embedded: append the check to the producing skill's body, e.g. "After creating the component file, run eslint on it and address any errors before reporting completion." Test by invoking on a fresh task. Works only on skills you can edit; plugin-managed and built-in skills "are off-limits for this pattern; for those, chain instead." ("Embedded")
- Chained: a wrapper skill runs one skill then another, e.g. `safe-refactor`: "Run /simplify on the current diff first. When /simplify finishes, invoke /verify-no-public-api-changes." ("Chained")
- The Claude Code team's own chain: "/code-review hunts for bugs, /simplify cleans up the diff, a /verify skill confirms end-to-end behavior", and "a custom /design skill checks against guidelines in a DESIGN.md file if the change touched UI." (same section)
- Chaining "trades flexibility for automation"; skip it when you sometimes want one step alone. (same section)
- PR-wide gates come last: "Hold off on PR-wide gates while the chain is still in flux". ("On every PR")
- Six-step procedure: pick the most frequent manual follow-up this week; try built-in `/verify`; write the procedure in plain English; give it to skill-creator or drop the file in `.claude/skills/`; invoke on a new task and confirm the check ran; then experiment with chaining. (closing list)
Evidence and numbers: none measured.
Tools and files named: `/verify`, `/code-review`, `/simplify`, `/skill-creator`, `.claude/skills/<name>/SKILL.md`, `allowed-tools`, `DESIGN.md`, GitHub Actions, `@claude` PR comments, Code Review, rubrics in Claude Managed Agents.
Caveats: "Chained verification loops can increase token spend, so it's best to test these loops before deploying them broadly." No stop condition or retry cap is specified for the fix loop (contrast the `max_attempts = 3` example in the multi-agent article and the loops article's "explicit turn caps").
Relevance: high. This is the template for a `verify-*` skill family and for a chained finish (review, simplify, verify, design check).

### Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp (Anthropic, 2026-04-29)
File: refs/articles/claude.com/resources-articles-claude-api-skill/article.md   URL: https://claude.com/resources/articles/claude-api-skill
Thesis: The open-source `claude-api` skill carries current Claude API knowledge (model names, parameters, caching rules) and is bundled into other coding tools.
Practices: `/claude-api migrate` walks through "updating model names, prompts, and effort settings for a new model"; `/claude-api managed-agents-onboard` sets up Managed Agents. ("Building with the Claude API skill")
Tools and files named: `anthropics/skills/skills/claude-api`, `/claude-api migrate`, `/claude-api managed-agents-onboard`.
Relevance: low-medium. Inference: it is Anthropic's own example of a skill used to correct stale training knowledge about a fast-moving API, the same job a project skill does for new library versions.

### Redesigning Claude Code on desktop for parallel agents (Anthropic, 2026-04-14)
File: refs/articles/claude.com/resources-articles-claude-code-desktop-redesign/article.md   URL: https://claude.com/resources/articles/claude-code-desktop-redesign
Thesis: The desktop app was rebuilt around running several sessions at once with the user "in the orchestrator seat".
Practices: side chats (Cmd/Ctrl + ;) "pull context from the main thread, but don’t add anything back to the thread"; sessions archive when their PR merges or closes; a usage button shows context window and session usage. ("Run sessions in parallel", "Customize for how you work")
Tools and files named: desktop sidebar, side chat, view modes Verbose/Normal/Summary, CLI plugin parity, SSH sessions.
Relevance: low. UI, not configuration; side chats are a context-hygiene feature.

### Customize Claude Code with mods in TypeScript (Anthropic, 2026-10-01)
File: refs/articles/claude.com/resources-articles-claude-code-mods/article.md   URL: https://claude.com/resources/articles/claude-code-mods
Thesis: Mods are TypeScript functions, shipped in plugins, that run before, after, instead of or around Claude Code events, and can do what hooks cannot.
Practices:
- Boundary with hooks: "hooks can't rewrite events, draw new UI, or replace features. Mods can." ("Why we built mods")
- A mod can "Block, rewrite, or retry a tool call", approve or deny a permission request, and "Redact secrets from tool output before Claude reads it." ("How mods work")
- Load order matters: "The first mod to load sees the event first and the result last." (same section)
- Some built-ins are now mods, e.g. `/diff`, which can be turned off in `/plugin`. ("Swap built-in features for your own")
- Example team use: "a mod can require confirmation before any command touches production config." ("Mods for teams and enterprises")
Tools and files named: mods, plugins, `/plugin`, `sec-default` built-in mod (managed settings and Team/Enterprise), `/diff`.
Caveats: "They aren’t sandboxed, and you should only install mods from sources you trust". Released five weeks before this note; the steering article (2026-06) predates mods and does not place them in its decision table. `sec-default` only loads first on Team/Enterprise or managed machines, so a solo Pro/Max user gets no such default restriction (inference from "Mods for teams and enterprises").
Relevance: medium. A newer extension point than hooks for rewriting or redacting; hooks remain the documented deterministic layer.

### Claude Code on the web (Anthropic, 2025-10-20; update note 2026-09-23)
File: refs/articles/claude.com/resources-articles-claude-code-on-the-web/article.md   URL: https://claude.com/resources/articles/claude-code-on-the-web
Thesis: Cloud sessions (the feature's current name per the update note) run tasks in isolated sandboxes on Anthropic infrastructure, in parallel, and open PRs.
Practices: best for "Bugfixes and routine, well-defined tasks" and "Backend changes, where Claude Code can use test-driven development to verify changes"; custom network configuration chooses reachable domains (e.g. to allow npm). ("Flexible for every workflow", "Security-first cloud execution")
Caveats: "Cloud-based sessions share rate limits with all other Claude Code usage."
Relevance: low-medium. Where routines and unattended tasks run; no project configuration detail.

### Customize Claude Code with plugins (Anthropic, 2025-10-09)
File: refs/articles/claude.com/resources-articles-claude-code-plugins/article.md   URL: https://claude.com/resources/articles/claude-code-plugins
Thesis: Plugins package slash commands, subagents, MCP servers and hooks for one-command install, and are "our standard way to bundle and share Claude Code customizations".
Practices: disable plugins you are not using "to reduce system prompt context and complexity"; a marketplace is a git repo with `.claude-plugin/marketplace.json`; add with `/plugin marketplace add user-or-org/repo-name`. ("Share your Claude Code setup with plugins", "Plugin marketplaces")
Tools and files named: `/plugin`, `.claude-plugin/marketplace.json`, `anthropics/claude-code` marketplace, `feature-dev` plugin.
Caveats: 2025-10 list omits skills, LSPs and mods, which later posts (2026-09-25, 2026-10-01) add.
Relevance: low-medium. Packaging only.

### Memory for Claude Managed Agents: agents that learn across sessions (Anthropic, 2026-04-23)
File: refs/articles/claude.com/resources-articles-claude-managed-agents-memory/article.md   URL: https://claude.com/resources/articles/claude-managed-agents-memory
Thesis: Managed Agents memory is a filesystem mount with scopes, audit log and rollback; Anthropic found agents use memory best "when it builds on the tools they already use".
Evidence and numbers: customer claims: Rakuten "97% fewer first-pass errors at 27% lower cost and 34% lower latency"; Wisedocs verification 30% faster.
Relevance: low for Claude Code setup. Supports file-based memory as the design choice; the product is API-side.

### Claude Code effort level and model selection (Lydia Hallie, Claude Code team, 2026-07-07)
File: refs/articles/claude.com/resources-articles-claude-model-and-effort-level-in-claude-code/article.md   URL: https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code
Thesis: Model picks which frozen weights (capability and per-token price); effort picks how much work Claude does per turn (thinking, files read, verification, how far before checking in). Leave both at defaults and change one only after diagnosing whether Claude did not know enough or did not try hard enough.
Practices:
- Effort is more than thinking: it controls "the number of files read, tools used, and how many steps it takes before it checks back in with you." (Key takeaways)
- At low effort Claude "would rather ask you for more context than spend tokens figuring something out on its own." ("Claude Code effort level and model selection")
- Default guidance: "for most tasks you should use the model’s default effort level". Treat effort "more as a general preference than a task-by-task decision." ("Picking an effort level")
- First check context, not knobs: "the fix is often upstream, in your context, your CLAUDE.md, or how the task is scoped." ("What to change when Claude gets it wrong")
- Diagnostic: "did it not *try* hard enough, or did it not *know* enough?" Bigger model for subtle bugs, unfamiliar domains, architecture decisions, or when it is "confidently wrong no matter how much context you give it". Higher effort if it erred "by skipping a file, not running the tests, or not double-checking its work." (same section)
- Smaller models need more explicit direction: "specific instructions directing execution are a better recipe for success on the smaller models." ("Model: The problem was too hard")
- Drop down when "the work has been routine for a while". (same section)
- Docs in context steer but do not teach: "If a library didn't exist when the model was trained, it isn't in the weights." ("How model selection works")
- Limits: effort "shapes token consumption but doesn't limit it"; the only hard cap is `max_tokens`; task budgets and "keep it brief" are softer guidance the model is trained to follow. ("Effort, model, and token consumption")
Evidence and numbers: Opus 4.8 at default effort gives "better results for about the same number of tokens" as Opus 4.7 at its default; Fable "finished jobs Opus and Sonnet can't reach at any effort level" in Anthropic's testing. No figures.
Tools and files named: effort level, model setting, `max_tokens`, task budgets, CLAUDE.md.
Caveats: Disagrees with the 2026-04-16 Opus 4.7 post, which suggested toggling effort "during the same task"; this later article says not to tune task by task. It does not list per-model default levels.
Relevance: high. Gives the rule for a setup's model/effort defaults and a troubleshooting order: context, then model or effort.

### Claude models explained: choosing the best model for your use case (Michael Segner, Anthropic, 2026-07-24)
File: refs/articles/claude.com/resources-articles-claude-models-explained-choosing-the-best-model-for-your-use/article.md   URL: https://claude.com/resources/articles/claude-models-explained-choosing-the-best-model-for-your-use-case
Thesis: Start with the most intelligent generally available model and tune with effort; move down a class only for latency- or cost-sensitive work that evals show a smaller model handles.
Practices:
- Default: "start with the most intelligent generally available model and use effort level to dial in performance and cost." ("Our advice: start smart")
- Why: "Starting with a smaller model can also make it harder to distinguish between model failures and setup failures." (same section)
- Opus versus Fable: "if your evals or internal testing show Opus struggling on some tasks, then Fable is the answer"; if Opus clears the bar, its speed and price may win. ("Opus")
- Sonnet suits "high-volume sub-agents in multi-agent orchestration setups"; Haiku is for "high-frequency workloads where latency and cost matter." ("Sonnet", "Haiku")
- Model classes do not specialise by domain; they differ in "*how hard a problem* they can reliably carry". ("How to choose which Claude model is best for your workload")
Evidence and numbers: "on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5’s score at 63% of the price".
Tools and files named: Mythos (restricted, Project Glasswing) and Fable (same underlying model with safeguards), Opus, Sonnet, Haiku; advisor strategy.
Caveats: The article admits the opposite approach (start cheap, move up) is also documented. Benchmarks saturate for Opus and Fable; use your own evals.
Relevance: medium-high. Sets the default: start with the strongest generally available model and lower effort before lowering the model.

### Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind. (Michael Segner, Anthropic, 2026-09-24)
File: refs/articles/claude.com/resources-articles-claude-opus-5-5-built-for-coding-sessions-that-use-more-conte/article.md   URL: https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
Thesis: Sessions now run longer with far more context per request, so cost is dominated by cached reads; Opus 5.5 pricing and recent Claude Code changes target that, and the user's job is to protect the cache and prune context.
Practices:
- "Run /usage in Claude Code to see how much of your usage is cached reads." Then: "Pick your model at the start of a session rather than switching midway", "Compact before you step away rather than after", and on API keys set the one-hour cache lifetime. ("Protect your cached reads")
- Context discipline has a price tag: "Claude reads more tokens. You need to make sure all the context you are providing is necessary". ("Claude Code trends", link text)
- Harness changes: for Opus 5.5 and Fable 5.1 "you can now change effort levels during your sessions without resetting your cache"; "forked subagents start from the parent's cache instead of paying for the same context again." ("Claude Code is better at using the cache")
Evidence and numbers (Claude Code aggregate, March to September 2026): "Claude works 3.3x longer on each prompt with more than 40% more model calls per prompt. There are 68% fewer interruptions"; developers are "about twice as likely to have a tool server connected or use a skill"; "Context per request has grown 2.6x"; input:output ratio from 189:1 to 324:1; input missing the cache "decreased by more than 50%". Opus 5.5: about 40% cheaper to run than Opus 5, input/output price down 20%, cached-read price down 60%, output more than 30% faster.
Tools and files named: `/usage`, one-hour cache TTL, forked subagents, Opus 5.5, Fable 5.1.
Caveats: Cost claims are for per-token billing. A quoted caveat: "No single number holds for every codebase, so measure it." Marketing comparison to competitors is unsourced.
Relevance: high for context/session rules (pick model at session start, compact before stepping away, keep always-loaded context small).

### Common workflow patterns for AI agents (Anthropic, 2026-03-05)
File: refs/articles/claude.com/resources-articles-common-workflow-patterns-for-ai-agents-and-when-to-use-them/article.md   URL: https://claude.com/resources/articles/common-workflow-patterns-for-ai-agents-and-when-to-use-them
Thesis: Three workflow patterns (sequential, parallel, evaluator-optimizer) cover most production cases; try a single agent first and add a pattern only when you can measure the gain.
Practices:
- Order of escalation: "Default to sequential." Then "Move to parallel when latency is the bottleneck and tasks are independent and add evaluator-optimizer loops only when you can measure the quality improvement." ("Agent workflow patterns")
- Sequential pro tip: "First try your pipeline as a single agent, where the steps are just part of the prompt." ("Sequential workflows")
- Parallel pro tip: "Design your aggregation strategy before implementing parallel agents." Avoid when agents "need cumulative context or must build on each other's work." ("Parallel workflows")
- Evaluator-optimizer needs "clear, measurable quality criteria that an AI evaluator can apply consistently". Prefer deterministic tools: "If deterministic tools exist (like linters for code style), use those instead." ("Evaluator-optimizer workflows")
- Stop conditions: "Define maximum iteration counts and specific quality thresholds." Otherwise "the evaluator keeps finding minor issues and the generator keeps tweaking, but quality plateaus". (same section, Pro tip)
- Always keep a baseline: "Set a baseline with a single agent so you can tell whether the workflow actually helps." ("Choosing the right workflow pattern")
Evidence and numbers: none; table of tradeoffs (sequential adds latency, parallel costs more and needs aggregation, evaluator-optimizer "Multiplies token usage").
Tools and files named: none.
Caveats: API-builder framing. Its suggestion that focusing "each agent on a specific subtask" improves accuracy sits uneasily with the 2026-01-23 warning against splitting sequential phases of the same work; the reconciliation offered here is to try a single agent first.
Relevance: medium. Supplies the stop-condition rule for review/fix loops and the rule to use linters before LLM evaluators.

### A complete guide to building skills for Claude (Anthropic, 2026-01-29)
File: refs/articles/claude.com/resources-articles-complete-guide-to-building-skills-for-claude/article.md   URL: https://claude.com/resources/articles/complete-guide-to-building-skills-for-claude
Thesis: Announcement page for the skills guide (PDF), whose chapters are the `resources-guides-...` entries at the end of this file.
Practices: "expect about 15-30 minutes to build and test your first working skill using the skill-creator."
Relevance: low (pointer only).

### Managing context on the Claude Developer Platform (Anthropic, 2025-09-29)
File: refs/articles/claude.com/resources-articles-context-management/article.md   URL: https://claude.com/resources/articles/context-management
Thesis: API features for long-running agents: context editing clears stale tool calls and results near the limit; the memory tool stores information in files outside the window.
Practices: split of roles: "Context editing clears old file reads and test results while memory preserves debugging insights and architectural decisions". ("Building long-running agents")
Evidence and numbers: internal agentic-search eval: memory tool plus context editing "improved performance by 39% over baseline", context editing alone 29%; in a 100-turn web search eval, token consumption fell 84%.
Caveats: Sonnet 4.5 era, API-level, public beta at the time. Not Claude Code configuration.
Relevance: low. Evidence that pruning stale tool output and keeping durable notes in files both help.

### Extending Claude's capabilities with skills and MCP (Anthropic, 2025-12-19)
File: refs/articles/claude.com/resources-articles-extending-claude-capabilities-with-skills-mcp-servers/article.md   URL: https://claude.com/resources/articles/extending-claude-capabilities-with-skills-mcp-servers
Thesis: MCP gives access; skills give the procedure for using that access. Keep them separate so each can be reused.
Practices:
- Decision rule: "If you're explaining *how* to do something, that's a skill. If you need Claude to *access* something, that's MCP." ("What to use MCP servers for")
- Overlap rule: "MCP instructions cover how to use the server and its tools correctly." And "Skill instructions cover how to use them for a given process or in a multiserver workflow." ("Where skills and MCP may overlap")
- Watch for conflicts: if the server says JSON and the skill says markdown tables, "Claude has to guess which one is right." (same section)
- Skills fit multi-step workflows with tools, processes where consistency matters, domain expertise, and knowledge that "should survive when team members leave". MCP fits real-time data, actions in external systems, file operations, API integrations. ("What to use skills for", "What to use MCP servers for")
- Loading behaviour (table): skills "Loads on-demand, preserving context"; MCP "Definitions loaded upfront". ("Quick reference table")
Evidence and numbers: none.
Tools and files named: Agent Skills open standard (agentskills.io), Notion Meeting Intelligence skill, MCP tools/resources/prompts.
Caveats: "Definitions loaded upfront" is the 2025-12 state; the 2026-10-22 article recommends tool search with deferred loading, and the session-value article (2026-08-14) says to turn off unneeded servers with `/mcp`, so upfront MCP cost is less fixed than this table implies.
Relevance: medium. Clean skill-versus-MCP criterion.

### Loop engineering: Getting started with loops (Delba de Oliveira and Michael Segner, Claude Code team, 2026-06-30)
File: refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md   URL: https://claude.com/resources/articles/getting-started-with-loops
Thesis: A loop is an agent "repeating cycles of work until a stop condition is met". The Claude Code team distinguishes four types by trigger, stop condition and primitive, and advises the simplest one that fits.
Practices (the four loop types, fields as given in the article):
- Turn-based. Triggered by: a user prompt. Stop: "Claude judges it has completed the task or needs additional context." Best for: shorter tasks not part of a regular process. Usage managed by: "Write specific prompts and improve verification using skills to reduce the number of turns." ("Turn-based loops")
- Goal-based (`/goal`). Triggered by: a manual prompt in real time. Stop: "Goal achieved OR maximum number of turns reached." Best for: "Tasks that have verifiable exit criteria." Usage managed by: specific completion criteria and explicit turn caps, "stop after 5 tries." ("Goal-based loop (/goal)")
- Time-based (`/loop`, `/schedule`). Triggered by: a time interval. Stop: "You cancel it, or the work completes (the PR merges, the queue is empty)." Best for: recurring work or interfacing with external systems. Usage managed by: "Set longer intervals or react based on events rather than time." ("Time-based loop (/loop and /schedule)")
- Proactive. Triggered by: "An event or schedule, with no human in real time." Stop: each task exits when its goal is met; the routine runs until turned off. Best for: "Recurring streams of well-defined work: bug reports, issue triage, migrations, dependency upgrades". Usage managed by: "Routing routines to smaller, faster models and using the most capable model for judgment calls." ("Proactive loops")
- Summary table, "You hand off": turn-based, the check; goal-based, the stop condition; time-based, the trigger; proactive, the prompt. ("Getting started")
- How `/goal` works: "Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work" until the goal is met or the turn cap you set is reached. Deterministic criteria (tests passed, a score threshold) work best. Example: `/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.` ("Goal-based loop (/goal)")
- `/loop` example: `/loop 5m check my PR, address review comments, and fix failing CI`. It "runs on your computer, so if you turn it off, it stops"; move it to the cloud as a routine with `/schedule`. ("Time-based loop")
- Composition for proactive work: `/schedule` (routine) + `/goal` (done) + skills (how to verify) + dynamic workflows (orchestrate triage, fix, review) + auto mode (no permission stops). ("Proactive loops")
- Verification skill in the turn-based loop: the `verify-frontend-change` example says never report a UI change complete from the edit alone; start the dev server, interact, screenshot before/after, check console for "zero new errors or warnings", run a performance trace via the Chrome Devtools MCP; "If any step fails, fix the issue and rerun from step 1". ("Turn-based loops")
- Make checks quantitative: "The more quantitative the checks are, the easier it is for Claude to self-verify." (same section)
- Code quality in loops: keep the codebase clean (Claude follows existing patterns); give Claude a way to verify; make docs reachable; "Use a second agent for code reviews: A reviewer with fresh context is less biased and not influenced by the main agent’s reasoning." ("Maintaining code quality")
- Systemic fix rule: "don’t stop at fixing the individual issue, try to encode it to improve the system for all future iterations." (same section)
- Token management: right primitive and model; clear success and stop criteria; "Pilot before a large run: Dynamic workflows can spawn hundreds of agents"; "Running a script is cheaper than reasoning through the steps"; match routine interval to how often the watched thing changes; review usage. ("Managing token usage")
- Usage inspection: "`/usage` command breaks down recent usage by skills, subagents, and MCPs", `/goal` with no arguments shows turns and tokens so far, `/workflows` shows each agent's token usage and lets you stop one. (same section)
Evidence and numbers: none.
Tools and files named: `/goal`, `/loop`, `/schedule`, routines, dynamic workflows (research preview), auto mode, `/code-review`, Code Review for GitHub, `/usage`, `/workflows`, `SKILL.md`, Chrome Devtools MCP, parallel worktrees.
Caveats: "Not all tasks require complex loops; start with the simplest solution". `/schedule` and dynamic workflows are labelled research preview in this article. The example verification skill opens with "Never report...", an absolute phrasing other Anthropic articles advise softening with reasons.
Relevance: high. The canonical taxonomy for (f).

### Agent harness design: 3 patterns for harnessing Claude's intelligence (Lance Martin, Claude Platform team, 2026-04-02)
File: refs/articles/claude.com/resources-articles-harnessing-claudes-intelligence/article.md   URL: https://claude.com/resources/articles/harnessing-claudes-intelligence
Thesis: Harnesses encode assumptions about what Claude cannot do, and those go stale. Use tools Claude already knows (bash, text editor), keep asking "what can I stop doing?", and put structure only where UX, cost or security need a boundary.
Practices:
- "every token added depletes Claude’s attention budget and it is wasteful to pre-load context with rarely used instructions." Skills are the remedy: only frontmatter is preloaded. ("Let Claude manage its own context")
- Let code filter tool output before it reaches context; "Only the output of code execution reaches Claude’s context window." ("Let Claude orchestrate its own actions")
- Cache rules: "Static first, dynamic last"; append a `<system-reminder>` in messages instead of editing the prompt; "Avoid switching models during a session. Caches are model-specific; switching breaks them. If you need a cheaper model, use a subagent."; adding or removing a tool invalidates the cached prefix, so use tool search. ("Design context to maximize cache hits", table)
- Promote an action to a dedicated tool when it needs a security boundary, UI or audit: "Reversibility is often a good criterion, and hard-to-reverse actions such as external API calls can be gated by user confirmation." ("Use declarative tools for UX, observability, or security boundaries")
- Auto mode "should only be used for tasks where users trust the general direction." (same section)
Evidence and numbers: Claude 3.5 Sonnet 49% on SWE-bench Verified with only bash and a text editor; BrowseComp with self-filtered tool output, Opus 4.6 45.3% to 61.6%; subagents +2.8% on BrowseComp; compaction: Sonnet 4.5 flat at 43%, Opus 4.5 68%, Opus 4.6 84%; memory folder lifted Sonnet 4.5 on BrowseComp-Plus from 60.4% to 67.2%; cached tokens "are 10% the cost" of base input.
Tools and files named: bash tool, text editor tool, code execution, skills, context editing, compaction, memory folder, tool search, auto-caching, prompt-cache breakpoints.
Caveats, and explicit statements that older advice no longer applies: Sonnet 4.5 "would wrap up prematurely as it sensed the context limit approaching"; resets were added for this "context anxiety", and "With Opus 4.5, the behavior was gone. The context resets we built to compensate had become dead weight". "Assumptions about what Claude can’t do need to be re-tested with each step change in its capability." API/harness-builder framing.
Relevance: medium-high. The pruning principle and cache rules transfer directly to a project setup.

### How Claude Code works in large codebases: Best practices and where to start (Anthropic Applied AI, 2026-05-14)
File: refs/articles/claude.com/resources-articles-how-claude-code-works-in-large-codebases-best-practices-and-w/article.md   URL: https://claude.com/resources/articles/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
Thesis: Claude Code navigates by agentic search on the live codebase, so its results depend on how well the repo is set up. The harness has five extension points built in order (CLAUDE.md, hooks, skills, plugins, MCP), plus LSP and subagents, and it needs review as models change.
Practices:
- "The harness matters as much as the model": the ecosystem around the model "determines how Claude Code performs more than the model alone." ("The harness matters as much as the model")
- CLAUDE.md first; because it loads every session, "keeping them focused on what applies broadly will prevent them from becoming a drag on performance." (same section)
- Hooks' "more valuable use is continuous improvement": "A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh." Also "A start hook can load team-specific context dynamically". For lint and format, hooks "produce more consistent results than relying on Claude to remember an instruction." (same section)
- Skills hold on-demand expertise and "can also be scoped to specific paths so they only activate in the relevant part of the codebase." (same section)
- Subagents "split exploration from editing": a read-only subagent maps a subsystem and writes findings to a file, then the main agent edits. (same section)
- Component table, "Common confusion" column: CLAUDE.md, "Using it for reusable expertise that belongs in a skill"; hooks, "Using prompts for things that should run automatically"; skills, "Loading everything into CLAUDE.md instead"; MCP, "Building MCP connections before the basics are working"; subagents, "Running exploration and editing in the same session"; LSP, "Assuming that it's automatic". (table)
- Root CLAUDE.md content: "The root file should be pointers and critical gotchas only; everything else drifts into noise." Subdirectory files carry local conventions and load additively. ("Making the codebase navigable at scale")
- Start sessions in the relevant subdirectory; Claude "automatically walks up the directory tree and loads every CLAUDE.md file it finds along the way". (same section)
- Scope test and lint commands per subdirectory: running the full suite for a one-service change "causes timeouts and wastes context on irrelevant output." (same section)
- Exclude generated files, build artefacts and third-party code via ignore files and committed `permissions.deny` rules in `.claude/settings.json`; individuals can override in local settings. (same section)
- Codebase map: "a lightweight markdown file at the repo root listing each top-level folder with a one-line description". (same section)
- LSP: install a code intelligence plugin and the language server so Claude "searches by symbol, not by string". (same section)
- Maintenance cadence: "Teams should expect to do a meaningful configuration review every three to six months", and after major model releases when performance plateaus. ("Actively maintaining CLAUDE.md files as model intelligence evolves")
- Ownership: at minimum a DRI for settings, permissions policy, marketplace and CLAUDE.md conventions. ("Assigning ownership for Claude Code management and adoption")
Evidence and numbers: none measured; patterns "observed" across enterprise deployments.
Tools and files named: `CLAUDE.md` (root and subdirectory), `.claude/settings.json` `permissions.deny`, ignore files, stop and start hooks, path-scoped skills, plugins and managed marketplaces, LSP code intelligence plugins, MCP servers, read-only subagents, native Perforce mode.
Caveats, and explicit statements that older advice no longer applies: "instructions written for your current model can work against a future one"; a rule to "break every refactor into single-file changes" would now prevent coordinated cross-file edits; "Skills and hooks built to compensate for specific model limitations ... become overhead once those limitations no longer exist." Written for enterprises; hierarchical CLAUDE.md breaks down at extreme sizes. The term "rules" (`.claude/rules/`) does not appear here; path scoping is described for skills and subdirectory CLAUDE.md files.
Relevance: high. Build order, root-file content rule, review cadence and the self-improving stop hook all apply to a solo repo.

### Claude Code power user customization: How to configure hooks (Anthropic, 2025-12-11)
File: refs/articles/claude.com/resources-articles-how-to-configure-hooks/article.md   URL: https://claude.com/resources/articles/how-to-configure-hooks
Thesis: Hooks are shell commands (or prompts) bound to session events. They remove repeated manual steps, enforce project rules every time, and inject dynamic context. The article documents eight events as of 2025-12.
Practices:
- Three problem categories: "eliminate repetitive manual steps", "enforce project-specific rules automatically", "inject dynamic context without manual effort". ("Why use hooks in Claude Code?")
- The eight events and their listed uses (table "Hooks at a glance"): `PreToolUse` (block dangerous commands, validate file paths, auto-approve safe operations); `PermissionRequest` (auto-approve test commands, block access to sensitive files); `PostToolUse` (formatters, linters, log file changes); `PreCompact` (back up transcripts, preserve decisions); `SessionStart` (inject git status, TODO lists, environment context); `Stop` (verify completion, run tests, summaries); `SubagentStop` (validate subagent output); `UserPromptSubmit` (inject context, validate requests).
- `PreToolUse` "is the most commonly used hook"; a script can "approve it, block it, request user confirmation, or modify the parameters". Uses include "Blocking dangerous Bash commands like rm -rf or force pushes". ("PreToolUse")
- `PostToolUse` formatter example: matcher `"Write|Edit"`, command `prettier --write "$CLAUDE_TOOL_INPUT_FILE_PATH"`. ("PostToolUse")
- `SessionStart`: "Stdout automatically becomes context." Example command: `git status --short && echo '---' && cat TODO.md`. ("SessionStart")
- `Stop` can force continuation: the script "can return JSON with "continue": true to make Claude continue working"; a `"type": "prompt"` hook asks a model whether the task is complete. Uses: "Verifying that tests pass before considering a task complete". ("Stop")
- `PreCompact` matcher is `"auto"` or `"manual"`. ("PreCompact")
- Locations: project `.claude/settings.json` (shared), user `~/.claude/settings.json`, local `.claude/settings.local.json` (uncommitted). "Project-level settings take precedence over user-level settings." ("Configuration and file locations")
- Matchers apply only to `PreToolUse`, `PostToolUse`, `PermissionRequest`; "Matchers are case sensitive, so "bash" won't be matched to the Bash tool"; argument patterns like `"Bash(npm test*)"`; MCP pattern `"mcp__memory__.*"`. ("Matcher syntax")
- Input: JSON on stdin with `session_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`, plus `tool_name` and `tool_input` for tool hooks. ("What hooks receive")
- Output: "Exit code 0 means success"; "Exit code 2 means a blocking error: stderr becomes the error message and the action gets prevented." JSON fields: `decision`, `reason`, `continue`, `updatedInput`. ("How hooks respond")
- Execution: "Hooks have a 60-second default timeout, configurable per hook. When multiple hooks match an event, they run in parallel." Env vars: `CLAUDE_PROJECT_DIR`, `CLAUDE_CODE_REMOTE`, `CLAUDE_ENV_FILE`. ("Environment and execution")
- Security: hooks run "with your user permissions"; "direct edits to hook configuration files require review in the /hooks menu before taking effect." Script hygiene: validate stdin, quote shell variables, absolute script paths, avoid processing sensitive files. ("Security considerations")
- Debugging: every hook gets `transcript_path` (JSONL); add logging via a wrapper script. Start with one hook: "The PostToolUse formatter hook is a good first choice". ("Debugging and testing", "Building your own hooks")
Evidence and numbers: 8 events; 60-second default timeout.
Tools and files named: `.claude/settings.json`, `~/.claude/settings.json`, `.claude/settings.local.json`, `/hooks`, `jq`, hook types `command` and `prompt`.
Caveats: Dated 2025-12. Its auto-approval uses, meant to reduce prompt fatigue (`PermissionRequest`, `PreToolUse` approvals), predate auto mode (2026-03, default 2026-08), which now covers that need; the block/deny uses remain. The steering article (2026-06-18) lists five hook types ("command, HTTP, mcp\_tool, prompt, and agent") where this one shows two (`command`, `prompt`), so this article is not a complete reference for current hooks. One example description says a command hook has "Claude review" the write, which does not match the `"type": "command"` config shown; treat the prose as loose. The `UserPromptSubmit` "append sprint context to every request" pattern adds tokens to every turn, which later context-cost guidance would discourage (inference).
Relevance: high for mechanics (exit code 2, matchers, file locations); medium for which uses to adopt.

### How to create Skills for Claude: steps and examples (Anthropic, 2025-11-19)
File: refs/articles/claude.com/resources-articles-how-to-create-skills-key-steps-limitations-and-examples/article.md   URL: https://claude.com/resources/articles/how-to-create-skills-key-steps-limitations-and-examples
Thesis: A skill is a name, a description and instructions; only the name and description affect triggering, so the description is the most important part. Build skills from real repeated tasks and test triggering and function separately.
Practices:
- "the name and description are the only parts of the SKILL.md file that influence triggering". Name: lowercase with hyphens. ("2. Write the name", link markup removed)
- Description: "Write it from Claude's perspective, focusing on triggers, capabilities, and use cases", balancing "specific capabilities, clear triggers, relevant context, and boundaries." The strong example ends with a negative boundary: "Not for simple PDF viewing or basic conversions." ("3. Write the description field")
- Instructions: "overview, prerequisites, execution steps, examples, error handling, and limitations"; include concrete examples and what the skill cannot do. ("4. Write the main instructions")
- Test matrix: normal operations, edge cases, and "Out-of-scope requests" where "The skill should stay dormant". Triggering tests use both explicit requests and natural phrasing. ("4. Testing and validation" [second item numbered 4 in the source])
- When to build: "Have I done this task at least five times? Will I do it at least ten more times?" and "Don't write skills speculatively." ("Start with use cases")
- Put success criteria in the skill "so Claude can self-check." ("Define success criteria—and include it in the skill")
- Size: use a "menu" approach, where SKILL.md "should describe what's available and use relative paths to reference separate files for each." ("Appropriate file sizes")
- Granularity: "Aim for single-purpose skills." Too broad: "Content marketing helper." Too narrow: "Add meta descriptions." ("What's the right granularity for my descriptions?")
- Debugging: "If skills don't activate, broaden your description and add use cases. If results are inconsistent, add specificity to instructions and include validation steps." ("How do I debug skills?")
- Triggering is semantic, not keyword matching, and "Multiple skills can activate simultaneously". ("Skill triggering")
Evidence and numbers: none. The 5/10 repetition threshold is a rule of thumb.
Tools and files named: `SKILL.md`, skill-creator, `anthropics/skills` (docx, brand-guidelines, frontend-design examples), Skills API `/v1/skills`, beta header `skills-2025-10-02`.
Caveats: Older (2025-11) and visibly unedited: step numbers repeat, the "What makes it strong" line under frontend-design is pasted from a different skill, and one FAQ appears twice. It shows a project-root `skills/` directory for Claude Code, whereas the 2026-07 verification article uses `.claude/skills/`. The embedded docx skill relies on capitals ("MANDATORY - READ ENTIRE FILE", "NEVER set any range limits"), a style the 2026-01 guide and later posts move away from; the guide's troubleshooting section still lists "CRITICAL" headers as one fix for ignored instructions.
Relevance: medium-high. Description-writing rules and the three-way test matrix are still the basis of later guidance.

### Improving frontend design through Skills (Prithvi Rajasekaran, Justin Wei, Alexander Bricken, Anthropic Applied AI, 2025-11-12)
File: refs/articles/claude.com/resources-articles-improving-frontend-design-through-skills/article.md   URL: https://claude.com/resources/articles/improving-frontend-design-through-skills
Thesis: Unguided models converge on generic UI ("Inter fonts, purple gradients on white backgrounds"). A compact skill that names the convergent defaults and offers concrete alternatives fixes this without adding permanent context to unrelated tasks.
Practices:
- Why a skill and not the system prompt: otherwise "every request–debugging Python, analyzing data, writing emails–carries frontend design context." ("The steerability challenge")
- Altitude: avoid "low-altitude hardcoded logic like specifying exact hex codes and vague high-altitude guidance that assumes shared context." ("Prompting for better frontend output")
- Map aesthetics to code: "The more you can map aesthetic improvements to implementable frontend code, the better Claude can execute." Axes that work: typography, animations, background effects, themes. (same section)
- The general prompt is "\~400 token", opens by telling the model about its own tendency ("You tend to converge toward generic, "on distribution" outputs"), lists what to focus on and what to avoid, and ends with a guard against a new local optimum (Space Grotesk). ("A general-purpose prompt")
- Scripts in skills: web-artifacts-builder ships scripts to set up a React repo and bundle with Parcel; "by giving Claude access to scripts to execute boilerplate actions, Claude is able to minimize token usage while increasing reliability". ("Improving artifact quality in claude.ai with Skills")
- Method for any domain with generic output: "identify convergent defaults, provide concrete alternatives, structure guidance at the right altitude, and make it reusable through Skills." ("Optimizing Claude’s frontend design capabilities with Skills")
Evidence and numbers: about 400 tokens for the aesthetics prompt; before/after screenshots only (not saved in the text).
Tools and files named: frontend-design plugin (`anthropics/claude-code/plugins/frontend-design`), web-artifacts-builder skill, React, Tailwind CSS, shadcn/ui, Parcel, skill-creator.
Caveats: 2025-11, Claude 4.x era. The prompt uses "Never use: Inter, Roboto..." lists and "it is critical that you think outside the box!", phrasing that later Anthropic guidance on stronger models treats as heavier than needed (inference from the Opus 4.7 and prompt-audit statements). The typography example names Space Grotesk as a good choice while the general prompt names it as an overused one.
Relevance: medium-high for a Tailwind/shadcn developer: shows the shape and size of a design skill, and the method of naming the convergent default and giving alternatives.

### Improving skill-creator: Test, measure, and refine Agent Skills (Anthropic, 2026-03-03)
File: refs/articles/claude.com/resources-articles-improving-skill-creator-test-measure-and-refine-agent-skills/article.md   URL: https://claude.com/resources/articles/improving-skill-creator-test-measure-and-refine-agent-skills
Thesis: skill-creator gained evals, a benchmark mode, parallel clean-context eval agents, blind comparator agents and description tuning, so a skill can be tested, compared with no skill, and retired when the model no longer needs it.
Practices:
- Two skill types: "Capability uplift" (the model cannot do it, or not consistently) and "Encoded preference" (the model can do each piece; the skill sequences them your way). ("Two kinds of skills")
- They age differently: "Capability uplift skills may become less necessary as models improve. Evals tell you when that's happened." Encoded-preference skills are "more durable, but only as valuable as their fidelity to your actual workflow." (same section)
- An eval is test prompts (plus files), a description of what good looks like, and a pass/fail from skill-creator. ("Using evals to test and improve skills")
- Retirement signal: "If the base model starts passing your evals *without* the skill loaded", its techniques "may have been incorporated into the model's default behavior." (same section)
- Benchmark mode "tracks eval pass rate, elapsed time, and token usage"; run after model updates or skill edits. (same section)
- Evals run in independent agents, "each in a clean context", to avoid context bleed; comparator agents "judge outputs without knowing which is which" for skill A versus B or skill versus no skill. ("Faster, more consistent evaluation with multi-agent support")
- Description tuning: "too broad and you get false triggers, too narrow and it never fires"; skill-creator checks the description against sample prompts. ("Getting skills to trigger at the right time")
Evidence and numbers: description tuning "improved triggering on 5 out of 6 public skills"; one PDF-skill failure (non-fillable forms) isolated by evals.
Tools and files named: skill-creator (plugin `anthropics/claude-plugins-official/plugins/skill-creator`, repo `anthropics/skills/skills/skill-creator`), benchmark mode, comparator agents.
Caveats: Forward-looking claim, not a practice: "a natural-language description of *what* the skill should do may be enough" over time.
Relevance: high. The tested way to iterate skills and the criterion for deleting them.

### Introducing dynamic workflows (Anthropic, 2026-05-28; update line says now generally available)
File: refs/articles/claude.com/resources-articles-introducing-dynamic-workflows-in-claude-code/article.md   URL: https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code
Thesis: In a dynamic workflow Claude writes an orchestration script that runs "tens to hundreds of parallel subagents in a single session", with independent verification and adversarial review, for jobs too big for one agent pass.
Practices:
- Two ways to start: ask ("Create a workflow"), or switch on `ultracode` in the effort menu, which "sets the effort level to xhigh, while letting Claude decide automatically when to use a workflow". (intro)
- "For the best experience, turn on auto mode when using dynamic workflows." (intro)
- Fits: codebase-wide bug hunts and audits with "independent verification on every finding"; large migrations; "Critical work you need checked twice" via independent attempts and "adversarial agents working to break the result". ("Dynamic workflows in action")
- Mechanics: "Progress is saved as the run goes, so a job that's interrupted picks up where it left off"; coordination "happens outside the conversation". The run "keeps iterating until the answers converge". ("How it works")
- Cost guard: "The first time a workflow triggers, Claude Code shows what's about to run and asks you to confirm." Start "on a scoped task to get a feel for usage". ("How it works", intro note)
Evidence and numbers: Bun port from Zig to Rust: "99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge", with "two reviewers on each file" and a fix loop driving build and tests; stated as "not yet in production".
Tools and files named: dynamic workflows, `ultracode`, `/config` (Pro users enable there), managed settings to disable, auto mode.
Caveats: "Dynamic workflows can consume substantially more tokens than a typical Claude Code session". The stop condition is described only as convergence; no cap is documented in this post (the loops article adds "Pilot before a large run" and `/workflows` to stop agents).
Relevance: medium for a solo developer: reserve for migrations and audits; everyday tasks do not need it.

### Introducing routines in Claude Code (Anthropic, 2026-04-14)
File: refs/articles/claude.com/resources-articles-introducing-routines-in-claude-code/article.md   URL: https://claude.com/resources/articles/introducing-routines-in-claude-code
Thesis: A routine is a saved Claude Code automation ("a prompt, repo, and connectors") that runs in the cloud on a schedule, from an API call, or on a GitHub event.
Practices:
- Three triggers: scheduled (hourly, nightly, weekly; `/schedule` tasks "are now scheduled routines"), API (own endpoint and auth token; "POST a message, get back a session URL"), GitHub webhook (one session per matching PR, fed follow-up comments and CI failures). ("How it works")
- Example prompts: "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR."; docs drift scan weekly; deploy verification posting go/no-go; "Bespoke code review: on PR opened, run your team's own checklist". ("Scheduled routines", "What teams are building")
Evidence and numbers: daily limits: Pro 5 routines per day, Max 15, "and Team and Enterprise users can run up to 25 routines per day"; routines draw on the same subscription limits as interactive sessions.
Tools and files named: routines, `/schedule`, claude.ai/code, connectors, Claude Code on the web.
Caveats: Research preview at publication (the 2026-06-30 loops article still labels `/schedule` research preview). Limits may have changed since.
Relevance: medium. Nightly triage, docs drift and PR checklist routines fit a solo repo; the daily caps bound how many.

### Maximizing the value of your Claude Code sessions (Anthropic; no byline in the saved text; 2026-08-14)
File: refs/articles/claude.com/resources-articles-maximizing-the-value-of-your-claude-code-sessions/article.md   URL: https://claude.com/resources/articles/maximizing-the-value-of-your-claude-code-sessions
Thesis: A session's cost is "how many tokens end up in the context, how many turns they stay there, and how many contexts you're running at the same time", multiplied by model price and softened by the prompt cache. Efficient use means keeping context short and relevant and not breaking the cache mid-conversation.
Practices:
- TL;DR list: `/clear` between tasks; set model and effort before you start; @-mention files; quiet flags on noisy commands or run them in a subagent; `/context` once in a fresh session; `/compact` before a break. ("TL;DR")
- Everything is re-sent: "Everything that ends up in the conversation ... gets sent again on every turn after it, for the rest of the session." ("What decides how many tokens a session sends")
- Request order is "tool definitions, then the system prompt, then the conversation (with `CLAUDE.md` at the front of it)"; a change near the front re-prefills everything behind it. ("Prompt caching")
- Cache breakers: `/model` ("every model has its own cache"; includes opusplan, "which switches models every time you go in or out of plan mode"); `/effort` (part of the cache key); fast mode; `/compact`; time (cache "expires after an hour on a subscription or five minutes on an API key", `ENABLE_PROMPT_CACHING_1H=1` extends it). (same section)
- Cheap moments to switch model or effort: "the start of a session or right after a `/clear`". (same section)
- `/rewind` beats `/compact` for discarding a bad tangent: "Rewinding only cuts those turns off the end, so everything before them is still cached and it costs nothing." (same section, Tip)
- CLAUDE.md content rule: "Keep CLAUDE.md to specific instructions and move workflow-specific ones into skills, which only get loaded when they're used." Turn off unneeded MCP servers with `/mcp`. ("What ends up in the context", Tip)
- Commands in CLAUDE.md with quiet flags: "put the two or three commands you run all day in CLAUDE.md, quiet flags included", e.g. `npx vitest run <file> --reporter=dot` (spacing in the source is garbled as `<file>--reporter=dot`). (same section, Tip)
- Specific prompts cut searching: "Fix the failing test in `@utils.test.ts`" avoids both the search and the Read call; mention a file once only, since a second @-mention "generally attaches a second copy." (same section)
- Output handling: after 30,000 characters output goes to a file with a preview (`BASH_MAX_OUTPUT_LENGTH`); the problem is medium-sized noise such as 400 passing-test lines; a documented hook can rewrite noisy commands. (same section)
- Session length: "turn 40 is also re-reading the 39 turns before it"; `/clear` "when you start something new, and `/compact` when the earlier part of the same task is done." ("How many turns it stays there")
- Before clearing or compacting: "`/rename` before you `/clear` if you'll want the session back later"; tell `/compact` what to keep "or put a "Compact instructions" section in CLAUDE.md"; "/autocompact 200k" restores the earlier auto-compact point on 1M models (needs Claude Code v2.1.221+). (same section, Tip)
- Loops: "A `/loop` fires as a full turn in the session you set it up in, carrying that whole conversation with it every time"; run it from a fresh session in another terminal. (same section)
- Subagents: get their own context with system prompt, tools and CLAUDE.md "but not your conversation"; only the answer returns. "For a small job it's just overhead." They pay off for jobs with "a lot of output you don't need to keep, like going through a log." ("Subagents")
- Cheap subagents: "give it a subagent definition of its own with model: haiku (or sonnet). Otherwise it runs on whatever your main session is running on." (same section, Tip)
- `/model` and `/effort` persist across sessions; check them in a fresh session. `MAX_THINKING_TOKENS=0 claude` turns thinking off for one session "(except on Fable 5)". ("Input and output tokens", Tips)
Evidence and numbers: output "priced at roughly 5x input"; cache reads cost "0.1x the input price"; cache writes "up to 2x"; one small fix took five requests, each carrying the whole conversation; 30,000-character output threshold; cache TTL one hour (subscription) or five minutes (API key).
Tools and files named: `/clear`, `/compact`, `/context`, `/rewind`, `/rename`, `/model`, `/effort`, `/mcp`, `/autocompact`, `/loop`, opusplan, fast mode, `MAX_THINKING_TOKENS`, `ENABLE_PROMPT_CACHING_1H`, `BASH_MAX_OUTPUT_LENGTH`, subagent `model:` field, "Compact instructions" section in `CLAUDE.md`.
Caveats: Saved via the jina fallback and incomplete: the final section "Where to look first" ends with "four things are worth keeping an eye on, roughly in order of how much they cost:" followed only by an image, so the ranked list is missing from the saved text. Charts are "for illustration purposes only". Partly superseded six weeks later: the Opus 5.5 post says that for Opus 5.5 and Fable 5.1 effort can change mid-session "without resetting your cache".
Relevance: high. The most concrete source in the batch for context and session rules.

### Bringing memory to teams (Anthropic, 2025-09-11; update 2025-10-23)
File: refs/articles/claude.com/resources-articles-memory/article.md   URL: https://claude.com/resources/articles/memory
Thesis: Claude app (chat) memory: per-project memory summaries the user can view and edit, plus incognito chats.
Practices: "Claude creates a separate memory for each project" to stop unrelated details mixing. ("Memory built for work")
Relevance: low. Chat-app feature, not Claude Code configuration.

### Multi-agent coordination patterns: Five approaches and when to use them (Cara Phillips et al., Anthropic, 2026-04-10)
File: refs/articles/claude.com/resources-articles-multi-agent-coordination-patterns/article.md   URL: https://claude.com/resources/articles/multi-agent-coordination-patterns
Thesis: Five coordination patterns with their failure modes; start with the simplest that could work, usually orchestrator-subagent, and evolve only where it struggles.
Practices (pattern, when it fits, where it fails):
- Generator-verifier: fits "when output quality is critical and evaluation criteria can be made explicit". Fails without criteria: a verifier "told only to check whether output is good ... will rubber-stamp the generator's output." Needs "A maximum iteration limit with a fallback strategy (escalate to a human, return the best attempt with caveats)". ("Pattern 1: Generator-verifier")
- Orchestrator-subagent: "Claude Code uses this pattern", dispatching background subagents "when it needs to search a large codebase or investigate independent questions". Fits clear decomposition with minimal interdependence (e.g. PR review split into security, coverage, style, architecture). Fails as "an information bottleneck"; unless parallelised it "incurs multi-agent token costs without the speed benefit." ("Pattern 2: Orchestrator-subagent")
- Agent teams: persistent workers claiming tasks from a shared queue; fits independent long-running subtasks such as per-service migration. "Independence is the critical requirement"; shared files cause conflicting edits, so it "requires careful task partitioning and conflict resolution mechanisms." ("Pattern 3: Agent teams")
- Message bus: publish/subscribe for event-driven pipelines; harder to trace, and a misrouting router "fails silently". ("Pattern 4: Message bus")
- Shared state: agents read and write a common store with no coordinator; risk is "reactive loops", which "need first-class termination conditions: a time budget, a convergence threshold (no new findings for N cycles), or a designated agent" that decides when to stop. ("Pattern 5: Shared state")
- Choosing: subagents when subtasks are "short, focused, and produce clear outputs"; teams when workers must keep state across assignments; bus when the workflow emerges from events; shared state when findings must flow between agents. ("Choosing and evolving between patterns")
- Default: "For most use cases, we recommend starting with orchestrator-subagent. It handles the widest range of problems with the least coordination overhead." ("Getting started")
Evidence and numbers: none.
Tools and files named: none specific; Claude Code named as an orchestrator-subagent example.
Caveats: Conceptual, for teams that have already decided on multi-agent. The saved page now links from the orchestrator section to the 2026-10-22 fold-in article, which argues many such designs should collapse into one loop with skills.
Relevance: medium. Useful vocabulary and the termination-condition rule; a solo setup mostly needs patterns 1 and 2.

### Onboarding Claude Code like a new developer: Lessons from 17 years of development (Anthropic, about Brendan MacLean, MacCoss Lab; 2026-04-28)
File: refs/articles/claude.com/resources-articles-onboarding-claude-code-like-a-new-developer-lessons-from-17-y/article.md   URL: https://claude.com/resources/articles/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
Thesis: Treat Claude like a trainee: give it enough context for a small successful project, and have each project leave improved context for the next. Context is a versioned artefact to maintain, not something Claude accumulates by itself.
Practices:
- Method in his words: introduce Claude "as I would a trainee developer: by explaining enough to achieve a successful limited project and produce improved context for the next iteration". ("The same onboarding problem, a different kind of developer")
- CLAUDE.md is orientation only: it "handles environment setup and points Claude to the relevant documentation: think of it as the ‘lay of the land,’ not the expertise itself." Expertise lives in skills. (same section)
- Skills follow "reference do not embed": each "points into a central documentation knowledgebase rather than duplicating content". ("Invest in building your skill library")
- Most-used skills: `skyline-development` (orients to project and docs), `version-control` (commit and PR conventions), `debugging` (pulls Claude out of "guess and test" mode toward root cause before any fix). (same section)
- Critical skills get explicit trigger wording; the `debugging` description reads "ALWAYS load when investigating bugs, failures, or unexpected behavior." ("The same onboarding problem...")
- Plans do not persist: "The to-do lists and plans Claude generates don't persist across sessions. Context is what persists, and it has to be maintained deliberately." ("Context is your best friend")
- Context repo: he keeps it in a separate repository (`pwiz-ai`) because it "applies to all branches and time points"; "Keeping context in the same repo is a valid alternative". (same section)
- MCP where real data is needed: "test results, exception reports, support threads." ("Use MCP integrations when data access is key")
Evidence and numbers: 700,000+ lines of C#, 17 years, 200,000+ nightly tests; a year-stalled Files View feature finished in two weeks; less than a day to add long-wanted features to a Java module; 2,000+ tutorial screenshots reproduced automatically; a daily morning summary of failures generated by Claude Code. Anecdotal, single lab.
Tools and files named: `CLAUDE.md`, `pwiz-ai` repo, skills `debugging`, `version-control`, `skyline-development`, custom MCP servers (C# and Python).
Caveats: Case study, not measured. The "ALWAYS load when..." trigger is a practitioner's choice; Anthropic's own description guidance prefers stating capabilities and trigger conditions (inference; no source here says ALWAYS is harmful in descriptions).
Relevance: high. Smallest credible large-codebase recipe: thin CLAUDE.md, pointer-style skills, docs as the knowledge base, context versioned and grown per task.

### Self-hosted environments for Claude Code (Anthropic, 2026-08-06)
File: refs/articles/claude.com/resources-articles-run-claude-code-sessions-on-your-own-compute/article.md   URL: https://claude.com/resources/articles/run-claude-code-sessions-on-your-own-compute
Thesis: Team and Enterprise organisations can run cloud Claude Code sessions on their own runners; Anthropic recommends its hosted option for most.
Practices: distinction worth knowing: Remote Control "lets developers continue sessions running on their own machines from a phone or browser", ending when that machine stops. ("How it works", Note)
Relevance: low. Team/Enterprise public beta; not for a solo developer.

### Skills explained: How Skills compares to prompts, Projects, MCP, and subagents (Anthropic, 2026-03-05)
File: refs/articles/claude.com/resources-articles-skills-explained/article.md   URL: https://claude.com/resources/articles/skills-explained
Thesis: Each building block has one job: prompts for one-off instructions, Projects for background knowledge, skills for procedural knowledge, subagents for delegated tasks with their own context and tools, MCP for connectivity. Repetition is the signal to move something into a skill.
Practices:
- Progressive disclosure sizes: "metadata loads first (\~100 tokens)", "Full instructions load when needed (\<5k tokens)", bundled files only as required. ("What are Skills?")
- Prompt to skill: "If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill." ("What are prompts?")
- Subagent uses: task specialisation, context management, parallel processing, and "Tool restriction: Limit specific subagents to safe operations (e.g., read-only access)". Example: a code-reviewer with Read, Grep and Glob "but not Write or Edit". ("What are subagents?")
- Skill versus subagent: "Use Skills to teach expertise that any agent can apply; use subagents when you need independent task execution with specific tool permissions and context isolation." If several agents need the same expertise, make it a skill. (same section)
- Skill versus MCP: "MCP connects Claude to data; Skills teach Claude what to do with that data." ("What is MCP?")
- Combination: "subagents can access and use Skills just like the main agent." ("Can subagents use Skills?")
- Comparison table, "When it loads": skills "Dynamically, as needed"; prompts "Each turn"; Projects "Always in project"; subagents "When invoked"; MCP "Always available". ("Comparison: choosing the right tool")
- Subagent definition shape in the examples: `name`, `description` (with "Use proactively for competitive analysis"), `tools`, then a system prompt beginning "You are a ...". ("Step 4: Configure subagents")
Evidence and numbers: about 100 tokens metadata, under 5k tokens for instructions.
Tools and files named: skills, Projects (claude.ai, 200K context, RAG mode), subagents (`name`, `description`, `tools` frontmatter), MCP.
Caveats: Covers claude.ai Projects, which are not a Claude Code primitive; CLAUDE.md, rules and hooks are absent (see the steering article). The example subagents use "You are a market research analyst" role prompts, which the prompt-engineering article calls often unnecessary. The saved page links its subagent FAQ to the 2026-10-22 fold-in article.
Relevance: medium. Clear skill-versus-subagent and skill-versus-MCP criteria; the read-only reviewer subagent example.

### Introducing Agent Skills (Anthropic, 2025-10-16; update note 2025-12-18)
File: refs/articles/claude.com/resources-articles-skills/article.md   URL: https://claude.com/resources/articles/skills
Thesis: Launch post: skills are folders of instructions, scripts and resources that Claude loads only when relevant; they are composable, portable, efficient and can include executable code.
Practices:
- Code in skills is for "tasks where traditional programming is more reliable than token generation." ("How Skills work")
- Claude Code: install via plugins, share through version control, or add manually to `~/.claude/skills`. ("Claude Code")
- Security: skills let Claude execute code, so "stick to trusted sources to keep your data safe." ("What's next")
Tools and files named: `SKILL.md`, `~/.claude/skills`, skill-creator, `/v1/skills`, Agent Skills open standard (agentskills.io).
Relevance: low-medium. Origin of the format; superseded in detail by the 2026 guide and skill-creator posts.

### Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents (Michael Segner, Anthropic, 2026-06-18)
File: refs/articles/claude.com/resources-articles-steering-claude-code-skills-hooks-rules-subagents-and-more/article.md   URL: https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more
Thesis: Claude Code has seven ways to deliver instructions (CLAUDE.md files, rules, skills, subagents, hooks, output styles, appending the system prompt). Each differs in when it loads, whether it survives compaction, and how much authority it carries; "Each method trades context cost against authority." The article gives a table and five "wrong place" tests.
Practices (the summary table, reproduced by column: when loaded; compaction behaviour; context cost; when to use):
- CLAUDE.md (root): "Session start; stays in context for the entire session"; "Memoized. Read once and cached for the session; cache cleared and re-read after compaction"; "High. Every line costs tokens whether relevant or not"; "Build commands, directory layout, monorepo structure, coding conventions, team norms".
- CLAUDE.md (subdirectory): "On-demand, when Claude reads a file under that subdirectory"; "Lost until that subdirectory is touched again"; Low; "Conventions specific to a subdirectory".
- Rules: "Session start (user-level rules) or only when matching files are touched (path-scoped)"; "Re-injected on compaction"; "Medium. Always-on unless path-scoped"; "Specific constraints or conventions (e.g., all API handlers must validate input with Zod)".
- Skills: "Name and description at session start; full body loads when the skill is invoked"; "Invoked skills re-injected up to a shared budget; oldest dropped first"; Low; "Procedural workflows (deploy or release checklists)".
- Subagents: "Name, description, and tool list at session start; body loads only when called via the Agent tool"; "Only the final message (summary plus metadata) returns to the main session"; "Low. Zero cost in main context until called"; parallel work or isolated side tasks returning only a summary "(deep search, log analysis, dependency audit)".
- Hooks: "Fire on lifecycle events"; "Bypass compaction entirely"; Low (config lives outside context; blocking errors may return); "Deterministic automation: run linters, post to Slack on completion, block commands, back up chat history on PreCompact".
- Output styles: session start, injected into the system prompt; "Never compacted"; "High. Occupies context window, but overwrites default system prompt"; "Significant role changes (code assistant to general assistant)".
- Appending the system prompt: session start via CLI flag; never compacted, that invocation only; "Moderate. Cached after first request in a session"; "Tone, response length, formatting preferences".
Practices (per method):
- CLAUDE.md length and ownership: "Keep CLAUDE.md under 200 lines, give it an owner, and review changes to it like code." Content follows prompt rules: "being explicit, explaining the why behind constraints, and showing examples." ("CLAUDE.md files", Tip)
- CLAUDE.md role: "an overview of your codebase, or as an index pointing to other files where Claude can find more information as needed." (same section)
- Why short: every line loads for every session, which "consumes tokens and dilutes adherence to the instructions that actually matter." As it grows, "push team-specific conventions into path-scoped rules and procedures into skills". (same section)
- Root CLAUDE.md files are re-read after compaction; a subdirectory file such as `app/api/CLAUDE.md` loads only when Claude reads a file under it and is "gone until that subdirectory is touched again" after compaction. `claudeMdExcludes` skips other teams' files. (same section)
- Rules: markdown files in `.claude/rules/`; "Unscoped rules behave like CLAUDE.md"; a `paths` frontmatter list (e.g. `"src/api/**"`, `"**/*.handler.ts"`) makes a rule load only when Claude reads matching files. ("Rules")
- Rule versus nested CLAUDE.md: use a path-scoped rule rather than a nested CLAUDE.md "when the instruction regards a cross-cutting concern or file that appears in multiple (but not all) corners of the codebase." Example constraint: "migrations are append-only". ("Rules", Tip)
- Skills: in `.claude/skills/`; invoked by slash command or auto-matching; "Instructions that are procedural, like deploy workflows, release checklists, or review processes, belong in a skill rather than in CLAUDE.md." After many invocations in one session, "the oldest ones drop first" on compaction. ("Skills")
- Subagents: markdown files in `.claude/agents/` with YAML frontmatter "(name, description, plus optional fields for model and tool access)" and a body that becomes the system prompt; the body "never enters the parent conversation at all"; "subagents can nest up to five levels deep". ("Subagents")
- Subagent versus skill: a subagent when a side task (deep search, log analysis, dependency audit) "would clutter your main conversation with intermediate results you won't reference again." And: "Use a skill when you want the procedure to play out inside the main thread so you can see and steer each step." ("Subagents", Tip)
- Hooks: registered in `settings.json`, managed policy settings, or skill/agent frontmatter. Types: "command, HTTP, mcp\_tool, prompt, and agent"; all are triggered deterministically, but prompt and agent hooks "use Claude’s judgment rather than a set of rules to determine the output." ("Hooks")
- Hook output is mostly invisible to Claude: a `PreCompact` backup hook writes a file but "Claude wouldn’t know which file had the chat history saved" unless the hook returns it; a blocking hook's stderr is saved to context. (same section)
- Hook use: "Use hooks for anything that should happen deterministically", e.g. linters after edits, a Slack post on completion, or blocking commands. "A `PreToolUse` hook can inspect any tool call and exit code 2 to deny it." ("Hooks", Tip)
- Output styles: files in `.claude/output-styles/`; they "carry the highest instruction-following weight" and by default replace the coding instructions (how to scope changes, comments, security concerns, "Verification habits like running tests before declaring work complete") unless `keep-coding-instructions: true`. Check built-ins "Proactive, Explanatory, and Learning" first. ("Output styles")
- Append flag: `append-system-prompt` is additive and per-invocation, with "diminishing returns for adherence": "the more instructions you provide using this method, the less strictly Claude will follow them, particularly if any contradict." ("Appending the system prompt", Tip)
Practices (the five relocation tests, "When to use each method"):
- ""Every time X, always do Y" in CLAUDE.md": use a hook. "The model choosing to run a formatter is different from the formatter running automatically."
- "“Never do this” in CLAUDE.md": "an instruction is the wrong tool"; under pressure, in a long session, an ambiguous situation or a prompt injection, "the model can fail to follow a prompted rule. A real guardrail needs to be deterministic, and the enforcement methods are hooks and permissions." Managed settings are the only organisation-wide enforcement.
- "A 30-line procedure in CLAUDE.md": "Procedures belong in skills. CLAUDE.md is for facts Claude should hold all the time: build commands, monorepo layout, team conventions."
- "An API-specific rule without paths": scope it; "An unscoped rule is mechanically identical to putting the content in CLAUDE.md: always loaded, always costing tokens."
- "Writing personal preferences to a project-level CLAUDE.md file": every file-based method has a user-level counterpart; personal preferences go there, team-wide codebase-specific ones in project files.
Evidence and numbers: under 200 lines for CLAUDE.md; nesting up to five levels; no measurements.
Tools and files named: `CLAUDE.md` (root, subdirectory, local, managed), `claudeMdExcludes`, `.claude/rules/` with `paths:`, `.claude/skills/<name>/SKILL.md`, `.claude/agents/`, Agent tool, `settings.json` hooks, `PreToolUse`, `PreCompact`, `.claude/output-styles/`, `keep-coding-instructions`, `append-system-prompt`, `/code-review`, plugins.
Caveats: MCP is not one of the seven methods and is not placed in the table (it is covered in "Skills explained" and the large-codebases table). Mods (2026-10) postdate it. The table says appending the system prompt has "Moderate" cost and output styles "High", while the prose calls output styles "moderate context cost": a small internal inconsistency. The table's rule row says session start for "(user-level rules)", while the prose says all unscoped rules load at session start.
Relevance: high. This is the primary source for (a).

### How and when to use subagents in Claude Code (Anthropic, 2026-04-07)
File: refs/articles/claude.com/resources-articles-subagents-in-claude-code/article.md   URL: https://claude.com/resources/articles/subagents-in-claude-code
Thesis: A subagent is "an isolated Claude instance with its own context window" that returns only its result. Use it for research, independent parallel tasks and unbiased review; skip it for small, sequential or same-file work. Start by asking in conversation and automate later.
Practices:
- Five use signals: research-heavy tasks ("Gathering context requires reading dozens of files"); multiple independent tasks ("Sub-tasks have no dependencies between them"); fresh perspective ("Verification is needed without conversation history influencing the analysis"); verification before committing (check the implementation "isn't overfitting to tests or missing edge cases"); pipeline workflows ("Sequential stages with clear handoffs"). ("When should you use subagents?")
- Threshold: a task that "requires exploring ten or more files, or involves three or more independent pieces of work" is "a strong signal to direct Claude toward subagents." (same section, Pro-tip)
- Prompting a subagent: scope clearly, request parallel execution explicitly, "Specify what should be returned", and ask for fresh context: "Use a subagent that does not see our previous discussion". ("Conversational invocation")
- Background: Ctrl+B sends a running subagent to the background; `/tasks` lists background work. (same section, Pro-tip)
- Custom subagents: markdown in `.claude/agents/` (project) or `~/.claude/agents/` (user), each with a system prompt, tool permissions and optionally a model; create with `/agents`. ("Custom subagents")
- Description routing: "Be specific about the trigger conditions, not just the capability. "Reviews code for security issues before commits" routes better than "security expert."" (same section, Pro-tip)
- CLAUDE.md holds the delegation policy: "Custom subagents define who the specialists are. CLAUDE.md files define the rules for when Claude should reach for them", e.g. "Code reviews should always use read-only subagents". ("CLAUDE.md instructions")
- Skills can orchestrate subagents (a `/deep-review` skill running a three-part subagent analysis). "A skill is a directory, not a single file"; "The legacy `.claude/commands/` format was a single flat file". ("Skills")
- Stop hook as a test gate: a script at `.claude/hooks/check-tests.sh` runs the suite and on failure "returns JSON with `decision: "block"` and a `reason`"; "The `stop_hook_active` guard at the top prevents infinite loops". ("Hooks")
- Order of adoption: "Conversational invocation or CLAUDE.md instructions are the better starting point; hooks come later, as workflows mature." (same section)
- When not to: "Sequential, dependent work" (a single session beats "a relay of subagents passing state through files"); "Same-file edits"; "Small tasks"; "Too many specialist agents" ("flooding Claude with options makes automatic delegation less reliable. Most teams settle on a handful of well-scoped agents"); work needing agents to talk to each other (use agent teams, which are "heavier and more expensive"). ("When shouldn’t you use subagents?")
- Built-in types: general-purpose, Plan, Explore ("optimized for fast, read-only code search"). ("What is a subagent?")
Evidence and numbers: thresholds of ten or more files and three or more independent pieces; no measurements.
Tools and files named: `.claude/agents/`, `~/.claude/agents/`, `/agents`, `/tasks`, Ctrl+B, `.claude/skills/`, `.claude/commands/` (legacy), `.claude/hooks/check-tests.sh`, `Stop` hook with `decision: "block"` and `stop_hook_active`, agent teams.
Caveats: The saved text has lost every code example (lines such as "Here's an effective prompt structure:" are followed by nothing), so the example agent file, CLAUDE.md policy, skill and hook script cannot be quoted. Disagreement: this article recommends "Pipeline workflows" (design, implement, test as separate subagents), which the 2026-01-23 multi-agent article lists as a problematic boundary ("Sequential phases of the same work") and this article's own "Sequential, dependent work" bullet warns against. The later Opus 4.7 post (2026-04-16) notes the model spawns fewer subagents by default, and the 2026-10-22 article argues for fewer subagents overall.
Relevance: high. Concrete signals, file locations and the short-roster advice for (e).

### The advisor strategy: Give Sonnet an intelligence boost with Opus (Anthropic, 2026-04-09)
File: refs/articles/claude.com/resources-articles-the-advisor-strategy/article.md   URL: https://claude.com/resources/articles/the-advisor-strategy
Thesis: Run a cheaper model (Sonnet or Haiku) as the executor end to end and let it consult a stronger model (Opus) only at hard decisions. The advisor returns "a plan, a correction, or a stop signal" and never calls tools or writes user-facing output.
Practices:
- It inverts the usual pattern: "a smaller, more cost-effective model drives and escalates without decomposition, a worker pool, or orchestration logic." ("Build cost-effective agents with the advisor strategy")
- API shape: tool type `advisor_20260301` with `model` and `max_uses` (example: 3) in one `/v1/messages` request; beta header `advisor-tool-2026-03-01`. ("The advisor tool", "Get started")
- Advisor output is short: "typically 400-700 text tokens". ("The advisor tool", Pricing)
- Evaluate three arms on your own evals: "Sonnet solo, Sonnet executor with Opus advisor, and Opus solo." ("Get started")
Evidence and numbers: Sonnet 4.6 with Opus 4.6 advisor: "a 2.7 percentage point increase" on SWE-bench Multilingual over Sonnet alone "while reducing cost per agentic task by 11.9%"; Haiku 4.5 with Opus advisor on BrowseComp 41.2% versus 19.7% solo, trailing Sonnet solo by 29% in score at 85% lower cost per task. Footnotes give setup (five trials of 300 problems; thinking off for advisor runs). A later figure (2026-07-24 models article): Sonnet 5 with a Fable 5 advisor "within 10% of Fable 5’s score at 63% of the price".
Tools and files named: advisor tool (Claude Platform beta), `advisor_20260301`, `max_uses`.
Caveats: This is an API feature. No article in this batch describes an advisor setting inside Claude Code, so using it in a Claude Code project setup is not supported by these sources (the nearest Claude Code analogues stated in the batch are a cheaper `model:` on a subagent and using "the most capable model for judgment calls" in routines). Benchmarks are the vendor's own and on 4.6-generation models. (`meta.json` lists a quoted customer as author.)
Relevance: medium. Supports the cost pattern of a cheap executor with a strong model for judgement; not directly configurable in Claude Code per these sources.

### Token-saving updates on the Anthropic API (Anthropic, 2025-03-13)
File: refs/articles/claude.com/resources-articles-token-saving-updates/article.md   URL: https://claude.com/resources/articles/token-saving-updates
Thesis: Claude 3.7 Sonnet era API changes: cache reads stopped counting against input rate limits, cache breakpoints became automatic-prefix, and a token-efficient tool-use beta was added.
Evidence and numbers: prompt caching "reducing costs by up to 90% and latency by up to 85% for long prompts"; token-efficient tool use cut output tokens "by up to 70%", 14% on average.
Relevance: low. Oldest item in the batch (2025-03); historical background for why cache hits dominate cost in the 2026 articles.

### Using Claude Code: session management and 1M context (Thariq Shihipar, Claude Code team, 2026-04-15)
File: refs/articles/claude.com/resources-articles-using-claude-code-session-management-and-1m-context/article.md   URL: https://claude.com/resources/articles/using-claude-code-session-management-and-1m-context
Thesis: After each turn there are five options (continue, rewind, clear, compact, subagent), and choosing among them is context management. Even with 1M tokens, context rot occurs, so new task means new session.
Practices:
- Context rot defined: "model performance degrades as context grows because attention gets spread across more tokens, and older, irrelevant content starts to distract from the current task." ("A quick primer on context, compaction and context rot")
- Rule of thumb: "when you start a new task, you should also start a new session." Exception: closely related follow-ups (documenting the feature just built), where a fresh session would have to reread the files. ("When to start a new session")
- Rewind instead of correcting: rewind to just after the useful file reads and re-prompt with what you learned, rather than typing "that didn't work, try X instead." ("Rewinding instead of correcting")
- Handoff via rewind: "summarize from here" or `/rewind` makes Claude "summarize its learnings and create a handoff message". (same section)
- Compact versus clear: compact is "lossy, but you didn't have to write anything yourself"; steer it, e.g. `/compact focus on the auth refactor, drop the test debugging`. With `/clear` "*you* write down what matters" (goal, constraint, files that matter, approaches ruled out). ("Compacting vs. launching a fresh session")
- Bad autocompacts happen "when the model can’t predict the direction your work is going", and "due to context rot, the model is at its least intelligent point when compacting." So compact proactively with a description of what comes next. ("What causes a bad autocompact?")
- Subagent test: "*will I need this tool output again, or just the conclusion?*" Example prompts: verify work against a spec file; read another codebase and summarise; write docs from git changes. ("Subagents and fresh context windows")
- Decision table: same task and context still relevant, Continue; wrong path, Rewind (double-Esc); mid-task but bloated, `/compact <hint>`; new task, `/clear` ("Zero rot; you control exactly what carries forward."); next step yields output you only need the conclusion of, Subagent. ("Putting it together")
Evidence and numbers: none; "Claude Code has a context window of one million tokens."
Tools and files named: `/usage`, `/rewind` (Esc Esc), `/clear`, `/compact <hint>`, "summarize from here", Agent tool.
Caveats: Contradicts the 1M GA post's "no longer needed" claim about clearing and summarising. No token threshold for rot is given in this saved text.
Relevance: high. The decision table is directly usable for (h).

### Using CLAUDE.md files: Customizing Claude Code for your codebase (Anthropic, 2025-11-25)
File: refs/articles/claude.com/resources-articles-using-claude-md-files/article.md   URL: https://claude.com/resources/articles/using-claude-md-files
Thesis: CLAUDE.md gives Claude persistent project context (map, tools, workflows). Start from `/init`, keep it concise, and grow it from real friction rather than writing a comprehensive file up front.
Practices:
- Content the article lists: "common bash commands, core utilities, code style guidelines, testing instructions, repository conventions, developer environment setup, and project-specific warnings. There is no required format." ("What is a CLAUDE.md file?")
- Admission test: "Each addition should solve a real problem you have encountered, not theoretical concerns about what Claude might need." (same section)
- Example file sections: Project Context, About This Project, Key Directories, Standards, Common Commands, Notes; about 20 lines. (same section)
- `/init` generates a starter from package files, docs, config and code; it is "a starting point, not a finished product". Afterwards: review for accuracy, add workflow instructions Claude could not infer (branch naming, deployment, review requirements), "Remove generic guidance that doesn't apply to your project", commit it. ("Getting started with /init")
- `/init` on a project that already has a CLAUDE.md reviews the file and suggests improvements. (same section)
- Maintenance by accretion: "use the `#` key to add instructions you find yourself repeating". (same section)
- Give Claude a map: project summary, high-level directory tree, main dependencies, architectural patterns, "any non-standard organizational choices". ("Give Claude a map")
- Document custom tools with usage examples and mention `--help` where it exists; describe MCP server usage limits (the Slack example: which channel, what for, what not for, rate limit). ("Connect Claude to your tools")
- Default workflow answers four questions before changes: investigate first? plan needed? what information is missing? "How will effectiveness be tested?" Named workflows: "explore-plan-code-commit for features, test-driven development for algorithmic work, or visual iteration for UI changes." ("Define standard workflows")
- Length: "CLAUDE.md is added to Claude Code's context every time", so "keep it concise. One option: break up information into separate markdown files and reference them inside the CLAUDE.md file." ("Start simple, expand deliberately")
- Exclude: "sensitive information, API keys, credentials, database connection strings, or detailed security vulnerability information"; "treat it as documentation that could be shared publicly." (same section)
- "It's tempting to create a comprehensive CLAUDE.md right away. Resist that urge." (same section)
- Adjacent tips: `/clear` between distinct tasks; a subagent for a distinct phase such as a security review after implementation; custom slash commands as markdown in `.claude/commands/` with `$ARGUMENTS`, `$1`, `$2`. ("Additional tips for working with Claude Code")
Evidence and numbers: none.
Tools and files named: `CLAUDE.md` (repo root, parent directories, home folder), `/init`, `#` key, `.mcp.json`, `--mcp-debug`, `.claude/commands/`, `$ARGUMENTS`, `/clear`.
Caveats: Dated 2025-11 and partly superseded. It puts multi-step workflows in CLAUDE.md, where the steering article (2026-06) says "Procedures belong in skills". It teaches `.claude/commands/`, which the subagents article (2026-04) calls "legacy" relative to skills. It says CLAUDE.md "becomes part of Claude's system prompt", while the session-value article (2026-08) says requests go "tool definitions, then the system prompt, then the conversation (with `CLAUDE.md` at the front of it)". It gives no line limit; the steering article gives "under 200 lines". The 34-item checklist command it shows is the kind of long always-explicit prompt later guidance trims (inference). One file name is misspelled in the source (`performance-optimization.mm`).
Relevance: high for what to include and exclude and for the `/init` then prune routine; use the 2026 articles for placement of procedures.

### The complete guide to building Skills for Claude: guide chapters (Anthropic, 2026-01-26)

The guide is saved as eight files (index plus seven chapters), listed here in the batch's order. All are dated 2026-01-26, before the 2026-03-03 skill-creator eval update.

#### Distribution and sharing
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-distribution-a/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/distribution-and-sharing
Thesis: As of January 2026 skills are distributed by folder (zip upload to Claude.ai, or the Claude Code skills directory), org-wide deployment, GitHub, or the API.
Practices:
- A skill folder "should not contain a README.md"; the README belongs at repo level for humans. ("Recommended approach today")
- Open standard: platform-specific needs go in the skill's `compatibility` field. ("An open standard")
- Describe a skill by outcome, not mechanism ("Focus on outcomes, not features"). ("Positioning your skill")
Tools and files named: `/v1/skills`, `container.skills`, `compatibility`, Agent Skills standard.
Relevance: low. Distribution; the no-README rule and `compatibility` field matter for cross-harness portability.

#### Fundamentals
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-fundamentals/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/fundamentals
Thesis: A skill is a folder with a required `SKILL.md` and optional `scripts/`, `references/`, `assets/`, loaded in three levels.
Practices:
- Three levels: frontmatter "Always loaded in Claude's system prompt"; body "Loaded when Claude thinks the skill is relevant to the current task"; linked files that Claude "can choose to navigate and discover only as needed." ("Progressive disclosure")
- Composability: "Your skill should work well alongside others, not assume it's the only capability available." ("Composability")
- Portability holds "provided the environment supports any dependencies the skill requires." ("Portability")
- MCP is "What Claude can do"; skills are "How Claude should do it". ("The kitchen analogy", table)
Relevance: medium. The canonical folder structure.

#### Introduction
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-introduction/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/introduction
Thesis: Skills suit repeatable workflows; expect "about 15-30 minutes to build and test your first working skill using the skill-creator."
Relevance: low (orientation only).

#### Patterns and troubleshooting
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-patterns-and-t/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/patterns-and-troubleshooting
Thesis: Five skill patterns seen in practice, then a failure-mode catalogue with fixes.
Practices:
- Patterns and their key techniques: (1) sequential workflow orchestration (explicit step order, dependencies, "Validation at each stage", "Rollback instructions for failures"); (2) multi-MCP coordination (phase separation, validation before the next phase); (3) iterative refinement (a validation script such as `scripts/check_report.py`, explicit quality criteria, "Know when to stop iterating"); (4) context-aware tool selection (decision tree, fallbacks, explain the choice); (5) domain-specific intelligence (rules applied before action, audit trail). ("Pattern 1" to "Pattern 5")
- Does not trigger: revise the description. Checklist: "Is it too generic?", "Does it include trigger phrases users would actually say?", file types. Debug by asking Claude: "When would you use the \[skill name\] skill?" ("Skill doesn't trigger")
- Triggers too often: add negative triggers ("Do NOT use for simple data exploration (use data-viz skill instead)"), be more specific, clarify scope. ("Skill triggers too often")
- Instructions not followed, causes: too verbose; buried ("Put critical instructions at the top"); ambiguous language (replace "Make sure to validate things properly" with an explicit checklist). ("Instructions not followed")
- Scripts over prose for critical checks: "Code is deterministic; language interpretation isn't." (same section, Advanced technique)
- "Model "laziness"": add encouragement such as "Quality is more important than speed", but "Adding this to user prompts is more effective than in SKILL.md". (same section)
- Size limits: "Keep SKILL.md under 5,000 words"; move detail to `references/`; "Evaluate if you have more than 20 - 50 skills enabled simultaneously". ("Large context issues")
- Upload errors: file must be exactly `SKILL.md`; frontmatter needs `---` delimiters; name must be kebab-case. ("Skill won't upload")
Evidence and numbers: 5,000-word SKILL.md ceiling; 20-50 enabled skills as the point to review.
Caveats: Patterns "represent common approaches we've seen work well, not prescriptive templates." The "CRITICAL:" header and "Take your time" encouragement are 2026-01 advice; the 2026-10-22 article's `/claude-api prompt-audit` exists to flag "instructions written for older models", so re-test such phrasing on current models (inference).
Relevance: high. The failure-mode list for skills.

#### Planning and design
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-planning-and-d/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/planning-and-design
Thesis: Start from two or three concrete use cases, define success criteria, then follow strict naming and frontmatter rules; the frontmatter description decides whether the skill ever loads.
Practices:
- "Before writing any code, identify 2-3 concrete use cases your skill should enable", each with trigger, steps and result. ("Start with use cases")
- Three categories: document and asset creation; workflow automation; MCP enhancement. ("Common skill use case categories")
- Success criteria (called "aspirational targets"): "Skill triggers on 90% of relevant queries" measured with "10-20 test queries"; compare tool calls and tokens with and without the skill; "0 failed API calls per workflow"; run the same request 3-5 times for consistency. ("Define success criteria")
- Structure: `your-skill-name/` with `SKILL.md`, `scripts/`, `references/`, `assets/`. `SKILL.md` exact and case-sensitive; folder in kebab-case; no `README.md` in the skill folder. ("File structure", "Critical rules")
- Frontmatter: `name` (kebab-case, should match the folder) and `description`, which "MUST include BOTH" what it does and when to use it, "Under 1024 characters", no XML angle brackets. Optional: `license`, `compatibility` (1-500 characters), `metadata` (author, version, mcp-server). ("Field requirements")
- Security reason: "Frontmatter appears in Claude's system prompt. Malicious content could inject instructions." Names containing "claude" or "anthropic" are reserved. ("Security restrictions")
- Description formula: "[What it does] + [When to use it] + [Key capabilities]", with quoted trigger phrases, e.g. "Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets"." Bad: "Helps with projects."; missing triggers; "Too technical, no user triggers". ("The description field")
- Body template: `## Instructions` with numbered steps, each with command and expected output; `## Examples` (user says, actions, result); `## Troubleshooting` (error, cause, solution). ("Writing the main instructions")
- Be specific: "Run `python scripts/validate.py --input {filename}` to check data format" versus the bad "Validate the data before proceeding." Reference bundled files by path and say what they contain. ("Best practices for instructions")
Evidence and numbers: 90% trigger target over 10-20 queries; 1024-character description limit; 3-5 repeat runs.
Tools and files named: `SKILL.md`, `scripts/`, `references/`, `assets/`, frontmatter keys `name`, `description`, `license`, `compatibility`, `metadata`.
Caveats: The guide admits "there will be an element of vibes-based assessment". Trigger-phrase-heavy descriptions here differ in style from the trigger-condition descriptions in the Claude Code articles (e.g. "Use when the diff touches error handling or logging"); both state what and when.
Relevance: high. Naming, frontmatter and description rules.

#### Resources and references
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-resources-and/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/resources-and-references
Thesis: Checklist and frontmatter reference.
Practices:
- Pre-upload checks: "Tested triggering on obvious tasks", "Tested triggering on paraphrased requests", "Verified doesn't trigger on unrelated topics", functional tests pass. ("Reference A: Quick checklist")
- Optional frontmatter includes `allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"` "Restrict tool access", plus `license` and `metadata` (author, version, mcp-server, category, tags). ("Reference B: YAML frontmatter")
- After release: "Monitor for under/over-triggering" and "Update version in metadata". ("After upload")
Caveats: The `allowed-tools` example uses a space-separated string with `Bash(python:*)`, while the 2026-07 verification article writes `allowed-tools: [Read, Edit, Grep]` (a list). The auto mode article (2026-08) says interpreter-wide allow rules such as `Bash(python:*)` amount to arbitrary code execution and are set aside in auto mode; whether that applies to a skill's `allowed-tools` is not stated in this batch.
Relevance: medium. The checklist is reusable as a skill-review rubric.

#### Testing and iteration
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude-testing-and-it/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/testing-and-iteration
Thesis: Test triggering, function and performance against a no-skill baseline; build a skill by first getting one hard task to succeed.
Practices:
- Origin of good skills: "the most effective skill creators iterate on a single challenging task until Claude succeeds, then extract the winning approach into a skill." (intro)
- Three test areas: triggering (obvious, paraphrased, and should-not-trigger prompts), functional (Given/When/Then cases), performance comparison with and without the skill (messages, failed calls, tokens). ("Recommended testing approach")
- Feed failures back: bring edge cases to skill-creator, e.g. "Use the issues & solution identified in this chat to improve how the skill handles \[specific edge case\]". ("Iterative improvement")
- Signals: undertriggering (skill "doesn't load when it should", users enabling it manually); overtriggering (loads for irrelevant queries, users disabling it); execution issues (inconsistent results, corrections needed). ("Iteration based on feedback")
Evidence and numbers: illustrative comparison only ("12,000 tokens" without versus "6,000 tokens" with), not a measurement.
Caveats: Superseded on one point: this chapter says "skill-creator helps you design and refine skills but does not execute automated test suites or produce quantitative evaluation results", but the 2026-03-03 post adds evals, benchmark mode and comparator agents.
Relevance: high. The test plan for any project skill.

#### Guide index page
File: refs/articles/claude.com/resources-guides-the-complete-guide-to-building-skills-for-claude/article.md   URL: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude
Thesis: Two-paragraph landing page restating that skills "let you teach Claude once and benefit every time."
Relevance: low (no content beyond the chapters).

