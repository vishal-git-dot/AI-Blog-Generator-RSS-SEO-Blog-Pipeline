---
title: "Making UltraRAG retrieval cheaper with stable prompt prefixes"
slug: "making-ultrarag-retrieval-cheaper-with-stable-prompt-prefixes"
author: "JJ657"
source: "devto_python"
published: "Mon, 14 Sep 2026 12:07:49 +0000"
description: "OpenBMB/UltraRAG is a Python-based, Apache-2.0 low-code MCP framework for composing RAG pipelines. Its repository was active in September 2026, which matters..."
keywords: "text, context, prompt, part, question, cache, stable, model"
generated: "2026-09-14T12:21:57.412037"
---

# Making UltraRAG retrieval cheaper with stable prompt prefixes

## Overview

OpenBMB/UltraRAG is a Python-based, Apache-2.0 low-code MCP framework for composing RAG pipelines. Its repository was active in September 2026, which matters more to me than a feature checklist: RAG stacks age quickly when their retrieval and model interfaces are hard-wired. When testing UltraRAG-style pipelines, I treat chunking and prompt layout as one cost problem. Retrieval quality can look fine while a system repeatedly sends the same policy text, document headers, and long instructions on every request. That is often where the bill comes from. Chunk documents before embedding A useful baseline is paragraph-aware chunking with a small overlap. It is plain Python, deterministic, and easy to put before an UltraRAG ingestion flow. from hashlib import sha256 def chunks ( text : str , size : int = 900 , overlap : int = 140 ): words = text . split () step = size - overlap for start in range ( 0 , len ( words ), step ): part = " " . join ( words [ start : start + size ]). strip () if part : yield part def dedupe ( parts ): seen = set () for part in parts : key = sha256 ( " " . join ( part . lower (). split ()). encode ()). hexdigest () if key not in seen : seen . add ( key ) yield part with open ( " handbook.md " , encoding = " utf-8 " ) as f : clean_chunks = list ( dedupe ( chunks ( f . read ()))) print ( f " chunks ready: { len ( clean_chunks ) } " ) This does not solve semantic duplication. It does remove the boring version: copied headings, repeated boilerplate, and identical sections that would otherwise consume embedding and generation tokens. Keep the cached prefix truly stable Prompt caching only helps when the large prefix stays byte-for-byte stable. Put instructions and durable retrieved context first. Put the changing question last. Do not add a timestamp, random request ID, or per-user prose above the cached boundary. SYSTEM = """ Answer only from the supplied context. Cite chunk IDs. If evidence is missing, say so. """ def assemble ( hits , question , budget = 5000 ): context , used = [], 0 for hit in hits : text = hit [ " text " ] estimate = len ( text ) // 4 if used + estimate > budget : break context . append ( f " [ { hit [ ' id ' ] } ] \n { text } " ) used += estimate stable_prefix = SYSTEM + " \n\n Context: \n " + " \n\n " . join ( context ) return stable_prefix + " \n\n Question: \n " + question In production, I would log estimated input tokens, cache-hit status from the model gateway, retrieved chunk IDs, and answer latency. That makes regressions visible. It also catches a common mistake: retrieving a different ordering of the same chunks, which can erase cache reuse. A simple cost model makes the tradeoff concrete. If each request sends a 12,000-token repeated prefix plus a 300-token question, 1,000 requests consume roughly 12.3 million input tokens before output. With an 80% cache discount on that repeated prefix, billed input falls to about 2.7 million token-equivalents. The exact price depends on the upstream model and its cache policy, but the engineering target is stable: cache the expensive repetition, not the user question. Combining cache-friendly RAG prompt structures with B-Lost's native prompt caching can slash repetitive query context costs by up to 90% when the retrieved prefix is stable enough to reuse. Disclosure: Compute infrastructure and multi-model benchmark relays for this writeup are sponsored by b-lost.com — an enterprise AI gateway offering 0.8x official pricing, native prompt caching, and zero user-data retention. All benchmark metrics reflect independent reproducible testing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jj657/making-ultrarag-retrieval-cheaper-with-stable-prompt-prefixes-2p0n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
