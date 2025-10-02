---
url: "https://platform.openai.com/docs/quickstart?context=node"
title: "Developer quickstart - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Developer quickstart

Take your first steps with the OpenAI API.

Copy page

The OpenAI API provides a simple interface to state-of-the-art AI [models](https://platform.openai.com/docs/models) for text generation, natural language processing, computer vision, and more. This example generates [text output](https://platform.openai.com/docs/guides/text) from a prompt, as you might using [ChatGPT](https://chatgpt.com/).

Generate text from a model

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
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5",
    input: "Write a one-sentence bedtime story about a unicorn."
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
    input="Write a one-sentence bedtime story about a unicorn."
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

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

OpenAIResponse response = client.CreateResponse(
    "Write a one-sentence bedtime story about a unicorn."
);

Console.WriteLine(response.GetOutputText());
```

```bash
1
2
3
4
5
6
7
curl "https://api.openai.com/v1/responses" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-5",
        "input": "Write a one-sentence bedtime story about a unicorn."
    }'
```

[Configure your development environment\\
\\
Install and configure an official OpenAI SDK to run the code above.](https://platform.openai.com/docs/libraries) [Responses starter app\\
\\
Start building with the Responses API.](https://github.com/openai/openai-responses-starter-app) [Text generation and prompting\\
\\
Learn more about prompting, message roles, and building conversational apps.](https://platform.openai.com/docs/guides/text)

## Analyze images and files

Send image URLs, uploaded files, or PDF documents directly to the model to extract text, classify content, or detect visual elements.

Image URLFile URLUpload file

Image URL

Analyze the content of an image

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
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5",
    input: [\
        {\
            role: "user",\
            content: [\
                {\
                    type: "input_text",\
                    text: "What is in this image?",\
                },\
                {\
                    type: "input_image",\
                    image_url: "https://openai-documentation.vercel.app/images/cat_and_otter.png",\
                },\
            ],\
        },\
    ],
});

console.log(response.output_text);
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
21
curl "https://api.openai.com/v1/responses" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-5",
        "input": [\
            {\
                "role": "user",\
                "content": [\
                    {\
                        "type": "input_text",\
                        "text": "What is in this image?"\
                    },\
                    {\
                        "type": "input_image",\
                        "image_url": "https://openai-documentation.vercel.app/images/cat_and_otter.png"\
                    }\
                ]\
            }\
        ]
    }'
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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=[\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "input_text",\
                    "text": "What teams are playing in this image?",\
                },\
                {\
                    "type": "input_image",\
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"\
                }\
            ]\
        }\
    ]
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
11
12
13
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("What is in this image?"),\
        ResponseContentPart.CreateInputImagePart(new Uri("https://openai-documentation.vercel.app/images/cat_and_otter.png")),\
    ]),\
]);

Console.WriteLine(response.GetOutputText());
```

File URL

Use a file URL as input

javascript

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
21
curl "https://api.openai.com/v1/responses" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-5",
        "input": [\
            {\
                "role": "user",\
                "content": [\
                    {\
                        "type": "input_text",\
                        "text": "Analyze the letter and provide a summary of the key points."\
                    },\
                    {\
                        "type": "input_file",\
                        "file_url": "https://www.berkshirehathaway.com/letters/2024ltr.pdf"\
                    }\
                ]\
            }\
        ]
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
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5",
    input: [\
        {\
            role: "user",\
            content: [\
                {\
                    type: "input_text",\
                    text: "Analyze the letter and provide a summary of the key points.",\
                },\
                {\
                    type: "input_file",\
                    file_url: "https://www.berkshirehathaway.com/letters/2024ltr.pdf",\
                },\
            ],\
        },\
    ],
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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=[\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "input_text",\
                    "text": "Analyze the letter and provide a summary of the key points.",\
                },\
                {\
                    "type": "input_file",\
                    "file_url": "https://www.berkshirehathaway.com/letters/2024ltr.pdf",\
                },\
            ],\
        },\
    ]
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
11
12
13
14
15
16
17
18
19
using OpenAI.Files;
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

using HttpClient http = new();
using Stream stream = await http.GetStreamAsync("https://www.berkshirehathaway.com/letters/2024ltr.pdf");
OpenAIFileClient files = new(key);
OpenAIFile file = files.UploadFile(stream, "2024ltr.pdf", FileUploadPurpose.UserData);

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("Analyze the letter and provide a summary of the key points."),\
        ResponseContentPart.CreateInputFilePart(file.Id),\
    ]),\
]);

Console.WriteLine(response.GetOutputText());
```

Upload file

Upload a file and use it as input

javascript

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
21
22
23
24
25
26
curl https://api.openai.com/v1/files \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -F purpose="user_data" \
    -F file="@draconomicon.pdf"

curl "https://api.openai.com/v1/responses" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-5",
        "input": [\
            {\
                "role": "user",\
                "content": [\
                    {\
                        "type": "input_file",\
                        "file_id": "file-6F2ksmvXxt4VdoqmHRw6kL"\
                    },\
                    {\
                        "type": "input_text",\
                        "text": "What is the first dragon in the book?"\
                    }\
                ]\
            }\
        ]
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
import fs from "fs";
import OpenAI from "openai";
const client = new OpenAI();

const file = await client.files.create({
    file: fs.createReadStream("draconomicon.pdf"),
    purpose: "user_data",
});

const response = await client.responses.create({
    model: "gpt-5",
    input: [\
        {\
            role: "user",\
            content: [\
                {\
                    type: "input_file",\
                    file_id: file.id,\
                },\
                {\
                    type: "input_text",\
                    text: "What is the first dragon in the book?",\
                },\
            ],\
        },\
    ],
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
from openai import OpenAI
client = OpenAI()

file = client.files.create(
    file=open("draconomicon.pdf", "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model="gpt-5",
    input=[\
        {\
            "role": "user",\
            "content": [\
                {\
                    "type": "input_file",\
                    "file_id": file.id,\
                },\
                {\
                    "type": "input_text",\
                    "text": "What is the first dragon in the book?",\
                },\
            ]\
        }\
    ]
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
11
12
13
14
15
16
17
using OpenAI.Files;
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

OpenAIFileClient files = new(key);
OpenAIFile file = files.UploadFile("draconomicon.pdf", FileUploadPurpose.UserData);

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputFilePart(file.Id),\
        ResponseContentPart.CreateInputTextPart("What is the first dragon in the book?"),\
    ]),\
]);

Console.WriteLine(response.GetOutputText());
```

[Image inputs guide\\
\\
Learn to use image inputs to the model and extract meaning from images.](https://platform.openai.com/docs/guides/images) [File inputs guide\\
\\
Learn to use file inputs to the model and extract meaning from documents.](https://platform.openai.com/docs/guides/pdf-files)

## Extend the model with tools

Give the model access to external data and functions by attaching [tools](https://platform.openai.com/docs/guides/tools). Use built-in tools like web search or file search, or define your own for calling APIs, running code, or integrating with third-party systems.

Web searchFile searchFunction callingRemote MCP

Web search

Use web search in a response

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
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5",
    tools: [\
        { type: "web_search" },\
    ],
    input: "What was a positive news story from today?",
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
10
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    tools=[{"type": "web_search"}],
    input="What was a positive news story from today?"
)

print(response.output_text)
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
curl "https://api.openai.com/v1/responses" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-5",
        "tools": [{"type": "web_search"}],
        "input": "what was a positive news story from today?"
    }'
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
11
12
13
14
15
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

ResponseCreationOptions options = new();
options.Tools.Add(ResponseTool.CreateWebSearchTool());

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("What was a positive news story from today?"),\
    ]),\
], options);

Console.WriteLine(response.GetOutputText());
```

File search

Search your files in a response

javascript

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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="What is deep research by OpenAI?",
    tools=[{\
        "type": "file_search",\
        "vector_store_ids": ["<vector_store_id>"]\
    }]
)
print(response)
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
10
11
12
13
14
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-4.1",
    input: "What is deep research by OpenAI?",
    tools: [\
        {\
            type: "file_search",\
            vector_store_ids: ["<vector_store_id>"],\
        },\
    ],
});
console.log(response);
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
11
12
13
14
15
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

ResponseCreationOptions options = new();
options.Tools.Add(ResponseTool.CreateFileSearchTool(["<vector_store_id>"]));

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("What is deep research by OpenAI?"),\
    ]),\
], options);

Console.WriteLine(response.GetOutputText());
```

Function calling

Call your own function

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
import OpenAI from "openai";
const client = new OpenAI();

const tools = [\
    {\
        type: "function",\
        name: "get_weather",\
        description: "Get current temperature for a given location.",\
        parameters: {\
            type: "object",\
            properties: {\
                location: {\
                    type: "string",\
                    description: "City and country e.g. Bogotá, Colombia",\
                },\
            },\
            required: ["location"],\
            additionalProperties: false,\
        },\
        strict: true,\
    },\
];

const response = await client.responses.create({
    model: "gpt-5",
    input: [\
        { role: "user", content: "What is the weather like in Paris today?" },\
    ],
    tools,
});

console.log(response.output[0].to_json());
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
from openai import OpenAI

client = OpenAI()

tools = [\
    {\
        "type": "function",\
        "name": "get_weather",\
        "description": "Get current temperature for a given location.",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "location": {\
                    "type": "string",\
                    "description": "City and country e.g. Bogotá, Colombia",\
                }\
            },\
            "required": ["location"],\
            "additionalProperties": False,\
        },\
        "strict": True,\
    },\
]

response = client.responses.create(
    model="gpt-5",
    input=[\
        {"role": "user", "content": "What is the weather like in Paris today?"},\
    ],
    tools=tools,
)

print(response.output[0].to_json())
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
using System.Text.Json;
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

ResponseCreationOptions options = new();
options.Tools.Add(ResponseTool.CreateFunctionTool(
    functionName: "get_weather",
    functionDescription: "Get current temperature for a given location.",
    functionParameters: BinaryData.FromObjectAsJson(new
    {
        type = "object",
        properties = new
        {
            location = new
            {
                type = "string",
                description = "City and country e.g. Bogotá, Colombia",
            },
        },
        required = new[] { "location" },
        additionalProperties = false,
    }),
    strictModeEnabled: true
));

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("What is the weather like in Paris today?"),\
    ]),\
], options);

Console.WriteLine(JsonSerializer.Serialize(response.OutputItems[0]));
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
21
22
23
24
25
26
27
28
curl -X POST https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "input": [\
      {"role": "user", "content": "What is the weather like in Paris today?"}\
    ],
    "tools": [\
      {\
        "type": "function",\
        "name": "get_weather",\
        "description": "Get current temperature for a given location.",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "City and country e.g. Bogotá, Colombia"\
            }\
          },\
          "required": ["location"],\
          "additionalProperties": false\
        },\
        "strict": true\
      }\
    ]
  }'
```

Remote MCP

Call a remote MCP server

javascript

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
curl https://api.openai.com/v1/responses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "gpt-5",
    "tools": [\
      {\
        "type": "mcp",\
        "server_label": "dmcp",\
        "server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",\
        "server_url": "https://dmcp-server.deno.dev/sse",\
        "require_approval": "never"\
      }\
    ],
    "input": "Roll 2d4+1"
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
10
11
12
13
14
15
16
17
18
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
  model: "gpt-5",
  tools: [\
    {\
      type: "mcp",\
      server_label: "dmcp",\
      server_description: "A Dungeons and Dragons MCP server to assist with dice rolling.",\
      server_url: "https://dmcp-server.deno.dev/sse",\
      require_approval: "never",\
    },\
  ],
  input: "Roll 2d4+1",
});

console.log(resp.output_text);
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
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-5",
    tools=[\
        {\
            "type": "mcp",\
            "server_label": "dmcp",\
            "server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",\
            "server_url": "https://dmcp-server.deno.dev/sse",\
            "require_approval": "never",\
        },\
    ],
    input="Roll 2d4+1",
)

print(resp.output_text)
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
11
12
13
14
15
16
17
18
19
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

ResponseCreationOptions options = new();
options.Tools.Add(ResponseTool.CreateMcpTool(
    serverLabel: "dmcp",
    serverUri: new Uri("https://dmcp-server.deno.dev/sse"),
    toolCallApprovalPolicy: new McpToolCallApprovalPolicy(GlobalMcpToolCallApprovalPolicy.NeverRequireApproval)
));

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("Roll 2d4+1"),\
    ]),\
], options);

Console.WriteLine(response.GetOutputText());
```

[Use built-in tools\\
\\
Learn about powerful built-in tools like web search and file search.](https://platform.openai.com/docs/guides/tools) [Function calling guide\\
\\
Learn to enable the model to call your own custom code.](https://platform.openai.com/docs/guides/function-calling)

## Stream responses and build realtime apps

Use server‑sent [streaming events](https://platform.openai.com/docs/guides/streaming-responses) to show results as they’re generated, or the [Realtime API](https://platform.openai.com/docs/guides/realtime) for interactive voice and multimodal apps.

Stream server-sent events from the API

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
import { OpenAI } from "openai";
const client = new OpenAI();

const stream = await client.responses.create({
    model: "gpt-5",
    input: [\
        {\
            role: "user",\
            content: "Say 'double bubble bath' ten times fast.",\
        },\
    ],
    stream: true,
});

for await (const event of stream) {
    console.log(event);
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
from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-5",
    input=[\
        {\
            "role": "user",\
            "content": "Say 'double bubble bath' ten times fast.",\
        },\
    ],
    stream=True,
)

for event in stream:
    print(event)
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
11
12
13
14
15
16
17
18
using OpenAI.Responses;

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
OpenAIResponseClient client = new(model: "gpt-5", apiKey: key);

var responses = client.CreateResponseStreamingAsync([\
    ResponseItem.CreateUserMessageItem([\
        ResponseContentPart.CreateInputTextPart("Say 'double bubble bath' ten times fast."),\
    ]),\
]);

await foreach (var response in responses)
{
    if (response is StreamingResponseOutputTextDeltaUpdate delta)
    {
        Console.Write(delta.Delta);
    }
}
```

[Use streaming events\\
\\
Use server-sent events to stream model responses to users fast.](https://platform.openai.com/docs/guides/streaming-responses) [Get started with the Realtime API\\
\\
Use WebRTC or WebSockets for super fast speech-to-speech AI apps.](https://platform.openai.com/docs/guides/realtime)

## Build agents

Use the OpenAI platform to build [agents](https://platform.openai.com/docs/guides/agents) capable of taking action—like [controlling computers](https://platform.openai.com/docs/guides/tools-computer-use)—on behalf of your users. Use the Agents SDK for [Python](https://openai.github.io/openai-agents-python) or [TypeScript](https://openai.github.io/openai-agents-js) to create orchestration logic on the backend.

Build a language triage agent

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
import { Agent, run } from '@openai/agents';

const spanishAgent = new Agent({
    name: 'Spanish agent',
    instructions: 'You only speak Spanish.',
});

const englishAgent = new Agent({
    name: 'English agent',
    instructions: 'You only speak English',
});

const triageAgent = new Agent({
    name: 'Triage agent',
    instructions:
        'Handoff to the appropriate agent based on the language of the request.',
    handoffs: [spanishAgent, englishAgent],
});

const result = await run(triageAgent, 'Hola, ¿cómo estás?');
console.log(result.finalOutput);
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
from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
)

async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

[Build agents that can take action\\
\\
Learn how to use the OpenAI platform to build powerful, capable AI agents.](https://platform.openai.com/docs/guides/agents)