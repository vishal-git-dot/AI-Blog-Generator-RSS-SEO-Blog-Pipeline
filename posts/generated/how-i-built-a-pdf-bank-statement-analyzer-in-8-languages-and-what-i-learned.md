---
title: "How I built a PDF bank statement analyzer in 8 languages (and what I learned)"
slug: "how-i-built-a-pdf-bank-statement-analyzer-in-8-languages-and-what-i-learned"
author: "FLOW by Vestelon"
source: "devto_python"
published: "Thu, 18 Jun 2026 20:16:07 +0000"
description: "I spent months building FLOW ( vestelonflow.com ) — a tool that analyzes bank statement PDFs and finds forgotten subscriptions, hidden fees, and recurring ch..."
keywords: "bank, pdf, people, specific, statement, what, building, most"
generated: "2026-06-18T20:32:55.628496"
---

# How I built a PDF bank statement analyzer in 8 languages (and what I learned)

## Overview

I spent months building FLOW ( vestelonflow.com ) — a tool that analyzes bank statement PDFs and finds forgotten subscriptions, hidden fees, and recurring charges. Here's what I learned building it in 8 languages. The Problem Most personal finance apps require you to connect your bank account. For many people (especially in Europe), that's a dealbreaker. GDPR concerns, privacy fears, and simply not trusting third-party apps with banking credentials. My insight: the data people need is already in their PDF bank statements. Every bank generates them. Most people never look past the total. The Tech Stack The core flow: User uploads PDF bank statement PDF text extraction (pdfplumber + fallback OCR) Transaction parsing — this is the hard part LLM categorization pipeline Subscription detection (recurring charges with same merchant) Report generation The trickiest part was transaction parsing. Every bank formats their PDF differently. German banks look nothing like Slovak banks. We ended up building bank-specific parsers for the most common formats and a fallback generic parser. The 8-Language Challenge Supporting Slovak, Czech, German, French, Spanish, Polish, Arabic, and Chinese wasn't just about translating the UI. The financial terminology varies significantly: "Permanent order" in English = "Trvalý príkaz" in Slovak = "Dauerauftrag" in German Subscription detection keywords differ by region Date/amount formats are locale-specific We ended up with language-specific merchant dictionaries for common subscription services in each market. What Actually Matters The biggest lesson: people don't want a budgeting dashboard. They want a specific, actionable number. "You're spending €137/month on forgotten subscriptions" converts. "Your spending breakdown by category" does not. The product is live at vestelonflow.com — first report is free, no card required, no bank connection needed. Happy to answer questions about the PDF parsing approach, the LLM pipeline, or the localization challenges.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vestelonflow/how-i-built-a-pdf-bank-statement-analyzer-in-8-languages-and-what-i-learned-3580

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
