---
url: "https://platform.openai.com/docs/bots"
title: "Overview of OpenAI Crawlers - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Overview of OpenAI Crawlers

Copy page

OpenAI uses web crawlers (“robots”) and user agents to perform actions for its products, either automatically or triggered by user request. OpenAI uses the following robots.txt tags to enable webmasters to manage how their sites and content work with AI. Each setting is independent of the others – for example, a webmaster can allow OAI-SearchBot to appear in search results while disallowing GPTbot to indicate that crawled content should not be used for training OpenAI’s generative AI foundation models. For search results, please note it can take ~24 hours from a site’s robots.txt update for our systems to adjust.

| User agent | Description & details |
| --- | --- |
| OAI-SearchBot | OAI-SearchBot is for search. OAI-SearchBot is used to link to and surface websites in search results in ChatGPT's search features. It is not used to crawl content to train OpenAI’s generative AI foundation models. To help ensure your site appears in search results, we recommend allowing OAI-SearchBot in your site’s robots.txt file and allowing requests from our published IP ranges below. <br>Full user-agent string will contain `; OAI-SearchBot/1.0; +https://openai.com/searchbot`<br>Published IP addresses: [https://openai.com/searchbot.json](https://openai.com/searchbot.json) |
| ChatGPT-User | ChatGPT-User is for user actions in ChatGPT and [Custom GPTs](https://openai.com/index/introducing-gpts/). When users ask ChatGPT or a CustomGPT a question, it may visit a web page with a ChatGPT-User agent. ChatGPT users may also interact with external applications via [GPT Actions](https://platform.openai.com/docs/actions/introduction). ChatGPT-User is not used for crawling the web in an automatic fashion, nor to crawl content for generative AI training. <br>Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot`<br>Published IP addresses: [https://openai.com/chatgpt-user.json](https://openai.com/chatgpt-user.json) |
| GPTBot | GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site’s content should not be used in training generative AI foundation models. <br>Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot`<br>Published IP addresses: [https://openai.com/gptbot.json](https://openai.com/gptbot.json) |