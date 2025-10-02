---
url: "https://platform.openai.com/docs/models/o1-pro"
title: "Model - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

[Models](https://platform.openai.com/docs/models)

![o1-pro](https://cdn.openai.com/API/docs/images/model-page/model-icons/o1-pro.png)

o1-pro

Default

Version of o1 with more compute for better responses

Version of o1 with more compute for better responses

CompareTry in Playground

Reasoning

Higher

Speed

Slowest

Price

$150 • $600

Input • Output

Input

Text, image

Output

Text

The o1 series of models are trained with reinforcement learning to think
before they answer and perform complex reasoning. The o1-pro model uses more
compute to think harder and provide consistently better answers.

o1-pro is available in the [Responses API only](https://platform.openai.com/docs/api-reference/responses)
to enable support for multi-turn model interactions before responding to API
requests, and other advanced API features in the future.

200,000 context window

100,000 max output tokens

Oct 01, 2023 knowledge cutoff

Reasoning token support

Pricing

Pricing is based on the number of tokens used. For tool-specific models, like search and computer use, there's a fee per tool call. See details in the [pricing page](https://platform.openai.com/docs/pricing).

Text tokens

Per 1M tokens

∙

Batch API price

Input

$150.00

Output

$600.00

Quick comparison

Input

Output

o1-pro

$150.00

o1

$15.00

o3-mini

$1.10

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

Not supported

Function calling

Supported

Structured outputs

Supported

Fine-tuning

Not supported

Distillation

Not supported

Predicted outputs

Not supported

Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for o1-pro.

![o1-pro](https://cdn.openai.com/API/docs/images/model-page/model-icons/o1-pro.png)

o1-pro

o1-pro-2025-03-19

o1-pro-2025-03-19

Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests or tokens used within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

| Tier | RPM | TPM | Batch queue limit |
| --- | --- | --- | --- |
| Free | Not supported |
| Tier 1 | 500 | 30,000 | 90,000 |
| Tier 2 | 5,000 | 450,000 | 1,350,000 |
| Tier 3 | 5,000 | 800,000 | 50,000,000 |
| Tier 4 | 10,000 | 2,000,000 | 200,000,000 |
| Tier 5 | 10,000 | 30,000,000 | 5,000,000,000 |