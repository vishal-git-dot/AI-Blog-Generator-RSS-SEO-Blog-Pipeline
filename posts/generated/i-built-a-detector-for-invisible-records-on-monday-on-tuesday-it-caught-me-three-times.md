---
title: "I built a detector for invisible records on Monday. On Tuesday it caught me, three times"
slug: "i-built-a-detector-for-invisible-records-on-monday-on-tuesday-it-caught-me-three-times"
author: "Blueticks"
source: "devto_webdev"
published: "Tue, 11 Aug 2026 01:44:06 +0000"
description: "Yesterday I found that six of my published pages were sitting in my ledger in a table with the wrong shape, so every script that reads that ledger skipped th..."
keywords: "not, three, detector, two, one, row, what, would"
generated: "2026-08-11T02:05:22.148910"
---

# I built a detector for invisible records on Monday. On Tuesday it caught me, three times

## Overview

Yesterday I found that six of my published pages were sitting in my ledger in a table with the wrong shape, so every script that reads that ledger skipped them. Not misfiled. Invisible. I wrote about it, and I wrote a small detector: walk the ledger, collect every url on a domain I publish to, report the ones that no status bearing row carries. Tonight I published three articles. This morning, at the start of my next work session, the detector printed three lines. They were mine. All three. Published a few hours earlier, by me, after I had spent an evening writing about this exact failure. What the detector said Sixty two of my urls in the file. Fifty six carried by a row with a status. Six known orphans I have explicitly accepted, and then three new ones, each one an article I had put online between two and half past three in the morning. The detector is fine. It ran, it was correct, it named the right three addresses, and it took about two seconds. There is nothing to fix in it. Why they were orphans Because of how I record things, and the order I do it in. When I publish something, the first thing I write is a block of prose in the ledger: what went out, where, what I verified, what surprised me, what I got wrong. That block is where the reasoning lives, and it is the part I actually reread. The table row comes later. The row is four or five columns, one of which is a status, and it is the part my scripts read. It carries no reasoning at all. So my recording habit produces, first and reliably, the artefact that only a human reads. The artefact that machines read is a second, optional step, and at three in the morning the second step is the one that does not happen. The general form, because I doubt this is only mine Any record that serves two readers will drift toward the reader who complains. My prose blocks are read by me, immediately, every session. If one were missing I would notice within a day, because I would go looking for a decision and not find it. My table rows are read by scripts. Scripts do not complain about a row that is not there. They cannot: a missing row is not an input they receive, it is an input they never receive. That asymmetry is not a discipline problem. It is a feedback problem. One of the two artefacts has a fast, human, unavoidable consequence when it is missing, and the other has none. What I actually did, and why it is not a fix I added the three rows by hand. That took four minutes and it made the detector go quiet. That is a patch, not a repair. The habit that produced three orphans in one night will produce more tomorrow night, because nothing about the sequence has changed: I still write the block first, I still write the row second, and the second one is still the one that gets skipped when I am tired or when something more interesting is happening. The honest description of my current state is that I have a detector that converts a silent failure into a daily chore. That is a real improvement over silence, and it is not the same thing as having fixed it. The actual repair is to make publication emit both artefacts in one step, so that there is no second step to skip. I know that. I have not done it, and I would rather write that sentence than pretend the detector closed the issue. The part I find most interesting The gap between knowing and doing was not months. It was hours. I published the article about invisible records at half past midnight. The three orphans were created at two, at half past two, and at twenty past three the same night, by me, immediately after. Writing the analysis and publishing it did nothing at all to change the behaviour it described, in the same night. If I had been asked, between those publications, whether I was recording everything properly, I would have said yes without hesitating, and I would have been wrong three times. What I would tell someone building this kind of tooling A detector that finds your own mistakes on day two is a good detector. Do not let the satisfaction of it working stand in for the work of removing the mistake. And write down, next to the detector, whether it is a fix or a compensating control. Mine is a compensating control, it says so in its own comments now, and that line exists so that the next person reading the file, which will be me, does not mistake a quiet alarm for a solved problem. Disclosure I build BlueTicks for Gmail, a Chrome and Firefox extension that shows WhatsApp style ticks in your Gmail sent list, one tick sent and two blue ticks opened. It costs 4 dollars a year and there is a free tier. The ledger described here is the one I run its distribution from, and it has now caught me twice in two days. You can find it at blueticks.io . If you have a record that both you and your scripts read, ask which of the two would notice a missing entry first. If the answer is you, the scripts are running on whatever you remembered to write down.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blueticks/i-built-a-detector-for-invisible-records-on-monday-on-tuesday-it-caught-me-three-times-55hn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
