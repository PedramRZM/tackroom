---
title: "Building verification loops in Claude Code"
author: "Claude"
url: "https://www.youtube.com/watch?v=mQZB0l-rhxE"
site: "youtube.com"
type: "video"
via: "invidious:yt.chocolatemoo53.com"
---
# Building verification loops in Claude Code

Caption track: English. Timestamps mark the start of each paragraph.

[00:00] For every prompt you send, Claude Code runs a loop. It gathers context, takes action, verifies its work, and responds. Today, part of that verify step is you in the browser, clicking around, watching the console, then telling Claude what to fix. But that part doesn't always have to be you. Claude is already good at checking its work against what's in your codebase. It runs your tests, type checks, and linters, and fixes what they catch. But passing all of those doesn't prove the change does what you meant. What proves it is the check you do by hand afterwards. On a web app, you might open the page, click around and watch the console. On a back end, you might call an endpoint and read the response. On a mobile app, you tap through the screens in a simulator. If you codify those steps in your project, Claude can run them itself using tools like a browser, the terminal, and an iOS simulator. When something's wrong, it can fix it and run them again.

[01:01] A good place to start is the verify skill that comes with Claude Code. The first time you use it, it runs your app and checks your change in the app itself. Then it saves the steps that worked as a skill in your project. Now, you should treat the generated skill as a starting point and extend what Claude checks. For example, on a web app, one thing that I always look for is layout shift, where parts of the page jump as content loads. You can codify that as a performance trace through Google Chrome's DevTools MCP, which measures layout shift as one of the Core Web Vitals. In this skill, you can say when Claude should run it, what to do when a check fails, and what proves each check passed. The more measurable a check is, the easier it is for Claude to tell whether it's passed or not. Let's try the verify skill we just created. I will ask Claude to add a Like button to a page I've been working on, which also has some layout shift I haven't yet fixed. Claude will make the

[02:02] edit, and because it's a UI change, it will run the skill on its own. It starts the dev server, opens the page, clicks the Like button, and takes a screenshot to prove that it works. Then it runs the performance trace, which finds layout shift. Claude fixes it and runs the checks again, and this time they pass. What I get back is a working Like button, a page that no longer jumps on load, and the screenshots and scores to prove it. Claude runs that verification loop itself without me having to point anything out. Alright, hopefully that gives you the idea. The more Claude can verify its own work, the further it gets on its own. The result is better, and it takes fewer rounds of back and forth to get there. So whenever you catch yourself checking something by hand and telling Claude what to fix, ask whether there's something Claude can measure its work against. That could be a performance budget, an accessibility checklist, or your design system's rules.

[03:02] Then codify it, so that the next time it's part of Claude's verification loop.
