---
title: "AI coding agents still write your SDK's old API — so I built a type-checker to measure it"
slug: "ai-coding-agents-still-write-your-sdks-old-api-so-i-built-a-type-checker-to-measure-it"
author: "Kalpit Rathore"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 19:32:26 +0000"
description: "Here's a bug I kept hitting. I'd ask an AI assistant to write some code against a library — Prisma, the Vercel AI SDK, Zod — and the code would look complete..."
keywords: "model, sdk, code, not, you, tool, city, api"
generated: "2026-07-20T19:49:00.046493"
---

# AI coding agents still write your SDK's old API — so I built a type-checker to measure it

## Overview

Here's a bug I kept hitting. I'd ask an AI assistant to write some code against a library — Prisma, the Vercel AI SDK, Zod — and the code would look completely right. Clean, idiomatic, exactly the shape I expected. Then I'd run it, and it wouldn't compile. The reason was always the same: the library had shipped a new major version, and the model was writing the previous major's API from memory. parameters instead of inputSchema . required_error instead of error . A new PrismaClient({ datasources }) call that no longer exists. Small things — but enough to break the build on the first try. Models are frozen at their training cutoff. Libraries are not. So there's a gap between "the API the model reaches for" and "the API you actually have installed" — and that gap is widest right after a library ships a breaking change. I wanted to know: how big is that gap, exactly — and can I measure it objectively? So I built SDKProof . The method: let the compiler be the judge The trick to measuring this without hand-waving is to not use an LLM to grade an LLM. Instead: Generate. Have a model solve 10–15 realistic tasks for a given SDK ("define a tool that returns the weather", "make an optional field with a custom error message"). Type-check. Drop each solution into a fixture that has the real, current package installed, and run tsc --noEmit . Score. Pass = compiles clean. Fail = the compiler's own diagnostics, classified into failure patterns. No LLM judge. No "looks plausible." The installed package's type definitions are the ground truth, and tsc is the referee. A pass means the code would actually build against the version you have. One design detail that matters: the prompts name the functions but never the option names . I ask for "a tool with a description and an input schema," not "use inputSchema ." That way I'm measuring what the model naturally reaches for — not whether it can echo back a name I already handed it. What I found Running claude-opus-4-8 across three SDKs: SDK Package Score Where it breaks Prisma 7 @prisma/client 80 / 100 still writes removed v6 setup — new PrismaClient() with datasources , $use middleware Vercel AI SDK 7 ai 90 / 100 old tool wiring — parameters (now inputSchema ), removed maxSteps Zod 4 zod 90 / 100 removed required_error (now error ) — but nails the new 2-arg z.record() Here's a representative miss. Ask for a tool definition with the AI SDK and you tend to get this: import { tool } from ' ai ' ; import { z } from ' zod ' ; const weatherTool = tool ({ description : ' Get the weather for a city ' , parameters : z . object ({ city : z . string () }), // ✗ this was the v4 API execute : async ({ city }) => getWeather ( city ), }); Looks right. But against ai v7, tsc says: error TS2353: Object literal may only specify known properties, and 'parameters' does not exist in type 'Tool<...>'. Because the option was renamed to inputSchema : const weatherTool = tool ({ description : ' Get the weather for a city ' , inputSchema : z . object ({ city : z . string () }), // ✓ v5+ execute : async ({ city }) => getWeather ( city ), }); Everything else about the code is fine. It's one renamed key — and it's exactly the kind of thing that slips past a quick read but stops the build cold. The pattern: readiness tracks the drift window The interesting part isn't any single score — it's why they differ. Notice the newest breaking change scores worst. The Vercel AI SDK and Zod shipped their renames in 2025; by now the model has largely absorbed them and mostly gets them right (90/100). Prisma 7 is more recent, and the model hasn't caught up (80/100) — it still writes setup calls that were removed. That's the whole thesis: a model's "readiness" for an SDK tracks how recently that SDK changed. Which means this isn't a one-time audit. The gap: re-opens every time a library ships a new major, and shifts every time a model is retrained. So it's something to monitor , not measure once. A library that scores 95 today can drop to 70 the week it ships v-next — then climb back as the next model generation learns it. Honest limitations I'd rather you trust the number than oversell it: Type-check only. It measures whether the code uses the real, current API surface — not whether it runs correctly. Compiling clean ≠ bug-free. One model, for now. Comparing across models over time is the plan; a single model is a starting point, not the whole story. A snapshot. Every score is tied to a specific package version and model version. Both move. None of that breaks the signal — it just scopes it. "Does the model reach for API surface that still exists?" is a real, useful question, and the compiler answers it without opinion. Why it matters If you use AI to write code: be most skeptical right after a library ships a major. That's exactly when "looks right" and "compiles" diverge. Pin your versions and read the diff. If you maintain an SDK: the day you ship a breaking major, AI-assisted users hit broken code on their first try — until the models catch up. That's a support-and-perception cost that's currently invisible. SDKProof makes it visible. It's open source — add your own SDK Adding an SDK is about an afternoon: install the package, add a tsconfig , write a tasks file, register it. The harness handles generation, type-checking, and scoring. Board + full breakdowns: sdkproof.dev Code: github.com/Kalpitrathore/sdkproof I'm looking for the next SDKs to score. What library have you watched an AI assistant get wrong since its last major? Tell me and I'll run it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kalpitrathore/ai-coding-agents-still-write-your-sdks-old-api-so-i-built-a-type-checker-to-measure-it-alk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
