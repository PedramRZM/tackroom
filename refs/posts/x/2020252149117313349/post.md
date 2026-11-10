---
title: "AI eliminated the natural barrier to entry that let OSS projects trust by default. People told me to do someth"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-02-07"
url: "https://x.com/mitchellh/status/2020252149117313349"
site: "x.com"
type: "post"
via: "fxtwitter"
---
AI eliminated the natural barrier to entry that let OSS projects trust by default. People told me to do something rather than just complain. So I did. Introducing Vouch: explicit trust management for open source. Trusted people vouch for others. https://github.com/mitchellh/vouch

The idea is simple: Unvouched users can't contribute to your projects. Very bad users can be explicitly "denounced", effectively blocked. Users are vouched or denounced by contributors via GitHub issue or discussion comments or via the CLI.

Integration into GitHub is as simple as adopting the published GitHub actions. Done. Additionally, the system itself is generic to forges and not tied to GitHub in any way.

Who and how someone is vouched or denounced is up to the project. I'm not the value police for the world. Decide for yourself what works for your project and your community.

All of the data is stored in a single flat text file in your own repository that can be easily parsed by standard POSIX tools or mainstream languages with zero dependencies.

My hope is that eventually projects can form a web of trust so that projects with shared values can share their vouch lists with each other (automatically) so vouching or denouncing a person in one project has ripple effects through to other projects.

The idea is based on the already successful system used by @badlogicgames in Pi. Thank you Mario.

Ghostty will be integrating this imminently.
