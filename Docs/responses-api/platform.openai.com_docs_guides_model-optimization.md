---
url: "https://platform.openai.com/docs/guides/model-optimization"
title: "Model optimization - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Model optimization

Ensure quality model outputs with evals and fine-tuning in the OpenAI platform.

Copy page

LLM output is non-deterministic, and model behavior changes between model snapshots and families. Developers must constantly measure and tune the performance of LLM applications to ensure they're getting the best results. In this guide, we explore the techniques and OpenAI platform tools you can use to ensure high quality outputs from the model.

[![Evals](https://cdn.openai.com/API/docs/images/blue_card.png)\\
\\
Evals\\
\\
Systematically measure performance.](https://platform.openai.com/docs/guides/evals) [![Prompt engineering](https://cdn.openai.com/API/docs/images/orange_card.png)\\
\\
Prompt engineering\\
\\
Give context, instructions, and goals.](https://platform.openai.com/docs/guides/text?api-mode=responses#prompt-engineering) [![Fine-tuning](https://cdn.openai.com/API/docs/images/purple_card.png)\\
\\
Fine-tuning\\
\\
Train models to excel at a task.](https://platform.openai.com/docs/guides/supervised-fine-tuning)

## Model optimization workflow

Optimizing model output requires a combination of **evals**, **prompt engineering**, and **fine-tuning**, creating a flywheel of feedback that leads to better prompts and better training data for fine-tuning. The optimization process usually goes something like this.

1. Write [evals](https://platform.openai.com/docs/guides/evals) that measure model output, establishing a baseline for performance and accuracy.
2. [Prompt the model](https://platform.openai.com/docs/guides/text) for output, providing relevant context data and instructions.
3. For some use cases, it may be desirable to [fine-tune](https://platform.openai.com/docs/guides/model-optimization#fine-tune-a-model) a model for a specific task.
4. Run evals using test data that is representative of real world inputs. Measure the performance of your prompt and fine-tuned model.
5. Tweak your prompt or fine-tuning dataset based on eval feedback.
6. Repeat the loop continuously to improve your model results.

Here's an overview of the major steps, and how to do them using the OpenAI platform.

## Build evals

In the OpenAI platform, you can [build and run evals](https://platform.openai.com/docs/guides/evals) either via API or in the [dashboard](https://platform.openai.com/evaluations). You might even consider writing evals _before_ you start writing prompts, taking an approach akin to behavior-driven development (BDD).

Run your evals against test inputs like you expect to see in production. Using one of several available [graders](https://platform.openai.com/docs/guides/graders), measure the results of a prompt against your test data set.

[Learn about evals\\
\\
Run tests on your model outputs to ensure you're getting the right results.](https://platform.openai.com/docs/guides/evals)

## Write effective prompts

With evals in place, you can effectively iterate on [prompts](https://platform.openai.com/docs/guides/text). The prompt engineering process may be all you need in order to get great results for your use case. Different models may require different prompting techniques, but there are several best practices you can apply across the board to get better results.

- **Include relevant context** \- in your instructions, include text or image content that the model will need to generate a response from outside its training data. This could include data from private databases or current, up-to-the-minute information.
- **Provide clear instructions** \- your prompt should contain clear goals about what kind of output you want. GPT models like `gpt-4.1` are great at following very explicit instructions, while [reasoning models](https://platform.openai.com/docs/guides/reasoning) like `o4-mini` tend to do better with high level guidance on outcomes.
- **Provide example outputs** \- give the model a few examples of correct output for a given prompt (a process called few-shot learning). The model can extrapolate from these examples how it should respond for other prompts.

[Learn about prompt engineering\\
\\
Learn the basics of writing good prompts for the model.](https://platform.openai.com/docs/guides/text)

## Fine-tune a model

OpenAI models are already pre-trained to perform across a broad range of subjects and tasks. Fine-tuning lets you take an OpenAI base model, provide the kinds of inputs and outputs you expect in your application, and get a model that excels in the tasks you'll use it for.

Fine-tuning can be a time-consuming process, but it can also enable a model to consistently format responses in a certain way or handle novel inputs. You can use fine-tuning with [prompt engineering](https://platform.openai.com/docs/guides/text) to realize a few more benefits over prompting alone:

- You can provide more example inputs and outputs than could fit within the context window of a single request, enabling the model handle a wider variety of prompts.
- You can use shorter prompts with fewer examples and context data, which saves on token costs at scale and can be lower latency.
- You can train on proprietary or sensitive data without having to include it via examples in every request.
- You can train a smaller, cheaper, faster model to excel at a particular task where a larger model is not cost-effective.

Visit our [pricing page](https://openai.com/api/pricing) to learn more about how fine-tuned model training and usage are billed.

### Fine-tuning methods

These are the fine-tuning methods supported in the OpenAI platform today.

| Method | How it works | Best for | Use with |
| --- | --- | --- | --- |
| [Supervised fine-tuning (SFT)](https://platform.openai.com/docs/guides/supervised-fine-tuning) | Provide examples of correct responses to prompts to guide the model's behavior.<br>Often uses human-generated "ground truth" responses to show the model how it should respond. | - Classification<br>- Nuanced translation<br>- Generating content in a specific format<br>- Correcting instruction-following failures | `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14` |
| [Vision fine-tuning](https://platform.openai.com/docs/guides/vision-fine-tuning) | Provide image inputs for supervised fine-tuning to improve the model's understanding of image inputs. | - Image classification<br>- Correcting failures in instruction following for complex prompts | `gpt-4o-2024-08-06` |
| [Direct preference optimization (DPO)](https://platform.openai.com/docs/guides/direct-preference-optimization) | Provide both a correct and incorrect example response for a prompt. Indicate the correct response to help the model perform better. | - Summarizing text, focusing on the right things<br>- Generating chat messages with the right tone and style | `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14` |
| [Reinforcement fine-tuning (RFT)](https://platform.openai.com/docs/guides/reinforcement-fine-tuning) | Generate a response for a prompt, provide an expert grade for the result, and reinforce the model's chain-of-thought for higher-scored responses.<br>Requires expert graders to agree on the ideal output from the model.<br>**Reasoning models only**. | - Complex domain-specific tasks that require advanced reasoning<br>- Medical diagnoses based on history and diagnostic guidelines<br>- Determining relevant passages from legal case law | `o4-mini-2025-04-16` |

### How fine-tuning works

In the OpenAI platform, you can create fine-tuned models either in the [dashboard](https://platform.openai.com/finetune) or [with the API](https://platform.openai.com/docs/api-reference/fine-tuning). This is the general shape of the fine-tuning process:

1. Collect a dataset of examples to use as training data
2. Upload that dataset to OpenAI, formatted in JSONL
3. Create a fine-tuning job using one of the methods above, depending on your goals—this begins the fine-tuning training process
4. In the case of RFT, you'll also define a grader to score the model's behavior
5. Evaluate the results

Get started with [supervised fine-tuning](https://platform.openai.com/docs/guides/supervised-fine-tuning), [vision fine-tuning](https://platform.openai.com/docs/guides/vision-fine-tuning), [direct preference optimization](https://platform.openai.com/docs/guides/direct-preference-optimization), or [reinforcement fine-tuning](https://platform.openai.com/docs/guides/reinforcement-fine-tuning).

## Learn from experts

Model optimization is a complex topic, and sometimes more art than science. Check out the videos below from members of the OpenAI team on model optimization techniques.

Cost/accuracy/latencyDistillationOptimizing LLM Performance

Cost/accuracy/latency

OpenAI DevDay 2024 \| Balancing accuracy, latency, and cost at scale - YouTube

[Photo image of OpenAI](https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A?embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

OpenAI

1.76M subscribers

[OpenAI DevDay 2024 \| Balancing accuracy, latency, and cost at scale](https://www.youtube.com/watch?v=Bx6sUDRMx-8)

OpenAI

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=Bx6sUDRMx-8&embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

0:00

0:00 / 33:36
•Live

•

Distillation

OpenAI DevDay 2024 \| Tuning powerful small models with distillation - YouTube

[Photo image of OpenAI](https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A?embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

OpenAI

1.76M subscribers

[OpenAI DevDay 2024 \| Tuning powerful small models with distillation](https://www.youtube.com/watch?v=CqWpJFK-hOo)

OpenAI

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=CqWpJFK-hOo&embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

0:00

0:00 / 30:50
•Live

•

Optimizing LLM Performance

A Survey of Techniques for Maximizing LLM Performance - YouTube

[Photo image of OpenAI](https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A?embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

OpenAI

1.76M subscribers

[A Survey of Techniques for Maximizing LLM Performance](https://www.youtube.com/watch?v=ahnGLM-RC1Y)

OpenAI

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=ahnGLM-RC1Y&embeds_referring_euri=https%3A%2F%2Fplatform.openai.com%2F)

0:00

0:00 / 45:32
•Live

•

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all