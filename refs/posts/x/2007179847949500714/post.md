---
title: "7/ I use slash commands for every \"inner loop\" workflow that I end up doing many times a day. This saves me fr"
author: "Boris Cherny (@bcherny)"
date: "2026-01-02"
url: "https://x.com/bcherny/status/2007179847949500714"
site: "x.com"
type: "post"
via: "fxtwitter"
---
7/ I use slash commands for every "inner loop" workflow that I end up doing many times a day. This saves me from repeated prompting, and makes it so Claude can use these workflows, too. Commands are checked into git and live in .claude/commands/.

For example, Claude and I use a /commit-push-pr slash command dozens of times every day. The command uses inline bash to pre-compute git status and a few other pieces of info to make the command run quickly and avoid back-and-forth with the model (https://code.claude.com/docs/en/slash-commands#bash-command-execution)

Media: https://pbs.twimg.com/media/G9rj3eFasAEK_8J.jpg?name=orig
