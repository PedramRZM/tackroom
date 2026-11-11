---
name: model-routes-and-harnesses
description: What each harness (Claude Code, Codex, OpenCode, Kimi Code, Qwen Code, Gemini CLI) reads and can set per project, and how GLM, DeepSeek, Kimi, MiniMax and Qwen are routed through the template's launcher. Read before touching scripts/agent/claude-with, opencode.json, .codex/ or model routing.
---

# Harnesses and model routes

## What is installed (2026-11-10)

- Claude Code 2.1.322. OpenCode 1.3.10 (binary). Codex, Gemini, Kimi, Qwen and MiniMax CLIs are not installed.
- The live OpenCode docs describe V2 (2.2.7), which changes config keys and drops V1 plugins. The
  template's `opencode.json` uses V1 keys (`permission`, `provider.<id>.options.baseURL`,
  `apiKey: "{env:VAR}"`). Check the installed version before editing.

## Which file each harness reads

- Instructions: Codex and OpenCode read `AGENTS.md`. Claude Code reads it only when no
  `CLAUDE.md` or `CLAUDE.local.md` exists (from v2.1.277). The template uses `CLAUDE.md` with
  `@AGENTS.md`. Codex reads `AGENTS.override.md` first and has a 32 KiB limit.
- Skills: Claude Code reads only `.claude/skills/`. Codex reads only `.agents/skills/`. OpenCode
  reads `.opencode/skills/`, `.claude/skills/` and `.agents/skills/`. The template keeps skills once
  in `.claude/skills/`. `tools/setup --codex` symlinks them into `.agents/skills/` (tested in a scratch project).
- Kimi Code and Qwen Code read `AGENTS.md` and `.agents/skills/` directly. Gemini CLI reads
  `GEMINI.md`, and `AGENTS.md` only through `context.fileName`.
- Codex ignores `model_provider` and `model_providers` in a project `.codex/config.toml`, with a
  startup warning. Provider selection needs user-level config or a launcher (`CODEX_HOME` or `-c`
  overrides; the launcher approach is an inference, not tested). Custom providers must speak the
  OpenAI Responses API (`wire_api = "responses"`).
- OpenCode documents no trust prompt and no sandbox. Project plugins in `.opencode/plugins/` run as
  code at startup.
- Kimi Code has no project config file. `KIMI_CODE_HOME` isolates it, and its hooks are user-level only.

## Vendor routes (documented 2026-11-10; none run against a live endpoint)

| Vendor | Claude Code | OpenCode | Codex |
|---|---|---|---|
| Z.ai GLM | `ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic`, token in `ANTHROPIC_AUTH_TOKEN`, `glm-5.3[1m]` | `opencode auth login` ("Z.AI Coding Plan") | `https://api.z.ai/api/v1`, responses |
| DeepSeek | `https://api.deepseek.com/anthropic`, `deepseek-v4-pro` | `/connect` to `deepseek` | `https://api.deepseek.com/`, responses |
| Moonshot Kimi | platform `https://api.moonshot.ai/anthropic`, `kimi-k3[1m]`; membership `https://api.kimi.ai/coding/` with `ANTHROPIC_API_KEY`, `k3.1-pro[1m]` | "Moonshot AI" or "Kimi For Coding" | `env_key = "KIMI_API_KEY"`, responses |
| MiniMax | `https://api.minimax.io/anthropic` | provider `minimax-coding-plan` | `https://api.minimax.io/v1`, responses |
| Alibaba Qwen | `https://coding-intl.dashscope.aliyuncs.com/apps/anthropic`, `qwen3.7-plus` | not read | not read |
| Gemini | none documented | a Google provider exists; setup not read | not documented |

- Anthropic's gateway docs say it does not support routing Claude Code to non-Claude models. These
  routes work only because the vendors emulate the Messages API. Advisor, fast mode, Remote Control
  and newer features are unavailable on them.
- Settings-file `env` overrides shell exports. Provider variables must not go in
  `.claude/settings.json` or `.claude/settings.local.json`, or per-session switching breaks.
- Unknown model IDs get a 200K window unless `[1m]` or `CLAUDE_CODE_MAX_CONTEXT_TOKENS` is set.
  Every tier (`ANTHROPIC_MODEL`, Opus, Sonnet, Haiku, the subagent model) must be mapped.
- Contradictions among vendor docs: MiniMax says shell exports override the settings file, while
  Claude Code and Kimi say the reverse. Kimi sets `CLAUDE_CODE_AUTO_COMPACT_WINDOW=1048576`, above
  the documented 1,000,000 maximum. Kimi's Haiku mapping points at a model its own list marks closed.
  Z.ai states its default mapping three ways.

## What the template ships

- `template/scripts/agent/claude-with <glm|deepseek|kimi|kimi-code> [args]`. It sources
  `.env.agents.local` (gitignored), sets base URL, token and all tiers, sets
  `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` and `CLAUDE_CODE_DISABLE_FAST_MODE=1`, then execs `claude`.
  Only usage and error paths were run. The key variable names are `ZAI_API_KEY`, `DEEPSEEK_API_KEY`,
  `MOONSHOT_API_KEY` and `KIMI_API_KEY`. The template example is `scripts/agent/keys.example`. The
  name `.env.agents.example` was dropped because the owner's secrets hook blocks it.
- `template/opencode.json`: providers `zai` (`https://api.z.ai/api/coding/paas/v4`), `deepseek-direct`
  and `kimi` (`https://api.moonshot.ai/v1`), with `{env:...}` keys. Bash is `ask` by default, with
  git read commands, `scripts/agent/check` and `next-task` allowed. Pushes to main or master and
  force pushes are denied. `opencode debug config` loads it.
- `template/.codex/config.toml` and `hooks.json`: no provider selection. Written from the Codex docs
  and not yet run under Codex.

## Unverified

- Whether the first-run login accepts a token from a shell export. Kimi and Alibaba say to set
  `hasCompletedOnboarding` in `~/.claude.json`.
- Whether `CLAUDE_CODE_EFFORT_LEVEL` works on unknown model IDs without `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT=1`.
- Which features (tool search, structured output, WebSearch, prompt caching) each endpoint supports.
  Only DeepSeek publishes a field-by-field table.

Related: [[template-hooks-and-guard]], [[live-testing-harnesses]], [[repo-purpose-and-scope]].
