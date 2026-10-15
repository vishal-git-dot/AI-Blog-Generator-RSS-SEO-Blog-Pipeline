---
title: "My webhook catcher stored 100 events — then a burst of 101 deleted the one that mattered"
slug: "my-webhook-catcher-stored-100-events-then-a-burst-of-101-deleted-the-one-that-mattered"
author: "InApp"
source: "devto_ai"
published: "Thu, 15 Oct 2026 11:00:21 +0000"
description: "I built a webhook catcher for integration testing: point any sender at an ephemeral HTTPS URL, it stores up to 100 POSTs, you read them back within 24 hours...."
keywords: "event, events, one, same, webhook, catcher, retried, cap"
generated: "2026-10-15T11:10:31.556140"
---

# My webhook catcher stored 100 events — then a burst of 101 deleted the one that mattered

## Overview

I built a webhook catcher for integration testing: point any sender at an ephemeral HTTPS URL, it stores up to 100 POSTs, you read them back within 24 hours. Simple. Then a retry storm happened. A third-party API was flapping, so it retried the same event dozens of times — well over my 100-event cap. My ring buffer silently overwrote the oldest entries, and the single event I actually needed to debug (a malformed payload from a specific client version) got evicted by its own retries. The bug wasn't the cap. It was that I treated "store events" and "treat events as interchangeable" as the same assumption. They aren't. A webhook catcher sees retries, duplicates, and bursts — the interesting event is often the unique one, not the latest one. The fix was boring and correct: keep the ring buffer, but fingerprint each payload (hash of body + selected headers) and maintain a separate set of "seen fingerprints." When the buffer is full, evict duplicates first; only evict unique events when nothing else is left. Also expose the fingerprint in the read-back response so I can tell "same event, retried" from "new event, same shape." I also added a per-source counter so I can see at a glance that one client sent 87 of my 100 slots. That number alone explained three "mystery" bugs in other people's test setups. Lesson: ephemeral debugging tools need the same durability thinking as production queues. If your tool's whole job is to catch the weird event, make sure a flood of normal events can't erase it. Retried webhooks are the normal case, not the edge case. It's running at https://x402.freeq.one/tools/webhook_catch.html if you want to poke at it. The 100-event cap is still there; the eviction policy just got honest.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/imapphelp/my-webhook-catcher-stored-100-events-then-a-burst-of-101-deleted-the-one-that-mattered-2iio

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
