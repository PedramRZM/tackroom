---
title: "Harnesses"
date: "2026-01-01"
url: "https://opencode.ai/docs/console/harnesses/"
site: "opencode.ai"
type: "doc"
via: "direct"
---
# Harnesses

Console works with coding agents other than OpenCode. Point a harness at the Console gateway with an API key to use any paid or Go model, and usage is billed to your workspace like any other request.

| Harness | Pay-as-you-go | Go | MCP | 
|---|---|---|---|
| [Claude Code](https://opencode.ai/docs/console/harnesses/claude-code) | Yes | Yes | Yes | 
| [Codex](https://opencode.ai/docs/console/harnesses/codex) | Yes | Yes | Yes | 
| [Hermes](https://opencode.ai/docs/console/harnesses/hermes) | Built in | Built in | Yes | 
| [Pi](https://opencode.ai/docs/console/harnesses/pi) | Built in | Built in | Yes | 
| [Raycast](https://opencode.ai/docs/console/harnesses/raycast) | Extension | Extension | Yes | 

Free-tier chat models are only available from within OpenCode. Other harnesses receive HTTP `403` for those models,
even with a Console API key. Use paid models or a Go subscription.

Harnesses authenticate with a Console API key. The quickest option is a
[personal API key](https://opencode.ai/docs/console/api#personal-api-keys), which calls models as you.

1. Open **Account** from the account menu in the [Console](https://opencode.ai/console).
2. Under **Personal API keys**, click **Add API key**.
3. Choose the workspace, name the key, and click **Create**.
4. Copy the key. It is shown only once.

`oc_sk_1a2b3c4d5e6f_...`
Usage counts toward your [member budget](https://opencode.ai/docs/console/budgets#member-budgets). Use a key from a workspace with credits for
pay-as-you-go, or from a workspace subscribed to [Go](https://opencode.ai/docs/console/go) for Go.

For shared machines or CI, owners and admins can create a [service account](https://opencode.ai/docs/console/api#service-accounts) key instead,
so usage isn’t tied to one person.

Pay-as-you-go and Go are served from different base URLs. Use the one that matches your plan.

| Plan | Base URL | 
|---|---|
| Pay-as-you-go | `https://opencode.ai/inference` | 
| Go | `https://opencode.ai/inference/go` | 

Append the path for the API your harness speaks. Every API serves every paid and Go text model: Console sends a request to the model’s own endpoint when it speaks that API, and translates it otherwise.

| API | Path | 
|---|---|
| OpenAI Responses | `/openai/v1/responses` | 
| OpenAI Chat Completions | `/openai/v1/chat/completions` | 
| Anthropic Messages | `/anthropic/v1/messages` | 
| Gemini | `/google/v1beta/models/<model>:generateContent` | 

`https://opencode.ai/inference/go/openai/v1/chat/completions`
Send a stable session ID with every request so Console can route a conversation consistently and reuse its prompt
cache. Go [requires it](https://opencode.ai/docs/console/go#where-can-i-use-it).

`x-opencode-session: ses_...`
Console also recognizes the native session headers sent by Claude Code, Codex, Hermes, and Pi, so they need no extra configuration.

Harnesses with MCP support can manage your workspace through the Console MCP server. It uses OAuth with dynamic client registration, so you sign in from the browser instead of pasting a key.

`https://opencode.ai/console/mcp`
Each harness page shows how to add it. OpenCode adds the server automatically as `opencode_console` when your workspace
enables it, and asks you to sign in from the browser the first time it uses it.
