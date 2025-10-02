---
url: "https://platform.openai.com/docs/overview?lang=python"
title: "Overview - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# OpenAI developer platform

[Developer quickstart\\
\\
Make your first API request in minutes. Learn the basics of the OpenAI platform.\\
\\
5 min](https://platform.openai.com/docs/quickstart)

python

```bash
1
2
3
4
5
6
7
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5",
    "input": "Write a short bedtime story about a unicorn."
  }'
```

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
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5",
  input: "Write a short bedtime story about a unicorn.",
});

console.log(response.output_text);
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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)
```

```csharp
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
using OpenAI.Responses;

string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
var client = new OpenAIResponseClient(model: "gpt-5", apiKey: apiKey);

OpenAIResponse response = client.CreateResponse(
    "Write a short bedtime story about a unicorn."
);

Console.WriteLine(response.GetOutputText());
```

Browse models

[View all](https://platform.openai.com/docs/models)

[GPT-5\\
\\
The best model for coding and agentic tasks across domains](https://platform.openai.com/docs/models/gpt-5) [GPT-5 mini\\
\\
A faster, cost-efficient version of GPT-5 for well-defined tasks](https://platform.openai.com/docs/models/gpt-5-mini) [GPT-5 nano\\
\\
Fastest, most cost-efficient version of GPT-5](https://platform.openai.com/docs/models/gpt-5-nano)

## Start building

[Read and generate text\\
\\
Use the API to prompt a model and generate text](https://platform.openai.com/docs/guides/text) [Use a model's vision capabilities\\
\\
Allow models to see and analyze images in your application](https://platform.openai.com/docs/guides/images) [Generate images as output\\
\\
Create images with GPT Image 1](https://platform.openai.com/docs/guides/image-generation) [Build apps with audio\\
\\
Analyze, transcribe, and generate audio with API endpoints](https://platform.openai.com/docs/guides/audio) [Build agentic applications\\
\\
Use the API to build agents that use tools and computers](https://platform.openai.com/docs/guides/agents) [Achieve complex tasks with reasoning\\
\\
Use reasoning models to carry out complex tasks](https://platform.openai.com/docs/guides/reasoning) [Get structured data from models\\
\\
Use Structured Outputs to get model responses that adhere to a JSON schema](https://platform.openai.com/docs/guides/structured-outputs) [Tailor to your use case\\
\\
Adjust our models to perform specifically for your use case with fine-tuning, evals, and distillation](https://platform.openai.com/docs/guides/fine-tuning)

[Help center\\
\\
Frequently asked account and billing questions](https://help.openai.com/) [Developer forum\\
\\
Discuss topics with other developers](https://community.openai.com/) [Cookbook\\
\\
Open-source collection of examples and guides](https://cookbook.openai.com/) [Status\\
\\
Check the status of OpenAI services](https://status.openai.com/)

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all