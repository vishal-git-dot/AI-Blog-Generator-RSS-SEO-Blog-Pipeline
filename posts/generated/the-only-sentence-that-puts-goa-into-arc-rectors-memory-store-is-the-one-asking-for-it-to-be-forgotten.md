---
title: "The Only Sentence That Puts Goa Into Arc Rector's Memory Store Is the One Asking For It To Be Forgotten"
slug: "the-only-sentence-that-puts-goa-into-arc-rectors-memory-store-is-the-one-asking-for-it-to-be-forgotten"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Sun, 23 Aug 2026 12:43:50 +0000"
description: "Level 7 of nine in Project Arc Rector - an agentic RAG stack built from free, self-hostable parts, one swappable level at a time. Level 6 was ingestion. This..."
keywords: "live, goa, turns, free, recall, sentence, memory, level"
generated: "2026-08-23T12:50:17.233921"
---

# The Only Sentence That Puts Goa Into Arc Rector's Memory Store Is the One Asking For It To Be Forgotten

## Overview

Level 7 of nine in Project Arc Rector - an agentic RAG stack built from free, self-hostable parts, one swappable level at a time. Level 6 was ingestion. This one is memory, whose trap is that three things all get called that: the chunks retrieved for this question, thrown away when it is answered; the session history, which lives until the visitor leaves; and durable facts, which outlive every session. The dependency-free adapter is where the argument lives, and it is the part to read before the vendors: _STOP = r " (?=[.!?,;]|\s+(?:and|but|so|because|then|while|which|what|who)\b|$) " re . compile ( r " \bi\s+(?:live|work|am based)\s+in\s+([\w\s ' \-]{2,60}?) " + _STOP , re . I ), # add(): seven first-person patterns, exact-text dedupe, append. No reconciliation. Repo: https://github.com/dev48v/arc-rector - 174 tests, no network, no model, no container. The page runs the extraction, the add/update/delete/noop decision, the scoping leak and the compaction in a dependency-free engine in your browser: https://dev48.infy.uk/arcrector/level7-memory.html Run the canonical case against the real LocalMemory , six turns, printing what each stored: "I live in Pune." -> ['I live in Pune'] "I moved to Goa." -> [] # no pattern matches "Forget that I live in Goa." -> ['I live in Goa'] # the request IS the fact store: ['My name is Devanshu', 'I live in Pune', 'I work with Java', 'I live in Goa'] search("where do I live") -> [('I live in Goa', 1.0018), ('I live in Pune', 1.0018)] The sentence announcing the move stores nothing; the sentence asking to forget it is the only thing that ever writes Goa. Both locations then come back tied, Goa first purely because recency is the tie-break. Negation behaves the same way: "I don't use Windows" is appended beside "I use Windows", so a fact and its own negation are recalled together. That is the argument for the layer existing, and why use: mem0 is the default - Mem0 spends an LLM call choosing between ADD, UPDATE, DELETE and NOOP, and on these six turns the reconciling decision leaves 2 facts where the append-only store holds 5. The defaults, as they ship: use: mem0 , path: .arc_rector/memory , fallback_to_local: true . Mem0 is reconfigured onto local Ollama ( llama3.2:3b , nomic-embed-text at 768 dims) and a local Qdrant collection so it needs no vendor key, with MEM0_TELEMETRY set before the import because the module reads it at load time. A hang is not an exception, so add runs under a 45-second wall clock on its own daemon thread per call - the first version used a single-worker pool, which head-of-line blocks: a timed-out call keeps running and later calls wait for it plus their own timeout. recall asks for top_k=3 and returns [] on any exception, because a Qdrant timeout is not the user's problem. Where compaction's cost actually was Squeeze ten turns into a 220-token budget and 51% of the text survives: 4 kept whole, 2 summarised by extraction, 4 dropped. Recall@3 over seven fact probes falls 1.00 to 0.43. budget tokens kept kept / summarised / dropped recall@3 120 31% 2 / 1 / 7 0.29 220 (default) 51% 4 / 2 / 4 0.43 320 78% 5 / 4 / 1 1.00 I assumed the losses were the dropped turns. Two of the four are; the other two are turns still in the context . The Goa turn and the InXpress turn both survived as extractive summaries, and the summariser kept the preference sentence and threw the location away. A dashboard reporting turns retained would say 6 of 10 survived; recall says 3 of 7 facts did. Compression above 78% here is free and below it the curve falls off a cliff, so a system reporting its ratio without its recall drop is telling you half the story. Next is Level 8, safety and guardrails. Nine levels, all free to self-host: https://dev48.infy.uk/arcrector.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/the-only-sentence-that-puts-goa-into-arc-rectors-memory-store-is-the-one-asking-for-it-to-be-3a11

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
