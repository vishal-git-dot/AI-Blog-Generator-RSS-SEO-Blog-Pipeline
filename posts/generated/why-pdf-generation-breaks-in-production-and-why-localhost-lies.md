---
title: "Why PDF generation breaks in production (and why localhost lies)"
slug: "why-pdf-generation-breaks-in-production-and-why-localhost-lies"
author: "Johin Johny"
source: "devto_webdev"
published: "Tue, 16 Jun 2026 20:44:03 +0000"
description: "PDF generation is one of those things that works perfectly… until real users touch it. On localhost: npm run dev Open Chrome → print → PDF. Done. Then produc..."
keywords: "pdf, your, html, browser, you, not, generation, pdfpipe"
generated: "2026-06-16T21:09:41.015514"
---

# Why PDF generation breaks in production (and why localhost lies)

## Overview

PDF generation is one of those things that works perfectly… until real users touch it. On localhost: npm run dev Open Chrome → print → PDF. Done. Then production arrives. A customer generates a 200-page report. Finance exports 5,000 invoices at midnight. A marketing team uploads a font your server has never seen. Suddenly your "simple PDF endpoint" becomes the most fragile part of your stack. The hidden problems nobody talks about Chromium is not a PDF library Most HTML-to-PDF systems are secretly browser automation systems. You are not calling: HTML → PDF You are calling: HTML → Browser → Renderer → PDF That means you inherit: browser crashes memory spikes process cleanup sandboxing problems version updates Your app does not need a browser. It needs a document. Concurrency changes everything A single PDF generation request? Easy. 100 requests at the same time? Now you need: queues workers retries timeouts monitoring The PDF code you wrote in 20 minutes becomes infrastructure you maintain forever. CSS is the real enemy The HTML looks perfect in Chrome. The PDF comes out broken. Common issues: tables split incorrectly headers disappear fonts fallback images fail loading page breaks happen randomly Because printing is not the same as rendering a webpage. Security is overlooked HTML rendering means executing a browser against user-controlled content. A malicious document can try: internal network requests metadata endpoints local file access A PDF service needs isolation. Not just a browser process. The approach I took with PDFPipe Instead of giving every developer another Puppeteer setup guide: The goal is: Your app | | HTML + data ↓ PDFPipe | ↓ PDF No Chromium servers. No worker management. No PDF infrastructure. The same reason we use Stripe instead of running payment infrastructure ourselves. The funny thing about PDF generation is: Nobody notices when it works. Everyone notices when it breaks. That is exactly why I started building PDFPipe. PDFPipe Curious: what is your current PDF stack? Puppeteer? Playwright? wkhtmltopdf? Something older?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/johin/why-pdf-generation-breaks-in-production-and-why-localhost-lies-195

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
