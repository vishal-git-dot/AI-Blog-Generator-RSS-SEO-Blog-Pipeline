---
title: "I built 31 developer tools in a weekend — here's what I learned"
slug: "i-built-31-developer-tools-in-a-weekend-heres-what-i-learned"
author: "chenghui wu"
source: "devto_webdev"
published: "Sun, 19 Jul 2026 08:08:27 +0000"
description: "Every time I want to format a JSON blob, decode a JWT, or convert a Unix timestamp, I end up on a different random site — each covered in ads, popups, and "c..."
keywords: "json, tools, tool, string, every, data, all, formatter"
generated: "2026-07-19T08:26:32.157830"
---

# I built 31 developer tools in a weekend — here's what I learned

## Overview

Every time I want to format a JSON blob, decode a JWT, or convert a Unix timestamp, I end up on a different random site — each covered in ads, popups, and "click here to install our extension" banners. Half of them upload my data to their server for no reason. So this weekend I built DevKits — a single site with 31 developer tools that all run 100% in the browser . No uploads, no accounts, no tracking. What's in it Right now, 31 tools across 9 categories: JSON : formatter, validator, JSONPath tester Converters : JSON ↔ TypeScript / Go / YAML / CSV / XML Encoding : Base64, URL, HTML entities, image → data URL Security : JWT decoder, MD5/SHA-256/SHA-512, password generator Text : regex tester, diff, case converter, word counter, Lorem Ipsum Web : color converter, user-agent parser Time : Unix timestamp, cron expression parser AI : OpenAI/Claude/Gemini token counter Formatting : SQL, XML, Markdown → HTML Live at devkits.vip . Open source? Not yet, but the whole project is deployable to Vercel in ~2 minutes. Why not just use it-tools.tech or smallpdf or …? Fair question. Existing sites have some (or all) of these problems: Bloat. Loading 500KB of JS to format 200 characters of JSON. Ads. Layout shifts on every visit. Privacy. Some upload your input to a backend to "process" it — a red flag when your input is a JWT or an API response. Cluttered UX. "Please sign in to save your favorite tools." No thanks. DevKits does the opposite: Every First Load JS is under 130KB. Most pages are 105–115KB. Zero ads, zero cookies, zero cross-site tracking. Everything runs client-side. Even the MD5 implementation, the tokenizer, the cron parser — all pure functions in your browser. Every tool page is a single URL you can bookmark. Tech stack Next.js 15 with the App Router TypeScript (strict mode) Tailwind CSS (with @tailwindcss/typography for the Markdown preview) Vercel for hosting I picked Next.js specifically because: SSG is a first-class citizen. All 41 pages are pre-rendered at build time. No cold starts. The metadata API is a joy. Per-page title , description , canonical , OpenGraph, and JSON-LD structured data — all just typed objects. File-based routing scales beautifully. Adding a new tool is: (1) one entry in tools.ts , (2) one page.tsx , (3) one client component. The sitemap, homepage listing, and "related tools" links update automatically. The tool registry pattern (my favorite part) The whole site is driven by a single tools.ts config file: export interface Tool { slug : string ; title : string ; shortName : string ; description : string ; category : ToolCategory ; keywords : string []; faq : { question : string ; answer : string }[]; } export const tools : Tool [] = [ { slug : " json-formatter " , title : " JSON Formatter & Validator " , shortName : " JSON Formatter " , description : " Format, beautify, and validate JSON online. Free, fast, and 100% local... " , category : " json " , keywords : [ " json formatter " , " json beautifier " , " json validator " ], faq : [ { question : " Is my data uploaded? " , answer : " No... " }, // ... ], }, // 30 more tools... ]; From this single array, four things are auto-generated: sitemap.xml — every tool becomes a URL entry Homepage listing — grouped by category Per-page metadata — title / description / canonical / OG / Twitter card JSON-LD structured data — SoftwareApplication + FAQPage schema for rich Google search results The "related tools" section on each page is also just tools.filter(t => t.slug !== current.slug).slice(0, 6) . So internal linking is automatic. Adding a new tool takes about 20 minutes. The token counter surprised me The AI Token Counter (for GPT-4o / Claude / Gemini) was the trickiest. Real tokenization requires shipping ~1MB of tokenizer vocabulary. Way too heavy for a "

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chenghui_wu_1613965a032b1/i-built-31-developer-tools-in-a-weekend-heres-what-i-learned-1f3h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
