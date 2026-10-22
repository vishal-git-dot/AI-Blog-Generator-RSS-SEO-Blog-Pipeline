---
title: "Your agent forgot a decision you made last week. Mine did too."
slug: "your-agent-forgot-a-decision-you-made-last-week-mine-did-too"
author: "TECHDEV"
source: "devto_ai"
published: "Thu, 22 Oct 2026 03:59:57 +0000"
description: "Your agent forgot a decision you made last week. Mine did too. Last month my team reversed a queue decision. Nobody could say why we had picked the first des..."
keywords: "memgraph, decision, what, source, you, graph, superseded, queue"
generated: "2026-10-22T04:08:58.352246"
---

# Your agent forgot a decision you made last week. Mine did too.

## Overview

Your agent forgot a decision you made last week. Mine did too. Last month my team reversed a queue decision. Nobody could say why we had picked the first design, what evidence it rested on, or who had signed off on the replacement. The old design was still half-wired in as a "fallback", quietly depending on the thing we had just replaced. We found out in production. Vector RAG remembers text . It does not remember decisions — what was chosen, what it rested on, what contradicted it, and what replaced it. So I built a tiny local graph for exactly that: memgraph . What it does One zero-dependency Node.js CLI. No network, no server, no embeddings. The store is a single JSON file you can commit next to your code. memgraph init memgraph add --type decision --title "Use Postgres LISTEN/NOTIFY for the queue" --source "ADR-014" memgraph add --type fact --title "NOTIFY payloads cap at 8000 bytes" --source "Postgres docs" memgraph link m-002 m-001 --relation contradicts memgraph add --type decision --title "Switch the queue to Redis Streams" --source "ADR-019" memgraph supersede m-001 m-003 --reason "payload cap makes NOTIFY the wrong tool" Three questions it answers, fast: Why did we decide this? memgraph why m-003 — source, supporters, contradictions, supersession. Is anything stale or contradictory? memgraph check — unresolved contradictions, live nodes resting on superseded ones, sourceless claims. What do we believe? memgraph list — every node, with superseded ones marked. memgraph check exits 1 when it finds an error, so it works as a CI gate: a PR that introduces a contradiction, or keeps depending on a superseded decision, fails before it merges. Demo The repo ships a small team graph — a queue decision, the fact that killed it, its replacement, and one leftover fallback still depending on the dead design: sh examples/run-demo.sh memgraph check on that graph reports exactly two problems: the fallback reader depends on a superseded decision, and one open question has no source. The contradiction between the payload-cap fact and the old decision does not get flagged — the old decision was superseded, so that contradiction is resolved history, not a live conflict. One honesty note A graph is only as good as what you record. memgraph cannot tell you whether a source is true — it tells you where every claim came from and whether the graph still holds together. A decision with no source is a rumor with formatting; that is why check flags it. And when a decision changes, supersede it — don't delete it. Deleting history is how teams end up re-litigating the same choice every six months. Repo: https://github.com/techdevfun/memgraph — MIT, zero dependencies, Node.js 18+.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/techdevfun/your-agent-forgot-a-decision-you-made-last-week-mine-did-too-1ba9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
