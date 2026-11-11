# Task, backlog, epic, spec and progress-state management for a solo developer running coding agents

Date written: 2026-11-10. Question: how should a solo full-stack developer with about a dozen repos, working mainly in Claude Code and also in Codex and OpenCode, keep tasks, backlog, epics, specs and progress state so that work survives sessions, agents can take the next task unattended, and the human keeps oversight.

Sources read: 58 in full (30 assigned corpus items, 8 further corpus items, 20 pages fetched today), plus 8 read only in the relevant section (marked "Read status" or "partial reads" in their entries).
Not read or not fetched:
- OpenAI Symphony `SPEC.md`: embedded in the saved article as one 52 KB line; only sections 1, 2, 4.1.1, 5.3.1 and 8.2 were extracted and read.
- Tessl's spec-driven framework: `https://docs.tessl.io/introduction-to-tessl/concepts` returned 404; only the docs home page was read, and it no longer describes a spec framework.
- BMAD story and epic file formats, Linear "coding sessions", GitHub Agentic Workflows documentation, Kiro sub-pages: not fetched.
- Corpus items that matched the Part A grep but were not read are listed at the end of the per-source section (notably Gas Town, the Cursor posts and the HumanLayer context-engineering essay). Nothing below relies on them.
- Nothing was tested end to end. The only local checks were `gh --version` and `gh issue create --help` (see finding 12).

Short source keys used below: A-harness25, A-harness26, A-sci, A-cc, A-mem, A-loops, A-sdlc, A-org (Anthropic posts); CC-goal, CC-projects, CC-sched, CC-routines, CC-teams, CC-workflows, CC-sessions, CC-memory, CC-tools (Claude Code docs); AC-quickstart (Anthropic autonomous-coding prompts); OAI-harness, OAI-plans, OAI-symphony, Lopopolo (OpenAI); Huntley, Horthy (Ralph); Yegge, Beads-README, TW-radar, GasCity (Beads); Böckeler, Eberhardt, Uvik (critiques and benchmark); Martinelli, Azriel, Batey, Burrows, Syme (talks); Backlog.md, SpecKit, OpenSpec, Kiro, BMAD, Taskmaster, Linear, GH-issues, GH-agents, OC-docs (tools).

## Cross-cutting findings

1. Durable state must live outside the conversation, in something a fresh session can read in its first minute; compaction and session resume are not enough. (A-harness25, A-harness26, A-sci, OAI-plans, OAI-harness, Yegge, CC-sessions)
2. One task per context window, ending in one commit or PR, is the most repeated rule in the whole set. (A-harness25, AC-quickstart, Huntley, Horthy, Backlog.md, Yegge, A-sdlc)
3. "Done" has to be defined before work starts as individually checkable behaviour, and decided by something other than the agent that did the work. (A-harness26, CC-goal, A-loops, Azriel, OAI-plans, A-sdlc, AC-quickstart)
4. Agents mark work complete too early and then trust their own mark; status fields set by the worker need a second check. (A-harness25, A-mem, CC-teams, Yegge, A-cc)
5. The two frontier teams that published details ended up with a split: the tracker holds what to do and its state, the repository holds how to work and what was decided. (OAI-symphony + OAI-harness; A-sdlc + routines examples; Syme; GasCity; TW-radar)
6. For unattended selection the working recipe is a deterministic filter and sort (eligible state, not claimed, no open blocker; priority, then age), not model judgement. (OAI-symphony, Beads-README, AC-quickstart; Huntley is the exception)
7. The human gate is the pull request and, before that, the act of marking a task ready; humans stay out of the middle. (Syme, A-sdlc, OAI-symphony, CC-projects, Backlog.md, Lopopolo)
8. Verification evidence belongs on the PR as output, screenshots or video, because the reviewer and the `/goal` evaluator can only judge what is shown. (Lopopolo, OAI-harness, OAI-plans, A-sdlc, CC-goal, AC-quickstart)
9. A per-task plan with a progress log, discoveries (including failed approaches) and decisions is the handoff artifact that works across harnesses, because it is plain markdown. (OAI-plans, A-sci, A-cc, A-harness26, Backlog.md)
10. Markdown plan trees rot when they nest, multiply or outlive their task; every positive report uses one plan per task with one owner. (Yegge, Böckeler, Eberhardt, Batey on ADR bloat, A-mem on small memory)
11. Full spec workflows pay on multi-file features and cost more than they return on bug fixes and small changes; size the process to the task. (Uvik, Böckeler, Eberhardt, BMAD, SpecKit, Kiro, Burrows)
12. GitHub Issues gained native sub-issues (8 levels, 100 per parent) and blocked-by relations with `gh` flags and JSON fields, but the `gh` 2.88.1 installed on this machine does not have those flags yet. (GH-issues, local check)
13. In-session todo tools are being retired: Claude Code leaves the Task tools out by default on models newer than Opus 4.7, and OpenCode V2 turns todos off by default. (CC-tools, OC-docs)
14. Cloud and scheduled runs see only what is pushed: they start from a fresh clone of the default branch, and Claude project threads load `CLAUDE.md` and root rules but not repo skills, hooks, settings or `.mcp.json`. (CC-routines, CC-sched, CC-projects)
15. One person can supervise about three concurrent agent sessions; beyond that the work has to be pulled from a queue and reviewed as PRs. (Lopopolo, OAI-symphony, Yegge, A-sdlc, Batey)
16. Agents should file discovered work as new items for later triage instead of widening the current task or dropping it. (OAI-symphony, Yegge, Huntley)
17. Scaffolding goes stale as models improve: sprint decomposition, context resets and written checklists were each removed within months. Keep the system small and re-test it at each model release. (A-harness26, CC-tools, Eberhardt, A-org, OAI-symphony)
18. Architectural decisions deserve their own short, human-reviewed record ahead of implementation; they are the documentation that keeps its value. (Batey, Eberhardt, OAI-harness)

### Contradictions and open questions

- Tracker versus files. Yegge: "GitHub Issues doesn’t work" and markdown plans are a "colossal" mistake. OpenAI: execution plans "checked into the repository". Huntley: one `fix_plan.md`. Anthropic's experiments: JSON and text files. The reports are compatible if the unit differs: Yegge's failure was hundreds of nested plan files as the backlog; OpenAI's plans are one per piece of complex work, and the same team later put the backlog in Linear. (Inference.)
- Who picks the next task. Huntley trusts the model to "choose the most important thing"; Symphony and Beads compute it; Anthropic's quickstart takes the first failing entry in a priority-ordered file.
- Tests versus specs as the check. Azriel says generated tests cover "imaginary scenarios" and verifies against the ticket in a running preview; Carlini, the SDLC playbook and Farley make tests the oracle. Both agree the check must be independent of the implementer.
- Is spec-driven development waterfall? Eberhardt and Böckeler: in practice yes for Spec Kit as of late 2025. Martinelli and OpenSpec: no, if you go one small unit at a time. Uvik's numbers suggest the answer depends on ticket size.
- Review gate. OpenAI's harness team runs with "minimal blocking merge gates" and agent-to-agent review; GitHub Next, Anthropic's playbook and Backlog.md keep a human PR gate. For a solo developer who also owns production, the sources give no reason to drop the human gate.
- Keep plans after merge? OpenAI keeps "completed plans" versioned; Eberhardt says specs "lack much value once the feature is complete"; Yegge shows what unbounded retention looks like. Unresolved.
- No source measures tracker choice (issues, files, Beads, Linear) against outcomes. The only controlled numbers found (Uvik) compare spec workflows, come from a vendor, and are mostly inside their own noise band.

## Comparison of the options

"?" means the sources read do not say. Cells without a key are direct readings of the tool's own page listed in the row.

Table A: storage and agent interface

| Option | Where state lives | Format | How an agent reads, claims, updates | Dependencies and epics |
|---|---|---|---|---|
| GitHub Issues + sub-issues + `gh` (GH-issues, GH-agents) | github.com, per repo | Issue body and comments (markdown), labels, assignee, relations | `gh issue list --label … --json …`; claim by assignee or label (not atomic, GasCity); update by comment, label, linked PR | Sub-issues to 8 levels; `--blocked-by` / `blockedBy` JSON; needs a newer `gh` than 2.88.1 (local check) |
| Linear + MCP + agents (Linear, OAI-symphony) | Linear cloud workspace | Issues, statuses, priority, relations | Hosted MCP (`mcp.linear.app/mcp`) or API; delegate by assigning to an agent; Symphony polls and dispatches | Parent and sub-issues, blocked/blocking (GasCity); priority integer (OAI-symphony) |
| Backlog.md (Backlog.md) | `backlog/` folder in the repo | One markdown file per task with acceptance criteria, DoD, plan, notes | `backlog task list --json`, `task edit`; CLI or MCP; no claim command described | Dependencies and milestones; no epic entity named |
| Beads `bd` (Beads-README, TW-radar) | Dolt database under `.beads/`, synced to `refs/dolt/data` | SQL rows; JSONL export only | `bd ready`, `bd update <id> --claim` (atomic), `bd close` | Typed dependency edges; hierarchical IDs `bd-a3f8.1.1` |
| Spec Kit (SpecKit, Böckeler) | Spec folder and branch per feature in the repo | Several markdown files per feature | Skills `/speckit-specify` … `/speckit-converge`; no backlog or claim | Tasks inside one feature only |
| OpenSpec (OpenSpec, Uvik) | `openspec/changes/<name>/`, archived into `openspec/specs/` | `proposal.md`, delta specs, `design.md`, `tasks.md` | `/opsx:propose`, `/opsx:apply`, `/opsx:archive`; checklist in `tasks.md` | Checklist order only; cross-repo "Stores" in beta |
| Kiro specs (Kiro, Böckeler) | `.kiro/specs/` in the repo (Uvik) | `requirements.md` or `bugfix.md`, `design.md`, `tasks.md` | Kiro runs `tasks.md`, marks in-progress and completed | Dependency graph inside one `tasks.md`, run in waves |
| BMAD (BMAD, Uvik) | Project docs folder (Uvik) | Tech spec, or PRD + architecture + story files (Uvik) | Skills (`bmad-build`); "BMad Loop" for a whole epic | Epics and stories; format not read |
| Taskmaster (Taskmaster) | `.taskmaster/` in the repo | PRD text parsed into tasks; file format not shown in README | MCP `next_task`, `set_task_status`; CLI `task-master next` | Dependencies, subtasks, tags as workstreams |
| OpenAI ExecPlan / `PLANS.md` (OAI-plans, OAI-harness) | One markdown file per complex task in the repo | Prose plan with `Progress`, `Decision Log`, `Surprises & Discoveries` | Agent reads the file, ticks timestamped checkboxes, appends logs, commits | None across plans; milestones inside a plan |
| Anthropic feature list (A-harness25, AC-quickstart) | `feature_list.json`, `claude-progress.txt`, `init.sh`, git | JSON array (`category`, `description`, `steps`, `passes`) + text log | `cat` the files; take first `"passes": false`; flip only `passes` | None; order in file is priority |
| Ralph `fix_plan.md` (Huntley) | `fix_plan.md`, `specs/*`, `AGENT.md` | Prioritised bullet list | Whole file loaded each loop; model picks; removes finished items | None |
| Claude Code Task tools and agent-team list (CC-tools, CC-teams) | `~/.claude/tasks/<name>/` on one machine | Internal task records | `TaskCreate/Get/List/Update`; file-locked self-claim in teams | States pending, in progress, completed; `blocked` by dependency |
| Claude Code Projects (CC-projects) | Anthropic cloud, per user | Conversation, threads, memory files | You paste tasks; the coordinator starts a thread per task | None described |

Table B: oversight, portability, maturity, failure modes

| Option | Human visibility | Offline / in-repo | Works from Claude Code, Codex, OpenCode | Maturity | Known failure modes |
|---|---|---|---|---|---|
| GitHub Issues | Web, mobile, Projects boards with blocked icon and parent grouping (GH-issues) | No / no | Yes through `gh`; all three also start from issue or PR comments (`@claude`, `/oc`), and issues can be assigned to Claude or Codex agents (GH-agents, OC-docs) | Core product; sub-issue CLI flags recent; third-party agents in public preview | No atomic ready-and-claim (GasCity); deleted issues are gone (GasCity); agent-filed churn can bury the human (GasCity); task text is not versioned with code |
| Linear | Fast UI, mobile, views by Delegate (Linear) | No / no | MCP in each harness; cloud Claude threads via connectors (CC-projects) | Mature; Symphony itself is an unmaintained reference (OAI-symphony) | Second system; MCP reconnects (Linear); "lost the ability to constantly nudge them mid-flight" (OAI-symphony) |
| Backlog.md | Terminal board, local web UI on `127.0.0.1`, files in git | Yes / yes | Yes via CLI instructions or MCP; CLI must be installed in every environment | v1.52.0 installed locally; self-dogfooded | Task state can differ between branches (config `checkActiveBranches` exists for this); no cross-repo view; hand edits can break metadata |
| Beads | No built-in board; community UIs | Yes / in the repo directory but in Dolt, not plain files | `bd setup claude`, `bd setup codex`, others | 1.0; Thoughtworks Trial (TW-radar) | "heavier than the lightweight tracker it started as"; pin one version per shared store; schema migrations (TW-radar); agents have deleted the database (Yegge) |
| Spec Kit | Markdown review | Yes / yes | 30+ agents (Uvik) | 1.0 in 2026 | "a sea of markdown", about ten times slower for one tester (Eberhardt); agent ignored or over-followed instructions (Böckeler); spec drift 12.5% (Uvik) |
| OpenSpec | Markdown review; dashboard screenshot | Yes / yes | 25+ tools (Uvik) | Active; Stores beta; telemetry on by default | Checklist is per change, not a backlog; lowest drift in Uvik (2.4%) but vendor data |
| Kiro specs | Kiro IDE task UI, markdown review | Yes / yes | Kiro IDE and CLI only (Uvik) | Commercial product | Small bug became 16 acceptance criteria in 2025 (Böckeler); since added Bugfix and Quick Spec (Kiro) |
| BMAD | Markdown review | Yes / yes | Claude Code and Codex plugins | v6.12 stable, v7 alpha with breaking changes | Highest cost and longest spec phase in Uvik; lowest "would use again" |
| Taskmaster | CLI lists | Yes / yes | MCP or CLI | Widely used; Commons Clause licence; docs on a vendor site | 36 tools cost about 21,000 tokens by default; needs its own model access |
| ExecPlan | Read the file or the PR diff | Yes / yes | Yes, plain markdown; `AGENTS.md` pointer | Used by OpenAI on a million-line repo (OAI-harness) | Not a queue; decays if plans multiply (Yegge) |
| Anthropic feature list | Count of `"passes": false`; git log | Yes / yes | Yes, plain files | Research demo, greenfield | Agents delete or rewrite entries unless forbidden; marks passing without real testing (A-harness25) |
| Ralph `fix_plan.md` | Watch the file "like a hawk" (Huntley) | Yes / yes | Any CLI agent in a shell loop | Folk technique | Broken codebase overnight; duplicate implementations; author says not for existing codebases (Huntley) |
| Claude Code Task tools | `Ctrl+T` list in one session | Local only / no | Claude only | Off by default on newer models; agent teams experimental | "Task status can lag"; lost on another machine; not in the repo (CC-teams, CC-tools) |
| Claude Code Projects | Overview pane: Ready for review, Waiting on you, Working (CC-projects) | No / no | Claude only | Public beta, Pro/Max/Ultra, not in the CLI | Tracks threads, not unstarted work; repo hooks and skills not loaded; uncommitted work can be lost |

## What frontier teams say they do

Anthropic, research harnesses (files in the repo):
- The 2025 harness: the first session writes "an `init.sh` script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit" (A-harness25, "The long-running agent problem").
- Each later session is told to "Read the features list file and choose the highest-priority feature that’s not yet done to work on." (A-harness25, "Getting up to speed")
- Scientific computing: "The progress file, which by convention we call here CHANGELOG.md, is the agent’s portable long-term memory" (A-sci, "Memory across sessions").
- C compiler, 16 agents: "Claude takes a "lock" on a task by writing a text file to current\_tasks/" (A-cc, "Running Claude in parallel"). The author adds: "nor do I enforce any process for managing high-level goals."
- 2026 harness: "Communication was handled via files"; and later, "I started by removing the sprint construct entirely." (A-harness26)

Anthropic, product and internal practice (tracker and PRs):
- Launch example for routines: "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR." (introducing-routines article)
- `/goal` use case: "Working through a labeled issue backlog until the queue is empty" (CC-goal).
- Claude Code team: "Our planning ritual shifted away from design docs toward discussions in PRs or prototypes." (A-org)
- Applied AI playbook: "Each stage ends by writing one to version control ... and the next stage begins by reading it." (A-sdlc; the artifacts are `intent.md`, `spec.md`, `plan.md`, the diff, the PR)

OpenAI (plans in the repo, then a tracker as control plane):
- "Plans are treated as first-class artifacts." and "Active plans, completed plans, and known technical debt are all versioned and co-located" (OAI-harness).
- An ExecPlan must let work "restart from _only_ the ExecPlan and no other work." (OAI-plans)
- Later, the same team: "Software workflows are largely organized around deliverables: issues, tasks, tickets, milestones." (OAI-symphony, "A shift in perspective")
- Symphony "turns a project-management board like Linear into a control plane for coding agents." Its first version "was just a Codex session running in `tmux`, polling Linear and spawning sub-agents for new tasks." (OAI-symphony)
- The process moved into a file: the workflow "is now captured in a simple `WORKFLOW.md` file." (OAI-symphony)

GitHub Next (issues and PRs as the shared fabric):
- Agentic workflows "don't ever merge pull requests"; output channels are narrow, for example "allowed to create one issue" (Syme `[14:29]`, `[15:30]`).

Practitioners:
- Yegge: "Let’s just move all known work from the plans into an issue tracker." (Yegge, "It’s Issues All The Way Down")
- Thoughtworks on Beads: "many of our developers now use it by default with coding agents", alongside a team tracker (TW-radar).
- Huntley: "The TODO list is what I'm watching like a hawk. And I throw it out often." (Huntley, "the todo list")
- Batey (CECG): "only work on one complex task at a time" `[23:36]`.
- Martinelli: "we use the use cases in a Kanban way to track the progress. That's all we do." `[21:37]`
- Backlog.md's author: "one task = one context window = one PR."

Reading across these (inference): none of the frontier teams uses a spec framework product, and none uses the harness's built-in todo list as the record. Both Anthropic's and OpenAI's published trajectories go from files-only experiments on one greenfield repo to a tracker for the queue, the repo for the knowledge and the PR for the evidence, once several streams of real work run at once.

## Recommendation for this developer

Everything in this section is a recommendation built from the cited evidence. It has not been run. Parts marked "untested" depend on behaviour I could not verify.

### Primary system: GitHub Issues for the queue, the repository for knowledge, the pull request for evidence

One sentence: every piece of work is a GitHub issue; an issue becomes eligible for agents only when you label it `ready`; an agent works one issue on one branch and records proof on one PR; durable knowledge (workflow contract, specs for large work, decisions, an in-flight plan) is committed markdown.

Why this and not the alternatives:
- It is the shape both frontier teams converged on (finding 5), and the Beads vendor's own guide says "GitHub Issues may be enough" for a small team "whose planning already lives next to pull requests" (GasCity).
- It is the only store all three harnesses reach with no extra server: `gh` from any shell, `@claude` and `/oc` comment triggers, issue assignment to Claude or Codex agents, and Claude cloud triggers on Issue events (GH-agents, OC-docs, CC-routines). Backlog.md and Beads need their CLI installed in every environment, and Claude cloud threads do not load a repo's `.mcp.json` (CC-projects).
- Unattended cloud runs start from a fresh clone of the default branch (CC-routines). File-based task state changed on a feature branch is invisible to them until merged; issue state is not tied to a branch.
- It gives one view across a dozen repos (a GitHub Project) and works from a phone; Backlog.md's board is per repo on `127.0.0.1`, and Beads has no built-in board.
- Native sub-issues and blocked-by now cover the epic and dependency needs that drove Yegge away from it in 2025 (GH-issues; inference).
- You already use it in most repos; Linear would add a second product and an MCP dependency per harness for capabilities a solo developer does not need (Linear, GasCity).
Main trade-off: no offline work on the queue, task text is not versioned with the code, and there is no atomic claim. The mitigations are the committed plan file, a WIP cap of three, and a claim-then-recheck step. If you later run more than about three agents concurrently in one repo, the missing atomic claim becomes real and Beads is the documented answer (Beads-README, TW-radar).

### Hierarchy

- Epic: a parent issue labelled `epic`. Body: goal in one to three sentences, in scope, out of scope, exit criteria, link to `docs/specs/<slug>.md` if a spec exists. No code is written against an epic directly.
- Task: a sub-issue of an epic, or a standalone issue. Sized to one context window and one PR (finding 2). Two levels only; GitHub allows eight, but every extra level is another place for the "phase 3 of phase 3" drift Yegge describes.
- Acceptance criteria: a numbered list `AC1 … ACn` in the task body, each one behaviour plus the check that proves it.
Justification: "one task = one context window = one PR" (Backlog.md); "a ticket is basically a full feature now" (Burrows `[21:35]`); acceptance "phrased as behavior a human can verify" (OAI-plans).
Trade-off: epics on GitHub give you grouping and a progress count, not scheduling; ordering comes from priority labels and blocked-by.

### Task issue format

Use an issue form with these sections (seven of Uvik's eight checklist items; "inputs and outputs" folds into Context for web work):

    ## Goal
    One or two sentences: what a user or the system can do after this, and why.
    ## Context
    Files, routes, tables, prior issues or ADRs to read first. Enough that a fresh session needs nothing else.
    ## Acceptance criteria
    AC1. <behaviour>. Check: <command, test name, or UI step and expected result>
    AC2. ...
    ## Edge cases and data changes
    ## Constraints
    ## Out of scope / do not change
    ## Verify
    Exact commands for this repo (typecheck, lint, the relevant tests, UI check if any).

- Agents never edit the Goal or Acceptance criteria. If a criterion is wrong or impossible they comment, label `needs-human`, and stop.
- Small bug: the issue is just a reproduction, one AC ("the failing test `<name>` passes") and Verify.
Justification: specs covering six or more of eight checklist items merged 89.3% versus 60.0% (Uvik, weak evidence); a scheduled prompt "must be self-contained and explicit about what to do and what success looks like" (CC-routines); the feature list may be changed only in its `passes` field (A-harness25); Azriel's agents skipped requirements when ten to twenty were bundled, so keep criteria few and separately checkable.
Trade-off: writing checks up front costs you minutes per task; that is where your time goes instead of mid-task steering.

### When to write a spec, and where

- Default: the issue body is the spec.
- Write `docs/specs/<epic-slug>.md` only when three or more of these hold: touches three or more files; four or more acceptance criteria; crosses a module, service or repo boundary; changes a schema or public API; more than one agent will work on it (Uvik's fit test, minus the regulatory item).
- Keep it under roughly 150 lines (Uvik medians were 93 to 188) and product-level: the planner should not fix "granular technical details upfront" because spec errors "cascade into the downstream implementation" (A-harness26).
- A decision about architecture, data model or infrastructure goes first, alone, as an ADR in `docs/decisions/`, reviewed by you before implementation (Batey `[14:27]`).
- Do not adopt Spec Kit, Kiro, BMAD or Taskmaster as the process. If you want tooling for the large-feature case, OpenSpec is the lightest fit in the evidence (shortest spec phase and lowest drift in Uvik; delta specs archived into living specs), but that is optional and its evidence is one vendor benchmark.
Trade-off: spec-first only. You give up the spec-anchored promise of always-current specs; Böckeler and Eberhardt both doubt that promise pays.

### States

Open issue with no status label = inbox (not eligible). Then:

| State | How it is represented | Who sets it |
|---|---|---|
| Inbox | open, no status label (agent-filed ones also carry `agent-filed`) | anyone |
| Ready | label `ready` | you only |
| In progress | assignee set + label `in-progress` + branch `task/<number>-<slug>` | the agent that claims it |
| Needs human | label `needs-human` + a comment with the question | agent |
| In review | open PR whose body says `Closes #<number>` | agent opens, you review |
| Done | issue closed by the merged PR | you, by merging |

Other labels: `p0` to `p3` (priority), `epic`, `interactive` (ready, but do it with me in a live session; excluded from unattended runs).
Justification: Symphony's defaults are `Todo`, `In Progress`, a `Human Review` handoff and terminal states, with success meaning "reached the next handoff state" (OAI-symphony); Claude Projects groups by Ready for review, Waiting on you, Working (CC-projects); "Not every task fits the Symphony style of work", ambiguous problems stay interactive (OAI-symphony); the lead or a teammate "can stop early" and "Task status can lag" when workers own the done state (CC-teams).
Trade-off: labels are last-writer-wins and a misapplied label can start a run. Keeping `ready` human-only is the control.

### Definition of done and verification evidence

- Repo-level definition of done lives in `AGENTS.md` as a short "Verifying your work" block with the exact commands and the rule that their output is pasted, never summarised (A-sdlc's CLAUDE.md verification block).
- Task-level done = every AC met with its stated check.
- Evidence is recorded in the PR body, one line per criterion:

      ## Evidence
      AC1: `pnpm test tasks/claims.test.ts` -> 4 passed (output below)
      AC2: screenshot verification/123/status-412.png, console clean
      Definition of done: typecheck ok, lint ok, tests ok (last lines pasted)
      Not verified: <anything you could not check, and why>

- For a task that passed the spec test, a fresh-context reviewer agent checks the diff against the issue's criteria before you look, working from the base branch and the issue, not from the implementer's summary.
- The issue closes only when you merge. An agent never closes an issue or ticks its own criteria.
Justification: the agent "needs to convince me to merge its code" (Lopopolo `[22:39]`); "Capture evidence" (OAI-plans); "Run the tests before reporting a task complete, and show the output" and "an agent fixing code must not be able to weaken the check" (A-sdlc); the `/goal` evaluator "doesn't run commands or read files independently" (CC-goal); a separate evaluator is "far more tractable than making a generator critical of its own work" (A-harness26); give the reviewer the base branch because the diff biases it (Azriel `[14:29]`).
Trade-off: the evaluator adds cost and is "unnecessary overhead" for tasks the model does reliably alone (A-harness26), which is why it is limited to larger tasks.

### How an unattended loop selects the next task

Selection is a script, not a judgement call:
1. List open issues labelled `ready`.
2. Drop any with an assignee, or labelled `in-progress`, `needs-human`, `interactive` or `epic`.
3. Drop any with an open blocker.
4. Sort by priority label (`p0` first), then oldest created.
5. Take the first. Claim it: add assignee and `in-progress`, wait a few seconds, re-read the issue, and abandon the claim if another assignee appeared.
6. Do that one issue following `WORKFLOW.md`. Open a draft PR. Stop.

Sketch (untested; needs a `gh` with the `blockedBy` field, and the field's JSON shape is assumed):

    gh issue list --state open --label ready --limit 100 \
      --json number,title,labels,assignees,createdAt,blockedBy

then filter and sort with `jq`.

Three ways to run it, cheapest first:
- Local, one issue: `claude -p "/goal <condition>"` in a worktree, in auto mode. Condition template: "PR is open for issue #N, its Evidence section covers every AC, and the Verify commands' passing output is printed in this conversation; or the issue is labelled needs-human; or stop after 30 turns."
- Nightly per repo: a cloud scheduled task (or a local cron) whose prompt is steps 1 to 6 with "if nothing is eligible, say so and stop". One task per run.
- On demand from anywhere: label an issue and let an event trigger start a session, or comment `@claude` / `/oc`, or assign the issue to a coding agent on GitHub.
Justification: Symphony's eligibility and sort rules (OAI-symphony, SPEC 8.2); `bd ready` then claim (Beads-README); "Use scripts for deterministic work" (A-loops); "one item per loop" (Huntley); one small PR each morning "is better than ... waking up to 50" (Horthy); time-based loops stop when "the queue is empty" (A-loops); a goal needs "One measurable end state" and "A stated check" (CC-goal).
Trade-off: a deterministic queue does exactly what the labels say, so stale priorities produce stale work; and one task per run is slower than draining the queue, on purpose, to keep review within your capacity.

### Progress and handoff notes

- Small task: no plan file. The PR description and commits are the record.
- Multi-session or spec-tested task: one file `docs/plans/<number>-<slug>.md` on the task branch, an ExecPlan cut down to: Purpose; Plan of work; Progress (timestamped checkboxes, split a half-done step into done and remaining); Discoveries and dead ends; Decisions; Evidence. Update it and commit at every stopping point.
- At every session end without a PR, the agent pushes the branch and posts one issue comment: `Handoff: state / done / next step / blocked on / branch`. That comment is what you see on your phone and what the next session, in any harness, reads first with `gh issue view <n> --comments`.
- Session start ritual for any harness: read the issue and its comments, read the plan file if present, `git log --oneline -20` on the branch, run the Verify commands before changing anything.
- Out-of-scope findings become new issues labelled `agent-filed` with "Discovered while working on #N". They stay in the inbox until you triage them.
- A lesson that will recur goes into `AGENTS.md`, a rule or a lint, not into the plan.
- On merge, lift any lasting decision into an ADR and delete the plan file in the PR's last commit (git and the PR keep it).
Justification: `Progress`, `Decision Log`, `Surprises & Discoveries` and restartability (OAI-plans); failed approaches matter because "successive sessions will re-attempt the same dead ends" (A-sci); the ten-step session ritual (AC-quickstart); cloud sandboxes can lose uncommitted work (CC-projects); agents "file a new issue that we can evaluate and schedule later" (OAI-symphony); "DO NOT PLACE STATUS REPORT UPDATES INTO @AGENT.md" (Huntley); 605 decaying plan files (Yegge); a small curated memory beat 413 files (A-mem); "I never want to give the same review feedback twice" (Lopopolo).
Trade-off: deleting plans on merge loses greppable history in the tree; keeping them risks the rot Yegge describes. This choice is my inference, see the last section.

### Where the contract lives, and scaling to a dozen repos

- `AGENTS.md` in each repo, under 100 lines, with a five-line "How work is tracked here" section pointing to `WORKFLOW.md`, plus the verification block. Add a `CLAUDE.md` containing `@AGENTS.md` so Claude Code, Codex and OpenCode read the same text (CC-memory; OAI-harness for the map-not-manual rule).
- `WORKFLOW.md` at the repo root: the numbered loop above (start ritual, claim, plan when needed, implement, verify, PR with evidence, handoff), written as plain steps. Keep it out of skills, because Claude cloud threads load `CLAUDE.md` and root rules but not repo skills or hooks (CC-projects).
- One template repo holds the label set, the issue form, the PR template with the Evidence section, `WORKFLOW.md` and the `AGENTS.md` section. Copy to each repo; do not let them drift.
- One GitHub Project across all repos is your board: columns from the labels, grouped by parent issue, blocked icon visible (GH-issues). This is the backlog view. Claude's Projects Overview or `claude agents` is the in-flight view (CC-projects, agent-view article).
- Limits: at most three agent sessions running at once across all repos, and at most one task you would call complex (Lopopolo, OAI-symphony, Batey). At most one unattended PR per repo per night to start with (Horthy).
- Re-test the whole convention when a new model generation lands and delete whatever no longer earns its place (A-harness26).
Trade-off: a dozen copies of four files need a sync habit; the alternative, a shared planning repo (OpenSpec "Stores", beta), puts tasks away from the code and its PRs.

### Lighter fallback for tiny projects

For a prototype, a script repo, or anything with no remote: one committed file, `TASKS.md`.

    # Tasks
    Goal: <one sentence>
    ## Next (in order)
    - [ ] T1 <title>. Done when: <check>
    - [ ] T2 ...
    ## Log
    2026-11-10: did T1. Tried X, failed because Y. Next: T2.

- Rules: one item per session; the agent ticks an item only after showing the check's output; discovered work is appended at the bottom of Next, never done in passing; rewrite the list when it stops matching reality.
- Start prompt for any harness: "Read TASKS.md and the last 20 commits, do the first unchecked item, update the file, commit."
- Graduate to issues when any of these appears: more than about 20 open items, a need for unattended or cloud runs, a dependency between tasks, or a second repo involved.
- If you want a board and structured acceptance criteria without GitHub, Backlog.md (already installed here, 1.52.0) is the step between: it fits local-only repos and offline work, at the cost of per-repo visibility and a CLI needed in every environment.
Justification: Anthropic's own multi-day run used two markdown files and git, restarted with "Read CHANGELOG.md and pick up the next task" (A-sci); Huntley's single prioritised list that he throws out often; Anthropic's quickstart flips one field per verified item (AC-quickstart); Böckeler's "sledgehammer to crack a nut".
Trade-off: no dependencies, no claim, nothing visible off the machine, and a markdown checklist is easier for an agent to rewrite than JSON (A-harness25 chose JSON for that reason). Acceptable only while the list is short enough for you to read in full.

## What I am unsure about

- `gh` support: the docs show `--parent`, `--add-sub-issue`, `--blocked-by` and the `blockedBy`, `parent`, `subIssues` JSON fields; the installed `gh` 2.88.1 (2026-03-12) has none of them. I do not know the minimum version, the JSON shape of `blockedBy`, or whether a search qualifier can filter "not blocked" server-side.
- Claude cloud triggers on issues: the docs list Issue events (including labelled) as triggers but document filters only for pull requests. Whether a trigger can be limited to "label `ready` was added" is unknown; without that, an event-driven run needs its prompt to check the label and exit.
- Whether Claude cloud threads expand an `@AGENTS.md` import inside `CLAUDE.md`, or read `AGENTS.md` directly. The Projects page names only `CLAUDE.md`, `.claude/CLAUDE.md` and root `.claude/rules/`.
- Whether the GitHub-hosted Claude and Codex agents (assign an issue) require a Copilot plan, and how they treat repo instructions. The page says they "can be powered by your existing Copilot subscription".
- The non-interactive equivalents of `claude -p "/goal …"` in Codex and OpenCode were not checked; cross-harness portability here rests on plain files and `gh`, not on a tested loop in each tool.
- The claim race. For one person and three sessions the recheck is probably enough; I have no evidence either way.
- Plan files after merge (delete or keep) and whether current models need a per-task plan file at all for anything short of multi-day work. A-harness26 and the removal of the Task tools point towards "less than you think"; OAI-plans points the other way and is a year old.
- The strength of the spec evidence. Uvik is a single vendor study with a date inconsistency and gaps inside its noise band; Eberhardt is one person on one feature; Böckeler is a qualitative review from 2025. They agree in direction, which is why the recommendation is "selective", but none is strong.
- Linear versus GitHub Issues. The direct frontier evidence (Symphony, Anthropic's routine example) names Linear. Treating GitHub Issues as equivalent for a solo developer is my inference from feature parity, not something a source demonstrates.
- Beads successors. Gas Town was not read; I only know from TW-radar and the README that Beads moved to the `gastownhall` organisation and Dolt. Whether a lighter alternative (`ticket`, `tracer`, named by TW-radar) fits better was not investigated.
- Tessl's spec framework status, BMAD's file formats and Kiro's cross-spec features were not established.

## Per source

Part A is the existing corpus; Part B is pages fetched on 2026-11-10 into the `task-management`
collection. Quotes are verbatim from the saved files.

### Part A: corpus

### Effective harnesses for long-running agents (Anthropic, 2025-11-26)
File: refs/articles/anthropic.com/research-effective-harnesses-for-long-running-agents/article.md   URL: https://www.anthropic.com/research/effective-harnesses-for-long-running-agents
Thesis: Compaction alone does not carry a multi-context-window build. An initializer session writes the environment (feature list, `init.sh`, progress file, first commit) and every later session does one feature, verifies it end to end, commits, and writes a progress note.
Practices:
- Two observed failures without the scaffold: one-shotting (runs out of context mid-feature, leaving it "half-implemented and undocumented"), and a later session that "would look around, see that progress had been made, and declare the job done." ("The long-running agent problem")
- Initializer writes `init.sh`, `claude-progress.txt` and an initial git commit; the feature list for the claude.ai clone had "over 200 features", each an end-to-end user-visible behaviour, "all initially marked as “failing”". ("Feature list")
- The coding agent may edit the feature file only by flipping a `passes` field. JSON chosen over Markdown: "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files." ("Feature list")
- One feature at a time; commit with descriptive messages and write a summary to the progress file so git can "revert bad code changes and recover working states". ("Incremental progress")
- Session start ritual: `pwd`; "Read the git logs and progress files to get up to speed"; "Read the features list file and choose the highest-priority feature that’s not yet done". Then run `init.sh` and a basic end-to-end smoke test before new work. ("Getting up to speed")
- Marking complete without real testing was a major failure; explicit browser-automation testing "as a human user would" fixed most of it. ("Testing")
Evidence and numbers: 200+ feature entries; model was Opus 4.5 on the Claude Agent SDK. No quantitative comparison.
Tools and files named: `init.sh`, `claude-progress.txt`, feature list JSON with `passes` field, Puppeteer MCP, Claude Agent SDK, quickstart `anthropics/claude-quickstarts/autonomous-coding`.
Caveats: Greenfield web app only. Authors say it is unclear whether a single general agent or a multi-agent structure is better. Superseded in part by the 2026-03 post below (context resets dropped with Opus 4.5/4.6).
Relevance: high. It is the origin of the "list of verifiable items + progress log + init script + git" pattern.

### Harness design for long-running application development (Anthropic, Prithvi Rajasekaran per the post's first person; 2026-03-24)
File: refs/articles/anthropic.com/research-harness-design-long-running-apps/article.md   URL: https://www.anthropic.com/research/harness-design-long-running-apps
Thesis: A planner, generator and separately tuned evaluator beat a solo agent on multi-hour builds. As models improved (Opus 4.5 to 4.6) the sprint decomposition and context resets could be removed, but the planner and an independent evaluator kept paying for themselves.
Practices:
- Context reset versus compaction: a reset "provides a clean slate, at the cost of the handoff artifact having enough state for the next agent to pick up the work cleanly." ("Why naive implementations fall short")
- Self-evaluation is unreliable: agents "tend to respond by confidently praising the work"; a separate evaluator tuned to be sceptical is "far more tractable than making a generator critical of its own work". (same section)
- Planner stays at product level: specifying granular technical detail up front risks that "errors in the spec would cascade into the downstream implementation." ("The architecture")
- Sprint contract: before each chunk, generator and evaluator agree "what "done" looked like for that chunk of work before any code was written"; Sprint 3 alone had 27 criteria. ("The architecture", "Running the harness")
- Agents communicate through files: "one agent would write a file, another agent would read it and respond". ("The architecture")
- With Opus 4.6 the sprint construct was removed; the generator "ran coherently for over two hours without the sprint decomposition that Opus 4.5 had needed". ("Results from the updated harness")
- Principle: "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing". ("Iterating on the harness")
Evidence and numbers: the full harness was "over 20x more expensive" than the solo run but the solo run's core feature did not work; DAW build "about 4 hours and $124".
Tools and files named: Claude Agent SDK, Playwright MCP, sprint contract files, product spec.
Caveats: "Out of the box, Claude is a poor QA agent"; the evaluator needed several rounds of prompt tuning and still missed bugs. The evaluator "is not a fixed yes-or-no decision": it is overhead for tasks the model does reliably alone.
Relevance: high. Shows which task-management scaffolding became unnecessary within four months, and which (spec, acceptance criteria agreed first, independent verification) did not.

### Long-running Claude for scientific computing (Siddharth Mishra-Sharma, Anthropic, 2026-03-23)
File: refs/articles/anthropic.com/research-long-running-claude/article.md   URL: https://www.anthropic.com/research/long-running-claude
Thesis: A multi-day autonomous build needs a plan in `CLAUDE.md`, a progress file, a test oracle, and git as the coordination and monitoring channel.
Practices:
- Plan and deliverables live in `CLAUDE.md`, which "Claude can edit ... as it works". ("Draft a plan and iterate locally")
- Progress file `CHANGELOG.md` is "the agent’s portable long-term memory"; it tracks "current status, completed tasks, failed approaches and why they didn't work, accuracy tables at key checkpoints, and known limitations." Failed approaches matter: "without them, successive sessions will re-attempt the same dead ends." ("Memory across sessions")
- "Commit and push after every meaningful unit of work"; the author monitored progress by reading GitHub commits on a phone. ("Git as coordination", "The execution loop")
- Restart prompt is one line: "Read CHANGELOG.md and pick up the next task". ("The execution loop")
- Ralph loop used against "agentic laziness"; `/loop` and GSD named as similar. ("The execution loop")
Evidence and numbers: sub-percent agreement with reference CLASS after "a few days"; test coverage gaps noted.
Tools and files named: `CLAUDE.md`, `CHANGELOG.md`, tmux, SLURM, Ralph loop plugin, GSD (`gsd-build/get-shit-done`), `/loop`.
Caveats: single well-scoped task with a reference oracle; "not production-grade".
Relevance: high. Smallest working version of in-repo progress state: two markdown files plus git.

### Building a C compiler with a team of parallel Claudes (Nicholas Carlini per the linked repo; Anthropic, 2026-02-05)
File: refs/articles/anthropic.com/research-building-c-compiler/article.md   URL: https://www.anthropic.com/research/building-c-compiler
Thesis: 16 parallel agents in an infinite loop built a 100,000-line compiler with no orchestrator; what mattered was the verifier quality and a trivial file-based task lock.
Practices:
- Task claiming: "Claude takes a "lock" on a task by writing a text file to current\_tasks/"; if two agents claim the same task, "git's synchronization forces the second agent to pick a different one." ("Running Claude in parallel")
- No orchestrator and no high-level goal management: "I leave it up to each Claude agent to decide how to act." Agents pick "the “next most obvious” problem". (same)
- Agents were told to "maintain extensive READMEs and progress files that should be updated frequently with the current status." ("Put yourself in Claude’s shoes")
- "it’s important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem." ("Write extremely high-quality tests")
- Parallelism only works when work is separable: on the single giant kernel task "Every agent would hit the same bug ... and then overwrite each other's changes." ("Make parallelism easy")
Evidence and numbers: nearly 2,000 sessions, about $20,000, 2 billion input tokens, 99% pass on most compiler test suites.
Tools and files named: `current_tasks/` lock files, bare git repo at `/upstream`, Docker, `--fast` test sampling.
Caveats: "very early research prototype"; "it is easy to see tests pass and assume the job is done, when this is rarely the case."
Relevance: medium. A dozen-repo solo developer rarely runs 16 agents on one repo, but the claim-by-file mechanism and "the test suite is the backlog" idea transfer.

### The components of agent memory (Anthropic, 2026-11-06)
File: refs/articles/anthropic.com/research-components-of-agent-memory/article.md   URL: https://www.anthropic.com/research/components-of-agent-memory
Thesis: Newer models judge what is worth writing down far better than old ones; small, curated memory beats exhaustive logs, and an offline "dreaming" pass corrects and reorganises notes.
Practices:
- Small beats large: Sonnet 3.7 wrote "413 memory files across 225 folders and earned one badge"; Fable 5 "wrote nine files in two folders, plus a single top-level file called `global.md`, and earned four badges." ("Claude has learned to judge salience")
- Store what cannot be re-read from the environment: state visible on screen is redundant, while "strategy, plans, and tested rules exist only if Claude works them out". (same)
- A top-level dashboard file holding "the current goal, a prewritten plan ... and the model’s own rules for using memory". (same)
- Do not over-prescribe: with "record only failures", Opus 5 and Opus 4.7 "lost much of the performance boost that memory gave them". ("Steering Claude to write memory")
- Wrong notes get trusted: a note "Mt Moon DONE" written in error sent later sessions the wrong way until a dreaming pass checked it against the transcript. ("Dreaming can correct memory")
- Shared tables written by several agents lost data "because agents had overwritten one another’s work"; one page per item written by a single agent fixed it (72% to 100% of criteria). ("Dreaming can focus memory on a specific goal")
Evidence and numbers: wiki+search 61% vs search alone 53% on an internal corpus; injected layer limited to "the first 200 lines or 25 KB of `MEMORY.md`".
Tools and files named: `global.md`, `MEMORY.md`, Claude Managed Agents memory directory, dreaming, CL-Bench 1.0.
Caveats: benchmarks are games and document QA, not backlog management. Inference: the failure of a wrongly written DONE note maps directly onto task status fields that agents set themselves.
Relevance: high for progress-note design (short, curated, one file per item, verify "done" against ground truth).

### How we built our multi-agent research system (Anthropic, 2025-06-13)
File: refs/articles/anthropic.com/research-multi-agent-research-system/article.md   URL: https://www.anthropic.com/research/multi-agent-research-system
Thesis: Orchestrator-worker research works by spending tokens in parallel; delegation needs explicit task descriptions and results should persist outside the conversation.
Practices:
- A delegated task needs "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." ("Prompt engineering and evaluations", item 2)
- Agents "summarize completed work phases and store essential information in external memory before proceeding to new tasks." (Appendix, "Long-horizon conversation management")
- Evaluate end state, not the path: "evaluate whether it achieved the correct final state." (Appendix)
Evidence and numbers: multi-agent uses "about 15× more tokens than chats"; "most coding tasks involve fewer truly parallelizable tasks than research".
Caveats: 2025, research not coding.
Relevance: low to medium. Supports "a task file must be self-contained" and a caution against parallelising coupled coding tasks.

### Loop engineering: Getting started with loops (Delba de Oliveira, Michael Segner; Anthropic, 2026-06-30)
File: refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md   URL: https://claude.com/resources/articles/getting-started-with-loops
Thesis: Four loop types (turn-based, goal-based `/goal`, time-based `/loop` and `/schedule`, proactive) differ by trigger and stop condition; pick the simplest.
Practices:
- `/goal` needs checkable exit criteria: "deterministic criteria, such as number of tests passed or clearing a certain score threshold, are so effective." ("Goal-based loop")
- Time-based loops stop when "the work completes (the PR merges, the queue is empty)". ("Time-based loop")
- Proactive loops suit "Recurring streams of well-defined work: bug reports, issue triage, migrations, dependency upgrades". ("Proactive loops")
- "Use a second agent for code reviews: A reviewer with fresh context is less biased". ("Maintaining code quality")
- "Pilot before a large run" and set turn caps ("stop after 5 tries"). ("Managing token usage")
Tools and files named: `/goal`, `/loop`, `/schedule`, dynamic workflows, auto mode, `SKILL.md`, `/usage`, `/workflows`.
Caveats: says nothing about where the queue itself is stored. Inference: every loop type presupposes an external queue (channel, issue list, PR) the loop can test for emptiness.
Relevance: high for the "unattended loop selects next task" requirement.

### The AI-native SDLC playbook (Louis Claxton, Anthropic Applied AI, 2026-08-21)
File: refs/articles/claude.com/resources-articles-the-ai-native-sdlc-playbook/article.md   URL: https://claude.com/resources/articles/the-ai-native-sdlc-playbook
Thesis: Each SDLC stage should end by committing an artifact to version control and the next stage should start by reading it; humans review at the gates.
Practices:
- The artifact chain is `intent.md`, `spec.md`, `plan.md`, the diff and tests, the PR with findings, the incident record: "Each stage ends by writing one to version control ... and the next stage begins by reading it." ("The shifts across the six stages")
- `intent.md` template headings: Problem, Proposed outcome, Affected users and systems, Constraints, Open questions; with `Author` and `Status: draft`. ("Capture as intent.md")
- `plan.md` template headings: Files that change, Order of work, Risks, Proof. Iterate "until an engineer who has never seen the conversation could implement the change from the plan alone." ("Claude Code plan mode as the default starting point")
- "When implementation departs from the plan, update `plan.md` in the same commit. Consider using a hook to enforce synchronization". (same)
- Verification is part of done: "Run the tests before reporting a task complete, and show the output." ("Give Claude a feedback loop")
- Protect the check: "an agent fixing code must not be able to weaken the check on that code." (same)
- Parallel ceiling: "The practical ceiling is how many streams one person can review properly". ("Parallel sessions and subagents")
- Existing tracker stays system of record where auditors expect it (export CSV/Markdown or webhooks). ("Recurring codebase scans", step 8)
Tools and files named: `intent.md`, `spec.md`, `plan.md`, `REVIEW.md`, `CLAUDE.md`, `.claude/agents/verifier.md`, `bands.yaml`, `claude -p`, claude-code-action, Claude Tag, Code Review.
Caveats: written for regulated enterprises with separate product owner, tech lead and release manager roles. It names no backlog or epic structure at all; tickets appear only as one entry route into `intent.md`.
Relevance: high. Strongest corpus statement that specs and plans are committed files, and the PR is the evidence record.

### Product development in the agentic era (Jess Yan, Anthropic, 2026-04-29)
File: refs/articles/claude.com/resources-articles-product-development-in-the-agentic-era/article.md   URL: https://claude.com/resources/articles/product-development-in-the-agentic-era
Thesis: A PM builds one-off Managed Agents for operational jobs instead of filing them in a backlog.
Practices: prototypes against real API specs replace doc review: "A spec that reads elegantly in a doc can fall apart the first time you try to build against it." ("Product development, then and now")
Relevance: low. No task-management mechanism described; one data point against long-lived written specs.

### Running an AI-native engineering org (Fiona Fung, Anthropic, 2026-06-03)
File: refs/articles/claude.com/resources-articles-running-an-ai-native-engineering-org/article.md   URL: https://claude.com/resources/articles/running-an-ai-native-engineering-org
Thesis: The Claude Code team dropped long roadmaps and design-doc rituals; the bottleneck moved to verification and review.
Practices:
- Just-in-time planning: a six-month roadmap "was out of date by month three"; "Our planning ritual shifted away from design docs toward discussions in PRs or prototypes." ("Planning: shift roadmaps to just in time")
- "Don’t hesitate to kill processes that no longer work". ("How we rolled out our new norms")
Caveats: a team with many internal users giving feedback; says nothing about how tasks are tracked.
Relevance: medium. Direct counterweight to heavy up-front epic and roadmap planning.

### How Anthropic teams use Claude Code (Anthropic, 2025-07-24)
File: refs/articles/claude.com/resources-articles-how-anthropic-teams-use-claude-code/article.md   URL: https://claude.com/resources/articles/how-anthropic-teams-use-claude-code
Thesis: Survey of internal uses (navigation, tests, debugging, prototyping, runbooks). No backlog or task-tracking practice is described.
Relevance: low for this topic; old (2025-07).

### Introducing routines in Claude Code (Anthropic, 2026-04-14)
File: refs/articles/claude.com/resources-articles-introducing-routines-in-claude-code/article.md   URL: https://claude.com/resources/articles/introducing-routines-in-claude-code
Thesis: Cloud routines run a saved prompt on a schedule, API call or GitHub event.
Practices:
- The launch example draws work from an issue tracker: "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR." ("Scheduled routines")
- "Backlog management: triage new issues nightly, label, assign, and post a summary to Slack". ("What teams are building")
Evidence and numbers: daily caps at launch: Pro 5, Max 15, Team/Enterprise 25 routines per day.
Relevance: high. Anthropic's own example of an unattended loop selects from a tracker, not from a file.

### Introducing dynamic workflows in Claude Code (Alessio Vallero, Anthropic, 2026-05-28)
File: refs/articles/claude.com/resources-articles-introducing-dynamic-workflows-in-claude-code/article.md   URL: https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code
Thesis: Claude writes an orchestration script that fans work out to many subagents; coordination state lives outside the conversation.
Practices: "Progress is saved as the run goes, so a job that's interrupted picks up where it left off"; "Because the coordination happens outside the conversation, the plan stays on track". ("How it works")
Evidence and numbers: Bun Zig-to-Rust port, "roughly 750,000 lines of Rust, and eleven days from first commit to merge", 99.8% of tests passing.
Relevance: medium. For one large job, not a standing backlog.

### Agent view in Claude Code (Anthropic, 2026-05-11)
File: refs/articles/claude.com/resources-articles-agent-view-in-claude-code/article.md   URL: https://claude.com/resources/articles/agent-view-in-claude-code
Thesis: `claude agents` lists local sessions with state (waiting, working, done) to replace "an overloaded mental ledger".
Practices: `claude --bg [task]`, `/bg`; rows show whether a session produced a PR. Inference: this is session visibility, not a backlog; nothing persists what is still to do.
Relevance: medium for oversight.

### Keep Claude working toward a goal (Claude Code docs, fetched copy undated; mentions v2.1.269)
File: refs/articles/code.claude.com/docs-en-goal-md/article.md   URL: https://code.claude.com/docs/en/goal.md
Thesis: `/goal <condition>` keeps a session taking turns until a separate small model judges the condition met or impossible.
Practices:
- Listed use: "Working through a labeled issue backlog until the queue is empty". (intro list)
- The evaluator "doesn't run commands or read files independently, so write the condition as something Claude's own output can demonstrate." ("Write an effective condition")
- A good condition has one measurable end state, a stated check (for example "`npm test` exits 0"), and constraints such as "no other test file is modified". Max 4,000 characters; bound with `or stop after 20 turns`.
- Headless: `claude -p "/goal ..."` runs the loop to completion in one invocation. ("Run non-interactively")
- "completion is decided by a fresh model rather than the one doing the work." ("Compare ways to keep a session running")
Caveats: the evaluator only reads the transcript, so a task's evidence must be printed, not just asserted. One goal per session.
Relevance: high. Defines the stop condition for a backlog-draining loop.

### Let Claude coordinate ongoing work with Projects (Claude Code docs, public beta; fetched copy undated, mentions v2.1.280)
File: refs/articles/code.claude.com/docs-en-claude-projects-md/article.md   URL: https://code.claude.com/docs/en/claude-projects.md
Thesis: A project is one coordinating conversation that turns pasted tasks into parallel cloud threads, each on its own branch and PR, with an Overview pane grouping threads by state.
Practices:
- Overview states: Ready for review, Waiting on you, Working, Landing, Idle, Resolved. Resolved happens "automatically after a week with no activity". ("See what needs you in Overview")
- Cloud threads load each repository's `CLAUDE.md`, `.claude/CLAUDE.md` and root `.claude/rules/`, "but not the repositories' skills, `.claude/settings.json`, or `.mcp.json`"; hooks are "Not run". ("What threads pick up from your repositories")
- Project instructions (up to 16,000 characters) should say "How a thread checks its own work before calling it done". ("Write project instructions")
- "Build what `docs/spec.md` describes" is a named fit. ("When to use a project")
- Thread limits stated in conversation are "a preference rather than a cap"; enforced limit "500 new threads per day". ("What draws on your plan")
Caveats: "Projects aren't offered on Team or Enterprise plans yet"; "not in the terminal CLI"; github.com only; a project "belongs to one user"; uncommitted work can be lost if a sandbox cannot resume. Inference: a project tracks threads (work in flight), not a prioritised backlog of unstarted work, and it is Claude-only, so it cannot be the cross-harness system of record.
Relevance: high as the oversight and dispatch layer for Claude; low as the task store.

### Run prompts on a schedule (Claude Code docs; fetched copy undated, mentions v2.1.299)
File: refs/articles/code.claude.com/docs-en-scheduled-tasks-md/article.md   URL: https://code.claude.com/docs/en/scheduled-tasks.md
Thesis: `/loop` and the cron tools run prompts inside a session; they are session-scoped and expire.
Practices:
- `.claude/loop.md` (project) or `~/.claude/loop.md` (user) replaces the default prompt for bare `/loop`; truncated beyond 25,000 bytes. ("Customize the default prompt with loop.md")
- Bare `/loop` built-in order: "continue any unfinished work from the conversation", tend the branch's PR, then cleanup passes; it "does not start new initiatives outside that scope". ("Run the built-in maintenance prompt")
- "Recurring tasks automatically expire 7 days after creation." ("Seven-day expiry")
- Comparison table: cloud tasks need no machine but get a "fresh clone" and minimum interval 1 hour; Desktop and `/loop` have local files.
Relevance: high for the unattended-loop design: a local loop reads local files; a cloud run only sees what is pushed.

### Automate work with scheduled tasks, formerly routines (Claude Code docs, research preview; fetched copy undated)
File: refs/articles/code.claude.com/docs-en-routines-md/article.md   URL: https://code.claude.com/docs/en/routines.md
Thesis: A cloud scheduled task is a saved prompt plus repositories plus connectors, fired by schedule, API POST or GitHub event.
Practices:
- "the prompt must be self-contained and explicit about what to do and what success looks like." ("Create from the web", step 2)
- GitHub triggers include Issue events: "An issue is opened, edited, closed, reopened, labeled, assigned, or otherwise updated". ("Supported events")
- Each run clones the repository, starts from the default branch, and pushes to a `claude/`-prefixed branch. ("Repositories and branch permissions")
- Run status is not task status: outcomes "say how the session ended, not whether Claude completed the work your prompt describes". ("View and interact with runs")
- API fire text arrives wrapped as untrusted data in `<routine-fire-payload>`. ("Trigger a scheduled task")
Evidence and numbers: scheduled runs 100 per hour per account; cron more frequent than hourly is rejected.
Caveats: research preview; tasks "belong to your individual claude.ai account".
Relevance: high. An issue label can be the trigger for unattended work; task state kept in files must be on the default branch to be seen.

### Orchestrate teams of Claude Code sessions (Claude Code docs, experimental; fetched copy undated, mentions v2.1.317)
File: refs/articles/code.claude.com/docs-en-agent-teams-md/article.md   URL: https://code.claude.com/docs/en/agent-teams.md
Thesis: A lead session plus teammates share a task list with claim locking and dependencies; it is session-scoped and experimental.
Practices:
- Task model: "Tasks have three states: pending, in progress, and completed. A task can also depend on other tasks and shows as blocked". Teammates self-claim "the next unassigned, unblocked task". ("Assign and claim tasks")
- "Task claiming uses file locking to prevent race conditions". (same)
- Storage: `~/.claude/tasks/{team-name}/` where the team name is `session-` plus eight characters of the session ID; "One team per session ... You can't ... share a team across sessions." ("Architecture", "Limitations")
- Hooks `TaskCreated` and `TaskCompleted` can exit 2 to block creation or completion; `TeammateIdle` can keep a teammate working. ("Enforce quality gates with hooks")
- Sizing: "self-contained units that produce a clear deliverable"; "5-6 tasks per teammate"; start with 3 to 5 teammates. ("Best practices")
Caveats: "Task status can lag: teammates sometimes fail to mark tasks as completed, which blocks dependent tasks." The lead "can stop early too, deciding the team is finished before all tasks are actually complete." Not available with `-p`.
Relevance: medium. The built-in task list has the right primitives (states, deps, claim lock, completion hook) but lives in the home directory under a session name, so it is working memory for one run, not a backlog.

### Orchestrate subagents at scale with dynamic workflows (Claude Code docs; fetched copy undated, mentions v2.1.319)
File: refs/articles/code.claude.com/docs-en-workflows-md/article.md   URL: https://code.claude.com/docs/en/workflows.md
Thesis: A workflow is a JavaScript script (`agent()`, `pipeline()`, `parallel()`) that holds the plan in code; results live in script variables and a run is resumable only within its session.
Practices:
- "A workflow moves the plan into code." Comparison table row "Where intermediate results live": agent teams "A shared task list", workflows "Script variables". ("When to use a workflow")
- Saved to `.claude/workflows/` (project) or `~/.claude/workflows/` (user), run as `/<name>`; accept `args`, for example "Run /triage-issues on issues 1024, 1025, and 1030". ("Save the workflow for reuse", "Pass input to a saved workflow")
- "No mid-run user input ... For sign-off between stages, run each stage as its own workflow". ("Behavior and limits")
- Caps: 16 concurrent agents by default, 1,000 agents per run; `Large workflow` warning above 25 agents or 1.5 million projected tokens.
Caveats: after leaving the session "the run doesn't continue on its own"; "In a fresh session, Claude has no earlier run to relaunch and starts the workflow over."
Relevance: medium. An executor for one large task or for "run my task-selection procedure across N issues"; not a backlog.

### Manage sessions (Claude Code docs; fetched copy undated, mentions v2.1.285)
File: refs/articles/code.claude.com/docs-en-sessions-md/article.md   URL: https://code.claude.com/docs/en/sessions.md
Thesis: Sessions are local JSONL transcripts per project directory that can be resumed, named, branched and exported.
Practices:
- `claude --from-pr <number>` opens "sessions linked to that pull request"; the picker accepts a pasted PR URL "to find the session that created it".
- Name sessions (`claude -n auth-refactor`, `/rename`); accepting a plan titles the session from the plan.
- Transcripts live at `~/.claude/projects/<project>/<session-id>.jsonl` with 30-day default retention (`cleanupPeriodDays`); "The entry format is internal to Claude Code and changes between versions".
- A resumed compacted session continues from "the last compaction's summary"; interrupted tool calls are not rerun.
Caveats: Inference: session resume is machine-local, harness-specific and expires, so it cannot be the place task state lives; it is a convenience on top of durable task files or issues.
Relevance: medium.

### How Claude remembers your project (Claude Code docs; fetched copy undated, mentions v2.1.309)
File: refs/articles/code.claude.com/docs-en-memory-md/article.md   URL: https://code.claude.com/docs/en/memory.md
Thesis: `CLAUDE.md` (or `AGENTS.md`) carries instructions; auto memory carries Claude's own notes; both are context, not enforcement.
Practices:
- Claude reads `AGENTS.md` by default "only when you have no `CLAUDE.md` in your working directory or above it"; to share one file use a `CLAUDE.md` containing `@AGENTS.md`. ("AGENTS.md", "Share one file with other coding tools") Requires v2.1.277 or later.
- "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." ("Write effective instructions")
- Auto memory `project` type holds "ongoing work, deadlines, and decisions that Claude can't derive from the code or git history". ("Auto memory")
- "Auto memory is machine-local ... Files are not shared across machines or cloud environments." ("Storage location")
- "Project-root CLAUDE.md survives compaction". ("Instructions seem lost after `/compact`")
- A step that must always run should be a hook: hooks "apply regardless of what Claude decides to do." ("Claude isn't following my CLAUDE.md")
Caveats: imports "don't reduce" context cost. Inference: auto memory is unsuitable for backlog state because it is machine-local, Claude-only and not loaded into subagents; the pointer to the task system belongs in `AGENTS.md`/`CLAUDE.md`.
Relevance: high for where the "how tasks work here" paragraph must live to reach all three harnesses.

### Common workflows (Claude Code docs; fetched copy undated)
File: refs/articles/code.claude.com/docs-en-common-workflows-md/article.md   URL: https://code.claude.com/docs/en/common-workflows.md
Thesis: Recipes for everyday use; the task-relevant parts are PR-linked sessions, plan mode and scheduling.
Practices:
- "Claude Code links the session to the PR when Claude creates it with `gh pr create` or `glab mr create`"; find it later with `claude --from-pr 1234`. ("Create pull requests")
- Plan mode: `claude --permission-mode plan`; Claude "proposes a plan but makes no edits until you approve". ("Plan before editing")
- Scheduled prompts must stand alone: "The task runs autonomously, so it can't ask clarifying questions." Example prompt works a label queue: "Review open PRs labeled `needs-review`". ("Run Claude on a schedule")
Relevance: medium. Confirms the label-as-queue pattern and that the PR is the join point between a task and its session.

### Lessons from Spec-driven Development (Simon Martinelli, AI Native DevCon, June 2026)
File: refs/videos/odbNXv9xXjc/transcript.md   URL: https://www.youtube.com/watch?v=odbNXv9xXjc
Thesis: For business applications he specifies with system use cases plus an entity model and generates code directly through stack-specific skills, skipping the plan and task phases that Kiro, spec-kit and BMAD insert. (Captions garble names: "BMT method" is BMAD, "Tesla" is Tessl.)
Practices:
- "I skipped the plant task phase. I just use communication entity model and generate code directly." `[06:10]` (caption garble for "plan/task phase" and "use case/entity model")
- A use case has an actor, preconditions, a main success scenario, alternative flows and postconditions; "the post conditions are kind of acceptance criteria". `[15:25]`
- Use cases are the unit of progress: "we use the use cases in a Kanban way to track the progress. That's all we do." `[21:37]`
- Changing behaviour means editing the use case and re-running the implement skill, not regenerating the application. `[30:00]`
- Keep instruction files small; most guidance lives in skills. `[22:39]` to `[23:41]`
- Review depth follows risk per module. `[07:11]` to `[08:13]`
Evidence and numbers: six customers on the process; teams of one to two developers per self-contained system; "two weeks to do the specification" versus minutes to generate. `[21:37]`
Caveats: he rejects the waterfall charge: "we go use case by use case because a lot of people say spectrum development is waterfall. And that's simply not true." `[28:57]` Enterprise context with separate requirements engineers.
Relevance: high. A practitioner arguing that an intermediate tasks.md layer is unnecessary when the spec unit is small and skills encode how to build.

### Executable Specs: Building a Verification Layer for Agentic Coding (Shachar Azriel, Baz, AI DevCon 2026)
File: refs/videos/aWrGSM5vVyc/transcript.md   URL: https://www.youtube.com/watch?v=aWrGSM5vVyc
Thesis: Coding agents implement but do not verify against the ticket; a separate spec reviewer extracts each requirement and checks it against the deployed preview, one subagent per requirement.
Practices:
- Split planner (extract requirements and failure cases) from verifier; then one verifier per requirement in parallel, because by "the fifth or the sixth requirement" one agent carries irrelevant context. `[09:19]` to `[12:28]`
- Ground the verifier in code, not only the ticket, or it invents requirements "that nobody asked him to do". `[12:28]` to `[13:28]`
- Give the reviewer the base branch, not the diff: with the diff "it's biased to the specific solution that the engineer choose to implement." `[14:29]`
- Specs live in the ticketing system ("JIRA, it can be linear, it can be Monday notion, it can be on GitHub"). `[07:16]`
- Side effect: knowing an agent verifies against specs "encouraged them to write better specs." `[25:45]`
Evidence and numbers: tickets with 10 to 20 requirements were partly skipped by a single agent. `[10:22]` Vendor talk; no measured accuracy.
Caveats: he dismisses generated tests as testing "imaginary scenarios" `[24:44]`, which conflicts with Anthropic's and OpenAI's test-first emphasis.
Relevance: high for how acceptance criteria should be written (enumerated, individually checkable) and verified (separately, against running software).

### Harness Engineering: How to Build Software When Humans Steer and Agents Execute (Ryan Lopopolo, OpenAI, AI Native DevCon 2026)
File: refs/videos/c8bE0cj7vHY/transcript.md   URL: https://www.youtube.com/watch?v=c8bE0cj7vHY
Thesis: Human time and attention are the scarce resources; write down what "good" means, surface it just in time, and turn every repeated review comment into a static guardrail.
Practices:
- The agent file is a map plus an operating loop: "the most important thing that ends up in that agent file is a numbered set of steps that we expect the model to go through". `[15:22]`
- First step of that loop: ground in "the documentation knowledge base in the ticket that is proposed", then design docs and critical user journeys. `[15:22]`
- "I never want to give the same review feedback twice". `[10:15]`
- Evidence before merge: the agent "needs to convince me to merge its code"; ask for logs, a screenshot or a recorded reproduction video. `[22:39]`
- Parallelism limit: "I max out probably at three concurrent sessions on my laptop." `[05:08]`
- Long runs are fine with compaction ("six, 12, 36 hours") but context is "continually being emptied and filled", so guardrails needed across "15 context windows" must be re-surfaced by tools. `[06:09]`, `[27:47]`
Caveats: OpenAI-internal, greenfield, heavy static-check investment. He says little on how tickets themselves are stored (see the Symphony post below for that).
Relevance: high. Work arrives as a ticket; the repo holds the definition of done; evidence is attached to the PR.

### Spec-Driven Development: Specs Are the Program Now (AI Native Dev compilation, 2026)
File: refs/videos/606n8YC_-fU/transcript.md   URL: https://www.youtube.com/watch?v=606n8YC_-fU
Thesis: Compilation of Martinelli, Dave Farley and Azriel clips arguing the spec is the maintained artifact.
Practices: Farley: the specification "takes the form of executable specifications tests" that "both specify what we want and also verify that we got it." `[03:10]`
Relevance: low (duplicates the two talks above); the Farley clip supports acceptance criteria written as executable checks.

### How PMs can set up a product brain and become an agent orchestrator (Emma Burrows, Rezonant, AI Native DevCon 2026)
File: refs/videos/M6Nhl4zR0uk/transcript.md   URL: https://www.youtube.com/watch?v=M6Nhl4zR0uk
Thesis: A git repository of ingested inputs and a synthesised wiki lets an agent triage incoming tickets: small, well-specified ones go straight to a coding agent, larger ones get a PRD first.
Practices:
- Repo layout: `inputs/` (daily queue, including Linear tickets and GitHub diffs), `sources/` (raw), `wiki/` (customer insight, features, product principles, technical context). `[07:11]`
- Triage decides the route: for a small ticket the agent recommends a narrow fix and asks; for a larger one "what it has recommended instead is that we write a PRD for this." `[13:21]`
- Human interface is chat, not the tracker UI. `[09:16]`
- Granularity shift: "a ticket is basically a full feature now, rather than something which is like, you know, broken out into your front end and your back end". `[21:35]`
- Context in Google Docs "now to us anyway feel very backwards"; keep it in git so coding agents can read it. `[19:31]`
Caveats: vendor demo ("I cheated a little bit on this first one" `[10:17]`); no outcome data.
Relevance: medium. Supports "one issue = one shippable feature slice" and triage-before-spec.

### Building Product Teams in the Age of AI: What We Had to Relearn Every Quarter (Christopher Batey, CECG, AI Native DevCon 2026)
File: refs/videos/tJUAef_dBtU/transcript.md   URL: https://www.youtube.com/watch?v=tJUAef_dBtU
Thesis: AI amplifies existing practice; keep system-level thinking human, write the ADR first, limit complex work in progress, and hold engineers to adoption, not merged features.
Practices:
- A system-level decision "always comes as a completely separate pull request in something called an architectural decision record", human-reviewed, then agents review every later PR against the ADRs. `[14:27]` to `[15:27]`
- Agent-written ADRs "got longer and more verbose" until nobody understood them. `[14:27]`
- "work in parallel. Absolutely. But only work on one complex task at a time"; issues are labelled so simple ones can be picked up while an agent runs. `[23:36]`
- Not allowed to start the next feature until the previous one is adopted. `[20:34]`, `[26:45]`
- Uses the superpowers plugin (brainstorm, write plan, execute plan). `[22:36]`
- Stay able to switch provider "with a single command". `[16:27]`
Evidence and numbers: 90 to 100% of code AI-written; sub-streams of two to four people; test suite budget of 15 minutes.
Relevance: high for WIP limits, labels as complexity markers, and ADR-before-implementation.

### The Agentic Repository Automation Revolution (Don Syme, GitHub Next, AI Native DevCon June 2026)
File: refs/videos/kbvqRWY-bUs/transcript.md   URL: https://www.youtube.com/watch?v=kbvqRWY-bUs
Thesis: "Continuous AI" is a third pillar next to CI and CD: scheduled or event-triggered agent workflows in the repository whose only outputs are issues and pull requests. (He says "GitHub workflows"; the product is GitHub Agentic Workflows.)
Practices:
- A workflow is one checked-in markdown file with front matter (triggers, tools, `safe outputs`) hardened into a GitHub Action. `[13:28]`
- Security shape: agent runs read-only, no secrets, in a container, with "an extremely narrow output channel", for example "allowed to create one issue". `[14:29]`
- "They don't ever merge pull requests ... it's always the human in the loop through a pull request." `[15:30]`
- Repo Assist: once a day it "reads it's memory. And then it chooses a couple of a smorgasbord of tasks" the maintainer defines (triage, propose fixes, labels). `[22:48]`
- Sub-factories are carved out "through labeling or issue titles". `[26:54]`
- When output is poor, add a quality gate to the flow instead of fixing items by hand. `[31:06]`
Evidence and numbers: one refactoring workflow "had 112 merged PRS out of 142" `[20:43]`; dormant repos with 200 to 400 open issues returned to releases. Technical preview.
Caveats: GitHub-only; he maintains "about seven open source repositories", which is close to this developer's scale.
Relevance: high. The clearest argument that issues and PRs are the shared "information fabric" for humans and unattended agents, with labels as the routing mechanism.

### Harness engineering: leveraging Codex in an agent-first world (OpenAI; saved copy undated, post describes work from August 2025 over five months, so early 2026)
File: refs/articles/openai.com/index-harness-engineering/article.md   URL: https://openai.com/index/harness-engineering/
Thesis: A team shipped about a million lines with no hand-written code by making the repository the system of record: a short `AGENTS.md` map, a structured `docs/` tree, plans checked in, and mechanical enforcement.
Practices:
- "Plans are treated as first-class artifacts." Small changes get "Ephemeral lightweight plans"; complex work gets execution plans "with progress and decision logs that are checked into the repository." ("We made repository knowledge the system of record")
- "Active plans, completed plans, and known technical debt are all versioned and co-located, allowing agents to operate without relying on external context." (same)
- `AGENTS.md` is "roughly 100 lines" and "the table of contents"; the one-big-file approach "rots instantly". (same)
- "anything it can’t access in-context while running effectively doesn’t exist. Knowledge that lives in Google Docs, chat threads, or people’s heads are not accessible". ("Agent legibility is the goal")
- Human role: "We prioritize work, translate user feedback into acceptance criteria, and validate outcomes." ("What “agent-generated” actually means")
- Evidence: the agent can "Record a video demonstrating the failure", fix, and "Record a second video demonstrating the resolution" before opening the PR. ("Increasing levels of autonomy")
- Linters and CI validate that the knowledge base "is up to date, cross-linked, and structured correctly"; a recurring "doc-gardening" agent opens fix-up PRs.
Evidence and numbers: roughly 1,500 PRs in five months, 3 then 7 engineers, "3.5 PRs per engineer per day"; single runs "upwards of six hours".
Caveats: "should not be assumed to generalize without similar investment". "Humans may review pull requests, but aren’t required to", with "minimal blocking merge gates", which they call irresponsible in a low-throughput setting. The post does not say where the backlog of not-yet-planned work lives (Symphony, below, answers: Linear).
Relevance: high. The frontier-team statement for plans and progress logs living in the repo.

### Using PLANS.md for multi-hour problem solving (OpenAI Cookbook, 2025-10-01)
File: refs/articles/developers.openai.com/cookbook-articles-codex-exec-plans/article.md   URL: https://developers.openai.com/cookbook/articles/codex_exec_plans
Thesis: An "ExecPlan" is a self-contained living design document that a stateless agent can follow for hours; `AGENTS.md` says when to use one and `.agent/PLANS.md` defines the format.
Practices:
- `AGENTS.md` hook, verbatim: "When writing complex features or significant refactors, use an ExecPlan (as described in .agent/PLANS.md) from design to implementation."
- Mandatory living sections: `Progress`, `Surprises & Discoveries`, `Decision Log`, `Outcomes & Retrospective`; plus `Purpose / Big Picture`, `Context and Orientation`, `Plan of Work`, `Concrete Steps`, `Validation and Acceptance`, `Idempotence and Recovery`, `Artifacts and Notes`, `Interfaces and Dependencies`. ("Skeleton of a Good ExecPlan")
- `Progress` is a timestamped checkbox list: "Every stopping point must be documented here, even if it requires splitting a partially completed task into two (“done” vs. “remaining”)."
- Restartability: "it should always be possible to restart from _only_ the ExecPlan and no other work."
- Acceptance "should be phrased as behavior a human can verify ... rather than internal attributes (“added a HealthCheck struct”)."
- "Capture evidence": include concise terminal output, diffs or logs that prove success.
- "Milestones are narrative, not bureaucracy"; each "must be independently verifiable".
- "Checklists are permitted only in the `Progress` section". Narrative sections stay prose.
Evidence and numbers: a similar `PLANS.md` "has enabled Codex to work for more than seven hours from a single prompt."
Caveats: 2025-10; "ExecPlan" is "an arbitrary term, Codex has not been trained on it". A plan covers one feature, not a backlog.
Relevance: high. Best available template for the per-task progress and handoff record, and it is harness-neutral markdown.

### An open-source spec for Codex orchestration: Symphony (Alex Kotliarskyi, Victor Zhu, Zach Brock; OpenAI, 2026-04-27)
File: refs/articles/openai.com/index-open-source-codex-orchestration-symphony/article.md   URL: https://openai.com/index/open-source-codex-orchestration-symphony/
Read status: the article prose was read in full. The embedded `SPEC.md` is flattened onto one 52 KB line in the saved copy; I extracted and read only its sections on goals, issue fields, tracker config and dispatch rules (sections 2, 4.1.1, 5.3.1, 8.2), not the whole spec.
Thesis: The same team moved from supervising sessions to letting agents pull work from the issue tracker: "an agent orchestrator that turns a project-management board like Linear into a control plane for coding agents."
Practices:
- Motivation: "most people could comfortably manage three to five sessions at a time before context switching became painful." ("The ceiling of interactive coding agents")
- "We built our workflow based on ticket statuses, using the task manager Linear as a state machine." ("Turning our issue tracker into an agent orchestrator")
- Planning as a ticket: an agent produces an implementation plan; "Once we’re happy with the plan, the agent generates a tree of tasks, breaking the work into stages and defining dependencies between tasks." (same)
- "Agents only start working on tasks that aren’t blocked". Example: a React upgrade marked blocked on a Vite migration. (same)
- Agents file follow-up issues for out-of-scope findings "that we can evaluate and schedule later". (same)
- The process itself is a file: the workflow of "put it in progress ... add the PR, move it to the **Review** status, attach videos" is "captured in a simple `WORKFLOW.md` file". ("Using Symphony to build Symphony")
- Spec dispatch rules (SPEC section 8.2): eligible if state is in `active_states` (default `Todo`, `In Progress`), not already claimed or running, and "If the issue state is `Todo`, do not dispatch when any blocker is non-terminal." Sort: "`priority` ascending", then "`created_at` oldest first", then identifier.
- A run "may end at a workflow-defined handoff state (for example `Human Review`), not necessarily `Done`." (SPEC section 1)
- "treating agents as rigid nodes in a state machine doesn’t work well ... we eventually moved toward giving agents _objectives_ instead of strict transitions". ("Progress comes with new, different problems")
Evidence and numbers: "the number of landed PRs increase by 500% in the first three weeks" on some teams; default `max_concurrent_agents` 10; polling 30 s.
Tools and files named: Symphony (`openai/symphony`), `SPEC.md`, `WORKFLOW.md`, Linear, Codex App Server, `linear_graphql` tool, `gh` CLI.
Caveats: "we don’t plan to maintain Symphony as a standalone product"; "Not every task fits the Symphony style of work", ambiguous problems stay interactive; "we lost the ability to constantly nudge them mid-flight". Tracker support in the spec is Linear (`tracker.kind == "linear"`).
Relevance: very high. A frontier team's working answer: tracker holds tasks, states, priority and blockers; the repo holds the workflow contract and the knowledge; humans gate at a review state.

### Ralph Wiggum as a "software engineer" (Geoffrey Huntley, 2025-07-14)
File: refs/articles/ghuntley.com/ralph/article.md   URL: https://ghuntley.com/ralph/
Thesis: Ralph is `while :; do cat PROMPT.md | claude-code ; done`: a fresh context each loop, loaded with the same specs and one plan file, doing one item and committing.
Practices:
- State files: `specs/*` (one spec per file, written after a long requirements conversation), `fix_plan.md` ("a bullet point list sorted in priority of the items which have yet to be implemeneted"), and `AGENT.md` (how to build and run, kept brief).
- Selection is delegated to the model: "Follow the @fix\_plan.md and **choose the most important thing**." ("first some fundamentals")
- "One item per loop. I need to repeat myself here—one item per loop." ("one item per loop")
- Plan and build are separate prompts; the plan prompt regenerates `fix_plan.md` by comparing source against specs. ("the todo list")
- The plan file is disposable: "The TODO list is what I'm watching like a hawk. And I throw it out often." (same)
- Discovered bugs go into `fix_plan.md`; completed items are removed; "When @fix\_plan.md becomes large periodically clean out the items that are completed". (prompt listing)
- Keep status out of the instruction file: "DO NOT PLACE STATUS REPORT UPDATES INTO @AGENT.md". (prompt listing)
- After tests pass: update `fix_plan.md`, `git add -A`, commit, push, tag.
- Search before assuming something is unimplemented; code search "can be non-deterministic". ("don't assume it's not implemented")
Evidence and numbers: anecdotal (the CURSED language); "approximately 170k of context window".
Caveats: "There's no way in heck would I use Ralph in an existing code base"; greenfield only, "you'll get 90% done"; "you'll wake up to a broken codebase". 2025-07, before long-context and compaction improvements.
Relevance: high as the minimal file-based loop and as a warning: its own author restricts it to greenfield.

### Introducing Beads: A coding agent memory system (Steve Yegge, 2025-10-13)
File: refs/articles/steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a/article.md   URL: https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a
Thesis: Markdown plans rot and nest until agents lose track; moving all known work into a queryable issue graph (`bd`) with first-class dependencies fixed long-horizon planning for him.
Practices:
- The failure he reports with plan files: "I discovered I had _six hundred and five_ markdown plan files in varying stages of decay in my plans/ folder." ("A Big Plan...")
- Nested phases get re-planned after compaction until the agent declares the system "DONE" with outer phases forgotten. ("Descent Into Madness")
- Schema: "parent/child pointers (for epics) and blocking-issue pointers"; Claude added "four kinds of dependency links", including `discovered-from`. ("The Problem(s) Beads Solves", Appendix A)
- Agent reads next work with `bd ready --json` (rendered in the saved copy as "`bd ready — json`"): "a definitive list of unblocked work". (Appendix A)
- Claiming is a status: agents "see what’s claimed (`status: in_progress`)". (Appendix A)
- Storage: "it’s writing the issues into git as JSONL lines". ("Beads “Just Works”")
- One issue per throwaway session: "you can just kill your agents after completing each issue." ("Famous Last Words")
- Discovered work gets filed instead of dropped: "I’ve filed issue 397 to get them working again". ("The End of Lost Work")
Evidence and numbers: anecdotal; 128 issues, six epics, filed from an old TODO list in half an hour; sustainable concurrency for him was "1–3 concurrent agents".
Caveats: "brand-new alpha software" at the time; of Claude he says "it’ll still happily delete the database file". He asserts "GitHub Issues doesn’t work" without giving a reason beyond schema power and weight. The appendix is model-written advocacy, not evidence.
Relevance: high. Strongest statement of the case against markdown plan trees and for a dependency-aware ready queue. Conflicts with OpenAI's checked-in ExecPlans and Huntley's `fix_plan.md`. Inference: the conflict narrows when plans are one-per-task with a single owner and are deleted or archived on completion, which is not what Yegge was doing.

### Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl (Birgitta Böckeler, martinfowler.com, 2025-10-15)
File: refs/articles/martinfowler.com/articles-exploring-gen-ai-sdd-3-tools-html/article.md   URL: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
Thesis: "Spec-driven development" covers three levels (spec-first, spec-anchored, spec-as-source); the tools she tried impose one heavy workflow regardless of problem size and produce more markdown than is pleasant or safe to review.
Practices:
- Definitions: spec-first (written first, used for the task), spec-anchored (kept and evolved), spec-as-source (human edits only the spec). ("Definition")
- Kiro: Requirements → Design → Tasks, one markdown file each; requirements are user stories with "GIVEN… WHEN… THEN…" criteria; tasks "trace back to the requirement numbers". Steering files default to `product.md`, `structure.md`, `tech.md`. ("Kiro")
- Spec-kit: Constitution, then Specify → Plan → Tasks via slash commands; "one spec is made up of many files"; "creates a branch for every spec", so she judges it spec-first, not spec-anchored. ("Spec-kit")
- Tessl: spec-anchored and exploring spec-as-source, 1:1 spec to code file, code marked `// GENERATED FROM SPEC - DO NOT EDIT`; private beta then. ("Tessl Framework")
- Size mismatch: Kiro turned a small bug into "4 “user stories” with a total of 16 acceptance criteria". ("One workflow to fit all sizes?")
- "To be honest, I’d rather review code than all these markdown files." ("Reviewing markdown over reviewing code?")
- "I frequently saw the agent ultimately not follow all the instructions"; spec-kit research notes were regenerated as duplicate classes. ("False sense of control?")
- "small work packages almost seem counter to the idea of SDD." (same)
- Historical parallel: model-driven development; risk of "Inflexibility *and* non-determinism". ("Spec-anchored and spec-as-source")
Caveats: based on trials in September 2025, with her own note that the tools "might have already changed". She still values spec-first: "the general principle of spec-first is definitely valuable in many situations".
Relevance: high. The best-argued critique; it supports a size-tiered workflow and short specs, and argues against adopting any single SDD framework wholesale.

### Part B: fetched 2026-11-10 (collection `task-management`)

### Backlog.md README (MrLesk; fetched 2026-11-10, undated; demo GIF is named v1.40)
File: refs/articles/raw.githubusercontent.com/mrlesk-backlog-md-main-readme-md/article.md   URL: https://raw.githubusercontent.com/MrLesk/Backlog.md/main/README.md
Thesis: A CLI that keeps every task as a markdown file in the repo and frames the human's job as three review checkpoints: spec, plan, code.
Practices:
- "one task = one context window = one PR. Diffs stay a size a human can actually read." ("Why Backlog.md in the AI era")
- Checkpoint 2 is a plan written into the task "right before implementation so the plan reflects the current state of the codebase." ("Working with AI agents", step 3)
- Per-task acceptance criteria plus project-wide Definition of Done defaults under `definition_of_done:` in `backlog/config.yml`, added to every new task. ("Definition of Done defaults")
- Milestones and dependencies; task detail shows "what a task waits on and what waits on it". ("Features")
- Agent interface: CLI instructions are the recommended setup (an instruction file tells agents to run `backlog instructions overview`); MCP optional (`claude mcp add backlog --scope user -- backlog mcp start`, `codex mcp add backlog -- backlog mcp start`). "A single user-scope server covers every repo."
- Machine-readable reads: `backlog task list --json`, `--watch`; prefer commands "over hand-editing task files, so field types and metadata stay consistent."
- Human views: `backlog board` (terminal Kanban), `backlog browser` (local web UI on `127.0.0.1`), `backlog board export`.
- Lifecycle: mark Done, later `backlog task archive`; archived tasks keep ID and links and are read-only.
- Rerun recipe when output is poor: "clear the plan/notes/final summary, refine the task description and acceptance criteria, and run the task again in a fresh session."
Evidence and numbers: self-reported dogfooding; no outcome data.
Caveats: the README names no "epic" entity (milestones are the grouping), no atomic claim command, and no ready-queue command; cross-branch state is handled by config options (`checkActiveBranches`, `remoteOperations`, `activeBranchDays`), which implies task files can diverge between branches. Per-repo only; there is no cross-repo view described.
Relevance: high. The developer already uses it; it is the closest packaged match to "task file with acceptance criteria and DoD in the repo".

### bd - Beads README (Steve Yegge / gastownhall; fetched 2026-11-10, undated; mentions releases after v1.3.2)
File: refs/articles/raw.githubusercontent.com/steveyegge-beads-main-readme-md/article.md   URL: https://raw.githubusercontent.com/steveyegge/beads/main/README.md
Thesis: Beads is now a "Distributed graph issue tracker for AI agents, powered by Dolt", with a ready queue, atomic claim, hierarchical IDs and agent memory.
Practices:
- Core loop: `bd ready` ("List tasks with no open blockers"), `bd update <id> --claim` ("Atomically claim a task (sets assignee + in_progress)"), `bd close <id>`. ("Essential Commands")
- Epics are hierarchical IDs: `bd-a3f8` (Epic), `bd-a3f8.1` (Task), `bd-a3f8.1.1` (Sub-task). ("Hierarchy & Workflow")
- Minimal `AGENTS.md` block ends with "Do not use markdown TODO lists for task tracking."
- "Hash-based IDs (`bd-a1b2`) prevent merge collisions in multi-agent/multi-branch workflows." ("Features")
- Setup per harness: `bd setup claude`, `bd setup codex`, and others; `bd init` writes `AGENTS.md`.
- `bd github sync` mirrors one configured GitHub repository's issues.
Caveats (all from the README itself): storage changed since the 2025 post: "`.beads/issues.jsonl` is an export for viewers and interchange, not the source of truth or a backup"; data lives in `.beads/embeddeddolt/`, synced with `bd dolt push` / `bd dolt pull` to `refs/dolt/data`. Embedded mode is "single writer". Upgrades can cross schema migrations where "exactly one designated clone runs `bd migrate schema`". An older binary refuses a newer schema ("schema version mismatch: database is at v45"). Human visibility is via community UIs, not a built-in board. Repo badges point at `gastownhall/beads` and docs at `beads.gascity.com`.
Relevance: high as the reference design for agent-side selection and claiming; the operational weight (a Dolt database per repo, schema migrations) is the cost for a solo developer with a dozen repos.

### Spec Kit README (GitHub; fetched 2026-11-10; lists news up to 2026-10-16 and "Spec Kit 1.0")
File: refs/articles/raw.githubusercontent.com/github-spec-kit-main-readme-md/article.md   URL: https://raw.githubusercontent.com/github/spec-kit/main/README.md
Thesis: Spec Kit has become a toolkit of processes (SDD, bug fixing, idea assessment) plus extension, preset and workflow mechanisms, installed with `uv tool install specify-cli`.
Practices:
- SDD flow as skills: `/speckit-constitution`, `/speckit-specify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-implement`, `/speckit-converge`; "Repeat implement and converge until convergence reports `Converged`."
- Processes are now "independent entry points, not mandatory phases"; a separate bug flow writes reports to `.specify/bugs/<slug>/` with verdict "`verified`, `partial`, or `failed`; only `verified` confirms a successful fix."
- Idea assessment ends in "`go`, `needs-clarification`, or `kill`".
Caveats: this README answers Böckeler's 2025 size-mismatch critique with separate bug and assessment flows, but it is still one spec folder per feature with several files; nothing here is a backlog, a priority order or a claim mechanism. Catalog listings "are not audits or endorsements".
Relevance: medium. A spec-authoring process, not a task store.

### OpenSpec README (Fission-AI; fetched 2026-11-10, undated)
File: refs/articles/raw.githubusercontent.com/fission-ai-openspec-main-readme-md/article.md   URL: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md
Thesis: A lighter change-folder model: each change gets `proposal.md`, `specs/`, `design.md`, `tasks.md` under `openspec/changes/<name>/`, and archiving merges the spec deltas into living specs under `openspec/specs`.
Practices:
- Commands: `/opsx:explore`, `/opsx:propose <name>`, `/opsx:apply`, `/opsx:archive` (archives to `openspec/changes/archive/<date>-<name>/`, "Specs updated").
- Spec delta format: `## ADDED Requirements`, `### Requirement:` with SHALL wording, `#### Scenario:` with WHEN / THEN bullets.
- Stated philosophy: "fluid not rigid", "iterative not waterfall", "built for brownfield not just greenfield".
- Cross-repo planning via "Stores": "planning in a repo of its own ... One source of truth your whole team and every coding agent can read, across every repo." Marked beta.
- "Clear your context before starting implementation".
Caveats: self-description ("The most loved spec framework"); its comparison calls Spec Kit "Thorough but heavyweight. Rigid phase gates, lots of Markdown". Telemetry is on by default (`OPENSPEC_TELEMETRY=0` to disable). `tasks.md` is a checklist inside one change, not a backlog.
Relevance: medium to high. The cleanest spec-anchored model (change deltas archived into living specs) and the only tool here that names a cross-repo planning store.

### Kiro docs: Specs (AWS Kiro, page dated 2026-10-15)
File: refs/articles/kiro.dev/docs-specs/article.md   URL: https://kiro.dev/docs/specs/
Thesis: A Kiro spec is three files: `requirements.md` (or `bugfix.md`), `design.md`, `tasks.md`, produced in three phases with review between them.
Practices:
- Since Böckeler's 2025 review Kiro added Bugfix Specs ("current/expected/unchanged behavior in `bugfix.md`") and "Quick Spec to auto-generate all three artifacts without approval gates."
- Task execution builds "a **dependency graph** of the tasks in your `tasks.md`" and runs them in waves: "Waves execute sequentially; tasks within a wave execute concurrently."
- Available in IDE, CLI and Web; property-based "Correctness" checks are IDE-only.
Caveats: this page does not describe a backlog across specs, priorities or cross-repo use. Vendor documentation.
Relevance: medium. Confirms the industry-standard three-file shape and that vendors have added lighter paths for small work.

### BMad Method README (BMad Code; fetched 2026-11-10; stable v6.12, v7 preview alpha with ETA "mid-November 2026")
File: refs/articles/raw.githubusercontent.com/bmad-code-org-bmad-method-main-readme-md/article.md   URL: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md
Thesis: An agile, role-based method delivered as skills and plugins for Claude Code and Codex; it now advertises a right-sized process.
Practices:
- "Small changes go straight to build. Complex work gets the depth it needs."
- Install: `npx bmad-method install` (v6.12) or `/plugin marketplace add bmad-code-org/bmad-plugins` (v7); entry skill `bmad-build`, help via `bmad-help`.
- Separate module "BMad Loop": "Builds, verifies, and retros a whole epic unattended".
Caveats: v7 "Expect breaking changes between updates". The README does not show the story or epic file format (that is in docs I did not fetch), so cells about BMAD's file layout in the table below are marked unknown.
Relevance: low to medium. A full methodology with personas; heavier than a solo developer needs, and mid-migration.

### Taskmaster README (Eyal Toledano, Ralph Krysler; fetched 2026-11-10, undated)
File: refs/articles/raw.githubusercontent.com/eyaltoledano-claude-task-master-main-readme-md/article.md   URL: https://raw.githubusercontent.com/eyaltoledano/claude-task-master/main/README.md
Thesis: An MCP server and CLI that parses a PRD into dependency-ordered tasks and answers "what is next".
Practices:
- Flow: PRD at `.taskmaster/docs/prd.txt`, `task-master parse-prd`, `task-master next`, `task-master show 1,3,5`, expand a task into subtasks; tags act as workstreams (`--from-tag=backlog --to-tag=in-progress`).
- Core MCP tools (7): `get_tasks`, `next_task`, `get_task`, `set_task_status`, `update_subtask`, `parse_prd`, `expand_task`.
Evidence and numbers: default tool load is "36 tools ... (~21,000 tokens)"; `core` mode is 7 tools at about 5,000 tokens.
Caveats: it calls a model itself, so it needs provider API keys unless routed through Claude Code or Codex CLI; licence is "MIT License with Commons Clause"; documentation has moved to a commercial vendor site (tryhamster.com). The README still says "designed to work seamlessly with Cursor AI".
Relevance: low to medium. `next_task` is the right primitive, but the context cost and a second model dependency are poor trades.

### Linear docs: Agent platform, and MCP server (Linear; fetched 2026-11-10; the saved `date` field 2021-10-07 is wrong for this content)
Files: refs/articles/linear.app/docs-agents-in-linear/article.md, refs/articles/linear.app/docs-mcp/article.md   URLs: https://linear.app/docs/agents-in-linear , https://linear.app/docs/mcp
Thesis: Linear treats agents as assignable teammates and exposes its data through a hosted MCP server.
Practices:
- "**Delegate issues** by assigning the issue to the agent"; or @mention it. Delegated issues "still appear" in My issues; views and Insights can filter by **Delegate**. ("Agent platform")
- Workspace and team "Agent guidance" is markdown passed to agents; "how it is interpreted or applied depends on the specific agent integration."
- "Agents are not counted as billable seats in Linear."
- MCP: `claude mcp add --transport http linear-server https://mcp.linear.app/mcp`; `codex mcp add linear --url https://mcp.linear.app/mcp`; read-only endpoint `https://mcp.linear.app/mcp/readonly`; API key via `Authorization: Bearer`.
- Linear's own planning prompt: draft plan, review, then "create a parent issue that captures the overall goal and create sub-issues for the concrete pieces of work".
Caveats: hosted SaaS, needs network and OAuth; "Remote MCP connections can occasionally need a reconnect"; one auth context per workspace. Issue text does not live in the repo.
Relevance: medium to high. The tracker OpenAI's Symphony targets, and Anthropic's own routine example names it; the cost is a second system and an MCP dependency in every harness.

### GitHub Docs: Adding sub-issues; Creating issue dependencies; `gh issue list` manual (GitHub; pages dated 2026-01-01 in saved metadata, fetched 2026-11-10)
Files: [refs/articles/docs.github.com/en-issues-tracking-your-work-with-issues-using-issues-adding-sub-issues/article.md](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues), [refs/articles/docs.github.com/en-issues-tracking-your-work-with-issues-using-issues-creating-issue-dependencie/article.md](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies), [refs/articles/cli.github.com/manual-gh-issue-list/article.md](https://cli.github.com/manual/gh_issue_list)
Thesis: GitHub Issues now has native hierarchy and blocking relations, both scriptable from `gh`.
Practices:
- "You can add up to 100 sub-issues per parent issue and create up to eight levels of nested sub-issues." Sub-issues can come from other repositories.
- CLI: `gh issue create --title "TITLE" --body "ISSUE-DESCRIPTION" --parent PARENT-ISSUE-NUMBER`; `gh issue edit PARENT-ISSUE-NUMBER --add-sub-issue SUB-ISSUE-NUMBER`.
- Dependencies: `gh issue create ... --blocked-by N --blocking M`; `gh issue edit N --add-blocked-by M`; read with `gh issue view ISSUE-NUMBER --json blockedBy,blocking`.
- `gh issue list` filters: `--label`, `--assignee`, `--milestone`, `--state`, `--search`, `--type`; JSON fields include `blockedBy`, `blocking`, `parent`, `subIssues`, `subIssuesSummary`, `issueType`, `closedByPullRequestsReferences`.
- "Blocked issues are marked with a "Blocked" icon on your project boards".
Caveats (verified locally on 2026-11-10): the `gh` on this machine is 2.88.1 (2026-03-12) and its `gh issue create --help` shows no `--parent` or `--blocked-by` flag and no `blockedBy` or `parent` JSON field, so these flags need a newer `gh` release than the one installed. There is no atomic claim; assignment or a label is last-writer-wins. Nothing here gives a single "ready" query; it has to be composed (open, labelled ready, no open `blockedBy`).
Inference: these features remove the schema gap Yegge cited in 2025 ("parent/child pointers ... and blocking-issue pointers"), though not the claim and offline gaps.
Relevance: very high. The developer already uses GitHub issues, and every harness can drive `gh` without an MCP server.

### Anthropic autonomous-coding quickstart: coding and initializer prompts (Anthropic; fetched 2026-11-10, undated; accompanies the 2025-11-26 post)
Files: [refs/articles/raw.githubusercontent.com/anthropics-claude-quickstarts-main-autonomous-coding-prompts-coding-prompt-md/article.md](https://raw.githubusercontent.com/anthropics/claude-quickstarts/main/autonomous-coding/prompts/coding_prompt.md), [refs/articles/raw.githubusercontent.com/anthropics-claude-quickstarts-main-autonomous-coding-prompts-initializer-prompt/article.md](https://raw.githubusercontent.com/anthropics/claude-quickstarts/main/autonomous-coding/prompts/initializer_prompt.md) (README saved at refs/articles/raw.githubusercontent.com/anthropics-claude-quickstarts-main-autonomous-coding-readme-md but not read)
Thesis: The concrete prompts behind the feature-list pattern.
Practices:
- `feature_list.json` entry shape: `category` ("functional" or "style"), `description`, `steps` (array of strings), `passes` (boolean). "Order features by priority: fundamental features first".
- Ten-step session: get bearings (`cat app_spec.txt`, `cat feature_list.json | head -50`, `cat claude-progress.txt`, `git log --oneline -20`, count `"passes": false`), run `init.sh`, re-verify one or two passing features, choose one, implement, verify in the browser, flip `passes`, commit, update progress notes, end clean.
- Regression rule: if a previously passing feature is broken, "Mark that feature as "passes": false immediately" and fix before new work.
- "**YOU CAN ONLY MODIFY ONE FIELD: "passes"**"; never remove, edit, combine or reorder tests.
- Progress notes contain: what was accomplished, tests completed, issues found, "What should be worked on next", and a count such as "45/200 tests passing".
- Evidence convention in the commit message: "Screenshots in verification/ directory".
Caveats: greenfield and single-agent; selection is "first failing entry in file order", with no dependencies or claim. Wording is emphatic in a way current models may not need (see the harness-design post).
Relevance: high. The exact minimal schema for a JSON pass/fail ledger and the session ritual.

### Claude Code docs: Task tool availability, and Task list (partial reads; fetched copies undated, state "applies in Claude Code v2.1.268 and later")
Files: [refs/articles/code.claude.com/docs-en-tools-reference-md/article.md](https://code.claude.com/docs/en/tools-reference.md) (section "Task tool availability" only), [refs/articles/code.claude.com/docs-en-interactive-mode-md/article.md](https://code.claude.com/docs/en/interactive-mode.md) (section "Task list" only)
Read status: only the named sections of these two long reference pages were read.
Thesis: Claude Code's in-session task tools are now off by default on current models.
Practices:
- "The task-tracking tools, `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`, and `TodoWrite`, are available by default only on Opus 4.7, Sonnet 4.6, Haiku 4.5, and earlier models."
- Reason given: "On newer models, Claude keeps track of multi-step work without a written checklist, and the tools' definitions and reminders take up context."
- Opt in with `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` or `--allowedTools TaskCreate`; background and cloud sessions provide them on every model.
- Sharing across sessions: `CLAUDE_CODE_TASK_LIST_ID=my-project claude` uses "a named directory in `~/.claude/tasks/`". "Tasks persist across context compactions".
Caveats: the list is home-directory state, Claude-only, and now opt-in. Inference: a convention that depends on the built-in checklist will silently stop working on newer models; it is in-session scratch, not the system of record.
Relevance: high (as a negative result).

### OpenCode and Codex plan and todo features (partial reads from corpus)
Files: [refs/articles/opencode.ai/docs-config/article.md](https://opencode.ai/docs/config/) ("Todos"), [refs/articles/opencode.ai/docs-migrate-v1/article.md](https://opencode.ai/docs/migrate-v1/), [refs/articles/opencode.ai/docs-agents/article.md](https://opencode.ai/docs/agents/) (Plan row), [refs/articles/raw.githubusercontent.com/anomalyco-opencode-v1-3-10-packages-web-src-content-docs-github-mdx/article.md](https://raw.githubusercontent.com/anomalyco/opencode/v1.3.10/packages/web/src/content/docs/github.mdx), [refs/articles/developers.openai.com/codex-learn-best-practices/article.md](https://developers.openai.com/codex/learn/best-practices) ("Plan first for difficult tasks"), [refs/articles/code.claude.com/docs-en-github-actions-md/article.md](https://code.claude.com/docs/en/github-actions.md) (intro lines)
Read status: grep-located passages only, not full reads.
Practices:
- OpenCode: "Todos are off by default in V2. To turn them on, use the experimental flag. It may change or be removed in a future release". Config: "Set `todo` to `true` to give agents a `todowrite` tool for tracking multi-step work. Defaults to `false`."
- OpenCode Plan agent "Explores and plans without editing normal project files. It may write OpenCode plan files when asked".
- OpenCode GitHub: "Mention `/opencode` or `/oc` in your comment, and OpenCode will execute tasks within your GitHub Actions runner"; also a `schedule` trigger.
- Codex: "Toggle with `/plan` or `Shift`+`Tab`"; for longer work "configure Codex to follow a `PLANS.md` or execution-plan template".
- Claude Code GitHub Actions: "Mention `@claude` in a pull request or issue comment".
Inference: two of the three harnesses have demoted the in-session todo tool in 2026, and all three can be started from a GitHub issue or PR comment, which makes the issue the one task handle common to all of them.
Relevance: high for cross-harness portability.

### Technology Radar: Beads (Thoughtworks, 2026-11-04)
File: refs/articles/thoughtworks.com/en-us-radar-tools-beads/article.md   URL: https://www.thoughtworks.com/en-us/radar/tools/beads
Thesis: Beads moved to Trial; it is positioned beneath a team tracker, not instead of one, and has grown heavier.
Practices:
- "It complements team issue trackers such as Linear ... Beads holds the finer-grained tasks agents create as they work, and it syncs both ways with Linear, Jira and GitHub Issues."
- "Each agent can claim the next available task without colliding with others."
Caveats: "additions such as an HTTP API, work leases and synchronization between stores make Beads heavier than the lightweight tracker it started as. Upgrades migrate the schema in place, and clients running different versions can't share a store, so teams should pin a single version for each shared store and review the instructions Beads writes into AGENTS.md". Names alternatives `ticket` (wedow) and `tracer`.
Relevance: high. An independent 2026 assessment that confirms both the value and the operational cost.

### Use Beads with Jira, Linear, and GitHub Issues (John Mayor, Gas City, 2026-08-07)
File: refs/articles/gascity.com/guide-beads-with-jira-linear-github-issues/article.md   URL: https://gascity.com/guide/beads-with-jira-linear-github-issues/
Thesis: Two layers: "Keep Jira, Linear, or GitHub Issues as the organization’s system of record. Use Beads as the coding agent’s local system of action."
Practices:
- The gap in hosted trackers, stated by the Beads vendor: "No universal documented atomic ready-and-claim operation".
- On GitHub Issues: "For an open-source project or a small team whose planning already lives next to pull requests, GitHub Issues may be enough. It minimizes the number of products a contributor must visit."
- Risk of one layer only: "Publishing every agent-discovered subtask into the company tracker can bury humans in machine churn."
- Linking: store the tracker URL as the bead's external reference; sync only "milestones or externally meaningful outcomes".
- Notes Linear "coding sessions that can run Claude or Codex from an issue" and GitHub "assigning issues to coding agents" (I did not fetch those two pages).
Caveats: vendor guide, so its framing favours adding Beads; facts "reviewed July 30, 2026". "Deleted issues are permanently deleted" on GitHub.
Relevance: high. The vendor with most to gain concedes GitHub Issues alone is sufficient at small scale, and names precisely what is missing (atomic ready-and-claim).

### Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall? (Colin Eberhardt, Scott Logic, 2025-11-26)
File: refs/articles/blog.scottlogic.com/2025-11-26-putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfa/article.md   URL: https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
Thesis: Rebuilding a known feature of a hobby app with Spec Kit took far longer than iterative prompting and produced no better code.
Evidence and numbers:
- Spec Kit, first feature: "33m30 - of agent execution time", "689 loc", "2,577 lines of markdown", "3.5 hrs review time". The plan step alone wrote 2,067 lines, including a "444-line module contract" that was "4x the length of the actual module itself".
- His usual approach for the same feature: "8m - of agent execution time", "1,000 loc (and no markdown!)", "15 min code review", "9 min functional test and small fixes".
- "I am a lot more productive without SDD, around ten times faster."
Practices he recommends instead: "Prompt Copilot to implement a modest size increment, something I feel I can confidently review in 10 minutes", then functionally verify immediately.
- On documentation worth keeping: "capturing architectural details and design decisions is very valuable. Code can give you the ‘what’, but cannot tell you the ‘why’".
- On stale scaffolding: "Are a bunch of smart and detailed prompts created in an open source project really going to keep up with and exceed the performance of the latest foundation models?"
Caveats: n=1, hobby app, feature he had already built, Copilot with Sonnet 4.5, Spec Kit of November 2025 (pre-1.0). He allows that he may be "simply just using it wrong" and that it may suit people who do not read code.
Relevance: high. The only source here with before/after numbers for a solo developer; it argues for small reviewable increments and ADR-style "why" docs over generated spec stacks.

### Spec-Driven Development Benchmark 2026 (Paul Francis, Uvik Software; page metadata 2026-09-24, text says the run was "October 15, 2026")
File: refs/articles/uvik.net/blog-spec-driven-development-benchmark/article.md   URL: https://uvik.net/blog/spec-driven-development-benchmark/
Thesis: On 50 brownfield Python tickets with one model, a written spec raised merge rate on features, data pipelines and multi-file changes, and did not pay on bug fixes, refactors or small tickets.
Evidence and numbers (Table 1 to 5):
- Merge rate: OpenSpec 42/50, Kiro 41/50, BMAD 41/50, Spec Kit 40/50, no-spec control 36/50. "The noise band on merge rate is plus or minus 10 percentage points."
- Cost per merged ticket: Kiro $2.35, control $2.43, OpenSpec $2.71, Spec Kit $3.33, BMAD $4.23.
- By size: small (1 to 2 files) control 85% equals best spec arm; medium (3 to 5 files) 85% vs 70%; large (6 or more) 80% vs 50%.
- By type: features and data pipelines 90% best spec arm vs 60% control; bug fix with failing test 90% vs 90%; refactor 80% vs 80%.
- "specs with 6 or more of the 8 checklist items merged 89.3% of tickets, against 60.0% otherwise."
- Review defects per merged ticket: 0.46 with a spec, 0.86 without. Spec drift: "the merged code did not match its own spec in 7.9% of merged spec-arm tickets."
- Median spec size 93 lines (OpenSpec) to 188 (BMAD); spec phase used 35.1% of tokens.
Practices:
- "Spec Fit Test": write a spec when 3 or more hold: touches 3 or more files; 4 or more acceptance criteria; crosses a module, service or repository boundary; alters a data schema or public API; more than one engineer or agent; regulated or audited code.
- Spec checklist (8): Goal, Scope, Inputs and outputs, Data changes, Edge cases, Acceptance tests, Constraints, No-change list.
- Otherwise "give the agent the ticket text and the acceptance criteria, then review the result."
Caveats: a staffing vendor's content-marketing page (it asks readers to "quote each one with a link to this page"); raw data and client code not inspected by me; one team, Python only, one model (claude-sonnet-5), fixed 45-minute boxes; Kiro ran in a different harness; the page date and the stated run date disagree; most gaps between spec arms are inside the stated noise band. It does not test Claude Code plan mode or spec-anchored use (listed as future work).
Relevance: high but treat as weak evidence. It is the only controlled comparison found, and it agrees in direction with Böckeler and Eberhardt on small tasks.

### A Brief History of Ralph (Dex Horthy, HumanLayer; body dated January 6, 2026, saved metadata 2026-06-01)
File: refs/articles/humanlayer.dev/blog-brief-history-of-ralph/article.md   URL: https://www.humanlayer.dev/blog/brief-history-of-ralph
Thesis: Ralph's lasting point is small work units in fresh context windows, not running forever.
Practices:
- "if the specs are bad, the results will be meh"; "if you are iterating/exploring, you probably don't want ralph in the first place". (August 2025 lessons)
- Existing codebases: run a desired-state loop "ONCE on a cron overnight, and merge small iterations over time. Waking up to one small refactor every morning is better than both a) waking up to none and b) waking up to 50."
- The key point "is not "run forever" but in "carve off small bits of work into independent context windows"."
- Stale PRs: "the easier alternative to "merge/rebase" is just to re-run the ralph loop on the fresh code with the same prompt".
Caveats: he found Anthropic's December 2025 ralph plugin "uses a strange markdown file to track state" and broke sessions if the file was deleted; anecdotal.
Relevance: medium to high. Supports a nightly loop that produces one small PR per repo rather than draining a queue.

### everything is a ralph loop (Geoffrey Huntley, 2026-01-17)
File: refs/articles/ghuntley.com/loop/article.md   URL: https://ghuntley.com/loop/
Thesis: Restates Ralph as "a single process that performs one task per loop" and tells readers to watch the loop and fix each failure "so it never happens again".
Practices: run the loop manually first ("automation with a pause") before going unattended.
Relevance: low to medium; no new mechanism. It is the page both the OpenAI harness post and Anthropic's scientific-computing post link to.

### What is Tessl? (Tessl docs home; fetched 2026-11-10, undated)
File: refs/articles/docs.tessl.io/index/article.md   URL: https://docs.tessl.io/
Thesis: Tessl now describes itself as "an open platform for managing agentic development across your organization", centred on skills distribution, review gates and policy.
Practices: none about specs or tasks on this page. The earlier concepts URL cited by Böckeler (`docs.tessl.io/introduction-to-tessl/concepts`) returned 404 on 2026-11-10.
Caveats: Inference: the spec-as-source framework Böckeler reviewed is no longer Tessl's headline product; I could not confirm its current status. The page contains a line addressed to AI agents telling them to read `docs.tessl.io/llms.txt` first; I did not follow it.
Relevance: low for task management.

### Third-party coding agents (GitHub Docs; public preview; fetched 2026-11-10)
File: refs/articles/docs.github.com/en-copilot-concepts-agents-about-third-party-coding-agents/article.md   URL: https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
Thesis: On github.com an issue can be assigned to the Anthropic Claude or OpenAI Codex coding agent, which works asynchronously and opens a PR.
Practices:
- "**Issues**: Assign the agent to an existing issue in a repository." "**Pull requests**: Mention `@AGENT_NAME` in a comment".
- Agent output is scanned (CodeQL, secret scanning, dependency advisories) before the PR is finalised.
- "Coding agents consume **GitHub Actions minutes** and **AI credits**."
Caveats: public preview; described as something that "can be powered by your existing Copilot subscription", so it appears tied to a Copilot plan (not confirmed); a different runtime from the developer's local Claude Code or Codex setup, so repo skills and hooks may not apply.
Relevance: medium. Confirms that assigning an issue is a harness-neutral dispatch action for both Claude and Codex.

### Sources located by the Part A grep but not read
Ranked by term density, these matched and were not read, so nothing above relies on them: `steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04` (Gas Town, 2026-01-01), `humanlayer.dev/blog-skill-issue-harness-engineering-for-coding-agents`, `raw.githubusercontent.com/humanlayer-advanced-context-engineering-for-coding-agents-main-ace-fca-md`, `cursor.com/blog-self-driving-codebases`, `cursor.com/blog-scaling-agents`, `code.claude.com/docs-en-changelog-md`, `code.claude.com/docs-en-agent-view-md`, `martinfowler.com/articles-exploring-gen-ai-humans-and-agents-html`, `developers.openai.com/blog-run-long-horizon-tasks-with-codex`, `developers.openai.com/codex-guides-build-ai-native-engineering-team`, `claude.com/resources-articles-product-management-on-the-ai-exponential`. Fetched in Part B but not read: the autonomous-coding quickstart README and `dev.to/pacheco-spec-driven-development-isnt-waterfall-but-it-keeps-ending-up-there-4eei`.
