---
title: "A live call coach with two modes: interviews and meetings"
slug: "a-live-call-coach-with-two-modes-interviews-and-meetings"
author: "Made by Asking"
source: "devto_python"
published: "Mon, 26 Oct 2026 03:45:56 +0000"
description: "Try the UI demo in the browser, no install: https://henrylop.github.io/live-call-coach/ui/ Interview mode In an interview, the right example is somewhere in ..."
keywords: "call, live, coach, question, card, demo, interview, mode"
generated: "2026-10-26T04:10:10.669071"
---

# A live call coach with two modes: interviews and meetings

## Overview

Try the UI demo in the browser, no install: https://henrylop.github.io/live-call-coach/ui/ Interview mode In an interview, the right example is somewhere in your head and it surfaces five minutes late. live-call-coach is a small package that listens to the other side of a call and shows tiered hints while the question is still fresh. The quick tier answers in about 1.5 seconds with an opening line, three key points and a hard-question flag. The deep tier is grounded in your own notes and cites them. When a new question starts before a card is ready, the stale card is dropped. The whole pipeline runs on a simulated clock, so replays are instant and the tests are deterministic. There is a UI demo in ui/ that needs no server: open index.html and watch a scripted interview play through. The demo and the tests use an offline stub, so nothing here calls a paid API. Meeting mode Work calls ask for facts you own but cannot look up in the moment. live-call-coach has a meeting mode for that: for each question it builds a card with a line to say and the facts behind it, with their sources, and it keeps a running ledger of commitments (who, what, when). Two details carry most of the design. A card that is still being built when the next question starts is dropped rather than shown late. And the reader that follows the call is read-only: it has an allow-list with one entry, turning on captions, and a test scans the source for anything that types or sends. The UI demo in ui/ replays an invented call with no server, so you can see the cards arrive, a stale card leave and the ledger fill. The code runs offline against a stub model. Repository: https://github.com/HenryLop/live-call-coach

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/madebyasking/a-live-call-coach-with-two-modes-interviews-and-meetings-2j42

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
