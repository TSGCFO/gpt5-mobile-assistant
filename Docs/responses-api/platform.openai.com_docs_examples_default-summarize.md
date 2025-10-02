---
url: "https://platform.openai.com/docs/examples/default-summarize"
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

## Summarize for a 2nd grader

Extract

Natural Language

Simplify text to a level appropriate for a second-grade student.

##### Prompt

SYSTEM

Summarize content you are provided with for a second-grade student.

USER

Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.\[19\] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,\[20\] and is on average the third-brightest natural object in the night sky after the Moon and Venus.

##### Sample response

Jupiter is a really big planet in our Solar System. It is the fifth planet from the Sun and it is the largest planet. It is called a gas giant because it is made mostly of gas. Jupiter is much smaller than the Sun, but it is bigger than all the other planets combined. It is very bright and can be seen in the night sky without a telescope. People have known about Jupiter for a very long time, even before they started writing things down. It is named after a god from ancient Rome. Sometimes, Jupiter is so bright that it can make shadows on Earth. It is usually the third-brightest thing we can see in the night sky, after the Moon and Venus.

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
          "text": "Summarize content you are provided with for a second-grade student."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."\
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
          "text": "Summarize content you are provided with for a second-grade student."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."\
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
          "text": "Summarize content you are provided with for a second-grade student."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."\
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
          "text": "Summarize content you are provided with for a second-grade student."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."\
        }\
      ]\
    }\
  ],
  "temperature": 1,
  "max_output_tokens": 1024
}
```