---
title: "Claude Code - Alibaba Cloud"
date: "2026-11-05"
url: "https://www.alibabacloud.com/help/en/model-studio/claude-code"
site: "alibabacloud.com"
type: "article"
via: "direct"
---
Use Alibaba Cloud Model Studio models in Claude Code.

## Quick Start

Choose your client and complete the configuration.

#### CLI

1. 1 Configure the model #### Token Plan Replace `YOUR_API_KEY` with your Token Plan API Key:
  - Token Plan Personal Edition: [Create or view API Key](https://modelstudio.console.alibabacloud.com/subscription/token-plan/personal)
  - Token Plan Team Edition: [Assign a seat and get the API Key](https://modelstudio.console.alibabacloud.com/subscription/uac-admin/organization/members/list)
```
export ANTHROPIC_AUTH_TOKEN="YOUR_API_KEY"
export ANTHROPIC_BASE_URL="https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic"
export ANTHROPIC_MODEL="auto"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3.6-flash"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3.8-flash"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3.8-max"
export CLAUDE_CODE_SUBAGENT_MODEL="auto"
export CLAUDE_CODE_MAX_CONTEXT_TOKENS="983616"
```
#### Pay-as-you-go Replace `YOUR_API_KEY` with your [Alibaba Cloud Model Studio API Key](https://www.alibabacloud.com/help/en/model-studio/get-api-key), and replace `{WorkspaceId}` with your actual [Workspace ID](https://www.alibabacloud.com/help/en/model-studio/regions#h2_migrate_domain). The following example uses Singapore.
```
export ANTHROPIC_AUTH_TOKEN="YOUR_API_KEY"
export ANTHROPIC_BASE_URL="https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic"
export ANTHROPIC_MODEL="qwen3.7-max"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3.6-flash"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3.7-max"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3.7-max"
export CLAUDE_CODE_SUBAGENT_MODEL="qwen3.7-max"
```
#### Coding Plan Replace `YOUR_API_KEY` with your [Coding Plan API Key](https://modelstudio.console.alibabacloud.com/ap-southeast-1/subscription/coding-plan).
```
export ANTHROPIC_AUTH_TOKEN="YOUR_API_KEY"
export ANTHROPIC_BASE_URL="https://coding-intl.dashscope.aliyuncs.com/apps/anthropic"
export ANTHROPIC_MODEL="qwen3.7-plus"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3.7-plus"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3.7-plus"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3.7-plus"
export CLAUDE_CODE_SUBAGENT_MODEL="qwen3.7-plus"
```
**Note**These environment variables apply only to the current terminal. For persistent configuration, use [Configure with a configuration file](https://www.alibabacloud.com#connect_bailian_h).
2. 2 Verify Run the following command to verify: ```
claude -p "Hello"
```

#### CC Switch

1. 1 Install CC Switch Download and install [CC Switch](https://github.com/farion1231/cc-switch).
2. 2 Add a Bailian provider In CC Switch, select the Claude Code icon, click **+**, and fill in the fields in the corresponding tab.
#### Token Plan
  - Provider name: Bailian-Token Plan
  - Token Plan Personal Edition API Key: [Create or view](https://modelstudio.console.alibabacloud.com/subscription/token-plan/personal)
  - Token Plan Team Edition API Key: [Assign a seat and get](https://modelstudio.console.alibabacloud.com/subscription/uac-admin/organization/members/list)
  - Endpoint: `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic`
#### Pay-as-you-go
  - Provider name: Bailian-Pay-as-you-go
  - API Key: [Model Studio API Key](https://www.alibabacloud.com/help/en/model-studio/get-api-key)
  - Endpoint: `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic`
#### Coding Plan
  - Provider name: Bailian-Coding Plan
  - API Key: [get from console](https://modelstudio.console.alibabacloud.com/ap-southeast-1/subscription/coding-plan)
  - Endpoint: `https://coding-intl.dashscope.aliyuncs.com/apps/anthropic`
3. 3 Configure model mapping Expand **Advanced Options** and set the main, Haiku, Sonnet, and Opus models. Example:
  - Main model: `qwen3.8-max`
  - Haiku default model: `qwen3.8-flash`
  - Sonnet default model: `qwen3.8-flash`
  - Opus default model: `qwen3.8-max`
4. 4 Switch to the Claude Desktop panel In CC Switch, switch to the **Claude Desktop** panel on the left. If it is not shown, enable it in **Settings > General > App visibility**.
5. 5 Import the provider Import the provider already configured in Claude Code, or click **+** to add one. Turn on **Needs model mapping** for Bailian model IDs and map Sonnet, Opus, and Haiku to the actual models.
6. 6 Enable local routing Go to **Settings > Routing > Local Routing** and turn on the main-page switch; in the Claude Desktop panel, turn on local routing. The default address is `127.0.0.1:15721`.
7. 7 Enable and restart the desktop app Click **Enable** on the provider card and do not enter an API Key manually in the desktop app. Keep CC Switch running, then **fully quit and restart** the desktop app.

#### IDE plugin

1. 1 Install the plugin Install the Claude Code plugin from your IDE's extension marketplace.
2. 2 Configure the model Add the configuration to `settings.json` as described in [Configure with a Configuration File](https://www.alibabacloud.com#connect_bailian_h), or complete the CLI configuration first.
3. 3 Open Claude Code Restart your IDE, click the Claude Code icon, type `/` in the dialog, select General config, and set the model in Selected Model.

#### Desktop

Claude Code Desktop connects to Model Studio through the CC Switch local gateway.

1. 1 Install Claude Code Desktop Download and install from the [Claude download page](https://claude.ai/download).
2. 2 Configure CC Switch Follow the **CC Switch** tab to configure the provider and routing.
3. 3 Restart the desktop app Keep CC Switch running, then fully quit and restart Claude Code Desktop.

## Configure with a Configuration File

In addition to the options above, you can also connect using a configuration file.

1. 1 Open or create the configuration file 
  - macOS / Linux: `~/.claude/settings.json`
  - Windows: `C:\Users\<username>\.claude\settings.json`
2. 2 Add the configuration #### Token Plan Replace `YOUR_API_KEY` with your Token Plan API Key:
  - Token Plan Personal Edition: [Create or view API Key](https://modelstudio.console.alibabacloud.com/subscription/token-plan/personal)
  - Token Plan Team Edition: [Assign a seat and get the API Key](https://modelstudio.console.alibabacloud.com/subscription/uac-admin/organization/members/list)
```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "auto",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "qwen3.6-flash",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen3.8-flash",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen3.8-max",
        "CLAUDE_CODE_SUBAGENT_MODEL": "auto",
        "CLAUDE_CODE_MAX_CONTEXT_TOKENS": "983616"
    }
}
```
#### Pay-as-you-go Replace `YOUR_API_KEY` with your [Alibaba Cloud Model Studio API Key](https://www.alibabacloud.com/help/en/model-studio/get-api-key), and replace `{WorkspaceId}` with your actual [Workspace ID](https://www.alibabacloud.com/help/en/model-studio/regions#h2_migrate_domain). The following example uses Singapore.
```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.7-max",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "qwen3.6-flash",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen3.7-max",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen3.7-max",
        "CLAUDE_CODE_SUBAGENT_MODEL": "qwen3.7-max"
    }
}
```
#### Coding Plan Replace `YOUR_API_KEY` with your [Coding Plan API Key](https://modelstudio.console.alibabacloud.com/ap-southeast-1/subscription/coding-plan).
```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://coding-intl.dashscope.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.7-plus",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "qwen3.7-plus",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen3.7-plus",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen3.7-plus",
        "CLAUDE_CODE_SUBAGENT_MODEL": "qwen3.7-plus"
    }
}
```
3. 3 Verify After saving, run the following command to verify: ```
claude -p "Hello"
```

## Configure Context Window Size

Claude Code defaults to a 200K context window. If the model supports 1M, extend it to 1M (1,000,000 tokens).

**Method 1: Set via environment variable**

Add `CLAUDE_CODE_MAX_CONTEXT_TOKENS` to the `env` field in `~/.claude/settings.json`:

```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.7-plus",
        "CLAUDE_CODE_MAX_CONTEXT_TOKENS": "1000000"
    }
}
```
**Method 2: Use a model name suffix**

Append `[1m]` to the model name. This works with Model Studio models that support a 1M context window:

```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.7-plus[1m]",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen3.7-plus[1m]",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen3.7-plus[1m]",
        "CLAUDE_CODE_SUBAGENT_MODEL": "qwen3.7-plus[1m]"
    }
}
```
After modifying the configuration, open a new terminal window to restart Claude Code for the changes to take effect.

## Permission modes

Claude Code provides six permission modes:

- `default`: Prompts for confirmation before every operation.
- `acceptEdits`: Approves file edits automatically. Other operations still prompt for confirmation.
- `plan`: Read-only planning mode. No changes are executed.
- `dontAsk`: Does not prompt. An operation that would require a prompt is rejected directly.
- `bypassPermissions`: Bypasses all permission checks.
- `delegate`: Delegated mode.

**Method 1: Command-line flag**

Use `--permission-mode` to set the default permission mode for a session:

```
claude --permission-mode plan
claude --permission-mode acceptEdits
```
**Method 2: Interactive command**

Enter `/permissions` in a session to manage pre-approve and pre-deny rules for the bash, edit, and MCP tools.

**Method 3: settings.json configuration**

Configure the `permissions` field in `~/.claude/settings.json`:

```
{
    "permissions": {
        "allow": ["Bash(git:*)", "Read", "Edit"],
        "deny": ["Bash(rm:*)"],
        "defaultMode": "default"
    }
}
```
## Integrate Bailian CLI

1. 1 Install [Bailian CLI](https://github.com/modelstudioai/cli)
```
Please install the Alibaba Cloud Bailian CLI globally: npm install -g bailian-cli
```
2. 2 Configure the API Key Go to the [Bailian console](https://www.alibabacloud.com/help/en/model-studio/get-api-key) to get an API Key, then tell Claude Code:
```
My API Key is: sk-xxxxxxxxxxxxx
```
3. 3 Get started Describe your task in natural language, for example: ```
Generate 6 Amazon e-commerce hero images for a white wireless Bluetooth headset.
Generate a 30-second product demo video for a white wireless Bluetooth headset.
```

## Error Codes

If you encounter errors during configuration, refer to the FAQ documentation for your billing plan:

- Token Plan: [Personal Edition FAQ](https://www.alibabacloud.com/help/en/model-studio/token-plan-personal-faq#tpp03-h-faq-errors) · [Team Edition FAQ](https://www.alibabacloud.com/help/en/model-studio/token-plan-team-faq#tpfaq-h-error-table)
- Pay-as-you-go: [Error codes](https://www.alibabacloud.com/help/en/model-studio/error-code)
- Coding Plan: [Coding Plan FAQ](https://www.alibabacloud.com/help/en/model-studio/coding-plan-faq#e07ad90b4f3l0)

## FAQ

How do I use a savings plan with pay-as-you-go?

The pay-as-you-go setup remains the same: use your general Model Studio API key and Base URL. After you purchase a savings plan, it takes effect automatically and eligible usage is deducted automatically. See [Savings plans](https://www.alibabacloud.com/help/en/model-studio/savings-plan-and-resource-package#universal-usage-title).

Requests return 401 invalid\_api\_key

The API key type does not match `ANTHROPIC_BASE_URL`. Model Studio provides three access methods, and each access method uses a different base URL and a dedicated API key.

| **Access method** | **Base URL** | **API key** | 
|---|---|---|
| Token Plan | [https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic](https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic) | Token Plan API key | 
| Pay-as-you-go | [https://dashscope-intl.aliyuncs.com/apps/anthropic](https://dashscope-intl.aliyuncs.com/apps/anthropic) | Model Studio API key (starts with `sk-`) | 
| Coding Plan | [https://coding-intl.dashscope.aliyuncs.com/apps/anthropic](https://coding-intl.dashscope.aliyuncs.com/apps/anthropic) | Coding Plan dedicated API key | 

Troubleshooting steps:

1. **Check the request URL.** Check `ANTHROPIC_BASE_URL` in `~/.claude/settings.json`.
2. **Confirm the API key type.** Using the table above, confirm that your API key type matches the base URL.
3. **Correct the configuration.** When you use a Model Studio Pay-as-you-go API key, set `ANTHROPIC_BASE_URL` to `https://dashscope-intl.aliyuncs.com/apps/anthropic`.

After starting Claude Code, the interface displays "Unable to connect to Anthropic services. Failed to connect to api.anthropic.com: ERR\_BAD\_REQUEST"

Claude Code is connecting to the official Anthropic service instead of Alibaba Cloud Model Studio. This usually means the environment variables are missing or have not taken effect. Follow these steps:

1. **Check the configuration.** Run the `/status` command after starting Claude Code. Verify that `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` point to the Model Studio address. If the output is empty or shows a non-Model Studio address, check the `settings.json` configuration.
2. **Verify hasCompletedOnboarding.** Confirm that `hasCompletedOnboarding` is set to `true` in `~/.claude.json`. Without this, Claude Code attempts to connect to the official Anthropic service for login verification on startup.
3. **Open a new terminal.** After editing the configuration file, open a new terminal window and run `claude` for the changes to take effect.
4. **Update Claude Code.** If the issue persists after all the steps above, the Claude Code version may be outdated. Run `npm install -g @anthropic-ai/claude-code@latest` to update to the latest version, then try again.

Model switching does not take effect when using the legacy interface

The legacy compatible interface `https://dashscope-intl.aliyuncs.com/api/v2/apps/claude-code-proxy` only supports deprecated models. Specifying other models has no effect. To use available models, migrate to the new interface by following the configuration in this document.

CC Switch reports "No available model list endpoint found. Check the Base URL or confirm that the provider has opened the port" when adding a provider

This message comes from the connectivity check CC Switch runs when saving a provider: it probes a model list endpoint (such as `/v1/models`) against the configured request URL. Model Studio's Anthropic-compatible endpoint (ending in `/apps/anthropic`) only provides the messages endpoint `/v1/messages` and does not provide a model list endpoint, so the probe returns 404 and CC Switch reports "No available model list endpoint found".

**This message does not affect normal use of Claude Code and can be ignored.** Claude Code sends conversations through `/v1/messages`, and the models it uses are specified directly by the model mapping in CC Switch's **Advanced options**, without relying on auto-discovery from a model list endpoint. When the request URL and API Key are configured correctly, simply click **Enable** and start a new Claude Code session to chat normally.

If you still cannot chat, verify that the request URL ends in `/apps/anthropic` without an extra `/v1`, and that you have filled in the models supported by your plan in the [model mapping under Advanced options](https://www.alibabacloud.com/help/en/model-studio/claude-code).

Model mapping in CC Switch returns AccessDenied

If model calls fail in Claude Code with an `AccessDenied` error (HTTP 403, code: `access_denied`) after you configure the model mapping, check whether the model is marked as **Upcoming deprecation** in Model Studio console > **Model Gallery**. Models marked for upcoming deprecation still appear in the list, but API calls return 403 `AccessDenied`. Follow these steps:

1. **Check whether the model is marked for deprecation.** In Model Studio console > **Model Gallery**, search for the model you are using and check its status label.
2. **Switch to the latest available model.** Replace the legacy model (such as `qwen-coder-turbo-0919`) in the model mapping with the latest available model (such as `qwen3.8-max`).
3. **Reconfigure the model mapping and test.** Update the model mapping under **Advanced options** in CC Switch, click **Enable**, and start a new Claude Code session to verify.

**Note**Pay attention to the model lifecycle. Models marked for upcoming deprecation in Model Studio console > **Model Gallery** may become unavailable at any time. You can check a model's availability status there.
