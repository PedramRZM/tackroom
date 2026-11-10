---
title: "In case it’s not clear in the docs:"
author: "Boris Cherny (@bcherny)"
date: "2026-01-28"
url: "https://x.com/bcherny/status/2016339448863355206"
site: "x.com"
type: "post"
via: "fxtwitter"
---
In case it’s not clear in the docs:

- Ancestor http://CLAUDE.md’s are loaded into context automatically on startup
- Descendent http://CLAUDE.md’s are loaded *lazily* only when Claude reads/writes files in a folder the http://CLAUDE.md is in. Think of it as a special kind of skill.

We designed it this way for monorepos and other big repos, tends to work pretty well in practice.
