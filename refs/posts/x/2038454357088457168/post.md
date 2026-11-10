---
title: "12/ Use --bare to speed up SDK startup by up to 10x"
author: "Boris Cherny (@bcherny)"
date: "2026-03-30"
url: "https://x.com/bcherny/status/2038454357088457168"
site: "x.com"
type: "post"
via: "fxtwitter"
---
12/ Use --bare to speed up SDK startup by up to 10x

By default, when you run claude -p (or the TypeScript or Python SDKs) we search for local CLAUDE.md's, settings, and MCPs.

But for non-interactive usage, most of the time you want to explicitly specify what to load via --system-prompt, --mcp-config, --settings, etc.

This was a design oversight when we first built the SDK, and in a future version, we will flip the default to --bare. For now, opt in with the flag.

Media: https://pbs.twimg.com/media/HEn6dsabEAAQQE1.jpg?name=orig
