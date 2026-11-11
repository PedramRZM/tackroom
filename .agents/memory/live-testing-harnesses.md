---
name: live-testing-harnesses
description: What happened when the template was run live with headless claude -p and opencode on this machine (project trust, the sandbox failure, permission denials, unreliable model-reported listings). Read before a live test or before trusting a headless result.
---

# Live testing the harnesses

## Pattern used

- Copy `template/` into `/tmp/tmpl-scratch-<x>`, run `git init` and commit, then run
  `claude -p --setting-sources project --permission-mode acceptEdits --output-format json "<prompt>"`.
- Parse `.result`, `.permission_denials` and `.total_cost_usd` from the JSON. Stdout can start with
  warning text, so parse from the first `{`.
- Cost: a Fable-model probe with three steps cost about $0.51. A Haiku one-line probe cost $0.007.
  Use Haiku for cheap checks.

## Trust

- In an untrusted scratch folder the run printed: "Ignoring 2 permissions.allow entries from
  .claude/settings.json: this workspace has not been trusted." Project allow rules do nothing until
  the folder is trusted. The message points at `projects["<path>"].hasTrustDialogAccepted` in
  `~/.claude.json`. That global file was not edited. To test allow rules, accept the trust dialog
  interactively first.
- In those untrusted runs, a Write to `.agents/memory/deploys.md` and `git push origin main` were
  listed in `permission_denials`. Appending to `.agents/memory/inbox.md` succeeded. Whether the
  denials came from the guard or from the untrusted folder was not separated.

## Sandbox failure on this machine

- With `sandbox.enabled: true`, sandboxed Bash failed on every call with:
  `apply-seccomp: write /proc/self/setgroups (nested userns is capability-restricted; caller must provide CAP_SYS_ADMIN): Permission denied`.
- Cause: Ubuntu 24.04 sets `kernel/apparmor_restrict_unprivileged_userns` to 1. bwrap 0.9.0 at
  `/usr/bin/bwrap` runs when called directly.
- Documented fix: an AppArmor profile for `/usr/bin/bwrap` (Claude Code docs, "Add an AppArmor
  profile for bubblewrap"). It was not applied in the session, so the fix is unverified here.
- Consequence: the shipped template settings have no `sandbox.enabled`. Enable it only after the
  profile is in place and `/sandbox` shows no missing dependencies.

## Model-reported facts are not evidence

- A Haiku headless session, asked to list the project skills and subagents, answered
  "second-opinion, spec, task, verify, wrap-up" and "memory-analyzer, memory-organizer, reviewer".
  It then said it could not confirm them from disk. The Bash sandbox had failed. Take
  inventories from the files.

## OpenCode

- `opencode debug config` (installed 1.3.10) prints the resolved config. Against the template's
  `opencode.json` it loaded the providers `zai`, `deepseek-direct` and `kimi`, 27 bash permission
  rules, and agents including `reviewer`. The output has log text before the JSON.
- The template's `opencode.json` uses the V1 schema. Live OpenCode docs describe V2 (2.2.7). See
  [[model-routes-and-harnesses]].

## Shell hooks in the owner's environment

- The owner's global `~/.claude/hooks/protect-secrets.sh` blocks a Bash command if its text
  contains `.env`, `credentials`, `server.pem`, or similar. This includes heredocs, fixtures and
  notes. `guard-bash.py` blocks `rm -rf "$T"` on a computed path and asks for the literal path.
  See [[process-lessons]].
- The inner headless runs were not blocked by these hooks. The blocks shown came from the outer
  session's own Bash calls.

## Not run

- The dream skill was launched in the background on a copy of the session transcript
  (`/dream --source /tmp/dream-src --since 30d`, sonnet). Its result is not in the transcript.
- Codex: not installed. The vendor launchers (`scripts/agent/claude-with`) were run only for usage
  and error paths, never against a live endpoint.
- Sandbox-on guardrail tests: not run, because of the AppArmor failure above.

Related: [[template-hooks-and-guard]], [[memory-dream-design]].
