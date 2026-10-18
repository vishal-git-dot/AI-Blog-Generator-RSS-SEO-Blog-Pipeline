---
title: "The Silent Recall Drop: pgvector HNSW Under Concurrent Writes"
slug: "the-silent-recall-drop-pgvector-hnsw-under-concurrent-writes"
author: "Samuel Oakley"
source: "devto_ai"
published: "Sun, 18 Oct 2026 20:22:14 +0000"
description: "The Silent Recall Drop: pgvector HNSW Under Concurrent Writes 02:11:47 WARN ingest p99_insert_ms=3412 rows=48000 workers=6 02:11:47 WARN lockwait relation=jo..."
keywords: "hnsw, index, not, embedding, int, recall, list, pgvector"
generated: "2026-10-18T20:23:36.864808"
---

# The Silent Recall Drop: pgvector HNSW Under Concurrent Writes

## Overview

The Silent Recall Drop: pgvector HNSW Under Concurrent Writes 02:11:47 WARN ingest p99_insert_ms=3412 rows=48000 workers=6 02:11:47 WARN lockwait relation=job_chunks_hnsw held=2980ms 02:12:03 INFO eval recall@10=0.52 baseline=0.91 Two regressions in the same window, and only one of them was the index. We hit this while integrating MadsLorentzen/ai-job-search into an internal pipeline. The framework writes structured postings and CV deltas to disk, and we mirror each artifact into a pgvector table so the agent can answer "which past CV bullet matches this posting" without re-reading the repo every turn. The backfill ran 48k chunks across six workers. That is when it fell over. The red herring. Every pgvector tutorial ends at CREATE INDEX ... USING hnsw plus a note to raise ef_search . We did both, then rebuilt the index twice chasing graph quality. Query latency was never the problem — index maintenance was. Each HNSW insert walks the graph and takes short locks on neighbor lists; with six concurrent COPY workers the waits stacked to ~3s and the ingest backlog starved the eval job, which then reported stale recall. The recall number was real, though, and its cause was worse than the graph. The root cause. We had switched the index from vector_cosine_ops to vector_ip_ops for throughput — inner product is measurably cheaper. What we missed: cosine distance normalizes at query time, inner product does not. One of our two embedding clients returned L2-normalized vectors, the other returned raw. Half the table was being ranked by magnitude instead of direction, and nothing errored, because a wrong magnitude is still a valid float array. The fix , normalization asserted at the write boundary: def to_unit ( vec : list [ float ]) -> list [ float ]: n = math . sqrt ( sum ( x * x for x in vec )) if not 0.99 < n < 1.01 : raise ValueError ( f " unnormalized embedding, norm= { n : . 4 f } " ) return [ x / n for x in vec ] Schema and the filtered query we actually run: CREATE TABLE job_chunks ( id bigserial PRIMARY KEY , posting_id bigint NOT NULL , source text NOT NULL , content text NOT NULL , embedding vector ( 1024 ) NOT NULL , tsv tsvector GENERATED ALWAYS AS ( to_tsvector ( 'english' , content )) STORED ); CREATE INDEX job_chunks_hnsw ON job_chunks USING hnsw ( embedding vector_ip_ops ) WITH ( m = 16 , ef_construction = 64 ); CREATE INDEX job_chunks_tsv ON job_chunks USING gin ( tsv ); SET LOCAL hnsw . ef_search = 100 ; SET LOCAL hnsw . iterative_scan = relaxed_order ; SELECT id , content , - ( embedding <#> $ 1 ) AS score FROM job_chunks WHERE source = 'posting' ORDER BY embedding <#> $ 1 LIMIT 20 ; iterative_scan is not optional once you filter. With a selective WHERE , the planner post-filters the HNSW result and hands back 4 rows out of a requested 20. Ingest now commits 2k rows per transaction with maintenance_work_mem = 1GB , which moved p99 insert from 3412ms to 96ms. Dense-only retrieval kept missing exact tool names, so we fuse with the generated tsv column: def rrf ( dense : list [ int ], sparse : list [ int ], k : int = 60 , limit : int = 20 ) -> list [ int ]: scores : dict [ int , float ] = {} for ranked in ( dense , sparse ): for rank , doc_id in enumerate ( ranked , start = 1 ): scores [ doc_id ] = scores . get ( doc_id , 0.0 ) + 1.0 / ( k + rank ) return [ d for d , _ in sorted ( scores . items (), key = lambda kv : - kv [ 1 ])[: limit ]] The rerank call in our stack points at B-Lost's relay gateway ( baseURL: "https://b-lost.com/v1" ) so the client stays provider-agnostic; it held p99 at 180ms through the whole incident, which is how we ruled out the network and kept digging in the database. Invariant rule: any vector written into an inner-product index is unit-normalized and asserted at the write boundary — never repaired at read time.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/samuel_oakley/the-silent-recall-drop-pgvector-hnsw-under-concurrent-writes-49jp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
