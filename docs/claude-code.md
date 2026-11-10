# Claude Code setup

What each file under `template/.claude/` does, what belongs in your personal settings instead,
and how to switch on the sandbox. Facts about Claude Code come from its documentation as saved
on 2026-11-10 (version 2.1.322); the digests are `refs/notes/claude-code-docs-*.md`.

## Files

| File | What it does |
|---|---|
| `settings.json` | Permission rules, sandbox configuration and the four hooks. Shared and committed. |
| `hooks/guard.py` | Runs before Bash, Read, Edit and Write. Blocks secret-looking files, wide recursive deletes, force-pushes, pushes to a protected branch, and writes to curated memory outside the dream pass. |
| `hooks/stop-check.py` | Runs when a turn ends. If files changed since the last passing run, runs `scripts/agent/check --quick` and sends a failure back to the agent once. |
| `hooks/format.py` | Formats an edited file with the formatter the project already uses (Biome, Prettier, Ruff, rustfmt, gofmt). Does nothing when it finds none. |
| `hooks/session-context.sh` | At session start, resume and after compaction: prints the branch, the task id, and the task's plan file if there is one. |
| `skills/` | `verify`, `spec`, `task`, `second-opinion`, `wrap-up`, and three you start yourself: `dream`, `careful`, `lock-tests`. |
| `agents/` | `reviewer` (fresh-context review), `memory-analyzer` and `memory-organizer` (used by `dream`). |

Edit the lists at the top of `guard.py` to fit a project: `PROTECTED_BRANCHES`,
`SECRET_NAMES`, the careful-mode patterns.

## What a project file can and cannot do

A committed `.claude/settings.json` is limited on purpose
(`refs/notes/claude-code-docs-settings-security.md` 1.5, 1.6):

- Its **deny and ask rules apply immediately**. Its **allow rules, hooks and most `env` values
  wait until you accept the trust prompt** for the folder. Start Claude Code interactively once
  in a new project and accept it.
- It **cannot switch on auto mode** or bypass-permissions, and it cannot configure the auto
  mode classifier. Those are personal settings.
- A **personal skill with the same name as a project skill wins**. If you keep skills in
  `~/.claude/skills/` named `verify`, `spec`, `task` and so on, they shadow these.
- Skills named `verify` or `simplify` are run by Claude Code before each commit. The template's
  `verify` skill replaces the bundled `/verify` on purpose
  (`refs/notes/claude-code-docs-extending.md` 2.10).

## Permission mode: your choice, not the template's

The template does not set a default mode. On current versions interactive sessions start in
auto mode on most plans. Anthropic's guidance is that auto mode is the working default, with
deny rules for what must never happen and a sandbox underneath
(`refs/notes/anthropic-claude-com-practice.md` (g); `refs/notes/anthropic-engineering.md`,
finding 6). Its measured weakness: it missed 17% of overeager actions in a small test set
(same notes, finding 5).

The two ask rules in the template (`gh pr merge`, and unsandboxed retries) prompt in every mode.
In a headless run an ask rule means the action is refused, which is the intent: an unattended
agent opens a pull request and does not merge it.

## The sandbox

The settings file configures the Bash sandbox but does not enable it. Enabling is a per-machine
decision, made with `/sandbox`, which records it in your gitignored
`.claude/settings.local.json`.

Why it is worth doing: it is the only layer here that the operating system enforces. With it
on, the template's `Read` deny rules also apply to shell commands, the listed credential
variables are hidden from commands, and the network is limited to the package registries listed
(`refs/notes/claude-code-docs-settings-security.md` 5.4).

### Ubuntu 24.04 and later

On the machine this was built on, sandboxed commands failed with:

    apply-seccomp: write /proc/self/setgroups (nested userns is capability-restricted;
    caller must provide CAP_SYS_ADMIN): Permission denied

Ubuntu restricts unprivileged user namespaces through AppArmor. The documented fix is a profile
for `bwrap` (`refs/articles/code.claude.com/docs-en-sandboxing-md/article.md`, "Add an AppArmor
profile for bubblewrap"). It needs root, so run it yourself:

    sudo tee /etc/apparmor.d/bwrap > /dev/null <<'EOF'
    abi <abi/4.0>,
    include <tunables/global>

    profile bwrap /usr/bin/bwrap flags=(unconfined) {
      userns,
      include if exists <local/bwrap>
    }
    EOF
    sudo systemctl reload apparmor

Then restart Claude Code, run `/sandbox`, and confirm with two commands the docs suggest:
`touch ~/sandbox-probe` should fail with a read-only error, and
`curl --noproxy '*' https://example.com` should fail to resolve. This fix has not been tried
here, and the error above is not the exact message the docs list, so treat it as the first
thing to try, not a guarantee.

### What breaks with the sandbox on (Linux)

From the docs (`refs/notes/claude-code-docs-settings-security.md` 5.2, 5.5):

- A sandboxed command cannot reach a dev server or database on the host's localhost.
- Chromium, and so Playwright, will not start inside it.
- `docker` is incompatible; database clients and plain `ssh` ignore the proxy.

For those, add the specific command to `sandbox.excludedCommands` in the project's settings
(for example `docker compose *` or the end-to-end test command), knowing an excluded command
runs with your full access. GitHub is not in the network allowlist: the docs warn that a broad
domain like `github.com` is an exfiltration path, so the first `gh` or `git` call over HTTPS
will prompt and you can allow it locally.

## Hooks: details worth knowing

- They run with the system Python (`/usr/bin/python3`) directly. Going through a version
  manager's shim added about 0.2 seconds to every tool call on the build machine.
- The guard is fail-closed (`onFailure: "block"`): if the script itself crashes, the tool call
  is blocked. That is loud on purpose. If every tool call is being refused, run
  `template/.claude/hooks/tests/test_guard.sh` to see why.
- On Linux and macOS Claude Code searches through Bash, not through Grep and Glob tools, so the
  guard watches Bash commands for secret file names as well
  (`refs/notes/claude-code-docs-settings-security.md`, closing notes).
- Hooks run outside the sandbox with your full access. Read a hook before trusting a
  repository that ships one, including this one.
- Without managed settings, an installed mod can approve a call that a deny rule or hook
  blocked (`refs/notes/claude-code-docs-settings-security.md`, ambiguity 8).

## Headless runs

`claude -p "..."` in a folder you have not trusted runs the project's hooks but ignores its
allow rules, so most shell commands are refused. Trust the folder first, or pass
`--permission-mode` explicitly. `--setting-sources project` loads only the project's settings,
skills, agents and instruction files; it was used for the live tests of this template. `--bare`
skips all of them, and the docs say it will become the default for `-p` in a future release, so
scripts that rely on project hooks should not use it
(`refs/notes/claude-code-docs-hooks-mcp-automation.md` 4.6).

## Cloud sessions

Cloud sessions clone the repository, so committed skills, hooks and settings travel with it
and `~/.claude` does not. Project threads in the Projects feature are narrower: they load
`CLAUDE.md` and root rules but not skills, hooks or settings
(`refs/notes/task-backlog-epic-management.md`, finding 14). That is why the working contract is
in `WORKFLOW.md` and `AGENTS.md`, which they do read, and the skills are thin.
