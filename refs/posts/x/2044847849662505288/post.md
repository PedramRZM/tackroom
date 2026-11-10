---
title: "1/ Auto mode = no more permission prompts"
author: "Boris Cherny (@bcherny)"
date: "2026-04-16"
url: "https://x.com/bcherny/status/2044847849662505288"
site: "x.com"
type: "post"
via: "fxtwitter"
---
1/ Auto mode = no more permission prompts

Opus 4.7 loves doing complex, long-running tasks like deep research, refactoring code, building complex features, iterating until it hits a performance benchmark.

In the past, you either had to babysit the model while it did these sorts of long tasks, our use --dangerously-skip-permissions.

We recently rolled out auto mode as a safer alternative. In this mode, permission prompts are routed to a model-based classifier to decide whether the command is safe to run. If it's safe, it's auto-approved.

This means no more babysitting while the model runs. More than that, it means you can run more Claudes in parallel. Once a Claude is cooking, you can switch focus to the next Claude.

Auto mode is now available for Opus 4.7 for Max, Teams, and Enterprise users. Shift-tab to enter auto mode in the CLI, or choose it in the dropdown in Desktop or VSCode.

Media: https://pbs.twimg.com/media/HGC8zk8a4AA5aag.png?name=orig
