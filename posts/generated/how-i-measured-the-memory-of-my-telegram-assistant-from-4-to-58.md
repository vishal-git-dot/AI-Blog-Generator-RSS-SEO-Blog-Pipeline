---
title: "How I measured the memory of my Telegram assistant, from 4% to 58%"
slug: "how-i-measured-the-memory-of-my-telegram-assistant-from-4-to-58"
author: "0xDevDav"
source: "devto_python"
published: "Fri, 16 Oct 2026 15:54:24 +0000"
description: "Zoe is a personal assistant I talk to on Telegram. She runs on my own server on top of the Claude Code CLI: every message becomes a claude -p run, and a SQLi..."
keywords: "memories, neurons, recall, zoe, every, message, search, memory"
generated: "2026-10-16T16:24:14.485051"
---

# How I measured the memory of my Telegram assistant, from 4% to 58%

## Overview

Zoe is a personal assistant I talk to on Telegram. She runs on my own server on top of the Claude Code CLI: every message becomes a claude -p run, and a SQLite queue in front of it makes sure nothing is lost when a turn hangs or the service restarts. The code is MIT and on GitHub: https://github.com/0xDevDav/zoe This post is about the part that took the most work: her memory, and how I found out that my first version barely worked. Memory as neurons and synapses Every fact, preference, habit or correction Zoe learns is a neuron, a row in SQLite. Neurons learned in the same conversation are linked by synapses with a weight. When a message arrives, recall does two things: It finds seed neurons that match the message. It spreads energy from the seeds along the synapses, in proportion to their weight. The best neurons go into the prompt, and Claude writes the reply. The reply ends with the numbers of the memories it actually used, and those paths get stronger, while links that keep pulling in unused memories fade. The first version, and why it was bad At first I didn't measure anything. Recall looked fine in the few cases I checked by hand. Then I built a test. I took about 50 of my real messages and asked Claude to judge, for each one, which memories it really needed. Recall is then replayed against the memory as it was at the time of each message, and the score is the share of needed memories that come back. The first version found 4%. The cause was a loop. Seeds were found with a LIKE search ranked by a popularity score, and after every turn the recalled neurons were linked together. So the popular neurons got more links, which made them more popular, and the same 8 memories came back for almost every message. What moved the number Each change below was kept only because the score went up. Recall Needed memories found Keyword search ranked by popularity 4% Full-text search, spreading normalized by link strength 28% Search by words and meaning, lasting memories first 46% The chat's latest messages searched too, twelve places 58% Full-text search: seeds now come from SQLite FTS5 ranked with bm25, so rare words count more than common ones. Spreading divides the energy by the square root of the strength of both ends of a synapse, so a neuron wired to everything takes little from each link, and recall stops linking recalled neurons together. Meaning: a second list of seeds comes from EmbeddingGemma 300M, quantized, running with ONNX Runtime on CPU. The two lists are fused with reciprocal rank fusion (k=60). Lasting memories like facts and preferences get their own places in the prompt, so past conversations can't push them out. Recent context: a short message like "how did it go?" has nothing to search for. Now the last four messages of the chat are searched too, at half energy, and lasting memories get twelve places. What didn't help A concept layer in the style of HippoRAG, with about 150 concepts extracted by Claude and linked to the memories: 54 to 56% against 57 to 58% without it. Left out. Newer embedding models. I tried e5-small, Granite 311M R2 and Harrier 270M and 0.6B on my own data. The newest was not the best for my messages. Linking each new neuron to its 3 nearest neighbors by meaning: one or two points, within the noise. Cutting the links of old hub neurons: no change. One trap in the measure Every night Zoe reviews her memory and merges duplicates. A day after reaching 46%, the score dropped to 42%, and part of the drop had nothing to do with recall: 9% of the judge's labels pointed to neurons that no longer existed, because they had been merged into others overnight. Now every merge is recorded, and the measure follows a merged neuron to the one that kept it. What is still missed Most of the memories still missed are preferences tied to a kind of request rather than to a name or a thing, like how I want a certain type of text written. Nothing in the message points at them. The next step I want to try is a tool that lets Zoe search her memory by herself in the middle of a turn. Zoe also runs this measure in her nightly study, and a new sample is judged every two weeks. If you try it, recall starts measuring after the first 40 messages. The repo is https://github.com/0xDevDav/zoe . I'm happy to hear how others measure recall in their own assistants.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/0xdevdav/how-i-measured-the-memory-of-my-telegram-assistant-from-4-to-58-2lao

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
