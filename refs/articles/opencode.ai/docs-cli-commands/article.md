---
title: "Commands"
date: "2026-01-01"
url: "https://opencode.ai/docs/cli/commands/"
site: "opencode.ai"
type: "doc"
via: "direct"
---
# Commands

Every command accepts `--help` for its full flag list, for example `opencode run --help`. Some server-backed commands accept `--standalone` to run a private server or `--server <url>` to target a specific one; check the command’s help for its supported flags.

Sends a message and prints the reply without opening the interactive interface.

`$ opencode run "Explain this repository"`
In CI, pass a provider API key as a secret and use standalone mode so the private server receives it. For example, this GitHub Actions job reviews the checked-out repository:

```
name: OpenCode review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install --global @opencode/cli
      - run: opencode run --standalone --model anthropic/claude-sonnet-5-5 "Review this repository for correctness and summarize any issues."
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```
Choose a model.

`$ opencode run --model anthropic/claude-sonnet-5-5 "Refactor parseToken"`
Continue the last session.

`$ opencode run --continue "Now handle the expired case"`
Emit newline-delimited JSON for scripts.

`$ opencode run --format json "List the TODO comments"`
Attach files to the message.

`$ opencode run --file src/server.ts --file src/client.ts "Review these for bugs"`
Run with a specific agent.

`$ opencode run --agent build "Fix the failing test"`
Continue a specific session.

`$ opencode run --session ses_4f2a1c "Check edge cases"`
Auto-approve permissions that are not explicitly denied.

`$ opencode run --auto "Fix the failing test"`
Create the session archived so scripted or CI runs stay out of session lists and the inbox. The session still exists: `opencode session list` includes it, and you can open it by ID.

`$ opencode run --archived "Review this diff"`
View all subcommands and flags.

`$ opencode run --help`
Starts the minimal interactive interface instead of the full-screen TUI.

`$ opencode mini`
Continue the last session.

`$ opencode mini --continue`
Start with a model and an initial prompt.

`$ opencode mini --model anthropic/claude-sonnet-5-5 --prompt "Summarize this repository"`
Continue a specific session.

`$ opencode mini --session ses_4f2a1c`
View all subcommands and flags.

`$ opencode mini --help`
Manages sessions.

`$ opencode session list`
Limit the list and print JSON.

`$ opencode session list --max-count 20 --format json`
Delete a session and its child sessions.

`$ opencode session delete ses_9c1b08`
Export session data as JSON.

`$ opencode session export ses_4f2a1c`
Redact sensitive transcript and file data when exporting.

`$ opencode session export ses_4f2a1c --sanitize`
Import session data from a JSON file or URL.

`$ opencode session import session.json`
Import into a specific directory.

`$ opencode session import session.json --directory ~/code/project`
View all subcommands and flags.

`$ opencode session --help`
Manages AI providers and credentials.

`$ opencode auth list`
List them as JSON.

`$ opencode auth list --format json`
Log in to a provider.

`$ opencode auth login anthropic`
Log in with a specific authentication method.

`$ opencode auth login anthropic --method key`
Log out of a saved account.

`$ opencode auth logout anthropic work`
Switch the active account for an integration.

`$ opencode auth switch anthropic work`
Export saved credentials and import them on another machine. The file contains secrets.

```
$ opencode auth export anthropic > credentials.json
$ opencode auth import credentials.json
```
View all subcommands and flags.

`$ opencode auth --help`
Lists every available model.

`$ opencode models`
View all subcommands and flags.

`$ opencode models --help`
Manages MCP (Model Context Protocol) servers.

`$ opencode mcp list`
Add a remote server.

`$ opencode mcp add context7 --url https://mcp.context7.com/mcp`
Add a local server to the global config.

`$ opencode mcp add everything --global -- npx -y @modelcontextprotocol/server-everything`
Add a local server with an environment variable.

`$ opencode mcp add everything --env LOG_LEVEL=debug -- npx -y @modelcontextprotocol/server-everything`
Add a remote server with a header.

`$ opencode mcp add context7 --url https://mcp.context7.com/mcp --header CONTEXT7_API_KEY=secret`
Authenticate with an OAuth-capable remote server.

`$ opencode mcp auth sentry`
Remove stored OAuth credentials for a server.

`$ opencode mcp logout sentry`
View all subcommands and flags.

`$ opencode mcp --help`
Manages plugins.

`$ opencode plugin list`
Include built-in server plugins.

`$ opencode plugin list --builtin`
Install a plugin and add it to the global configuration.

`$ opencode plugin add @example/opencode-tui`
Check package plugins for updates.

`$ opencode plugin check`
Update package plugins.

`$ opencode plugin update`
Remove a plugin from global configuration.

`$ opencode plugin remove @example/opencode-tui`
View all subcommands and flags.

`$ opencode plugin --help`
Shows shareable usage statistics.

`$ opencode stats`
Show the last 7 days.

`$ opencode stats --days 7`
Show model usage.

`$ opencode stats --models`
Show cost and token details.

`$ opencode stats --cost`
Print JSON instead of a report.

`$ opencode stats --json`
Show only the current project.

`$ opencode stats --project .`
View all subcommands and flags.

`$ opencode stats --help`
Starts the API and web server. See [Web](https://opencode.ai/docs/cli/web).

`$ opencode serve`
Bind to all interfaces on a fixed port.

`$ opencode serve --hostname 0.0.0.0 --port 4096`
Allow a browser client from another origin.

`$ opencode serve --cors https://app.example.com`
View all subcommands and flags.

`$ opencode serve --help`
Prints one-time links, plus a QR code of the first one, that sign a browser or app in to the server. Links expire after 5 minutes and work once.

`$ opencode pair`
Use an external URL in the links.

`$ opencode pair --url https://dev.example.com`
Pair from anywhere through an OpenTunnel remote address. This exposes the
server to the internet, so the first time it enables remote access it explains
this and asks you to accept. See [Remote access](https://opencode.ai/docs/cli/web#remote-access).

`$ opencode pair --remote`
Accept without a prompt, for example in a script without a terminal.

`$ opencode pair --remote --yes`
View all subcommands and flags.

`$ opencode pair --help`
Manages the background server. See [Web](https://opencode.ai/docs/cli/web).

`$ opencode service start`
Restart it.

`$ opencode service restart`
Show its status.

`$ opencode service status`
Stop it.

`$ opencode service stop`
Read a setting.

`$ opencode service get hostname`
Set a setting.

`$ opencode service set hostname 0.0.0.0`
Allow an extra CORS origin.

`$ opencode service set cors https://app.example.com`
Pass an environment variable to the server process.

`$ opencode service set env OPENCODE_LOG_LEVEL DEBUG`
Reset a setting to its default.

`$ opencode service unset hostname`
View all subcommands and flags.

`$ opencode service --help`
Reloads configuration without restarting the server. Running sessions continue with fresh services at the next step boundary.

`$ opencode reload`
Makes a request to the running server.

`$ opencode api GET /api/session`
Call an operation ID with a query parameter.

`$ opencode api session.list --param limit=10`
Send a JSON body.

`$ opencode api session.create --data '{"title": "New session"}'`
Add a request header.

`$ opencode api GET /api/session -H "accept: application/json"`
View all subcommands and flags.

`$ opencode api --help`
Starts an Agent Client Protocol server over stdin and stdout for editor integrations. It runs until the client closes the connection.

`$ opencode acp`
View all subcommands and flags.

`$ opencode acp --help`
Provides debugging and troubleshooting tools.

`$ opencode debug agents`
List configuration sources.

`$ opencode debug config`
Write a heap snapshot of the running background server and print its path.

`$ opencode debug heap-dump`
Write the snapshot into a directory of your choice.

`$ opencode debug heap-dump --directory ./snapshots`
Show global paths.

`$ opencode debug paths`
Print a single path.

`$ opencode debug paths db`
View all subcommands and flags.

`$ opencode debug --help`
Upgrades OpenCode to the latest or a specific version. Alias: `update`.

`$ opencode upgrade`
Upgrade to a specific version with a specific package manager.

`$ opencode upgrade 2.0.21 --method bun`
View all subcommands and flags.

`$ opencode upgrade --help`
Stops background services, removes the global cache, and uninstalls OpenCode. Session data, configuration, and state are not removed.

`$ opencode uninstall`
Preview what would be removed.

`$ opencode uninstall --dry-run`
View all subcommands and flags.

`$ opencode uninstall --help`
