---
url: "https://platform.openai.com/docs/assistants/tools/code-interpreter"
title: "Assistants Code Interpreter - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Assistants Code Interpreter  Deprecated

Copy page

After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the [migration guide](https://platform.openai.com/docs/assistants/migration) to update your integration. [Learn more](https://platform.openai.com/docs/guides/responses-vs-chat-completions).

## Overview

Code Interpreter allows Assistants to write and run Python code in a sandboxed execution environment. This tool can process files with diverse data and formatting, and generate files with data and images of graphs. Code Interpreter allows your Assistant to run code iteratively to solve challenging code and math problems. When your Assistant writes code that fails to run, it can iterate on this code by attempting to run different code until the code execution succeeds.

See a quickstart of how to get started with Code Interpreter [here](https://platform.openai.com/docs/assistants/overview#step-1-create-an-assistant?context=with-streaming).

## How it works

Code Interpreter is charged at $0.03 per session. If your Assistant calls Code Interpreter simultaneously in two different threads (e.g., one thread per end-user), two Code Interpreter sessions are created. Each session is active by default for one hour, which means that you only pay for one session per if users interact with Code Interpreter in the same thread for up to one hour.

### Enabling Code Interpreter

Pass `code_interpreter` in the `tools` parameter of the Assistant object to enable Code Interpreter:

python

```python
1
2
3
4
5
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}]
)
```

```javascript
1
2
3
4
5
const assistant = await openai.beta.assistants.create({
  instructions: "You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model: "gpt-4o",
  tools: [{"type": "code_interpreter"}]
});
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
curl https://api.openai.com/v1/assistants \
  -u :$OPENAI_API_KEY \
  -H 'Content-Type: application/json' \
  -H 'OpenAI-Beta: assistants=v2' \
  -d '{
    "instructions": "You are a personal math tutor. When asked a math question, write and run code to answer the question.",
    "tools": [\
      { "type": "code_interpreter" }\
    ],
    "model": "gpt-4o"
  }'
```

The model then decides when to invoke Code Interpreter in a Run based on the nature of the user request. This behavior can be promoted by prompting in the Assistant's `instructions` (e.g., “write code to solve this problem”).

### Passing files to Code Interpreter

Files that are passed at the Assistant level are accessible by all Runs with this Assistant:

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
# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("mydata.csv", "rb"),
  purpose='assistants'
)

# Create an assistant using the file ID
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
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
// Upload a file with an "assistants" purpose
const file = await openai.files.create({
  file: fs.createReadStream("mydata.csv"),
  purpose: "assistants",
});

// Create an assistant using the file ID
const assistant = await openai.beta.assistants.create({
  instructions: "You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model: "gpt-4o",
  tools: [{"type": "code_interpreter"}],
  tool_resources: {
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
});
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
# Upload a file with an "assistants" purpose
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F purpose="assistants" \
  -F file="@/path/to/mydata.csv"

# Create an assistant using the file ID
curl https://api.openai.com/v1/assistants \
  -u :$OPENAI_API_KEY \
  -H 'Content-Type: application/json' \
  -H 'OpenAI-Beta: assistants=v2' \
  -d '{
    "instructions": "You are a personal math tutor. When asked a math question, write and run code to answer the question.",
    "tools": [{"type": "code_interpreter"}],
    "model": "gpt-4o",
    "tool_resources": {
      "code_interpreter": {
        "file_ids": ["file-BK7bzQj3FfZFXr7DbL6xJwfo"]
      }
    }
  }'
```

Files can also be passed at the Thread level. These files are only accessible in the specific Thread. Upload the File using the [File upload](https://platform.openai.com/docs/api-reference/files/create) endpoint and then pass the File ID as part of the Message creation request:

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
thread = client.beta.threads.create(
  messages=[\
    {\
      "role": "user",\
      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",\
      "attachments": [\
        {\
          "file_id": file.id,\
          "tools": [{"type": "code_interpreter"}]\
        }\
      ]\
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
const thread = await openai.beta.threads.create({
  messages: [\
    {\
      "role": "user",\
      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",\
      "attachments": [\
        {\
          file_id: file.id,\
          tools: [{type: "code_interpreter"}]\
        }\
      ]\
    }\
  ]
});
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
curl https://api.openai.com/v1/threads/thread_abc123/messages \
  -u :$OPENAI_API_KEY \
  -H 'Content-Type: application/json' \
  -H 'OpenAI-Beta: assistants=v2' \
  -d '{
    "role": "user",
    "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",
    "attachments": [\
      {\
        "file_id": "file-ACq8OjcLQm2eIG0BvRM4z5qX",\
        "tools": [{"type": "code_interpreter"}]\
      }\
    ]
  }'
```

Files have a maximum size of 512 MB. Code Interpreter supports a variety of file formats including `.csv`, `.pdf`, `.json` and many more. More details on the file extensions (and their corresponding MIME-types) supported can be found in the [Supported files](https://platform.openai.com/docs/assistants/tools/code-interpreter#supported-files) section below.

### Reading images and files generated by Code Interpreter

Code Interpreter in the API also outputs files, such as generating image diagrams, CSVs, and PDFs. There are two types of files that are generated:

1. Images
2. Data files (e.g. a `csv` file with data generated by the Assistant)

When Code Interpreter generates an image, you can look up and download this file in the `file_id` field of the Assistant Message response:

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
{
	"id": "msg_abc123",
	"object": "thread.message",
	"created_at": 1698964262,
	"thread_id": "thread_abc123",
	"role": "assistant",
	"content": [\
    {\
      "type": "image_file",\
      "image_file": {\
        "file_id": "file-abc123"\
      }\
    }\
  ]
  # ...
}
```

The file content can then be downloaded by passing the file ID to the Files API:

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
from openai import OpenAI

client = OpenAI()

image_data = client.files.content("file-abc123")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)
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
import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const response = await openai.files.content("file-abc123");

  // Extract the binary data from the Response object
  const image_data = await response.arrayBuffer();

  // Convert the binary data to a Buffer
  const image_data_buffer = Buffer.from(image_data);

  // Save the image to a specific location
  fs.writeFileSync("./my-image.png", image_data_buffer);
}

main();
```

```bash
1
2
3
curl https://api.openai.com/v1/files/file-abc123/content \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  --output image.png
```

When Code Interpreter references a file path (e.g., ”Download this csv file”), file paths are listed as annotations. You can convert these annotations into links to download the file:

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
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699073585,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [\
    {\
      "type": "text",\
      "text": {\
        "value": "The rows of the CSV file have been shuffled and saved to a new CSV file. You can download the shuffled CSV file from the following link:\\n\\n[Download Shuffled CSV File](sandbox:/mnt/data/shuffled_file.csv)",\
        "annotations": [\
          {\
            "type": "file_path",\
            "text": "sandbox:/mnt/data/shuffled_file.csv",\
            "start_index": 167,\
            "end_index": 202,\
            "file_path": {\
              "file_id": "file-abc123"\
            }\
          }\
          ...\
```\
\
### Input and output logs of Code Interpreter\
\
By listing the steps of a Run that called Code Interpreter, you can inspect the code `input` and `outputs` logs of Code Interpreter:\
\
python\
\
```python\
1\
2\
3\
4\
run_steps = client.beta.threads.runs.steps.list(\
  thread_id=thread.id,\
  run_id=run.id\
)\
```\
\
```javascript\
1\
2\
3\
4\
const runSteps = await openai.beta.threads.runs.steps.list(\
  thread.id,\
  run.id\
);\
```\
\
```bash\
1\
2\
3\
curl https://api.openai.com/v1/threads/thread_abc123/runs/RUN_ID/steps \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -H "OpenAI-Beta: assistants=v2" \\
```\
\
```bash\
1\
2\
3\
4\
5\
6\
7\
8\
9\
10\
11\
12\
13\
14\
15\
16\
17\
18\
19\
20\
21\
22\
23\
24\
{\
  "object": "list",\
  "data": [\
    {\
      "id": "step_abc123",\
      "object": "thread.run.step",\
      "type": "tool_calls",\
      "run_id": "run_abc123",\
      "thread_id": "thread_abc123",\
      "status": "completed",\
      "step_details": {\
        "type": "tool_calls",\
        "tool_calls": [\
          {\
            "type": "code",\
            "code": {\
              "input": "# Calculating 2 + 2\\nresult = 2 + 2\\nresult",\
              "outputs": [\
                {\
                  "type": "logs",\
                  "logs": "4"\
                }\
						...\
 }\
```\
\
## Supported files\
\
| File format | MIME type |\
| --- | --- |\
| `.c` | `text/x-c` |\
| `.cs` | `text/x-csharp` |\
| `.cpp` | `text/x-c++` |\
| `.csv` | `text/csv` |\
| `.doc` | `application/msword` |\
| `.docx` | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |\
| `.html` | `text/html` |\
| `.java` | `text/x-java` |\
| `.json` | `application/json` |\
| `.md` | `text/markdown` |\
| `.pdf` | `application/pdf` |\
| `.php` | `text/x-php` |\
| `.pptx` | `application/vnd.openxmlformats-officedocument.presentationml.presentation` |\
| `.py` | `text/x-python` |\
| `.py` | `text/x-script.python` |\
| `.rb` | `text/x-ruby` |\
| `.tex` | `text/x-tex` |\
| `.txt` | `text/plain` |\
| `.css` | `text/css` |\
| `.js` | `text/javascript` |\
| `.sh` | `application/x-sh` |\
| `.ts` | `application/typescript` |\
| `.csv` | `application/csv` |\
| `.jpeg` | `image/jpeg` |\
| `.jpg` | `image/jpeg` |\
| `.gif` | `image/gif` |\
| `.pkl` | `application/octet-stream` |\
| `.png` | `image/png` |\
| `.tar` | `application/x-tar` |\
| `.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |\
| `.xml` | `application/xml or "text/xml"` |\
| `.zip` | `application/zip` |\
\
We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.\
\
Reject allAccept all