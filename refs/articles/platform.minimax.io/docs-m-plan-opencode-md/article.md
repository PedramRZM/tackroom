---
title: "OpenCode"
url: "https://platform.minimax.io/docs/m-plan/opencode.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenCode

> Use the latest MiniMax M-series models in OpenCode.

[**OpenCode**](https://github.com/sst/opencode) is an open-source terminal AI coding agent by SST, with multi-provider support and LSP integration.

> [tab] Option 1: Setup wizard
>
> Run:
>
> ```bash theme={null}
> npx -y mmx-cli@latest agent setup
> ```
>
> Select **OpenCode**. If OpenCode isn't installed, select it again when prompted to choose which tools to install. The wizard installs the official npm package, verifies its version, and sets a MiniMax default model.
>
> Run `opencode` when setup finishes.

> [tab] Option 2: Manual setup
>
> **1. Install OpenCode**
>
> ```bash theme={null}
> curl -fsSL https://opencode.ai/install | bash
> # or: npm i -g opencode-ai
> ```
>
> **2. Authenticate**
>
> Run `opencode auth login`, then when prompted, search and pick **MiniMax Token Plan (minimax.io)** (the provider name in OpenCode), and enter your [M Plan API key](https://platform.minimax.io/console/plan).
>
> **3. Launch**
>
> Run `opencode` and select `MiniMax-M3.1-Flash` from the model list. If your version does not list it, add the following to `~/.config/opencode/opencode.json` and run it again:
>
> ```json theme={null}
> {
>   "$schema": "https://opencode.ai/config.json",
>   "provider": {
>     "minimax-coding-plan": {
>       "models": {
>         "MiniMax-M3.1-Flash": {
>           "name": "MiniMax-M3.1-Flash",
>           "limit": { "context": 524288, "output": 131072 }
>         }
>       }
>     }
>   }
> }
> ```
>
> This example sets a **512K (524288 tokens)** client context window to balance cost and usability; the model itself supports up to 1M. See the [512K guidance](https://platform.minimax.io/docs/m-plan/codex.md#context-window-512k).
>
> Both `context` and `output` are required inside `limit`. Leaving either one out makes OpenCode fail validation and refuse to start. `output` is the maximum tokens per response; OpenCode may lower it further based on its own ceiling and the room left in the context window, so setting the model's absolute maximum has no effect.
>
> > [accordion] When configuring through tools such as CC Switch
> >
> > When using third-party tools such as CC Switch to configure MiniMax in OpenCode, check that the protocol and Base URL match. For the Anthropic-compatible protocol (`@ai-sdk/anthropic`), use `https://api.minimax.io/anthropic/v1` as the Base URL.
> >
> > To adjust the configuration manually, open `~/.config/opencode/opencode.json` and add or update these fields:
> >
> > * `provider.minimax-coding-plan.npm`: set to `@ai-sdk/anthropic`.
> > * `provider.minimax-coding-plan.options.baseURL`: set to `https://api.minimax.io/anthropic/v1`.
> >
> > The example below shows where these two fields belong and retains the `models` configuration from the preceding example. Merge these two changes into your existing configuration, keeping your M Plan API key, other models, and settings unchanged:
> >
> > ```json theme={null}
> > {
> >   "provider": {
> >     "minimax-coding-plan": {
> >       "npm": "@ai-sdk/anthropic",
> >       "options": {
> >         "baseURL": "https://api.minimax.io/anthropic/v1"
> >       },
> >       "models": {
> >         "MiniMax-M3.1-Flash": {
> >           "name": "MiniMax-M3.1-Flash",
> >           "limit": { "context": 524288, "output": 131072 }
> >         }
> >       }
> >     }
> >   }
> > }
> > ```
> >
> > This adapter appends `/messages` to the Base URL, so keep `/anthropic/v1`. When changing protocols, also check that the Base URL matches.

## Troubleshooting

> [accordion] Web search (web-search) not working?
>
> Some older versions of OpenCode may not enable web search by default, so the model falls back to fetching pages repeatedly or running curl. If this happens, enable web search by setting the environment variables described in the [OpenCode documentation](https://opencode.ai/docs/tools/#websearch).

