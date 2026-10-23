---
title: "Calling open models inside a TEE with the OpenAI Python SDK"
slug: "calling-open-models-inside-a-tee-with-the-openai-python-sdk"
author: "VoltageGPU"
source: "devto_python"
published: "Fri, 23 Oct 2026 16:16:28 +0000"
description: "If you already call OpenAI from Python, switching to an open model that runs in a trusted execution environment (TEE) is two lines: the base URL and the key...."
keywords: "tee, you, model, voltagegpu, openai, what, models, does"
generated: "2026-10-23T16:48:37.613309"
---

# Calling open models inside a TEE with the OpenAI Python SDK

## Overview

If you already call OpenAI from Python, switching to an open model that runs in a trusted execution environment (TEE) is two lines: the base URL and the key. Here is what that looks like, with real output captured on 23 October 2026. The two lines that change from openai import OpenAI import os client = OpenAI ( base_url = " https://api.voltagegpu.com/v1 " , api_key = os . environ [ " VOLTAGEGPU_API_KEY " ], # a vgpu_... key, never commit it ) resp = client . chat . completions . create ( model = " google/gemma-4-31B-turbo-TEE " , messages = [{ " role " : " user " , " content " : " In one sentence, what does a TEE protect? " }], ) print ( resp . choices [ 0 ]. message . content ) Every model id ends in -TEE : the model runs in an Intel TDX guest with confidential-computing NVIDIA GPUs. Streaming works as usual ( stream=True ). What came back x-voltagegpu-model: google/gemma-4-31B-turbo-TEE x-voltagegpu-confidential: tee x-voltagegpu-cost-usd: 0.000025 answer: A TEE protects sensitive data and code from being accessed or modified by the rest of the device's operating system. usage: 36 prompt + 25 completion tokens The response headers tell you which model actually ran and what the call cost, so you can log it next to your own usage. Listing the models GET /v1/models is public and returns, for each model, its live status (available, busy, saturated, unavailable), the price per million tokens and the context length. On 23 October there were 14 models, from small ones such as Mistral Nemo up to Qwen3.5-397B, DeepSeek V3.2 and Kimi K3. What the TEE does and does not give you GET /v1/attestation returns the Intel and NVIDIA evidence of the running instances, bound to a nonce you choose. It proves genuine TDX guests with confidential-computing GPUs. It does not prove which instance served a given response, nor which code runs inside. If you need to check the hardware evidence yourself, offline, the open-source voltage-verify verifies an Intel TDX quote and NVIDIA attestation tokens against a manifest you control. Same thing with LiteLLM, LangChain or LlamaIndex Because the API is OpenAI-compatible, the usual integrations work by pointing them at the base URL. Tested examples for each, with their unedited output, are in the cookbook: github.com/VoltageGPU/voltagegpu-cookbook . Disclosure: I build VoltageGPU.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/voltagegpu/calling-open-models-inside-a-tee-with-the-openai-python-sdk-18k5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
