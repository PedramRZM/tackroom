---
title: "The problem with the \"if it works who cares what the code looks like\" mindset for agentic work is that it assu"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-06-15"
url: "https://x.com/mitchellh/status/2066657032938442833"
site: "x.com"
type: "post"
via: "fxtwitter"
---
The problem with the "if it works who cares what the code looks like" mindset for agentic work is that it assumes the agent has a perfect understanding of "works." Realistically, things are underspecified, agents make bad assumptions, etc.

To be fair, agents are pretty good at unit test coverage. They're pretty bad at designing human experiences (API, CLI flags, etc.), especially cohesive ones for future roadmap plans they may not have visibility into (unless your backlog is perfect and vision fully laid out, which I doubt). They're bad at knowing where performance matters and what type (CPU vs memory tradeoffs). They're bad at where compatibility matters and where it doesn't (and tend to err on the side of preserving it without further guidance). Etc.

Unless you have this ALL specified, you can't possibly claim "it works" without taking a look and thinking about it.
