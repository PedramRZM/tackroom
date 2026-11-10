---
title: "MCP server – Linear Docs"
author: "Enterprise-managed authorization"
date: "2021-10-07"
url: "https://linear.app/docs/mcp"
site: "Linear"
type: "doc"
via: "direct"
---
# MCP server

The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model or agent to access your Linear data in a simple and secure way.

Connect to our MCP server natively in Claude, Cursor, and other clients or use the   [`mcp-remote`](https://github.com/geelen/mcp-remote) module for backwards compatibility with clients that do not support remote MCP.

Linear’s MCP server follows the authenticated remote [MCP spec](https://modelcontextprotocol.io/specification/2025-03-26), so the server is centrally hosted and managed. The Linear MCP server has tools available for finding, creating, and updating objects in Linear like issues, projects, and comments — with more functionality on the way, and [feedback](https://linear.app/contact/support) on its functionality is welcomed.

For help getting started after setup, see some of our [example prompts](https://linear.app/docs/mcp#common-use-cases).

## Setup[](https://linear.app#setup)

### General[](https://linear.app#general)

Our MCP server uses Streamable HTTP as the primary transport, accessible at the following address. The interactive setup flow uses OAuth 2.1 with dynamic client registration. You can also authenticate directly with a bearer token or Linear API key — see the FAQ for details.

Read-write access is provided through `https://mcp.linear.app/mcp` by default.

For read-only access, you have two options:

- Connect to `https://mcp.linear.app/mcp/readonly`, which only ever exposes read tools.
- Use the standard `/mcp` endpoint, but only request the `read` OAuth scope.  Clients that request `read` are granted read-only access, and the underlying token can’t reach write APIs.

For instructions for specific clients, read on. Dedicated setup pages are also available for [Claude](https://linear.app/integrations/claude), [Cursor](https://linear.app/integrations/cursor-mcp), [VS Code](https://linear.app/integrations/vs-code-mcp), [Windsurf](https://linear.app/integrations/windsurf), and [Zed](https://linear.app/integrations/zed/).

### Claude[](https://linear.app#claude)

**Team, Enterprise (Claude.ai)**

Navigate to the [connectors](https://claude.ai/customize/connectors) page and connect Linear.

**Free, Pro (Claude desktop)**

From Claude settings > Connectors you can add the Linear connector.

If you use Okta, first configure SAML for Linear using [Okta’s OIN](https://linear.app/docs/saml-and-access-control#configure). Then enable **MCP enterprise managed authentication** from the bottom of your Okta identity provider settings in Linear.

Once this is toggled on, copy the [**Issuer URI**](https://developer.okta.com/docs/guides/sign-into-spa-redirect/-/main/#find-your-config-values) for the authorization server from Okta’s side and paste this into your Linear settings:

`e.g. https://your-org.okta.com`
This allows supported external MCP clients such as Claude to authenticate users automatically using your Okta-managed access policies.

### Claude auto-connect (beta)[](<https://linear.app#claude-auto-connect-(beta)>)

Claude auto-connect lets members with matching Linear accounts on Business or Enterprise plans connect automatically, without a separate sign-in or consent screen. Members retain their existing Linear permissions. Setup requires a Claude Team or Enterprise plan and admin access in both Claude and Linear.

- In Claude, go to **Organization settings → Connectors → Linear** and select **Set up** next to **Managed authorization**.
- Under **Identity source**, select **Claude-issued** and copy the issuer URL shown in Claude.
- In Linear, go to **Workspace settings → Security**, enable **Claude-issued authentication for MCP**, and enter the URL in **Claude issuer URL**.
- Copy the **Tenant ID** from Linear and paste it into **Tenant ID** in Claude.
- Select **Run test**. Once all checks pass, select **Enable and continue** and choose who gets the connector.

Members’ Claude and Linear email addresses must match. Test with a few members before rolling this out. To turn it off, disable managed authorization in Claude and **Claude-issued authentication for MCP** in Linear.

### Claude Code[](https://linear.app#claude-code)

`claude mcp add --transport http linear-server https://mcp.linear.app/mcp`
Then run `/mcp` once you’ve opened a Claude Code session to go through the authentication flow.

### Codex[](https://linear.app#codex)

The setup steps for the MCP server are the same regardless of whether you use the IDE Extension or the CLI since the configuration is shared.

**Configuration via CLI:**

Run the following command in Terminal:

`codex mcp add linear --url https://mcp.linear.app/mcp`
This will automatically prompt you to log in with your Linear account and connect it to your Codex.

**Note**: If this is the first time you are using an MCP in Codex you will need to enable the `rmcp` feature for this to work. Add the following into your `~/.codex/config.toml`:

```
[features]
experimental_use_rmcp_client = true
```
**Configuration through environment variables:**

1. Open the `~/.codex/config.toml` file in your preferred editor
2. Add the following:

```
[features]
experimental_use_rmcp_client = true
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"
```
Run `codex mcp login linear` to move through the authentication flow.

### Cursor[](https://linear.app#cursor)

To add the MCP to Cursor, you can install by clicking [here](cursor://anysphere.cursor-deeplink/mcp/install?name=Linear&config=eyJ1cmwiOiJodHRwczovL21jcC5saW5lYXIuYXBwL21jcCJ9), or searching for Linear from Cursor’s [MCP tools page](https://cursor.com/docs/context/mcp/directory).

### fx[](https://linear.app#fx)

In fx, add Linear’s MCP server:

`/mcp add linear https://mcp.linear.app/mcp`
Then run:

`/mcp login linear`
Follow the prompts in your browser to authorize access to Linear.

For more configuration options, see the [fx MCP documentation](https://fx.sh/docs/capabilities/mcp).

### Visual Studio Code[](https://linear.app#visual-studio-code)

```
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```
1. `CTRL/CMD  P` and search for **MCP: Add Server**.
2. Select **Command (stdio)**
3. Enter the following configuration, and hit enter.

`npx mcp-remote https://mcp.linear.app/mcp`

1. Enter the name **Linear** and hit enter.
2. Activate the server using **MCP: List Servers** and selecting **Linear**, and selecting **Start Server**.

### v0 by Vercel[](https://linear.app#v0-by-vercel)

To add the MCP to v0, you can install from the [connections](https://v0.app/settings/mcp-connections) page.

### Windsurf[](https://linear.app#windsurf)

1. `CTRL/CMD  ,` to open Windsurf settings.
2. Under Scroll to Cascade -> MCP servers
3. Select **Add Server -> Add custom server**
4. Add the following:

```
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```
### Zed[](https://linear.app#zed)

1. `CMD  ,` to open Zed settings.
2. Add the following:

```
{
  "context_servers": {
    "linear": {
      "source": "custom",
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"],
      "env": {}
    }
  }
}
```
### Others[](https://linear.app#others)

Hundreds of other tools now support MCP servers, you can configure them to use Linear’s MCP server with the following settings:

- **Command**: `npx`
- **Arguments**: `-y mcp-remote https://mcp.linear.app/mcp`
- **Environment**: None

## Common use cases[](https://linear.app#common-use-cases)

The MCP server lets you work with your Linear data from any compatible AI client. To help get started with the Linear MCP tooling, feel free to copy some example prompts into your own client to explore what’s possible.

**Use case**

Use this workflow to turn a planning document into a structured Linear project, with issues, milestones, and relationships that make the work easier to organize and track.

**Example prompt**

You are helping turn a planning document into a well-structured Linear project.

Read the document, create a project that reflects its objective, scope, and timeline, then create the issues needed to represent the work with clear titles and populated descriptions. Each issue should make the work actionable by capturing the problem, the goal, the proposed approach when one is provided, and any open questions that remain. Organize issues into milestones when the document clearly implies phases, deliverables, or checkpoints, and add related relationships where issues are meaningfully connected, but do not invent dependencies or structure that the source material does not support.

If the document is too vague or ambiguous to produce high-quality work, flag the uncertainty and return a proposed outline for review instead of guessing.

Before creating anything, show the proposed project, milestones, issues, relationships, and any decisions that need review.

**Use case**

Use this workflow to turn standup notes into clear updates on the relevant Linear issues, so progress and blockers stay documented without extra manual work.

**Example prompt**

You are helping turn live standup notes into updates on existing Linear issues.

Read the notes, identify any issues mentioned by ID, title, owner, or clear surrounding context, and match each note only when the connection is strong.

For every confident match, add a concise comment that captures what changed, the current status or blocker, and the next step if one is mentioned. Keep each comment factual and specific to that issue. If a note is ambiguous or you cannot confidently match it, do not guess or create work from it; return it as unmatched with a short explanation.

Before applying any changes, show which issues you plan to update and the exact comment you would post to each one, then apply the comments and separately list any notes you skipped.

Standup notes: `[Paste the notes’ raw text here or attach the transcript as a document]`

**Use case**

Use this workflow to investigate a reported bug from an existing Linear issue, identify a likely root cause, and capture the findings back on the issue for the team.

**Example prompt**

You are helping investigate a bug that is already tracked in Linear.

Start from the referenced issue, use its description and any linked context as the starting point, and search for the most likely root cause by following relevant technical, product, or workflow clues.

Focus on producing a clear, evidence-based explanation of what is happening, what changed if that is relevant, and what the likely cause appears to be. Do not guess when the evidence is weak; instead, call out uncertainty and explain what additional context would help.

Once you have enough information, write a concise summary of the findings and post that summary as a comment on the issue so the investigation is documented for the team.

Linear issue to investigate: `[LIN-123]`

**Use case**

Use this workflow to summarize what a team completed during a specific cycle or timeframe, making it easier to review progress and communicate outcomes.

**Example prompt**

You are helping summarize work completed during a specific Linear cycle or timeframe.

Identify the most recently completed cycle to analyze for the selected team or teams, gather the relevant issues, and produce a concise summary of what was accomplished. Focus on the work that was actually completed, the main themes across that work, and any notable patterns such as bugs resolved, projects advanced, or areas of concentrated effort.

Keep the summary clear and useful for sharing with others, and avoid overstating progress where the underlying work is still in flight.

Team identifiers: `[LIN, FEA]`

**Use case**

Use this workflow to build a historical timeline of work in Linear around a topic, so teams can understand how a project, incident, or theme evolved over time.

**Example prompt**

You are helping document the history of work in Linear around a specific topic.

Gather the relevant issues and projects connected to that topic, review their historical activity, and produce a timeline that shows the key developments in chronological order.

Focus on meaningful milestones such as when work was created, when direction changed, when major decisions or updates were recorded, and when important work was completed.

Keep the timeline factual and grounded in the underlying activity, and call out any gaps or ambiguity rather than inferring events that are not clearly supported.

Topic: `[Insert a specific topic from your workspace]`

**Use case**

Use this workflow to turn an initial idea into a reviewed implementation plan, then create the corresponding Linear work and delegate execution to the right people or agents.

**Example prompt**

You are helping plan and structure a development effort in Linear.

Start by designing an approach based on the provided context, with enough detail to explain the proposed solution, major workstreams, and any important tradeoffs or open questions. Treat that initial plan as a draft that can be reviewed and edited before any work is created.

Once the plan is approved, create a parent issue that captures the overall goal and create sub-issues for the concrete pieces of work needed to execute it.

Keep the breakdown clear and actionable, and assign or delegate work only when the requested owners or agents are explicitly specified.

Context: `[Insert enough context to help orient the agent]`

## FAQ[](https://linear.app#faq)

Enter the following in the Terminal to clear saved auth info: `rm -rf ~/.mcp-auth` then try again to connect.

Additionally you may need to update to a newer version of node if required.

The Linear MCP server authenticates each session via OAuth. Because reconnecting alone does not switch the workspace within an existing auth session, each workspace needs its own separate authentication context.

If your client or the `mcp-remote` module supports a configuration directory (for example via `MCP_REMOTE_CONFIG_DIR`), point each workspace to a different path:

```
MCP_REMOTE_CONFIG_DIR=~/.mcp-auth/workspace-a npx mcp-remote https://mcp.linear.app/mcp
MCP_REMOTE_CONFIG_DIR=~/.mcp-auth/workspace-b npx mcp-remote https://mcp.linear.app/mcp
```
Authenticate each configuration separately. For clients that manage their own auth storage, check the client’s documentation for workspace-switching options.

The MCP server supports passing OAuth token and API keys directly in the `Authorization: Bearer <yourtoken>` header instead of using the interactive authentication flow.

You can use this to interact with the MCP server as an `app` user, provide read-only access through a restricted API key, or integrate with an existing Linear OAuth application without an extra authentication hop.

For an alternative read-only approach with your own API key, create a Linear API key with only the `Read` permission enabled.

The SSE endpoint at `https://mcp.linear.app/sse` is a deprecated fallback for clients that do not support Streamable HTTP.

For all new setups, use the primary Streamable HTTP endpoint at `https://mcp.linear.app/mcp`.

Remote MCP connections can occasionally need a reconnect in some client setups. Try disconnecting and reconnecting the server from your client’s MCP settings. This is a routine client-side reset and does not affect your Linear data or authentication session.

The default connection uses Streamable HTTP at `https://mcp.linear.app/mcp`. If that does not work in WSL, use this SSE fallback instead (`/sse` is a legacy path for clients that do not support Streamable HTTP):

`{"mcpServers": {"linear": {"command": "wsl","args": ["npx","-y","mcp-remote","`[https://mcp.linear.app/sse](https://mcp.linear.app/sse)","--transport sse-only"\]}}}
