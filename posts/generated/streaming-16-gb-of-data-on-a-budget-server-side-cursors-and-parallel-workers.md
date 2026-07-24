---
title: "Streaming 16 GB of data on a budget: server-side cursors and parallel workers"
slug: "streaming-16-gb-of-data-on-a-budget-server-side-cursors-and-parallel-workers"
author: "Wonder-David Efe"
source: "devto_python"
published: "Fri, 24 Jul 2026 08:30:00 +0000"
description: "A data processing pipeline that processes 100,000 rows is not the same as one that processes 10 million. At a small scale, a single-threaded Python script do..."
keywords: "workers, worker, cur, rows, memory, each, row, pool"
generated: "2026-07-24T08:34:24.199944"
---

# Streaming 16 GB of data on a budget: server-side cursors and parallel workers

## Overview

A data processing pipeline that processes 100,000 rows is not the same as one that processes 10 million. At a small scale, a single-threaded Python script does the job. At tens of millions of rows, the first bottleneck you hit is time: the pipeline takes too long to finish. The obvious fix is to run the work in parallel across multiple workers, and that's where the second bottleneck shows up: memory. Sequential is too slow and naive parallelizing hits memory A typical pipeline reads from a database, transforms each row in Python, and writes the results back. The first pass is a straight loop against that database: open one connection, SELECT ... FROM records , iterate, transform each row, write it back. It works. However, at tens of millions of rows, the CPU is mostly idle and it takes days. Every iteration waits on the database or the network. Tens of millions of round-trips of "fetch a row, do a bit of Python, write back" saturate nothing except your patience. The obvious move is to parallelize. Split the work across N workers, done in roughly 1/N of the time. In Python, the database read can be written in two natural shapes: # Shape A: fetch everything in the main process, distribute to workers via Pool.map cur . execute ( " SELECT * FROM records " ) rows = cur . fetchall () with mp . Pool ( 8 ) as pool : pool . map ( transform , rows ) # Shape B: split by row_id range, each worker fetches its own slice def worker ( lo , hi ): conn = get_conn () cur = conn . cursor () cur . execute ( " SELECT * FROM records WHERE record_id BETWEEN %s AND %s " , ( lo , hi )) for row in cur . fetchall (): transform ( row ) Both shapes use the default psycopg2 cursor, and that's what makes both fail the same way. The default cursor pulls the entire result set into client memory the moment execute() returns; fetchall() just iterates over what's already been loaded. Shape A OOMs in the main process before any worker spins up. Shape B splits the OOM across N workers: each worker tries to hold its share of the data (still in the gigabytes for large tables), and N processes racing to eat the machine either OOM together or swap so hard that "faster than sequential" becomes slower than sequential. You've traded a time bottleneck for a memory bottleneck. Neither budget is available. Keep the results on the server while keeping reads parallel The problem isn't parallelism, it's how each worker reads. The fix is for the data to be streamed: the result set stays on the Postgres server, and only itersize rows are streamed to the client at a time, on demand, as it iterates. In psycopg2, you get this behavior by using a named cursor. One knock-on: a named cursor holds an open read transaction on its connection, which means you can't commit writes on the same connection while it's open. This requires each worker to use two connections in practice, one for the streaming read and one for the batched write. def worker ( lo , hi ): read_conn = get_conn () read_conn . set_session ( readonly = True ) cur = read_conn . cursor ( name = f " worker_ { lo } " ) # named = server-side cur . itersize = 10_000 cur . execute ( " SELECT * FROM records WHERE record_id BETWEEN %s AND %s " , ( lo , hi )) for row in cur : transform ( row ) # only itersize rows in memory Each worker holds only a few MB of client memory at a time (itersize rows times row width, plus Python overhead), regardless of how big its slice is. The server holds the query state and streams. N workers together hold tens of MB in memory, not the full 16 GB. Parallelism is preserved. The memory problem disappears. Distributing the chunks: SQL ID ranges The way you split work across workers matters. Each worker owning a non-overlapping range of the primary key is the simplest coordination-free option. No shared queue, no producer/consumer starvation, no locks. Divide the row_id space evenly: lo , hi = get_bounds () # SELECT MIN(record_id), MAX(record_id) chunk = ( hi - lo + 1 ) // workers jobs = [ ( lo + i * chunk , lo + ( i + 1 ) * chunk - 1 if i < workers - 1 else hi ) for i in range ( workers ) ] with mp . Pool ( processes = workers ) as pool : pool . map ( worker , jobs ) The primary key's uniqueness means the ranges never overlap, so workers can process their slices independently without any runtime coordination. The split is done once, at startup, and never revisited. Modulo hashing ( WHERE record_id % N = worker_id ) also works, but range splits are usually faster because they let the query use an index range scan instead of a full scan with a modulo filter. With streaming reads on the input side and range partitioning across workers, a 16 GB read-transform-write job fits comfortably on a modest machine. The write side has its own scaling story, covered in Part 3 of this series (CTAS-and-swap).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wondadav/streaming-16-gb-of-data-on-a-budget-server-side-cursors-and-parallel-workers-5een

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
