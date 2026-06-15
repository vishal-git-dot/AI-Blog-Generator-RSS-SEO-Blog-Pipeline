---
title: "I Built Frogger in 120 Lines of Vanilla JavaScript"
slug: "i-built-frogger-in-120-lines-of-vanilla-javascript"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 20:59:40 +0000"
description: "Frogger looks like a different beast from a side-scroller — roads, rivers, hopping, riding logs. But under the hood it's one of the cleanest little game-desi..."
keywords: "you, frog, frogger, one, game, row, log, its"
generated: "2026-06-15T21:11:31.716104"
---

# I Built Frogger in 120 Lines of Vanilla JavaScript

## Overview

Frogger looks like a different beast from a side-scroller — roads, rivers, hopping, riding logs. But under the hood it's one of the cleanest little game-design lessons there is: lanes of moving rectangles, and one rule per terrain. Let me build it from scratch in vanilla JavaScript. This is Day 8 of GameFromZero, where I rebuild a classic game every day. Hopping, not gliding Unlike Flappy Bird's smooth physics, Frogger moves in discrete hops . Each arrow press changes the frog's row (up/down) or shifts it one cell left/right. Snapping to a grid is exactly what gives Frogger its timing-puzzle feel — you commit to a square and live with it. if ( key === " ArrowUp " ) frog . row ++ ; if ( key === " ArrowLeft " ) frog . x -= CELL ; Lanes that scroll and wrap Each road or river row is a "lane" with its own direction and speed. Every frame the obstacles slide along; when one exits one side it reappears on the other. That endless wrap is what makes a few rectangles feel like continuous traffic. for ( const o of lane . items ) { o . x += lane . speed ; if ( o . x > W ) o . x = - o . w ; // wrap around } Two terrains, two opposite rules This is the heart of Frogger, and it's beautifully symmetric: The road kills on contact. On a road row, the frog dies if its box overlaps any car's box — the same axis-aligned overlap check from every collision-based game. if ( onRoad && cars . some ( car => overlap ( frog , car ))) die (); The river is inverted. Here, open water kills and a log saves you. So you must be standing on a log — and while you are, the log carries you sideways at its speed. Drift off the screen edge and you drown. const log = logs . find ( l => overlap ( frog , l )); if ( onRiver ) log ? ( frog . x += log . speed ) : die (); Same overlap test, opposite consequence. That single inversion is what makes the river feel so different from the road. Reaching the top When the frog reaches the top grass row, you score and it respawns at the bottom to do it again. Add a few lives and you've got the full game loop: if ( frog . row === TOP ) { score ++ ; resetFrog (); } What you actually learn Frogger teaches a pattern you'll reuse constantly: independent lanes of recycled objects, each with its own behaviour, and per-terrain rules for the player. That structure scales up to endless runners, tower-defense paths, traffic sims — anything with "stuff moving across the screen in tracks." And the deeper lesson: a game's feel often comes from one clever rule (here, "the river's logic is flipped"), not from piles of code. Frogger is maybe 120 lines, and most of it is drawing rectangles. 👉 Play it (arrow keys — click the board first): https://dev48v.infy.uk/game/day8-frogger.html 🌐 All games: https://dev48v.infy.uk/gamefromzero.php Tomorrow: Space Invaders.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-frogger-in-120-lines-of-vanilla-javascript-23c5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
