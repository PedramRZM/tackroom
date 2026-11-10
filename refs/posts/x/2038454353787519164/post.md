---
title: "10/ Use git worktrees"
author: "Boris Cherny (@bcherny)"
date: "2026-03-30"
url: "https://x.com/bcherny/status/2038454353787519164"
site: "x.com"
type: "post"
via: "fxtwitter"
---
10/ Use git worktrees

Claude Code ships with deep support for git worktrees. Worktrees are essential for doing lots of parallel work in the same repository. I have dozens of Claudes running at all times, and this is how I do it.

Use claude -w to start a new session in a worktree, or hit the "worktree" checkbox in the Claude Desktop app.

For non-git VCS users, use the WorktreeCreate hook to add your own logic for worktree creation.

Learn more: https://x.com/bcherny/status/2025007393290272904

> Quoting @bcherny: Introducing: built-in git worktree support for Claude Code 
> 
> Now, agents can run in parallel without interfering with one other. Each agent gets its own worktree and can work independently.
> 
> The Claude Code Desktop app has had built-in support for worktrees for a while, and now we're bringing it to CLI too.
> 
> Learn more about worktrees: https://git-scm.com/docs/git-worktree
