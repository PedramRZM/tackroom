---
title: "Good moment today to remind everyone to stay frosty with AI. I was working on making a server stoppable via th"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-08-17"
url: "https://x.com/mitchellh/status/2089446702285758559"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Good moment today to remind everyone to stay frosty with AI. I was working on making a server stoppable via the CLI, and Codex decided the best path forward was to implement an unauthenticated network API to every server to shut itself down. Excellent work.

I responded with "I don't know about that." (I usually give more direct feedback but this was so absurd) and it thought for like 20 seconds and responded "Server stopping should not be part of an unauthenticated network API." Yes. lol. 

By the way, the result I was looking for was that we automatically start a locally discovery Unix-socket bound server so I wanted it to discover that (using prior mechanisms already made) and gracefully stop that. 

The driver is absolutely accountable here (me). My lazy prompting led AI to think I wanted to be able to stop ANY configured server I was talking to. Shame on me for thinking it was obvious here. But, I also reviewed it and found this idiocy, so, that's where good AI drivers come in. Also me.
