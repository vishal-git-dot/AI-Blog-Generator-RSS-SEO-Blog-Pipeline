---
title: "Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein"
slug: "show-hn-gravity-interactive-solar-system-simulator-from-newton-to-einstein"
author: "qunabu"
source: "hackernews"
published: "Tue, 09 Jun 2026 11:46:40 +0000"
description: "Just for fun and self education, I've built this over a weekend to teach myself why orbits exist, not just show planets going around. Something that was neve..."
keywords: "real, gravity, scale, just, you, can, physics, show"
generated: "2026-06-09T15:18:05.197929"
---

# Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein

## Overview

Just for fun and self education, I've built this over a weekend to teach myself why orbits exist, not just show planets going around. Something that was never clearly explain to me in school. It opens with a guided tour that builds the idea up step by step: two bodies and the equal/opposite force, inertia (the Sun is removed and Earth just drifts straight), then "an orbit is falling and continuously missing," cosmic velocities with a little rocket, Voyager 1 & 2's real gravity assists (the clock runs the actual 1977–1989 dates so the planets orbit into their grand-tour alignment and the slingshots line up), and it ends on Einstein — gravity as curved spacetime, the classic rubber-sheet well. What's real: every body uses its real radius/mass and J2000 orbital elements; positions come from solving Kepler's equation each frame. You can toggle to an N-body mode (symplectic leapfrog) that shows live energy drift (~1e-6%) so you can see the integrator is honest. The only thing faked is scale — at true scale you can't see anything — so there's a toggle between true scale and a log-remapped "visual" scale, with physics always running in real AU. Tech: TypeScript + Three.js + Vite, fully client-side, no backend, works offline (surface textures are generated procedurally from value-noise; only Earth uses a real image). Source: https://github.com/qunabu/Gravity Happy to answer questions — and feedback on the physics or the explanations is very welcome. This project might be totally inaccurate in terms of real physics, this is how i do understand this on my own - i'm happy to confront this with reality Comments URL: https://news.ycombinator.com/item?id=48459837 Points: 48 # Comments: 14

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://qunabu.github.io/Gravity/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
