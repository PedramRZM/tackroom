# Other harnesses and other models

What carries over from the Claude Code setup to Codex, OpenCode and the vendor CLIs, and how to
run GLM, DeepSeek and Kimi models. Research: `refs/notes/harness-codex-opencode-standards.md`
and `refs/notes/model-routes-glm-deepseek-kimi.md`.

**Validation scope:** the original setup was tried with Claude Code and config loading in
OpenCode 1.3.10. On 2026-11-15, local inspection also found Codex CLI 0.169.0 with native goals
enabled. Installation/feature detection is not validation of the full Codex harness; see
the current [task evidence](plans/1-verification-before-implementation.md) for the limited
scratch exercise. Kimi Code, Qwen Code, Gemini CLI and vendor endpoints remain documentation-only.

## What each harness reads from a project

| | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Instructions | `CLAUDE.md` (imports `AGENTS.md`) | `AGENTS.md` | `AGENTS.md` |
| Skills | `.claude/skills/` | `.agents/skills/` | `.claude/skills/` and `.agents/skills/` |
| Subagents | `.claude/agents/*.md` | `.codex/agents/*.toml` | `.opencode/agents/*.md` |
| Hooks | `.claude/settings.json` | `.codex/hooks.json` | none; code plugins only |
| Permissions | `.claude/settings.json` | `.codex/config.toml`, `.codex/rules/` | `opencode.json` |
| Sandbox | optional, per machine | on by default, enforced by the OS | none documented |
| Trust before loading project config | yes | yes, and each hook separately | none documented |

So the template keeps one copy of what can be shared and a thin file per harness:

- `AGENTS.md` and `WORKFLOW.md` are the shared text.
- Skills live in `.claude/skills/`. `tools/setup --codex` links each one into `.agents/skills/`,
  which is where Codex, Kimi Code and Qwen Code look. Only `name` and `description` are
  portable front matter; the Claude-only fields (`disable-model-invocation`, `hooks`,
  `allowed-tools`) are ignored elsewhere, so `careful`, `lock-tests` and `dream` do less there.
  Whether Codex tolerates unknown front matter keys is not documented.
- The hook scripts (`guard.py`, `stop-check.py`) are shared with Codex, which uses the same
  contract: JSON on stdin, exit code 2 to block.
- Claude and Codex both ship `reviewer`, `memory-analyzer` and `memory-organizer`.
  Their descriptions and instruction bodies match; OpenCode has its own reviewer.

## Codex

`template/.codex/`: approvals on request, a workspace-write sandbox with the network off, and a
setting that stops Codex passing variables named like keys or tokens to the commands it runs
(by default it passes them through). Hooks point at the shared scripts.

Standalone `.codex/agents/*.toml` files are discovered automatically; no per-role entry in
`config.toml` is needed. Each supplies `name`, `description` and `developer_instructions`.
Codex roles inherit the parent's model and permissions. Claude's `haiku` alias and tool
allow/deny lists are deliberately not translated into unsupported settings. The reviewer
therefore has a no-edit instruction, not a separate read-only sandbox.
Source: `refs/notes/harness-codex-opencode-standards.md`, section 1, and the
[Codex subagents guide](https://learn.chatgpt.com/docs/subagents).
The repository check compares all three briefs and exercises a fresh `tools/setup --codex`.

Limits to know (`refs/notes/harness-codex-opencode-standards.md`, section 1):

- A project file cannot choose a model provider. Codex ignores those keys there.
- A custom provider must speak OpenAI's Responses API. A Chat Completions or Anthropic-style
  endpoint is not enough.
- Codex asks you to trust the project, and to review each hook, before anything in `.codex/`
  takes effect. A changed hook script must be reviewed again.
- Project workflows use skills, invoked as `$name`; this is separate from native commands.
  Codex has native `/goal` for persistent objectives. Use the shared criteria/check/evidence
  workflow described in [Loops](loops.md#goals-across-harnesses), not a Claude-specific clone.
- The memory roles are available in Codex, but the end-to-end dream pass is not ported: its
  exporter still reads Claude Code transcripts. Role presence does not prove native Codex
  transcript export or a complete dream run.

## OpenCode

`template/opencode.json`: read rules that deny env files and keys, edit rules that keep curated
memory read-only, and a shell allowlist with everything else set to ask. It is written with the
1.x key names, which 2.x still loads.

- OpenCode 2.x is current (the docs describe 2.2); 1.3.10 is installed here. 2.x reads only
  `AGENTS.md`, renames several config keys and does not run 1.x plugins. The template ships no
  plugin for that reason.
- OpenCode has no documented sandbox and no trust prompt, and it loads code from
  `.opencode/plugins/` at startup. Its permission rules are the only control. Be careful
  opening someone else's repository with it.
- On this machine 1.3.10 also listed the agents from `.claude/agents/`, so the reviewer may
  appear twice. That came from one `opencode debug config` run and may be due to an installed
  plugin.

## Kimi Code, Qwen Code, Gemini CLI

From their documentation only (`refs/notes/model-routes-glm-deepseek-kimi.md`): Kimi Code and
Qwen Code read `AGENTS.md` and `.agents/skills/` directly, so `tools/setup --codex` gives them
the shared files. Gemini CLI reads `GEMINI.md` unless `context.fileName` in
`.gemini/settings.json` names `AGENTS.md`. None of their own config is in the template.

## GLM, DeepSeek and Kimi models

Each vendor offers an endpoint that imitates Anthropic's API, so Claude Code can be pointed at
it with environment variables. `scripts/agent/claude-with <vendor>` does that for one session:

    scripts/agent/claude-with glm
    scripts/agent/claude-with deepseek
    scripts/agent/claude-with kimi          # Moonshot platform, pay as you go
    scripts/agent/claude-with kimi-code     # Kimi Code membership

Keys go in `.env.agents.local` at the repository root (gitignored; the variable names are in
`scripts/agent/keys.example`). After starting, run `/status` and check the base URL.

Why a launcher and not a settings file: a settings `env` block overrides the shell, so provider
variables there would pin every session in the repository to one vendor and defeat switching.
The vendors' own guides use shell exports followed by `claude`
(`refs/notes/model-routes-glm-deepseek-kimi.md`, section (b)).

What to expect:

- Anthropic does not support this. Their gateway docs say Claude Code is not supported with
  non-Claude models through any gateway. It works because the vendors emulate the API.
- The advisor, fast mode, Remote Control and features behind Anthropic's feature flags are
  unavailable. Only DeepSeek publishes a field-by-field compatibility table.
- GLM-5.3 and DeepSeek V4 Pro are text-only; the flash variants accept images.
- Model names change often and were copied from vendor pages on 2026-11-10. If a request fails
  with an unknown-model error, check the vendor's page first.
- Subagent and skill files in the template name models by alias (`haiku`), never by a dated
  Claude ID, so the launcher's tier mapping redirects them.

In OpenCode, the same three vendors are provider entries in `opencode.json`, with keys read
from the same variables: export them (or source the keys file) before starting OpenCode, then
pick the model with `/models`. These entries use the vendors' OpenAI-style endpoints.

In Codex, a vendor needs an entry in your user-level Codex config, or a launcher that sets
`CODEX_HOME` to a gitignored folder holding a generated config. Neither is built here.

## Keys

- The only file that holds keys is `.env.agents.local`. It is gitignored, matched by the
  guard's and OpenCode's env-file rules, and denied to Claude Code's file tools.
- Exported keys reach every command the agent runs unless the sandbox is on, in which case the
  template's settings hide the listed variables from commands.
- Do not paste a key into an agent conversation, and do not run a vendor's `curl | bash` setup
  script: they rewrite user-level config.
- Coding-plan keys are personal and product-specific. A key for one product on the wrong
  endpoint fails or bills the wrong account.
