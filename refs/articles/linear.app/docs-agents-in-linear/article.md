---
title: "Agent platform – Linear Docs"
date: "2021-10-07"
url: "https://linear.app/docs/agents-in-linear"
site: "Linear"
type: "doc"
via: "direct"
---
# Agent platform

## Overview[](https://linear.app#overview)

While [Linear Agent](https://linear.app/docs/linear-agent) works by default in every workspace, Linear also maintains an open platform for third party agents (including those you build yourself.)

Agents are designed to work seamlessly alongside human teammates, and can open PRs against issues, help write documents, and take most actions that human users can, depending on their granted scopes.

To interact with an agent in Linear:

- **Delegate issues** by assigning the issue to the agent. This triggers the agent to take action based on its programmed behavior.
- **@mention them** in comments or descriptions to trigger their functions.

If you’re not sure how to interact or what they’re able to help with, you can try @mentioning the agent to ask for help.

## Adding Agents[](https://linear.app#adding-agents)

Workspace admins can install agents by following the setup instructions provided by the agent developer. Find available agents in the [Integrations Directory](https://linear.app/integrations/agents).

During installation, you’ll be prompted to choose which teams the agent has access to.

Once installed, any user with access to the selected teams can interact with the agent. Admins can also review agent access from the [AI & Agents](https://linear.app/settings/ai) settings in the *Installed Agents* section.

Depending on the permissions granted during installation, agents can be mentioned, delegated issues through assignment, create and reply to comments, and collaborate on projects and documents. App users are installed and managed by workspace admins.

## Guiding Agents[](https://linear.app#guiding-agents)

Agent guidance lets you provide instructions that agents will automatically receive when they work on issues in your workspace.

Agent guidance provides instructions that help agents work within your team’s conventions. Guidance can specify which repository to use for certain code changes, how to reference issues in commits or pull requests, and what review process to follow, so agents align with your existing workflows.

**Note:** All guidance is passed to the agent, but how it is interpreted or applied depends on the specific agent integration. If an agent doesn’t appear to follow the guidance, please share feedback with the team responsible for that agent directly.

Workspace guidance applies across the entire organization, while team-specific guidance can be used to include additional instructions unique to that team. When both exist, team guidance takes priority.

Guidance is authored in a markdown editor with full history, so instructions can be formatted clearly and reviewed or updated over time.

To edit your workspace-level agent guidance, navigate to [*Settings* > *Agents* > *Additional guidance*](https://linear.app/settings/agents). For team-level guidance, navigate into your parent or sub-team’s settings > *Agents* > *Additional guidance*. Both workspace and team level guidance may not exist in all agent contexts.

## Viewing Agent Activity[](https://linear.app#viewing-agent-activity)

You can track what an agent has done in the same ways you track other teammates:

- **Agent** [**user pages**](https://linear.app/docs/custom-views#user-views) show issue activity and contributions.
- In the **My issues** view, issues that you’ve delegated to agents will still appear—so you maintain visibility and control over the work in progress.
- **Custom views** filtered by **Delegate** to monitor agent involvement on specific types of issues or workflows.
- Use **Insights** sliced or segmented by **Delegate** to measure how much work is being directed to and handled by agents.

## Building Your Own Agent[](https://linear.app#building-your-own-agent)

Developers can build custom agents using Linear’s developer platform. Documentation on agent APIs, authentication, and behavior can be found in our [Developer Docs](https://linear.app/developers/agents).

## FAQs[](https://linear.app#faqs)

Agents are not counted as billable seats in Linear. The services that provide the agent may have their own pricing structure, and you should refer to their documentation before installing.

Linear does not train on customer’s data. We use models from common model providers, a complete list is available in our [DPA](https://linear.app/dpa).

Agents themselves would be 3rd party integrations approved by your workspace, in which case we can’t speak to how the agent provider operates and you’d have to refer to the agent service provider.
