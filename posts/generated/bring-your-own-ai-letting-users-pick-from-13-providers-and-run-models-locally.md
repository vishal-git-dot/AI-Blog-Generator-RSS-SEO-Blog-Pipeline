---
title: "Bring your own AI: letting users pick from 13 providers (and run models locally)"
slug: "bring-your-own-ai-letting-users-pick-from-13-providers-and-run-models-locally"
author: "Apoorv Darshan"
source: "devto_webdev"
published: "Sat, 20 Jun 2026 14:00:11 +0000"
description: "Most AI apps pick one model for you and bill you for it. In Fud AI (an open-source calorie tracker) I went the other way: the user brings their own key. Why ..."
keywords: "one, fud, provider, device, own, letting, users, pick"
generated: "2026-06-20T14:15:47.239551"
---

# Bring your own AI: letting users pick from 13 providers (and run models locally)

## Overview

Most AI apps pick one model for you and bill you for it. In Fud AI (an open-source calorie tracker) I went the other way: the user brings their own key. Why BYOK Food analysis is a vision + reasoning task that almost every modern model can do. Locking users to one provider means one bill, one rate limit, one point of failure. Letting them choose means cost control, resilience, and privacy — requests go device → provider directly. The provider routing Fud AI routes across 13 providers behind one interface — Gemini, OpenAI, Claude, Grok, Groq, Mistral, OpenRouter, Together, Hugging Face, Fireworks, DeepInfra, plus any OpenAI-compatible endpoint, plus local Ollama . On supported iPhones it can also fall back to on-device Apple Intelligence , so text/voice logging works with no network at all. Lessons A thin provider abstraction + a configurable fallback chain pays off fast. Transient overloads (429/503/529) should auto-retry with backoff so spikes resolve invisibly. On-device fallback is a genuine privacy and resilience feature, not just a nice-to-have. Code: https://github.com/apoorvdarshan/fud-ai · App: https://fud-ai.app

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/apoorvdarshan/bring-your-own-ai-letting-users-pick-from-13-providers-and-run-models-locally-22i6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
