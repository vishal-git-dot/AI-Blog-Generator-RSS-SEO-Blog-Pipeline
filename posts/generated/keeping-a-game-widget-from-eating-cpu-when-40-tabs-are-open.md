---
title: "Keeping a game widget from eating CPU when 40 tabs are open"
slug: "keeping-a-game-widget-from-eating-cpu-when-40-tabs-are-open"
author: "haibo kan"
source: "devto_webdev"
published: "Fri, 06 Nov 2026 05:47:33 +0000"
description: "This is a follow-up to my earlier write-up, Injecting a game widget into every page without breaking the host site's CSS . That one covered style isolation. ..."
keywords: "game, one, you, state, widget, loop, three, when"
generated: "2026-11-06T05:56:57.118255"
---

# Keeping a game widget from eating CPU when 40 tabs are open

## Overview

This is a follow-up to my earlier write-up, Injecting a game widget into every page without breaking the host site's CSS . That one covered style isolation. This one is about lifecycle, which turned out to be the harder half. The product constraint sounds innocuous: a small draggable ball sits in the corner of every page, you click it, pick a game, press Space, and click again to fold it away. The part that matters is the last step — folding it away pauses the game and keeps the state, so you come back to the same round. If you take that literally on every tab, you have 40 game loops. That's the design problem. The widget is everywhere; the game is not The content script that mounts the ball is tiny: one host element, a Shadow DOM root, a drag handler. It does no work when idle. The game itself doesn't exist until you pick one. When you pick a game, an iframe is created on demand, the game bundle loads into it, and the loop starts. When you switch games or collapse the panel, the iframe is destroyed. There is no persistent background page holding a loop, and no service worker ticking on a timer. That gives a useful invariant: the number of running game loops is at most one per active widget, and usually zero. Forty tabs means forty tiny idle elements, not forty requestAnimationFrame loops. Three different kinds of "pause" I initially lumped everything under "auto-pause", and it caused bugs, because the three cases have different semantics: Collapse / Esc — an explicit user action. Freeze immediately and keep the state. This is the one people notice, and the one that has to feel instant. Tab hidden — the browser already throttles requestAnimationFrame in background tabs. I don't need to tear anything down; a loop driven by rAF naturally stops advancing. Fighting the browser here just adds a state-restore bug. Switching games — this is not a pause at all. Tear down the iframe and start clean. Keeping a hidden game alive "just in case" is what creates the 40-loop problem in the first place. Separating those three removed most of the state bugs I had early on. Store the smallest thing that can restore a round The tempting approach is to serialize the whole game object. Don't. Most of it is derived state — sprite positions, timers, DOM nodes — and rehydrating it is both brittle and pointless. What actually needs to survive: { score : 120 , level : 3 , grid : [...], // board state only direction : ' right ' , nextDirection : ' right ' , tick : 1840 // logical ticks elapsed, not wall-clock ms } tick instead of Date.now() matters. If your speed curve is derived from elapsed wall-clock time, a round that sat paused for twenty minutes comes back at a different difficulty from the one you left. A logical counter that only advances inside the loop doesn't have that problem. The other trap is writing on every frame. chrome.storage.local is not a frame buffer. I write on pause, on game over, and on a coarse interval — never inside the loop. Click-through is a pointer-events problem with one exception "Click-through mode" means the widget stops intercepting your mouse entirely, so it never steals a click from the page underneath. The obvious implementation is pointer-events: none on the widget surface. The exception is the drag handle: it still needs pointer events while everything else doesn't. So the handle keeps pointer-events: auto and the rest is disabled as a layer, rather than toggling one global flag and then wondering why the ball can't be moved anymore. What I'd do differently Two things: I treated "paused" as one state for too long. Collapse, background tab and game switch are three different transitions and should have been three code paths from day one. I should have designed the save-state shape before the game code. Deciding what to serialize after the fact means the game object leaks into storage and you end up versioning a format nobody designed. None of this is novel — it's the same lifecycle discipline you'd apply to any embedded widget. It's just easy to forget when the thing you're embedding happens to be a game. If you want to see it in practice, the extension is called InTab Arcade. Three games are free with no account; a retro arcade cabinet is a paid upgrade.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/haibo_kan_9d238a8ee4215b9/keeping-a-game-widget-from-eating-cpu-when-40-tabs-are-open-44aj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
