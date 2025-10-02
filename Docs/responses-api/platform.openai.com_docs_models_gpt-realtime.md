---
url: "https://platform.openai.com/docs/models/gpt-realtime"
title: "Model - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

[Models](https://platform.openai.com/docs/models)

![gpt-realtime](https://cdn.openai.com/API/docs/images/model-page/model-icons/gpt-realtime.png)

gpt-realtime

Default

Model capable of realtime text and audio inputs and outputs

Model capable of realtime text and audio inputs and outputs

CompareTry in Playground

Performance

Highest

Speed

Fast

Price

$4 • $16

Input • Output

Input

Text, audio, image

Output

Text, audio

This is our first general-availability realtime model, capable of responding to audio and text inputs in realtime over WebRTC, WebSocket, or SIP connections.

32,000 context window

4,096 max output tokens

Oct 01, 2023 knowledge cutoff

Pricing

Pricing is based on the number of tokens used. For tool-specific models, like search and computer use, there's a fee per tool call. See details in the [pricing page](https://platform.openai.com/docs/pricing).

Text tokens

Per 1M tokens

Input

$4.00

Cached input

$0.40

Output

$16.00

Audio tokens

Per 1M tokens

Input

$32.00

Cached input

$0.40

Output

$64.00

Image tokens

Per 1M tokens

Input

$5.00

Cached input

$0.50

Modalities

Text

Input and output

Image

Input only

Audio

Input and output

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

Function calling

Supported

Structured outputs

Not supported

Fine-tuning

Not supported

Distillation

Not supported

Predicted outputs

Not supported

Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for gpt-realtime.

![gpt-realtime](https://cdn.openai.com/API/docs/images/model-page/model-icons/gpt-realtime.png)

gpt-realtime

gpt-realtime-2025-08-28

gpt-realtime-2025-08-28

Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests or tokens used within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

| Tier | RPM | RPD | TPM |
| --- | --- | --- | --- |
| Free | Not supported |
| Tier 1 | 200 | 1,000 | 40,000 |
| Tier 2 | 400 | - | 200,000 |
| Tier 3 | 5,000 | - | 800,000 |
| Tier 4 | 10,000 | - | 4,000,000 |
| Tier 5 | 20,000 | - | 15,000,000 |