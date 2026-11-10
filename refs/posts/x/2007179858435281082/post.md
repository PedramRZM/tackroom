---
title: "12/ For very long-running tasks, I will either (a) prompt Claude to verify its work with a background agent wh"
author: "Boris Cherny (@bcherny)"
date: "2026-01-02"
url: "https://x.com/bcherny/status/2007179858435281082"
site: "x.com"
type: "post"
via: "fxtwitter"
---
12/ For very long-running tasks, I will either (a) prompt Claude to verify its work with a background agent when it's done, (b) use an agent Stop hook to do that more deterministically, or (c) use the ralph-wiggum plugin (originally dreamt up by @GeoffreyHuntley). I will also use either --permission-mode=dontAsk or --dangerously-skip-permissions in a sandbox to avoid permission prompts for the session, so Claude can cook without being blocked on me.

https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum

https://code.claude.com/docs/en/hooks-guide

Media: https://pbs.twimg.com/media/G9ro4W5bEAAQ3ug.jpg?name=orig
