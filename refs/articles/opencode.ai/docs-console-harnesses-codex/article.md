---
title: "Codex"
date: "2026-01-01"
url: "https://opencode.ai/docs/console/harnesses/codex/"
site: "opencode.ai"
type: "doc"
via: "direct"
---
# Codex

Codex speaks the OpenAI Responses API. Point it at Console and use any paid or Go model, including Claude, Gemini, and open models. Console translates the request for models that don’t accept Responses.

Add Console as a model provider in `~/.codex/config.toml` and make it the default.

```
model = "gpt-6.1-sol"
model_provider = "opencode"
[model_providers.opencode]
name = "OpenCode Console"
base_url = "https://opencode.ai/inference/openai/v1"
env_key = "OPENCODE_API_KEY"
wire_api = "responses"
```
Codex appends `/responses` to the base URL and reads the key from `env_key`. Create a
[personal API key](https://opencode.ai/docs/console/harnesses#get-an-api-key), then export it.

```
export OPENCODE_API_KEY="oc_sk_..."
codex
```
Use the Go base URL and a key from a workspace with a [Go](https://opencode.ai/docs/console/go) subscription.

```
model = "kimi-k3"
model_provider = "opencode-go"
[model_providers.opencode-go]
name = "OpenCode Go"
base_url = "https://opencode.ai/inference/go/openai/v1"
env_key = "OPENCODE_API_KEY"
wire_api = "responses"
```
Set `model` to any model ID from the [Console](https://opencode.ai/docs/console/models#endpoints) or [Go](https://opencode.ai/docs/console/go#endpoints) table. Override
it for one run with `--model`.

`codex --model claude-sonnet-5-5`
Codex doesn’t know the context window or reasoning settings of models outside its own catalog. It uses generic defaults for them and prints a warning, which you can ignore.

Keep pay-as-you-go and Go side by side with a profile. Define both providers in `~/.codex/config.toml`, then add a
profile file that switches to Go.

```
model = "kimi-k3"
model_provider = "opencode-go"
```
`codex --profile go`
Add the [Console MCP](https://opencode.ai/docs/console/harnesses#console-mcp) server and sign in from the browser.

`codex mcp add opencode-console --url https://opencode.ai/console/mcp`
If the sign-in doesn’t start automatically, run it yourself.

`codex mcp login opencode-console`
