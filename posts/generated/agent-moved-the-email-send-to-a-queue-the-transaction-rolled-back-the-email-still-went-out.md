---
title: "Agent moved the email send to a queue. The transaction rolled back. The email still went out."
slug: "agent-moved-the-email-send-to-a-queue-the-transaction-rolled-back-the-email-still-went-out"
author: "Jeff"
source: "devto_ai"
published: "Tue, 20 Oct 2026 16:27:18 +0000"
description: "The agent's PR looked clean. Checkout handler was taking 800ms. Three hundred of those milliseconds were the SMTP call. The agent moved sendConfirmationEmail..."
keywords: "order, agent, commit, email, handler, transaction, out, await"
generated: "2026-10-20T16:39:11.049751"
---

# Agent moved the email send to a queue. The transaction rolled back. The email still went out.

## Overview

The agent's PR looked clean. Checkout handler was taking 800ms. Three hundred of those milliseconds were the SMTP call. The agent moved sendConfirmationEmail(order) into a BullMQ job, enqueued it from the handler, and reported p95 down to 210ms. Tests passed. The diff was small. The PR description even called it "non-breaking." It was breaking in a way that took us four days to notice. What actually happened The handler did roughly this, after the refactor: export async function checkout ( req ) { const order = await db . insert ( orders ). values ( req . body ). returning ( ' * ' ); await emailQueue . add ( ' confirm ' , { orderId : order . id }); await db . commit (); return order ; } Look closely. The queue publish happens before the commit. In the happy path this is fine. Commit succeeds, email goes out, customer is happy. In the sad path — a foreign key violation on a late constraint, a deadlock on the inventory row, a serializable-isolation retry that aborts — the commit throws. The db.commit() line fails. The handler returns 500. The customer sees a failed checkout. But the email job was already on the queue. A worker picks it up thirty seconds later, renders the template with the order ID that no longer exists in the database, and sends: Your order #A-4821 is confirmed. We'll send another email when it ships. The order doesn't exist. The tracking link in that email 404s. Customer replies to support, support has no record, we look foolish. Four days of this happened before a customer forwarded us the email and asked why their order number didn't show up in the app. Why the agent got it wrong The agent was optimizing for the metric it was given: handler latency. It saw the SMTP call as the obvious thing to move. It did what a human under the same pressure would have done — it picked the cheapest refactor that made the number go down. What it did not do, because nothing in its prompt or its test suite asked it to, was reason about the ordering of side effects relative to the transaction. It had no model for "what should happen when the commit fails." The tests it wrote covered the happy path. The integration test that would have exercised a rolled-back transaction with an enqueued job was not in scope. This is the shape of a whole class of agent bugs: the agent is happy to move work out of the request path, but it has no intuition for the invariants that were accidentally preserved by doing that work inline. SMTP before commit was a (bad) guarantee that the email only went out on a successful transaction. Once the call moved, the guarantee had to be reconstructed explicitly. The fix We reverted to a transactional outbox pattern. On commit, the order row itself carries a pending_emails list; a separate reader process drains it and publishes to the queue. If the transaction rolls back, the row never lands, and there is nothing to send. export async function checkout ( req ) { const order = await db . insert ( orders ). values ({ ... req . body , pending_emails : [{ type : ' confirm ' , orderId : order . id }] }). returning ( ' * ' ); await db . commit (); // outbox reader, not this handler, enqueues the email return order ; } Same p95. No phantom confirmations. The cheap guard we ask for now When an agent PR moves a side effect out of a handler, we ask one question in review: Does anything in this diff still happen when the surrounding transaction rolls back? If the answer is "the side effect was enqueued, written to a cache, POSTed to a webhook, or pushed to an analytics sink before the commit," we stop and look. It doesn't mean the PR is wrong — sometimes you genuinely want the side effect to fire on failure. It means the ordering has become a load-bearing decision, and it should be visible in the diff, not an accident of where the agent happened to put the line. We ended up wrapping that check into the local API/contract review loop we run before merge. The point isn't that agents are dangerous — it's that the invariants humans used to hold by muscle memory now have to be written down and re-verified on every diff. The agent won't reconstruct them for you. If you're seeing agent PRs that "optimize" slow handlers by moving calls to queues, webhooks, or caches, that's the next thing I'd audit.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jeff_pdc/agent-moved-the-email-send-to-a-queue-the-transaction-rolled-back-the-email-still-went-out-4ih8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
