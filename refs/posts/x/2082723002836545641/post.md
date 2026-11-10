---
title: "Software quality now depends on the constraints you set around your agents."
author: "Addy Osmani (@addyosmani)"
date: "2026-07-30"
url: "https://x.com/addyosmani/status/2082723002836545641"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Software quality now depends on the constraints you set around your agents.

When humans manually wrote most of the code we could look at the code itself for signs of quality. Is it clean? Is it thoughtful? Is it fast? Can another engineer understand it? Does it have tests?

Agents can now generate more code than people can read. When code generation scales beyond review, quality - checks for one or more of correctness, maintainability, security, performance etc - increasingly has to live somewhere else.

It moves into the harness, environment and operating system around the agent.

This can be the tests and deterministic checks that decide what the system is allowed to do (amongst others). Your constraints are what may eventually enable loops of agents to deliver production software reliably. They can include unit tests, property tests, acceptance tests, mutation testing and quality metrics. 

This back-pressure lets the system resist bad work before it becomes somebody elses problem. 

Set your constraints. They decide whether the code your agents generate is good enough to ship.

Media: https://pbs.twimg.com/media/HOdPzoWaYAA6dgQ.jpg?name=orig
