---
title: "Claude Code: Auto mode"
author: "Delba (@delba_oliveira)"
date: "2026-06-11"
url: "https://x.com/delba_oliveira/status/2065106020347613598"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Claude Code: Auto mode

Auto mode lets Claude safely complete long-running tasks without asking permission for every action. But how does it work?

4 key terms:

• Classifier: a separate model that approves or denies each action based on your intent and scope
• Filtering: the classifier only sees your messages and Claude's tool calls, not Claude’s reasoning or tool outputs, so it isn't influenced when making decisions
• Tier check: read-only and easily-undone actions (like edits inside your repo) skip the classifier; everything else goes through it
• Probe: a server-side check that scans incoming content, like web pages, for prompt injection and flags it to Claude

I'm working on a longer video that explains how auto mode works and how to configure it.

What questions do you have about it?

Media: https://video.twimg.com/amplify_video/2065100915124666368/vid/avc1/2880x2160/7qqgc439XBK4VHS1.mp4?tag=27
