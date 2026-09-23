---
title: "What building a bot with real memory taught me about storage that cannot be edited"
slug: "what-building-a-bot-with-real-memory-taught-me-about-storage-that-cannot-be-edited"
author: "Ar1Ma「🦑」🦭/acc | 🥃"
source: "devto_python"
published: "Wed, 23 Sep 2026 20:58:19 +0000"
description: "A support bot asks for your order number for the third time. A companion app has no idea what you told it yesterday. Most of us have met a chatbot that forge..."
keywords: "line, not, one, what, bot, lines, memory, seconds"
generated: "2026-09-23T21:20:28.046469"
---

# What building a bot with real memory taught me about storage that cannot be edited

## Overview

A support bot asks for your order number for the third time. A companion app has no idea what you told it yesterday. Most of us have met a chatbot that forgets, and the usual fix is a chat history table. I have been building one that does not forget, for the Walrus Sessions 8 hackathon. The theme is chatbots that remember, and the memory lives on Walrus rather than in a database I run. The bot talks on Telegram, uses DeepSeek for the language model, and stores everything it knows as lines of text with tags on them. I assumed the language model would be the hard part. It was not. The hard part was timing, and the ways a storage layer can tell you something that is not true. Memory you cannot edit There is no update and no delete. A line, once written, stays. So the bot does not change its mind by editing anything. When you finish a task, it writes a second line saying the task is done, and the reader folds every line about that task down to the newest one. That works, but only if the fold is predictable. Mine was not. A write is a job, not a write The call that stores a line returns in about a second. It does not mean the line is stored. What comes back is a job id and a status of running. I watched one job to the end. It sat pending for the first 1.2 seconds, went to running at 3.2 seconds, and only reached uploaded at 26.1 seconds. That last state is the first one where the line can be read back. So a client on this has to keep its own outbox, hold each line until a read proves the world can see it, and decide what "accepted" means. In my case a failed job and a slow job look identical for the first four minutes, which is a gap I cannot close from the client side. A read that returns nothing This one cost me a user's trust in a way I did not notice at first. The bot told someone their memory was empty. It was not. That namespace held three lines, written half an hour earlier. I asked the same question again 3 seconds later and got all three back. The retriever sometimes answers an empty list for a query that matches, and then matches. My first retry waited 0.6 seconds, which sits inside that gap, so the read gave up and the bot reported an empty memory. The waits now grow, 0.6 then 2 then 3 seconds, and there is a test that checks a namespace which really is empty still stops rather than paying all of that on every message. Two lines, one second, one lost reminder Timestamps were precise to the second. Every line the model produces in one turn is stamped from a single clock reading, so a turn that mentions the same task twice produces two lines with identical timestamps. The fold keeps the newest line, and with two lines tied there was nothing left to sort by except the order the storage layer returned them in. That order is not guaranteed. One of the two orders kept the line without the reminder time, so a reminder vanished and nothing on screen said so. I found it by accident, when the same deadline appeared twice with different wording. The fix was to stop guessing: the tie is now broken by what a line knows before it is broken by the text of the line, so both orders produce the same answer. What changed With those three fixed, the bot does what it says it does. Reminders survive a restart, a finished task stays finished, and when someone asks what it knows it answers from the stored lines rather than from a cached guess. There is a script in the repo that prints the before and after side by side on the same input, because a paragraph claiming a bug is fixed is worth less than two printed lines that show it. The session It is called Walrus Sessions 8: Chatbots That Remember, and it runs until October 9. If you have wanted to try agent memory that is not a vector store on your own machine, it is a good excuse to build something small. Register directly on DeepSurge: https://www.deepsurge.xyz/hackathons/c0141a4a-21be-4009-bc63-7c168608c849

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ar1madotsui/what-building-a-bot-with-real-memory-taught-me-about-storage-that-cannot-be-edited-5c9g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
