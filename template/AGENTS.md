<!--
This file is read at the start of every session by Claude Code (through CLAUDE.md), Codex,
OpenCode, Kimi Code and Qwen Code. Every line costs attention on every task, so keep it under
about 100 lines and write only what an agent cannot learn by reading the repository:
exact commands, traps, decisions that are not in the code, and how work is handed over.
Leave out the architecture tour, the file listing and general coding advice.
Comments like this one are stripped by Claude Code before the file is loaded.
-->

# PROJECT NAME

One or two sentences: what this is, who uses it, and anything unusual about how it runs.

## Checks

- `scripts/agent/check` runs types, lint and tests. `scripts/agent/check --quick` skips the full test run.
- One test file: `REPLACE with the exact command`
- Run the app: `REPLACE with the exact command` (then open `REPLACE with the URL`)

Before saying work is done, run the checks and show their output. If something could not be
verified, say which thing and why. A change a user can see is also checked in the running app;
the `verify` skill describes how.

## How work is tracked

`WORKFLOW.md` has the full loop. In short: one task, one branch named `task/<id>-<slug>`, one
pull request that shows evidence for each acceptance criterion. You commit on the task branch and
open the pull request. The user merges; nothing is pushed to `main` directly.

Stop and ask when an acceptance criterion is wrong or cannot be met, when the work needs a
decision about data, money or user-visible behaviour that the task does not settle, or when the
same fix has failed twice. Otherwise keep going until the criteria are met.

Work you discover outside the task becomes a new task in the tracker. It is not folded into the
current change.

## Gotchas

What the code will not tell you. Add a line when something has had to be corrected twice, and
delete a line when it stops being true.

- REPLACE, for example: "Amounts are integers in the smallest currency unit, never floats."

## Memory

`.agents/memory/` holds what earlier sessions learned about this project the hard way: commands
that worked, decisions and their reasons, traps. `_index.md` lists what is there. It exists so a
new session does not have to rediscover those things. It is rewritten only by the `dream` pass;
when you learn something a future session would need, append one dated line to
`.agents/memory/inbox.md`.

## More

- `docs/decisions/`: decisions about architecture, data and infrastructure, one short file each.
  Read the relevant one before changing what it covers.
- `docs/specs/`: specs for larger features. `docs/plans/`: the plan and progress log of a task in flight.
