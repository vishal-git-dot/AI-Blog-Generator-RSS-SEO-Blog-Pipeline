---
title: "I built a leak scanner, then measured exactly where it fails. Here's both."
slug: "i-built-a-leak-scanner-then-measured-exactly-where-it-fails-heres-both"
author: "이령"
source: "devto_python"
published: "Mon, 06 Jul 2026 10:43:06 +0000"
description: "The scary 2026 stat isn't the 340% surge in prompt injection or the 88% of orgs reporting agent incidents (OWASP-linked, Beam AI). It's this: the leak is oft..."
keywords: "not, where, reasoning, answer, leak, then, measured, exactly"
generated: "2026-07-06T10:49:20.342506"
---

# I built a leak scanner, then measured exactly where it fails. Here's both.

## Overview

The scary 2026 stat isn't the 340% surge in prompt injection or the 88% of orgs reporting agent incidents (OWASP-linked, Beam AI). It's this: the leak is often not in the answer your logs capture — it's in the model's reasoning, which most people never scan. A 2026 benchmark found data escaping through reasoning/logs while the visible output stayed clean in most scenarios (AgentLeak). And the cost is not abstract. A stolen Gemini key burned $82,314 in 48 hours for a three-person startup this year — 457× their normal bill, with the provider's shared-responsibility model leaving them to pay it, and it kept happening to devs worldwide through mid-2026 (The Register, Cybernews). If personal data leaks, add the legal bill: GDPR fined Meta €251M for a token-exposure security failure, and the EU AI Act stacks up to 7% of global turnover on top (DPO Europe). Yet ~88% of orgs had an agent incident this year while ~82% thought they were covered (Beam AI). Confidence isn't coverage — and the people getting hit assumed "it's just a token." I measured a deterministic slice of this on four indie-common models. The matcher held steady across formats, languages, and multi-turn attacks — zero misses where a literal secret surfaced, zero false positives on known families. The reasoning channel leaked more than the answer. And hardening the answer didn't secure the reasoning. Then the honest part: outside its known families it catches nothing (I published the 0-of-10 test before expanding), it's literal-not-semantic, offline-not-runtime, and tested on small models. It's one layer, not a fix — prompt injection is still unsolved industry-wide. I publish exactly where it works and where it doesn't; raw stays private, aggregates public. [ https://github.com/ghkfuddl1327-wq/agentproof ] [ https://github.com/ghkfuddl1327-wq ]

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/leeryeong/i-built-a-leak-scanner-then-measured-exactly-where-it-fails-heres-both-4f2b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
