---
title: "Ollama: Run LLMs Locally and Swap Them Into Your App With One base_url Change"
slug: "ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change"
author: "M.T.Ramkrushna"
source: "devto_python"
published: "Thu, 22 Oct 2026 04:02:10 +0000"
description: "This week's AI tool: Ollama , the simplest way I know to run open-weight LLMs on your own machine and call them from code. Why it's worth 15 minutes of your ..."
keywords: "ollama, model, you, your, openai, ticket, local, models"
generated: "2026-10-22T04:08:58.348930"
---

# Ollama: Run LLMs Locally and Swap Them Into Your App With One base_url Change

## Overview

This week's AI tool: Ollama , the simplest way I know to run open-weight LLMs on your own machine and call them from code. Why it's worth 15 minutes of your time: most of the LLM calls you make while building (trying prompts, running unit tests, iterating on a parser) don't need a frontier model. They need something fast, free, and available offline. Ollama gives you that, and because it speaks an OpenAI-compatible API, the same client code can point at a local model in dev and a hosted model in production. Here's exactly how to use it. 1. Install and pull a model On Linux: curl -fsSL https://ollama.com/install.sh | sh On macOS and Windows, download the app from ollama.com/download . Then pull a model from the model library and chat with it: ollama pull llama3.2 ollama run llama3.2 A few commands you'll use daily: ollama list # models you've downloaded ollama ps # models currently loaded in memory ollama rm llama3.2 # free the disk space How big a model can you run? The Ollama README gives this rule of thumb: at least 8 GB of RAM for 7B models, 16 GB for 13B, and 32 GB for 33B. Start small (a 3B model) and move up only if quality isn't enough for your task. 2. Call it from Python Ollama runs a local server at http://localhost:11434 . The official Python library is the most direct way in: pip install ollama from ollama import chat response = chat ( model = " llama3.2 " , messages = [{ " role " : " user " , " content " : " Explain idempotency in one sentence. " }], ) print ( response . message . content ) 3. Or keep your OpenAI client and change one line Ollama also exposes an OpenAI-compatible endpoint at /v1 . If your app already uses the OpenAI SDK, you don't rewrite anything: from openai import OpenAI client = OpenAI ( base_url = " http://localhost:11434/v1 " , api_key = " ollama " , # required by the SDK, ignored by Ollama ) resp = client . chat . completions . create ( model = " llama3.2 " , messages = [{ " role " : " user " , " content " : " Summarize: the deploy failed because the DB migration timed out. " }], ) print ( resp . choices [ 0 ]. message . content ) Put base_url and model in config, and the same code runs against a local model on your laptop and a hosted model in production. 4. Get structured output you can validate Free-text answers are hard to test. Ollama supports structured outputs : pass a JSON schema in format and the model's reply is constrained to it. Pair it with Pydantic: from ollama import chat from pydantic import BaseModel class Ticket ( BaseModel ): category : str priority : str summary : str response = chat ( model = " llama3.2 " , messages = [{ " role " : " user " , " content " : " Customer says checkout returns a 500 error since this morning. " }], format = Ticket . model_json_schema (), options = { " temperature " : 0 }, ) ticket = Ticket . model_validate_json ( response . message . content ) print ( ticket ) Setting temperature to 0 makes runs more repeatable, which matters when the output feeds a test. 5. Pin your settings in a Modelfile Instead of repeating the system prompt and parameters everywhere, bake them into a named model with a Modelfile : FROM llama3.2 PARAMETER temperature 0 SYSTEM You classify support tickets. Reply only with the requested JSON. ollama create ticket-bot -f Modelfile ollama run ticket-bot Now every teammate gets the same model, prompt, and parameters by name, and the Modelfile lives in version control next to your code. The workflow I'd use Here's a hypothetical setup for a support-ticket classifier, to show how the pieces fit: Local dev: base_url points at Ollama with a small model. You iterate on prompts and parsing as often as you like, offline, with no API bill. Tests: the Pydantic schema plus temperature 0 give you outputs you can assert on (valid JSON, allowed categories). Production: change base_url and model in config to your hosted provider. The code doesn't change. Before shipping: run the same eval set against the production model, because a small local model passing isn't proof the big one behaves the same way (and vice versa). Where Ollama is not the answer Quality-critical answers: small local models are weaker than frontier models. Use them for dev loops and simple tasks, not as a silent drop-in for hard reasoning. Serving many users: Ollama is built for running models on a machine you control. For high-traffic production serving, look at dedicated inference servers or hosted APIs. Hardware limits: if a model doesn't fit in memory it will be slow or won't load. Check ollama ps and pick a smaller model. References Ollama website and model library Ollama on GitHub (README, install, RAM guidance) OpenAI compatibility docs Structured outputs announcement Modelfile reference ollama-python library What do you use local models for today: dev loops, tests, privacy-sensitive data, or not at all yet?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/m_t_ramkrushna/ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change-oab

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
