---
title: "There's a lot of tradeoffs when building for the terminal. Unlike web, mobile, and desktop, terminal have fair"
author: "Boris Cherny (@bcherny)"
date: "2026-04-01"
url: "https://x.com/bcherny/status/2039421580435222576"
site: "x.com"
type: "post"
via: "fxtwitter"
---
There's a lot of tradeoffs when building for the terminal. Unlike web, mobile, and desktop, terminal have fairly restrictive instruction sets for rendering: ANSI escape codes.

There's an ANSI code for "move cursor to (x, y)", another for "write 'foo'", etc. It feels a little like writing Assembly.

Because there is no ANSI code for "move the cursor to (x, -y)" to repaint a row that is out of the viewport, we have to use the code for "clear the entire screen" -- aka, flickering.
