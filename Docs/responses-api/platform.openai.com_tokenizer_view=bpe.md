---
url: "https://platform.openai.com/tokenizer?view=bpe"
title: "Tokenizer - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Tokenizer

### Learn about language model tokenization

OpenAI's large language models process text using **tokens**, which are common sequences of characters found in a set of text. The models learn to understand the statistical relationships between these tokens, and excel at producing the next token in a sequence of tokens. [Learn more](https://platform.openai.com/docs/concepts/tokens).

You can use the tool below to understand how a piece of text might be tokenized by a language model, and the total count of tokens in that piece of text.

GPT-4o & GPT-4o miniGPT-3.5 & GPT-4GPT-3 (Legacy)

ClearShow example

Tokens

0

Characters

0

A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words).

If you need a programmatic interface for tokenizing text, check out our [tiktoken](https://github.com/openai/tiktoken) package for Python. For JavaScript, the community-supported [@dbdq/tiktoken](https://www.npmjs.com/package/tiktoken) package works with most GPT models.