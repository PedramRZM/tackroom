---
title: "Permissions"
date: "2026-01-01"
url: "https://opencode.ai/docs/permissions/"
site: "opencode.ai"
type: "doc"
via: "direct"
---
# Permissions

Permissions control whether an agent may perform an action on a resource.

A common setup is to ask before running shell commands, allow routine Git
inspection, and always block pushes. Add these ordered rules to `opencode.jsonc`:

```
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" },
    { "action": "shell", "resource": "git push *", "effect": "deny" },
  ],
}
```
The last matching rule wins, so the specific exceptions follow the broad rule.

Each rule requires three string fields:

| Field | Meaning | 
|---|---|
| `action` | Tool permission action | 
| `resource` | Value being used, such as a path, command, URL, query, skill ID, or agent ID | 
| `effect` | `allow`, `deny`, or `ask` | 

```
{
  "permissions": [
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "read", "resource": "*.env", "effect": "deny" },
  ],
}
```
| Effect | Result | 
|---|---|
| `allow` | Continue without prompting | 
| `deny` | Block the operation | 
| `ask` | Wait for a decision from the client | 

If no rule matches, OpenCode uses `ask`.

Actions and resources use simple whole-value wildcards:

| Pattern | Match | 
|---|---|
| `*` | Zero or more characters, including `/` | 
| `?` | Exactly one character | 
| Other | The literal character | 

```
{
  "permissions": [
    { "action": "edit", "resource": "packages/docs/*.mdx", "effect": "allow" },
  ],
}
```
This pattern matches the entire normalized path. Backslashes are normalized to slashes, and matching is case-insensitive on Windows.

A shell pattern ending in  `*` also matches the command without arguments:

`{ "action": "shell", "resource": "git status *", "effect": "allow" }`
This matches both `git status` and `git status --short`.

OpenCode combines rules in order and uses the last match. Lower-priority configuration is loaded first, global rules are appended next, and agent rules are appended last.

```
{
  "permissions": [
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "read", "resource": "secrets/*", "effect": "deny" },
  ],
}
```
Operations may check several resources, such as a patch that touches multiple
files. Any `deny` denies the operation; otherwise any `ask` asks; otherwise the
operation is allowed.

V2 action names are strings, so plugins may define more actions. Built-in tools currently use these actions and resources:

| Action | Resource | 
|---|---|
| `read` | Location-relative internal path or canonical absolute external path | 
| `edit` | Target path for `edit`, `write`, and `patch` | 
| `glob` | Requested glob pattern | 
| `grep` | Requested regular expression, not the search path | 
| `shell` | Scanner-produced command string; compound commands may produce several | 
| `subagent` | Target agent ID | 
| `skill` | Skill ID | 
| `question` | `*` | 
| `webfetch` | Requested URL | 
| `websearch` | Search query | 
| `experimental_image_generate` | Selected image model as `providerID/modelID`, plus `#variant` when set | 
| `external_directory` | Canonical external directory boundary, normally ending in `/*` | 
| `<server>_<tool>` | `*` for an MCP tool; unsupported characters in both names become `_` | 
| `opencode_list_mcp_resources` | MCP server name | 
| `opencode_read_mcp_resource` | `<server>:<uri>` | 
| `execute` | `*`; a deny removes Code Mode and the tools reached only through it, while nested tools enforce their rules | 

For example, allow one skill and deny all other skills:

```
{
  "permissions": [
    { "action": "skill", "resource": "*", "effect": "deny" },
    { "action": "skill", "resource": "effect", "effect": "allow" },
  ],
}
```
`doom_loop` and `lsp` are not current V2 Core permission actions.

A path outside both the active Location and its non-root project worktree is
checked against `external_directory` before its `read` or `edit` rules. The
default policy allows `external_directory`, so external paths are not prompted
unless you add a rule. To be asked before any access outside the project:

```
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "external_directory", "resource": "*", "effect": "ask" },
  ],
}
```
Narrower rules after it can allow or deny specific directories:

```
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "external_directory", "resource": "~/projects/reference/*", "effect": "allow" },
    { "action": "read", "resource": "~/projects/reference/*", "effect": "allow" },
    { "action": "edit", "resource": "~/projects/reference/*", "effect": "deny" },
  ],
}
```
This applies to external paths used by `read`, `edit`, `write`, and `patch`.
Shell checks its external working directory and directories inferred by its
scanner before checking `shell` resources.

For `external_directory`, `read`, and `edit`, a leading `~`, `~/`, `$HOME`, or
`$HOME/` is expanded when configuration loads:

`{ "action": "read", "resource": "$HOME/reference/*", "effect": "allow" }`
Shell resources remain raw command text and are not home-expanded.

Relative mutation paths may leave the active Location while remaining inside its project worktree. Explicit external paths are canonicalized before matching, so authorize only trusted directory boundaries.

Shell permission checks use OpenCode’s built-in shell scanner across Bash, Zsh, POSIX `sh`, and PowerShell. A command with malformed syntax or dynamic evaluation that the scanner cannot safely analyze returns a scanner error rather than executing unverified subcommands.

```
{
  "$schema": "https://opencode.ai/config.json",
  "policies": [
    {
      "permissions": [
        { "action": "shell", "resource": "git status *", "effect": "allow" },
        { "action": "shell", "resource": "rm *", "effect": "deny" },
      ],
    },
  ],
}
```
Permission rules, saved approval patterns, and best-effort directory inference apply to every extracted subcommand and `cd` target. There is no extra approval mode or blanket restriction for unknown directories.

Every agent, including custom agents, starts with this ordered base policy:

```
[
  { "action": "*", "resource": "*", "effect": "allow" },
  { "action": "read", "resource": "*.env", "effect": "ask" },
  { "action": "read", "resource": "*.env.*", "effect": "ask" },
  { "action": "read", "resource": "*.env.example", "effect": "allow" },
]
```
Shipped agents append these policies:

| Agent | Additional policy | 
|---|---|
| `build` | Allows questions | 
| `plan` | Allows questions; denies edits except files under `~/.opencode/plan` | 
| `general` | Denies questions and launching subagents | 
| `explore` | Denies everything except shell, reads, globs, grep, web fetches, web searches, and external directories; asks for `.env` reads | 
| `title` | Denies all actions | 
| `summary` | Denies all actions | 
| `compaction` | Keeps the base policy | 

Because no default rule asks for `external_directory`, reads and edits outside
the Location and worktree proceed without a prompt. Add an
`external_directory` `ask` or `deny` rule, as shown in
[Directories](https://opencode.ai#directories), to restore a prompt or block outside access.
Later global and agent rules override these defaults.

Put shared rules at the top level and narrower rules under
`agents.<id>.permissions`:

```
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
  ],
  "agents": {
    "reviewer": {
      "description": "Review code without changing it",
      "mode": "subagent",
      "permissions": [
        { "action": "edit", "resource": "*", "effect": "deny" },
      ],
    },
  },
}
```
Agent rules are appended after global rules; they do not replace the global array. A custom subagent uses its own permissions, not a subset of its parent’s permissions.

When a rule resolves to `ask`, clients can reply with:

| Choice | Reply | Result | 
|---|---|---|
| Allow once | `once` | Approve only the pending request | 
| Allow always | `always` | Approve it and save the tool’s proposed patterns for the project | 
| Reject | `reject` | Reject it and every other pending permission request in that session | 

For example, choosing **Allow always** for `git status --short` may save a
shell prefix that covers later `git status` commands:

`shell: git status * → allow`
Saved approvals are durable, project-scoped `allow` rules. They never override
a configured `deny`. Tools choose the proposed saved pattern: some propose `*`,
shell proposes command prefixes, and skills and subagents propose their IDs.
Review broad approvals and remove those no longer needed.

Clients may attach feedback when rejecting. Non-interactive clients must decide
how to handle approval requests; configured `deny` rules always remain enforced.

A [policy](https://opencode.ai/docs/policies) can hard-deny a permission check after these rules and saved
approvals run. It turns `allow` or `ask` into `deny` and never grants access.

```
{
  "policies": [{ "action": "tool.use", "resource": "shell:sudo *", "effect": "deny" }],
}
```
Global and Console-managed policies override project configuration, which is how an organization blocks a command that a repository would allow.
