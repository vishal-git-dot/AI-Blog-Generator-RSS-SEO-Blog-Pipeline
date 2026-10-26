---
title: "A publish gate for AI-assisted posts: check every claim before it goes out"
slug: "a-publish-gate-for-ai-assisted-posts-check-every-claim-before-it-goes-out"
author: "Todd Doane"
source: "devto_python"
published: "Mon, 26 Oct 2026 12:23:11 +0000"
description: "If an AI agent drafts what you publish, the risk is not bad grammar. It is a confident number nobody measured, a feature that does not exist, or a paragraph ..."
keywords: "not, gate, post, agent, file, publisher, every, your"
generated: "2026-10-26T12:37:04.184868"
---

# A publish gate for AI-assisted posts: check every claim before it goes out

## Overview

If an AI agent drafts what you publish, the risk is not bad grammar. It is a confident number nobody measured, a feature that does not exist, or a paragraph of stock phrases with your name on it. We let our store's daily agent post under a real person's name, so we built a gate it cannot skip. What goes wrong without one A language model writes what is plausible. Plausible is fine for a first draft and wrong for a public claim. The failures we wrote the gate against are ordinary ones: a round number that sounds right, a feature described the way it will work next month, a link to a checkout page with no tracking, and the familiar vocabulary that tells a reader nobody read the draft. Asking the agent to "be accurate" does not fix this. The agent that wrote the claim is the one judging it, in the same context, with the same blind spots. The check has to sit outside the writing step and it has to be able to say no. The gate, in three layers A facts file is the only source of truth Every claim and every number a post may use lives in facts.md , each with its evidence: a file path, a command and its output, or a URL. If it is not in the file, it is not claimable. The file also has a "not claimable" section: customer counts, benchmarks, anything nobody has measured. Writing that section down is what keeps later posts honest. Deterministic checks are the floor Numbers: every number in the body must appear in facts.md , or the line carries a source link. Years, times, versions and list numbering are exempt. Phrases: a built-in list of stock AI phrases plus your own "Banned phrases" list from voice.md . Structure: no emoji, at most one exclamation mark, no rhetorical-question openers, a cap on em-dash density. Links: every link must resolve, and checkout links must carry utm_source so you can see which post sent the buyer. These cost nothing to run and they never get tired. They catch the cheap mistakes before a model is involved. An LLM checks each claim, and fails closed The last check sends the draft and the facts file to a model and asks for a verdict per claim: SUPPORTED, UNSUPPORTED or CONTRADICTED. Anything other than SUPPORTED fails the post. If the model cannot be reached, the gate fails too. A check that passes when it cannot run is not a check. A PASS writes a small sidecar file with the SHA-256 of the post body. Every publisher script calls one function before it posts: side = require_verified ( path , body ) # refuses if the sidecar is missing, # the hash differs, or the LLM step was skipped Edit one word after the PASS and the publisher refuses until the gate runs again. That rule stops an agent from tweaking a post after it passed. It does not stop an agent with write access from changing the publisher itself; that part is still code review. What it caught, and what it did not The gate checks content. Today it showed us the edge of that. Our Show HN post passed the gate, the publisher submitted it and printed PUBLISHED, and the account's submissions page was empty. Hacker News had answered with a notice that it is temporarily restricting Show HNs from new accounts. The publisher had trusted the redirect after submitting and, when it could not find the item, reported a generic URL as success. That is a publisher bug, not a content problem, and we handled it the way we handle any failure: find the cause, fix it, add the test, then recover. The publisher now reports success only when the item appears under the account's own submissions, saves HN's response page otherwise, and reports the restriction as declined. We did not retitle the post to get around the rule; the draft is parked and the rule is logged. A gate tells you a post matches your facts file and your voice guide. It cannot tell you a community will take it, and your publishers need their own proof that the post actually exists. Try the pattern without buying anything Start with the cheapest part: a facts.md with evidence per line and a "not claimable" section, plus a rule in your CLAUDE.md or AGENTS.md that nothing is published unless every number in it is in that file. Then add the hash lock: write the body's hash on approval and refuse to publish if it changed. Those two steps are the core of the pattern. The free Agent Ops Kit Lite (MIT) has the CLAUDE.md structure this runs inside. Disclosure: I sell the finished version. Publish Gate v1 is verify_post.py with configurable facts and voice files, any model CLI through PUBLISH_GATE_LLM (default claude -p ), the require_verified helper, an example dev.to publisher, templates, a directive for your agent and 8 tests: $19, or $29 bundled with the Agent Ops Kit, at calyx-ai.net . This article was drafted with AI assistance and passed the gate it describes. Originally published at calyx-ai.net .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/skibuff/a-publish-gate-for-ai-assisted-posts-check-every-claim-before-it-goes-out-5b2a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
