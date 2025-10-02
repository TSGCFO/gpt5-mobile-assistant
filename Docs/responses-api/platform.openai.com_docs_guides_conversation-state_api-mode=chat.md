---
url: "https://platform.openai.com/docs/guides/conversation-state?api-mode=chat"
title: "Conversation state - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Conversation state

Learn how to manage conversation state during a model interaction.

Copy page

OpenAI provides a few ways to manage conversation state, which is important for preserving information across multiple messages or turns in a conversation.

## Manually manage conversation state

While each text generation request is independent and stateless, you can still implement **multi-turn conversations** by providing additional messages as parameters to your text generation request. Consider a knock-knock joke:

Manually construct a past conversation

python

```javascript
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
import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [\
        {\
            role: "user",\
            content: "knock knock.",\
        },\
        {\
            role: "assistant",\
            content: "Who's there?",\
        },\
        {\
            role: "user",\
            content: "Orange.",\
        },\
    ],
});

console.log(response.choices[0].message.content);
```

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
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[\
        {"role": "user", "content": "knock knock."},\
        {"role": "assistant", "content": "Who's there?"},\
        {"role": "user", "content": "Orange."},\
    ],
)

print(response.choices[0].message.content)
```

By using alternating `user` and `assistant` messages, you capture the previous state of a conversation in one request to the model.

To manually share context across generated responses, include the model's previous response output as input, and append that input to your next request.

In the following example, we ask the model to tell a joke, followed by a request for another joke. Appending previous responses to new requests in this way helps ensure conversations feel natural and retain the context of previous interactions.

Manually manage conversation state with the Chat Completions API.

python

```javascript
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
import OpenAI from "openai";

const openai = new OpenAI();

let history = [\
    {\
        role: "user",\
        content: "tell me a joke",\
    },\
];

const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: history,
});

console.log(completion.choices[0].message.content);

history.push(completion.choices[0].message);
history.push({
    role: "user",
    content: "tell me another",
});

const secondCompletion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: history,
});

console.log(secondCompletion.choices[0].message.content);
```

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
from openai import OpenAI

client = OpenAI()

history = [\
    {\
        "role": "user",\
        "content": "tell me a joke"\
    }\
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=history,
)

print(response.choices[0].message.content)

history.append(response.choices[0].message)
history.append({ "role": "user", "content": "tell me another" })

second_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=history,
)

print(second_response.choices[0].message.content)
```

## OpenAI APIs for conversation state

Our APIs make it easier to manage conversation state automatically, so you don't have to do pass inputs manually with each turn of a conversation.

We recommend using the [Responses API](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses) instead. Because it's stateful, managing context across conversations is a simple parameter.

If you're using the Chat Completions endpoint, you'll need to either manually manage state, as documented above.

## Managing the context window

Understanding context windows will help you successfully create threaded conversations and manage state across model interactions.

The **context window** is the maximum number of tokens that can be used in a single request. This max tokens number includes input, output, and reasoning tokens. To learn your model's context window, see [model details](https://platform.openai.com/docs/models).

### Managing context for text generation

As your inputs become more complex, or you include more turns in a conversation, you'll need to consider both **output token** and **context window** limits. Model inputs and outputs are metered in [**tokens**](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them), which are parsed from inputs to analyze their content and intent and assembled to render logical outputs. Models have limits on token usage during the lifecycle of a text generation request.

- **Output tokens** are the tokens generated by a model in response to a prompt. Each model has different [limits for output tokens](https://platform.openai.com/docs/models). For example, `gpt-4o-2024-08-06` can generate a maximum of 16,384 output tokens.
- A **context window** describes the total tokens that can be used for both input and output tokens (and for some models, [reasoning tokens](https://platform.openai.com/docs/guides/reasoning)). Compare the [context window limits](https://platform.openai.com/docs/models) of our models. For example, `gpt-4o-2024-08-06` has a total context window of 128k tokens.

If you create a very large prompt—often by including extra context, data, or examples for the model—you run the risk of exceeding the allocated context window for a model, which might result in truncated outputs.

Use the [tokenizer tool](https://platform.openai.com/tokenizer), built with the [tiktoken library](https://github.com/openai/tiktoken), to see how many tokens are in a particular string of text.

For example, when making an API request to [Chat Completions](https://platform.openai.com/docs/api-reference/chat) with the [o1 model](https://platform.openai.com/docs/guides/reasoning), the following token counts will apply toward the context window total:

- Input tokens (inputs you include in the `messages` array with [Chat Completions](https://platform.openai.com/docs/api-reference/chat))
- Output tokens (tokens generated in response to your prompt)
- Reasoning tokens (used by the model to plan a response)

Tokens generated in excess of the context window limit may be truncated in API responses.

![context window visualization](https://cdn.openai.com/API/docs/images/context-window.png)

You can estimate the number of tokens your messages will use with the [tokenizer tool](https://platform.openai.com/tokenizer).

## Next steps

For more specific examples and use cases, visit the [OpenAI Cookbook](https://cookbook.openai.com/), or learn more about using the APIs to extend model capabilities:

- [Receive JSON responses with Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Extend the models with function calling](https://platform.openai.com/docs/guides/function-calling)
- [Enable streaming for real-time responses](https://platform.openai.com/docs/guides/streaming-responses)
- [Build a computer using agent](https://platform.openai.com/docs/guides/tools-computer-use)

Chat Completions