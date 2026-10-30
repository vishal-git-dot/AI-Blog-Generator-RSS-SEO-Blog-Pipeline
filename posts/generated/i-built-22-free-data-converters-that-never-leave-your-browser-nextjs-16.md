---
title: "I built 22 free data converters that never leave your browser (Next.js 16)"
slug: "i-built-22-free-data-converters-that-never-leave-your-browser-nextjs-16"
author: "minh"
source: "devto_webdev"
published: "Fri, 30 Oct 2026 21:18:38 +0000"
description: "Every time I needed to turn an API response into a CSV, or paste a JSON blob out of ChatGPT into something usable, I ended up on a tool site that either want..."
keywords: "json, csv, your, data, paste, converters, needed, chatgpt"
generated: "2026-10-30T22:07:19.231001"
---

# I built 22 free data converters that never leave your browser (Next.js 16)

## Overview

Every time I needed to turn an API response into a CSV, or paste a JSON blob out of ChatGPT into something usable, I ended up on a tool site that either wanted me to upload my data, buried the tool under 15 ads, or choked on quoted fields. So I built JSONSheet — 22 converters that run 100% in your browser . No upload. No signup. No server-side processing at all. What it does JSON ↔ CSV with proper RFC 4180 parsing (quoted fields, embedded commas/newlines, escaped quotes) JSON ↔ YAML — clean block-style output, correct quoting of ambiguous values JSON → XML and JSON → JSONL (NDJSON) for pipelines and fine-tuning datasets JSON ↔ Markdown tables — for READMEs, Notion, GitHub issues CSV/JSON → SQL INSERTs (Postgres & MySQL, with CREATE TABLE + type inference) JSON → TypeScript interfaces — nested objects become named interfaces Flatten / unflatten JSON to dot-notation paths JSON escape/unescape , Base64 encode/decode (UTF-8 safe), TSV → JSON (paste straight from Excel/Sheets), CSV dedupe & transpose , CSV → HTML table , JSON ↔ URL query string The "AI-paste" feature The part I use daily: paste JSON straight out of ChatGPT/Claude — markdown fences, "Here's your data:" prose and all — and the tool strips the noise before converting. One step instead of four. I wrote a full guide about this workflow: Convert ChatGPT / Claude output to CSV the clean way . The privacy angle (and why it's also cheap) Everything is a pure TypeScript function running in your tab. There is no API to call, so: Your data never leaves your device — genuinely, not as a marketing line The whole site is a static export — nginx serves ~2MB of files, the VPS idles at 0% CPU No DB, no auth, no PII to protect — the security surface is tiny Stack Next.js 16.4.3 , static export ( output: 'export' ) — no Node runtime needed in production React 19 + TypeScript , zero UI libraries — the converters are plain functions 76 unit tests on the converter core ( npm test in the repo) Deployed on a small VPS behind Cloudflare with Let's Encrypt; deploys via a 30-line bash script (no CI/CD needed at this scale) Try it 👉 jsonsheet.com · Source: github.com/kami2k1/jsonsheet If you hit a file it chokes on, open an issue with a sample — the CSV parser is RFC 4180-tested but real-world data always finds new edge cases.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mnh_10c67ea5971f38774b74/i-built-22-free-data-converters-that-never-leave-your-browser-nextjs-16-424c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
