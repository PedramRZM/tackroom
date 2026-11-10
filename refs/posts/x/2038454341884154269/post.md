---
title: "3/ Two of the most powerful features in Claude Code: /loop and /schedule"
author: "Boris Cherny (@bcherny)"
date: "2026-03-30"
url: "https://x.com/bcherny/status/2038454341884154269"
site: "x.com"
type: "post"
via: "fxtwitter"
---
3/ Two of the most powerful features in Claude Code: /loop and /schedule

Use these to schedule Claude to run automatically at a set interval, for up to a week at a time.

I have a bunch of loops running locally:

- /loop 5m /babysit, to auto-address code review, auto-rebase, and shepherd my PRs to production
- /loop 30m /slack-feedback, to automatically put up PRs for Slack feedback every 30 mins
- /loop /post-merge-sweeper to put up PRs to address code review comments I missed
- /loop 1h /pr-pruner to close out stale and no longer necessary PRs
- lots more!..

Experiment with turning workflows into skills + loops. It's powerful.

https://code.claude.com/docs/en/scheduled-tasks
