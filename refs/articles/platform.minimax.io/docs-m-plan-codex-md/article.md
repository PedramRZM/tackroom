---
title: "Codex"
url: "https://platform.minimax.io/docs/m-plan/codex.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Codex

> Use the latest MiniMax M-series models in Codex.

[**Codex**](https://developers.openai.com/codex/) is OpenAI's AI coding agent. This guide covers setup for the Codex desktop app and CLI.

## Install Codex

For Codex CLI, use the setup wizard below. If it cannot find the `codex` command, it offers to install the official `@openai/codex` npm package.

For the desktop app, download and install it from the [OpenAI Codex page](https://developers.openai.com/codex/).

## Configure MiniMax API

> [tab] Option 1: Setup wizard
>
> Run:
>
> ```bash theme={null}
> npx -y mmx-cli@latest agent setup
> ```
>
> Select **Codex**. If Codex CLI is missing, the wizard offers to install it. **Codex CLI 0.146.0 or newer** is recommended. The wizard configures `~/.codex/config.toml` and `~/.codex/mmx-model-catalog.json`.
>
> Close Codex and any editor that has `~/.codex/config.toml` open before running the wizard. This prevents another process from saving stale contents over the configuration it just wrote.
>
> Restart Codex after setup. See [MiniMax CLI](https://platform.minimax.io/docs/m-plan/minimax-cli.md) for command options and backup behavior.

> [tab] Option 2: Manual setup
>
> **1. Edit the config file**
>
> Open `~/.codex/config.toml` and add or update the following entries, replacing `<MINIMAX_API_KEY>` with your M Plan API key from [Plan Details](https://platform.minimax.io/console/plan):
>
> ```toml theme={null}
> model = "MiniMax-M3.1-Flash"
> model_provider = "minimax"
> model_context_window = 524288
> preferred_auth_method = "apikey"
> forced_login_method = "api"
>
> [model_providers.minimax]
> name = "MiniMax"
> base_url = "https://api.minimax.io/v1"
> experimental_bearer_token = "<MINIMAX_API_KEY>"
> wire_api = "responses"
> ```
>
> `preferred_auth_method` and `forced_login_method` select API Key authentication. To show model capabilities and reasoning levels in `/model`, you can also add the optional catalog below.
>
> **2. Restart Codex and start using MiniMax-M3.1-Flash**
>
> Restart Codex to start using MiniMax-M3.1-Flash.
>
> ### Configure model capabilities (optional)
>
> For manual setup, you can add a model capability catalog so Codex shows MiniMax-M3.1-Flash and its reasoning levels in `/model`.
>
> Add this line to `~/.codex/config.toml`:
>
> ```toml theme={null}
> model_catalog_json = "~/.codex/model-catalogs/custom-catalog.json"
> ```
>
> Then create `~/.codex/model-catalogs/custom-catalog.json` with the model configuration:
>
> ```json theme={null}
> {
>   "models": [
>     {
>       "slug": "MiniMax-M3.1-Flash",
>       "display_name": "MiniMax-M3.1-Flash",
>       "description": "MiniMax M3.1 Flash",
>       "default_reasoning_level": "max",
>       "supported_reasoning_levels": [
>         { "effort": "low", "description": "Low" },
>         { "effort": "medium", "description": "Medium" },
>         { "effort": "high", "description": "High" },
>         { "effort": "xhigh", "description": "Extra high" },
>         { "effort": "max", "description": "Maximum" }
>       ],
>       "shell_type": "shell_command",
>       "visibility": "list",
>       "supported_in_api": true,
>       "priority": 0,
>       "base_instructions": "You are Codex, a coding agent based on MiniMax-M3.1-Flash. You and the user share the same workspace and collaborate to achieve the user's goals.",
>       "supports_reasoning_summaries": true,
>       "default_reasoning_summary": "none",
>       "support_verbosity": false,
>       "truncation_policy": { "mode": "tokens", "limit": 10000 },
>       "supports_parallel_tool_calls": true,
>       "experimental_supported_tools": [],
>       "prefer_websockets": false,
>       "apply_patch_tool_type": "freeform",
>       "web_search_tool_type": "text",
>       "supports_image_detail_original": false,
>       "tool_mode": "code_mode_only",
>       "multi_agent_version": "v2",
>       "use_responses_lite": false,
>       "input_modalities": ["text", "image"],
>       "context_window": 524288,
>       "max_context_window": 524288,
>       "effective_context_window_percent": 95,
>       "auto_compact_token_limit": null,
>       "reasoning_summary_format": "experimental",
>       "supports_search_tool": true
>     }
>   ]
> }
> ```
>
> > [!WARNING]
> >
> > Do not add `{ "effort": "none" }` to `supported_reasoning_levels`. MiniMax-M3.1-Flash always thinks, so selecting that level makes Codex send `reasoning: {"effort": "none"}` and the API returns `400`.
>
> Common fields in this configuration:
>
> * `slug` / `display_name`: The model identifier and display name used in Codex config and the `/model` list. Keep this aligned with the model name used by the API.
> * `default_reasoning_level`: The default reasoning effort. MiniMax-M3.1-Flash uses `max` by default.
> * `supported_reasoning_levels`: Reasoning options users can switch between in `/model`. MiniMax-M3.1-Flash supports `low`, `medium`, `high`, `xhigh`, and `max`; `none` is not supported.
> * `base_instructions`: Base system prompt Codex adds when using this model. Use it to describe the model identity and collaboration style.
> * `supports_reasoning_summaries`: Enables Codex's Responses API reasoning path for this model. Set this to `true` so Codex sends `reasoning.effort`; otherwise Codex omits the `reasoning` field even when `default_reasoning_level` is configured. In this example, `default_reasoning_summary` is set to `none` so Codex does not request a separate reasoning summary.
> * `shell_type`: Declares the shell tool-call type supported by the model. This example uses `shell_command`.
> * `visibility` / `supported_in_api` / `priority`: Control whether the model appears in the list, whether it is available through the API, and its ordering priority in the model list.
> * `supports_parallel_tool_calls`: Indicates that the model supports parallel tool calls, allowing Codex to handle multiple tool requests.
> * `experimental_supported_tools`: Reserved list for experimental tool capabilities. Leave it as an empty array when no extra tools are needed.
> * `input_modalities`: Supported input modalities. `["text", "image"]` means text and image input are supported.
> * `truncation_policy`: Controls content truncation; this example counts tokens.
> * `context_window` / `max_context_window`: Set the client context window to the recommended 512K (524,288 tokens) in this example. See the [512K guidance](#context-window-512k).
> * `effective_context_window_percent` / `auto_compact_token_limit`: Use 95% of the window as the effective context budget without a separate fixed auto-compaction threshold.
>
> Restart Codex after changing the model catalog.
>
> ### Context window and cost optimization (optional)
>
> MiniMax-M3.1-Flash supports a context window of up to 1M tokens. For everyday coding and other multi-turn tasks, consider setting your tool's context window to **512K**. Managing and compacting conversation history earlier can reduce the number of historical tokens carried into subsequent requests. Use **1M** when your task requires retaining extensive code or document details throughout the conversation.
>
> #### Why consider 512K?
>
> In a ProgramBench comparison using MiniMax-M3.1-Flash, average model performance was similar with 512K and 1M context windows, while the estimated cost with 512K was approximately **20% lower**. Consider 512K as an optional configuration for everyday coding.
>
> **Model performance and usage across context windows**
>
> | Metric | 1M window | 512K window | 512K vs. 1M |
> | - | - | - | - |
> | Evaluation tasks | 200 | 200 | Same |
> | Model performance | Similar | Similar | No clear difference detected |
> | Average total tokens per task | 136.76 million | 111.42 million | **18.5% fewer** |
> | Estimated usage-based charges | 100% | 80.1% | **19.9% lower** |

