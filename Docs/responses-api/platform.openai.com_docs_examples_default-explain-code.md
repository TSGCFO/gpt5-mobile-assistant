---
url: "https://platform.openai.com/docs/examples/default-explain-code"
title: "Prompt examples - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Prompt examples

Explore what's possible with some example prompts

All categories

Grammar correction

Convert ungrammatical statements into standard English.

Summarize for a 2nd grader

Simplify text to a level appropriate for a second-grade student.

Parse unstructured data

Create tables from unstructured text.

Emoji Translation

Translate regular text into emoji text.

Calculate time complexity

Find the time complexity of a function.

Explain code

Explain a complicated piece of code.

Keywords

Extract keywords from a block of text.

Product name generator

Generate product names from a description and seed words.

Python bug fixer

Find and fix bugs in source code.

Spreadsheet creator

Create spreadsheets of various kinds of data.

Tweet classifier

Detect sentiment in a tweet.

Airport code extractor

Extract airport codes from text.

Mood to color

Turn a text description into a color.

VR fitness idea generator

Generate ideas for fitness promoting virtual reality games.

Marv the sarcastic chat bot

Marv is a factual chatbot that is also sarcastic.

Turn by turn directions

Convert natural language to turn-by-turn directions.

Interview questions

Create interview questions.

Function from specification

Create a Python function from a specification.

Improve code efficiency

Provide ideas for efficiency improvements to Python code.

Single page website creator

Create a single page website.

Rap battle writer

Generate a rap battle between two characters.

Memo writer

Generate a company memo based on provided points.

Emoji chatbot

Generate conversational replies using emojis only.

Translation

Translate natural language text.

Socratic tutor

Generate responses as a Socratic tutor.

Natural language to SQL

Convert natural language into SQL queries.

Meeting notes summarizer

Summarize meeting notes including overall discussion, action items, and future topics.

Review classifier

Classify user reviews based on a set of tags.

Pro and con discusser

Analyze the pros and cons of a given topic.

Lesson plan writer

Generate a lesson plan for a specific topic.

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all

## Explain code

Extract

Code

Explain a complicated piece of code.

##### Prompt

SYSTEM

You will be provided with a piece of code, and your task is to explain it in a concise way.

USER

class Log:
def \_\_init\_\_(self, path):
dirname = os.path.dirname(path)
os.makedirs(dirname, exist\_ok=True)
f = open(path, "a+")

# Check that the file is newline-terminated
size = os.path.getsize(path)
if size > 0:
f.seek(size - 1)
end = f.read(1)
if end != "\\n":
f.write("\\n")
self.f = f
self.path = path

def log(self, event):
event\["\_event\_id"\] = str(uuid.uuid4())
json.dump(event, self.f)
self.f.write("\\n")

def state(self):
state = {"complete": set(), "last": None}
for line in open(self.path):
event = json.loads(line)
if event\["type"\] == "submit" and event\["success"\]:
state\["complete"\].add(event\["id"\])
state\["last"\] = event
return state

##### Sample response

This code defines a class \`Log\` that is used to log events to a file and retrieve the state of the log.

The \`\_\_init\_\_\` method initializes the log file. It takes a file path as an argument, creates the directory if it doesn't exist, and opens the file in append mode. If the file is not empty and doesn't end with a newline, it appends a newline.

The \`log\` method logs an event to the file. It takes a dictionary as an argument, adds a unique identifier to it, converts it to JSON, and writes it to the file followed by a newline.

The \`state\` method retrieves the state of the log. It initializes a dictionary with two keys: "complete" (a set of completed events) and "last" (the last event). It then reads the log file line by line, parses each line as JSON, and if the event type is "submit" and it was successful, it adds the event id to the "complete" set and updates the "last" event. Finally, it returns the state dictionary.

##### API request

python

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
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4o",
  "input": [\
    {\
      "role": "system",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "You will be provided with a piece of code, and your task is to explain it in a concise way."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "class Log:\n        def __init__(self, path):\n            dirname = os.path.dirname(path)\n            os.makedirs(dirname, exist_ok=True)\n            f = open(path, \"a+\")\n    \n            # Check that the file is newline-terminated\n            size = os.path.getsize(path)\n            if size > 0:\n                f.seek(size - 1)\n                end = f.read(1)\n                if end != \"\\n\":\n                    f.write(\"\\n\")\n            self.f = f\n            self.path = path\n    \n        def log(self, event):\n            event[\"_event_id\"] = str(uuid.uuid4())\n            json.dump(event, self.f)\n            self.f.write(\"\\n\")\n    \n        def state(self):\n            state = {\"complete\": set(), \"last\": None}\n            for line in open(self.path):\n                event = json.loads(line)\n                if event[\"type\"] == \"submit\" and event[\"success\"]:\n                    state[\"complete\"].add(event[\"id\"])\n                    state[\"last\"] = event\n            return state"\
        }\
      ]\
    }\
  ],
  "temperature": 1,
  "max_output_tokens": 1024
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
24
25
26
27
28
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-4o",
  input=[\
    {\
      "role": "system",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "You will be provided with a piece of code, and your task is to explain it in a concise way."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "class Log:\n        def __init__(self, path):\n            dirname = os.path.dirname(path)\n            os.makedirs(dirname, exist_ok=True)\n            f = open(path, \"a+\")\n    \n            # Check that the file is newline-terminated\n            size = os.path.getsize(path)\n            if size > 0:\n                f.seek(size - 1)\n                end = f.read(1)\n                if end != \"\\n\":\n                    f.write(\"\\n\")\n            self.f = f\n            self.path = path\n    \n        def log(self, event):\n            event[\"_event_id\"] = str(uuid.uuid4())\n            json.dump(event, self.f)\n            self.f.write(\"\\n\")\n    \n        def state(self):\n            state = {\"complete\": set(), \"last\": None}\n            for line in open(self.path):\n                event = json.loads(line)\n                if event[\"type\"] == \"submit\" and event[\"success\"]:\n                    state[\"complete\"].add(event[\"id\"])\n                    state[\"last\"] = event\n            return state"\
        }\
      ]\
    }\
  ],
  temperature=1,
  max_output_tokens=1024
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
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = await openai.responses.create({
  model: "gpt-4o",
  input: [\
    {\
      "role": "system",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "You will be provided with a piece of code, and your task is to explain it in a concise way."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "class Log:\n        def __init__(self, path):\n            dirname = os.path.dirname(path)\n            os.makedirs(dirname, exist_ok=True)\n            f = open(path, \"a+\")\n    \n            # Check that the file is newline-terminated\n            size = os.path.getsize(path)\n            if size > 0:\n                f.seek(size - 1)\n                end = f.read(1)\n                if end != \"\\n\":\n                    f.write(\"\\n\")\n            self.f = f\n            self.path = path\n    \n        def log(self, event):\n            event[\"_event_id\"] = str(uuid.uuid4())\n            json.dump(event, self.f)\n            self.f.write(\"\\n\")\n    \n        def state(self):\n            state = {\"complete\": set(), \"last\": None}\n            for line in open(self.path):\n                event = json.loads(line)\n                if event[\"type\"] == \"submit\" and event[\"success\"]:\n                    state[\"complete\"].add(event[\"id\"])\n                    state[\"last\"] = event\n            return state"\
        }\
      ]\
    }\
  ],
  temperature: 1,
  max_output_tokens: 1024
});
```

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
{
  "model": "gpt-4o",
  "input": [\
    {\
      "role": "system",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "You will be provided with a piece of code, and your task is to explain it in a concise way."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "class Log:\n        def __init__(self, path):\n            dirname = os.path.dirname(path)\n            os.makedirs(dirname, exist_ok=True)\n            f = open(path, \"a+\")\n    \n            # Check that the file is newline-terminated\n            size = os.path.getsize(path)\n            if size > 0:\n                f.seek(size - 1)\n                end = f.read(1)\n                if end != \"\\n\":\n                    f.write(\"\\n\")\n            self.f = f\n            self.path = path\n    \n        def log(self, event):\n            event[\"_event_id\"] = str(uuid.uuid4())\n            json.dump(event, self.f)\n            self.f.write(\"\\n\")\n    \n        def state(self):\n            state = {\"complete\": set(), \"last\": None}\n            for line in open(self.path):\n                event = json.loads(line)\n                if event[\"type\"] == \"submit\" and event[\"success\"]:\n                    state[\"complete\"].add(event[\"id\"])\n                    state[\"last\"] = event\n            return state"\
        }\
      ]\
    }\
  ],
  "temperature": 1,
  "max_output_tokens": 1024
}
```