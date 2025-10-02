---
url: "https://platform.openai.com/docs/guides/completions"
title: "Completions API - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Completions API  Legacy

Copy page

The completions API endpoint received its final update in July 2023 and has a different interface than the new Chat Completions endpoint. Instead of the input being a list of messages, the input is a freeform text string called a `prompt`.

An example legacy Completions API call looks like the following:

python

```python
1
2
3
4
5
6
7
from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop."
)
```

```javascript
1
2
3
4
const completion = await openai.completions.create({
    model: 'gpt-3.5-turbo-instruct',
    prompt: 'Write a tagline for an ice cream shop.'
});
```

See the full [API reference documentation](https://platform.openai.com/docs/api-reference/completions) to learn more.

#### Inserting text

The completions endpoint also supports inserting text by providing a [suffix](https://platform.openai.com/docs/api-reference/completions/create#completions-create-suffix) in addition to the standard prompt which is treated as a prefix. This need naturally arises when writing long-form text, transitioning between paragraphs, following an outline, or guiding the model towards an ending. This also works on code, and can be used to insert in the middle of a function or file.

Deep dive

Inserting text

### Completions response format

An example completions API response looks as follows:

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
{
  "choices": [\
    {\
      "finish_reason": "length",\
      "index": 0,\
      "logprobs": null,\
      "text": "\n\n\"Let Your Sweet Tooth Run Wild at Our Creamy Ice Cream Shack"\
    }\
  ],
  "created": 1683130927,
  "id": "cmpl-7C9Wxi9Du4j1lQjdjhxBlO22M61LD",
  "model": "gpt-3.5-turbo-instruct",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 16,
    "prompt_tokens": 10,
    "total_tokens": 26
  }
}
```

In Python, the output can be extracted with `response['choices'][0]['text']`.

The response format is similar to the response format of the Chat Completions API.

### Inserting text

The completions endpoint also supports inserting text by providing a [suffix](https://platform.openai.com/docs/api-reference/completions/create#completions-create-suffix) in addition to the standard prompt which is treated as a prefix. This need naturally arises when writing long-form text, transitioning between paragraphs, following an outline, or guiding the model towards an ending. This also works on code, and can be used to insert in the middle of a function or file.

Deep dive

Inserting text

## Chat Completions vs. Completions

The Chat Completions format can be made similar to the completions format by constructing a request using a single user message. For example, one can translate from English to French with the following completions prompt:

```text
Translate the following English text to French: "{text}"
```

And an equivalent chat prompt would be:

```text
[{"role": "user", "content": 'Translate the following English text to French: "{text}"'}]
```

Likewise, the completions API can be used to simulate a chat between a user and an assistant by formatting the input [accordingly](https://platform.openai.com/playground/p/default-chat?model=gpt-3.5-turbo-instruct).

The difference between these APIs is the underlying models that are available in each. The Chat Completions API is the interface to our most capable model ( `gpt-4o`), and our most cost effective model ( `gpt-4o-mini`).

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all