# Headless goal limits: documentation and local probe

Date: 2026-11-16. Task: [6](../../tasks/6-hard-limits-for-goal-examples.md).

## Primary sources

- [Goal documentation](https://code.claude.com/docs/en/goal.md), refreshed with `tools/refs
  article https://code.claude.com/docs/en/goal.md --force --collection claude-code-docs`, saved under
  `refs/articles/code.claude.com/docs-en-goal-md/`: the evaluator reads conversation evidence,
  cannot independently inspect files or execute checks, and judges prose turn/time clauses.
- [CLI reference](https://code.claude.com/docs/en/cli-reference.md), refreshed the same way,
  saved under `refs/articles/code.claude.com/docs-en-cli-reference-md/`: `--max-turns` limits
  agentic turns in print mode. Streamed queued input can start a new turn with a new limit.
  `--max-budget-usd` uses estimated cost, can overshoot and can differ from actual billing.

## Setup and command

`claude --version` returned `2.1.323 (Claude Code)`. `claude --help` included the budget flag
but omitted `--max-turns`; absence from help was not evidence that the option was unsupported.

Created `/tmp/tackroom-task6-cap` and ran `tools/setup /tmp/tackroom-task6-cap`. A temporary
Python standard-library HTTP server listened only on `127.0.0.1` on an ephemeral port. On
each Messages request it returned a synthetic SSE `tool_use` response asking `Read` to read
`/tmp/tackroom-task6-cap/fixture.txt`, a harmless one-line file. It always requested another
read, so the synthetic response could not end the run voluntarily. It supplied 10 input and
10 output tokens as synthetic usage and echoed the request's model field.

The subprocess environment contained only PATH, LANG, a disposable `CLAUDE_CONFIG_DIR`,
`ANTHROPIC_BASE_URL` pointing to that local server, a dummy `ANTHROPIC_API_KEY`, and
`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`. No provider endpoint was used. No model flag
was supplied or default model setting changed. The Python subprocess had a 30-second timeout
as a test-harness backstop; neither run reached it.

In the scratch directory, for N=1 and N=2:

```sh
claude -p '/goal fixture.txt has been read repeatedly and every result is shown in this conversation' \
  --bare --setting-sources project --max-turns N --output-format json \
  --tools Read --allowedTools Read --permission-mode dontAsk \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' --no-session-persistence
```

Replace N with the cap. The local fixture is required: this command alone, without the
isolated subprocess environment above, would use the caller's configured provider.

Temporary artifacts on the test machine: `/tmp/tackroom-task6-probe.py`,
`/tmp/tackroom-task6-cap1.json`, `/tmp/tackroom-task6-cap2.json`.

## Results

| Requested cap | Local Messages requests | Exit | JSON subtype | terminal_reason | num_turns |
|---|---|---|---|---|---|
| 1 | 1 | 1 | error_max_turns | max_turns | 2 |
| 2 | 2 | 1 | error_max_turns | max_turns | 3 |

The errors were `Reached maximum number of turns (1)` and `(2)` respectively. Both results
had `is_error: true` and no permission denials. Each run warned that three project permission
allow entries were ignored because the scratch workspace was untrusted; trust was not changed.
The probe explicitly allowed only Read and exposed no other built-in tools or MCP servers.

The second run is a boundary control: raising the limit allowed one additional request, then
the same enforced stop. The JSON turn count is not the observed request count. Report the
limit result and request count rather than asserting that `num_turns` equals the cap.

## Limits and decisions

This is real CLI execution against a synthetic local transport, not a provider/model test.
It verifies option acceptance and interruption of a continuing tool loop with `/goal` in
the prompt. `--bare` skips customization discovery, so it does not validate template hooks,
the full unattended task workflow, or goal-evaluator decisions. Synthetic usage/cost fields
are not billing evidence. Dollar-cap enforcement, streamed queued input, resumed goals,
subagents and background-process cleanup were not exercised. A turn limit is not a timeout
for a running tool; a process supervisor is needed for a wall-clock boundary.

Local judgment: retain soft clauses in interactive goal examples with an explicit explanation,
put the supported hard flag in the headless recipe, use `dontAsk` with task-specific approvals,
and treat a limit result as interrupted work. No scheduler, provider call, global permission
change or template change was needed. Nothing in this task was run under Codex as the target
harness, and vendor launchers were not run against a live endpoint.

## Cross-harness follow-up

The owner requested cross-harness verification before merging. This extends the initial
Claude-only evidence above; it does not claim a full model-driven task run in every harness.
No model/provider calls or persistent user configuration changes were made.

### Shared setup and discovery

Fresh install: `tools/setup /tmp/tackroom-task6-multi --codex --opencode`.

```text
python3 tools/check-skill-setup.py
Shared skills: template copy, default, Codex, OpenCode, combined; references, dry run and existing files passed

uv run --quiet --no-project --python '>=3.11' python tools/check-codex-agents.py
Codex roles match Claude briefs, root copies and fresh setup: memory-analyzer, memory-organizer, reviewer
```

Codex CLI 0.169.0: generated its actual App Server JSON schema, initialized a local stdio
server, then called `skills/list` with `cwds: ["/tmp/tackroom-task6-multi"]` and
`forceReload: true`. All 12 shared skills were returned with repo scope and `enabled: true`,
with no discovery errors. Paths resolved through the shared symlinks into `.claude/skills/`.
The probe's first attempt hit Python's default 64 KiB line limit because the inventory also
includes personal skills; raising the transport buffer to 4 MiB let the response be parsed.

`codex app-server --stdio --strict-config -c goals.max_goal_token_budget=1000` plus
`config/read` returned `goals.max_goal_token_budget: 1000`. This is configuration acceptance,
not budget-exhaustion evidence. The project config layer was present but disabled pending
project trust; an invocation-only `projects` override did not enable it. No persistent trust
or hook approval was changed. Do not infer active sandbox/hook rules from discovered skills.

OpenCode 1.3.10: `opencode --pure debug skill` returned all 12 project skills at the shared
`.agents/skills/` paths. `opencode --pure debug config` loaded the project reviewer with edit
denied and the `scripts/agent/check*` shell allow rule. A subprocess-only
`OPENCODE_CONFIG_CONTENT` containing `{"agent":{"task6-limit-probe":{"description":"Local configuration probe","steps":2}}}`
and `opencode --pure debug agent task6-limit-probe` returned `steps: 2`, exit 0. This proves
V1 parser acceptance, not enforcement at the last model step. `--pure` disables external plugins.

The discovered skill set in both clients: careful, dream, kickoff, lock-tests, performance,
second-opinion, spec, task, ui-craft, verify, wrap-up, write-tests. `command -v` found no
`kimi`, `qwen` or `gemini` executables; their loader behavior remains documentation-only.

### Enforced wall-clock boundary

GNU coreutils `timeout` 9.4 wrapped each real CLI with
`timeout --signal=TERM --kill-after=2s 10s <command>`. A local Python HTTP server accepted
requests and deliberately withheld responses. It returned 404 for metadata GET requests.
The subprocess environment and command-line overrides routed model traffic only to that
loopback listener; no provider was contacted and no default model setting was changed.

- Codex command: `codex exec --ignore-user-config --ephemeral --sandbox read-only
  --skip-git-repo-check --json` with invocation-only `model_provider="probe"` and
  `model_providers.probe` settings: `name="Local timeout fixture"`, `base_url` at the local
  server's `/v1`, `wire_api="responses"`, `requires_openai_auth=false`,
  `supports_websockets=false`. Prompt: `Reply only with OK. Do not use tools.`
- OpenCode command: `opencode run --pure --model probe/fixture --format json` with the same
  prompt. Subprocess-only `OPENCODE_CONFIG_CONTENT` enabled only `probe`, using
  `@ai-sdk/openai-compatible`, the local `/v1` base URL, a dummy API key and a synthetic
  `fixture` model. `OPENCODE_DISABLE_MODELS_FETCH=true` and
  `OPENCODE_DISABLE_DEFAULT_PLUGINS=true`; no global config was edited.

| CLI | Local model request paths | Elapsed | Exit |
|---|---|---|---|
| Codex | One `/v1/responses` | 10.02 seconds | 124 |
| OpenCode | Two `/v1/chat/completions` | 10.07 seconds | 124 |

Codex warned that project config was untrusted and that the local model-list requests got
404. It still reached the stalled Responses endpoint before the timeout. OpenCode's two
requests were both local; no inference about their purpose or billing is made.

Controls for the supervisor itself: a command printing `ok` exited 0 before a 0.2-second
timeout; a Python process ignoring SIGTERM was killed after the additional 0.2-second grace
(Python subprocess return `-9`, shell status 137). The actual CLI probes exited on TERM;
forced-kill escalation was exercised only with that harmless Python process.

Artifacts on this machine: `/tmp/tackroom-task6-codex-discovery.py`,
`/tmp/tackroom-task6-codex-discovery.json`, `/tmp/tackroom-task6-opencode-skills.json`,
`/tmp/tackroom-task6-opencode-steps.json`, `/tmp/tackroom-task6-timeouts.py`, and
`/tmp/tackroom-task6-timeouts.json`. The scripts are local probes, not a shipped scheduler.

### Sources and remaining limits

Refreshed through `tools/refs`, saved in `refs/articles/`:

- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference.md):
  `goals.max_goal_token_budget` controls the default and largest requested goal budget.
- [Codex App Server](https://learn.chatgpt.com/docs/app-server.md): `skills/list`,
  `thread/goal/set`, `tokenBudget` and goal state; ordinary `codex exec` is not evidence of a
  native goal being created.
- [OpenCode agents](https://opencode.ai/docs/agents/): V2 `steps` ends with a text-summary
  step and new input resets the allowance; V2 uses `agents` rather than V1's `agent` map.
- [OpenCode skills](https://opencode.ai/docs/skills/): shared skill discovery.
- [GNU timeout](https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html):
  termination, kill grace and exit codes. Detached/remote processes need separate management.

The offline probes establish shared installation, actual discovery, selected config parsing,
and external timeout enforcement. They do not prove model compliance, Codex goal-budget
exhaustion, OpenCode step-limit enforcement, trusted hook execution, every permission boundary,
an end-to-end dream pass, dollar billing or detached-process cleanup. No vendor launchers or
uninstalled clients were exercised against live endpoints. macOS and Windows were not tested.
