---
url: "https://platform.openai.com/docs/examples/default-memo-writer"
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

## Memo writer

Transform

Natural Language

Generate a company memo based on provided points.

##### Prompt

USER

Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:

Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.

Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).

Project Updates: Provide a brief update on the status of the three ongoing company projects:

a. Project Alpha: 75% complete, expected completion by May 30th.
b. Project Beta: 50% complete, expected completion by June 15th.
c. Project Gamma: 30% complete, expected completion by July 31st.

Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.

Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including "Advanced Customer Service" on May 10th and "Project Management Essentials" on May 25th.

##### Sample response

Dear Team,

I hope this message finds you well. I am writing to remind everyone about the upcoming quarterly review scheduled for the last week of April. This is an important time for us to reflect on our performance and set goals for the next quarter.

During the review, we will be focusing on three key performance indicators (KPIs): sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time). These metrics are crucial in assessing our overall performance and identifying areas for improvement.

I would also like to provide a brief update on the status of our ongoing company projects:

1\. Project Alpha is currently 75% complete, with an expected completion date of May 30th.
2\. Project Beta is 50% complete, and we anticipate it to be finished by June 15th.
3\. Project Gamma is 30% complete, with a projected completion date of July 31st.

I am pleased to announce that the Sales Team was the top-performing team of the past quarter, achieving 120% of their target. Congratulations to the entire team for their exceptional work!

Lastly, I would like to inform everyone about the upcoming training workshops that will be held in May. "Advanced Customer Service" will be on May 10th and "Project Management Essentials" on May 25th. These workshops are excellent opportunities for professional development and skill enhancement.

Thank you for your continued dedication and hard work. Let's keep pushing forward and make the next quarter even more successful.

Best Regards,

\[Your Name\]
\[Your Position\]

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
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4o",
  "input": [\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:\n    \n    Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.\n    \n    Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).\n    \n    Project Updates: Provide a brief update on the status of the three ongoing company projects:\n    \n    a. Project Alpha: 75% complete, expected completion by May 30th.\n    b. Project Beta: 50% complete, expected completion by June 15th.\n    c. Project Gamma: 30% complete, expected completion by July 31st.\n    \n    Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.\n    \n    Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including \"Advanced Customer Service\" on May 10th and \"Project Management Essentials\" on May 25th."\
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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-4o",
  input=[\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:\n    \n    Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.\n    \n    Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).\n    \n    Project Updates: Provide a brief update on the status of the three ongoing company projects:\n    \n    a. Project Alpha: 75% complete, expected completion by May 30th.\n    b. Project Beta: 50% complete, expected completion by June 15th.\n    c. Project Gamma: 30% complete, expected completion by July 31st.\n    \n    Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.\n    \n    Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including \"Advanced Customer Service\" on May 10th and \"Project Management Essentials\" on May 25th."\
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
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = await openai.responses.create({
  model: "gpt-4o",
  input: [\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:\n    \n    Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.\n    \n    Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).\n    \n    Project Updates: Provide a brief update on the status of the three ongoing company projects:\n    \n    a. Project Alpha: 75% complete, expected completion by May 30th.\n    b. Project Beta: 50% complete, expected completion by June 15th.\n    c. Project Gamma: 30% complete, expected completion by July 31st.\n    \n    Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.\n    \n    Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including \"Advanced Customer Service\" on May 10th and \"Project Management Essentials\" on May 25th."\
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
{
  "model": "gpt-4o",
  "input": [\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "input_text",\
          "text": "Draft a company memo to be distributed to all employees. The memo should cover the following specific points without deviating from the topics mentioned and not writing any fact which is not present here:\n    \n    Introduction: Remind employees about the upcoming quarterly review scheduled for the last week of April.\n    \n    Performance Metrics: Clearly state the three key performance indicators (KPIs) that will be assessed during the review: sales targets, customer satisfaction (measured by net promoter score), and process efficiency (measured by average project completion time).\n    \n    Project Updates: Provide a brief update on the status of the three ongoing company projects:\n    \n    a. Project Alpha: 75% complete, expected completion by May 30th.\n    b. Project Beta: 50% complete, expected completion by June 15th.\n    c. Project Gamma: 30% complete, expected completion by July 31st.\n    \n    Team Recognition: Announce that the Sales Team was the top-performing team of the past quarter and congratulate them for achieving 120% of their target.\n    \n    Training Opportunities: Inform employees about the upcoming training workshops that will be held in May, including \"Advanced Customer Service\" on May 10th and \"Project Management Essentials\" on May 25th."\
        }\
      ]\
    }\
  ],
  "temperature": 1,
  "max_output_tokens": 1024
}
```