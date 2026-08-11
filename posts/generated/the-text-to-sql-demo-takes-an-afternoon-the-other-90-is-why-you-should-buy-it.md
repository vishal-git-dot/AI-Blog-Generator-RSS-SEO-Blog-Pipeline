---
title: "The text-to-SQL demo takes an afternoon. The other 90% is why you should buy it."
slug: "the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it"
author: "Omer Hochman"
source: "devto_webdev"
published: "Tue, 11 Aug 2026 01:46:04 +0000"
description: "Originally published at nlqdb.com/blog The demo really is an afternoon. Pull the table definitions out of information_schema , template them into a prompt wi..."
keywords: "you, sql, your, question, demo, buy, model, stack"
generated: "2026-08-11T02:05:22.148557"
---

# The text-to-SQL demo takes an afternoon. The other 90% is why you should buy it.

## Overview

Originally published at nlqdb.com/blog The demo really is an afternoon. Pull the table definitions out of information_schema , template them into a prompt with the user's question, call a model, run whatever SQL comes back, render the rows. Every stack has a tutorial for this now, and they all work — "let our users ask their data in English" goes from ticket to working prototype before the day ends. That's the 10%. The other 90% shows up after the first real user The prototype's job was to produce SQL. The feature's job is to run model-authored SQL against your production database, on your users' behalf, unattended. Those are different jobs, and the gap between them is a stack of infrastructure the tutorial never mentions: A validator that fails closed. The model will eventually emit a write — a DELETE inside a CTE, a DROP behind a comment, a join onto a table the asker should never see. You need a parser-level allow-list that rejects everything except the reads you meant to permit, and rejects anything it can't parse. A regex denylist is the bug report you haven't received yet. A plan cache keyed on question + schema version. The same question shouldn't cost a model call twice, so you cache compiled plans — but a cached plan is only valid until the schema moves, so the key has to carry a schema fingerprint and invalidation becomes your problem. Skip this and every dashboard load bills you fresh tokens at p95 model latency. An eval harness over a labelled set. Prompts get edited, models get swapped or silently updated, and NL→SQL accuracy moves when either happens. Without a scored question→gold-answer set you find the regression when a customer does. Building the harness is a project; keeping the labelled set honest as your schema evolves is a chore with no finish line. None of this is exotic — every piece is buildable. The catch is that every piece is maintainable : production infrastructure with your on-call rotation's name on it, in service of a feature that probably isn't your product. The honest build-vs-buy test The wrong question is "can I generate SQL from English?" Yes — in an afternoon, that's the point. The right question is "do I want to own that stack?" If natural-language querying is your product — you're building a BI tool, a data platform, an agent framework — own it; the validator and the eval harness are your moat. If it's a reporting tab, a search box over each user's own rows, an in-app assistant — a feature inside a product that's about something else — buy the pipeline and embed it, the way you'd buy auth or email instead of running an SMTP server. (That second case is the one nlqdb exists for: drop in one element or one POST /v1/ask , the English compiles against the live schema, the compiled SQL is shown before anyone trusts it, reads pass a fail-closed allow-list, and the validator/cache/eval stack is our maintenance burden instead of yours. Honest limits: it's a hosted pipeline you embed, not a library you vendor — and "many users over their own rows" still means a database or an isolation scope per tenant, because per-user row-level security inside one shared database isn't shipped.) The general lesson: a demo prices the first afternoon; a feature prices the years after it. When an AI capability collapses the demo cost to nearly zero — and text-to-SQL has — the build-vs-buy decision doesn't disappear. It just moves to the part of the stack the demo never showed you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/omer_hochman/the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it-4iko

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
