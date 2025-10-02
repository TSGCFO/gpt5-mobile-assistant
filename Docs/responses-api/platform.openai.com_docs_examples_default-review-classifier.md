---
url: "https://platform.openai.com/docs/examples/default-review-classifier"
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

## Review classifier

Extract

Natural Language

Classify user reviews based on a set of tags.

##### Prompt

SYSTEM

You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):

\- Provides good value for the price OR Costs too much
\- Works better than expected OR Did not work as well as expected
\- Includes essential features OR Lacks essential features
\- Easy to use OR Difficult to use
\- High quality and durability OR Poor quality and durability
\- Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair
\- Easy to transport OR Difficult to transport
\- Easy to store OR Difficult to store
\- Compatible with other devices or systems OR Not compatible with other devices or systems
\- Safe and user-friendly OR Unsafe or hazardous to use
\- Excellent customer support OR Poor customer support
\- Generous and comprehensive warranty OR Limited or insufficient warranty

USER

I recently purchased the Inflatotron 2000 airbed for a camping trip and wanted to share my experience with others. Overall, I found the airbed to be a mixed bag with some positives and negatives.

Starting with the positives, the Inflatotron 2000 is incredibly easy to set up and inflate. It comes with a built-in electric pump that quickly inflates the bed within a few minutes, which is a huge plus for anyone who wants to avoid the hassle of manually pumping up their airbed. The bed is also quite comfortable to sleep on and offers decent support for your back, which is a major plus if you have any issues with back pain.

On the other hand, I did experience some negatives with the Inflatotron 2000. Firstly, I found that the airbed is not very durable and punctures easily. During my camping trip, the bed got punctured by a stray twig that had fallen on it, which was quite frustrating. Secondly, I noticed that the airbed tends to lose air overnight, which meant that I had to constantly re-inflate it every morning. This was a bit annoying as it disrupted my sleep and made me feel less rested in the morning.

Another negative point is that the Inflatotron 2000 is quite heavy and bulky, which makes it difficult to transport and store. If you're planning on using this airbed for camping or other outdoor activities, you'll need to have a large enough vehicle to transport it and a decent amount of storage space to store it when not in use.

##### Sample response

\- Easy to use
\- Poor quality and durability
\- Difficult to transport
\- Difficult to store

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
          "text": "You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):\n    \n    - Provides good value for the price OR Costs too much\n    - Works better than expected OR Did not work as well as expected\n    - Includes essential features OR Lacks essential features\n    - Easy to use OR Difficult to use\n    - High quality and durability OR Poor quality and durability\n    - Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair\n    - Easy to transport OR Difficult to transport\n    - Easy to store OR Difficult to store\n    - Compatible with other devices or systems OR Not compatible with other devices or systems\n    - Safe and user-friendly OR Unsafe or hazardous to use\n    - Excellent customer support OR Poor customer support\n    - Generous and comprehensive warranty OR Limited or insufficient warranty"\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "I recently purchased the Inflatotron 2000 airbed for a camping trip and wanted to share my experience with others. Overall, I found the airbed to be a mixed bag with some positives and negatives.\n    \n    Starting with the positives, the Inflatotron 2000 is incredibly easy to set up and inflate. It comes with a built-in electric pump that quickly inflates the bed within a few minutes, which is a huge plus for anyone who wants to avoid the hassle of manually pumping up their airbed. The bed is also quite comfortable to sleep on and offers decent support for your back, which is a major plus if you have any issues with back pain.\n    \n    On the other hand, I did experience some negatives with the Inflatotron 2000. Firstly, I found that the airbed is not very durable and punctures easily. During my camping trip, the bed got punctured by a stray twig that had fallen on it, which was quite frustrating. Secondly, I noticed that the airbed tends to lose air overnight, which meant that I had to constantly re-inflate it every morning. This was a bit annoying as it disrupted my sleep and made me feel less rested in the morning.\n    \n    Another negative point is that the Inflatotron 2000 is quite heavy and bulky, which makes it difficult to transport and store. If you\"re planning on using this airbed for camping or other outdoor activities, you\"ll need to have a large enough vehicle to transport it and a decent amount of storage space to store it when not in use."\
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
          "text": "You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):\n    \n    - Provides good value for the price OR Costs too much\n    - Works better than expected OR Did not work as well as expected\n    - Includes essential features OR Lacks essential features\n    - Easy to use OR Difficult to use\n    - High quality and durability OR Poor quality and durability\n    - Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair\n    - Easy to transport OR Difficult to transport\n    - Easy to store OR Difficult to store\n    - Compatible with other devices or systems OR Not compatible with other devices or systems\n    - Safe and user-friendly OR Unsafe or hazardous to use\n    - Excellent customer support OR Poor customer support\n    - Generous and comprehensive warranty OR Limited or insufficient warranty"\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "I recently purchased the Inflatotron 2000 airbed for a camping trip and wanted to share my experience with others. Overall, I found the airbed to be a mixed bag with some positives and negatives.\n    \n    Starting with the positives, the Inflatotron 2000 is incredibly easy to set up and inflate. It comes with a built-in electric pump that quickly inflates the bed within a few minutes, which is a huge plus for anyone who wants to avoid the hassle of manually pumping up their airbed. The bed is also quite comfortable to sleep on and offers decent support for your back, which is a major plus if you have any issues with back pain.\n    \n    On the other hand, I did experience some negatives with the Inflatotron 2000. Firstly, I found that the airbed is not very durable and punctures easily. During my camping trip, the bed got punctured by a stray twig that had fallen on it, which was quite frustrating. Secondly, I noticed that the airbed tends to lose air overnight, which meant that I had to constantly re-inflate it every morning. This was a bit annoying as it disrupted my sleep and made me feel less rested in the morning.\n    \n    Another negative point is that the Inflatotron 2000 is quite heavy and bulky, which makes it difficult to transport and store. If you're planning on using this airbed for camping or other outdoor activities, you'll need to have a large enough vehicle to transport it and a decent amount of storage space to store it when not in use."\
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
          "text": "You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):\n    \n    - Provides good value for the price OR Costs too much\n    - Works better than expected OR Did not work as well as expected\n    - Includes essential features OR Lacks essential features\n    - Easy to use OR Difficult to use\n    - High quality and durability OR Poor quality and durability\n    - Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair\n    - Easy to transport OR Difficult to transport\n    - Easy to store OR Difficult to store\n    - Compatible with other devices or systems OR Not compatible with other devices or systems\n    - Safe and user-friendly OR Unsafe or hazardous to use\n    - Excellent customer support OR Poor customer support\n    - Generous and comprehensive warranty OR Limited or insufficient warranty"\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "I recently purchased the Inflatotron 2000 airbed for a camping trip and wanted to share my experience with others. Overall, I found the airbed to be a mixed bag with some positives and negatives.\n    \n    Starting with the positives, the Inflatotron 2000 is incredibly easy to set up and inflate. It comes with a built-in electric pump that quickly inflates the bed within a few minutes, which is a huge plus for anyone who wants to avoid the hassle of manually pumping up their airbed. The bed is also quite comfortable to sleep on and offers decent support for your back, which is a major plus if you have any issues with back pain.\n    \n    On the other hand, I did experience some negatives with the Inflatotron 2000. Firstly, I found that the airbed is not very durable and punctures easily. During my camping trip, the bed got punctured by a stray twig that had fallen on it, which was quite frustrating. Secondly, I noticed that the airbed tends to lose air overnight, which meant that I had to constantly re-inflate it every morning. This was a bit annoying as it disrupted my sleep and made me feel less rested in the morning.\n    \n    Another negative point is that the Inflatotron 2000 is quite heavy and bulky, which makes it difficult to transport and store. If you're planning on using this airbed for camping or other outdoor activities, you'll need to have a large enough vehicle to transport it and a decent amount of storage space to store it when not in use."\
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
          "text": "You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):\n    \n    - Provides good value for the price OR Costs too much\n    - Works better than expected OR Did not work as well as expected\n    - Includes essential features OR Lacks essential features\n    - Easy to use OR Difficult to use\n    - High quality and durability OR Poor quality and durability\n    - Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair\n    - Easy to transport OR Difficult to transport\n    - Easy to store OR Difficult to store\n    - Compatible with other devices or systems OR Not compatible with other devices or systems\n    - Safe and user-friendly OR Unsafe or hazardous to use\n    - Excellent customer support OR Poor customer support\n    - Generous and comprehensive warranty OR Limited or insufficient warranty"\
        }\
      ]\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "I recently purchased the Inflatotron 2000 airbed for a camping trip and wanted to share my experience with others. Overall, I found the airbed to be a mixed bag with some positives and negatives.\n    \n    Starting with the positives, the Inflatotron 2000 is incredibly easy to set up and inflate. It comes with a built-in electric pump that quickly inflates the bed within a few minutes, which is a huge plus for anyone who wants to avoid the hassle of manually pumping up their airbed. The bed is also quite comfortable to sleep on and offers decent support for your back, which is a major plus if you have any issues with back pain.\n    \n    On the other hand, I did experience some negatives with the Inflatotron 2000. Firstly, I found that the airbed is not very durable and punctures easily. During my camping trip, the bed got punctured by a stray twig that had fallen on it, which was quite frustrating. Secondly, I noticed that the airbed tends to lose air overnight, which meant that I had to constantly re-inflate it every morning. This was a bit annoying as it disrupted my sleep and made me feel less rested in the morning.\n    \n    Another negative point is that the Inflatotron 2000 is quite heavy and bulky, which makes it difficult to transport and store. If you're planning on using this airbed for camping or other outdoor activities, you'll need to have a large enough vehicle to transport it and a decent amount of storage space to store it when not in use."\
        }\
      ]\
    }\
  ],
  "temperature": 1,
  "max_output_tokens": 1024
}
```