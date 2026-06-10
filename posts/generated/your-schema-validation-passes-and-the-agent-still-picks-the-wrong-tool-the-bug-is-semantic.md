---
title: "Your schema validation passes and the agent still picks the wrong tool. The bug is semantic."
slug: "your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic"
author: "James O'Connor"
source: "devto_python"
published: "Wed, 10 Jun 2026 04:05:27 +0000"
description: "Pydantic and JSON-schema guarantee the shape of a tool call. They say nothing about whether it was the right call for the user's intent. TL;DR: We put strict..."
keywords: "tool, call, wrong, validation, schema, intent, not, agent"
generated: "2026-06-10T04:15:10.536196"
---

# Your schema validation passes and the agent still picks the wrong tool. The bug is semantic.

## Overview

Pydantic and JSON-schema guarantee the shape of a tool call. They say nothing about whether it was the right call for the user's intent. TL;DR: We put strict Pydantic validation on every tool call our agent makes, expecting tool-call failures to drop. They barely did. When I categorized 40 logged failures, 31 of them passed schema validation cleanly. They were well-formed calls to the wrong tool, or the right tool with arguments that were valid types but wrong values. Schema validation catches structural errors. Our actual problem was semantic, and the validator is blind to it. What schema validation actually guarantees Pydantic checks types, required fields, enums, ranges. A call like cancel_order(order_id="A123") is structurally perfect even when the user asked to cancel a subscription, not an order. The validator passes it. The user is still angry. Shape is not intent. The 40-failure breakdown Of 40 tool-call failures we logged over a few weeks: 9 were real schema violations the validator caught (working as intended). 18 were the wrong tool for the intent, all schema-valid. 13 were the right tool with a semantically wrong argument (valid type, wrong value). So 31 of 40 sailed through validation. The thing we added to fix tool-call failures addressed less than a quarter of them. A cheap semantic precheck that helped After structural validation passes, run a deterministic check that the call's preconditions match the resolved state. No model required. def precheck ( call , ctx ): # structural validation already passed; now check semantics vs resolved state if call . tool == " cancel_order " : o = ctx . orders . get ( call . args . order_id ) return o is not None and o . user_id == ctx . user_id and o . status in CANCELABLE # ... one branch per destructive tool return True This killed the 13 wrong-argument cases almost entirely: the id was valid as a string but did not resolve to a cancelable order owned by this user. The case this does not solve The wrong-tool-for-intent bucket (the 18) is harder. Detecting that the agent chose cancel_order when the user meant cancel_subscription is itself an intent-understanding problem, and using another model to judge it just inherits the same blind spot. We stopped trying to verify intent automatically for destructive tools and put a one-line confirmation step in front of them instead. Open question How do you test that an agent picked the right tool, not just a well-formed one, without leaning on an LLM judge that shares the failure mode? The precheck handles arguments. Tool selection itself I still gate behind a human-style confirmation, which feels like admitting defeat. FAQ Doesn't an LLM judge catch the wrong-tool case? Sometimes, but it misreads intent the same way the agent did, so we do not trust it on the destructive path. Which model? Genericize: the agent and any judge should be from different model families, but the precheck above is model-agnostic on purpose.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/james_oconnor_dev/your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic-2i41

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
