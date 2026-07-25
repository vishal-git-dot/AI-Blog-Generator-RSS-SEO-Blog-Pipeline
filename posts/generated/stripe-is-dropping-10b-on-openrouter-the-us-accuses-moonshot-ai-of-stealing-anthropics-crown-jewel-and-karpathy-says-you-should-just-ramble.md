---
title: "Stripe Is Dropping $10B on OpenRouter, the US Accuses Moonshot AI of Stealing Anthropic's Crown Jewel, and Karpathy Says You Should Just Ramble"
slug: "stripe-is-dropping-10b-on-openrouter-the-us-accuses-moonshot-ai-of-stealing-anthropics-crown-jewel-and-karpathy-says-you-should-just-ramble"
author: "AI Pulse"
source: "devto_ai"
published: "Sat, 25 Jul 2026 03:14:39 +0000"
description: "Stripe Is Dropping $10B on OpenRouter, the US Accuses Moonshot AI of Stealing Anthropic's Crown Jewel, and Karpathy Says You Should Just Ramble The past few ..."
keywords: "you, model, openrouter, stripe, moonshot, should, just, something"
generated: "2026-07-25T03:16:45.367495"
---

# Stripe Is Dropping $10B on OpenRouter, the US Accuses Moonshot AI of Stealing Anthropic's Crown Jewel, and Karpathy Says You Should Just Ramble

## Overview

Stripe Is Dropping $10B on OpenRouter, the US Accuses Moonshot AI of Stealing Anthropic's Crown Jewel, and Karpathy Says You Should Just Ramble The past few days have been a lot. Let me untangle it. Stripe buying OpenRouter for roughly $10 billion is the kind of deal that makes you stop scrolling. The WSJ broke it — Stripe is in advanced talks to acquire the three-year-old LLM marketplace, and the price tag is somewhere around $10B. That's almost 8x its last reported valuation of $1.3B from CapitalG's round back in May. For context, OpenRouter is basically the Kayak of AI models. You go there, you compare 400+ LLMs from ~70 providers, you pick the one that fits your budget and latency needs. It handles routing, billing, fallbacks — the whole messy plumbing of "which model should I call right now." Stripe already processes OpenRouter's payments. They've been partners since early this year. So the acquisition makes sense on paper — Stripe gets a captive AI workload generator that feeds directly into its payment rails, and OpenRouter gets the financial infrastructure to scale without constantly rebuilding billing logic. But $10B for a marketplace that's basically a thin API layer? To be fair, the value isn't in the code. It's in the routing intelligence and the user base. OpenRouter has become the default entry point for a lot of indie devs and small teams who don't want to manage 17 API keys. That distribution is worth something. Whether it's worth $10B is another question — I'd love to see their revenue numbers, but those aren't public. On the other side of the Pacific, things got ugly. The Trump administration formally accused China's Moonshot AI of stealing from Anthropic's most advanced model, Fable , to build its K3 release. Michael Kratsios, the US tech official, used the phrase "large-scale, covert industrial distillation" — which is Washington-speak for "they copied our homework and changed a few variables." Treasury Secretary Scott Bessent said he's considering adding Moonshot to the trade blacklist and slapping sanctions on them. The Chinese embassy called the allegations "entirely unfounded." I have no way of verifying who's telling the truth here, and honestly, neither do you. What's interesting is the timing — Moonshot's K3 launched just days ago, and Alibaba dropped Qwen 3.8 Max around the same window. China's open-source model pipeline is accelerating fast, and US officials are clearly nervous about losing the edge. The distillation accusation is a common one in AI circles — you can't really prove a model was "stolen" from another model's outputs unless you have access to both training datasets, which nobody outside those companies does. But the geopolitical friction is real, and it's only going to get louder. Meanwhile, Andrej Karpathy said something that made me laugh out loud. The guy literally said he turns on voice mode and rambles at his LLM for 10 minutes — "total mess, anything goes, full stream of consciousness" — and then lets the model organize his thoughts into something coherent. He even prefaces it with a warning to the bot: "This might be jumbled, there might be typos." I tried this yesterday. Opened up ChatGPT Voice, rambled for about 7 minutes about a side project I've been overthinking, and honestly? The summary it gave back was better than anything I would have written in a carefully crafted prompt. There's something to the idea that your first-pass thinking is noisy, and the LLM is actually good at being the noise filter. Karpathy's point is that we're over-optimizing prompt quality when we should be optimizing information density — just dump everything in, let the model sort it. It's the opposite of the "prompt engineering" hype, and I kind of love it. One more practical bit before I wrap up. There's a post making rounds on XDA about running a local LLM alongside Claude to cut costs by half. The author spent over $300 on Anthropic credits in the first half of 2026 because he kept reaching for Opus 4.8 and Fable 5 for every single task. His fix? Route simple tasks — classification, summarization, formatting — through a local model (Qwen or Llama running on Ollama), and only hit the cloud APIs for the hard reasoning stuff. I've been doing something similar for a few weeks. Most of my daily prompts don't need 200-billion-parameter reasoning. A 7B or 13B local model handles "summarize this email thread" just fine. The savings are real — my API bill dropped from about $80/month to ~$35, and I barely noticed a quality difference on routine tasks. The catch, of course, is that you need hardware. A MacBook with 32GB+ RAM or a desktop with a half-decent GPU. If you're running on a laptop with 16GB, a 7B quantized model will work but you'll feel the memory pinch. Still, the hybrid approach — local for cheap, cloud for smart — is probably where most of us should land. That's the roundup for this week. The AI landscape is moving fast — $10B acquisitions, geopolitical fireworks over model distillation, and a surprising reminder from one of the field's sharpest minds that sometimes the best prompt is no prompt at all. Catch you next time. If you enjoyed this, you might find PayCalc useful.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lucky012501/stripe-is-dropping-10b-on-openrouter-the-us-accuses-moonshot-ai-of-stealing-anthropics-crown-53ab

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
