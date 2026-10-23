---
title: "Prilizer: stop rereading every pull request"
slug: "prilizer-stop-rereading-every-pull-request"
author: "Huzaifa Rehman"
source: "devto_ai"
published: "Fri, 23 Oct 2026 21:05:34 +0000"
description: "My entry for Hacktoberfest Week 3: Slow and Steady . What I Built A reviewer asks for a test. You read the message, push another commit, and come back later...."
keywords: "model, request, local, requests, github, not, what, one"
generated: "2026-10-23T21:14:15.044462"
---

# Prilizer: stop rereading every pull request

## Overview

My entry for Hacktoberfest Week 3: Slow and Steady . What I Built A reviewer asks for a test. You read the message, push another commit, and come back later. The thread has moved on. Was the request satisfied, withdrawn, or simply buried? Prilizer is a local catch-up desk for up to three public pull requests by one contributor. It reads PR bodies, comments, reviews and inline comments, then uses a local Qwen3 model to identify requests and explain changed discussion. Each action carries the original quote and a GitHub link. The piece I care about most is what happens on the next refresh. An outstanding request stays visible even if the next summary omits it. Marking a digest reviewed only records that you read it. A request leaves the active list after explicit source confirmation, a local dismissal, or a fresh closed/merged state. Closing a PR does not prove the requested code was fixed. If collection is partial or the model fails, the card says Check manually and keeps the older evidence. The app never posts a reply or resolves a GitHub thread. Demo Source and setup · Watch the uncut walkthrough This is the actual app with fictional discussion and simulated GitHub/model responses. The uncut walkthrough shows review, local dismissal, edited evidence and a partial-fetch failure. It is fixture playback, not a live model or customer session. Code Prilizer on GitHub . The repository includes setup, evaluation inputs, raw outputs and failed runs. How I Built It A React page talks to a loopback Node server. A bounded anonymous collector keeps discussion channels separate and compares complete snapshots. Qwen3 1.7B proposes structured requests; application code validates quotes and provenance, then persists requests independently of the next model summary. The intended shortcut is opening one small desk instead of reconstructing several conversations. Refresh is manual, unchanged successful analysis is cached, and older requests remain visible. There is no notification feed to keep watching. I have not measured how much human review time this saves. I would rather leave that question open than turn a fast cache read into a claim about someone's working day. What Worked, and What Didn't The first frozen evaluation failed: 8/12 correct outcomes, including one false Waiting. The model missed indirect requests and confused who was asking whom. I added source-role and fresh-confirmation constraints, retained the failures, and froze twelve different synthetic cases before the next run. The revised pipeline scored 12/12 , with zero false Waiting results and zero invalid action quotes. A fixed keyword baseline scored 10/12 , with one false Waiting. The model picked up an approval condition that the keyword baseline missed. That result belongs to the full pipeline, including deterministic persistence and validation. It does not establish general reliability. Summary wording was not scored; manual inspection still found misleading actor attribution in two summaries. Speed is another limit. Fresh-set model calls took 8.4–47.1 seconds. A real Docker CLI PR took 47.3 seconds, then reused its analysis on an unchanged refresh. A Node.js PR hit the 60-second timeout twice. The app kept it at Check manually. My 30-second target remains unmet. Raw results and the earlier failures are retained . Why Does Open Innovation Matter? Qwen3's open weights and Ollama let the interpretation run on the same laptop as the saved discussion. GitHub still needs a network connection for fresh data; cached evidence remains readable offline. The model proposes meaning; inspectable application code checks source IDs, exact quotes, actor eligibility, freshness and request persistence. I can change those rules or test another local model without depending on a hosted inference endpoint. There is no per-request inference API bill. Hardware, electricity, memory and waiting still cost something. The open approach makes this local workflow possible, while the measurements show where it is still too slow.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/huzaifa_abdulrehman9/prilizer-stop-rereading-every-pull-request-1k1c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
