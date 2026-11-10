---
title: "Release v1.8.0 · vercel-labs/skills"
date: "2026-11-10"
url: "https://github.com/vercel-labs/skills/releases/latest"
site: "GitHub"
type: "article"
via: "direct"
---
## Repository navigation

## Changelog

- fix(update): keep locked skill paths inside the clone ([#2726](https://github.com/vercel-labs/skills/pull/2726))
- feat(add): skip agents whose install path is a category dir ([#2725](https://github.com/vercel-labs/skills/pull/2725))
- fix(installer): check all install targets before writing ([#2724](https://github.com/vercel-labs/skills/pull/2724))
- fix(installer): never delete agent category dirs on install ([#2723](https://github.com/vercel-labs/skills/pull/2723))
- fix(update): read only locked skill paths for project updates ([#2721](https://github.com/vercel-labs/skills/pull/2721))
- test: relax vitest timeouts on windows to reduce flakes ([#2720](https://github.com/vercel-labs/skills/pull/2720))
- fix: respect NO\_COLOR and TTY detection for all CLI escape codes ([#2716](https://github.com/vercel-labs/skills/pull/2716))
- fix(remove): only remove lock-tracked project skills with --all ([#2715](https://github.com/vercel-labs/skills/pull/2715))
- refactor: simplify GitHub rename following ([#2713](https://github.com/vercel-labs/skills/pull/2713))
- fix(cli): parse subcommand options with util.parseArgs ([#2712](https://github.com/vercel-labs/skills/pull/2712))
- feat(add): follow renamed GitHub repos to their canonical owner/repo ([#2711](https://github.com/vercel-labs/skills/pull/2711))
- fix(skills): support string metadata.internal values ([#2702](https://github.com/vercel-labs/skills/pull/2702))
- chore: keep factory-board.md out of the published npm package ([#2691](https://github.com/vercel-labs/skills/pull/2691))
- feat(lock): verifiable, portable computedHash and lock v2 ([#2685](https://github.com/vercel-labs/skills/pull/2685))
- fix(remove): remove skills installed as directory symlinks ([#2684](https://github.com/vercel-labs/skills/pull/2684))
- fix(cli): restore skills-lock.json with `skills install` / `skills i` and no source ([#2683](https://github.com/vercel-labs/skills/pull/2683))
- feat: lock direct downloads so update and restore can fetch them again ([#2682](https://github.com/vercel-labs/skills/pull/2682))
- feat(install): link restored skills into agent directories ([#2681](https://github.com/vercel-labs/skills/pull/2681))
- feat(install): keep restoring when a lock entry fails ([#2680](https://github.com/vercel-labs/skills/pull/2680))
- test(e2e): cover the programmatic API from the packed package ([#2675](https://github.com/vercel-labs/skills/pull/2675))
- fix(installer): skip metadata.json and cache dirs in blob installs ([#2674](https://github.com/vercel-labs/skills/pull/2674))
- test: add production e2e suite against packed tarball ([#2673](https://github.com/vercel-labs/skills/pull/2673))
- fix: stop well-known fallback on artifact digest mismatch ([#2670](https://github.com/vercel-labs/skills/pull/2670))
- feat: expose programmatic API ([#2666](https://github.com/vercel-labs/skills/pull/2666))
- build: Pin license checker for reproducible builds ([#2664](https://github.com/vercel-labs/skills/pull/2664))
- fix(git): enable core.longpaths so long Windows paths can be checked out ([#2637](https://github.com/vercel-labs/skills/pull/2637))
- fix(add): support /tree/ in GitHub SSH URLs ([#2636](https://github.com/vercel-labs/skills/pull/2636))
- fix(add): report lock file write failures instead of ignoring them ([#2606](https://github.com/vercel-labs/skills/pull/2606))
- fix(agents): install Antigravity global skills into \~/.gemini/config/skills ([#2566](https://github.com/vercel-labs/skills/pull/2566))
- refactor: route errors through a nostics diagnostic catalog ([#2561](https://github.com/vercel-labs/skills/pull/2561))
- fix: check out owner/repo@v1.2.3 instead of the default branch ([#2527](https://github.com/vercel-labs/skills/pull/2527))
- fix: discover skills in registered agent directories ([#2509](https://github.com/vercel-labs/skills/pull/2509))
- fix: exit by draining the event loop after telemetry flush ([#2462](https://github.com/vercel-labs/skills/pull/2462))
- chore: move Factory definitions to .vc/automations ([#2443](https://github.com/vercel-labs/skills/pull/2443))
- fix: reject incomplete well-known skill downloads ([#2386](https://github.com/vercel-labs/skills/pull/2386))
- fix: verify blob snapshot contents against the GitHub tree ([#2354](https://github.com/vercel-labs/skills/pull/2354))
- fix: misleading install summary for universal agents ([#2271](https://github.com/vercel-labs/skills/pull/2271))
- fix(parser): anchor GitHub and GitLab URL regexes to avoid rewriting proxy URLs ([#2079](https://github.com/vercel-labs/skills/issues/2079)) ([#2082](https://github.com/vercel-labs/skills/pull/2082))
- fix: initialize recursive submodules after clone ([#2075](https://github.com/vercel-labs/skills/pull/2075))
- fix: never delete unmanaged files from collision-prone agent dirs on remove ([#1771](https://github.com/vercel-labs/skills/issues/1771)) ([#2073](https://github.com/vercel-labs/skills/pull/2073))
- feat: add ctrl+a select all to search multiselect ([#1872](https://github.com/vercel-labs/skills/pull/1872))
- fix(add): treat --agent '\*' as a blanket selection when skipping global-less agents ([#1421](https://github.com/vercel-labs/skills/pull/1421))
- fix: remove only lockfile-managed global skills ([#609](https://github.com/vercel-labs/skills/pull/609))
