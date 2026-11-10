---
title: "Quickstart"
url: "https://platform.minimax.io/docs/m-plan/quickstart.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Subscribe to M Plan, get your M Plan API key, and test an API call.

## 1. Subscribe to M Plan

Go to [Plan Details](https://platform.minimax.io/console/plan), choose a tier, and complete payment.

> [!TIP]
>
> If you only use M Plan in MiniMax Code, sign in to MiniMax Code after completing step 1. You do not need to configure an M Plan API key.

## 2. Get your M Plan API key

After subscribing, find your M Plan API key in [Plan Details](https://platform.minimax.io/console/plan). You need this M Plan API key to use M Plan in AI tools such as Claude Code and Cursor.

Note:

* Your M Plan API key uses your included M Plan quota and Credits and is not interchangeable with a pay-as-you-go API Key.
* Keep your M Plan API key secure. Do not share it with others or commit it to a code repository. Use an environment variable or configuration file to store it.

## 3. Test an API call (optional)

For example, use the Anthropic SDK to quickly test MiniMax-M3.1-Flash.

**Install the SDK**

```bash Python theme={null}
pip install anthropic
```

```bash Node.js theme={null}
npm install @anthropic-ai/sdk
```

**Configure environment variables**

Replace `${YOUR_API_KEY}` with your M Plan API key:

```bash theme={null}
export ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic
export ANTHROPIC_API_KEY=${YOUR_API_KEY}
```

See [Configure environment variables](https://platform.minimax.io/docs/guides/quickstart-preparation.md#env-vars).

**Call the API**

```python Python theme={null}
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="MiniMax-M3.1-Flash",
    output_config={"effort": "max"},
    max_tokens=4096,
    system="You are a helpful assistant.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hi, how are you?"
                }
            ]
        }
    ]
)

for block in message.content:
    if block.type == "thinking":
        print(f"Thinking:\n{block.thinking}\n")
    elif block.type == "text":
        print(f"Text:\n{block.text}\n")
```

