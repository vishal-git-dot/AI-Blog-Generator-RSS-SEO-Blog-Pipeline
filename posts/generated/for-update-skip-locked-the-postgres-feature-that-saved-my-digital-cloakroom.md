---
title: "FOR UPDATE SKIP LOCKED: the Postgres feature that saved my digital cloakroom"
slug: "for-update-skip-locked-the-postgres-feature-that-saved-my-digital-cloakroom"
author: "Philippe"
source: "devto_webdev"
published: "Tue, 07 Jul 2026 14:34:24 +0000"
description: "Last year I watched a nightclub cloakroom melt down at 3am: two hundred people waving paper tickets, three staff members, and a lost-ticket dispute blocking ..."
keywords: "hanger, you, update, locked, skip, free, transaction, one"
generated: "2026-07-07T14:49:42.587397"
---

# FOR UPDATE SKIP LOCKED: the Postgres feature that saved my digital cloakroom

## Overview

Last year I watched a nightclub cloakroom melt down at 3am: two hundred people waving paper tickets, three staff members, and a lost-ticket dispute blocking the whole line. I ended up building StashMe , a digital cloakroom system for venues — and the scariest technical problem turned out to be one SQL clause away from boring. The problem: "give this guest the next free hanger" The core operation sounds trivial. But on a busy night you get bursts of simultaneous check-ins, and the naive version fails exactly when you need it most: -- DON'T: classic read-then-write race SELECT id FROM hanger WHERE venue_id = $ 1 AND status = 'FREE' LIMIT 1 ; -- two requests get the same hanger here UPDATE hanger SET status = 'OCCUPIED' WHERE id = $ 2 ; Two guests, one hanger, one very awkward conversation at pickup. The usual reflexes all have drawbacks: App-level mutex or queue — works on one server, breaks the moment you scale horizontally. SELECT ... FOR UPDATE — correct, but every concurrent check-in now waits in line for the same first row. Your throughput becomes serial exactly during the rush. Serializable isolation — correct too, but now you're writing retry loops for serialization failures. The fix: FOR UPDATE SKIP LOCKED Postgres has had the answer built in since 9.5, and it deserves more love: SELECT id FROM hanger WHERE venue_id = $ 1 AND status = 'FREE' ORDER BY number FOR UPDATE SKIP LOCKED LIMIT 1 ; SKIP LOCKED changes the locking behavior in one crucial way: instead of waiting on rows another transaction holds, the query simply skips them. So ten concurrent check-ins each lock a different free hanger, in parallel, with no queuing and no deadlocks. Each transaction claims its row, updates it, commits. It's the same primitive that makes Postgres-based job queues (like Graphile Worker or Solid Queue) viable: many workers, one table, no fighting. Using it from Prisma Prisma's query API doesn't expose SKIP LOCKED , but $queryRaw inside an interactive $transaction works fine: await db . $transaction ( async ( tx ) => { const [ hanger ] = await tx . $queryRaw ` SELECT id, number FROM hanger WHERE venue_id = ${ venueId } AND status = 'FREE' ORDER BY number FOR UPDATE SKIP LOCKED LIMIT 1` ; if ( ! hanger ) throw new NoFreeHangerError (); // claim it inside the same transaction }); Two details that matter: The lock only lives as long as the transaction. The SELECT and the UPDATE that claims the row must happen inside the same transaction, or you've just rebuilt the race with extra steps. An empty result doesn't mean "no free hangers." It can also mean "every free hanger is currently locked by someone else" — which, at a cloakroom, is precisely the moment the last coats are being taken. Decide explicitly whether that's a "full" or a "retry once" for your domain. When to reach for it If you're building anything that hands out finite resources under concurrent load — seats, time slots, inventory units, jobs, coat hangers — FOR UPDATE SKIP LOCKED is usually the answer before you reach for Redis, advisory locks, or a message queue. The database you already run solves the problem you were about to add infrastructure for. The cloakroom system is live at stashme.io if you're curious what it looks like in production. Happy to answer questions in the comments — I've since reused this exact pattern in two other projects and it hasn't blinked.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/philippesj/for-update-skip-locked-the-postgres-feature-that-saved-my-digital-cloakroom-3dm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
