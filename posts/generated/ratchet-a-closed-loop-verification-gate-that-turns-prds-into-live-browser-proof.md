---
title: "Ratchet: A Closed-Loop Verification Gate That Turns PRDs into Live Browser Proof"
slug: "ratchet-a-closed-loop-verification-gate-that-turns-prds-into-live-browser-proof"
author: "Miracle Alajemba"
source: "devto_ai"
published: "Tue, 24 Nov 2026 22:06:57 +0000"
description: "AI coding agents are great at writing code, but they love saying "it's done" the moment unit tests pass—without ever checking if the app actually works in a ..."
keywords: "kane, cli, browser, verification, run, ratchet, closed, loop"
generated: "2026-11-24T22:10:49.164066"
---

# Ratchet: A Closed-Loop Verification Gate That Turns PRDs into Live Browser Proof

## Overview

AI coding agents are great at writing code, but they love saying "it's done" the moment unit tests pass—without ever checking if the app actually works in a real browser. To fix that, I built Ratchet : a closed-loop verification gate powered by Kane CLI that refuses to lock a build until 100% of your PRD's acceptance criteria are proven in a live browser. How the Closed Loop Works Instead of relying on an agent's self-reported completion, Ratchet drives Kane CLI headlessly and enforces a strict verification flow: Spec Sync: Reads the project's PRD and syncs acceptance criteria against Kane CLI's structured design and coverage state ( kane-cli cover gaps --json ), including safe no-op handling when the design is already up to date. Live Browser Verification: Executes real browser tests via kane-cli testrun run against the running application (tested against a Pro Plan checkout demo with SAVE20 promo pricing). Evidence-Backed Lock: Parses Kane's coverage rollup and evidence packs, failing closed ( locked: false ) until every use case and acceptance criterion is proven. What Kane CLI Caught During the Build Wiring a real browser verification loop surfaced issues that standard unit tests would never catch: Sync Edge Cases: Caught a subtle mismatch where Kane's EMPTY_DESIGN event was treated as a hard failure when non-blocking clarification gaps were present, leading to a cleaner no-op sync path. Root-Cause Triage via Evidence Packs: Using kane-cli evidence serve , Kane separated real application behavior from test/environment noise—flagging a canonical trailing-slash URL assertion issue ( http://localhost:4173 vs http://localhost:4173/ ) and a transient screenshot timeout, confirming zero application bugs in the checkout flow. Run It Locally bash # 1. Install, build, and run offline engine tests npm install && npm run build && npm test # 2. Start the demo app (Terminal 1) cd demo-app && python3 -m http.server 4173 # 3. Run live browser verification and inspect coverage (Terminal 2) cd demo-app && kane-cli testrun run && kane-cli cover gaps --json Check out the code on GitHub: Miracle-Alajemba/ratchet

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/miracle_alajemba_6b425827/ratchet-a-closed-loop-verification-gate-that-turns-prds-into-live-browser-proof-13j3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
