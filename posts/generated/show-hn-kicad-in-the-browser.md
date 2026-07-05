---
title: "Show HN: KiCad in the Browser"
slug: "show-hn-kicad-in-the-browser"
author: "ViktorEE"
source: "hackernews"
published: "Sun, 05 Jul 2026 12:06:57 +0000"
description: "KiCad, a PCB EDA suite is now working in a browser, you can try it at the link, there's a demo project or you can bring your own. Firefox is best, Chrome is ..."
keywords: "you, kicad, can, code, native, there, project, but"
generated: "2026-07-05T13:51:56.694785"
---

# Show HN: KiCad in the Browser

## Overview

KiCad, a PCB EDA suite is now working in a browser, you can try it at the link, there's a demo project or you can bring your own. Firefox is best, Chrome is good, Safari is "working". We’re Emergence Engineering, a dev shop from Hungary, mostly working with rich text editors, CRDTs. PCBJam started as my (Viktor, CTO, ex-electrical engineer) hobby project but as time went on I put more and more energy into it, and a product started shaping up in my head, in the last few months we’ve started to focus on this project a bit more, and this is the first MVP~ish result. This project is a ton of fun, ton of learning, ton of improvements over improvements: - I thought there must be ways to emulate the PCB canvas OpenGL code on the web. And yes, there are a lot of ways, all of them very buggy. Turns out it’s faster to just write WebGL code that works with KiCad’s Graphics Abstraction Layer if you add the right intermediate debugging steps. I (with Claude) implemented the features and compared them to native at every step, then the app loaded up the first time and just worked. I spent weeks hunting weird emulation bugs before that. - There was an old wxWidgets web port as a starting point that helped a lot, bringing it up to the level KiCad needed is a long (and still ongoing) task. Thanks ahilss! - Pthreads on the web: with Emscripten it’s possible to port multithreaded apps (used by DRC, software 3D renderer). A lot of Emscripten features (Asyncify, Pthreads, native exceptions) are in a war with each other, but it’s possible. - Asyncify with native exceptions: Asyncify (used to make the WASM code suspend then call into the JS land, emulating blocking C++ calls by rewriting the WASM directly) is not compatible with native exceptions, even on the latest Binaryen version it can’t suspend inside catch arms. If you write a new Binaryen pass then it can, making the bundle 30-40% smaller and the app load in a second instead of 10. - Optimizing bundle size is a fun game. We just moved Open CASCADE into a separate lazy-loaded WASM module, moving from 180 to 130 MB (24 MB brotli), still on -O1. -O2 / -Oz etc will be more work than it looks. And a ton more problems like these above on a daily basis. A few months ago I had a barely loading laggy pcbnew that crashed when you looked at it wrong, now we have the whole application working. I should say with quite a few bugs still, but now it feels pretty close to native. There’s a lot of built up knowledge / code that we want to release as blogposts, mainline our changes to Binaryen / KiCad / wxWidgets, but I want to focus on the release first. Our wxWidgets port is quite close to the core, the KiCad is ~150 changed core files (mostly build scripts, some code changes too). The goal is to keep as close to the mainline as possible, and merge eventually. We’ll have a free tier for sure and something around $30/mo for bigger/closed projects, optional paid AI integration / self hosting / enterprise features / native & mobile version down the line. The goal is to build a product on top of KiCad (collaboration, AI integration, sharing, integrations), kind of like what Red Hat did with Linux back then. We’re heads down making it functional and have the first version up in a ~month or so. And of course we’re standing on the shoulders of the people who made KiCad & wxWidgets and we want to give back and contribute as much as possible, if you have an idea on how to do that best let me know, I released a few moderately successful open source projects, but I’ve never been a contributor. All of the front-end code is GPL (it has to be) and you can run this project if you want. You can find the sources at: https://github.com/emergence-engineering/pcbjam . Our company site is at: https://emergence-engineering.com/ Our crappy LP is at: https://www.pcbjam.com/ Comments URL: https://news.ycombinator.com/item?id=48793542 Points: 15 # Comments: 4

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://demo.pcbjam.com/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
