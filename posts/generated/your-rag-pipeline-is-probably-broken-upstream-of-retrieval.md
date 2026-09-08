---
title: "Your RAG Pipeline Is Probably Broken Upstream Of Retrieval"
slug: "your-rag-pipeline-is-probably-broken-upstream-of-retrieval"
author: "Paul Crinigan"
source: "devto_ai"
published: "Tue, 08 Sep 2026 16:17:50 +0000"
description: "Most teams debugging a retrieval system start in the same place. Chunk size, embedding model, top-k, the prompt. Those knobs are visible, they are easy to ch..."
keywords: "ingestion, source, document, retrieval, one, text, never, most"
generated: "2026-09-08T16:23:34.874708"
---

# Your RAG Pipeline Is Probably Broken Upstream Of Retrieval

## Overview

Most teams debugging a retrieval system start in the same place. Chunk size, embedding model, top-k, the prompt. Those knobs are visible, they are easy to change, and changing one produces a different answer, which feels like progress. Meanwhile the thing that actually set the ceiling on the whole system ran once, weeks ago, in a script nobody has opened since. That script is the ingestion layer. The Five Stages Before Chunking Ingestion is not one step. It is five, and each one fails on its own terms. Extraction pulls raw data from the source. Files off disk, HTML over HTTP, paginated API responses behind rate limits, rows out of a database with connection pooling and timeouts. Parsing turns that raw data into structured text. A PDF becomes text blocks with positional metadata. An HTML page becomes clean prose with the navigation and ads removed. Most of the format specific complexity lives here, and so do most of the quality problems. Cleaning normalizes what parsing produced. Encoding fixes, repeated headers and footers removed, whitespace collapsed, boilerplate stripped. Cleaning also covers deduplication, so the same FAQ arriving from a wiki, a help center and an email thread does not become three retrievable copies of one answer. Enrichment attaches metadata. Source identifier, title, timestamp and content type at a minimum. Without it you cannot filter retrieval by date or source, and you cannot attribute an answer to anything. Output writes the finished document somewhere consistent and self describing, carrying its text, its metadata and the provenance of which pipeline version produced it. Chunking, embedding and indexing all happen after this. Collapsing them into one script is what makes the failures hard to isolate later. The Failures That Never Raise An Error The dangerous ingestion bugs do not throw. They return something that looks like a document. A parser hits a multi column layout and interleaves the columns, so every sentence is grammatical and the meaning is scrambled. A table extraction merges two columns and the numbers now belong to the wrong rows. A scanned page produces an empty string, which gets stored as a valid document with a title and a timestamp. An encoding slip turns quotes and dashes into mojibake the embedding model has never seen. Cheap checks catch most of this at ingestion time: Content length thresholds flag documents too short to be real, or long enough to suggest two documents got concatenated Language detection is reliable past about 50 words, so it works as either a filter or a tag for filtered retrieval Schema validation requires a non empty title, a valid source, a timestamp and a content type on every document Alphabetic character ratio is blunt but effective, since ordinary prose runs 70 to 85 percent alphabetic and garbled extraction output falls well below that The reason to spend effort here is that language models are confident by default. They will write a polished, authoritative answer out of garbled input and never signal that the source was broken. The full guide to AI data ingestion walks through each of these checks with threshold recommendations. Keeping A Knowledge Base Current A pipeline that runs once is a slowly expiring asset. Product docs change every release, policies get revised quarterly, support articles are written daily. If ingestion never runs again, the knowledge base drifts from reality while the system keeps answering with total confidence. Incremental ingestion needs three capabilities: change detection, differential processing and cleanup. Change detection looks different per source. Filesystems give you modification timestamps. APIs usually support an updated_at filter. Databases offer CDC streams. Crawlers compare content hashes against stored values. The common pattern is a sync state record per source holding the last sync timestamp, the document IDs last seen and those hashes, so each run asks only for what moved. Cleanup is the part that gets skipped. When a document is deleted at the source, nothing tells the index. It stays retrievable, and it keeps answering questions with information that stopped being true. The Audit Worth Running First Before touching another retrieval parameter, pull ten documents at random out of the index and read them next to their sources. If the stored text does not match, no amount of chunk tuning will fix the answers, because the answers were never going to be better than the text they were built from. The ingestion layer is boring, it runs unattended, and it sets the ceiling for everything downstream.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulcrinigan/your-rag-pipeline-is-probably-broken-upstream-of-retrieval-32dh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
