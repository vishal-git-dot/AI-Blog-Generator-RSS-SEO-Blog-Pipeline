---
title: "How to detect N+1 queries in SQLAlchemy 2.0 — sync and async"
slug: "how-to-detect-n1-queries-in-sqlalchemy-20-sync-and-async"
author: "Rodrigo Nogueira"
source: "devto_python"
published: "Sun, 09 Aug 2026 06:08:01 +0000"
description: "Django hands you assertNumQueries , nplusone , and a debug toolbar. SQLAlchemy hands you an event API and a shrug — every answer to "how do I catch N+1 queri..."
keywords: "statement, sqlalchemy, load, async, lazy, not, none, one"
generated: "2026-08-09T07:03:35.996385"
---

# How to detect N+1 queries in SQLAlchemy 2.0 — sync and async

## Overview

Django hands you assertNumQueries , nplusone , and a debug toolbar. SQLAlchemy hands you an event API and a shrug — every answer to "how do I catch N+1 queries" ends with write your own before_cursor_execute listener . That advice is right, and the listener is about fifteen lines. Here it is, along with the three things that will quietly make it wrong. The event you want SQLAlchemy 2.0 added do_orm_execute , which fires for every ORM-level statement and carries an ORMExecuteState with enough context to identify a lazy load: from sqlalchemy import event from sqlalchemy.orm import Session @event.listens_for ( Session , " do_orm_execute " ) def on_orm_execute ( state ): if state . lazy_loaded_from is not None : print ( " lazy load: " , state . loader_strategy_path ) Register on the Session class , not an instance. AsyncSession wraps a sync Session internally, so class-level registration covers async for free and your users pass nothing. Trap 1: the obvious flag reports the fix as the bug The attribute that looks made for this job is is_relationship_load . It is the wrong one. Measured against SQLAlchemy 2.0.51: Scenario is_relationship_load lazy_loaded_from Queries lazy load (sync) True set 4 awaitable_attrs loop (async) True set 4 selectinload True None 2 subqueryload True None 2 joinedload — — 1 selectinload and subqueryload are the fixes for an N+1, and both report is_relationship_load=True . A detector keyed on that flag reports correctly-written code as broken. Key on lazy_loaded_from . It holds the InstanceState that triggered the load, and it is set only for a genuine lazy load — never for an eager loader doing its job. Trap 2: in async, the stack is empty A count with no source line is close to useless, so the natural next step is to walk the stack and report the first frame that isn't SQLAlchemy's. In sync code that works. In async it silently returns nothing. SQLAlchemy runs an async lazy load inside a greenlet it spawns. That greenlet's stack holds no application frames at all — only strategies.py , session.py and friends. The caller's frames are on the parent greenlet: import greenlet def caller_frames (): current = getattr ( greenlet . getcurrent (), " parent " , None ) while current is not None : yield getattr ( current , " gr_frame " , None ) current = getattr ( current , " parent " , None ) Walk the live stack first; if it yields nothing, walk from there. Without this, the single most common async N+1 — await obj.awaitable_attrs.items in a loop — reports with no source line, which is exactly the case you most wanted to diagnose. Trap 3: don't render the statement inside the listener str(state.statement) looks free. It is a full statement compile, measured at roughly 43µs per query. Calling it on every recorded statement made recording 2.7× slower — about half of all the overhead: 400 queries per run, best of 7 no recording 20.4 ms 50.9 µs/query recording, rendering eagerly 55.1 ms 137.7 µs/query recording, rendering deferred 27.9 ms 69.8 µs/query Keep the statement object and render it only for the handful of records you actually report. In Python that is one decorator: @dataclass ( frozen = True ) class QueryRecord : statement : Any = field ( repr = False ) @cached_property def sql ( self ) -> str : return " " . join ( str ( self . statement ). split ()) Two useful side effects. str(statement) compiles with the default dialect rather than your connection's, so the rendered SQL is identical on SQLite, PostgreSQL and MySQL — which makes it a stable key for grouping repeated statements across backends. And bind parameters stay as :param_1 placeholders, so you never capture parameter values . Counting statements is a separate problem do_orm_execute is not a statement counter. Flushes never reach it: an autoflush INSERT followed by a SELECT is one ORM execute and two statements. For a true count, use the Core-level events: from sqlalchemy import Engine @event.listens_for ( Engine , " before_cursor_execute " ) def count ( conn , cursor , statement , parameters , context , executemany ): ... @event.listens_for ( Engine , " after_cursor_execute " ) def timing ( conn , cursor , statement , parameters , context , executemany ): ... # duration lives here, not in the ORM layer Resist correlating the two layers. One ORM execute can produce several cursor executions — selectinload batches — and flushes appear in one layer and not the other. Report them as two separate, clearly-labelled numbers. Stitching them together is the fragility that broke the previous generation of these tools. What the ORM hooks can't see One shape deserves its own mention, because no relationship-load hook will ever fire for it: for user_id in user_ids : user = await session . get ( User , user_id ) # N round trips That is not a lazy load. It is a loop of ordinary queries, and it is just as expensive. Catching it needs a different signal entirely: normalise each statement to its template and count identical templates executed with different parameters inside one unit of work. Or don't write it yourself I packaged all of the above as queryspy — the three detectors, source attribution through the greenlet hop, and a pytest gate: pip install queryspy pytest --queryspy-strict N+1 detected: 11 queries for User.addresses (lazy load) triggered from app/services/users.py:28 in list_users() SELECT address.id AS address_id, address.email ... fix: .options(selectinload(User.addresses)) But the recipe above is the whole idea, and it is yours either way.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rodrigobnogueira/how-to-detect-n1-queries-in-sqlalchemy-20-sync-and-async-4lge

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
