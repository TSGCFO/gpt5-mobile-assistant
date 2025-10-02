---
url: "https://platform.openai.com/docs/examples/default-keywords"
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

## Keywords

Extract

Natural Language

Extract keywords from a block of text.

##### Prompt

SYSTEM

You will be provided with a block of text, and your task is to extract a list of keywords from it.

USER

Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.

##### Sample response

Black-on-black ware, pottery tradition, Puebloan Native American, ceramic artists, Northern New Mexico, reduction-fired blackware, pueblo artists, smooth surface, designs, selective burnishing, refractory slip, carving, incising designs, polishing, generations, families, Kha'po Owingeh, P'ohwhóge Owingeh pueblos, matriarch potters, contemporary artists, ancestors

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
          "text": "You will be provided with a block of text, and your task is to extract a list of keywords from it."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha\"po Owingeh and P\"ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."\
        }\
      ]\
    }\
  ],
  "temperature": 0.5,
  "max_output_tokens": 256
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
          "text": "You will be provided with a block of text, and your task is to extract a list of keywords from it."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."\
        }\
      ]\
    }\
  ],
  temperature=0.5,
  max_output_tokens=256
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
          "text": "You will be provided with a block of text, and your task is to extract a list of keywords from it."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."\
        }\
      ]\
    }\
  ],
  temperature: 0.5,
  max_output_tokens: 256
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
          "text": "You will be provided with a block of text, and your task is to extract a list of keywords from it."\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."\
        }\
      ]\
    }\
  ],
  "temperature": 0.5,
  "max_output_tokens": 256
}
```