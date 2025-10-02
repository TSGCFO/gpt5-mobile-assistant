---
url: "https://platform.openai.com/docs/models/gpt-4.1-mini"
title: "Model - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

[Models](https://platform.openai.com/docs/models)

![gpt-4.1-mini](https://cdn.openai.com/API/docs/images/model-page/model-icons/gpt-4.1-mini.png)

GPT-4.1 mini

Default

Smaller, faster version of GPT-4.1

Smaller, faster version of GPT-4.1

CompareTry in Playground

Intelligence

High

Speed

Fast

Price

$0.4 • $1.6

Input • Output

Input

Text, image

Output

Text

GPT-4.1 mini excels at instruction following and tool calling. It features a
1M token context window, and low latency without a reasoning step.

Note that we recommend starting with [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini) for
more complex tasks.

1,047,576 context window

32,768 max output tokens

Jun 01, 2024 knowledge cutoff

Pricing

Pricing is based on the number of tokens used. For tool-specific models, like search and computer use, there's a fee per tool call. See details in the [pricing page](https://platform.openai.com/docs/pricing).

Text tokens

Per 1M tokens

∙

Batch API price

Input

$0.40

Cached input

$0.10

Output

$1.60

Quick comparison

Input

Cached input

Output

GPT-4.1 mini

$0.40

GPT-5 mini

$0.25

GPT-4o mini

$0.15

Modalities

Text

Input and output

Image

Input only

Audio

Not supported

Endpoints

Chat Completions

v1/chat/completions

Responses

v1/responses

Realtime

v1/realtime

Assistants

v1/assistants

Batch

v1/batch

Fine-tuning

v1/fine-tuning

Embeddings

v1/embeddings

Image generation

v1/images/generations

Image edit

v1/images/edits

Speech generation

v1/audio/speech

Transcription

v1/audio/transcriptions

Translation

v1/audio/translations

Moderation

v1/moderations

Completions (legacy)

v1/completions

Features

Streaming

Supported

Function calling

Supported

Structured outputs

Supported

Fine-tuning

Supported

Distillation

Not supported

Predicted outputs

Supported

Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for GPT-4.1 mini.

![gpt-4.1-mini](https://cdn.openai.com/API/docs/images/model-page/model-icons/gpt-4.1-mini.png)

gpt-4.1-mini

gpt-4.1-mini-2025-04-14

gpt-4.1-mini-2025-04-14

Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests or tokens used within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

Long Context

| Tier | RPM | RPD | TPM | Batch queue limit |
| --- | --- | --- | --- | --- |
| Free | 3 | 200 | 40,000 | - |
| Tier 1 | 500 | 10,000 | 200,000 | 2,000,000 |
| Tier 2 | 5,000 | - | 2,000,000 | 20,000,000 |
| Tier 3 | 5,000 | - | 4,000,000 | 40,000,000 |
| Tier 4 | 10,000 | - | 10,000,000 | 1,000,000,000 |
| Tier 5 | 30,000 | - | 150,000,000 | 15,000,000,000 |