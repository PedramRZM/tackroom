# Principles

Why the template is shaped the way it is. Each principle says what the template does, what it
rests on, and how well that part is tested. Sources are paths under `refs/`; a notes file
(`refs/notes/...`) points on to the primary texts with quotes and locators.

Read the status lines. Some of this was run and observed, some follows documentation that was
not run here, and some is a judgement call.

## 1. Give the agent a check it can run, and make it show the result

Template: `scripts/agent/check` is the one command for "is this repository healthy". It prints
one line per check and shows a failure's last lines, so a pass costs almost no context. The
`verify` skill asks for evidence per acceptance criterion, and the pull request template has an
Evidence section.

Why: this is the most repeated finding in the whole corpus. Anthropic's Claude Code team
presents a runnable check as the first fix to try, before raising effort or changing model
(`notes/anthropic-claude-dev-blog.md`, recurring practice 1). The docs call the check command
"the single most useful line" in an instruction file (`notes/claude-code-docs-extending.md`
1.10). Independent practitioners say the same, and add that the check must be cheap in context:
silent on success, loud on failure (`notes/industry-practices.md`, finding 3;
`notes/people-osmani-karpathy-willison.md`, finding 1).

Status: the script and the skill were run in scratch projects. The auto-detection in the
shipped `check` is a convenience of mine; replace it with the project's exact commands.

## 2. What must always happen is a hook or a rule, not a sentence

Template: `.claude/hooks/guard.py` blocks reads of secret-looking files, recursive deletes of
the repository or home, force-pushes and pushes to a protected branch. `stop-check.py` runs the
quick checks when a turn ends with changed files and sends failures back. Preferences stay in
prose.

Why: Anthropic's placement guide: "every time X, do Y" goes in a hook, and "never do this" goes
in hooks and permissions, because the model can fail to follow a prompted rule
(`notes/anthropic-claude-com-practice.md` (a)). "The skill makes violations rare and the hook
makes them close to impossible" (`notes/anthropic-claude-com-org-and-cases.md`, finding 5). The
docs: a rule a hook can enforce should not be left to an instruction, and adding emphasis to a
line that keeps being missed is the signal to move it (`notes/claude-code-docs-extending.md`
1.10). OpenAI and others describe the same ladder from note to mechanical check
(`notes/devcon-2-harness-specs-verification.md`, finding 1; `notes/industry-practices.md`,
finding 2).

Status: guard logic has 56 unit tests. Under Claude Code, a live headless run showed the
memory-tier rule and the protected-branch rule refusing the action. The secrets rule was not
run live here (the owner's own hook intercepts first); `tools/live-test` does it.

## 3. A hook is a guardrail. The boundary is what the agent cannot reach

Template: the guard's header says so. The settings file carries sandbox configuration
(credential variables hidden from commands, a short network allowlist) and deny rules for
credential files, and `docs/claude-code.md` explains how to switch the sandbox on.

Why: a recorded demo shows auto mode refusing a secret-reading skill and then running the same
logic rewritten as a Python module (`notes/devcon-4-security-runtime-misc.md`, finding 1).
Anthropic's numbers: people approve about 93% of permission prompts, sandboxing cut prompts by
84%, and their 2026 containment post puts auto mode inside a sandbox
(`notes/anthropic-engineering.md`, findings 5 and 6). The docs state that deny rules do not stop
a script that opens a file itself, and that hooks run outside the sandbox
(`notes/claude-code-docs-settings-security.md` 3.5, 5.1).

Status: the sandbox does not start on the machine this was built on (Ubuntu 24.04, AppArmor
restriction on user namespaces), so it ships switched off and its configuration is untested.

## 4. Keep the always-loaded instructions short, and prune them

Template: `AGENTS.md` is a skeleton under 50 lines with four sections (checks, how work is
tracked, gotchas, memory). The repository's own check fails if it passes 100 lines.

Why: Anthropic removed over 80% of Claude Code's own system prompt for current models with no
measured loss, and says to drop emphasis words, "think carefully" lines and mandatory rituals
(`notes/anthropic-claude-dev-blog.md` (b)). The docs target under 200 lines, list what to leave
out (architecture tours, anything the agent can find by reading), and say emphasis makes the
model over-apply a rule (`notes/claude-code-docs-extending.md` 1.3, 1.10). OpenAI's harness
team settled at about 100 lines that act as a map (`notes/industry-practices.md`, finding 1).
Boris Cherny's advice is to delete instruction files, skills and hooks every six months and
re-add only what the model still gets wrong (`notes/talks-anthropic-and-others.md`, finding 2).

Status: judgement call on the exact size. One dissent is recorded: Steinberger's 800-line file
(`notes/industry-practices.md`, finding 1). At the other end, Cherny said in October 2026 that
he no longer uses a custom `CLAUDE.md` at all (`notes/x-posts.md`, his setup over time).

## 5. One instruction file for every harness

Template: `AGENTS.md` holds the text. `CLAUDE.md` is one line, `@AGENTS.md`.

Why: Codex and OpenCode read `AGENTS.md`; Claude Code reads it directly only when no
`CLAUDE.md` exists, and the docs recommend the import as the portable way to share one file
(`notes/claude-code-docs-extending.md` 1.5; `notes/harness-codex-opencode-standards.md`,
finding 1).

Status: the import was observed working under Claude Code (the headless session followed a rule
that exists only in `AGENTS.md`). Codex and OpenCode behaviour is from their documentation.

## 6. Skills are small, single-purpose, and described by when to use them

Template: eleven skills, each in one category. Descriptions name the situations and phrases
that should trigger them. Each has a Gotchas section meant to grow. Four can only be started by
the user (`kickoff`, `dream`, `careful`, `lock-tests`), so they cost nothing in context until
used; seven are listed to the model.

Why: Anthropic's skills post: a skill should fit one category, the description is a trigger and
not a summary, the Gotchas section is the highest-signal content, and verification skills had
the most measurable impact (`notes/anthropic-claude-dev-blog.md` (a)). Every skill's description
is loaded in every session and overflow is silently truncated
(`notes/devcon-1-skills-context-memory.md` (a); `notes/claude-code-docs-extending.md` 2.10). A
Stanford study found the model did what a skill said 55% of the time without the skill being
loaded, so a skill that restates default behaviour is wasted context
(`notes/devcon-1-skills-context-memory.md` (e)).

Status: Claude Code's validator passes all eleven. A live session, run when there were eight,
listed the five model-invocable ones and hid the three user-only ones; `kickoff`, `write-tests`
and `performance` were added later and have not been used. None has an eval yet, which the same
sources say is the real test (principle 12). There is a serious case for fewer still: Lopopolo
reports "Zero skills in my repos", and that his team saw lower token use and higher eval scores
after deleting hundreds of skills in favour of a few plus docs (`notes/x-posts.md`, "Skills").
Delete any of these that does not change what the model does.

## 7. Tests are the judge, and the judge is protected

Template: the workflow says to write the failing test first for a bug. `/lock-tests` blocks
edits to test files for the rest of a session. The reviewer treats an edited existing test as a
finding.

Why: Anthropic's playbook: commit the failing test, then block test edits with a hook
(`notes/anthropic-claude-com-org-and-cases.md`, finding 6). Tests written from the code only
confirm the code does what it does, and "passes the tests but is still wrong" is a commonly
reported failure (`notes/devcon-2-harness-specs-verification.md`, finding 3).

Status: the lock is unit-tested, not exercised in a live session.

## 8. The writer does not grade its own work

Template: the `reviewer` agent and the `second-opinion` skill. The reviewer gets the task and
the base branch, not the author's summary, and is told to try to show the change is wrong. Three
rounds at most.

Why: Anthropic's security team found that agents asked to both find and verify filtered out
true positives (`notes/anthropic-claude-com-org-and-cases.md`, finding 7). Giving a reviewer
the base branch instead of the diff made it more critical; a single agent with ten requirements
skipped some (`notes/devcon-2-harness-specs-verification.md`, finding 4). Anthropic caps review
rounds at three after one pull request looped more than fifty times
(`notes/anthropic-claude-dev-blog.md` (h)).

Status: judgement call on when to use it, and the practice itself is disputed. It is expensive:
in Anthropic's one direct comparison a full planner, generator and evaluator harness cost about
twenty times a solo run (`notes/anthropic-engineering.md`, finding 3). The Claude Code team
promoted adversarial review through August 2026; by November Thariq Shihipar, after leaving
Anthropic, endorsed the view that it is mostly a waste of tokens next to empirical and formal
verification, and OpenAI's Ryan Lopopolo argues for collaborative review instead
(`notes/x-posts.md`, "Adversarial review"; `posts/x/2117670540148347273`). So the workflow asks
for a second opinion only on tasks that needed a plan, and principle 1 (a check the agent can
run) comes first. The reviewer has shell access because it must run checks, so "does not edit"
is an instruction to it, not a restriction.

## 9. State lives in files and the tracker, not in the conversation

Template: `WORKFLOW.md`, the task format, `docs/plans/` for a task in flight, handoff notes on
the task, and the `wrap-up` skill.

Why: `notes/task-backlog-epic-management.md`, findings 1, 2 and 9, drawing on Anthropic's and
OpenAI's long-running harnesses. See `docs/tasks.md`.

Status: the file tracker's selection script is tested. The GitHub path was checked only for its
read query. The workflow as a whole has not been run end to end on a real task.

## 10. Memory is plain files, and it is corrected out of band

Template: `.agents/memory/`, the inbox, the `dream` skill and its two agents.

Why: see `docs/memory-and-dreaming.md`.

Status: see that file for what the end-to-end run showed.

## 11. Loops need a stop condition and a cap

Template: no loop is configured to run on its own. `docs/loops.md` gives the forms to type.

Why: Anthropic's loops article: every loop type has a stop condition, deterministic criteria
work best, and a turn cap bounds cost (`articles/claude.com/resources-articles-getting-started-with-loops`).
A stop hook that cannot pass must not trap a session, which is why `stop-check.py` lets the
agent stop after one forced continuation.

Status: described from documentation. The stop hook's behaviour was run in a scratch
repository.

## 12. Treat this setup as code that rots

Template: the repository checks itself (`scripts/agent/check`), `tools/refs watch` reports new
and changed sources, and `docs/keeping-current.md` sets a review rhythm.

Why: harness parts go stale as models improve; Anthropic removed pieces of its own harness
within months (`notes/anthropic-engineering.md`, finding 1). Skills rot the same way and need
lint, evals and owners (`refs/videos/KpfnldjO3Iw/transcript.md`, from 15:23). A controlled
experiment found a behavioural harness took a cheap model from 3 of 10 to 10 of 10 and did
nothing for a frontier model except cost about seven times as much (`notes/industry-practices.md`,
finding 4).

Status: there are no evals for the skills here. That is the largest gap between this template
and what its sources recommend.

## What was left out on purpose

- **Stack rules** (React, Next.js, databases and so on). The docs say to write down only what
  the agent cannot find, and none of the sources supports shipping generic language advice.
  Add path-scoped rules in a project when a correction repeats.
- **Role-named subagents** (planner, architect, tester). Several independent teams found them
  unhelpful; subagents earn their cost through context isolation and independent review
  (`notes/industry-practices.md`, finding 5; `notes/anthropic-claude-com-practice.md` (e)).
- **A spec framework.** No frontier team in the corpus uses one as its process
  (`notes/task-backlog-epic-management.md`, "What frontier teams say they do").
- **MCP servers.** A CLI plus a few lines of usage beat an MCP server in six independent
  accounts, and connected servers cost context when idle (`notes/industry-practices.md`,
  finding 5). Add one per project when there is no CLI.
- **Cross-project sync.** Decided by the owner. The corpus also has no worked example of it
  (`notes/devcon-3-teams-org-brownfield.md`, gaps).
