---
title: "I re-ran a rival's memory benchmark. It tied mine. Here is the interesting part."
slug: "i-re-ran-a-rivals-memory-benchmark-it-tied-mine-here-is-the-interesting-part"
author: "Calas Automations"
source: "devto_ai"
published: "Fri, 20 Nov 2026 23:49:00 +0000"
description: "I build Monomem, shared memory for AI coding agents. It records which app wrote each note and holds suspicious writes until a person looks. On LongMemEval-S,..."
keywords: "monomem, memory, not, question, known, own, can, ran"
generated: "2026-11-20T23:51:31.229394"
---

# I re-ran a rival's memory benchmark. It tied mine. Here is the interesting part.

## Overview

I build Monomem, shared memory for AI coding agents. It records which app wrote each note and holds suspicious writes until a person looks. On LongMemEval-S, a standard long-term-memory test, a well-known memory project (agentmemory) publishes 84.7%. I re-ran its own evaluation on the same data file and got 84.7% back, exactly. Monomem scored 86.0% (404 of 470 questions). Question by question, 14 were answered only by Monomem and 8 only by agentmemory. That gap is not significant (exact McNemar test, p = 0.29). It is a tie. Two more things I will not hide: Monomem's ranking was tuned on half of this question set, so the fairer figure is the other half: R@5 97.5, Rall@5 86.2. The repo says so. Another system, Vestige, reports a higher score than mine (its own number, which I have not re-run). It is named in the docs. Why post a tie? Because memory search is turning into a commodity. What I think still matters is trust: who wrote a note, whether an outside web page could have poisoned it, and whether you can undo it. Monomem's own attack check ( monomem check --attacks ) replays 26 known poisoning attacks on a copy of your store. Two are known misses (a reworded override, and self-poisoning), and the README lists them next to the headline number. It is pattern matching, so a reworded attack it does not know can get through. Everything runs on your computer in one file: no cloud, no account. MIT licence. Beta, not independently security-reviewed. Reproduce the numbers: monomem bench --longmemeval ... --per-question out.ndjson (instructions in docs/BENCHMARK.md). If you can beat or break it, tell me. Repo: https://github.com/calasdan-sketch/monomem Using it at work? Team setup and support: https://calasautomations.com/devtools/monomem/#teams

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/calasdansketch/i-re-ran-a-rivals-memory-benchmark-it-tied-mine-here-is-the-interesting-part-191c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
