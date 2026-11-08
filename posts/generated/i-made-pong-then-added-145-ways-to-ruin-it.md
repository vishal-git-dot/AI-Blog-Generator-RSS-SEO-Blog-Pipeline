---
title: "I made Pong, then added 145 ways to ruin it"
slug: "i-made-pong-then-added-145-ways-to-ruin-it"
author: "Gotharden"
source: "devto_python"
published: "Sun, 08 Nov 2026 12:52:26 +0000"
description: "It started with a pretty simple idea, i wanted a more fun version of Pong that I could just launch and play offline The original game is great, but after a w..."
keywords: "game, pong, wanted, can, event, effects, events, simple"
generated: "2026-11-08T13:02:50.717379"
---

# I made Pong, then added 145 ways to ruin it

## Overview

It started with a pretty simple idea, i wanted a more fun version of Pong that I could just launch and play offline The original game is great, but after a while, matches can become a little repetitive. I wanted something that kept the familiar Pong gameplay but made every match less predictable. That's how Pong: Chaos Edition started. The game is written in Python using Pygame, the foundation is obviously still regular Pong: two paddles, a ball, a scoreboard, a CPU opponent and local multiplayer (if you want) I wanted to keep that foundation relatively simple because almost everything else would be built around it. The first major addition was the event system. Instead of having the game follow exactly the same rules throughout a match, events can temporarily change how things work. You might get multiple balls, different paddle sizes, unusual movement, obstacles or effects that interfere with your controls. Some events are helpful, while others are deliberately annoying. One of the more interesting parts of the development was figuring out how to make events affect the same game without constantly interfering with each other. For example, imagine one event making a paddle larger while another makes it smaller or changes its movement speed. When an event ends, it should only remove the effects that it introduced. I ended up using an ownership-based modifier system. Effects are associated with the event that created them, which allows the game to clean them up when that event finishes. This also makes it possible for several effects to coexist instead of having each event directly rewrite the same game properties. Sometimes it stops being Pong Another thing I wanted was for some events to go much further than simply changing the rules. Certain events temporarily take over the entire game and introduce a different mini-game. There are platforming challenges, football, tank battles, Snake, chess, quizzes, typing challenges and even a small first-person shooter called PONGDOOM. These aren't just visual effects on top of Pong, since they quite literally have their own gameplay, controls and objectives. The interesting part is that their results can still affect the original match, winning a takeover mini-game can earn you points. Giving it an old-school look and sound I also wanted the game to have a recognizable retro arcade appearance. Rather than relying entirely on standard fonts and modern rendering, I implemented a small 5x7 bitmap font, a restricted color palette and pixel-aligned drawing. There are also scanlines and other visual details to give it an older arcade feel. The audio was another part I wanted to handle myself, instead of relying entirely on prerecorded sound effects, the game generates its sounds using simple waveforms such as square waves, pulses and noise. The music follows the same general idea, with different tracks and moods depending on what's happening during a match. What's interesting about the project What I find interesting about this kind of project is how much can grow out of a relatively simple game. The underlying Pong mechanics haven't disappeared, they're still there, but an additional system can temporarily change almost every aspect of the experience. I originally just wanted a more entertaining way to play Pong offline, but hey, itt ended up becoming a much larger experiment in combining small gameplay systems into one chaotic arcade game. The project The source code is available on GitHub: Pong: Chaos Edition Feel free to check it out, explore the code or try the game yourself.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gotharden/i-made-pong-then-added-145-ways-to-ruin-it-4p35

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
