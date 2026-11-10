---
title: "FAQ"
url: "https://platform.minimax.io/docs/m-plan/faq.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ

> Find answers to common questions about M Plan tiers, usage, M Plan API keys, and usage rules.

## Which M Plan tiers are available?

The available subscription tiers are **Go**, **Explore**, and **Build**.

| Tier | Intended usage | Usage quota relative to Go |
| :- | :- | :- |
| Go | Getting started | 1× |
| Explore | Everyday use | 3× |
| Build | Intensive use | 7.5× |

***

## Which models does M Plan include? How do I switch models?

All three tiers support the M3.1 Flash text model, the H3 Image model, and the speech model, along with web search and multimodal understanding. Explore and Build also support the H3 video model.

To switch models, enter the model ID in your API request or tool configuration.

***

## Do I need a separate subscription or M Plan API key to use MiniMax Code?

No. After subscribing to M Plan, sign in to [MiniMax Code](https://agent.minimax.io/download) to get your subscription benefits. No separate subscription or M Plan API key is needed. For other AI tools, use your M Plan API key or sign in with MiniMax where supported.

***

## Can I use my subscription in multiple tools at the same time?

Yes. You can use the same subscription in all supported tools, but usage is shared. Usage from all tools counts toward the same M Plan usage limits.

***

## Is annual billing cheaper?

Yes. With annual billing, you pay for 10 months and get 2 months free.

***

## Do text, speech, video, and image models have separate usage limits?

No. All models included in M Plan share the same weekly quota, which you can use however you need. Image and video models are subject only to the weekly window, not the 5-hour window; text, speech, and other models are also subject to the 5-hour window.

***

## Do different models use my quota at the same rate?

No. How much of your quota each request uses depends mainly on:

* **Model**: Models use your quota at different rates. Video generation uses more of your quota than text generation, so frequent video use can exhaust it faster.
* **Context length**: Longer conversations and more files or code in context mean more content to process in each request.
* **Task complexity**: Multi-step agent tasks send many requests in a row and call tools, so they use more of your quota than a single question and answer.
* **Reasoning effort**: Higher reasoning effort can increase response time and usage.

If you are reaching your usage limit quickly, use lower reasoning effort for simple tasks, start new sessions when appropriate, and include only the files the task needs.

***

## How can I check M Plan usage?

You can check M Plan usage in three ways:

**Method 1: Visit the usage page**

Visit the [usage page](https://platform.minimax.io/console/usage) to view your plan, usage limits, Credits, and usage history.

**Method 2: Use MiniMax CLI**

```bash theme={null}
mmx quota
```

**Method 3: Use the API endpoint**

```bash theme={null}
curl --location 'https://www.minimax.io/v1/token_plan/remains' \
--header 'Authorization: Bearer <M Plan API key>' \
--header 'Content-Type: application/json'
```

***

## How is usage reset?

M Plan usage is shown through the console usage bar and controlled by usage windows:

* **Image and video models**: Subject only to a weekly window, with no 5-hour window.
* **Text, speech, and other models**: Subject to a 5-hour window and a weekly window.
* **Subscription cycle**: Unused M Plan quota does not carry over to the next billing cycle.
* **Credits**: Valid for one year from the date of purchase. This validity period is not reset when usage windows reset.

Both windows start with your first use: the 5-hour window lasts 5 hours, and the weekly window lasts 7 days. When a window ends, your full usage quota becomes available again, and your next use starts a new window. The two windows reset independently, so a 5-hour reset does not reset your weekly usage.

***

## Does unused quota carry over?

No. Unused quota does not carry over to the next usage window or billing period.

***

## What happens when I reach my usage limit?

When you reach your 5-hour or weekly limit, you can:

* **Use Credits**: Your included M Plan quota is used first. Once you reach your limit, additional usage is deducted from your Credits by default, starting with the Credits that expire soonest. Credits apply only to the models and capabilities they support. You can also continue generating images with available Credits after reaching your weekly quota.
* **Upgrade to a higher tier**: In MiniMax Code, click **Upgrade** in **Settings > Usage & Models**, or go to [Plan Details](https://platform.minimax.io/console/plan) and click **Change plan** to choose a higher tier with higher usage limits.
* **Wait for the usage window to reset**: Image and video models are subject only to the weekly window; a 5-hour window reset does not reset their weekly usage. Text, speech, and other models are subject to 5-hour and weekly windows.
* **Switch to pay-as-you-go**: Replace the M Plan API key in your tool with a standard API Key. Actual resource usage is charged to your account balance.

***

## Will my account balance be charged when I reach my usage limit?

No. An M Plan API key uses your included M Plan quota and Credits. When you reach your usage limit, any remaining Credits are used next. Your account balance is charged only when you use a pay-as-you-go API Key.

***

## What are the limits of M Plan? Is it suitable for production?

M Plan is designed for individual, interactive developer use, with higher tiers offering higher usage limits. Pay-as-you-go is recommended for production use.

Key limits include:

* **Rate limits (RPM / TPM)**: Requests may be throttled when exceeded, typically recovering within about one minute. Limits may tighten during peak traffic.
* **Image and video model usage**: Subject only to a weekly window, with no 5-hour window.
* **Text, speech, and other model usage**: Subject to 5-hour and weekly windows.

***

## What are the platform traffic rules?

MiniMax may adjust request limits based on account usage and demand, including during peak hours, to keep the service available to all users.

***

## What is an M Plan API key?

An M Plan API key is used for M Plan subscriptions and Credits. Configure it in AI agents and coding tools to call available models and capabilities.

M Plan API keys are separate from standard pay-as-you-go API Keys and cannot be used interchangeably.

***

## Where do I get my M Plan API key?

After subscribing to M Plan, find your M Plan API key in [Plan Details](https://platform.minimax.io/console/plan). Keep it secure; do not share it or commit it to a code repository.

***

## Which tools can I use my M Plan API key with?

Any AI tool that supports the OpenAI-compatible or Anthropic-compatible protocol, such as Claude Code, Codex, Cursor, OpenCode, Hermes Agent, and OpenClaw. See each tool's guide for setup, or [Other tools](https://platform.minimax.io/docs/m-plan/other-tools.md) for general settings.

***

## Can the M Plan API key and the standard API Key be used interchangeably?

No.

* **M Plan API key**: Uses your included M Plan quota and Credits. API endpoints with pay-as-you-go pricing deduct from your included M Plan quota at the corresponding endpoint price. Credits can be used for the models and capabilities they support and can cover eligible overflow beyond subscription usage limits.
* **Standard API Key**: Uses pay-as-you-go billing for API Platform endpoints. Actual resource usage consumes your account balance.

***

## Why is my account balance still being charged after subscribing?

Usually because the tool is using a pay-as-you-go API Key. Pay-as-you-go API Keys charge your account balance and do not use your M Plan usage. Replace it with your [M Plan API key](https://platform.minimax.io/console/plan).

***

## Which models do Credits support?

Credits support text, video, image, and speech models, along with web search and multimodal understanding.

***

## How are Credits valued and charged?

Credits can be used for supported models and capabilities. You can use them on their own or after reaching your M Plan usage limit.

* Calls to models with pay-as-you-go pricing deduct the equivalent Credits amount at the model's API price.
* When both your included M Plan quota and Credits can cover a request, your included quota is used first, followed by Credits for the excess.
* **Validity**: Credits are valid for one year from the date of purchase.

***

## How long are Credits valid?

Credits are valid for one year from the date of purchase. Their validity is not reset when usage windows reset.

***

## Can I use Credits without an M Plan subscription?

Yes. Credits can be purchased separately and used without an M Plan subscription.

Note:

* If you also subscribe to M Plan, your included M Plan quota is used before your Credits.
* In MiniMax Code, Credits purchased on their own do not include M Plan subscription benefits, such as additional cloud projects, scheduled tasks, and website publishing limits, custom domains, and watermark removal.
* For resources outside M Plan coverage, use a pay-as-you-go API Key.

***

## How do I upgrade, and when does it take effect?

In [Plan Details](https://platform.minimax.io/console/plan), click **Change plan** and choose your target tier. The unused portion of your current subscription is prorated by the time remaining and applied toward the upgrade, so you only pay the difference. Once you complete payment, the upgrade takes effect immediately, and your subscription then renews at the new tier's price. See [Upgrades and cancellation](https://platform.minimax.io/docs/m-plan/change-plan.md).

***

## Can I downgrade?

Downgrades are not currently supported.

***

## Can I switch from monthly to annual billing?

A monthly subscription can be upgraded to a higher tier with monthly or annual billing. An annual subscription can be upgraded to a higher tier with annual billing.

***

## How do I turn off auto-renewal?

Turn off auto-renewal in [Plan Details](https://platform.minimax.io/console/plan). Your benefits remain available for the current paid period, and the subscription will not renew when it ends.

If you change your mind, you can turn auto-renewal back on in Plan Details before your subscription expires.

***

## What do I need to do as a Token Plan subscriber?

Nothing. Your current plan and benefits stay the same, and as long as auto-renewal stays on, your subscription renews at the original price with the same benefits. You can also upgrade to M Plan at any time, and the unused portion of your current subscription will be credited toward the cost. Learn more about [what changes for Token Plan subscribers](https://platform.minimax.io/docs/m-plan/token-plan-notice.md).

***

## How is TPS (Tokens Per Second) calculated for LLMs?

TPS measures the number of tokens generated per second, and is used to evaluate the inference output speed of a model. The formula is:

$$
\text{TPS} = \frac{\text{Number of output tokens}}{\text{Time of last token} - \text{Time of first token}}
$$

In other words, timing starts when the model outputs the first token and ends when the last token is generated. The total number of tokens produced is then divided by that elapsed time (in seconds).

> [!NOTE]
>
> TPS may fluctuate during actual usage. The TPS values indicated on each model page are reference values.

***

## Still getting 401 after login?

`mmx auth login` usually auto-detects the service region from your API Key. If you still get 401, region detection likely failed. Set it manually:

```bash theme={null}
mmx config set --key region --value global   # Global API Key
mmx config set --key region --value cn       # Mainland China API Key
```

Run `mmx auth status` to confirm the active region matches the platform your key comes from.

