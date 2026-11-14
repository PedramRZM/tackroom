# Isolated environments for a GitHub-board coding agent

**Current direction:** [Hetzner worker slots with the owner's Claude subscription](2026-11-13-hetzner-claude-subscription-development.md)
supersedes the managed-first recommendation after the owner clarified existing VPS
capacity and subscription use. Retain this note as the earlier vendor comparison.

Research date: 2026-11-13. Owner constraint: compare managed and self-hosted options;
favor a small managed pilot; infrastructure budget $100/month, model use separate.

## Questions

1. Which services provide the control plane, isolated agent workspace, preview application,
   and database branch, and which parts still need building?
2. Can three concurrent implementations fit a $100/month infrastructure ceiling when
   human review does not retain idle agent compute?
3. What does a prebuild or snapshot preserve, how is application readiness measured, and
   how do migrations, sanitized data, test services, cleanup and retries work?
4. Which choices support self-hosting, and what licensing or paid-plan restrictions apply?
5. Which boundaries isolate untrusted task code, and what access is needed to test a preview?

## Recommendation

Use **Vercel Sandbox for task compute, Vercel Pro for previews, Neon for isolated dev
database branches, and a small Cloudflare Worker/Durable Object controller** for the
managed pilot. Keep GitHub Projects as the human interface. This is a proposed
integration of existing services, not a turnkey product. Model usage, existing production
hosting, taxes and engineering time are outside the $100 pilot infrastructure allowance.

An always-available webhook endpoint does not require an always-running agent VM.
The controller can sleep between events; task workers run only while doing work.
Stop workers at human review while keeping the preview and its database available
with expiry. Three concurrent tasks is a ceiling, not three workspaces running all month.

## Managed and self-hosted comparison

Prices checked 2026-11-13, USD before tax; verify account/region terms before purchase.

| Option | Evidence and limitations | Fit for this pilot |
|---|---|---|
| **Vercel Sandbox + Pro previews** | Firecracker microVM per sandbox; filesystem snapshots/persistence; Pro sessions up to 24 hours. Pro platform fee $20 includes one deploying seat and $20 shared usage credit. Memory is billed while provisioned; CPU only while active. [V1–V5] | Preferred for the assumed Next.js stack because previews and sandbox billing share an existing platform. Still needs controller, browser/data setup and trusted release gate |
| **Daytona managed** | Starter has no platform fee; listed compute is $0.0706/core-hour and $0.0113/GiB-hour. A documented core corresponds to two SMT vCPUs. Stopped/paused sandboxes do not incur CPU/RAM charges. [D1] | Strong alternative; compare actual startup, CPU billing and pause/resume behavior in the spike. Do not assume its isolation boundary is identical to Firecracker from pricing alone |
| **E2B** | Hobby has a one-hour session limit and ten concurrent sandboxes; Pro is $150/month before usage, with 24-hour sessions. One-time trial credit is not recurring budget. [E1] | Hobby can support checkpointed short jobs; Pro alone exceeds the budget. Not the default for multi-hour implementation sessions |
| **Coder** | Workspace management around provisioned infrastructure. Its automatically maintained pool of prebuilt workspaces requires Premium. Pricing extraction does not establish a usable Premium quote. [C1, C2] | Consider when self-hosting, developer workspace governance and remote human IDE access justify operating it. Free Coder does not make compute or the Premium prebuild pool free |
| **DevPod + cloud VMs** | Open-source client creates devcontainer environments across providers; supports prebuilds/inactivity shutdown and has no required always-on DevPod server. [DP1] | Lighter self-hosted route. Useful environment definition; still need board orchestration. A container on a shared host is not a separate kernel boundary |
| **Own controller + per-task DigitalOcean VMs** | Basic 2-vCPU/4-GiB VM is $24/month capped, or $0.03571/hour; three continuously allocated VMs are $72 before controller/storage/backups/preview retention. [DO1] | Can fit raw compute under $100, especially on demand. Operator owns images, patching, isolation, networking, snapshots, cleanup and recovery. More work than the managed pilot |

**Inference:** Coder is valuable when managing a fleet of developer environments is
itself a requirement. For one project and a $100 pilot, an API-provisioned sandbox is
the smaller starting point. Reconsider if managed compute grows expensive, projects
need private networking or persistent IDE sessions, or data policy requires own-cloud
execution. DevPod is a candidate for that transition, not a complete replacement for
the board controller.

## Budget with explicit workload assumptions

Reserve the following amounts rather than treating provider free tiers as unlimited:

| Monthly allocation | Ceiling used in planning | What is included |
|---|---:|---|
| Vercel | $45 | One Pro seat, sandbox CPU/RAM/snapshots and modest preview build/runtime usage |
| Cloudflare | $10 | $5 Workers base plus allowance for Durable Object and R2 usage |
| Neon | $15 | Small sanitized root, branches, active DB compute and retention |
| GitHub | $10 | One Team seat if needed for private-repo rules, plus a small CI allowance |
| Unallocated contingency | $20 | Storage/egress variability and unexpected runs |
| **Total** | **$100** | Model calls and current production hosting excluded |

The allocations are operating targets, not provider-enforced universal spending caps.
Vercel Pro's $20 credit is shared across usage products: it cannot be counted once for
Sandbox and again for previews. GitHub Team is listed at $4/user/month; extra seats
reduce this budget. Cloudflare Workers Paid starts at $5/month. R2 Standard storage is
$0.015/GB-month with operation charges and included allowances. [V2, CF1, CF4, GH1]

Example using Vercel's default `iad1` Sandbox rates, **120 total sandbox-hours/month**,
2 vCPU and 4 GB per workspace, averaging 25% active CPU across both cores:

```text
CPU        120 × 2 × 25% × $0.128  = $7.68
RAM        120 × 4 × $0.0212       = $10.176
Snapshots  5 GB-month × $0.08      = $0.40
Sandbox subtotal                  = $18.256
Illustrative preview usage        = $10.00
Pro invoice = $20 + max(0, $28.256 - $20 shared credit)
                                  = $28.256, before other charges
```

120 hours could mean 60 two-hour tasks, but must include retries, browser review,
scoping compute and dream experiments, not just the first implementation attempt.
At full active CPU, that sandbox subtotal rises to $41.296; with the same preview usage
the illustrative Vercel invoice becomes $51.296. Concurrency is not a cost model.
Three 4-GB workers running 24/7 for a 30-day month cost about **$321.41** in CPU/RAM
at the same 25% CPU assumption, before other services. [V1]

Neon Launch currently has no minimum monthly fee, $0.106/CU-hour compute and
$0.35/GB-month data storage. Three 0.25-CU branches each active for 40 hours would
consume 30 CU-hours, or $3.18 compute, before root compute, data and extras. Branch
count and active compute time both matter; persistent connections can keep a branch
awake. Use scale-to-zero, bounded compute, a small seed and branch expiry. [N1, N2]

Operational proposal: stop admitting work at $75 projected month-to-date committed
cost, preserve $25 for active tasks/cleanup, and require an explicit budget revision
before resuming. Track reserved task-hours and provider usage because invoices lag.
Limit retry rounds, wall time, model spend separately, artifact size and retained
previews. Stop admission when more than six tasks await human review; the user can
change that pilot threshold. Billing alerts alone do not guarantee a hard $100 cap.

## Fast, isolated application readiness

Prebuild a versioned base snapshot with the runtime, pinned dependencies, browser
binaries and OS packages. Key it by lockfile, toolchain, browser version and base-image
revision. Do not bake production access or task-specific tokens into that snapshot.
On task assignment, create a microVM from it, check out the exact task revision,
apply dependency differences, provision a DB branch, migrate, create fixture accounts,
start required services, then verify health **and an authenticated critical page**.

Vercel snapshots preserve filesystem state, not a running application's memory.
Resuming starts a new VM session; services must restart. Snapshotting a running sandbox
stops its session. Uncached restores can be slower, and snapshots are region-specific.
Keep one clean base and bounded task checkpoints; deleting a sandbox does not by
itself delete all its snapshots. Automatic resume also means a careless SDK call can
restart a worker after review: the controller must check state before accessing it.
[V3, V4]

**Proposed measured targets, not vendor promises:** p50 under 60 seconds and p95 under
120 seconds from lease to usable authenticated app for a cached base; cold cache under
five minutes. Measure image restore, dependency work, DB wake/branch/migration and app
startup separately over 20 starts, including simultaneous starts and invalidated caches.
Use 2 vCPU/4 GB initially, and measure whether build plus Chromium fits; do not run
several browsers/builds concurrently inside each of the three workers by default.

A Neon branch is copy-on-write and isolated from its parent, but by default it contains
the parent's data. **Branching is not sanitization.** Maintain a dedicated synthetic or
sanitized development root, optionally schema-only plus fixtures. Derive each task's
branch from that root and preserve the seed version. Keep object storage prefixes,
cache/queue namespaces, external-service test tenants and browser accounts isolated
too; DB branches alone are insufficient. Reset data between tests without altering
another task or the human review preview. [N1]

Each worker gets its own microVM filesystem/process/network environment, task-scoped
access and database role. Vercel allows outbound traffic by default and exposed ports
need application access protection; isolation does not automatically set the desired
network policy. Restrict egress and expose only authenticated dev endpoints. Keep the
GitHub App, provider provisioning and production deployment authority in the controller,
outside the code-writing worker. Shared physical hardware remains a vendor trust
boundary; "totally isolated" should mean explicit logical/kernel/data boundaries,
not an unsupported physical-isolation guarantee. [V5]

## Sources and verification limits

Pricing, introductory pages, Vercel security and Neon branching were read; longer
reference documents were checked at the named sections. No provider account was
provisioned and no startup, isolation or billing claim was benchmarked. Documentation
rates support the estimates; the workload assumptions are ours. Living docs checked
2026-11-13. Several extractors assign placeholder publication dates, including Daytona's
2002 date and January 1 dates; do not treat those as release dates.

| Key | Publisher and source | Saved article under `refs/articles/`; locator |
|---|---|---|
| V1 | Vercel, [Sandbox pricing](https://vercel.com/docs/sandbox/pricing) | `vercel.com/docs-sandbox-pricing/article.md`; regional rates, Pro credit, runtime limits |
| V2 | Vercel, [Pro plan](https://vercel.com/docs/plans/pro-plan) | `vercel.com/docs-plans-pro-plan/article.md`; platform fee, seats, shared credit |
| V3 | Vercel, [persistence](https://vercel.com/docs/sandbox/concepts/persistent-sandboxes) | `vercel.com/docs-sandbox-concepts-persistent-sandboxes/article.md`; lifecycle, auto-resume and retention |
| V4 | Vercel, [snapshots](https://vercel.com/docs/sandbox/concepts/snapshots) | `vercel.com/docs-sandbox-concepts-snapshots/article.md`; restore, regions, deletion |
| V5 | Vercel, [security](https://vercel.com/docs/sandbox/concepts/security) | `vercel.com/docs-sandbox-concepts-security/article.md`; microVM and network boundaries |
| D1 | Daytona, [pricing](https://www.daytona.com/pricing) | `daytona.com/pricing/article.md`; Starter and compute rates |
| E1 | E2B, [pricing](https://e2b.dev/pricing) | `e2b.dev/pricing/article.md`; Hobby/Pro limits |
| C1 | Coder, [pricing](https://coder.com/pricing) | `coder.com/pricing/article.md`; extraction incomplete, no Premium price assumed |
| C2 | Coder, [prebuilt workspaces](https://coder.com/docs/admin/templates/extending-templates/prebuilt-workspaces/) | `coder.com/docs-admin-templates-extending-templates-prebuilt-workspaces/article.md`; Prerequisites: Premium |
| DP1 | DevPod maintainers, [what is DevPod](https://devpod.sh/docs/what-is-devpod) | `devpod.sh/docs-what-is-devpod/article.md`; client/provider model |
| DO1 | DigitalOcean, [Droplets pricing](https://www.digitalocean.com/pricing/droplets) | `digitalocean.com/pricing-droplets/article.md`; Basic table; quote is compute only |
| N1 | Neon, [branching](https://neon.com/docs/introduction/branching) | `neon.com/docs-introduction-branching/article.md`; copy-on-write, data and expiry |
| N2 | Neon, [plans](https://neon.com/docs/introduction/plans) | `neon.com/docs-introduction-plans/article.md`; plan overview, price, compute and extra branches |
| CF1 | Cloudflare, [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) | `developers.cloudflare.com/workers-platform-pricing/article.md`; paid base and DO usage |
| CF2 | Cloudflare, [SQLite storage](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/) | `developers.cloudflare.com/durable-objects-api-sqlite-storage-api/article.md`; transactionSync; also checked via Context7 |
| CF3 | Cloudflare, [alarms](https://developers.cloudflare.com/durable-objects/api/alarms/) | `developers.cloudflare.com/durable-objects-api-alarms/article.md`; at-least-once execution and retry limit |
| CF4 | Cloudflare, [R2 pricing](https://developers.cloudflare.com/r2/pricing/) | `developers.cloudflare.com/r2-pricing/article.md`; Standard storage and operations |
| GH1 | GitHub, [pricing](https://github.com/pricing) | `github.com/pricing/article.md`; Team and included Actions usage |

The initially fetched `vercel.com/docs-sandbox-concepts-persistence/article.md` contains
navigation rather than the intended content. It is retained as fetched but excluded
from evidence; V3 is the working source. See the [board design](2026-11-13-github-agent-development-system.md)
for queue recovery, approvals and task-state ownership.
