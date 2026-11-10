---
title: "Using Kimi in Codex"
date: "2024-11-01"
url: "https://www.kimi.com/code/docs/en/third-party-tools/codex.html"
site: "kimi.com"
type: "doc"
via: "direct"
---
# Using Kimi in Codex [](https://www.kimi.com#using-kimi-in-codex)

[Codex](https://openai.com/codex/) is OpenAI's coding agent. The Kimi Code server natively supports the OpenAI Responses API (streaming and non-streaming, reasoning, and function calling all work), so Codex CLI and the Codex desktop app can connect directly with a custom model provider — no local routing or protocol-translation tool is needed. This guide covers the configuration.

The OpenAI Responses API supports text and image input, but not video input. To analyze video, extract key frames with ffmpeg first.


## Membership [](https://www.kimi.com#membership)

Introducing the K3.1 Pro series

**K3.1 Pro** is now fully rolled out in Kimi Code. It is our most capable 3T-class model to date, with a 1-million-token context window and substantial improvements in coding, 3D creation, financial research, and other long-horizon agent capabilities.

We also launched **K3.1 Pro Highspeed**. With the same model quality, it delivers approximately 2–3× the speed of K3.1 Pro for more responsive interactions.

**Note**: K3.1 Pro models only support thinking mode, and requests with thinking disabled are rejected. Start a new session and use the Kimi Coding Plan's native API protocols for the most stable results; protocol conversion through proxy tools may cause behavior to vary.

Before configuring, check your membership tier (see [Membership Benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html#plan-comparison) for a comparison of the legacy and new plans) and pick a model from the table below:

| Tier | Available models | Context window | 
|---|---|---|
| Go (new plans) | No coding quota | — | 
| Andante (legacy plans) | `kimi-for-coding` | `1048576` | 
| Plus / Moderato | `k3.1-pro` `k3` `k3-256k` `kimi-for-coding` | `k3.1-pro`: `262144` `k3`: `262144` `k3-256k`: `262144` `kimi-for-coding`: `1048576` | 
| Pro and above / Allegretto and above | `k3.1-pro` `k3.1-pro-highspeed` `k3` `k3-256k` `kimi-for-coding` `kimi-for-coding-highspeed` | `k3.1-pro`: `1048576` `k3.1-pro-highspeed`: `1048576` `k3`: `1048576` `k3-256k`: `262144` `kimi-for-coding`: `1048576` `kimi-for-coding-highspeed`: `262144` | 

## Prerequisites [](https://www.kimi.com#prerequisites)

1. Create and save an API Key in the [Kimi Code Console](https://www.kimi.com/code/console).
2. Install Codex CLI:

`npm install -g @openai/codex`
## Step 1: Create the model catalog models.json [](https://www.kimi.com#step-1-create-the-model-catalog-models-json)

Create `models.json` in the Codex config directory:

`~/.codex/models.json``C:\Users\<username>\.codex\models.json`
Write the following content (K3.1 Pro models shown as examples):

```
{
  "models": [
    {
      "slug": "k3.1-pro",
      "display_name": "K3.1 Pro",
      "description": "K3.1 Pro, 1M context",
      "default_reasoning_level": "high",
      "supported_reasoning_levels": [
        { "effort": "low", "description": "Light reasoning" },
        { "effort": "high", "description": "Enhanced reasoning" },
        { "effort": "max", "description": "Deep reasoning" }
      ],
      "shell_type": "shell_command",
      "apply_patch_tool_type": "freeform",
      "visibility": "list",
      "supported_in_api": true,
      "priority": 0,
      "base_instructions": "",
      "supports_reasoning_summaries": true,
      "default_reasoning_summary": "none",
      "support_verbosity": false,
      "truncation_policy": { "mode": "bytes", "limit": 10000 },
      "context_window": 1048576,
      "max_context_window": 1048576,
      "effective_context_window_percent": 95,
      "supports_parallel_tool_calls": true,
      "experimental_supported_tools": [],
      "input_modalities": ["text", "image"]
    },
    {
      "slug": "k3.1-pro-highspeed",
      "display_name": "K3.1 Pro Highspeed",
      "description": "K3.1 Pro Highspeed, 1M context",
      "default_reasoning_level": "high",
      "supported_reasoning_levels": [
        { "effort": "low", "description": "Light reasoning" },
        { "effort": "high", "description": "Enhanced reasoning" },
        { "effort": "max", "description": "Deep reasoning" }
      ],
      "shell_type": "shell_command",
      "apply_patch_tool_type": "freeform",
      "visibility": "list",
      "supported_in_api": true,
      "priority": 1,
      "base_instructions": "",
      "supports_reasoning_summaries": true,
      "default_reasoning_summary": "none",
      "support_verbosity": false,
      "truncation_policy": { "mode": "bytes", "limit": 10000 },
      "context_window": 1048576,
      "max_context_window": 1048576,
      "effective_context_window_percent": 95,
      "supports_parallel_tool_calls": true,
      "experimental_supported_tools": [],
      "input_modalities": ["text", "image"]
    }
  ]
}
```
## Step 2: Write config.toml [](https://www.kimi.com#step-2-write-config-toml)

Path of the Codex CLI config file:

`~/.codex/config.toml``C:\Users\<username>\.codex\config.toml`
Write the following content (create the file if it does not exist):

```
model = "k3.1-pro"
model_provider = "kimi"
web_search = "live"
model_catalog_json = "~/.codex/models.json"
[model_providers.kimi]
name = "Kimi"
base_url = "https://api.kimi.ai/coding/v1"
env_key = "KIMI_API_KEY"
wire_api = "responses"
[desktop]
enabled-reasoning-efforts = ["low", "high", "max"]
```
Field reference:

| Field | Description | 
|---|---|
| `model` | Default model, shown here as `k3.1-pro`; use `k3.1-pro-highspeed` for faster output. Both support up to 1M context | 
| `model_provider` | Default provider, matching the `[model_providers.kimi]` table below | 
| `web_search` | Web search switch. The Kimi Code endpoint supports web search; set to `"live"` to enable real-time search | 
| `model_catalog_json` | Path of the model catalog created in the previous step, declaring each model's context window and image input support | 
| `base_url` | Kimi Code API address — China `https://api.kimi.com/coding/v1`, Overseas `https://api.kimi.ai/coding/v1` | 
| `env_key` | The **name** of the environment variable holding the API Key (`KIMI_API_KEY` here — the Key itself goes elsewhere). Codex reads the secret from this variable at startup; you set its value in the next step | 
| `wire_api` | Wire protocol, must be `"responses"` to use the Responses API | 
| `enabled-reasoning-efforts` | Reasoning levels shown in the desktop model picker; desktop only — the CLI does not need this | 

## Step 3: Set the API Key [](https://www.kimi.com#step-3-set-the-api-key)

The recommended approach is an environment variable (the `env_key` above): the config file contains no plaintext secret, so it can be shared and backed up safely. This is also the officially recommended approach by Codex.

Pick the command for your operating system:

```
echo 'export KIMI_API_KEY="sk-kimi-your-key"' >> ~/.zshrc
source ~/.zshrc
```
```
echo 'export KIMI_API_KEY="sk-kimi-your-key"' >> ~/.bashrc
source ~/.bashrc
```
`setx KIMI_API_KEY "sk-kimi-your-key"`
One more step is required for the Codex desktop app: apps launched from the Dock or Finder do not inherit environment variables from your terminal, so the Key must be injected into the current user session. Run in a terminal:

`launchctl setenv KIMI_API_KEY "sk-kimi-your-key"`
After running it, **fully quit** the desktop app (Cmd+Q) and reopen it for the change to take effect. Note: the variable does not survive a reboot — run the command again after restarting. Windows does not need this step: `setx` writes a system environment variable, and restarting the app is enough.

### Alternative: write the Key into the config (experimental\_bearer\_token) [](https://www.kimi.com#alternative-write-the-key-into-the-config-experimental-bearer-token)

If environment variables do not take effect (for example, GUI apps cannot read them, or CI environments make injection inconvenient), use `experimental_bearer_token` to write the Key directly into the provider config, replacing `env_key`:

```
[model_providers.kimi]
name = "Kimi"
base_url = "https://api.kimi.ai/coding/v1"
wire_api = "responses"
experimental_bearer_token = "sk-kimi-your-key"
```
Plaintext secret risk

With this approach the Key is stored in **plaintext** in the config file. Do not commit the file to a version-control repository or share it publicly in dotfiles — weigh the trade-off yourself. Do not configure `env_key` and `experimental_bearer_token` at the same time.

## Step 4: Launch and verify [](https://www.kimi.com#step-4-launch-and-verify)

Open a new terminal, switch to the project directory, and start Codex:

```
cd /path/to/your/project
codex
```
Send a `hello` message in the session — a normal reply means the configuration works.

Signs of a successful setup:

- The startup banner shows `model: k3.1-pro` (or your chosen model) and `provider: kimi`;
- The `Model metadata not found` warning no longer appears (models.json is in effect).

## Using the Codex desktop app [](https://www.kimi.com#using-the-codex-desktop-app)

The desktop app reads the same `~/.codex/models.json` and `~/.codex/config.toml` as the CLI. Follow the CLI configuration above through Step 3, then:

1. **(macOS only) Inject the environment variable**: GUI apps cannot read variables set in your terminal, so run the following command first to inject `KIMI_API_KEY` into the user session. On Windows, `setx` writes a system environment variable, so this step is not needed.
sh`launchctl setenv KIMI_API_KEY "sk-kimi-your-key"`
2. **Restart the desktop app**: fully quit (Cmd+Q on macOS) and reopen it for the new configuration to load.
3. **Pick a model and start chatting**: select a Kimi model from the model picker in a new thread.

TIP

The desktop app automatically appends managed blocks (plugins, MCP servers, etc.) to `config.toml`. This is expected — your manually added Kimi Code configuration is preserved intact, and these auto-generated blocks should not be deleted.

## Switching reasoning effort [](https://www.kimi.com#switching-reasoning-effort)

K3.1 Pro models, the K3 series, and K2.8 Preview support `low` / `high` / `max`. In a Codex CLI session, type `/model` to re-select the current model, then choose a level from the **Select Reasoning Level** menu:

| Codex selection | Actual effort | 
|---|---|
| Not set (default) | `high` (K3.1 Pro default) / `high` (K3 series default) / `max` (K2.8 Preview default) | 
| `low` | `low` | 
| `high` | `high` | 
| `max` | `max` | 

K3.1 Pro models only support thinking mode, and disabling thinking returns 400. With thinking disabled, requests to the K3 series, K2.8 Preview, and K2.7 Code HighSpeed are served by K2.8 Preview without thinking.

After switching, start a new session to avoid extra cost from stale context caches.

## FAQ [](https://www.kimi.com#faq)

## Error: Missing environment variable: KIMI\_API\_KEY

The current process cannot read the environment variable. Make sure it is written to the correct shell config file and open a new terminal; on macOS for the desktop app, use the `launchctl` method from Step 3. If it still fails, switch to `experimental_bearer_token`.

## codex exec cannot run tool commands

In environments with a restricted user namespace (for example, bwrap reporting ENOSPC), Codex's default sandbox does not work. Add `--sandbox danger-full-access` to run tool commands: `codex exec --sandbox danger-full-access "your task"`. Note that this disables sandbox isolation — commands run directly in your real environment, so only use it with tasks from trusted sources.

## Next steps [](https://www.kimi.com#next-steps)

- [Model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html) — compare model capabilities and see the full effort mapping table
- [Membership](https://www.kimi.com/code/docs/en/kimi-code/membership.html) — check model availability and tier requirements
