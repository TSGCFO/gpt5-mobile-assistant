---
url: "https://platform.openai.com/docs/assistants/tools/function-calling"
title: "Assistants Function Calling - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Assistants Function Calling  Deprecated

Copy page

After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the [migration guide](https://platform.openai.com/docs/assistants/migration) to update your integration. [Learn more](https://platform.openai.com/docs/guides/responses-vs-chat-completions).

## Overview

Similar to the Chat Completions API, the Assistants API supports function calling. Function calling allows you to describe functions to the Assistants API and have it intelligently return the functions that need to be called along with their arguments.

## Quickstart

In this example, we'll create a weather assistant and define two functions,
`get_current_temperature` and `get_rain_probability`, as tools that the Assistant can call.
Depending on the user query, the model will invoke parallel function calling if using our
latest models released on or after Nov 6, 2023.
In our example that uses parallel function calling, we will ask the Assistant what the weather in
San Francisco is like today and the chances of rain. We also show how to output the Assistant's response with streaming.

With the launch of Structured Outputs, you can now use the parameter `strict: true` when using function calling with the Assistants API.
For more information, refer to the [Function calling guide](https://platform.openai.com/docs/guides/function-calling#function-calling-with-structured-outputs).
Please note that Structured Outputs are not supported in the Assistants API when using vision.

### Step 1: Define functions

When creating your assistant, you will first define the functions under the `tools` param of the assistant.

python

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
from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="gpt-4o",
  tools=[\
    {\
      "type": "function",\
      "function": {\
        "name": "get_current_temperature",\
        "description": "Get the current temperature for a specific location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g., San Francisco, CA"\
            },\
            "unit": {\
              "type": "string",\
              "enum": ["Celsius", "Fahrenheit"],\
              "description": "The temperature unit to use. Infer this from the user's location."\
            }\
          },\
          "required": ["location", "unit"]\
        }\
      }\
    },\
    {\
      "type": "function",\
      "function": {\
        "name": "get_rain_probability",\
        "description": "Get the probability of rain for a specific location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g., San Francisco, CA"\
            }\
          },\
          "required": ["location"]\
        }\
      }\
    }\
  ]
)
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
const assistant = await client.beta.assistants.create({
  model: "gpt-4o",
  instructions:
    "You are a weather bot. Use the provided functions to answer questions.",
  tools: [\
    {\
      type: "function",\
      function: {\
        name: "getCurrentTemperature",\
        description: "Get the current temperature for a specific location",\
        parameters: {\
          type: "object",\
          properties: {\
            location: {\
              type: "string",\
              description: "The city and state, e.g., San Francisco, CA",\
            },\
            unit: {\
              type: "string",\
              enum: ["Celsius", "Fahrenheit"],\
              description:\
                "The temperature unit to use. Infer this from the user's location.",\
            },\
          },\
          required: ["location", "unit"],\
        },\
      },\
    },\
    {\
      type: "function",\
      function: {\
        name: "getRainProbability",\
        description: "Get the probability of rain for a specific location",\
        parameters: {\
          type: "object",\
          properties: {\
            location: {\
              type: "string",\
              description: "The city and state, e.g., San Francisco, CA",\
            },\
          },\
          required: ["location"],\
        },\
      },\
    },\
  ],
});
```

### Step 2: Create a Thread and add Messages

Create a Thread when a user starts a conversation and add Messages to the Thread as the user asks questions.

python

```python
1
2
3
4
5
6
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What's the weather in San Francisco today and the likelihood it'll rain?",
)
```

```javascript
1
2
3
4
5
const thread = await client.beta.threads.create();
const message = client.beta.threads.messages.create(thread.id, {
  role: "user",
  content: "What's the weather in San Francisco today and the likelihood it'll rain?",
});
```

### Step 3: Initiate a Run

When you initiate a Run on a Thread containing a user Message that triggers one or more functions,
the Run will enter a `pending` status. After it processes, the run will enter a `requires_action` state which you can
verify by checking the Run’s `status`. This indicates that you need to run tools and submit their outputs to the
Assistant to continue Run execution. In our case, we will see two `tool_calls`, which indicates that the
user query resulted in parallel function calling.

Note that a runs expire ten minutes after creation. Be sure to submit your tool outputs before the 10 min mark.

You will see two `tool_calls` within `required_action`, which indicates the user query triggered parallel function calling.

json

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
23
24
25
26
27
28
29
{
  "id": "run_qJL1kI9xxWlfE0z1yfL0fGg9",
  ...
  "status": "requires_action",
  "required_action": {
    "submit_tool_outputs": {
      "tool_calls": [\
        {\
          "id": "call_FthC9qRpsL5kBpwwyw6c7j4k",\
          "function": {\
            "arguments": "{"location": "San Francisco, CA"}",\
            "name": "get_rain_probability"\
          },\
          "type": "function"\
        },\
        {\
          "id": "call_RpEDoB8O0FTL9JoKTuCVFOyR",\
          "function": {\
            "arguments": "{"location": "San Francisco, CA", "unit": "Fahrenheit"}",\
            "name": "get_current_temperature"\
          },\
          "type": "function"\
        }\
      ]
    },
    ...
    "type": "submit_tool_outputs"
  }
}
```

Run object truncated here for readability

How you initiate a Run and submit `tool_calls` will differ depending on whether you are using streaming or not,
although in both cases all `tool_calls` need to be submitted at the same time.
You can then complete the Run by submitting the tool outputs from the functions you called.
Pass each `tool_call_id` referenced in the `required_action` object to match outputs to each function call.

With streamingWithout streaming

With streaming

For the streaming case, we create an EventHandler class to handle events in the response stream and submit all tool outputs at once with the “submit tool outputs stream” helper in the Python and Node SDKs.

python

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
from typing_extensions import override
from openai import AssistantEventHandler

class EventHandler(AssistantEventHandler):
    @override
    def on_event(self, event):
      # Retrieve events that are denoted with 'requires_action'
      # since these will have our tool_calls
      if event.event == 'thread.run.requires_action':
        run_id = event.data.id  # Retrieve the run ID from the event data
        self.handle_requires_action(event.data, run_id)

    def handle_requires_action(self, data, run_id):
      tool_outputs = []

      for tool in data.required_action.submit_tool_outputs.tool_calls:
        if tool.function.name == "get_current_temperature":
          tool_outputs.append({"tool_call_id": tool.id, "output": "57"})
        elif tool.function.name == "get_rain_probability":
          tool_outputs.append({"tool_call_id": tool.id, "output": "0.06"})

      # Submit all tool_outputs at the same time
      self.submit_tool_outputs(tool_outputs, run_id)

    def submit_tool_outputs(self, tool_outputs, run_id):
      # Use the submit_tool_outputs_stream helper
      with client.beta.threads.runs.submit_tool_outputs_stream(
        thread_id=self.current_run.thread_id,
        run_id=self.current_run.id,
        tool_outputs=tool_outputs,
        event_handler=EventHandler(),
      ) as stream:
        for text in stream.text_deltas:
          print(text, end="", flush=True)
        print()


with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  event_handler=EventHandler()
) as stream:
  stream.until_done()
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
class EventHandler extends EventEmitter {
  constructor(client) {
    super();
    this.client = client;
  }

  async onEvent(event) {
    try {
      console.log(event);
      // Retrieve events that are denoted with 'requires_action'
      // since these will have our tool_calls
      if (event.event === "thread.run.requires_action") {
        await this.handleRequiresAction(
          event.data,
          event.data.id,
          event.data.thread_id,
        );
      }
    } catch (error) {
      console.error("Error handling event:", error);
    }
  }

  async handleRequiresAction(data, runId, threadId) {
    try {
      const toolOutputs =
        data.required_action.submit_tool_outputs.tool_calls.map((toolCall) => {
          if (toolCall.function.name === "getCurrentTemperature") {
            return {
              tool_call_id: toolCall.id,
              output: "57",
            };
          } else if (toolCall.function.name === "getRainProbability") {
            return {
              tool_call_id: toolCall.id,
              output: "0.06",
            };
          }
        });
      // Submit all the tool outputs at the same time
      await this.submitToolOutputs(toolOutputs, runId, threadId);
    } catch (error) {
      console.error("Error processing required action:", error);
    }
  }

  async submitToolOutputs(toolOutputs, runId, threadId) {
    try {
      // Use the submitToolOutputsStream helper
      const stream = this.client.beta.threads.runs.submitToolOutputsStream(
        threadId,
        runId,
        { tool_outputs: toolOutputs },
      );
      for await (const event of stream) {
        this.emit("event", event);
      }
    } catch (error) {
      console.error("Error submitting tool outputs:", error);
    }
  }
}

const eventHandler = new EventHandler(client);
eventHandler.on("event", eventHandler.onEvent.bind(eventHandler));

const stream = await client.beta.threads.runs.stream(
  threadId,
  { assistant_id: assistantId },
  eventHandler,
);

for await (const event of stream) {
  eventHandler.emit("event", event);
}
```

Without streaming

Runs are asynchronous, which means you'll want to monitor their `status` by polling the Run object until a
[terminal status](https://platform.openai.com/docs/assistants/deep-dive#runs-and-run-steps) is reached. For convenience, the 'create and poll' SDK helpers assist both in
creating the run and then polling for its completion. Once the Run completes, you can list the
Messages added to the Thread by the Assistant. Finally, you would retrieve all the `tool_outputs` from
`required_action` and submit them at the same time to the 'submit tool outputs and poll' helper.

python

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
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
)

if run.status == 'completed':
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)

# Define the list to store tool outputs
tool_outputs = []

# Loop through each tool in the required action section
for tool in run.required_action.submit_tool_outputs.tool_calls:
  if tool.function.name == "get_current_temperature":
    tool_outputs.append({
      "tool_call_id": tool.id,
      "output": "57"
    })
  elif tool.function.name == "get_rain_probability":
    tool_outputs.append({
      "tool_call_id": tool.id,
      "output": "0.06"
    })

# Submit all tool outputs at once after collecting them in a list
if tool_outputs:
  try:
    run = client.beta.threads.runs.submit_tool_outputs_and_poll(
      thread_id=thread.id,
      run_id=run.id,
      tool_outputs=tool_outputs
    )
    print("Tool outputs submitted successfully.")
  except Exception as e:
    print("Failed to submit tool outputs:", e)
else:
  print("No tool outputs to submit.")

if run.status == 'completed':
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)
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
const handleRequiresAction = async (run) => {
  // Check if there are tools that require outputs
  if (
    run.required_action &&
    run.required_action.submit_tool_outputs &&
    run.required_action.submit_tool_outputs.tool_calls
  ) {
    // Loop through each tool in the required action section
    const toolOutputs = run.required_action.submit_tool_outputs.tool_calls.map(
      (tool) => {
        if (tool.function.name === "getCurrentTemperature") {
          return {
            tool_call_id: tool.id,
            output: "57",
          };
        } else if (tool.function.name === "getRainProbability") {
          return {
            tool_call_id: tool.id,
            output: "0.06",
          };
        }
      },
    );

    // Submit all tool outputs at once after collecting them in a list
    if (toolOutputs.length > 0) {
      run = await client.beta.threads.runs.submitToolOutputsAndPoll(
        thread.id,
        run.id,
        { tool_outputs: toolOutputs },
      );
      console.log("Tool outputs submitted successfully.");
    } else {
      console.log("No tool outputs to submit.");
    }

    // Check status after submitting tool outputs
    return handleRunStatus(run);
  }
};

const handleRunStatus = async (run) => {
  // Check if the run is completed
  if (run.status === "completed") {
    let messages = await client.beta.threads.messages.list(thread.id);
    console.log(messages.data);
    return messages.data;
  } else if (run.status === "requires_action") {
    console.log(run.status);
    return await handleRequiresAction(run);
  } else {
    console.error("Run did not complete:", run);
  }
};

// Create and poll run
let run = await client.beta.threads.runs.createAndPoll(thread.id, {
  assistant_id: assistant.id,
});

handleRunStatus(run);
```

### Using Structured Outputs

When you enable [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) by supplying `strict: true`, the OpenAI API will pre-process your supplied schema on your first request, and then use this artifact to constrain the model to your schema.

python

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
from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="gpt-4o-2024-08-06",
  tools=[\
    {\
      "type": "function",\
      "function": {\
        "name": "get_current_temperature",\
        "description": "Get the current temperature for a specific location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g., San Francisco, CA"\
            },\
            "unit": {\
              "type": "string",\
              "enum": ["Celsius", "Fahrenheit"],\
              "description": "The temperature unit to use. Infer this from the user's location."\
            }\
          },\
          "required": ["location", "unit"],\
          "additionalProperties": False\
        },\
        "strict": True\
      }\
    },\
    {\
      "type": "function",\
      "function": {\
        "name": "get_rain_probability",\
        "description": "Get the probability of rain for a specific location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g., San Francisco, CA"\
            }\
          },\
          "required": ["location"],\
          "additionalProperties": False\
        },\
        "strict": True\
      }\
    }\
  ]
)
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
const assistant = await client.beta.assistants.create({
  model: "gpt-4o-2024-08-06",
  instructions:
    "You are a weather bot. Use the provided functions to answer questions.",
  tools: [\
    {\
      type: "function",\
      function: {\
        name: "getCurrentTemperature",\
        description: "Get the current temperature for a specific location",\
        parameters: {\
          type: "object",\
          properties: {\
            location: {\
              type: "string",\
              description: "The city and state, e.g., San Francisco, CA",\
            },\
            unit: {\
              type: "string",\
              enum: ["Celsius", "Fahrenheit"],\
              description:\
                "The temperature unit to use. Infer this from the user's location.",\
            },\
          },\
          required: ["location", "unit"],\
          additionalProperties: false\
        },\
        strict: true\
      },\
    },\
    {\
      type: "function",\
      function: {\
        name: "getRainProbability",\
        description: "Get the probability of rain for a specific location",\
        parameters: {\
          type: "object",\
          properties: {\
            location: {\
              type: "string",\
              description: "The city and state, e.g., San Francisco, CA",\
            },\
          },\
          required: ["location"],\
          additionalProperties: false\
        },\
        strict: true\
      },\
    },\
  ],
});
```

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all