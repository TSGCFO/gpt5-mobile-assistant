---
url: "https://platform.openai.com/docs/assistants/migration"
title: "Assistants migration guide - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Assistants migration guide

Migrate from the Assistants API to the Responses API.

Copy page

After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the guidance below to update your integration. [Learn more](https://platform.openai.com/docs/guides/responses-vs-chat-completions).

We're moving from the Assistants API to the new [Responses API](https://platform.openai.com/docs/guides/responses-vs-chat-completions) for a simpler and more flexible mental model.

Responses are simpler—send input items and get output items back. With the Responses API, you also get better performance and new features like [deep research](https://platform.openai.com/docs/guides/deep-research), [MCP](https://platform.openai.com/docs/guides/tools-remote-mcp), and [computer use](https://platform.openai.com/docs/guides/tools-computer-use). This change also lets you manage conversations instead of passing back `previous_response_id`.

### What's changed?

| Before | Now | Why? |
| --- | --- | --- |
| `Assistants` | `Prompts` | Prompts hold configuration (model, tools, instructions) and are easier to version and update |
| `Threads` | `Conversations` | Streams of items instead of just messages |
| `Runs` | `Responses` | Responses send input items or use a conversation object and receive output items; tool call loops are explicitly managed |
| `Run steps` | `Items` | Generalized objects—can be messages, tool calls, outputs, and more |

## From assistants to prompts

Assistants were persistent API objects that bundled model choice, instructions, and tool declarations—created and managed entirely through the API. Their replacement, prompts, can only be created in the dashboard, where you can version them as you develop your product.

### Why this is helpful

- **Portability and versioning**: You can snapshot, review, diff, and roll back prompt specs. You can also version a prompt, so your code can just point the latest version.
- **Separation of concerns**: Your application code now handles orchestration (history pruning, tool loop, retries) while your prompt focuses on high‑level behavior and constraints (system guidance, tool availability, structured output schema, temperature defaults).
- **Realtime compatibility**: The same prompt configuration can be reused when you connect through the Realtime API, giving you a single definition of behavior across chat, streaming, and low‑latency interactive sessions.
- **Tool and output consistency**: Using prompts, every Responses or Realtime session you start inherits a consistent contract because prompts encapsulate tool schemas and structured output expectations.

### Practical migration steps

1. Identify each existing Assistant’s _instruction + tool_ bundle.
2. In the dashboard, recreate that bundle as a named prompt.
3. Store the prompt ID (or its exported spec) in source control so application code can refer to a stable identifier.
4. During rollout, run A/B tests by swapping prompt IDs—no need to create or delete assistant objects programmatically.

Think of a prompt as a **versioned behavioral profile** to plug into either Responses or Realtime API.

* * *

## From threads to conversations

A thread was a collection of messages stored server-side. Threads could _only_ store messages. Conversations store items, which can include messages, tool calls, tool outputs, and other data.

### Request example

Thread object

```python
1
2
3
4
thread = openai.beta.threads.create(
  messages=[{"role": "user", "content": "what are the 5 Ds of dodgeball?"}],
  metadata={"user_id": "peter_le_fleur"},
)
```

Conversation object

```python
1
2
3
4
conversation = openai.conversations.create(
  items=[{"role": "user", "content": "what are the 5 Ds of dodgeball?"}],
  metadata={"user_id": "peter_le_fleur"},
)
```

### Response example

Thread object

```json
1
2
3
4
5
6
7
8
9
{
"id": "thread_CrXtCzcyEQbkAcXuNmVSKFs1",
"object": "thread",
"created_at": 1752855924,
"metadata": {
  "user_id": "peter_le_fleur"
},
"tool_resources": {}
}
```

Conversation object

```json
1
2
3
4
5
6
7
8
{
"id": "conv_68542dc602388199a30af27d040cefd4087a04b576bfeb24",
"object": "conversation",
"created_at": 1752855924,
"metadata": {
	"user_id": "peter_le_fleur"
}
}
```

* * *

## From runs to responses

Runs were asynchronous processes that executed against threads. See the example below. Responses are simpler: provide a set of input items to execute, and get a list of output items back.

Responses are designed to be used alone, but you can also use them with prompt and conversation objects for storing context and configuration.

### Request example

Run object

```python
1
2
3
4
5
6
7
8
thread_id = "thread_CrXtCzcyEQbkAcXuNmVSKFs1"
assistant_id = "asst_8fVY45hU3IM6creFkVi5MBKB"

run = openai.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant.id)

while run.status in ("queued", "in_progress"):
  time.sleep(1)
  run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
```

Response object

```python
1
2
3
4
5
response = openai.responses.create(
  model="gpt-4.1",
  input=[{"role": "user", "content": "What are the 5 Ds of dodgeball?"}]
  conversation: "conv_689667905b048191b4740501625afd940c7533ace33a2dab"
)
```

### Response example

Run object

```python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{
"id": "run_FKIpcs5ECSwuCmehBqsqkORj",
"assistant_id": "asst_8fVY45hU3IM6creFkVi5MBKB",
"cancelled_at": null,
"completed_at": 1752857327,
"created_at": 1752857322,
"expires_at": null,
"failed_at": null,
"incomplete_details": null,
"instructions": null,
"last_error": null,
"max_completion_tokens": null,
"max_prompt_tokens": null,
"metadata": {},
"model": "gpt-4.1",
"object": "thread.run",
"parallel_tool_calls": true,
"required_action": null,
"response_format": "auto",
"started_at": 1752857324,
"status": "completed",
"thread_id": "thread_CrXtCzcyEQbkAcXuNmVSKFs1",
"tool_choice": "auto",
"tools": [],
"truncation_strategy": {
  "type": "auto",
  "last_messages": null
},
"usage": {
  "completion_tokens": 130,
  "prompt_tokens": 34,
  "total_tokens": 164,
  "prompt_token_details": {
    "cached_tokens": 0
  },
  "completion_tokens_details": {
    "reasoning_tokens": 0
  }
},
"temperature": 1.0,
"top_p": 1.0,
"tool_resources": {},
"reasoning_effort": null
}
```

Response object

```python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
{
"id": "resp_687a7b53036c819baad6012d58b39bcb074adcd9e24850fc",
"created_at": 1752857427,
"conversation": {
  "id": "conv_689667905b048191b4740501625afd940c7533ace33a2dab"
},
"error": null,
"incomplete_details": null,
"instructions": null,
"metadata": {},
"model": "gpt-4.1-2025-04-14",
"object": "response",
"output": [\
  {\
    "id": "msg_687a7b542948819ba79e77e14791ef83074adcd9e24850fc",\
    "content": [\
      {\
        "annotations": [],\
        "text": "The \"5 Ds of Dodgeball\" are a humorous set of rules made famous by the 2004 comedy film **\"Dodgeball: A True Underdog Story.\"** In the movie, dodgeball coach Patches O’Houlihan teaches these basics to his team. The **5 Ds** are:\
\
1. **Dodge**\
2. **Duck**\
3. **Dip**\
4. **Dive**\
5. **Dodge** (yes, dodge is listed twice for emphasis!)\
\
In summary:\
> **“If you can dodge a wrench, you can dodge a ball!”**\
\
These 5 Ds are not official competitive rules, but have become a fun and memorable pop culture reference for the sport of dodgeball.",\
        "type": "output_text",\
        "logprobs": []\
      }\
    ],\
    "role": "assistant",\
    "status": "completed",\
    "type": "message"\
  }\
],
"parallel_tool_calls": true,
"temperature": 1.0,
"tool_choice": "auto",
"tools": [],
"top_p": 1.0,
"background": false,
"max_output_tokens": null,
"previous_response_id": null,
"reasoning": {
  "effort": null,
  "generate_summary": null,
  "summary": null
},
"service_tier": "scale",
"status": "completed",
"text": {
  "format": {
    "type": "text"
  }
},
"truncation": "disabled",
"usage": {
  "input_tokens": 17,
  "input_tokens_details": {
    "cached_tokens": 0
  },
  "output_tokens": 150,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 167
},
"user": null,
"max_tool_calls": null,
"store": true,
"top_logprobs": 0
}
```

* * *

## Migrating your integration

Follow the migration steps below to move from the Assistants API to the Responses API, without losing any feature support.

### 1\. Create prompts from your assistants

1. Identify the most important assistant objects in your application.
2. Find these in the dashboard and click `Create prompt`.

This will create a prompt object out of each existing assistant object.

### 2\. Move new user chats over to conversations and responses

We will not provide an automated tool for migrating Threads to Conversations. Instead, we recommend migrating new user threads onto conversations and backfilling old ones as necessary.

Here's an example for how you might backfill a thread:

```python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
thread_id = "thread_EIpHrTAVe0OzoLQg3TXfvrkG"

for page in openai.beta.threads.messages.list(thread_id=thread_id, order="asc").iter_pages():
    messages += page.data

items = []
for m in messages:
    item = {"role": m.role}
    item_content = []

    for content in m.content:
        match content.type:
            case "text":
                item_content_type = "input_text" if m.role == "user" else "output_text"
                item_content += [{"type": item_content_type, "text": content.text.value}]
            case "image_url":
                item_content + [\
                    {\
                        "type": "input_image",\
                        "image_url": content.image_url.url,\
                        "detail": content.image_url.detail,\
                    }\
                ]

    item |= {"content": item_content}
    items.append(item)

# create a conversation with your converted items
conversation = openai.conversations.create(items=items)
```

## Comparing full examples

Here’s a few simple examples of integrations using both the Assistants API and the Responses API so you can see how they compare.

### User chat app

Assistants APIResponses API

Assistants API

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
thread = openai.threads.create()

@app.post("/messages")
async def message(message: Message):
openai.beta.threads.messages.create(
	role="user",
	content=message.content
)

run = openai.beta.threads.runs.create(
	assistant_id=os.getenv("ASSISTANT_ID"),
	thread_id=thread.id
)
while run.status in ("queued", "in_progress"):
  await asyncio.sleep(1)
  run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

messages = openai.beta.threads.messages.list(
	order="desc", limit=1, thread_id=thread.id
)

return { "content": messages[-1].content }
```

Responses API

```json
1
2
3
4
5
6
7
8
9
10
conversation = openai.conversations.create()

@app.post("/messages")
async def message(message: Message):
response = openai.responses.create(
	prompt={ "id": os.getenv("PROMPT_ID") },
	input=[{ "role": "user", "content": message.content }]
)

return { "content": response.output_text }'
```