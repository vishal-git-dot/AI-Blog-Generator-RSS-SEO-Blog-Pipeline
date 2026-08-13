---
title: "An AI agent read 13 invoices and blocked $1,411.25 in bad payments"
slug: "an-ai-agent-read-13-invoices-and-blocked-141125-in-bad-payments"
author: "Ships Itself"
source: "devto_python"
published: "Thu, 13 Aug 2026 07:02:01 +0000"
description: "I handed an AI agent 13 invoices and a list of what we had actually ordered. It approved 10 of them, $9,049.05, and refused 3. The 3 it refused were the exac..."
keywords: "you, model, not, invoice, one, code, read, wrong"
generated: "2026-08-13T07:41:34.963994"
---

# An AI agent read 13 invoices and blocked $1,411.25 in bad payments

## Overview

I handed an AI agent 13 invoices and a list of what we had actually ordered. It approved 10 of them, $9,049.05, and refused 3. The 3 it refused were the exact 3 I had rigged to be wrong: a padded total, an invoice nobody ordered, and a straight duplicate. Together they came to $1,411.25 in payments that should never have gone out. The satisfying part is not that it caught them. It is that the AI did almost none of the deciding. The setup 13 invoice images across 4 different layouts, including one deliberately awful scan (crooked, low contrast, the kind of thing a phone camera produces at a bad angle on a bad day). A vision model reads each image into strict JSON. Then plain code, no AI anywhere in it, checks that JSON against the purchase orders we placed. The stack: n8n for orchestration Gemini Flash via fal for the vision read, about $0.01 per image A code node holding three hard rules The 13 reads took 28 seconds end to end. At roughly a cent an image, the model cost here is a rounding error. The value is entirely in what happens after the read. The three rules that actually catch the fraud The gate checks every invoice against three conditions, and all three have to pass: The PO must exist. If there is no matching purchase order, nobody authorized this spend. The amount must match to the cent. Not "close," not "within a threshold." Exact. The invoice number must be one we have never seen. Seen it before means we are being asked to pay twice. Here are the three problems I planted, and which rule stopped each one: A padded total : a legitimate PO, but the invoice quietly added a $118.80 "priority support fee" on top. The amount no longer matched to the cent, so it flagged. An invoice with no PO at all , $980 for something nobody ordered. No matching PO, flagged. An exact duplicate of an invoice already approved, $312.45. The invoice number had been seen, flagged. Notice what none of these required. None of them needed intelligence, judgment, or a model. They needed a lookup and a comparison. That is the whole point. The honest failure I left in The awful scan bit me, and I kept it in the numbers because pretending otherwise would defeat the purpose of this channel. The invoice date printed as 02/08/2026 . The model read it as February 8. It was meant to be August 2. Classic US-versus-EU date order, and the model picked wrong with complete confidence. It did not flag any uncertainty. It handed me a clean, plausible, internally consistent February 8 and moved on. Nothing broke, because my gate does not use dates for anything. But that is luck, not design. If you build anything that touches due dates, payment terms, or late fees, the date field is the one you hand-verify, because a wrong date will sail through every arithmetic check you have. The broader lesson is the one worth carrying: a vision model will give you a wrong value with the same confidence it gives you a right one, and the wrong value will often be internally consistent. Confidence is not correctness, and there is no exception in the JSON telling you which fields to trust. The pattern: the model votes, the code decides Vision extraction is probabilistic. Every read is a best guess, and best guesses are wrong some fraction of the time in ways you cannot predict per-invoice. So the rule I follow is simple: Never let a probabilistic component make a deterministic decision about money. Keep the model's job narrow. Its only responsibility is turning pixels into structured data. Every decision with a consequence lives in code you can read, test, and reason about. The model votes. The code decides. When those two things blur together, you have built something that pays $118.80 it should not have, and you will not find out until you reconcile the statement. A few things that made this work in practice: Force strict JSON, not prose. A schema the model must fill gives you fields to validate. Free text gives you a paragraph to parse and hope over. Compare exact, not approximate, for anything financial. A tolerance of "a few dollars" is exactly the gap a padded fee hides in. Track invoice numbers you have already processed. Duplicate billing is one of the most common and least sophisticated ways money leaks, and a set lookup catches it for free. Treat every extracted field as a claim to check, not a fact to use. The date failure is proof that a value can be confident, consistent, and simply wrong. You do not need a smarter model to build this. You need a dumber, stricter layer sitting between the model and the bank. Takeaways A vision model plus a deterministic gate caught $1,411.25 in bad payments across 13 invoices in 28 seconds, at about a cent per read. The three checks that did the work were existence, exact-cent match, and duplicate detection. No AI in any of them. The model misread a date with full confidence and passed every math check anyway. Confidence is not correctness. Put deterministic code between the model and any money decision. The model votes, the code decides. The full n8n workflow, the code node, and the 13 test invoices (including the awful scan) are here: github.com/Ships-Itself/builds/tree/main/ep04-invoice-agent . If you want to watch this one get built and stress-tested end to end, the video lives on youtube.com/@shipsitself .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shipsitself/an-ai-agent-read-13-invoices-and-blocked-141125-in-bad-payments-3npi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
