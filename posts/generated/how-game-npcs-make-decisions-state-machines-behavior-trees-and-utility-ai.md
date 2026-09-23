---
title: "How Game NPCs Make Decisions: State Machines, Behavior Trees And Utility AI"
slug: "how-game-npcs-make-decisions-state-machines-behavior-trees-and-utility-ai"
author: "Paul Crinigan"
source: "devto_ai"
published: "Wed, 23 Sep 2026 16:27:34 +0000"
description: "If you write software for a living you have probably built a decision system: a rules engine, a router, a workflow that picks a branch. Game developers have ..."
keywords: "they, you, state, four, behavior, them, because, where"
generated: "2026-09-23T16:33:33.338368"
---

# How Game NPCs Make Decisions: State Machines, Behavior Trees And Utility AI

## Overview

If you write software for a living you have probably built a decision system: a rules engine, a router, a workflow that picks a branch. Game developers have been building those under hard real time constraints for forty years, and almost none of it involves machine learning, so the patterns are worth a look even if you never ship a game. The Four Patterns Behind Almost Every NPC Finite state machines give a character one active state at a time. Patrol, alert, chase, attack, with rules for moving between them. They are trivial to reason about and cheap at runtime, and they fall apart once the state count grows, because transitions grow roughly with the square of the number of states. Behavior trees replace that web with a hierarchy that gets walked from the root each tick. Sequence nodes run children in order and need all of them to succeed. Selector nodes try children in order and stop at the first success, which is how fallback chains get expressed: attack if possible, otherwise take cover, otherwise run. They became the AAA default around 2005 and they are the reason a modern enemy can gain a behavior without anyone rewiring the rest. Steering behaviors handle movement once a destination exists. Craig Reynolds described the three flocking rules in 1987, separation, alignment and cohesion, and those three forces still drive squads moving down a corridor, crowds fleeing an explosion and birds in the background of a menu screen. Individual behaviors like seek, arrive, flee and wander get weighted and blended, usually with collision avoidance given absolute priority so nothing walks into a wall while holding formation. Utility AI skips explicit structure entirely and scores every possible action against the current world state, then runs the winner. The Sims is the famous example, where every object in the world advertises a utility value that pulls characters toward it. It is the most flexible of the four and the hardest to debug, because the answer to why did it do that is a number that beat other numbers. Why Enemies Feel Smart When They Are Not The four ghosts in Pac-Man are four targeting functions. Blinky heads straight for you. Pinky aims a few tiles ahead of where you are going. Inky uses an offset computed from Blinky position. Clyde alternates between chasing and giving up. Players read those as four personalities with different attitudes, and they are four small functions with no state worth mentioning. The marines in Half-Life were the same trick at a larger scale. They were not doing deep tactical reasoning, their behaviors were tuned so that the timing and the callouts read as coordination. That is the central lesson of the field: perception beats complexity. A simple system with responsive timing feels smarter than a sophisticated one with awkward pacing, every time. The practical version of this is the pattern vocabulary encounters get built from. Patrollers walk a route and give the player something to learn. Turrets hold a zone and force movement decisions. Flankers push wide while something else holds attention from the front. Rushers collapse the distance and disrupt positioning. Supporters heal or buff and make the player choose a priority. None of them is interesting alone. Mixed into one encounter they produce pressure that a player has to think their way out of, which is the actual goal. The full game AI guide goes through each pattern along with the pathfinding layer underneath them. Difficulty That Adjusts Without Telling You Static difficulty settings tune parameters: health, damage, aggression, drop rates. They are honest and they are coarse, and most players sit between the bands or move between them as they learn. Dynamic difficulty adjustment watches how the player is doing and quietly moves those numbers. Resident Evil 4 is the textbook case, tracking damage taken and deaths and adjusting enemy accuracy, aggression and item drops behind the scenes. The reason it is admired rather than resented is that it never announces itself and never makes a large jump. The more expensive version changes behavior rather than numbers. Instead of dealing less damage, the enemy reacts a beat slower, picks a worse position, or telegraphs longer. It costs more to author because you are writing several tiers of AI, and it feels far better, because the enemy still looks like it is trying. The LLM Question Everything above is deterministic, and that is the feature. Designers can author the experience, balance it precisely, and know an NPC will never break the fiction or say something the studio has to apologize for. The price is that NPCs feel scripted, because they are. Language models offer the opposite trade. Freeform dialogue, memory of earlier conversations, sensible answers to questions nobody anticipated. They also add hundreds of milliseconds of latency, per interaction cost that scales with playtime, content safety work, and nondeterminism that makes a guaranteed story beat impossible. So the shape that ships is hybrid. Classic systems own combat, navigation and world simulation, where failure is visible and control matters. Generative models own dialogue, quest text and reactive narration, where surprise is the product. The Takeaway The transferable idea for anyone building agents is not A star or behavior trees. It is that games settled the predictability argument decades ago by putting deterministic systems wherever a user can see failure, and keeping the unpredictable parts at the edges where surprise is welcome. Most agent architectures would be better off with the same split.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulcrinigan/how-game-npcs-make-decisions-state-machines-behavior-trees-and-utility-ai-4k71

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
