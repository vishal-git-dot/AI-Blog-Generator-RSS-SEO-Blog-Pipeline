---
title: "Building RealityOS: a deterministic world with an AI reality-show surface"
slug: "building-realityos-a-deterministic-world-with-an-ai-reality-show-surface"
author: "Harish Kotra (he/him)"
source: "devto_ai"
published: "Sun, 02 Aug 2026 13:28:36 +0000"
description: "AI agents are compelling when they look like they have a world, not when a screen is filled with chat bubbles. RealityOS is an experiment in that distinction..."
keywords: "state, viewer, not, simulator, world, next, events, contestants"
generated: "2026-08-02T13:39:46.253360"
---

# Building RealityOS: a deterministic world with an AI reality-show surface

## Overview

AI agents are compelling when they look like they have a world, not when a screen is filled with chat bubbles. RealityOS is an experiment in that distinction: a persistent house of 100 contestants, shown as a live 3D spectator experience. The design decision that shapes the whole project is simple: the simulator owns facts; models own interpretation. The problem with asking an LLM everything An LLM loop that asks every contestant “what do you do next?” every few seconds is expensive, inconsistent, and impossible to replay with confidence. It also gives a language model authority over mundane facts it should not own: whether someone is hungry, whether a room is full, or whether a party physically happened. RealityOS instead advances a deterministic world on a tick. Each system receives state, applies its rule, and emits typed events: export interface SimulationSystem { readonly name : string ; apply ( state : WorldState ): readonly WorldEvent []; } export class DeterministicSimulation { advance ( state : WorldState ) { const next = structuredClone ({ ... state , tick : state . tick + 1 }); const events = this . systems . flatMap (( system ) => system . apply ( next )); return { state : next , events }; } } Needs are resources that recover at a critical point rather than freezing at zero. The same principle will ultimately drive eating, resting, and social routines: deterministic transitions produce reliable facts; agents decide why a situation matters to them. Events, not polling The second core choice is to activate reasoning from events. A model should be prompted after an important encounter, a relationship change, a memory, or a viewer event—not because three seconds elapsed. flowchart LR Tick --> Systems Systems --> DomainEvents DomainEvents --> ImpactRouter ImpactRouter -->|"only affected contestants"| LLM LLM --> IntentValidator IntentValidator --> FutureSimulationCommand The EventReasoningRouter already implements this selection boundary. In its mature form, it will assemble personality, retrieved memory, social context, and a constrained set of legal actions, then record both response and validated outcome for auditability. A viewer action should create pressure, not puppet contestants The party button is a good small example. A viewer does not select who talks to whom. They request a world event. The server broadcasts the command, the simulator deterministically assigns the garden as a temporary destination, and the browser receives movement events with a new world state. sequenceDiagram participant Viewer participant SocketAPI participant Simulator participant ThreeHouse Viewer->>SocketAPI: viewer:command("party") SocketAPI->>Simulator: viewer:event("party") Simulator->>Simulator: destination = garden for ten ticks Simulator->>SocketAPI: contestant.moved + state batch SocketAPI->>ThreeHouse: world:updated ThreeHouse->>ThreeHouse: lerp each contestant to new location That is the beginning of a useful rule: viewers influence context, contestants retain agency. The 3D house is the product surface The web app is built with Next.js, React Three Fiber, Drei, and Three.js. The house is a cutaway set rather than a dashboard; every contestant is a small clickable character. Their identity is deterministic so it does not flicker between live updates or later replay. // A stable golden-angle hue avoids a repeating color palette. const outfit = `hsl( ${( index * 137.508 ) % 360 } 58% ${ 38 + ( index % 4 ) * 7 } %)` ; const height = 0.88 + ( index % 6 ) * 0.045 ; Characters are intentionally lightweight geometry today: head, hair silhouette, body, legs, occasional glasses, and occasional hats. This keeps 100 visible contestants performant while creating a strong hook for future GLTF avatars and animation states. Runtime topology The services are deliberately separate. The web app can be deployed independently; the simulator can continue while no viewer is present. The current Prisma schema models shows, contestants, event records, memories, and encrypted provider credentials, ready for the next persistence implementation phase. What comes next The interesting work is not adding more boxes to the interface. It is making the world legible and trustworthy as it becomes deeper: Append simulation events in Postgres and derive state from the log. Add contestant profiles, relationships, and goals. Connect server-side model providers to a typed, validated intention contract. Store episodic and relationship memories, then retrieve them selectively. Add confession-room reflections, event narration, daily Gazette articles, clips, and viewer polling. Implement replay/forked timelines and show-level permissions. RealityOS is a bet that the most watchable AI systems will feel less like a chat window and more like a place with rules, history, and consequences. Code & more: https://www.dailybuild.xyz/project/210-realityos

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/harishkotra/building-realityos-a-deterministic-world-with-an-ai-reality-show-surface-3nli

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
