---
title: "Convert chrome-devtools (or really any) MCP to compiled cli with this one weird trick:"
author: "Peter Steinberger (@steipete)"
date: "2025-11-08"
url: "https://x.com/steipete/status/1986968745504334300"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Convert chrome-devtools (or really any) MCP to compiled cli with this one weird trick:

>npx mcporter generate-cli "npx -y chrome-devtools-mcp" --compile

Store somewhere + add a one-liner to agents file. It will call help menu and learn as needed. Progressive disclosure, no context pollution.

Media: https://pbs.twimg.com/media/G5L-Wf_WUAAHhOy.jpg?name=orig
