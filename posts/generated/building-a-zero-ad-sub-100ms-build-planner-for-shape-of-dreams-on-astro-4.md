---
title: "Building a Zero-Ad, Sub-100ms Build Planner for Shape of Dreams on Astro 4"
slug: "building-a-zero-ad-sub-100ms-build-planner-for-shape-of-dreams-on-astro-4"
author: "Echo Zhang"
source: "devto_webdev"
published: "Tue, 20 Oct 2026 21:03:22 +0000"
description: "The Problem with Gaming Wikis in 2026 If you play deep roguelites or action RPGs like Shape of Dreams , you know the pain of looking up game mechanics. Histo..."
keywords: "build, shape, dreams, game, essences, cooldown, planner, wiki"
generated: "2026-10-20T21:26:05.882974"
---

# Building a Zero-Ad, Sub-100ms Build Planner for Shape of Dreams on Astro 4

## Overview

The Problem with Gaming Wikis in 2026 If you play deep roguelites or action RPGs like Shape of Dreams , you know the pain of looking up game mechanics. Historically, community documentation has been monopolized by ad-bloated MediaWiki or Fandom hubs packed with autoplaying video banners, intrusive interstitials, and slow 4-second page loads. Worse yet, patch balance numbers are frequently out of date, leading players to make suboptimal build choices. We decided to build an open, zero-ad, client-side web companion: Shape of Dreams Wiki & Interactive Build Planner . Here is how we designed and engineered it for sub-100ms performance and verified accuracy. 1. Deep Mechanics & Data Modeling Shape of Dreams features intricate theorycrafting layers across its 9 Travelers (including Cetus from the recent v1.4 Starless Path update): 93 Essences : Unique passive gems modifying skill behavior, with complex damage scaling and elemental conversions. 196 Hero Stars : Passive celestial talent nodes tailored for each character. Memories (Active Skills) : Dual-slot abilities with cooldown thresholds and combo mechanics. The cooldown reduction in the game follows a diminishing return curve based on Memory Haste: $$\text{Actual Cooldown} = \frac{\text{Base Cooldown}}{1 + \frac{\text{Memory Haste}}{100}}$$ To model this accurately without game client de-sync, our build engine consumes verified game-asset schemas directly, ensuring exact floating-point precision for damage amplification, barrier conversion, and cooldown caps. 2. Engineering Architecture: 0-Backend, Instant Client State To guarantee instantaneous feedback when theorycrafting builds on mobile or desktop, we eliminated server roundtrips: A. Static Pre-Rendering with Astro 4 All database pages—including the compendium of 93 Essences and character sheets—are pre-rendered to pure semantic HTML. LCP (Largest Contentful Paint) : < 120ms CLS (Cumulative Layout Shift) : 0.00 Third-Party Tracker Bloat : Zero B. Micro-Hydrated Island for the Calculator The Shape of Dreams Build Planner runs as an isolated, lightweight reactive island. When swapping a Memory or socketing an Essence, active DPS, effective cooldowns, and defense stats recalculate in under 16ms within a single animation frame. C. Stateless URL Serialization Instead of requiring user sign-ups or PostgreSQL databases for saving builds, entire character configurations serialize into a compact base64 URL hash: // Compact state serialization for instant sharing const serializedState = btoa ( JSON . stringify ({ traveler : ' cetus ' , memories : [ ' WinterDive ' , ' Permafrost ' ], essences : [ ' Gem_L_SolarEye ' , ' Gem_E_Twilight ' ], stars : [ 1 , 5 , 12 ] })); window . location . hash = `build= ${ serializedState } ` ; Players can copy their URL and immediately share full build setups on Discord or Reddit without creating accounts. 3. Open Source Datasets & Live Tools We believe game databases should be accessible to everyone in the community. We have published the cleaned datasets and interactive tools openly: 🎮 Main Hub & Database : shapeofdreams.wiki 🛠️ Interactive Build Planner : shapeofdreams.wiki/builds 💎 All 93 Essences Compendium : shapeofdreams.wiki/essences 📦 Open Game Dataset on GitHub : github.com/zjianchun/shape-of-dreams-database Feel free to test out build synergies and let us know what features or calculations you'd like to see next!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/powerechozhang/building-a-zero-ad-sub-100ms-build-planner-for-shape-of-dreams-on-astro-4-2630

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
