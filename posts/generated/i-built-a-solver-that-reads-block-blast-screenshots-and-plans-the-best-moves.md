---
title: "I Built a Solver That Reads Block Blast Screenshots and Plans the Best Moves"
slug: "i-built-a-solver-that-reads-block-blast-screenshots-and-plans-the-best-moves"
author: "michal"
source: "devto_python"
published: "Fri, 30 Oct 2026 21:52:48 +0000"
description: "Like a lot of people, I got hooked on Block Blast — and kept dying on boards that looked totally winnable. So I built a solver for it. The idea is simple: up..."
keywords: "board, solver, block, you, built, blast, screenshot, pieces"
generated: "2026-10-30T22:07:19.228988"
---

# I Built a Solver That Reads Block Blast Screenshots and Plans the Best Moves

## Overview

Like a lot of people, I got hooked on Block Blast — and kept dying on boards that looked totally winnable. So I built a solver for it. The idea is simple: upload a screenshot of your game, and the solver reads the board for you, then shows the best move for each of your 3 pieces, step by step. Try it live: https://blockblastsolversi.com Here's how it works. Two problems, not one Vision. A screenshot has to become data: an exact 8×8 board plus the shapes of the 3 pieces in the tray. Search. Given that board, try the placements for all 3 pieces and keep the sequence that leaves the board healthiest. Reading the board with Python The screenshot analysis runs on a small FastAPI service: Find the board area in the image and split it into an 8×8 grid Classify each cell (filled / empty) by sampling colors near the cell center Extract the tray pieces the same way, as mini shape grids Themes and skins change the block colors, so fixed RGB matching failed constantly. Comparing relative color differences instead fixed most of it — on 71 real test screenshots, board-cell detection lands around 99% accuracy. Planning the moves Once the board is data, the search is straightforward: Generate every legal placement for piece 1, 2 and 3 Simulate the game's line clears (rows + columns) after each sequence Score the final board: reward clears and combos, punish rough surfaces, trapped holes and clutter The search runs in the browser, so the scoring function has to be cheap and bad branches get pruned early. The result feels instant, even on a phone. Stack Next.js + TypeScript on the front end (search runs client-side) Python + FastAPI for screenshot analysis Capacitor wrapper for the Android app Links Live solver: https://blockblastsolversi.com GitHub showcase: https://github.com/buzdarama/block-blast-solver If you've built board-evaluation heuristics for puzzle games before, I'd genuinely like to hear how you scored "future flexibility" — that's the part I keep tweaking. ] GitHub showcase: https://github.com/buzdarama/block-blast-solver If you've built board-evaluation heuristics for puzzle games before, I'd genuinely like to hear how you scored "future flexibility" — that's the part I keep tweaking.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/michal15/i-built-a-solver-that-reads-block-blast-screenshots-and-plans-the-best-moves-3cj4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
