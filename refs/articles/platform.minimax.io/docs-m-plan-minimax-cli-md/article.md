---
title: "MiniMax CLI"
url: "https://platform.minimax.io/docs/m-plan/minimax-cli.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax CLI

> Install MiniMax CLI to use MiniMax multimodal and search capabilities from your terminal or AI agent.

MiniMax CLI (the `mmx` command) is MiniMax's official command-line tool. With an M Plan subscription, you can use MiniMax text, image, video, speech, vision, and web search capabilities directly in your terminal or let AI agents such as Claude Code and OpenClaw call them for you, with no code required. Available capabilities depend on your plan and CLI version.

MiniMax CLI requires Node.js 18 or later.

> [accordion] How to install Node.js
>
> Visit the [Node.js website](https://nodejs.org/en/download), then download and install the current LTS version. When installation finishes, reopen your terminal and run:
>
> ```bash theme={null}
> node --version
> npx --version
> ```
>
> If both commands show a version number, the installation was successful.

## Install and configure

> [tab] Install via an agent
>
> Send the prompt below to your AI agent to install the CLI and add the skill. Sign in yourself in the terminal; do not send your M Plan API key to the agent.
>
> ```text theme={null}
> Please set up MiniMax CLI (https://github.com/MiniMax-AI/cli) for me:
>
> 1. Install globally: run `npm install -g mmx-cli`, then verify with `mmx --version`.
> 2. Sign in: ask me to run `mmx auth login` in my local terminal. Do not ask for, print, or store my key in this conversation.
> 3. After I confirm sign-in is complete, install the official skill: run `npx skills add MiniMax-AI/cli -y -g`.
> 4. Finally, run `mmx quota` to confirm my M Plan usage is shown.
> ```

> [tab] Manual install
>
> **1. Install MiniMax CLI**
>
> ```bash theme={null}
> npm install -g mmx-cli
> ```
>
> **2. Sign in**
>
> Replace `sk-xxxxx` with your [M Plan API key](https://platform.minimax.io/console/plan):
>
> ```bash theme={null}
> mmx auth login --api-key sk-xxxxx
> ```
>
> MiniMax CLI detects the service region from your key. After signing in, run `mmx quota`; if your M Plan usage is shown, setup is complete. If API calls return 401, see [Troubleshooting](#troubleshooting).
>
> **3. Install the skill (optional)**
>
> To let AI agents call `mmx`, install the official skill so the agent knows how each command works:
>
> ```bash theme={null}
> npx skills add MiniMax-AI/cli -y -g
> ```
>
> The skill is linked into `~/.claude/skills/`, `~/.openclaw/skills/`, and similar directories, and takes effect after the agent restarts. Skip this step if you only use `mmx` in the terminal.

## Examples

After installing the skill, you can ask your agent in plain language to use MiniMax CLI, or run the matching command in your terminal.

**Text**

* Ask your agent: `Use MiniMax to write a four-line poem about AI`
* Terminal command: `mmx text chat --message "Write a four-line poem about AI"`

**Video**

* Ask your agent: `Generate a video: at sunset, a cat sits by the window looking into the distance`
* Terminal command: `mmx video generate --prompt "At sunset, a cat sits by the window looking into the distance"`

**Image**

* Ask your agent: `Generate a cyberpunk city night scene in 16:9`
* Terminal command: `mmx image generate --prompt "Cyberpunk city night scene" --aspect-ratio 16:9`

When no output option is specified, images are saved to the current working directory. Use `--out` for a single output path or `--out-dir` for batch output.

**Speech**

* Ask your agent: `Read in a gentle female voice: Welcome to MiniMax M Plan. With a subscription, your agent can generate video, speech, and images.`
* Terminal command: `mmx speech synthesize --text "Welcome to MiniMax M Plan. With a subscription, your agent can generate video, speech, and images." --out voiceover.mp3`

## CLI dashboard

Run `mmx` with no arguments to open the CLI dashboard, which shows the main commands, options, and usage.

![MiniMax CLI dashboard](https://file.cdn.minimax.io/public/agent-tool/mmx-cli/20260903-211340.png)

* **resources**: resource types you can call
* **flags**: options supported by commands
* **usage**: current plan usage
* **help**: usage instructions

## Command reference

| Capability | Command | Description |
| - | - | - |
| Text | `mmx text chat` | Multi-turn chat, streaming output, system prompts, JSON output |
| Image | `mmx image generate` | Text-to-image with aspect ratio control and batch generation |
| Video | `mmx video generate` | Asynchronous video generation with task status and download |
| Speech | `mmx speech synthesize` | Text-to-speech with multiple voices and streaming |
| Vision | `mmx vision describe` | Image understanding from local files, URLs, or file IDs |
| Search | `mmx search query` | Web search |

> [accordion] More management commands
>
> | Command | Purpose | Example |
> | - | - | - |
> | `mmx auth status / refresh / logout` | Show sign-in identity / refresh credentials / sign out | `mmx auth status` |
> | `mmx config show / set` | View or change configuration (service region, default model, etc.) | `mmx config set --key region --value global` |
> | `mmx agent setup` | Configure MiniMax in AI coding tools | `mmx agent setup` |
> | `mmx quota` | View M Plan usage and remaining quota | `mmx quota` |
> | `mmx update` | Show the current version and upgrade hint | `mmx update` |

## Setup wizard

The setup wizard verifies your key, installs missing tools if you choose, and adds MiniMax to the configuration of the AI coding tools you select. It currently supports Claude Code, Codex CLI, OpenCode, Grok CLI, Hermes Agent, and Pi.

### Configure with the wizard

**1. Get your M Plan API key**

Get your M Plan API key from [Plan Details](https://platform.minimax.io/console/plan).

The wizard also accepts pay-as-you-go API Keys. M Plan API keys (`sk-cp-...`) and pay-as-you-go API Keys (`sk-api-...`) are billed separately, and the wizard asks which type you are using.

**2. Run the wizard**

```bash theme={null}
npx -y mmx-cli@latest agent setup
```

Select the tools to configure. If a selected tool is not detected on `PATH`, another prompt asks which missing tools to install. Then choose the service region and key type, and paste your key.

After you confirm, the wizard verifies the key, then shows and runs the official package or installer script. It checks each installed tool before writing the MiniMax configuration. If installation fails, you can skip it and continue writing the configuration.

**3. Start your tool**

After setup succeeds, start the selected tool, such as `claude`, `codex`, or `opencode`, to use MiniMax models.

Automatic installation supports macOS, Linux, and Windows. All tools except Pi currently require an arm64 or x64 system.

> [accordion] View installer sources and commands
>
> > [tab] macOS / Linux
> >
> > **Claude Code**
> >
> > ```bash theme={null}
> > curl -fsSL https://claude.ai/install.sh | bash
> > ```
> >
> > **Codex CLI**
> >
> > ```bash theme={null}
> > npm install -g @openai/codex
> > ```
> >
> > **Grok CLI**
> >
> > ```bash theme={null}
> > curl -fsSL https://x.ai/cli/install.sh | bash
> > ```
> >
> > **OpenCode**
> >
> > ```bash theme={null}
> > npm install -g opencode-ai
> > ```
> >
> > **Pi**
> >
> > ```bash theme={null}
> > npm install -g --ignore-scripts --engine-strict @earendil-works/pi-coding-agent
> > ```
> >
> > For Hermes Agent, the wizard runs the non-interactive core CLI stages of the [official installer](https://hermes-agent.nousresearch.com/install.sh) and skips optional flows such as `setup` and `gateway`.
>
> > [tab] Windows
> >
> > **Claude Code**
> >
> > ```powershell theme={null}
> > irm https://claude.ai/install.ps1 | iex
> > ```
> >
> > **Codex CLI**
> >
> > ```powershell theme={null}
> > npm install -g @openai/codex
> > ```
> >
> > **Grok CLI**
> >
> > ```powershell theme={null}
> > irm https://x.ai/cli/install.ps1 | iex
> > ```
> >
> > **OpenCode**
> >
> > ```powershell theme={null}
> > npm install -g opencode-ai
> > ```
> >
> > **Pi**
> >
> > ```powershell theme={null}
> > npm install -g --ignore-scripts --engine-strict @earendil-works/pi-coding-agent
> > ```
> >
> > For Hermes Agent, the wizard runs the non-interactive core CLI stages of the [official PowerShell installer](https://hermes-agent.nousresearch.com/install.ps1) and skips Computer Use and other optional flows.

### Non-interactive mode

Pass options after the npx command to run the wizard non-interactively, for example in scripts. Non-interactive mode only writes configuration and does not install tools. You must specify the tools, key, and service region:

```bash theme={null}
npx -y mmx-cli@latest agent setup \
  --agent claude-code \
  --agent codex \
  --api-key "$MINIMAX_API_KEY" \
  --region global
```

Use `--all` to configure every supported tool. Add `--dry-run` to preview the files that would change; it does not make network requests, install tools, or write files.

| Option | Description |
| - | - |
| `--agent <name>` | Select one tool; repeat to select more |
| `--all` | Select every supported tool |
| `--api-key <key>` | M Plan API key or pay-as-you-go API Key |
| `--region cn\|global` | Service region; use `global` for the overseas service |
| `--model <model>` | Default model to write |
| `--dry-run` | Preview only; do not verify the key or write files |
| `--output json` | Return JSON for scripts |

### Configuration files

| Tool | Configuration files |
| - | - |
| Claude Code | `~/.claude/settings.json` |
| Codex | `~/.codex/config.toml`, `~/.codex/mmx-model-catalog.json` |
| Grok CLI | `~/.grok/config.toml` |
| OpenCode | `~/.config/opencode/opencode.json` or `opencode.jsonc` |
| Hermes Agent | `~/.hermes/config.yaml`, `~/.hermes/.env` |
| Pi | `~/.pi/agent/models.json`, `~/.pi/agent/settings.json` |

When writing configuration, the wizard:

* Updates only the MiniMax configuration of the selected tools and keeps other providers and unrelated settings
* Creates a timestamped `.bak` backup before changing an existing file
* Makes configuration files readable and writable only by the current user (except on Windows)
* Restores the files it changed if any step fails

## Troubleshooting

> [accordion] API calls return 401 after sign-in
>
> The service region was probably not detected. Set the overseas region manually, then check the active region:
>
> ```bash theme={null}
> mmx config set --key region --value global
> mmx auth status
> ```

> [accordion] The agent setup command is missing
>
> Make sure Node.js 18 or later is installed, then run `npx -y mmx-cli@latest agent setup` again. If your local `mmx` is outdated, you can use this npx command instead.

> [accordion] A tool shows not detected on PATH
>
> The wizard did not find the tool in the current terminal's `PATH`. In interactive mode, it checks the installation requirements and asks whether to install each eligible tool.

> [accordion] The installation choices do not appear
>
> The install list does not appear when the tool is already installed, the wizard is running non-interactively, or the environment does not meet the installation requirements. The wizard lists missing commands or unsupported architectures; Pi also requires Node.js 22.19 or later.

> [accordion] Installation fails
>
> The wizard shows the command it ran and the error. For npm permission errors with Codex, OpenCode, or Pi, see the [npm documentation](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally). You can also skip installation and continue writing the configuration.

> [accordion] The tool still connects to another service
>
> Check for environment variables that override configuration files, such as `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` for Claude Code, or `OPENAI_API_KEY` and `OPENAI_BASE_URL` for Grok CLI.

> [accordion] Codex already uses a custom model catalog
>
> If `model_catalog_json` in `~/.codex/config.toml` points to a custom file, the wizard stops without changing any files. Keep the catalog and configure Codex manually, or remove that setting and try again.

