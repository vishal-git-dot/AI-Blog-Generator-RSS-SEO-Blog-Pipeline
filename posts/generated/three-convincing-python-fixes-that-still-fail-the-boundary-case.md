---
title: "Three convincing Python fixes that still fail the boundary case"
slug: "three-convincing-python-fixes-that-still-fail-the-boundary-case"
author: "Failure Map"
source: "devto_python"
published: "Thu, 01 Oct 2026 21:20:59 +0000"
description: "A fix can remove the first failure and still violate the contract. Here are three small examples where the attempted repair looks reasonable until you run th..."
keywords: "repair, contract, attempted, events, amount, not, returns, its"
generated: "2026-10-01T22:31:42.467423"
---

# Three convincing Python fixes that still fail the boundary case

## Overview

A fix can remove the first failure and still violate the contract. Here are three small examples where the attempted repair looks reasonable until you run the boundary checks. These examples come from Failure Map, a project I created. They are controlled Python models with explicit contracts, not reports of production incidents. The programs below use only the standard library. 1. Deduplicating values instead of events The contract is to count each event identity once, while preserving distinct events with equal amounts. events = [ { " id " : " a " , " amount " : 1 }, { " id " : " a " , " amount " : 1 }, { " id " : " b " , " amount " : 1 }, ] The original implementation adds every delivery and returns 3. The attempted repair deduplicates amounts: def solve ( events ): return sum ( set ( e [ " amount " ] for e in events )) It returns 1, although the two distinct event identities should contribute 2. A set is useful only if its equality relation matches the contract. Two events having the same amount does not make them the same event. The attempted repair passes the empty-stream check but fails both the replayed-delivery and distinct-equal-amount checks: 1 of 3 passed . Inspect FA-001 and download its source . 2. Moving an expiration boundary by a whole tick The contract says an entry is valid before its expiration instant and invalid at that instant. An inclusive comparison keeps it alive too long. This attempted repair overcorrects: def solve ( value , now , expires ): return value if now < expires - 1 else None At now=1 and expires=1 , it correctly returns None . But at now=0.5 , the entry has not expired; subtracting a whole unit rejects it anyway. This is a useful test-design pattern: check the exact boundary, a nearby valid value, and a value beyond it. A patch that happens to work on integer timestamps may be wrong under a contract that admits fractional values. The attempted repair passes 2 of 3 checks . Fixing the reported expiration instant did not preserve the valid interval. Inspect FA-006 and download its source . 3. Making pagination inclusive to recover ties Suppose a page is ordered by a primary key and a unique identifier: rows = [[ 1 , 1 ], [ 1 , 2 ], [ 2 , 3 ]] cursor = [ 1 , 1 ] Filtering only on r[0] > cursor[0] skips [1, 2] . Changing that operator seems like a quick way to recover tied records: def solve ( rows , cursor ): return [ r for r in rows if r [ 0 ] >= cursor [ 0 ]] Now the cursor row itself returns again. At the last record, the query also returns a record where the next page should be empty. The comparison must respect the complete ordering contract, including the unique tie-breaker. The attempted repair passes only the before-first-record check: 1 of 3 passed . Inspect FA-011 and download its source . Reproduce the failures Download an open case bundle, extract it, and run: python3 broken.py python3 attempt.py Both programs intentionally exit with status 1 when a recorded check fails. Their JSON output includes inputs where available, actual and expected observations, and pass/fail results. The three attempted repairs above were executed for this article and produced the pass counts reported here. Using these tasks for coding-model experiments Failure Map publishes 20,168 open debugging tasks across 254 categories . The compressed JSONL task export contains prompts, broken implementations, hard-negative repair attempts, and embedded checks. Open sources and observations are CC0. That structure is useful for repair-prompt experiments and reinforcement-learning workflows with execution feedback. It is not a collection of open reference solutions: those are omitted from the open export. No coding-model performance improvement is claimed here. When designing an evaluation, keep case families and every shared evaluation_group together. Related faults can share a solution; a random row split can make the result look more independent than it is. Keep grading fixtures outside generated code's control, and execute candidates in an isolated environment. The common lesson in these three cases is to preserve the contract while fixing the failure. Testing the nearby valid case is often what exposes the second bug.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/failuremap/three-convincing-python-fixes-that-still-fail-the-boundary-case-5gk7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
