---
title: "13/ Use --add-dir to give Claude access to more folders"
author: "Boris Cherny (@bcherny)"
date: "2026-03-30"
url: "https://x.com/bcherny/status/2038454359047156203"
site: "x.com"
type: "post"
via: "fxtwitter"
---
13/ Use --add-dir to give Claude access to more folders

When working across multiple repositories, I usually start Claude in one repo and use --add-dir (or /add-dir) to let Claude see the other repo. This not only tells Claude about the repo, but also gives it permissions to work in the repo.

Or, add "additionalDirectories" to your team's settings.json to always load in additional folders when starting Claude Code.

https://code.claude.com/docs/en/cli-reference
