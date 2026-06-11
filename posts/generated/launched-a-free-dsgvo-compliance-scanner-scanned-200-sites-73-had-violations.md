---
title: "Launched a free DSGVO compliance scanner — scanned 200+ sites, 73% had violations"
slug: "launched-a-free-dsgvo-compliance-scanner-scanned-200-sites-73-had-violations"
author: "Nevik Schmidt"
source: "devto_webdev"
published: "Thu, 11 Jun 2026 10:39:37 +0000"
description: "Originally written for r/SideProject on Reddit — sharing here for the dev.to community. TL;DR: Built a free tool that scans websites for GDPR/DSGVO complianc..."
keywords: "google, what, had, one, free, compliance, built, fonts"
generated: "2026-06-11T10:47:52.349129"
---

# Launched a free DSGVO compliance scanner — scanned 200+ sites, 73% had violations

## Overview

Originally written for r/SideProject on Reddit — sharing here for the dev.to community. TL;DR: Built a free tool that scans websites for GDPR/DSGVO compliance violations. Try it: nevik.de/guard/ — no signup, just paste a URL. The Origin Story A few months ago, a client forwarded me an Abmahnung (German legal warning letter) demanding €900 because their website loaded Google Fonts from Google's CDN. I'd built the site. I felt terrible. One Google Fonts request = one IP address sent to Google = one GDPR violation in Germany. I went down the rabbit hole. Started manually checking every client site. Then wrote a script. Then built a web tool. Then spent 3 weekends polishing it. Here's what I learned: Out of 200+ German websites I scanned, 73% had at least one compliance issue that could trigger a warning letter. What It Does The scanner checks for: External font loading (Google Fonts CDN — the #1 Abmahngrund in Germany) Third-party trackers (Google Analytics, Facebook Pixel, Hotjar, etc.) Cookie consent presence and configuration SSL/TLS status Legal pages (Impressum, Datenschutzerklärung) Server location (EU vs non-EU data processing) All checks run server-side. No browser extensions, no signup. Tech Stack Built with what I had lying around: Backend: Node.js + Express (running on my Hetzner VPS in Nuremberg) Scanning: Puppeteer headless browser + custom regex patterns Frontend: Vanilla JS + Tailwind (kept it simple) Database: PostgreSQL for scan results Infrastructure: Docker + Caddy reverse proxy Total cost: €0 (runs on my existing server) Some Interesting Findings The most common violation: Google Fonts loading externally (52% of sites) The most expensive mistake: A small e-commerce shop had Google Analytics + Facebook Pixel + Hotjar ALL loading without consent. That's potentially 3 separate Abmahnungen = €1,500-6,000 in legal fees. The surprise: Even some "DSGVO compliant" website builders (Jimdo, Wix) had issues with their default setups. Not their fault per se — users install third-party scripts without realizing the implications. What I'm Building Next Weekly monitoring emails — get notified when new violations appear PDF reports — for agencies to send to clients API access — integrate scans into CI/CD pipelines Multi-language — currently German-focused, expanding to English Try It nevik.de/guard/ — paste any URL, get results in 30 seconds. The basic scan is free and always will be. There's a paid tier for agencies who need ongoing monitoring and reports, but the one-time scan is completely free. If you're building websites for European clients, I'd strongly recommend scanning them. The average Abmahnung costs €500-2,000. Preventing it takes 30 seconds. Would love feedback on what checks to add next. What compliance issues have you run into?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nevik_schmidt_3635afa2b85/launched-a-free-dsgvo-compliance-scanner-scanned-200-sites-73-had-violations-kfk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
