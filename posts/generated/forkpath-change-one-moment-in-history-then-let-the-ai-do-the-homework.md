---
title: "Forkpath: Change One Moment in History, Then Let the AI Do the Homework"
slug: "forkpath-change-one-moment-in-history-then-let-the-ai-do-the-homework"
author: "Srilal Sachintha"
source: "devto_ai"
published: "Tue, 20 Oct 2026 04:08:50 +0000"
description: "What I Built Forkpath is an alternate-history explorer. You type one sentence ("What if the Ming treasure fleets kept sailing?"), pick when it happens, and a..."
keywords: "forkpath, you, history, one, writer, event, your, model"
generated: "2026-10-20T04:19:10.502175"
---

# Forkpath: Change One Moment in History, Then Let the AI Do the Homework

## Overview

What I Built Forkpath is an alternate-history explorer. You type one sentence ("What if the Ming treasure fleets kept sailing?"), pick when it happens, and an AI writer maps out what follows, event by event, as a branching tree with the odds at every fork. Writing good alternate history is a lot of work. You research the period, think through who wants what, follow second- and third-order effects, and keep half a dozen storylines consistent. Forkpath does that homework for you. You type one line, lean back, and watch the timeline grow. What it gives you: 🌳 A map, not a story. Every event is a node. Where outcomes are genuinely uncertain, the writer branches and gives each branch a likelihood. A Most likely view fades every path history probably did not take. 🧵 Parallel streams. Regions, wars and programs run as separate threads that influence and merge into each other. ⚖️ A realism check. Language models lean toward tidy, happy endings. The writer checks incentives, capabilities and historical base rates before each event, and an optional second review flags unearned outcomes, anachronisms and numbers out of scale. ✍️ You stay the author. Edit, regenerate, branch or delete any event. Your edits become canon, and events that depended on them are marked stale. Demo Forkpath runs locally, so here's a quick tour in screenshots. Code SrilalS / ForkPath Change one moment in history and watch the consequences branch out. An AI-powered alternate-history mapper with odds at every fork. Forkpath Change one moment in history. Watch the consequences branch out. An AI writer maps what happens next, event by event, across parallel storylines, with the odds at every fork. Runs on your machine; your timelines stay there Guide · Getting started · Engines and costs · Development Why Forkpath Alternate history is usually told as one story. Real history is a tree of things that almost happened. Forkpath keeps the whole tree: 🌳 A map, not a story. Every event is a node. The writer branches where outcomes are genuinely uncertain gives each branch a likelihood, and tracks regions, wars and programs as parallel streams that influence and merge into each other. ⚖️ Neutral as water. Language models lean toward tidy, peaceful endings. Forkpath's writer runs a realism check (incentives, capabilities, historical base rates) before every event, and a separate review can flag unearned outcomes, anachronisms and numbers out… View on GitHub npm install npm run dev Then open http://localhost:5173 and pick an engine in Settings . How I Built It TypeScript end to end: React 19 and React Flow (with dagre layout) in the browser, Express and Zod on the server, and the graph rules shared between the two. Timelines are plain JSON files on your disk. The model layer was designed to be swappable from day one: No SDKs. The server talks to models through two small adapters built on plain fetch : one for the Anthropic Messages API and one for any OpenAI-compatible endpoint. That second adapter is the open door. Point it at Ollama ( http://localhost:11434/v1 ) or LM Studio ( http://localhost:1234/v1 ) and an open-weight model running on your own machine writes your history. The Settings page has presets for both, plus a Test connection button. Same rules for every model. Whatever engine you pick gets the same compact briefs, schema validation and writer rules, so swapping models doesn't mean rewriting prompts. Built to scale on a laptop. Layout caching, viewport culling and a background layout worker keep thousand-node timelines smooth. Why Does Open Innovation Matter? Alternate history is personal. People use it to work through "what if" questions about their own country, family history or politics, and those are exactly the questions you might not want sitting in someone else's logs. With an open-weight model behind it, Forkpath is fully local: 🏠 Nothing leaves your machine. The app, the model and your timelines all live on your laptop. There's no telemetry and no account. 💸 Set it up once, never pay again. A big timeline can mean hundreds of model calls. Over a paid API that adds up (Forkpath even has a monthly budget feature for that reason). A local model makes the meter disappear, so you can regenerate and branch freely. 🔁 Swap the brain whenever you want. A new open model comes out, you change one setting. Want a grimmer or more hopeful writer? Change the temperament, or try a different model and compare. 📂 Open all the way down. Forkpath itself is MIT-licensed, and timelines are plain JSON you can read, diff and share. The Lazy Payoff Researching and writing a believable alternate timeline by hand takes days. In Forkpath it takes one sentence and a cup of tea. The writer handles the reasoning, the bookkeeping across storylines, and the "wait, would that actually happen?" check. You just decide which branch looks fun and click Continue .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/srilals/forkpath-change-one-moment-in-history-then-let-the-ai-do-the-homework-4l47

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
