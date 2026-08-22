---
title: "I built an npm package that catches API contract drift before your users do"
slug: "i-built-an-npm-package-that-catches-api-contract-drift-before-your-users-do"
author: "Nakshatra Garg"
source: "devto_webdev"
published: "Sat, 22 Aug 2026 12:33:25 +0000"
description: "You've seen this before. Backend quietly renames user_id to userId . Or changes amount from a number to a string. Or drops a field entirely. The TypeScript t..."
keywords: "api, type, your, string, diff, you, before, every"
generated: "2026-08-22T12:48:49.583344"
---

# I built an npm package that catches API contract drift before your users do

## Overview

You've seen this before. Backend quietly renames user_id to userId . Or changes amount from a number to a string. Or drops a field entirely. The TypeScript types go stale. Nobody updates the frontend. And three days later, a user files a bug report about a blank screen. This happens in every team, at every scale. I've personally shipped three production bugs in fintech because of it — and in fintech, a broken loan amount field is not a "minor UI glitch." So I built something to stop it. Introducing @nakshatra6350/api-diff A zero-config fetch interceptor that watches every API response at runtime and tells you the moment something drifts from what you expected. npm install @nakshatra6350/api-diff The entire setup is 7 lines import { init , defineSchema } from ' @nakshatra6350/api-diff ' ; defineSchema ( ' /api/users ' , { id : { type : ' string ' }, name : { type : ' string ' }, email : { type : ' string ' }, }); init ( ' warn ' ); That's it. Drop this in your app's entry point. Every fetch call to /api/users is now contract-checked automatically. When your backend ships a breaking change, you'll see this in your console immediately: [api-diff] Contract drift on /api/users: • email: expected string, got missing • id: expected string, got number Before your users see anything. Before Sentry fires. Before the support tickets come in. Three modes for three environments init ( ' warn ' ); // Development — console.warn, non-blocking init ( ' throw ' ); // Tests / CI — throws an Error, fails the suite init ( ' silent ' ); // Production — silent collection, no noise In your test suite, flip it to throw mode and API drift becomes a failing test — it gets caught in CI before it ever reaches production. Nested objects? Handled. defineSchema ( ' /api/loans ' , { loanId : { type : ' string ' }, amount : { type : ' number ' }, status : { type : ' string ' }, user : { type : ' object ' , fields : { id : { type : ' string ' }, name : { type : ' string ' }, } }, }); The diff engine recurses into nested objects and reports the exact path that drifted — user.name: expected string, got missing — not just a vague "response mismatch." How it works under the hood You call defineSchema() to register URL → schema pairs in an internal registry init() wraps globalThis.fetch with a thin interceptor Every fetch call passes through — if the URL matches a schema, the response is cloned (your app gets the original, untouched) The clone is parsed and deep-compared field by field, type by type Drift is reported based on your chosen mode Zero latency added to your actual requests The interceptor adds no overhead to unmatched requests and only clones responses on matched ones — the clone is a native browser API, not a re-fetch. Why not just use Zod or OpenAPI validators? Fair question. Here's how I think about it: Tool What it's for Zod Compile-time + runtime validation wired into your data layer. Great, but requires you to own and update the schema actively. OpenAPI validators Full contract testing with generated specs. Powerful, but heavy — you need backend cooperation and a build step. api-diff A lightweight safety net at the fetch layer. No backend changes, no code-gen, no build step. Drop it in, define what you expect, move on. These tools aren't competitors. I use Zod for domain validation and api-diff as an early warning system at the network boundary. Full TypeScript support, zero extra packages import type { ApiSchema , DiffResult , DriftItem , DiffMode } from ' @nakshatra6350/api-diff ' ; Types ship with the package. No @types/ install needed. What's coming in v0.2.0 Array item validation — define a schema for items inside array responses onDrift callback — pipe drift events to Sentry, analytics, or your own endpoint - Vite plugin — define schemas in a config file instead of in code Links 📦 npm → npmjs.com/package/@nakshatra6350/api-diff 🐙 GitHub → github.com/nakshatra6350/api-diff Built this after 2.5 years of fintech frontend work watching silent API failures slip past TypeScript into production. If you've felt this pain, give it a try and open an issue with feedback — every response shape I haven't thought of yet is a bug I want to know about.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nakshatra6350/i-built-an-npm-package-that-catches-api-contract-drift-before-your-users-do-5d55

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
