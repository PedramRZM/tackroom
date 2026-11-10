---
title: "To simplify our system, I asked Opus to port the file indexer to native TypeScript. Here's the prompt I used:"
author: "Boris Cherny (@bcherny)"
date: "2026-04-09"
url: "https://x.com/bcherny/status/2042352725481177315"
site: "x.com"
type: "post"
via: "fxtwitter"
---
To simplify our system, I asked Opus to port the file indexer to native TypeScript. Here's the prompt I used:

> compile our rust+napi file index to native ts. compile the code over, and make sure the code perfectly passes the ORIGINAL test suite from the package. then profile compared to napi/wasm, and put up a pr with the result. dont stop until you have conclusively proven that the new impl is faster.

I then followed up with:

> anything else you can do to improve performance? profile it in <large monorepo>. hoping for p99 < 10ms

And:

> im still feeling a little stutter when i first start typing "@ cc"

Finally:

> nice that feels really good. /go
