---
title: "In Claude Code, we’ve recently launched HTTP hooks, easier to use and more secure than existing command hooks!"
author: "Dickson Tsai (@dickson_tsai)"
date: "2026-03-04"
url: "https://x.com/dickson_tsai/status/2029235808235078095"
site: "x.com"
type: "post"
via: "fxtwitter"
---
In Claude Code, we’ve recently launched HTTP hooks, easier to use and more secure than existing command hooks! You can build a web app (even on localhost) to view CC’s progress, manage its permissions, and more. Then, now that you have a server with your hooks processing logic, you can easily deploy new changes or manage state across your CCs with a DB.

How do HTTP hooks work? CC posts the hook event to a URL of your choice and awaits a response. They work wherever hooks are supported, including plugins, custom agents, and enterprise managed settings.

Docs: https://code.claude.com/docs/en/hooks
