---
title: "Integrate with Reasonix | DeepSeek API Docs"
date: "2026-01-01"
url: "https://api-docs.deepseek.com/quick_start/agent_integrations/reasonix"
site: "api-docs.deepseek.com"
type: "article"
via: "direct"
---
# Integrate with Reasonix

Reasonix is a coding agent that runs in the terminal.

#### 1. Install Node.js[](https://api-docs.deepseek.com#1-install-nodejs)

- Install [Node.js](https://nodejs.org/en/download/) 20.10+.
- Windows users need to install [Git for Windows](https://git-scm.com/download/win).

#### 2. Get a DeepSeek API Key[](https://api-docs.deepseek.com#2-get-a-deepseek-api-key)

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). The first run of Reasonix prompts for it via a built-in wizard and persists it to `~/.reasonix/config.json` — no environment variable needed.

#### 3. Enter the project directory and run `npx reasonix code` to get started.[](https://api-docs.deepseek.com#3-enter-the-project-directory-and-run-npx-reasonix-code-to-get-started)

```
cd /path/to/my-project
npx reasonix code
```
No global install required. By default Reasonix uses **DeepSeek-V4-Flash** for cost-efficient iteration. Type `/pro` inside the TUI to arm **DeepSeek-V4-Pro** for the next turn, or `/preset max` to use Pro for the whole session. Run `/help` for the full slash-command reference.
