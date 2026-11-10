---
title: "I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing var"
author: "Boris Cherny (@bcherny)"
date: "2026-09-22"
url: "https://x.com/bcherny/status/2102543349102338309"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached.

TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt.

I don't know either language well, but Claude is excellent at both. This approach is super useful for formally modeling your code and finding bugs that a human probably wouldn't have spotted.

Is formal verification the future of coding (or at least, bug finding)?

Media: https://video.twimg.com/amplify_video/2102541708466769920/vid/avc1/1584x1200/T7hY-sKgG3C1nHto.mp4?tag=29
