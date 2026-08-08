---
title: "I built an async wrapper for OpenAI/Anthropic SDKs because I didn't want a proxy in my request path"
slug: "i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path"
author: "Mandar Shinde"
source: "devto_python"
published: "Sat, 08 Aug 2026 12:46:54 +0000"
description: "I kept running into the same tradeoff building cost tooling for teams shipping LLM features. Every attribution tool in this space works the same way: you poi..."
keywords: "you, call, your, wrapper, want, path, before, cognocient"
generated: "2026-08-08T12:58:39.633577"
---

# I built an async wrapper for OpenAI/Anthropic SDKs because I didn't want a proxy in my request path

## Overview

I kept running into the same tradeoff building cost tooling for teams shipping LLM features. Every attribution tool in this space works the same way: you point base_url at a proxy, and it sees every call before it happens. That's genuinely useful if you want to block or downgrade a call before it fires. It also means the proxy's uptime is now your uptime, and you've added a network hop to every single request. I wanted the attribution without touching the request path at all. So I wrote a wrapper instead. Cognocient wraps the OpenAI and Anthropic Python clients directly. You still call client.chat.completions.create() exactly the way you always did. The wrapper times the call, then fires a cost report on a background thread after your real response has already returned to your code. The part I actually spent the most time on wasn't the happy path, it was making sure a dead reporting endpoint can never touch your application. If Cognocient's ingestion API is slow, down, or just does not exist, that failure has to stay invisible to whatever you're building. No exception bubbling up, no retry pile-up blocking your real call. There is a test, test_reporter_failure_isolation.py , that specifically points the reporter at an unreachable host and asserts the actual API call still returns clean. Writing that test is what convinced me the design was sound, not the other way around. What you get: per-call cost, and tags for feature/team/user if you want chargeback-style reporting later. What you do not get, on purpose: pre-call blocking. If a call is about to blow your budget, this wrapper finds out after it already happened, same as any billing dashboard does. If you need to stop a call before it fires, you want a proxy, and honestly LiteLLM or Portkey do that well. This is for people who've already decided visibility without a critical-path dependency is the right tradeoff for their setup. Also worth knowing before you reach for it: streaming responses ( stream=True ) aren't reported yet. If most of your traffic streams, this won't give you complete numbers right now. Non-streaming is solid, I would call it production-safe there. Streaming is next. from cognocient import CognocientOpenAI as OpenAI client = OpenAI ( api_key = " sk-... " , cognocient_key = " sk-cog-... " ) # everything else about the client works exactly like before MIT licensed, signed provenance on the PyPI release, genuinely early (v0.1.x). If you're already routing through a gateway and it is working for you, this probably isn't for you. If you have been putting off cost visibility specifically because you didn't want another hop in the path, I would like to hear if this is useful or if I have missed something obvious. GitHub : https://github.com/mandarvshinde/cognocient-python-wrapper PyPI : pip install cognocient

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mandarvshinde/i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path-1h1p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
