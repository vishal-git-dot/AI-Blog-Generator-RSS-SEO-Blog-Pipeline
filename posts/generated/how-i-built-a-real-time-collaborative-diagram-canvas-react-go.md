---
title: "How I built a real-time collaborative diagram canvas (React + Go)"
slug: "how-i-built-a-real-time-collaborative-diagram-canvas-react-go"
author: "Victor Agudo Gonzalez"
source: "devto_webdev"
published: "Tue, 30 Jun 2026 14:19:01 +0000"
description: "I wanted a fast way to sketch architecture diagrams and share them with other people live, without installing anything and without the heavy, corporate feel ..."
keywords: "not, node, hub, time, without, free, never, only"
generated: "2026-06-30T14:30:32.340880"
---

# How I built a real-time collaborative diagram canvas (React + Go)

## Overview

I wanted a fast way to sketch architecture diagrams and share them with other people live, without installing anything and without the heavy, corporate feel of most diagram tools. So I built Diagraw: a free infinite canvas with a hand-drawn look and real-time collaboration. It is free and works without an account. Here are the parts that were the most interesting to build. Edges are derived, never stored The first decision that paid off: node positions are the only source of truth. An edge just references the two nodes it connects (or two free points). The actual arrow geometry, clipped to each node's border, is recomputed on every render. That sounds wasteful, but it means moving a node keeps its arrows attached for free. There is no "update the arrows" code path, because arrows have no stored geometry to update. Geometry lives in world coordinates and is converted to screen coordinates only at render time (screen = world * zoom + translate), so panning and zooming never touch the data. The hand-drawn look, without rough.js The sketchy style is a small self-contained generator: a seeded PRNG (mulberry32) keyed by a hash of each node's id. The same node always perturbs the same way, so shapes do not "wobble" between renders, and they are only recomputed when a cache key changes (id + type + rounded size + color + roughness). No external drawing library. Real-time collaboration: a small Go hub The backend is a Go service with an in-memory WebSocket hub. Clients diff their local store into deltas (upsert / remove by id) and send only those; the hub relays them to the other participants and persists to MongoDB with a debounce, so a burst of edits is one write, not hundreds. Live cursors and presence are ephemeral messages that are relayed but never persisted. There is also a "presenter" mode: the owner broadcasts their viewport (throttled) so everyone else can follow their camera, which is great for walking a team through a diagram. The honest limitation Because the hub is in-process, the API runs at one replica per environment. It does not scale horizontally yet. The blocker is the in-memory hub, not the data; a shared pub/sub (Redis, NATS) would fix it. I have not needed it yet, and I would rather ship and learn than pre-scale for traffic I do not have. Importing Mermaid and docker-compose You can paste a Mermaid flowchart or a docker-compose file and Diagraw draws it for you. Two pieces make this work: A Sugiyama-style layered layout (longest-path ranking with back-edge handling) to place the nodes. Edge routing that bends a connector around groups instead of crossing them, turning it into a smooth curve when a straight line would cut through a layer. Getting the import to match what people drew in Mermaid was more fiddly than the layout itself (edge labels that became phantom nodes, quoted subgraphs, shape mapping). Inverse parsers are never as clean as the generators. Stack and infra Front end: React + TypeScript + Vite. Two zustand stores: one persisted document, one for transient gesture state that must not enter undo history. Backend: Go, hexagonal-ish (domain / use cases / adapters), Mongo or in-memory. Infra: a single small VPS, Docker Swarm behind Traefik, Cloudflare in front, daily off-site encrypted Mongo backups, CI-gated deploys. Try it / tell me where it breaks It is still early. If you draw something, I would love to know what felt slow or confusing, and whether the Mermaid import did what you expected. Link: Diagraw.com Thanks for reading.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/victor_agudogonzalez_51b/how-i-built-a-real-time-collaborative-diagram-canvas-react-go-4g2o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
