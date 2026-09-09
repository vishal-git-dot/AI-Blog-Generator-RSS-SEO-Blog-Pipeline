---
title: "The approval gate: a pattern for AI agents that write to production systems"
slug: "the-approval-gate-a-pattern-for-ai-agents-that-write-to-production-systems"
author: "Kunwar Harshit"
source: "devto_ai"
published: "Wed, 09 Sep 2026 20:34:38 +0000"
description: "Most AI agent demos end at the moment the agent decides something. The interesting engineering starts right after that, when the agent writes to a system oth..."
keywords: "you, not, write, action, diff, approval, agent, system"
generated: "2026-09-09T20:46:26.463079"
---

# The approval gate: a pattern for AI agents that write to production systems

## Overview

Most AI agent demos end at the moment the agent decides something. The interesting engineering starts right after that, when the agent writes to a system other people depend on. I build automation that writes to CRMs, ticketing systems and inboxes for revenue teams. Those are systems of record. A wrong write is not a bad answer you can regenerate. It is a support ticket, a corrupted forecast, or an email a customer has already read. Here is the pattern that survived contact with production. The failure mode The naive design gives the agent credentials and lets it call the API directly. This works most of the time. Most of the time is the problem. At 95 percent action accuracy, one in twenty writes is wrong, and those writes compound into a database humans use to make decisions. The cleanup cost per bad write is much higher than the time saved per good write, so the automation goes net negative while still looking successful in your metrics. The second order failure is worse. Once users find two or three wrong records they stop trusting the whole dataset and go back to their spreadsheets. Now you have added a system nobody trusts. The pattern: propose, diff, approve, execute, log Split the decision from the side effect. The agent never touches the target API. It emits a proposed action, and a separate executor applies it only after approval. { "action_id" : "act_01H8Z..." , "type" : "crm.opportunity.update" , "target" : { "system" : "salesforce" , "object" : "Opportunity" , "id" : "0061..." }, "diff" : { "StageName" : { "from" : "Discovery" , "to" : "Proposal" }, "CloseDate" : { "from" : "2026-10-31" , "to" : "2026-11-30" } }, "evidence" : { "source" : "call_2291" , "quote" : "let us aim to get paperwork out next month" }, "status" : "pending_approval" , "idempotency_key" : "call_2291:opp_0061:stage" } Four things make this work in practice. A diff, not a payload. Show the reviewer from and to . A human can approve or reject a diff in about two seconds. Nobody actually reviews a raw JSON payload, so if you show a payload you have built an approval step that everyone rubber stamps, which is the same as having no gate at all. Evidence attached to the claim. Every proposed change carries the quote or source that produced it. That is what makes review fast, and what makes the audit log useful six weeks later when someone asks why a field changed. Idempotency keys. Approval is asynchronous and humans double click. Derive the key from the source event plus the target field so a replay is a no-op instead of a duplicate ticket. Reversibility. Store the from values, not just the to . Every applied action gets an inverse. Undo turns a scary automation into one people will actually leave switched on, and it is nearly free to implement once you have captured the diff. Preflight validation, before a human ever sees it Do not spend human attention on actions that were going to fail anyway. Before an action enters the approval queue, validate it against the target system. Does the field exist, is the picklist value legal, does the record still exist, does this user have write permission on it. Most bad proposals are not judgment errors. They are schema errors, and schema errors are cheap to catch in code. What to log Log the whole envelope, not just the outcome. Proposal, evidence, reviewer, decision, timestamp, applied result, and the inverse. If you can answer "who approved this, based on what, and how do I undo it" from a single table, you can pass a security review and you can debug production. Do not log the raw customer content that produced the action beyond the specific evidence quote. You want interaction patterns and decisions, not a shadow copy of your customers' data. The tradeoff This is slower per action than full autonomy, and that is fine. Reviewing a diff is cheap. Recovering trust after a bad automated write is expensive, and often you do not get the chance. Autonomy is the part that demos well. The gate is the part that decides whether the system is still switched on in six months. I build this pattern for revenue teams at Mindlyft , where agents draft the post-call CRM updates, tickets and follow ups, and a human approves before anything ships.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hrshitkunwartech/the-approval-gate-a-pattern-for-ai-agents-that-write-to-production-systems-471f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
