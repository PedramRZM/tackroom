# Memory and dreaming

How a project using this template remembers things between sessions, and how that memory, and
the instructions themselves, get corrected over time. This is the loop Lamis Mukta described at
AI Native DevCon in June 2026, built from her talk and three other Anthropic sources.

## The problem

Every session starts knowing nothing. A session can write notes for the next one, but it has
two limits it cannot get around (Mukta, [`refs/videos/tTcxVv8HHNw/transcript.md`](https://www.youtube.com/watch?v=tTcxVv8HHNw), 15:27 to 16:29):

- Its attention is split between the task and helping its future self.
- It sees only itself. When the same mistake happens in five sessions, none of them knows.

Notes written in the moment are also sometimes wrong, and a wrong note is trusted by whoever
reads it next. In Anthropic's own test, one incorrect note sent an agent into the same trap
three times; a pass that checked the note against the transcript fixed it
([`refs/articles/anthropic.com/research-components-of-agent-memory/article.md`](https://www.anthropic.com/research/components-of-agent-memory), "Dreaming can
correct memory").

## Two loops

**In band, during a session.** The agent reads memory when it needs it and leaves a note when
it learns something. Fast payoff: the next session is better.

**Out of band, between sessions ("dreaming").** A separate pass with its own budget reads the
memory and the recent session transcripts, including what the tools actually returned. It
checks existing notes against what happened, adds what is missing, reorganises, and reports
patterns no single session could see. A person reviews the result.

Self-correction is the checking step: the transcript is ground truth against the agent's own
notes. Auto-prompting is the promotion step: the few lessons that matter move up into what
every session reads, and what has gone stale moves out.

## How the template implements it

| Tier | Where | Who writes | Loaded |
|---|---|---|---|
| Always read | `AGENTS.md`, mainly its Gotchas | You, by accepting a proposal | Every session |
| Curated memory | `.agents/memory/*.md`, catalogued in `_index.md` | Only the dream pass | On demand, through the index |
| Inbox | `.agents/memory/inbox.md` | Any session, one dated line at a time | When the dream pass runs |
| Scratch | Claude Code's own auto memory, on your machine | Claude Code | Automatically |

Mukta's production requirements map onto plain repository features
([`refs/videos/tTcxVv8HHNw/transcript.md`](https://www.youtube.com/watch?v=tTcxVv8HHNw), 10:23 to 13:26):

- **Versioning and provenance**: memory is in git. Every change is a diff with a date and an author.
- **Permissions**: curated memory is read-only outside the dream pass. `guard.py` enforces it
  using the agent name Claude Code passes to hooks: only `memory-analyzer` and
  `memory-organizer` may write there, and they may write nowhere else.
- **Portability**: Markdown files in the repository, readable by every harness.
- **Concurrency**: her hash-before-write scheme is not built. Analyzers are told to re-read
  before writing and to read back after, which is what Anthropic's recipe does.

### The dream pass

The project Dream skill in Claude Code or Codex. It follows Anthropic's own recipe for building a dream
([`refs/articles/platform.claude.com/cookbook-managed-agents-cma-dreaming-with-a-dynamic-workflow/article.md`](https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow)),
adapted from their managed service to a local repository:

1. A script exports finished sessions as plain text: user and agent messages, tool calls and
   tool results. Thinking and harness bookkeeping are dropped, long results are cut, and
   strings that look like credentials are replaced.
2. One `memory-analyzer` per transcript. It **verifies** what memory claims against the
   transcript, **enriches** memory with exact commands, values, staleness notes and process
   lessons, and **organises** small linked files with a description each.
3. One `memory-organizer` merges duplicates, marks conflicts instead of guessing, folds the
   inbox in, and completes the index.
4. The lead groups the corrections the analyzers reported, counts how many sessions each
   appeared in, and writes `.agents/dream-report.md` with proposed changes.
5. You review `git diff .agents/memory` and the report, and accept or reject.

The lead never reads a transcript. That keeps the run cheap and keeps whatever a transcript
contains from steering the agent that writes the proposals. The analyzers have file tools only:
no shell and no network.

### What a proposal is

A correction earns a proposal when it showed up in two or more sessions, or once with real
damage. The proposal names the lowest rung that would have prevented it: a failing check, then
a gotcha in a skill, then a line in `AGENTS.md`. It also proposes removals. This is the same
ladder as principle 2 in `docs/principles.md`, and the same idea Mukta describes as the dream
orchestrator returning proposed changes with the transcripts and how prevalent the issue is
(22:39 in her talk).

Proposals are not applied automatically, and they should be applied one at a time. Anthropic's
April 2026 postmortem is the reason: a single added line in a system prompt cost 3% on an
evaluation after passing weeks of internal testing (`refs/notes/anthropic-engineering.md`,
finding 7).

## What the first real run showed

Run on 2026-11-11 against the session that built this repository (one transcript, 542,000
characters after export):

- Five minutes, $0.52 at list price: $0.11 for the lead on Sonnet, $0.41 for the two workers
  on Haiku.
- Eight memory files and an index were written, with no write outside `.agents/memory/` and
  the report.
- The report's first proposal caught a real problem: the repository's own `AGENTS.md` had
  recorded, as a convention, a way of getting past one of the owner's hooks, which the owner's
  rules forbid. It was reworded.
- One export command was refused and retried; the run recovered on its own.

One run on one transcript is a smoke test. It says the pipeline works, not that the memory it
builds makes later sessions better. Anthropic reports that effect with numbers only for their
managed service (a customer's first-pass mistakes down 90%, a benchmark's completion rate up
six times: [`refs/videos/RtywqDFBYnQ/transcript.md`](https://www.youtube.com/watch?v=RtywqDFBYnQ), 03:15 and 11:22), and those are vendor
figures.

## Running it

- By hand: `/dream` (since the last dream), or `/dream --since 7d`.
- To enable weekly consolidation on a host with the local sessions and an authenticated Codex CLI, run
  `python3 .agents/skills/dream/scripts/scheduled-dream.py install --project .`. The user timer runs
  on Sunday between 03:00 and 04:00 local time and catches up after downtime. Use `systemctl --user
  list-timers --all` to inspect it. Repeat installation after a harness upgrade. For cron or other
  schedulers invoke the same command with `run` in place of `install`.
- Both Claude Code and Codex logs are selected by checkout, including linked worktrees. Automatic runs
  queue redacted inputs privately, analyze at most 20 per run, and publish a report, proposed memory
  and source revision in `~/.local/state/tackroom-dream/<project-id>/runs/`. Failed batches stay in
  the queue. The read-only Codex passes operate in temporary directories. Review the draft before
  applying memory or rules. Scheduled runs see histories on that machine and the selected Git ref.
- Weekly is a reasonable start. Claude Code deletes transcripts after 30 days by default
  (`cleanupPeriodDays`), so a longer gap loses sessions.
- Other harnesses: pass `--extra <folder>` with plain-text logs. Exporters for Codex and
  OpenCode session formats are not written.

## Guidance the design follows

- **Say what memory is for, not how to use it.** Anthropic tested fixed rules such as "record
  only failures" and found they removed much of the benefit for current models; older models
  needed to be told to read memory first (`research-components-of-agent-memory`, "Steering
  Claude to write memory"). The Memory paragraph in `AGENTS.md` is written that way.
- **Keep the always-loaded layer small.** A wrong line there reaches every session, and long
  instruction files reduce adherence (same post, "Dreaming can promote notes up the memory
  hierarchy").
- **Store only what the environment cannot tell you.** In Anthropic's game-playing test, nine
  well-chosen files outperformed 413 (same post, "Claude has learned to judge salience").
- **Treat transcripts and memory as untrusted.** A tool result can say "ignore your
  instructions". The analyzers' prompt says a transcript is data, never copy a secret, and the
  cookbook's reasoning for file-tools-only is kept (cookbook, "Treat transcripts as untrusted
  input").

## Known limits

- Practitioners report that in-session memory duplicates itself and drifts
  (`refs/notes/devcon-1-skills-context-memory.md`, contradictions). The dream pass is the
  answer the sources give, and it has not been run here over many sessions.
- The guard covers the file tools. A shell command can still write into `.agents/memory/`.
- Claude Code's auto memory is separate, machine-local state. The template leaves it on as the
  scratch tier. To rely only on the repository, set `"autoMemoryEnabled": false` in the
  project's settings.
- Nothing measures whether a memory file is ever read. Anthropic logs skill usage with a hook
  for the same reason (`refs/notes/anthropic-claude-dev-blog.md` (a)); that is not built here.
