---
title: "Listen to this guy."
author: "Kent C. Dodds 🐨 (@kentcdodds)"
date: "2026-11-09"
url: "https://x.com/kentcdodds/status/2119812466037428392"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Listen to this guy.

Try this prompt I slightly adjusted from some who I think got it from @steveruizok:

Find all of the implicit state machines in my app (there are probably a ton). Make the best decision that will elevate all three: the user experience (UX), developer experience (DX), and agent experience (AX) always, without breaking anything. Also, make state machines explicit.

> Quoting @DavidKPiano: What is an implicit state machine? 
> 
> Your apps are full of state machines, which is the logic that says "when we're in this state, and this event happens, now we're in this state" (given, when, then).
> 
> Sometimes those state machines are clearly mapped out (switch statements, reducers, tables/maps, libraries like XState for the more complex ones, etc.) and the logic is explicitly enumerable.
> 
> And sometimes it's not. The ad-hoc logic is spread all over the place. That's how developers typically code, and that's how agents typically vibe-code (they learned from you). Those are implicit state machines.
> 
> What's wrong with implicit state machines? It's not clear what state transitions are possible, so you might have "allowed" states that should have been impossible without knowing it. Agents make the same mistakes. 
> 
> You can get all tests passing and your code review agents (even the well-funded ones) can say "LGTM" and you can *still* have very bad bugs because an implicit state machine allowed unexpected or illegal behavior. (Remember the Apple FaceTime bug?)
> 
> So yeah, making your app logic explicit is important.
