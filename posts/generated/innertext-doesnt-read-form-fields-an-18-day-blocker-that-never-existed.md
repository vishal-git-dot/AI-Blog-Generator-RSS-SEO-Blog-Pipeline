---
title: "inner_text() Doesn't Read Form Fields: An 18-Day Blocker That Never Existed"
slug: "innertext-doesnt-read-form-fields-an-18-day-blocker-that-never-existed"
author: "Sungsoo Youn"
source: "devto_ai"
published: "Sat, 26 Sep 2026 04:10:06 +0000"
description: "A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. This one is sho..."
keywords: "read, agent, had, value, not, page, one, fields"
generated: "2026-09-26T04:26:44.941806"
---

# inner_text() Doesn't Read Form Fields: An 18-Day Blocker That Never Existed

## Overview

A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. This one is short, and I wish someone had told my agent earlier. The setup My agent manages a few storefronts through a headless browser (Playwright). One store had a settings page with three required fields: country, address, phone number. The agent read that page twice, eleven days apart, with the same line: text = page . inner_text ( " body " ) Both times the three values were not in the text. Both times it concluded that the fields were empty, and it put "fill in the three settings fields" at the top of my to-do list, as the most important human task for the whole project. It stayed there for 18 days. What was actually on the page When I finally asked the agent to do the task itself, it read each field's value this time, and all three were already filled in. They had been filled in the whole time. inner_text() returns the rendered text of elements. The value of an <input> or <textarea> is not text content, so it does not appear. An input with a value and an input without one produce the same result: nothing. The correct read is the element's value: page . locator ( " input[name=phone] " ). input_value () # or, for every field at once page . eval_on_selector_all ( " input, textarea " , " els => els.map(e => [e.name, e.value]) " ) The second mistake behind the first The store had also sent a notification about the account. The agent had marked it "cannot read — no access to that mailbox" and left it to me. It turned out the agent already had a logged-in browser profile for the same mail service (created weeks earlier for a different job). It could have read the message on day one. The real reason in that message had nothing to do with the settings fields. So there were two gaps stacked on each other: "I can't see a value" was recorded as "there is no value". "My usual route is blocked" was recorded as "I can't read it", without trying the other sessions it already had. What changed Form checks read value , never page text. An empty-field claim has to come from the element itself. Before handing a task to a human, try every session you already own. The rule is now: if one route is blocked, try two more before escalating. A human task needs a proof trail. When the task was finally closed, the agent saved, reloaded, and read the values back before marking it done. The cost of the original mistake was not the 18 days. It was that the most important item on my list was pointing at something that didn't need doing, while the thing that did need doing sat unread in a mailbox. Want the whole system? The book has 11 chapters plus 4 ready-to-use templates (CLAUDE.md starter, memory files, auditor checklist, measurement guide) and a hands-on section for every chapter. It's $19 as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code Not sure yet? The first three chapters are free, same PDF format: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample Questions about the setup are welcome in the comments — I'll answer with what actually happened, not theory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dbsoul/innertext-doesnt-read-form-fields-an-18-day-blocker-that-never-existed-2pac

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
