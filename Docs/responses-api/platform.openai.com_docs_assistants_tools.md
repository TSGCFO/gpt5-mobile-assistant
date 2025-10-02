---
url: "https://platform.openai.com/docs/assistants/tools"
title: "Assistants API tools - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Assistants API tools  Deprecated

Explore tools for file search, code, and function calling.

Copy page

After achieving feature parity in the Responses API, we've deprecated the Assistants API. It will shut down on August 26, 2026. Follow the [migration guide](https://platform.openai.com/docs/assistants/migration) to update your integration. [Learn more](https://platform.openai.com/docs/guides/responses-vs-chat-completions).

## Overview

Assistants created using the Assistants API can be equipped with tools that allow them to perform more complex tasks or interact with your application.
We provide built-in tools for assistants, but you can also define your own tools to extend their capabilities using Function Calling.

The Assistants API currently supports the following tools:

[File Search\\
\\
Built-in RAG tool to process and search through files](https://platform.openai.com/docs/assistants/tools/file-search) [Code Interpreter\\
\\
Write and run python code, process files and diverse data](https://platform.openai.com/docs/assistants/tools/code-interpreter) [Function Calling\\
\\
Use your own custom functions to interact with your application](https://platform.openai.com/docs/assistants/tools/function-calling)

## Next steps

- See the API reference to [submit tool outputs](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs)
- Build a tool-using assistant with our [Quickstart app](https://github.com/openai/openai-assistants-quickstart)