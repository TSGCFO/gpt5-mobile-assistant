---
url: "https://platform.openai.com/docs/guides/predicted-outputs"
title: "Predicted Outputs - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Predicted Outputs

Reduce latency for model responses where much of the response is known ahead of time.

Copy page

**Predicted Outputs** enable you to speed up API responses from [Chat Completions](https://platform.openai.com/docs/api-reference/chat/create) when many of the output tokens are known ahead of time. This is most common when you are regenerating a text or code file with minor modifications. You can provide your prediction using the [`prediction` request parameter in Chat Completions](https://platform.openai.com/docs/api-reference/chat/create#chat-create-prediction).

Predicted Outputs are available today using the latest `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, and `gpt-4.1-nano` models. Read on to learn how to use Predicted Outputs to reduce latency in your applications.

## Code refactoring example

Predicted Outputs are particularly useful for regenerating text documents and code files with small modifications. Let's say you want the [GPT-4o model](https://platform.openai.com/docs/models#gpt-4o) to refactor a piece of TypeScript code, and convert the `username` property of the `User` class to be `email` instead:

```typescript
1
2
3
4
5
6
7
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
```

Most of the file will be unchanged, except for line 4 above. If you use the current text of the code file as your prediction, you can regenerate the entire file with lower latency. These time savings add up quickly for larger files.

Below is an example of using the `prediction` parameter in our SDKs to predict that the final output of the model will be very similar to our original code file, which we use as the prediction text.

Refactor a TypeScript class with a Predicted Output

javascript

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
import OpenAI from "openai";

const code = `
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
`.trim();

const openai = new OpenAI();

const refactorPrompt = `
Replace the "username" property with an "email" property. Respond only
with code, and with no markdown formatting.
`;

const completion = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages: [\
    {\
      role: "user",\
      content: refactorPrompt\
    },\
    {\
      role: "user",\
      content: code\
    }\
  ],
  store: true,
  prediction: {
    type: "content",
    content: code
  }
});

// Inspect returned data
console.log(completion);
console.log(completion.choices[0].message.content);
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
from openai import OpenAI

code = """
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
"""

refactor_prompt = """
Replace the "username" property with an "email" property. Respond only
with code, and with no markdown formatting.
"""

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[\
        {\
            "role": "user",\
            "content": refactor_prompt\
        },\
        {\
            "role": "user",\
            "content": code\
        }\
    ],
    prediction={
        "type": "content",
        "content": code
    }
)

print(completion)
print(completion.choices[0].message.content)
```

```bash
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
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "messages": [\
      {\
        "role": "user",\
        "content": "Replace the username property with an email property. Respond only with code, and with no markdown formatting."\
      },\
      {\
        "role": "user",\
        "content": "$CODE_CONTENT_HERE"\
      }\
    ],
    "prediction": {
        "type": "content",
        "content": "$CODE_CONTENT_HERE"
    }
  }'
```

In addition to the refactored code, the model response will contain data that looks something like this:

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
{
  id: 'chatcmpl-xxx',
  object: 'chat.completion',
  created: 1730918466,
  model: 'gpt-4o-2024-08-06',
  choices: [ /* ...actual text response here... */],
  usage: {
    prompt_tokens: 81,
    completion_tokens: 39,
    total_tokens: 120,
    prompt_tokens_details: { cached_tokens: 0, audio_tokens: 0 },
    completion_tokens_details: {
      reasoning_tokens: 0,
      audio_tokens: 0,
      accepted_prediction_tokens: 18,
      rejected_prediction_tokens: 10
    }
  },
  system_fingerprint: 'fp_159d8341cc'
}
```

Note both the `accepted_prediction_tokens` and `rejected_prediction_tokens` in the `usage` object. In this example, 18 tokens from the prediction were used to speed up the response, while 10 were rejected.

Note that any rejected tokens are still billed like other completion tokens generated by the API, so Predicted Outputs can introduce higher costs for your requests.

## Streaming example

The latency gains of Predicted Outputs are even greater when you use streaming for API responses. Here is an example of the same code refactoring use case, but using streaming in the OpenAI SDKs instead.

Predicted Outputs with streaming

javascript

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
import OpenAI from "openai";

const code = `
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
`.trim();

const openai = new OpenAI();

const refactorPrompt = `
Replace the "username" property with an "email" property. Respond only
with code, and with no markdown formatting.
`;

const completion = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages: [\
    {\
      role: "user",\
      content: refactorPrompt\
    },\
    {\
      role: "user",\
      content: code\
    }\
  ],
  store: true,
  prediction: {
    type: "content",
    content: code
  },
  stream: true
});

// Inspect returned data
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
from openai import OpenAI

code = """
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
"""

refactor_prompt = """
Replace the "username" property with an "email" property. Respond only
with code, and with no markdown formatting.
"""

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4.1",
    messages=[\
        {\
            "role": "user",\
            "content": refactor_prompt\
        },\
        {\
            "role": "user",\
            "content": code\
        }\
    ],
    prediction={
        "type": "content",
        "content": code
    },
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Position of predicted text in response

When providing prediction text, your prediction can appear anywhere within the generated response, and still provide latency reduction for the response. Let's say your predicted text is the simple [Hono](https://hono.dev/) server shown below:

```typescript
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
import { serveStatic } from "@hono/node-server/serve-static";
import { serve } from "@hono/node-server";
import { Hono } from "hono";

const app = new Hono();

app.get("/api", (c) => {
  return c.text("Hello Hono!");
});

// You will need to build the client code first `pnpm run ui:build`
app.use(
  "/*",
  serveStatic({
    rewriteRequestPath: (path) => `./dist${path}`,
  })
);

const port = 3000;
console.log(`Server is running on port ${port}`);

serve({
  fetch: app.fetch,
  port,
});
```

You could prompt the model to regenerate the file with a prompt like:

```text
1
2
3
4
Add a get route to this application that responds with
the text "hello world". Generate the entire application
file again with this route added, and with no other
markdown formatting.
```

The response to the prompt might look something like this:

```typescript
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
import { serveStatic } from "@hono/node-server/serve-static";
import { serve } from "@hono/node-server";
import { Hono } from "hono";

const app = new Hono();

app.get("/api", (c) => {
  return c.text("Hello Hono!");
});

app.get("/hello", (c) => {
  return c.text("hello world");
});

// You will need to build the client code first `pnpm run ui:build`
app.use(
  "/*",
  serveStatic({
    rewriteRequestPath: (path) => `./dist${path}`,
  })
);

const port = 3000;
console.log(`Server is running on port ${port}`);

serve({
  fetch: app.fetch,
  port,
});
```

You would still see accepted prediction tokens in the response, even though the prediction text appeared both before and after the new content added to the response:

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
{
  id: 'chatcmpl-xxx',
  object: 'chat.completion',
  created: 1731014771,
  model: 'gpt-4o-2024-08-06',
  choices: [ /* completion here... */],
  usage: {
    prompt_tokens: 203,
    completion_tokens: 159,
    total_tokens: 362,
    prompt_tokens_details: { cached_tokens: 0, audio_tokens: 0 },
    completion_tokens_details: {
      reasoning_tokens: 0,
      audio_tokens: 0,
      accepted_prediction_tokens: 60,
      rejected_prediction_tokens: 0
    }
  },
  system_fingerprint: 'fp_9ee9e968ea'
}
```

This time, there were no rejected prediction tokens, because the entire content of the file we predicted was used in the final response. Nice! 🔥

## Limitations

When using Predicted Outputs, you should consider the following factors and limitations.

- Predicted Outputs are only supported with the GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, and GPT-4.1-nano series of models.
- When providing a prediction, any tokens provided that are not part of the final completion are still charged at completion token rates. See the [`rejected_prediction_tokens` property of the `usage` object](https://platform.openai.com/docs/api-reference/chat/object#chat/object-usage) to see how many tokens are not used in the final response.
- The following [API parameters](https://platform.openai.com/docs/api-reference/chat/create) are not supported when using Predicted Outputs:

  - `n`: values higher than 1 are not supported
  - `logprobs`: not supported
  - `presence_penalty`: values greater than 0 are not supported
  - `frequency_penalty`: values greater than 0 are not supported
  - `audio`: Predicted Outputs are not compatible with [audio inputs and outputs](https://platform.openai.com/docs/guides/audio)
  - `modalities`: Only `text` modalities are supported
  - `max_completion_tokens`: not supported
  - `tools`: Function calling is not currently supported with Predicted Outputs

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all