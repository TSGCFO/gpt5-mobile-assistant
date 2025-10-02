---
url: "https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat"
title: "Web search - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Web search

Allow models to search the web for the latest information before generating a response.

Copy page

Using the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat), you can directly access the fine-tuned models and tool used by [Search in ChatGPT](https://openai.com/index/introducing-chatgpt-search/).

When using Chat Completions, the model always retrieves information from the web before responding to your query. To use `web_search_preview` as a tool that models like `gpt-4o` and `gpt-4o-mini` invoke only when necessary, switch to using the [Responses API](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses).

Currently, you need to use one of these models to use web search in Chat Completions:

- `gpt-4o-search-preview`
- `gpt-4o-mini-search-preview`

Web search parameter example

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
import OpenAI from "openai";
const client = new OpenAI();

const completion = await client.chat.completions.create({
    model: "gpt-4o-search-preview",
    web_search_options: {},
    messages: [{\
        "role": "user",\
        "content": "What was a positive news story from today?"\
    }],
});

console.log(completion.choices[0].message.content);
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
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-search-preview",
    web_search_options={},
    messages=[\
        {\
            "role": "user",\
            "content": "What was a positive news story from today?",\
        }\
    ],
)

print(completion.choices[0].message.content)
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
curl -X POST "https://api.openai.com/v1/chat/completions" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-type: application/json" \
    -d '{
        "model": "gpt-4o-search-preview",
        "web_search_options": {},
        "messages": [{\
            "role": "user",\
            "content": "What was a positive news story from today?"\
        }]
    }'
```

## Output and citations

The API response item in the `choices` array will include:

- `message.content` with the text result from the model, inclusive of any inline citations
- `annotations` with a list of cited URLs

By default, the model's response will include inline citations for URLs found in the web search results. In addition to this, the `url_citation` annotation object will contain the URL and title of the cited source, as well as the start and end index characters in the model's response where those sources were used.

When displaying web results or information contained in web results to end users,
inline citations must be made clearly visible and clickable in your user interface.

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
[\
    {\
        "index": 0,\
        "message": {\
            "role": "assistant",\
            "content": "the model response is here...",\
            "refusal": null,\
            "annotations": [\
                {\
                    "type": "url_citation",\
                    "url_citation": {\
                        "end_index": 985,\
                        "start_index": 764,\
                        "title": "Page title...",\
                        "url": "https://..."\
                    }\
                }\
            ]\
        },\
        "finish_reason": "stop"\
    }\
]
```

## Domain filtering

Domain filtering in web search lets you limit results to a specific set of domains. With the `filters` parameter you can set an allow-list of up to 20 URLs. When formatting URLs, omit the HTTP or HTTPS prefix. For example, use [`openai.com`](http://openai.com/) instead of [`https://openai.com/`](https://openai.com/). This approach also includes subdomains in the search.
Note that domain filtering is only available in the Responses API with the `web_search` tool.

## Sources

To view all URLs retrieved during a web search, use the `sources` field. Unlike inline citations, which show only the most relevant references, sources returns the complete list of URLs the model consulted when forming its response.
The number of sources is often greater than the number of citations. Real-time third-party feeds are also surfaced here and are labeled as `oai-sports`, `oai-weather`, or `oai-finance`. The sources field is available with both the `web_search` and `web_search_preview` tools.

List sources

curl

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
curl "https://api.openai.com/v1/responses" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "gpt-5",
  "reasoning": { "effort": "low" },
  "tools": [\
    {\
      "type": "web_search",\
      "filters": {\
        "allowed_domains": [\
          "pubmed.ncbi.nlm.nih.gov",\
          "clinicaltrials.gov",\
          "www.who.int",\
          "www.cdc.gov",\
          "www.fda.gov"\
        ]\
      }\
    }\
  ],
  "tool_choice": "auto",
  "include": ["web_search_call.action.sources"],
  "input": "Please perform a web search on how semaglutide is used in the treatment of diabetes."
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
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5",
  reasoning: { effort: "low" },
  tools: [\
      {\
          type: "web_search",\
          filters: {\
              allowed_domains: [\
                  "pubmed.ncbi.nlm.nih.gov",\
                  "clinicaltrials.gov",\
                  "www.who.int",\
                  "www.cdc.gov",\
                  "www.fda.gov",\
              ],\
          },\
      },\
  ],
  tool_choice: "auto",
  include: ["web_search_call.action.sources"],
  input: "Please perform a web search on how semaglutide is used in the treatment of diabetes.",
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
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-5",
  reasoning={"effort": "low"},
  tools=[\
      {\
          "type": "web_search",\
          "filters": {\
              "allowed_domains": [\
                  "pubmed.ncbi.nlm.nih.gov",\
                  "clinicaltrials.gov",\
                  "www.who.int",\
                  "www.cdc.gov",\
                  "www.fda.gov",\
              ]\
          },\
      }\
  ],
  tool_choice="auto",
  include=["web_search_call.action.sources"],
  input="Please perform a web search on how semaglutide is used in the treatment of diabetes.",
)

print(response.output_text)
```

## User location

To refine search results based on geography, you can specify an approximate user location using country, city, region, and/or timezone.

- The `city` and `region` fields are free text strings, like `Minneapolis` and `Minnesota` respectively.
- The `country` field is a two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1), like `US`.
- The `timezone` field is an [IANA timezone](https://timeapi.io/documentation/iana-timezones) like `America/Chicago`.

Note that user location is not supported for deep research models using web search.

Customizing user location

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
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-search-preview",
    web_search_options={
        "user_location": {
            "type": "approximate",
            "approximate": {
                "country": "GB",
                "city": "London",
                "region": "London",
            }
        },
    },
    messages=[{\
        "role": "user",\
        "content": "What are the best restaurants around Granary Square?",\
    }],
)

print(completion.choices[0].message.content)
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
import OpenAI from "openai";
const client = new OpenAI();

const completion = await client.chat.completions.create({
    model: "gpt-4o-search-preview",
    web_search_options: {
        user_location: {
            type: "approximate",
            approximate: {
                country: "GB",
                city: "London",
                region: "London",
            },
        },
    },
    messages: [{\
        "role": "user",\
        "content": "What are the best restaurants around Granary Square?",\
    }],
});
console.log(completion.choices[0].message.content);
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
curl -X POST "https://api.openai.com/v1/chat/completions" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-type: application/json" \
    -d '{
        "model": "gpt-4o-search-preview",
        "web_search_options": {
            "user_location": {
                "type": "approximate",
                "approximate": {
                    "country": "GB",
                    "city": "London",
                    "region": "London"
                }
            }
        },
        "messages": [{\
            "role": "user",\
            "content": "What are the best restaurants around Granary Square?"\
        }]
    }'
```

## API compatibility

Web search is available in the Responses API as the generally available version of the tool, `web_search`, as well as the earlier tool version, `web_search_preview`.
To use web search in the Chat Completions API, use the specialized web search models `gpt-4o-search-preview` and `gpt-4o-mini-search-preview`.

## Limitations

- Web search is currently not supported in [`gpt-5`](https://platform.openai.com/docs/models/gpt-5) with `minimal` reasoning, and [`gpt-4.1-nano`](https://platform.openai.com/docs/models/gpt-4.1-nano).
- When used as a tool in the [Responses API](https://platform.openai.com/docs/api-reference/responses), web search has the same tiered rate limits as the models above.
- Web search is limited to a context window size of 128000 (even with [`gpt-4.1`](https://platform.openai.com/docs/models/gpt-4.1) and [`gpt-4.1-mini`](https://platform.openai.com/docs/models/gpt-4.1-mini) models).

## Usage notes

| API Availability | Rate limits | Notes |
| --- | --- | --- |
| [Responses](https://platform.openai.com/docs/api-reference/responses)<br>[Chat Completions](https://platform.openai.com/docs/api-reference/chat)<br>[Assistants](https://platform.openai.com/docs/api-reference/assistants) | Same as tiered rate limits for underlying [model](https://platform.openai.com/docs/models) used with the<br>tool. | [Pricing](https://platform.openai.com/docs/pricing#built-in-tools)<br>[ZDR and data residency](https://platform.openai.com/docs/guides/your-data) |

Chat Completions