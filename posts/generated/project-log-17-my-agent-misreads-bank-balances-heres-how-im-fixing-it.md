---
title: "Project Log #17: My Agent Misreads Bank Balances. Here's How I'm Fixing It."
slug: "project-log-17-my-agent-misreads-bank-balances-heres-how-im-fixing-it"
author: "Okeke Chukwudubem"
source: "devto_python"
published: "Sat, 18 Jul 2026 18:21:54 +0000"
description: "Day 17. OCR on banking apps is unreliable. I built a verification layer that double-checks every number. Day 16 was a milestone: multi-app workflows. The age..."
keywords: "agent, verification, ocr, task, balance, financial, read, double"
generated: "2026-07-18T19:11:40.225147"
---

# Project Log #17: My Agent Misreads Bank Balances. Here's How I'm Fixing It.

## Overview

Day 17. OCR on banking apps is unreliable. I built a verification layer that double-checks every number. Day 16 was a milestone: multi-app workflows. The agent copied my bank balance and sent it to Mom on WhatsApp. Three apps. One task. But behind that success was an uncomfortable truth: the agent misreads numbers about 20% of the time. For a message to Mom, that's a typo. For a financial transaction, that's a disaster. Today, I built the fix. The Problem Banking apps scored F on my accessibility audit. No UI labels. No content descriptions. The agent has to rely entirely on OCR to read anything on screen. And banking apps have terrible OCR conditions: Small, condensed fonts for account numbers and balances Low contrast (grey text on slightly darker grey backgrounds) Currency symbols (₦, $, £) that OCR often confuses with numbers Commas in large numbers that OCR sometimes reads as decimals The result? A balance of "₦15,000" sometimes gets read as "₦15.000" or "₦15,00" or "₦15000." One missing digit. One wrong decimal. And the entire task is compromised. The Fix: Numeric Verification Layer I built a verification step specifically for financial data. Before any number gets stored in task memory, it goes through three checks. Check 1: Format Validation The extracted text must match a valid currency format. It must contain a currency symbol (₦, $, £, €) followed by digits, optionally with commas and a decimal point. Anything that doesn't match this pattern is rejected immediately. Check 2: Double-Read Confirmation The agent reads the same number twice—two separate screenshots, two separate OCR passes. If both readings match exactly, the number is accepted. If they differ, the agent reads a third time. If two out of three match, that value wins. If all three differ, the task is aborted with an error message. Check 3: Range Validation The extracted number must fall within a reasonable range. A bank balance of "₦0" or "₦999,999,999,999" is probably an OCR error. The agent checks that the number is between ₦1 and ₦1,000,000,000. Anything outside that range triggers a re-read. Today's Progress Task Status Built numeric verification layer ✅ Done Tested on banking app balance (50 attempts) ✅ 94% accuracy (up from ~80%) Tested on "₦15,000" specifically (20 attempts) ✅ 100% accuracy with double-read Added verification to vision.py ✅ Done Updated agent.py to use verification for financial data ✅ Done The Results Before the verification layer: 20% error rate on financial data. After the verification layer: 6% error rate. Still not perfect, but dramatically better. For the specific task of reading a bank balance and sending it to Mom, the agent now succeeds 19 times out of 20. The one failure is usually a timeout (banking app loads slowly) rather than a misread. What Still Breaks The double-read confirmation adds about 4-6 seconds to any task involving financial data. For a 3-app workflow, that's an extra 10-15 seconds. Not a dealbreaker, but noticeable. The range validation is crude. A legitimate bank balance of "₦0" (empty account) would be rejected as an error. I need a way to distinguish between "zero" and "OCR failed completely." And the verification only works for numbers. Text extraction—names, addresses, transaction descriptions—still has no verification. The agent could send "Mom" the wrong transaction description and have no way of knowing. What's Next (Day 18) Add text verification for transaction descriptions Test with real financial data (multiple transactions, not just balance) Start building the demo video The Repo 👉 github.com/Dexter2344/phone-agent vision.py now includes verify_financial_data() with format validation, double-read confirmation, and range checking. agent.py calls it before storing any financial data in task memory. This is Day 17. The agent is learning to double-check its own work.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/okeke_chukwudubem_5f3bf49/project-log-17-my-agent-misreads-bank-balances-heres-how-im-fixing-it-4egj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
