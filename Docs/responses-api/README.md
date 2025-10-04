# OpenAI API Reference Documentation

Complete OpenAI API reference documentation from platform.openai.com

**Total Files:** 541 markdown files
**Last Updated:** 2025-10-04
**Source:** https://platform.openai.com/docs/api-reference

---

## 🚨 Critical: Fix for "AsyncOpenAI object has no attribute 'responses'" Error

**Our Current Error:**
```python
ERROR: 'AsyncOpenAI' object has no attribute 'responses'
```

**Solution - See:** [api-reference-responses-create.md](api-reference-responses-create.md)

The Responses API is accessed via:
```python
from openai import AsyncOpenAI

client = AsyncOpenAI()

# Correct usage:
response = await client.responses.create(
    model="gpt-5",
    input="Your message here"
)
```

**Key Documentation Files:**
- [api-reference-responses-create.md](api-reference-responses-create.md) - How to create responses
- [api-reference-responses-streaming-response-output_text.md](api-reference-responses-streaming-response-output_text.md) - Streaming responses
- [api-reference-responses-object.md](api-reference-responses-object.md) - Response object structure

---

## 📁 Documentation Organization

### Responses API (Core)
**Create, retrieve, manage model responses with stateful conversations**

- [api-reference-responses.md](api-reference-responses.md) - Responses API overview
- [api-reference-responses-create.md](api-reference-responses-create.md) - Create response
- [api-reference-responses-get.md](api-reference-responses-get.md) - Retrieve response
- [api-reference-responses-list.md](api-reference-responses-list.md) - List responses
- [api-reference-responses-delete.md](api-reference-responses-delete.md) - Delete response
- [api-reference-responses-cancel.md](api-reference-responses-cancel.md) - Cancel background response
- [api-reference-responses-object.md](api-reference-responses-object.md) - Response object spec

### Streaming Responses
**Server-Sent Events (SSE) for real-time responses**

- [api-reference-responses-streaming.md](api-reference-responses-streaming.md) - Streaming overview
- All `api-reference-responses-streaming-*.md` files - Stream event types

### Conversations API
**Manage stateful conversations**

- [api-reference-conversations.md](api-reference-conversations.md) - Conversations overview
- [api-reference-conversations-create.md](api-reference-conversations-create.md) - Create conversation
- [api-reference-conversations-get.md](api-reference-conversations-get.md) - Retrieve conversation
- [api-reference-conversations-create-items.md](api-reference-conversations-create-items.md) - Add items

### Chat Completions
**Traditional chat completion endpoint (older API)**

- [api-reference-chat.md](api-reference-chat.md) - Chat overview
- [api-reference-chat-create.md](api-reference-chat-create.md) - Create chat completion

### Tools & Extensions
- **Web Search:** [api-reference-tools-web-search.md](api-reference-tools-web-search.md)
- **Code Interpreter:** Search for `code_interpreter` files
- **File Search:** Search for `file_search` files
- **Function Calling:** [api-reference-function-calling.md](api-reference-function-calling.md)

### Models
- [api-reference-models.md](api-reference-models.md) - Models API
- [api-reference-models-list.md](api-reference-models-list.md) - List models
- [api-reference-models-retrieve.md](api-reference-models-retrieve.md) - Get model info

### Images
- [api-reference-images-create.md](api-reference-images-create.md) - Generate images
- [api-reference-images-edit.md](api-reference-images-edit.md) - Edit images
- [api-reference-images-variations.md](api-reference-images-variations.md) - Image variations

### Audio
- [api-reference-audio-speech.md](api-reference-audio-speech.md) - Text-to-speech
- [api-reference-audio-transcription.md](api-reference-audio-transcription.md) - Speech-to-text
- [api-reference-audio-translation.md](api-reference-audio-translation.md) - Audio translation

### Embeddings
- [api-reference-embeddings-create.md](api-reference-embeddings-create.md) - Create embeddings

### Fine-tuning
- [api-reference-fine-tuning.md](api-reference-fine-tuning.md) - Fine-tuning overview
- [api-reference-fine-tuning-jobs-create.md](api-reference-fine-tuning-jobs-create.md) - Create job

### Batch API
- [api-reference-batch.md](api-reference-batch.md) - Batch processing

### Assistants API
- [api-reference-assistants.md](api-reference-assistants.md) - Assistants overview
- All `api-reference-assistants-*.md` and `api-reference-threads-*.md` files

### Realtime API
- [api-reference-realtime.md](api-reference-realtime.md) - Realtime API overview
- All `api-reference-realtime-*.md` files - WebSocket events

### Administration
- [api-reference-admin-api-keys.md](api-reference-admin-api-keys.md) - API key management
- [api-reference-admin-audit-logs.md](api-reference-admin-audit-logs.md) - Audit logs
- [api-reference-admin-invites.md](api-reference-admin-invites.md) - User invites
- [api-reference-admin-projects.md](api-reference-admin-projects.md) - Project management
- [api-reference-admin-rate-limits.md](api-reference-admin-rate-limits.md) - Rate limits
- [api-reference-admin-usage.md](api-reference-admin-usage.md) - Usage tracking

---

## 🔍 Quick Reference: Responses API

### Basic Usage

```python
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="your-api-key")

# Non-streaming
response = await client.responses.create(
    model="gpt-5",
    input="Tell me about quantum computing"
)

# Streaming
stream = await client.responses.create(
    model="gpt-5",
    input="Tell me about quantum computing",
    stream=True
)

async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")
```

### Key Parameters

- **model:** `"gpt-5"`, `"gpt-5-mini"`, etc.
- **input:** Text string or array of message objects
- **stream:** `true` for SSE streaming
- **reasoning:** `{"effort": "low" | "medium" | "high"}` for reasoning models
- **tools:** Array of built-in tools (web_search, code_interpreter, file_search)
- **instructions:** System message
- **conversation:** Conversation ID for stateful multi-turn chats

---

## 📚 All Documentation Files

541 files organized by category. Use file search or grep to find specific topics.

**Search Examples:**
```bash
# Find streaming documentation
ls Docs/responses-api/*streaming*.md

# Find tool documentation
ls Docs/responses-api/*tool*.md

# Find reasoning documentation
grep -l "reasoning" Docs/responses-api/*.md
```

---

## 🔗 External Links

- [OpenAI Platform](https://platform.openai.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python SDK](https://github.com/openai/openai-python)
- [API Changelog](https://platform.openai.com/docs/changelog)
