---
title: "Release v43.8.0 · dyoshikawa/rulesync"
date: "2026-11-08"
url: "https://github.com/dyoshikawa/rulesync/releases/latest"
site: "GitHub"
type: "article"
via: "direct"
---
## Repository navigation

[dyoshikawa](https://github.com/dyoshikawa)released this

[14 commits](https://github.com/dyoshikawa/rulesync/compare/v43.8.0...main)to main since this release

## What's Changed

### Behavior Changes

- **mcp (Google Antigravity IDE / CLI / plugin):** the canonical `timeout` (milliseconds) is now written as Antigravity's `timeoutSeconds` (integer seconds, rounded up; a negative value becomes `-1`) instead of an ignored `timeout` key, and is read back on import. Per-server `enabledTools` is now emitted instead of stripped, and an `sse` server is warned about because Antigravity does not support the legacy HTTP+SSE transport. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3813](https://github.com/dyoshikawa/rulesync/pull/3813)
- **permissions (Reasonix):** canonical `agent` rules are now written under both `task` (before studio-v2.58.0) and `spawn_agents` (v2.58.0+), so they keep matching after the upstream rename. Import reads both names back to `agent`, and the strictest action wins when they conflict. When the `agent` category is set, existing `task` / `spawn_agents` entries are replaced by rulesync, with a warning when a replaced entry was stricter. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3814](https://github.com/dyoshikawa/rulesync/pull/3814)
- **permissions (Crush):** canonical bash rules now reach Crush v0.100.0's command lists:
  - an exact `allow` becomes a `safe_commands` entry, withheld when a deny or ask overlaps a form Crush would approve through it;
  - a whole-command `deny` becomes a `blocked_commands` entry, with a warning that it is not a full deny (a direct call still prompts);
  - pattern `ask` rules are skipped with a warning;
  - hand-written `blocked_commands` entries are always kept.
Import maps `safe_commands` back to `allow` and `blocked_commands` back to `deny`. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3818](https://github.com/dyoshikawa/rulesync/pull/3818)

### New Features

- **hooks (JetBrains Junie):** canonical `postToolUse` maps to Junie's `PostToolUse` event, with its tool-name matcher. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3810](https://github.com/dyoshikawa/rulesync/pull/3810)
- **hooks (Qwen Code):** canonical `fileChanged` maps to Qwen Code's `FileChanged` event (v0.27.0), with its matcher. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3809](https://github.com/dyoshikawa/rulesync/pull/3809)
- **mcp (OpenCode):** the per-server `pool` key (OpenCode 2.2.6) is passed through on generate when a canonical server carries it. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3811](https://github.com/dyoshikawa/rulesync/pull/3811)
- **mcp (Kimi Code):** the stdio `environment_id` key (Kimi Code 2.5.0) is passed through on generate and validated; `runtime_id` is still passed through unchanged for 2.2–2.4. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3812](https://github.com/dyoshikawa/rulesync/pull/3812)
- **permissions (Devin Desktop):** `devin.permission_mode` (`normal` / `accept-edits` / `smart` / `dangerous`) can be authored through the `devin` override. It is written to the user config on `--global` generate only and is never derived from canonical rules. `dangerous` warns on generate and import, and a project-config value is skipped on import. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3816](https://github.com/dyoshikawa/rulesync/pull/3816)
- **permissions (Codex CLI):** new opt-in `codexcli.bash_canonical_matching`. When `true`, it writes `canonical_matching = True` on the generated `forbidden` / `prompt` rules (never on allows), so case and Unicode look-alike spellings cannot slip past them. Requires Codex 0.167.0 or later. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3817](https://github.com/dyoshikawa/rulesync/pull/3817)

### Documentation

- **permissions (AugmentCode):** `recommendedMarketplaces` is documented as read by Auggie 0.x only; it is still emitted. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3815](https://github.com/dyoshikawa/rulesync/pull/3815)

### Internal

- Recorded the 2026-11-08 new-target watchlist re-check. by [@dyoshikawa](https://github.com/dyoshikawa) in [#3808](https://github.com/dyoshikawa/rulesync/pull/3808)

## Contributors

**Full Changelog**: `v43.7.0...v43.8.0`
