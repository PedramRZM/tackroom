---
title: "Claude Code"
url: "https://platform.minimax.io/docs/m-plan/claude-code.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code

> Use the latest MiniMax M-series models in Claude Code.

[**Claude Code**](https://github.com/anthropics/claude-code) is Anthropic's official terminal-native coding agent powered by Claude.

## Install Claude Code

You can skip this section when using the setup wizard below. If it cannot find the `claude` command, it offers to run the official Claude Code installer.

Refer to the [Claude Code documentation](https://code.claude.com/docs/en/setup) for installation.

## Configure MiniMax API

> [!WARNING]
>
> Before configuring, clear these environment variables. They take priority over the settings file and override the MiniMax configuration:
>
> ```bash theme={null}
> unset ANTHROPIC_AUTH_TOKEN
> unset ANTHROPIC_BASE_URL
> ```
>
> If `~/.bashrc` or `~/.zshrc` exports them, remove those lines too, or new shells will load them again.

> [tab] Option 1: Setup wizard
>
> Run:
>
> ```bash theme={null}
> npx -y mmx-cli@latest agent setup
> ```
>
> Select **Claude Code**. If Claude Code isn't installed, select it again when prompted to choose which tools to install. The wizard runs the official installer, checks `claude --version`, updates `~/.claude/settings.json`, and adds the MiniMax model list.
>
> See [MiniMax CLI](https://platform.minimax.io/docs/m-plan/minimax-cli.md) for command options and backup behavior.

> [tab] Option 2: Edit the settings file
>
> 1. Edit or create `~/.claude/settings.json` and replace `<MINIMAX_API_KEY>` with your [M Plan API key](https://platform.minimax.io/console/plan):
>
>    ```json theme={null}
>    {
>      "env": {
>        "ANTHROPIC_BASE_URL": "https://api.minimax.io/anthropic",
>        "ANTHROPIC_AUTH_TOKEN": "<MINIMAX_API_KEY>",
>        "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "524288",
>        "CLAUDE_CODE_EFFORT_LEVEL": "max",
>        "ANTHROPIC_MODEL": "MiniMax-M3.1-Flash[1m]",
>        "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M3.1-Flash[1m]",
>        "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M3.1-Flash[1m]",
>        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M3.1-Flash[1m]"
>      }
>    }
>    ```
>
> 2. Go to your working directory, run `claude`, and select **Trust This Folder** to start.
>
> The manual example uses the recommended 512K auto-compaction window (`CLAUDE_CODE_AUTO_COMPACT_WINDOW=524288`). See the [512K guidance](https://platform.minimax.io/docs/m-plan/codex.md#context-window-512k). It also sets reasoning effort to `max` (`CLAUDE_CODE_EFFORT_LEVEL`); see "How to adjust reasoning effort" below.

> [tab] Option 3: Use CC Switch
>
> [CC Switch](https://github.com/farion1231/cc-switch) lets you switch Claude Code API providers.
>
> 1. Install CC Switch: on macOS / Linux, run `brew tap farion1231/ccswitch && brew install --cask cc-switch`; on Windows, download it from [GitHub Releases](https://github.com/farion1231/cc-switch/releases).
>
> 2. Open CC Switch, click **+**, select the MiniMax preset, and enter your [M Plan API key](https://platform.minimax.io/console/plan).
>
> 3. Set all model names to `MiniMax-M3.1-Flash` and select **Declare 1M**.
>
> 4. Add the following two entries to the provider configuration JSON's `env`, then click **Add**:
>
>    ```json theme={null}
>    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "524288",
>    "CLAUDE_CODE_EFFORT_LEVEL": "max"
>    ```
>
>    * `CLAUDE_CODE_AUTO_COMPACT_WINDOW`: the recommended 512K auto-compaction window. See the [512K guidance](https://platform.minimax.io/docs/m-plan/codex.md#context-window-512k).
>    * `CLAUDE_CODE_EFFORT_LEVEL`: the default reasoning effort. See "How to adjust reasoning effort" below.
>
> 5. Return to the home screen and click **Enable**.

To add web search, see [Web Search MCP](https://platform.minimax.io/docs/m-plan/mcp-guide.md).

## Verify the configuration

After starting `claude`, run the following slash commands inside the TUI to confirm Claude Code is using MiniMax instead of the default Claude provider:

```text theme={null}
/status
/model
```

* `/status` should show the `ANTHROPIC_BASE_URL` pointing to `api.minimax.io/anthropic`.
* `/model` should show the active model as `MiniMax-M3.1-Flash`.

> [accordion] How to adjust reasoning effort
>
> Thinking is always enabled for MiniMax-M3.1-Flash and cannot be disabled. Reasoning effort controls thinking depth. Choose from `low`, `medium`, `high`, `xhigh`, or `max`. Higher reasoning effort can increase response time and usage.
>
> * **Default level**: set by `CLAUDE_CODE_EFFORT_LEVEL` in `env` of `~/.claude/settings.json`. The Option 2 and Option 3 examples set it to `max`. When it is not set, Claude Code uses `high`.
> * **Switch during a session**: run `/effort` to pick a level, or run `/effort <level>` directly, for example `/effort low`. You can also start with `claude --effort <level>`, which applies to that session only. While `CLAUDE_CODE_EFFORT_LEVEL` is set, `/effort` in a session has no effect; remove the variable first if you want to switch in a session.
> * Some Claude Code versions send `xhigh` as `high`; use `max` if you need deeper thinking.
> * Settings that turn thinking off, such as `MAX_THINKING_TOKENS=0` or `"alwaysThinkingEnabled": false`, have no effect on MiniMax-M3.1-Flash; the model still thinks.

