---
title: "Other tools"
url: "https://platform.minimax.io/docs/m-plan/other-tools.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Other tools

> Use the latest MiniMax M-series models in other AI tools.

If your tool has no dedicated guide but accepts a custom Base URL and API Key, use the values below.

## Configuration reference

MiniMax exposes two protocols. Pick whichever your tool supports — most modern tools support at least one.

### OpenAI-compatible protocol

| Field | Value |
| - | - |
| **Provider** | `OpenAI Compatible` (sometimes called `Custom` or `OpenAI-format`) |
| **Base URL** | `https://api.minimax.io/v1` |
| **API Key** | [Get M Plan API key](https://platform.minimax.io/console/plan) |
| **Model ID** | `MiniMax-M3.1-Flash` |

### Anthropic-compatible protocol

| Field | Value |
| - | - |
| **Provider** | `Anthropic Compatible` (sometimes called `Claude` or `Custom Anthropic`) |
| **Base URL** | `https://api.minimax.io/anthropic` |
| **API Key** | [Get M Plan API key](https://platform.minimax.io/console/plan) |
| **Model ID** | `MiniMax-M3.1-Flash` |

## Protocol selection

| Tool style | Recommended protocol | Typical environment variables |
| - | - | - |
| Claude Code-style (TUI / CLI written for Anthropic) | Anthropic-compatible | `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` |
| Cursor / Continue / Aider / OpenAI-format IDE plugins | OpenAI-compatible | `OPENAI_BASE_URL` + `OPENAI_API_KEY` |
| Tools that ask for both | Either works — Anthropic-compatible is recommended for prompt-cache benefits | |

## Dify

[**Dify**](https://github.com/langgenius/dify) is an open-source LLM application development platform with workflows, RAG, agents, and observability.

**1. Install the plugin**

Open [Dify Cloud](https://cloud.dify.ai), sign in, and go to **Settings → Workspace → Model Provider**. Find **Minimax** and click **Install**.

**2. Configure your M Plan API key**

Click **Add API Key**, enter your [M Plan API key](https://platform.minimax.io/console/plan), set **API Base** to `https://api.minimax.io/anthropic`, and leave **Group ID** blank.

**3. Start using the model**

Save the settings to use MiniMax-M3.1-Flash in your workflows.

## Oh My Pi

[**Oh My Pi**](https://github.com/can1357/oh-my-pi) is an open-source terminal coding agent built on Pi, with integrated LSP, code editing, and subagents.

> [tab] Option 1: Setup wizard
>
> Run:
>
> ```bash theme={null}
> npx -y mmx-cli@latest agent setup
> ```
>
> Select **Oh my Pi (omp)**. If Oh My Pi isn't installed, select it again when prompted to choose which tools to install. The wizard runs the official installer, checks `omp --version`, and adds MiniMax models to Oh My Pi's models and defaults.
>
> Then launch Oh My Pi directly:
>
> ```bash theme={null}
> omp
> ```

> [tab] Option 2: Manual setup
>
> **1. Install Oh My Pi**
>
> Follow the [official Oh My Pi installation instructions](https://github.com/can1357/oh-my-pi#install), then run `omp --version` to verify the installation.
>
> **2. Configure MiniMax models**
>
> Edit or create `~/.omp/agent/models.yml` (`user directory\.omp\agent\models.yml` on Windows), replacing `<MINIMAX_API_KEY>` with your [M Plan API key](https://platform.minimax.io/console/plan). If the file already contains other providers, merge `minimax` into the existing `providers` mapping.
>
> ```yaml theme={null}
> providers:
>   minimax:
>     baseUrl: https://api.minimax.io/anthropic
>     apiKey: "<MINIMAX_API_KEY>"
>     api: anthropic-messages
>     auth: apiKey
>     models:
>       - id: MiniMax-M3.1-Flash
>         name: MiniMax-M3.1-Flash
>         reasoning: true
>         input: [text, image]
>         contextWindow: 524288
>         maxTokens: 131072
>         thinking:
>           mode: anthropic-adaptive
>           efforts: [low, medium, high, xhigh, max]
>           defaultLevel: max
>           requiresEffort: true
> ```
>
> This example uses the Anthropic-compatible protocol and sets the client context window to **512K (524288 tokens)**. See the [512K configuration guidance](https://platform.minimax.io/docs/m-plan/codex.md#context-window-512k). Thinking is always enabled for MiniMax-M3.1-Flash and cannot be disabled.
>
> **3. Verify and launch**
>
> Run the following commands to confirm that `MiniMax-M3.1-Flash` appears in the model list, then launch it:
>
> ```bash theme={null}
> omp models minimax
> omp --model minimax/MiniMax-M3.1-Flash:max
> ```
>
> To save it as the default, enter `/model` in a session and assign the model to the `default` role. For more options, see the [Oh My Pi model configuration docs](https://github.com/can1357/oh-my-pi/blob/main/docs/models.md).

## Cherry Studio

[**Cherry Studio**](https://github.com/CherryHQ/cherry-studio) is an open-source desktop client supporting 50+ LLM providers, with built-in MCP servers and 300+ assistants.

**1. Install**

Install Cherry Studio per the [official docs](https://docs.cherryai.com.cn/docs/en-us/cherry-studio/installation).

**2. Add MiniMax provider**

Open Cherry Studio → click **Choose other Providers** → search `MiniMax`, then pick **MiniMax**.

**3. Enter your M Plan API key**

Enter your [M Plan API key](https://platform.minimax.io/console/plan) (the API Host is prefilled), then click **Check** to verify.

**4. Pick the model**

Select `MiniMax-M3.1-Flash` from the model list.

## Chatbox

[**Chatbox**](https://github.com/chatboxai/chatbox) is a free, open-source, cross-platform AI client supporting advanced LLMs, custom API keys (BYOK), and AI agents across desktop, mobile, and web.

**1. Install Chatbox**

Install Chatbox per the [official docs](https://chatboxai.app/en/guide).

**2. Add MiniMax provider**

Open Chatbox → click **Settings** → click **Model Provider** → click **Add** → search `MiniMax`, then pick **MiniMax Global**.

**3. Enter your M Plan API key**

Enter your [M Plan API key](https://platform.minimax.io/console/plan) (the API Host is prefilled), then click **Check** next to **API Key** to verify the connection.

**4. Pick the model**

Select `MiniMax-M3.1-Flash` from the model list.

## Xcode

[**Xcode**](https://developer.apple.com/xcode/) is Apple's official IDE for macOS, iOS, iPadOS, watchOS, and visionOS, now with built-in Coding Intelligence.

**1. Install Xcode**

Install Xcode 26 or later from the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835).

**2. Add a model provider**

Open Xcode → top menu **Xcode → Settings → Intelligence → Add a Model Provider**, choose the **Internet Hosted** tab, and fill in:

* **URL**: `https://api.minimax.io` (bare host, no path)
* **API Key Header**: `Authorization` (override the default `x-api-key`)
* **API Key**: `Bearer <your M Plan API key>` (the word `Bearer`, **a single space**, then your `sk-cp-…` key — [get one here](https://platform.minimax.io/console/plan))
* **Description**: `MiniMax` (any value)

![Xcode Add a Model Provider dialog](https://file.cdn.minimax.io/public/xcode-provider-filled-en.png)

**3. Enable the model**

Click **Add**. Back in the Intelligence pane, open the new MiniMax provider and enable `MiniMax-M3.1-Flash`.

**4. Start chatting**

Open any project, press **⌘+0** to bring up the Coding Assistant, click the edit icon at the top-left to pick `MiniMax-M3.1-Flash`.

## Kilo Code

[**Kilo Code**](https://github.com/Kilo-Org/kilocode) is an open-source AI coding agent for VS Code, supporting multiple LLM providers and MCP servers.

> [!WARNING]
>
> First clear the `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` env vars — otherwise they will override the configuration.

**1. Install the extension**

Search `Kilo Code` in the VS Code Extensions panel and install.

**2. Configure MiniMax provider**

Open Kilo Code → **Settings**:

* **API Provider** = `MiniMax`
* **MiniMax Entrypoint** = `api.minimax.io`
* **MiniMax API Key** = your [M Plan API key](https://platform.minimax.io/console/plan)
* **Model** = `MiniMax-M3.1-Flash`

Click **Save** then **Done**.

## Zed

[**Zed**](https://github.com/zed-industries/zed) is an open-source, high-performance multiplayer code editor written in Rust by the Atom creators.

**1. Install Zed**

Install Zed per the [official docs](https://zed.dev/docs/getting-started).

**2. Add an LLM provider**

Settings → **LLM Provider** → **+Add Provider** → choose **OpenAI**, fill:

* **API URL** = `https://api.minimax.io/v1`
* **API Key** = your [M Plan API key](https://platform.minimax.io/console/plan)
* **Model Name** = `MiniMax-M3.1-Flash`

**3. Confirm your M Plan API key**

Click **Save Provider**. Then back in the LLM Provider list, click the new MiniMax entry, **re-enter your M Plan API key and press Enter** to confirm.

**4. Pick the model**

Return to the agent panel, click **Select a Model** at the bottom-right and pick `MiniMax-M3.1-Flash`.

## Grok CLI

[**Grok CLI**](https://github.com/superagent-ai/grok-cli) is an open-source terminal coding agent that connects to xAI's Grok and OpenAI-compatible providers.

> [!WARNING]
>
> First clear the `OPENAI_API_KEY` and `OPENAI_BASE_URL` env vars.

> [tab] Option 1: Setup wizard
>
> Run:
>
> ```bash theme={null}
> npx -y mmx-cli@latest agent setup
> ```
>
> Select **Grok CLI**. If Grok CLI isn't installed, select it again when prompted to choose which tools to install. The wizard runs the official Grok Build installer, checks `grok --version`, preserves unrelated settings, and adds a MiniMax model to `~/.grok/config.toml`.
>
> Run `grok` when setup finishes.

> [tab] Option 2: Manual setup
>
> **1. Install Grok CLI**
>
> ```bash theme={null}
> npm install -g grok-dev
> ```
>
> **2. Set environment variables and launch**
>
> ```bash theme={null}
> export GROK_BASE_URL=https://api.minimax.io/v1
> export GROK_API_KEY=sk-cp-...   # from M Plan
> grok --model MiniMax-M3.1-Flash
> ```

## Droid

[**Droid**](https://factory.ai) is Factory's official terminal coding agent that integrates with IDEs and developer collaboration tools.

> [!WARNING]
>
> First clear the `ANTHROPIC_AUTH_TOKEN` env var, otherwise it overrides the API Key in the settings file.

**1. Install Droid**

```bash theme={null}
curl -fsSL https://app.factory.ai/cli | sh        # macOS / Linux
# Windows:  irm https://app.factory.ai/cli/windows | iex
```

**2. Edit config file**

Add the following to `customModels` in `~/.factory/settings.json`, replacing `<MINIMAX_API_KEY>` with your M Plan API key:

```json theme={null}
{
  "customModels": [{
    "displayName": "MiniMax-M3.1-Flash",
    "model": "MiniMax-M3.1-Flash",
    "baseUrl": "https://api.minimax.io/anthropic",
    "apiKey": "<MINIMAX_API_KEY>",
    "provider": "anthropic",
    "maxOutputTokens": 64000
  }]
}
```

**3. Launch and pick model**

Launch `droid`, then `/model` and pick `MiniMax-M3.1-Flash`.

## Qwen Code

[**Qwen Code**](https://github.com/QwenLM/qwen-code) is Alibaba's open-source terminal coding agent optimized for the Qwen model family.

**1. Install Qwen Code**

Linux / macOS:

```bash theme={null}
bash -c "$(curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh)"
```

Windows (works in both Command Prompt and PowerShell):

```powershell theme={null}
powershell -Command "Invoke-WebRequest 'https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat' -OutFile (Join-Path $env:TEMP 'install-qwen.bat'); & (Join-Path $env:TEMP 'install-qwen.bat')"
```

**2. Launch and pick provider**

Run `qwen` in your terminal. Pick **Third-party Providers** → **MiniMax API Key** → region **International**.

**3. Enter your M Plan API key**

Enter your [M Plan API key](https://platform.minimax.io/console/plan) (prefix `sk-cp-…`) and press Enter.

**4. Confirm model IDs**

The default model ID should be `MiniMax-M3.1-Flash` — press Enter to submit and start chatting.

## Open WebUI

[**Open WebUI**](https://github.com/open-webui/open-webui) is a self-hosted, open-source AI chat platform with offline support, RAG, and multi-model runners.

**1. Install Open WebUI**

Install via Python pip (requires **Python 3.11** to avoid compatibility issues):

```bash theme={null}
pip install open-webui
open-webui serve
```

**2. Create admin account**

Open [http://localhost:8080](http://localhost:8080) in your browser and follow the prompt to create a local admin account.

**3. Add an OpenAI connection**

Click the avatar (top-right) → **Admin Panel** → top **Settings** tab → left **Connections**. In the **OpenAI** row, click **➕ Add Connection**, fill:

* **URL**: `https://api.minimax.io/v1`
* **Auth** (Bearer mode): your [M Plan API key](https://platform.minimax.io/console/plan) (prefix `sk-cp-…`)

**4. Pick the model**

Click **Save** and back in the chat view, pick `MiniMax-M3.1-Flash` from the top model selector to start chatting.

## nanobot

[**nanobot**](https://github.com/HKUDS/nanobot) is an ultra-lightweight open-source personal AI agent CLI from HKUDS, with chat channels, memory, and MCP support.

**1. Install nanobot**

```bash theme={null}
uv tool install nanobot-ai
# or:  pipx install nanobot-ai
# or:  pip install nanobot-ai          # may need --user or --break-system-packages on macOS
```

**2. Initialize**

```bash theme={null}
nanobot onboard
```

**3. Configure MiniMax in one shot**

Replace `sk-cp-...` with your [M Plan API key](https://platform.minimax.io/console/plan):

```bash theme={null}
python3 -c '
import json, os, sys
p = os.path.expanduser("~/.nanobot/config.json")
c = json.load(open(p))
c["providers"]["minimax"]["apiKey"] = sys.argv[1]
c["providers"]["minimax"]["apiBase"] = "https://api.minimax.io/v1"
c["agents"]["defaults"]["provider"] = "minimax"
c["agents"]["defaults"]["model"] = "MiniMax-M3.1-Flash"
json.dump(c, open(p, "w"), indent=2)
' sk-cp-...
```

**4. Launch**

```bash theme={null}
nanobot agent
```

## OpenHands

[**OpenHands**](https://github.com/All-Hands-AI/OpenHands) (formerly OpenDevin) is an open-source AI software-development agent by All-Hands-AI, with TUI, web GUI, and IDE integrations.

**1. Install OpenHands**

```bash theme={null}
pipx install openhands
```

**2. Configure MiniMax in one shot**

Replace `sk-cp-...` with your [M Plan API key](https://platform.minimax.io/console/plan):

```bash theme={null}
pipx run --spec openhands python -c '
import sys
from openhands_cli.stores.agent_store import AgentStore
AgentStore().create_and_save_from_settings(
    llm_api_key=sys.argv[1],
    settings={"llm_model": "openai/MiniMax-M3.1-Flash",
              "llm_base_url": "https://api.minimax.io/v1"},
)
' sk-cp-...
```

**3. Launch**

```bash theme={null}
openhands
```

## LangChain

[**LangChain**](https://github.com/langchain-ai/langchain) is the open-source framework by LangChain Inc. for building LLM-powered applications, with model adapters, retrieval, agents, and tracing.

**1. Install**

```bash theme={null}
pip install langchain-openai
```

**2. Use MiniMax via the OpenAI-compatible adapter**

Replace `sk-cp-...` with your [M Plan API key](https://platform.minimax.io/console/plan):

```python theme={null}
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="MiniMax-M3.1-Flash",
    api_key="sk-cp-...",
    base_url="https://api.minimax.io/v1",
)
print(llm.invoke("Hello").content)
```

## TRAE

[**TRAE**](https://www.trae.ai) is ByteDance's AI-native IDE with intelligent collaboration and agent automation.

**Install and launch TRAE**

**1. Download and install TRAE**

Download and install TRAE from [its website](https://www.trae.ai/?utm_source=content\&utm_medium=doc_minimax\&utm_campaign=minimax).

**2. Complete initial setup**

Launch TRAE. On first launch, the following screen appears:

![](https://filecdn.minimax.chat/public/ace1b07e-9296-43f1-87ff-e423795716fb.png)

**3. Start setup**

Click **Get Started** to begin setup.

For detailed instructions, see the [TRAE setup guide](https://docs.trae.ai/ide/set-up-trae?_lang=en).

**Configure MiniMax API**

> [!WARNING]
>
> **Clear OpenAI environment variables before configuration**
>
> Before configuring, ensure you clear the following OpenAI-related environment variables to avoid conflicts with MiniMax API:
>
> * `OPENAI_API_KEY`
> * `OPENAI_BASE_URL`

In TRAE, connect to MiniMax-M3.1-Flash with your [M Plan API key](https://platform.minimax.io/console/plan).

**1. Open settings**

At the top right of the chat panel, click the **Settings** icon, then **Models**.

**2. Select the Models tab**

Switch to the **Models** tab.

**3. Add a model**

Click **+ Add Model** to open the model configuration dialog.

Enter the following settings:

* Provider: Select **MiniMax-Global**
* Model: Select **MiniMax-M3.1-Flash**
* API Key: Enter your **[M Plan API key](https://platform.minimax.io/console/plan)**

**4. Save the model**

Click **Add Model**.

