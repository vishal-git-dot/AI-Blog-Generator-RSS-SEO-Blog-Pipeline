---
title: "How I gave a self-hosted AI agent long-term memory, without a vector database"
slug: "how-i-gave-a-self-hosted-ai-agent-long-term-memory-without-a-vector-database"
author: "HemantAcharya"
source: "devto_python"
published: "Mon, 03 Aug 2026 19:33:09 +0000"
description: "TL;DR: I added long-term memory to a self-hosted AI agent. The memory lives on the user's own server — no cloud, no vector database. Embeddings are stored as..."
keywords: "memory, database, user, one, vector, own, memories, never"
generated: "2026-08-03T19:44:41.764503"
---

# How I gave a self-hosted AI agent long-term memory, without a vector database

## Overview

TL;DR: I added long-term memory to a self-hosted AI agent. The memory lives on the user's own server — no cloud, no vector database. Embeddings are stored as float32 blobs in SQLite and compared with a plain numpy cosine similarity. The easy part was storing memories; the hard part was consolidating them (add / update / delete), and two LLM bugs taught me the most. The constraint that shaped everything Most "AI memory" tutorials start by spinning up a vector database and shipping your data to someone's cloud. I couldn't do either. The AI agent I work on AIDA by Autafy is self-hosted — it runs on the user's own server, under their own API key. Its whole point is that your data never leaves your hands. So when I added memory, the memory had to live there too: on your box, in a file you can open, back up, or delete. That one constraint decided the whole design. Two kinds of memory: semantic and episodic Most memory features only store facts — "prefers concise answers," "works in real estate." Useful, but flat. I wanted two layers: Semantic memory — durable facts: preferences, projects, the people you work with. Episodic memory — the moments worth remembering: "was excited about landing their first customer." The episodic layer is what makes an assistant feel like it knows you, instead of just holding a profile card. Both are just rows in SQLite. Why no vector database? At per-user scale, a vector database is overkill. One person accumulates a few hundred to a few thousand memories — not millions. So embeddings get stored as raw float32 blobs right next to the memory text, and retrieval is a brute-force cosine similarity in numpy: python import numpy as np memories store their embedding as a float32 blob in SQLite def cosine_search(query_vec, rows, top_k=3): q = query_vec / np.linalg.norm(query_vec) scored = [] for mem_id, blob in rows: v = np.frombuffer(blob, dtype=np.float32) scored.append((mem_id, float(np.dot(q, v / np.linalg.norm(v))))) scored.sort(key=lambda x: x[1], reverse=True) return scored[:top_k] At a few thousand rows this runs in well under a millisecond. What you get for free by skipping the vector database: No second store to sync — one SQLite file is the memory. Isolation — memory embeddings never touch the document/RAG store; different file, different code path. Ownership is literal — the entire memory is one portable file the user controls, not rows in a database they don't. The hard part: consolidation, not storage Anyone can append rows. The real problem is the tenth conversation, where you contradict yourself. "My favorite color is green." → store it. Later: "actually I hate green, blue's my color." → this should rewrite the row, not add a second one. "I'm not vegetarian anymore." → this should delete the fact, not store a weird negation. So a nightly job (a cron sweep — never on the hot path of a chat) reviews each day's conversations, extracts candidate facts, and asks an LLM to decide against the existing memories: Given a NEW fact and up to 3 EXISTING memories, choose ONE: ADD → genuinely new information UPDATE → same subject, changed info; rewrite that memory DELETE → new fact contradicts and replaces nothing NOOP → duplicate or not worth keeping Every decision — the op and the distances to the nearest existing memories — gets logged, so thresholds can be tuned later from real data instead of guessed up front. Two bugs that taught me the most 1. The model that silently returned nothing. Consolidation kept defaulting to ADD — contradictions never deleted, updates never updated. The cause: I was running a cheap reasoning model with max_tokens capped low. Reasoning models spend tokens thinking before they answer, so the budget got burned on reasoning, the response came back truncated to nothing, my JSON parse failed, and the fallback quietly chose ADD. Three sweeps ran that way because nothing errored. Lessons: give reasoning models room, log the full API response body when debugging, and never let a fallback hide a failure. 2. The feedback loop. The extractor started reading the assistant's own replies as new facts — memory-informed answers getting laundered back into memory as fresh "facts," and even user questions becoming false facts. The fix was one load-bearing rule in the extraction prompt: only the user's statements count as a source. Assistant turns are never facts. Memory you can audit and delete Because this runs on the user's own server, the pitch isn't "trust us with your data" — it's auditability. So every control ships with it: memory is off by default, every memory is visible and editable, each one shows its source, there's an incognito mode per conversation, and a forget-everything button. Memory without control is just surveillance. Takeaways For per-user memory at human scale, SQLite blobs + numpy cosine beat a vector database on simplicity and portability. Storing memories is easy; consolidating them (add / update / delete / noop) is the real work. Beware silent fallbacks — a parse failure that defaults to the harmless-looking action can hide a broken pipeline for days. If your extractor reads a conversation, make sure it can't treat the assistant's own words as ground truth. This is built into AIDA, a self-hosted AI agent at autafy.ca — but the approach works for any assistant where you'd rather own the memory than rent it. I'd genuinely like to compare notes on consolidation; it's the part I'm least sure I've nailed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hemantacharya/how-i-gave-a-self-hosted-ai-agent-long-term-memory-without-a-vector-database-55gg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
