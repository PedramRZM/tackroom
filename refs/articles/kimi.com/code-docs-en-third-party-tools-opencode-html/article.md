---
title: "Using Kimi in OpenCode"
date: "2024-11-01"
url: "https://www.kimi.com/code/docs/en/third-party-tools/opencode.html"
site: "kimi.com"
type: "doc"
via: "direct"
---
# Using Kimi in OpenCode [](https://www.kimi.com#using-kimi-in-opencode)

[OpenCode](https://opencode.ai/) is a terminal-based coding agent. This guide shows how to forward OpenCode model requests to Kimi For Coding via built-in authentication, with K3.1 Pro models, K3, or K2.8 Preview providing the model inference.

## Install OpenCode [](https://www.kimi.com#install-opencode)

The easiest way to install OpenCode is through the installation script:

`curl -fsSL https://opencode.ai/install | bash`
Or install via npm:

`npm install -g opencode-ai`
## Configure API key [](https://www.kimi.com#configure-api-key)

Run `opencode auth login` and select **Kimi For Coding** from the provider list:

```
$ opencode auth login
┌  Add credentials
│
◆  Select provider
│  ● Kimi For Coding
│  ...
└
```
Enter your Kimi For Coding API Key:

```
$ opencode auth login
┌  Add credentials
│
◇  Select provider
│  Kimi For Coding
│
◇  Enter your API key
│  _
└
```
API Keys can be created and managed in the [Kimi Code Console](https://www.kimi.com/code/console) (up to 5 keys; each key is shown only once at creation).


## Launch and use [](https://www.kimi.com#launch-and-use)

After configuring, start OpenCode:

`$ opencode`
Type `/models` in a session:

`/models`
Pick a model under the **Kimi For Coding** list.

Introducing the K3.1 Pro series

**K3.1 Pro** is now fully rolled out in Kimi Code. It is our most capable 3T-class model to date, with a 1-million-token context window and substantial improvements in coding, 3D creation, financial research, and other long-horizon agent capabilities.

We also launched **K3.1 Pro Highspeed**. With the same model quality, it delivers approximately 2–3× the speed of K3.1 Pro for more responsive interactions.

**Note**: K3.1 Pro models only support thinking mode, and requests with thinking disabled are rejected. Start a new session and use the Kimi Coding Plan's native API protocols for the most stable results; protocol conversion through proxy tools may cause behavior to vary.

Before you start, check your membership tier and what it entitles you to (see [Membership Benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html#plan-comparison) for a comparison of the legacy and new plans) — calling models or context windows beyond your plan will fail with an error:

| Tier | Available models | Context window | 
|---|---|---|
| Go (new plans) | No coding quota | — | 
| Andante (legacy plans) | K2.8 Preview | `1048576` | 
| Plus / Moderato | K3.1 Pro K3 K3-256K K2.8 Preview | K3.1 Pro: `262144` K3: `262144` K3-256K: `262144` K2.8 Preview: `1048576` | 
| Pro and above / Allegretto and above | K3.1 Pro K3.1 Pro Highspeed K3 K3-256K K2.8 Preview K2.7 Code HighSpeed | K3.1 Pro: `1048576` K3.1 Pro Highspeed: `1048576` K3: `1048576` K3-256K: `262144` K2.8 Preview: `1048576` K2.7 Code HighSpeed: `262144` | 

With K3.1 Pro, the K3 series, or K2.8 Preview selected, type `/variants` to switch the thinking effort:

`/variants`
Thinking effort mapping

OpenCode offers the variants `Default` / `low` / `high` / `max`, mapped to the K3 series' actual effort levels as follows (full mapping table in [Model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html#switch-model)):

| OpenCode variant | K3 series actual effort | 
|---|---|
| `Default` | `high` (K3.1 Pro default) / `high` (K3 series default) / `max` (K2.8 Preview default) | 
| `low` | `low` | 
| `high` | `high` (recommended) | 
| `max` | `max` | 

K3.1 Pro models, the K3 series, and K2.8 Preview support `low` / `high` / `max`. Disabling thinking for K3.1 Pro returns 400; with thinking disabled, requests to the K3 series, K2.8 Preview, and K2.7 Code HighSpeed are served by K2.8 Preview without thinking. K2.7 Code HighSpeed does not require this setting.

See [Model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html) for model capabilities and setup details.

## Next steps [](https://www.kimi.com#next-steps)

- [Model configuration](https://www.kimi.com/code/docs/en/kimi-code/models.html) — Compare the models and see the full effort mapping table
- [Membership Benefits](https://www.kimi.com/code/docs/en/kimi-code/membership.html) — Confirm which models are available for your plan
