---
title: "Our new experimental NO_FLICKER renderer solves this by virtualizing the entire viewport."
author: "Boris Cherny (@bcherny)"
date: "2026-04-01"
url: "https://x.com/bcherny/status/2039421581907374320"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Our new experimental NO_FLICKER renderer solves this by virtualizing the entire viewport.

We hook into keyboard and mouse events to make scrolling work, and we virtualize the viewport to move control over what is rendered into the application layer.

This approach has tradeoffs, but feels surprisingly good in practice. It is a way of living within the constraints of a terminal renderer, while giving you a richer and more performant user experience.
