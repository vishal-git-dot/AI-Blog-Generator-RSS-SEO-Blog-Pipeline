---
title: "5 things to agree before any AI pilot"
slug: "5-things-to-agree-before-any-ai-pilot"
author: "Slava Kotenev"
source: "devto_ai"
published: "Sun, 25 Oct 2026 10:41:06 +0000"
description: "Most AI pilots fail before they start. Not because the model is weak, but because nobody wrote down what "success" means. Three months later one person says ..."
keywords: "pilot, one, you, can, target, test, accuracy, before"
generated: "2026-10-25T11:03:34.783846"
---

# 5 things to agree before any AI pilot

## Overview

Most AI pilots fail before they start. Not because the model is weak, but because nobody wrote down what "success" means. Three months later one person says "it works pretty well", another says "it makes mistakes", and there is no number to settle the argument. Here are five things to agree on in one meeting, before any code is written. If you can't answer all five, the pilot isn't ready. 1. One process, one owner Pick a single process, not "customer experience". For example: incoming support requests, invoices from suppliers, or questions about internal documents. Then name one person who owns it and can say "yes, this result is acceptable". Without an owner, nobody can accept the pilot. Without a single process, nobody can measure it. 2. The baseline How long does the work take today? How often does it go wrong? Take a real sample, even 100 items, and measure by hand. This is the step teams skip most often. If you don't know that a person spends 6 minutes per invoice with a 3% error rate, you can't say whether the pilot improved anything. You can only say it "feels" faster. 3. A number that counts as success Write the target as a number before you see any results. Examples: "At least 70% of requests are handled without a human, with at least 97% accuracy on those." "Extraction errors on invoice totals below 1%." Two numbers usually work better than one: how much is automated, and how accurate that automated part is. They pull against each other, and the pilot is really about choosing the point between them. 4. What data the pilot may touch Which systems, which fields, which time period? Is personal data involved? Can a third-party model API see it, or does it have to stay inside your infrastructure? Settle this early. It is the most common reason a "successful" pilot dies in legal review a month later. 5. A date to decide: scale, fix or stop Put the decision date in the calendar and name the three outcomes in advance: scale it, fix specific problems and re-test, or stop. "Stop" has to be an allowed answer. A pilot that cannot be stopped is just a project with a smaller budget. What this looks like in practice I built a small demo to show the shape of an agreed target. It routes customer-support messages (Banking77, a public dataset, 77 intents). The acceptance target was fixed first: at least 97% accuracy on automatically handled tickets. The confidence threshold was then chosen on a validation split to meet that target, and the test set was used once for reporting. On the held-out test set: 75.9% of tickets were handled automatically at 97.7% accuracy, and the rest went to a human. If everything had been automated, accuracy would have been 90.2%. To be clear: this is a public benchmark and a demo on test data, not a client result. The point is the structure. The automation level was not guessed, it fell out of an accuracy target that was agreed first, and there is a human fallback for uncertain cases. Raise the target and you get fewer errors and less automation; that is the trade-off the owner in point 1 has to decide on. Code and the numbers are in the repo: https://github.com/TerrKot/WorkSearchHepler (folder demos/ticket-triage ). The one-meeting test Put the five questions on one slide and ask the stakeholders to answer them in the meeting. If the answers take a week of emails, you have found the real first task of the pilot, and it was cheap to find out. I write short notes like this about practical, measurable AI adoption in business, with demos on test data and no invented case studies: Telegram (EN): https://t.me/+F9aauS7IAPAxMTQy Portfolio mini app: https://t.me/Kotenev01_bot

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/slava_kotenev_159/5-things-to-agree-before-any-ai-pilot-4mem

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
