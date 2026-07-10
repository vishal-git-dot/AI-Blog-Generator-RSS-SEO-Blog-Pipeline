---
title: "Every AI provider fails in its own way. I stopped checking status codes and built an error model instead."
slug: "every-ai-provider-fails-in-its-own-way-i-stopped-checking-status-codes-and-built-an-error-model-instead"
author: "Lolo"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 09:33:00 +0000"
description: "I built an API gateway that routes between OpenAI, Anthropic and Gemini. I figured integrating both providers would be the hard part. It wasn't. Calling thei..."
keywords: "error, provider, you, status, what, something, its, instead"
generated: "2026-07-10T09:45:24.783199"
---

# Every AI provider fails in its own way. I stopped checking status codes and built an error model instead.

## Overview

I built an API gateway that routes between OpenAI, Anthropic and Gemini. I figured integrating both providers would be the hard part. It wasn't. Calling their APIs is maybe an afternoon of work each. The hard part showed up later, the first time something went wrong. The moment it broke Early on, my error handling was basically: catch whatever the provider throws, forward the status code, move on. } catch ( error ) { res . status ( error . status || 500 ). json ({ error : error . message }) } This worked fine until I actually looked at what each provider sends back when something goes wrong. OpenAI wraps its errors in an object with a type and sometimes a code . Anthropic wraps its errors differently, with its own type field that means something else entirely. A 429 from one provider might mean "you're sending too fast, back off." A 429 from another context might mean something closer to "we're out of capacity right now, this isn't really about your rate at all." If you're just forwarding error.status and error.message straight through, none of that nuance survives. Your own error handling ends up being provider-specific whether you meant it to be or not, because the shape of the failure is different depending on who you called. What I built instead Instead of trusting each provider's raw error shape, every call now normalizes into the same internal error model before it reaches the response: } catch ( error ) { const classified = classifyProviderError ( error ) res . status ( classified . httpStatus ). json ({ error : ' AI provider error. Please try again. ' , error_class : classified . error_class , provider : classified . provider }) } error_class is one of a small fixed set: rate_limited , overloaded , quota_exceeded , invalid_request , authentication_error , server_error . That's true regardless of which provider actually failed. The raw provider error still gets logged for me to debug, but what the caller sees is the category of failure, not the provider's specific wire format. The point isn't that this retries anything automatically. It doesn't. It's that "should I retry, and how" becomes a decision you can make once, based on error_class , instead of once per provider you happen to be calling that day. The part that surprised me I expected the differences between providers to be about capability, better reasoning, different context windows, that kind of thing. What actually ate my time was smaller and dumber: two APIs disagreeing about what a 429 even means . Once you stop trusting the HTTP status code to tell you the whole story and start asking "what actually happened here, independent of who I called," a lot of the provider-specific special-casing just goes away. If you're building anything that calls more than one LLM provider, worth checking early: are you branching your error handling on the provider, or on the actual failure type? Those aren't the same question, and the difference only shows up once something breaks in production. This eventually became part of Apiarium , the AI gateway I'm building. Not because I wanted another abstraction layer. Because I got tired of writing provider-specific error handling.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/manolito99/every-ai-provider-fails-in-its-own-way-i-stopped-checking-status-codes-and-built-an-error-model-25do

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
