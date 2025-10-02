---
url: "https://platform.openai.com/docs/changelog/changelog"
title: "Changelog - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Changelog

### September, 2025

Sep 23

Feature

gpt-5-codex

v1/responses

Launched special-purpose model [gpt-5-codex](https://platform.openai.com/docs/models/gpt-5-codex), built and optimized for use with the [Codex CLI](https://github.com/openai/codex).

### August, 2025

Aug 28

Feature

v1/realtime

The OpenAI Realtime API is now generally available. Learn more [in our Realtime API guide](https://platform.openai.com/docs/guides/realtime).

Aug 21

Feature

v1/responses

Added support for [connectors](https://platform.openai.com/docs/guides/tools-connectors-mcp) to the Responses API. Connectors are OpenAI-maintained MCP wrappers for popular services like Google apps, Dropbox, and more that can be used to give model read access to data stored in those services.

Aug 20

Feature

v1/conversations

v1/responses

v1/assistants

Released the Conversations API, which allows you to create and manage long-running conversations with the Responses API. See the [migration guide](https://platform.openai.com/docs/assistants/migration) to see a side-by-side comparison and learn how to migrate from an Assistants API integration to Responses and Conversations.

Aug 7

Feature

v1/chat/completions

v1/responses

Released GPT-5 family of models in the API, including [`gpt-5`](https://platform.openai.com/docs/models/gpt-5), [`gpt-5-mini`](https://platform.openai.com/docs/models/gpt-5-mini), and [`gpt-5-nano`](https://platform.openai.com/docs/models/gpt-5-nano).

Introduced the `minimal` [reasoning effort](https://platform.openai.com/docs/guides/reasoning) value to optimize for fast responses in GPT-5 models (which support reasoning).

Introduced `custom` [tool call](https://platform.openai.com/docs/guides/function-calling#custom-tools) type, which allows for freeform inputs to and outputs from the model when tool calling.

### June, 2025

Jun 24

Feature

o3-deep-research

o3-deep-research-2025-06-26

o4-mini-deep-research

o4-mini-deep-research-2025-06-26

v1/responses

Released [o3-deep-research](https://platform.openai.com/docs/models/o3-deep-research) and [o4-mini-deep-research](https://platform.openai.com/docs/models/o4-mini-deep-research), deep research variants of our o-series reasoning models optimized for deep analysis and research tasks. Learn more in the [deep research guide](https://platform.openai.com/docs/guides/deep-research).

Added support for async event handling with [webhooks](https://platform.openai.com/docs/guides/webhooks). [Reduced and simplified pricing](https://platform.openai.com/docs/pricing) for the web search tool. Added support for the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Jun 13

Feature

v1/responses

[New reusable prompts](https://platform.openai.com/chat/edit) are now available in the dashboard and [Responses API](https://platform.openai.com/docs/api-reference/responses/create). Via API, you can now reference templates created in the dashboard via the `prompt` parameter (with a prompt `id`, optional `version`) and supply dynamic `variables` that can include strings, images, or file inputs. Reusable prompts are not available in Chat Completions. [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

Jun 10

Feature

o3-pro

v1/responses

v1/batch

Released [o3-pro](https://platform.openai.com/docs/models/o3-pro), a version of the [o3](https://platform.openai.com/docs/models/o3) reasoning model that uses more compute to answer hard problems with better reasoning and consistency. [Prices for the o3 model have also been reduced](https://platform.openai.com/docs/pricing) for all API requests, including batch and flex processing.

Jun 4

Feature

v1/fine\_tuning

Added fine-tuning support with [direct preference optimization](https://platform.openai.com/docs/guides/direct-preference-optimization) for the models `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, and `gpt-4.1-nano-2025-04-14`.

Jun 3

Feature

v1/chat/completions

v1/realtime

New model snapshots available for [gpt-4o-audio-preview](https://platform.openai.com/docs/models/gpt-4o-audio-preview) and [gpt-4o-realtime-preview](https://platform.openai.com/docs/models/gpt-4o-realtime-preview). Released [Agents SDK for TypeScript](https://openai.github.io/openai-agents-js).

### May, 2025

May 20

Feature

v1/responses

Added support for new built-in tools in the Responses API, including [remote MCP servers](https://platform.openai.com/docs/guides/tools-remote-mcp) and [code interpreter](https://platform.openai.com/docs/guides/tools-code-interpreter). [Learn more about tools](https://platform.openai.com/docs/guides/tools).

May 20

Feature

v1/responses

v1/chat/completions

Added support for using `strict` mode for tool schemas when using parallel tool calling with non-fine-tuned models.
Added new [schema features](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses#supported-schemas), including string validation for `email` and other patterns and specifying ranges for numbers and arrays.

May 15

Feature

codex-mini-latest

v1/responses

v1/chat/completions

Launched [codex-mini-latest](https://platform.openai.com/docs/models/codex-mini-latest) in the API, optimized for use with the [Codex CLI](https://github.com/openai/codex).

May 7

Feature

v1/fine-tuning

v1/responses

v1/chat/completions

Launched support for [reinforcement fine-tuning](https://platform.openai.com/docs/guides/reinforcement-fine-tuning). Learn about available [fine-tuning methods](https://platform.openai.com/docs/guides/fine-tuning). [gpt-4.1-nano](https://platform.openai.com/docs/models/gpt-4.1-nano) is now available for fine-tuning.

### April, 2025

Apr 23

Feature

v1/images/generations

v1/images/edits

Added a new image generation model, `gpt-image-1`. This model sets a new standard for image generation, with improved quality and instruction following.

Updated the Image Generation and Edit endpoints to support new parameters specific to the `gpt-image-1` model.

Apr 16

Feature

v1/chat/completions

v1/responses

Added two new o-series reasoning models, `o3` and `o4-mini`. They set a new standard for math, science, and coding, visual reasoning tasks, and technical writing.

Launched Codex, our code generation CLI tool.

Apr 14

Feature

gpt-4.1

gpt-4.1-mini

gpt-4.1-nano

v1/responses

v1/chat/completions

v1/fine\_tuning

Added [`gpt-4.1`](https://platform.openai.com/docs/models/gpt-4.1), [`gpt-4.1-mini`](https://platform.openai.com/docs/models/gpt-4.1-mini), and [`gpt-4.1-nano`](https://platform.openai.com/docs/models/gpt-4.1-nano) models to the API. These new models feature improved instruction following, coding, and a larger context window (up to 1M tokens). `gpt-4.1` and `gpt-4.1-mini` are available for supervised fine-tuning. Announced deprecation of [`gpt-4.5-preview`](https://platform.openai.com/docs/deprecations).

### March, 2025

Mar 20

Update

v1/audio

Added `gpt-4o-mini-tts`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `whisper-1` models to the Audio API.

Mar 19

Feature

o1-pro

v1/responses

v1/batch

Released [o1-pro](https://platform.openai.com/docs/models/o1-pro), a version of the [o1](https://platform.openai.com/docs/models/o1) reasoning model that uses more compute to answer hard problems with better reasoning and consistency.

Mar 11

Feature

gpt-4o-search-preview

gpt-4o-mini-search-preview

computer-use-preview

v1/chat/completions

v1/assistants

v1/responses

Released several new models and tools and a new API for agentic workflows:

- Released the [Responses API](https://platform.openai.com/docs/guides/responses-vs-chat-completions), a new API for creating and using agents and tools.
- Released a set of built-in tools for the Responses API: [web search](https://platform.openai.com/docs/guides/tools-web-search), [file search](https://platform.openai.com/docs/guides/tools-file-search), and [computer use](https://platform.openai.com/docs/guides/tools-computer-use).
- Released the [Agents SDK](https://platform.openai.com/docs/guides/agents), an orchestration framework for designing, building, and deploying agents.
- Announced new models: `gpt-4o-search-preview`, `gpt-4o-mini-search-preview`, `computer-use-preview`.
- Announced plans to bring all [Assistants API](https://platform.openai.com/docs/assistants) features to the easier to use [Responses API](https://platform.openai.com/docs/guides/responses-vs-chat-completions), with an anticipated sunset date for Assistants in 2026 (after achieving full feature parity).

Mar 3

Feature

v1/fine\_tuning/jobs

Added `metadata` field support to fine-tuning jobs.

### February, 2025

Feb 27

Feature

GPT-4.5

v1/chat/completions

v1/assistants

v1/batch

Released a research preview of [GPT-4.5](https://platform.openai.com/docs/models/gpt-4-5)—our largest and most capable chat model yet. GPT-4.5's high "EQ" and understanding of user intent make it better at creative tasks and agentic planning.

### January, 2025

Jan 31

Feature

o3-mini

o3-mini-2025-01-31

v1/chat/completions

Launched [o3-mini](https://platform.openai.com/docs/models/o3-mini), a new small reasoning model that is optimized for science, math, and coding tasks.

### December, 2024

Dec 18

Feature

Launched [Admin API Key Rotations](https://platform.openai.com/docs/api-reference/admin-api-keys), enabling customers to programmatically rotate their admin api keys.

Updated [Admin API Invites](https://platform.openai.com/docs/api-reference/invite), enabling customers to programmatically invite users to projects at the same time they are invited to organizations.

Dec 17

Feature

o1

gpt-4o

gpt-4o-mini

v1/fine\_tuning

v1/chat/completions

v1/realtime

Added new models for [o1](https://platform.openai.com/docs/models/o1), [gpt-4o-realtime](https://platform.openai.com/docs/models/gpt-4o-realtime-preview), [gpt-4o-audio](https://platform.openai.com/docs/models/gpt-4o-audio-preview) and [more](https://platform.openai.com/docs/models).

Added WebRTC connection method for the [Realtime API](https://platform.openai.com/docs/guides/realtime).

Added [`reasoning_effort` parameter](https://platform.openai.com/docs/api-reference/chat/create#chat-create-reasoning_effort) for o1 models.

Added [`developer` message role](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages) for o1 model. Note that o1-preview and o1-mini do not support system or developer messages.

Launched Preference Fine-tuning using [Direct Preference Optimization (DPO)](https://platform.openai.com/docs/guides/fine-tuning#preference).

Launched beta SDKs for Go and Java. [Learn more](https://platform.openai.com/docs/libraries).

Added [Realtime API](https://platform.openai.com/docs/guides/realtime) support in the [Python SDK](https://github.com/openai/openai-python).

Dec 4

Feature

Launched [Usage API](https://platform.openai.com/docs/api-reference/usage), enabling customers to programmatically query activities and spending across OpenAI APIs.

### November, 2024

Nov 20

Update

v1/chat/completions

Released [gpt-4o-2024-11-20](https://platform.openai.com/docs/models/gpt-4o), our newest model in the gpt-4o series.

Nov 4

Feature

v1/chat/completions

Released [Predicted Outputs](https://platform.openai.com/docs/guides/predicted-outputs), which greatly reduces latency for model responses where much of the response is known ahead of time. This is most common when regenerating the content of documents and code files with only minor changes.

### October, 2024

Oct 30

Feature

gpt-4o-realtime-preview

gpt-4o-audio-preview

v1/chat/completions

Added five new voice types in the [Realtime API](https://platform.openai.com/docs/guides/realtime) and [Chat Completions API](https://platform.openai.com/docs/guides/audio).

Oct 17

Feature

gpt-4o-audio-preview

v1/chat/completions

Released [new `gpt-4o-audio-preview` model](https://platform.openai.com/docs/guides/audio) for chat completions, which supports both audio inputs and outputs. Uses the same underlying model as the [Realtime API](https://platform.openai.com/docs/guides/realtime).

Oct 1

Feature

v1/realtime

v1/chat/completions

v1/fine\_tuning

Released several new features at [OpenAI DevDay in San Francisco](https://openai.com/devday/):

[Realtime API](https://platform.openai.com/docs/guides/realtime): Build fast speech-to-speech experiences into your applications using a WebSockets interface.

[Model distillation](https://platform.openai.com/docs/guides/distillation): Platform for fine-tuning cost-efficient models with your outputs from a large frontier model.

[Image fine-tuning](https://platform.openai.com/docs/guides/fine-tuning#vision): Fine-tune GPT-4o with images and text to improve vision capabilities.

[Evals](https://platform.openai.com/docs/guides/evals): Create and run custom evaluations to measure model performance on specific tasks.

[Prompt caching](https://platform.openai.com/docs/guides/prompt-caching): Discounts and faster processing times on recently seen input tokens.

[Generate in playground](https://platform.openai.com/chat/edit): Easily generate prompts, function definitions, and structured output schemas in the playground using the Generate button.

### September, 2024

Sep 26

Feature

omni-moderation-latest

v1/moderations

Released [new `omni-moderation-latest` moderation model](https://platform.openai.com/docs/guides/moderation), which supports both images and text (for some categories), supports two new text-only harm categories, and has more accurate scores.

Sep 12

Feature

o1-preview

o1-mini

v1/chat/completions

Released [o1-preview and o1-mini](https://platform.openai.com/docs/guides/reasoning), new large language models trained with reinforcement learning to perform complex reasoning tasks.

### August, 2024

Aug 29

Feature

v1/assistants

Assistants API now supports [including file search results used by the file search tool, and customizing ranking behavior](https://platform.openai.com/docs/assistants/tools/file-search#improve-file-search-result-relevance-with-chunk-ranking).

Aug 20

Feature

gpt-4o

v1/fine\_tuning

GA release for [`gpt-4o-2024-08-06` fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)—all API users can now fine-tune the latest GPT-4o model.

Aug 15

Update

gpt-4o

v1/chat/completions

Released [dynamic model for `chatgpt-4o-latest`](https://platform.openai.com/docs/models/chatgpt-4o-latest)—this model will point to the latest GPT-4o model used by ChatGPT.

Aug 6

Update

Launched [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)—model outputs now reliably adhere to developer supplied JSON Schemas.

Released [gpt-4o-2024-08-06](https://platform.openai.com/docs/models/gpt-4o), our newest model in the gpt-4o series.

Aug 1

Update

Launched [Admin and Audit Log APIs](https://platform.openai.com/docs/api-reference/administration), allowing customers to programmatically administer their organization and monitor changes using the audit logs. Audit logging must be enabled within [settings](https://platform.openai.com/docs/changelog/changelog).

### July, 2024

Jul 24

Update

Launched [self-serve SSO configuration](https://help.openai.com/en/articles/9641482-api-platform-single-sign-on-sso-integration-for-existing-enterprise-customers), allowing Enterprise customers on custom and unlimited billing to set up authentication against their desired IDP.

Jul 23

Update

Launched [fine-tuning for GPT-4o mini](https://platform.openai.com/docs/guides/fine-tuning), enabling even higher performance for specific use cases.

Jul 18

Update

Released [GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini), our affordable an intelligent small model for fast, lightweight tasks.

Jul 17

Update

Released [Uploads](https://platform.openai.com/docs/api-reference/uploads) to upload large files in multiple parts.

### June, 2024

Jun 6

Update

[Parallel function calling](https://platform.openai.com/docs/guides/function-calling#configure-parallel-function-calling) can be disabled in Chat Completions and the Assistants API by passing `parallel_tool_calls=false`.

[.NET SDK](https://platform.openai.com/docs/libraries#dotnet-library) launched in Beta.

Jun 3

Update

Added support for [file search customizations](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings).

### May, 2024

May 15

Update

Added support for [archiving projects](https://platform.openai.com/projects) . Only organization owners can access this functionality.

Added support for [setting cost limits](https://platform.openai.com/settings/organization/general) on a per-project basis for pay as you go customers.

May 13

Update

Released [GPT-4o](https://platform.openai.com/docs/models/gpt-4o) in the API. GPT-4o is our fastest and most affordable flagship model.

May 9

Update

Added support for [image inputs to the Assistants API.](https://platform.openai.com/docs/assistants/overview)

May 7

Update

Added support for [fine-tuned models to the Batch API](https://platform.openai.com/docs/guides/batch#model-availability) .

May 6

Update

Added [`stream_options: {"include_usage": true}`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_options) parameter to the Chat Completions and Completions APIs. Setting this gives developers access to usage stats when using streaming.

May 2

Update

Added [a new endpoint](https://platform.openai.com/docs/api-reference/messages/deleteMessage) to delete a message from a thread in the Assistants API.

### April, 2024

Apr 29

Update

Added a new [function calling option `tool_choice: "required"`](https://platform.openai.com/docs/guides/function-calling#function-calling-behavior) to the Chat Completions and Assistants APIs.

Added a [guide for the Batch API](https://platform.openai.com/docs/guides/batch) and Batch API support for [embeddings models](https://platform.openai.com/docs/guides/batch#model-availability)

Apr 17

Update

Introduced a [series of updates to the Assistants API](https://platform.openai.com/docs/assistants/whats-new) , including a new file search tool allowing up to 10,000 files per assistant, new token controls, and support for tool choice.

Apr 16

Update

Introduced [project based hierarchy](https://platform.openai.com/docs/changelog/changelog) for organizing work by projects, including the ability to create [API keys](https://platform.openai.com/docs/api-reference/authentication) and manage rate and cost limits on a per-project basis (cost limits available only for Enterprise customers).

Apr 15

Update

Released [Batch API](https://platform.openai.com/docs/guides/batch)

Apr 9

Update

Released [GPT-4 Turbo with Vision](https://platform.openai.com/docs/models/gpt-4-turbo) in general availability in the API

Apr 4

Update

Added support for [seed](https://platform.openai.com/docs/api-reference/fine-tuning/create) in the fine-tuning API

Added support for [checkpoints](https://platform.openai.com/docs/api-reference/fine-tuning/list-checkpoints) in the fine-tuning API

Added support for [adding Messages when creating a Run](https://platform.openai.com/docs/api-reference/runs/createRun#runs-createrun-additional_messages) in the Assistants API

Apr 1

Update

Added support for [filtering Messages by run\_id](https://platform.openai.com/docs/api-reference/messages/listMessages#messages-listmessages-run_id) in the Assistants API

### March, 2024

Mar 29

Update

Added support for [temperature](https://platform.openai.com/docs/api-reference/runs/createRun#runs-createrun-temperature) and [assistant message creation](https://platform.openai.com/docs/api-reference/messages/createMessage#messages-createmessage-role) in the Assistants API

Mar 14

Update

Added support for [streaming](https://platform.openai.com/docs/assistants/overview) in the Assistants API

### February, 2024

Feb 9

Update

Added [`timestamp_granularities` parameter](https://platform.openai.com/docs/guides/speech-to-text#timestamps) to the Audio API

Feb 1

Update

Released [gpt-3.5-turbo-0125, an updated GPT-3.5 Turbo model](https://platform.openai.com/docs/models/gpt-3-5-turbo)

### January, 2024

Jan 25

Update

Released embedding V3 models and an updated GPT-4 Turbo preview

Added [`dimensions` parameter](https://platform.openai.com/docs/api-reference/embeddings/create#embeddings-create-dimensions) to the Embeddings API

### December, 2023

Dec 20

Update

Added [`additional_instructions` parameter](https://platform.openai.com/docs/api-reference/runs/createRun#runs-createrun-additional_instructions) to run creation in the Assistants API

Dec 15

Update

Added [`logprobs` and `top_logprobs` parameters](https://platform.openai.com/docs/api-reference/chat/create#chat-create-logprobs) to the Chat Completions API

Dec 14

Update

Changed [function parameters](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools) argument on a tool call to be optional

### November, 2023

Nov 30

Update

Released [OpenAI Deno SDK](https://deno.land/x/openai)

Nov 6

Update

Released [GPT-4 Turbo Preview](https://platform.openai.com/docs/models/gpt-4-turbo), [updated GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo), [GPT-4 Turbo with Vision](https://platform.openai.com/docs/guides/vision), [Assistants API](https://platform.openai.com/docs/assistants/overview), [DALL·E 3 in the API](https://platform.openai.com/docs/models/dall-e-3), and [text-to-speech API](https://platform.openai.com/docs/guides/text-to-speech)

Deprecated the Chat Completions `functions` parameter [in favor of `tools`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)

Released [OpenAI Python SDK V1.0](https://platform.openai.com/docs/libraries#python-library)

### October, 2023

Oct 16

Update

Added [`encoding_format` parameter](https://platform.openai.com/docs/api-reference/embeddings/create#embeddings-create-encoding_format) to the Embeddings API

Added `max_tokens` to the [Moderation models](https://platform.openai.com/docs/models/text-moderation-latest)

Oct 6

Update

Added [function calling support](https://platform.openai.com/docs/guides/fine-tuning#fine-tuning-examples) to the Fine-tuning API