---
title: "Kimi Code Overview"
date: "2024-11-01"
url: "https://www.kimi.com/code/docs/en/"
site: "kimi.com"
type: "doc"
via: "direct"
---
# Kimi Code Overview [](https://www.kimi.com#kimi-code-overview)

## What is Kimi Code [](https://www.kimi.com#what-is-kimi-code)

Kimi Code is an intelligent programming service for developers included in [Kimi membership benefits](https://www.kimi.com/membership/pricing?from=kfc_docs_overview). Built on Kimi's latest flagship models, it provides AI-assisted capabilities—such as code reading, file editing, and command execution—through product forms like the Desktop app, CLI, and VS Code extension. Subscribers can also obtain an API Key to integrate Kimi Code's model capabilities into third-party development tools and platforms.

## Core Advantages [](https://www.kimi.com#core-advantages)

**1. Models and inference**

**2. Ecosystem and extensibility**

## Getting Started [](https://www.kimi.com#getting-started)

Kimi Code allows members to use their benefits in both the official client and third-party platforms, covering different development scenarios.

### Using the Official Client [](https://www.kimi.com#using-the-official-client)

Choose the client that fits you and install with one click:

For developers who prefer a graphical app. Open a local project folder in Kimi Code Desktop and let the Agent read code, edit files, run commands, and verify results through conversation. Available on macOS, Windows, and Linux.

After installing, open the app and sign in with your Kimi account as prompted—no API Key management needed. See [Desktop Quick Start](https://www.kimi.com/code/docs/en/kimi-code-desktop/getting-started.html) for more.

### API Access [](https://www.kimi.com#api-access)

When integrating Kimi Code into third-party development tools, you need to manually configure an API Key to complete authentication.

#### Service Endpoint [](https://www.kimi.com#service-endpoint)

The Kimi Code API is compatible with both OpenAI and Anthropic protocols. Different tools have different requirements for address configuration:

- **Base URL**: Some tools (e.g., Claude Code) only require the Base URL, and the tool will automatically append the subsequent path.
- **Full Endpoint**: Some tools (e.g., Trae) require the complete API request address.

Choose the corresponding address as needed:

| Protocol | Base URL | Common Endpoint Examples | 
|---|---|---|
| OpenAI Compatible (Chat Completions and Responses protocols) | China: `https://api.kimi.com/coding/v1` Overseas: `https://api.kimi.ai/coding/v1` | `https://api.kimi.com/coding/v1/chat/completions` `https://api.kimi.com/coding/v1/responses` | 
| Anthropic Compatible | China: `https://api.kimi.com/coding/` Overseas: `https://api.kimi.ai/coding/` | `https://api.kimi.com/coding/v1/messages` | 

#### Model IDs [](https://www.kimi.com#model-ids)

Different model IDs correspond to different membership tiers and context windows. See [Membership Benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) for details.

Both protocols accept the following 6 model IDs:

| Model ID | Description | 
|---|---|
| `k3.1-pro` | K3.1 Pro — available to Moderato / Plus members and above; Allegretto / Pro members and above unlock up to 1M context. Thinking is required, with `max` as the default; requests with thinking disabled are rejected. | 
| `k3.1-pro-highspeed` | K3.1 Pro Highspeed — available to Allegretto / Pro members and above; delivers approximately 2–3× the output speed of K3.1 Pro at about 2× the quota usage, with up to 1M context. | 
| `k3` | K3 — available to Moderato / Plus members and above; Allegretto / Pro members and above unlock the up-to-1M context window; supports `low` / `high` / `max` thinking effort levels. Best for large codebase analysis, multi-file refactoring, and long-document processing. | 
| `k3-256k` | K3 256K context version — available to Moderato / Plus members and above; supports `low` / `high` / `max` thinking effort levels. Within 256k context, it delivers the same results as K3. `k3` (1M) consumes about twice as much quota as `k3-256k`. Ideal for everyday Q&A, code completion, routine feature development, and single-file or small-file edits — video input is not supported. | 
| `kimi-for-coding` | K2.8 Preview — available to Andante / Plus members and above; supports up to 1M context and `low` / `high` / `max` reasoning effort. | 
| `kimi-for-coding-highspeed` | K2.7 Code HighSpeed — available to Allegretto / Pro members and above. | 

See [Model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html) for model capabilities and setup details.

#### Obtaining an API Key [](https://www.kimi.com#obtaining-an-api-key)

Kimi members can create and manage API Keys in the [Kimi Code Console](https://www.kimi.com/code/console) (up to 5 keys; each is shown only once upon creation—please keep it safe).

#### Configuring in Third-Party Tools [](https://www.kimi.com#configuring-in-third-party-tools)

After obtaining an API Key, configure the corresponding Base URL and API Key in the environment variables of the respective tool to start using it. For detailed setup steps, see the corresponding tool guide:

[Claude CodeAnthropic's command-line coding assistant](https://www.kimi.com/code/docs/en/third-party-tools/claude-code)

[OpenCodeA terminal-based coding agent](https://www.kimi.com/code/docs/en/third-party-tools/opencode)

[CodexOpenAI's coding agent](https://www.kimi.com/code/docs/en/third-party-tools/codex)

**Note**: Please maintain the tool's real identity identifier when using. Tampering with the client identifier (User-Agent) is considered a violation and may result in suspension of membership benefits.


## Platform Comparison [](https://www.kimi.com#platform-comparison)

Kimi Code membership benefits are designed specifically for programming scenarios. If you need to call large model capabilities in your own product, or require team collaboration and usage management, please visit the [Kimi Platform](https://platform.kimi.ai).

| Comparison Item | Kimi Code Platform | Kimi Platform | 
|---|---|---|
| Base URL | OpenAI Compatible: China `https://api.kimi.com/coding/v1` Overseas `https://api.kimi.ai/coding/v1` Anthropic Compatible: China `https://api.kimi.com/coding/` Overseas `https://api.kimi.ai/coding/` | China `https://api.moonshot.cn/v1` Overseas `https://api.moonshot.ai/v1` | 
| Billing | Membership subscription, monthly/annual payment, with rate limiting | Pay-as-you-go, top up and use | 
| Best For | Terminal/IDE Agent programming, multi-file engineering tasks | Product integration, enterprise-level calls, multimodal application development | 

## Next Steps [](https://www.kimi.com#next-steps)

- [Kimi Code CLI Quick Start](https://www.kimi.com/code/docs/kimi-code-cli/guides/getting-started.html) – Install, log in, and start your first conversation
- [Kimi Code for VS Code Quick Start](https://www.kimi.com/code/docs/kimi-code-for-vscode/getting-started.html) – Install the extension, log in, and typical workflows
- [Using in More Third-Party Tools](https://www.kimi.com/code/docs/third-party-tools/claude-code.html) – Claude Code, OpenCode, Codex, and more
- [Membership Benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) – Quota refresh and rate limits, quota sharing, Extra Usage, and more
- [FAQ](https://www.kimi.com/code/docs/kimi-code/faq.html) – Common issues with installation, login, and usage
