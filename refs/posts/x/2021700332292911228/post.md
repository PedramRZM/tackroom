---
title: "5/ Pre-approve common permissions"
author: "Boris Cherny (@bcherny)"
date: "2026-02-11"
url: "https://x.com/bcherny/status/2021700332292911228"
site: "x.com"
type: "post"
via: "fxtwitter"
---
5/ Pre-approve common permissions

Claude Code uses a sophisticated permission system with a combo of prompt injection detection, static analysis, sandboxing, and human oversight.

Out of the box, we pre-approve a small set of safe commands. To pre-approve more, run /permissions and add to the allow and block lists. Check these into your team's settings.json.

We support full wildcard syntax. Try "Bash(bun run *)" or "Edit(/docs/**)"

https://code.claude.com/docs/en/permissions

Media: https://pbs.twimg.com/media/HA6FurbbsAM95NS.png?name=orig
