---
title: "The tests were green but our async loops were doomed: Plugging a severe memory leak in Google GenAI"
slug: "the-tests-were-green-but-our-async-loops-were-doomed-plugging-a-severe-memory-leak-in-google-genai"
author: "S M Tahosin"
source: "devto_python"
published: "Sun, 23 Aug 2026 18:20:06 +0000"
description: "This is a submission for DEV's Summer Bug Smash: Clear the Lineup . The setting Building AI applications that process thousands of text prompts requires spee..."
keywords: "memory, text, sdk, google, genai, after, async, leak"
generated: "2026-08-23T18:35:57.069460"
---

# The tests were green but our async loops were doomed: Plugging a severe memory leak in Google GenAI

## Overview

This is a submission for DEV's Summer Bug Smash: Clear the Lineup . The setting Building AI applications that process thousands of text prompts requires speed and concurrency. When Google released their official google-genai Python SDK, I immediately integrated it to run bulk asynchronous generation tasks. I wrote a loop that fired off hundreds of calls to generate_content asynchronously. The logic was rock solid. The tests went green. The responses were flowing in fast. Then, out of nowhere, the application crashed. The server simply ran out of memory. The crash I restarted the application and watched the system monitor. With every loop iteration, the RAM footprint grew larger and larger. Even after the LLM responses were fully processed, saved to the database, and the local variables went out of scope, the memory just kept climbing. The garbage collector wasn't cleaning up. I was facing a textbook, catastrophic memory leak. The investigation I imported tracemalloc to trace memory allocations deep inside the runtime. After running the loop for just 10 seconds, the profiler pointed its finger straight at the underlying HTTP clients: httpx and aiohttp . A massive accumulation of raw byte strings ( b"" ) and HTTP response objects was stubbornly clinging to the memory heap. I traced the bug down to google/genai/_api_client.py . When a non-streaming asynchronous request completes, the SDK extracts the .text payload from the network response and wraps it in a beautiful SDK model for the user. But there was a fatal omission: the SDK never explicitly called .close() or .release() on those underlying network objects. Because complex asynchronous connection pools (like httpx.AsyncClient ) often keep references to recent connections alive, those massive byte buffers—sometimes megabytes of JSON text—were being held hostage in memory indefinitely. The fix Relying on Python's garbage collector in high-throughput async loops is a dangerous game. To fix this permanently, the SDK needed to manually obliterate the network buffers the moment the text payload was safely extracted. I submitted a patch to the core request engine to introduce an eager memory release pattern : text = client_response . text if hasattr ( client_response , " aclose " ): await client_response . aclose () if hasattr ( client_response , " _content " ): client_response . _content = b "" if hasattr ( client_response , " _text " ): client_response . _text = "" By manually setting _content = b"" , we aggressively break the reference to the massive byte strings. Even if the empty response shell is temporarily held alive by an async stack frame, the actual payload memory is instantly freed back to the system. Memory usage completely flatlined after the fix! After applying the patch, I pushed 10,000 generation requests through the system. The memory footprint remained completely flat. The leak was finally plugged! GitHub PR: googleapis/python-genai#2900

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tahosin/the-tests-were-green-but-our-async-loops-were-doomed-plugging-a-severe-memory-leak-in-google-genai-311g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
