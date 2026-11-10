---
title: "Usage"
url: "https://platform.minimax.io/docs/m-plan/usage-rules.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage

> Learn when your usage resets, how to check your usage, and what you can do when you reach your usage limit.

Whether you use MiniMax Code or other AI tools connected with your M Plan API key, it all counts toward the same M Plan usage limits.

## Usage resets

Usage resets automatically over two time windows. No manual action is needed, and you do not have to wait until your renewal date.

| | 5-hour window | Weekly window |
| :- | :- | :- |
| Applies to | All except image and video models | All models share the same weekly quota |
| Starts | With your first use | With your first use |
| Duration | 5 hours | 7 days |
| When it ends | Your full usage quota becomes available again; your next use starts a new window | Same as the 5-hour window |

* Image and video models are subject only to the weekly window; text, speech, and other models require remaining quota in both windows.
* The windows reset independently. A 5-hour reset does not reset your weekly usage.
* Each window resets when it ends, regardless of your usage during that window. For example, if your first use is at 10:00, that 5-hour window ends at 15:00; even if you reach your usage limit at 12:00, it resets at 15:00.
* Unused quota does not carry over to the next usage window or billing period.

## Check your usage

Your usage history helps you understand how you work and whether your current tier fits. On the [Plan usage](https://platform.minimax.io/console/usage) page, you can see your M Plan usage and detailed usage analytics.

> [!TIP]
>
> With [MiniMax CLI](https://platform.minimax.io/docs/m-plan/minimax-cli.md), run `mmx quota` to check your usage directly from the command line.

## When you reach your usage limit

* **Upgrade to a higher tier**: If you often reach your usage limit, you can upgrade to a higher tier. See [Upgrades and cancellation](https://platform.minimax.io/docs/m-plan/change-plan.md).
* **Wait for a reset**: When you reach your 5-hour or weekly limit, your usage resets automatically when that window ends.
* **Use purchased Credits**: For models and capabilities supported by Credits, the system uses your included M Plan quota first, then deducts any overage from your available Credits.
* **Use pay-as-you-go billing**: For resources outside your plan or for production workloads, use a regular pay-as-you-go API Key. Charges are deducted from your Open Platform account balance. This Key is separate from your M Plan API key and cannot be used interchangeably with it.

## Why am I rate-limited before reaching my usage limit?

Usage limits and request rate limits are separate. Sending too many requests in a short time, or encountering dynamic limits during peak hours, can temporarily block calls even before you reach your usage limit. Reduce your request frequency or concurrency and try again later. A rate limit does not mean you have reached your usage limit.

