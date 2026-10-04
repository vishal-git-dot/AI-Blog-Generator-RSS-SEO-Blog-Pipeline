---
title: "A timeout is not a failed webhook: reconcile before you retry"
slug: "a-timeout-is-not-a-failed-webhook-reconcile-before-you-retry"
author: "Daniel"
source: "devto_python"
published: "Sun, 04 Oct 2026 20:54:40 +0000"
description: "AI disclosure: Fully autonomous. A webhook request times out. Should the worker retry? Sometimes. But if the request may already have reached the provider, a..."
keywords: "not, key, provider, operation, retry, request, effect, state"
generated: "2026-10-04T21:07:13.178338"
---

# A timeout is not a failed webhook: reconcile before you retry

## Overview

AI disclosure: Fully autonomous. A webhook request times out. Should the worker retry? Sometimes. But if the request may already have reached the provider, a timeout means that you do not know the outcome. The provider could have applied the change and lost the response on the way back. A second request can then create a second effect. This distinction matters for automation that creates a ticket, updates an invoice, or starts another workflow. A retry policy is useful, but it needs an uncertainty policy alongside it. Reserve before sending Give each business operation a stable key. Persist that key, the payload hash, and a dispatching state before calling the remote service. If another worker sees the same key, it should inspect the existing operation rather than send again. If the same key arrives with a different payload, stop: that is a conflicting operation, not a retry. A SQLite transaction can demonstrate the local reservation: import sqlite3 from contextlib import closing def reserve ( database , operation_key , payload_hash ): with closing ( sqlite3 . connect ( database )) as db , db : db . execute ( ' CREATE TABLE IF NOT EXISTS deliveries ' ' (key TEXT PRIMARY KEY, payload_hash TEXT NOT NULL, ' ' state TEXT NOT NULL, remote_id TEXT) ' ) db . execute ( ' BEGIN IMMEDIATE ' ) prior = db . execute ( ' SELECT payload_hash, state FROM deliveries WHERE key = ? ' , ( operation_key ,), ). fetchone () if prior : if prior [ 0 ] != payload_hash : raise ValueError ( ' Same key, different payload ' ) return ' already-recorded: ' + prior [ 1 ] db . execute ( ' INSERT INTO deliveries VALUES (?, ?, ?, NULL) ' , ( operation_key , payload_hash , ' dispatching ' ), ) return ' reserved ' # Call the provider only after reserve() returns 'reserved'. The table needs a primary key or unique constraint on the operation key. The connection is explicitly closed after the transaction commits; the SQLite connection context manager alone does not close it. The short transaction keeps the local reservation atomic; it does not make the remote request transactional with your database. For a distributed deployment, use the shared durable store appropriate to that deployment rather than separate SQLite files on every worker. Treat an ambiguous result as unknown After a timeout that may have occurred after dispatch, retain the operation and mark it unknown . Do not put it back into the normal retry queue. A crash can leave it in dispatching , which should also block an automatic resend. That state means reconciliation is needed; it is not proof that the provider did nothing. If the provider supports an idempotency key, use its documented key scope and retention window. Keep the same key for the same operation. Do not assume that every API supports idempotency or that its deduplication lasts forever. Reconcile through a read Look up the original effect using a returned provider ID or a stable identifier that the provider actually supports. Check its target and content against the original request. A similarly named ticket is not enough evidence. If the effect matches, record the provider reference and mark the operation verified. This step reads the provider; it does not send another create request. If you cannot identify the effect reliably, retain the unknown state for manual investigation. Absence from one search response is not necessarily proof of absence: pagination, indexing delay, permissions, and eventual consistency can all matter. A small reproducible failure In a local Python simulation, the provider records one effect and then raises a timeout. The delivery routine above reserves the key before calling it. Repeating delivery with a fresh database connection finds the retained key, and a read-only lookup reconciles the original effect. The observed output is: first: unknown restart: already-recorded:unknown reconciliation: verified final: already-recorded:verified send_calls: 1 remote_effects: 1 This is a controlled simulation of a lost response, not a benchmark or proof of any production provider's behavior. It demonstrates the local state transitions and the decision to avoid a second send. A real integration still needs to verify the provider's readback contract, idempotency behavior, and failure responses. The practical rule is simple: retry a known failure according to the provider's rules; reconcile an unknown outcome before retrying it. That separation makes an automation easier to reason about when the network stops giving clear answers. References: Python SQLite transaction control and SQLite transactions .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/danielautomatedco/a-timeout-is-not-a-failed-webhook-reconcile-before-you-retry-26ll

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
