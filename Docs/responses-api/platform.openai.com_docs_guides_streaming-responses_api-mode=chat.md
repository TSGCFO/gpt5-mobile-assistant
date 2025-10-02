---
url: "https://platform.openai.com/docs/guides/streaming-responses?api-mode=chat"
title: "Streaming API responses - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Streaming API responses

Learn how to stream model responses from the OpenAI API using server-sent events.

Copy page

By default, when you make a request to the OpenAI API, we generate the model's entire output before sending it back in a single HTTP response. When generating long outputs, waiting for a response can take time. Streaming responses lets you start printing or processing the beginning of the model's output while it continues generating the full response.

## Enable streaming

Streaming Chat Completions is fairly straightforward. However, we recommend using the [Responses API for streaming](https://platform.openai.com/docs/guides/streaming-responses?api-mode=responses), as we designed it with streaming in mind. The Responses API uses semantic events for streaming and is type-safe.

### Stream a chat completion

To stream completions, set `stream=True` when calling the Chat Completions or legacy Completions endpoints. This returns an object that streams back the response as data-only server-sent events.

The response is sent back incrementally in chunks with an event stream. You can iterate over the event stream with a `for` loop, like this:

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
import OpenAI from "openai";
const openai = new OpenAI();

const stream = await openai.chat.completions.create({
    model: "gpt-5",
    messages: [\
        {\
            role: "user",\
            content: "Say 'double bubble bath' ten times fast." ,\
        }\
    ],
    stream: true,
});

for await (const chunk of stream) {
    console.log(chunk);
    console.log(chunk.choices[0].delta);
    console.log("****************");
}
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
from openai import OpenAI
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-5",
    messages=[\
        {\
            "role": "user",\
            "content": "Say 'double bubble bath' ten times fast.",\
        },\
    ],
    stream=True,
)

for chunk in stream:
    print(chunk)
    print(chunk.choices[0].delta)
    print("****************")
```

## Read the responses

When you stream a chat completion, the responses has a `delta` field rather than a `message` field. The `delta` field can hold a role token, content token, or nothing.

```text
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
{ role: 'assistant', content: '', refusal: null }
****************
{ content: 'Why' }
****************
{ content: " don't" }
****************
{ content: ' scientists' }
****************
{ content: ' trust' }
****************
{ content: ' atoms' }
****************
{ content: '?\n\n' }
****************
{ content: 'Because' }
****************
{ content: ' they' }
****************
{ content: ' make' }
****************
{ content: ' up' }
****************
{ content: ' everything' }
****************
{ content: '!' }
****************
{}
****************
```

To stream only the text response of your chat completion, your code would like this:

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
import OpenAI from "openai";
const client = new OpenAI();

const stream = await client.chat.completions.create({
    model: "gpt-5",
    messages: [\
        {\
            role: "user",\
            content: "Say 'double bubble bath' ten times fast.",\
        },\
    ],
    stream: true,
});

for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
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
from openai import OpenAI
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-5",
    messages=[\
        {\
            "role": "user",\
            "content": "Say 'double bubble bath' ten times fast.",\
        },\
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Advanced use cases

For more advanced use cases, like streaming tool calls, check out the following dedicated guides:

- [Streaming function calls](https://platform.openai.com/docs/guides/function-calling#streaming)
- [Streaming structured output](https://platform.openai.com/docs/guides/structured-outputs#streaming)

## Moderation risk

Note that streaming the model's output in a production application makes it more difficult to moderate the content of the completions, as partial completions may be more difficult to evaluate. This may have implications for approved usage.

Chat Completions