---
title: "A boring data bug: one exam PDF, two file names"
slug: "a-boring-data-bug-one-exam-pdf-two-file-names"
author: "Prince"
source: "devto_python"
published: "Thu, 05 Nov 2026 05:49:06 +0000"
description: "Disclosure: I work on GTU Hero, a site that counts repeated questions in Gujarat Technological University exam papers. This post is about one boring data bug..."
keywords: "file, one, two, papers, physics, code, topic, count"
generated: "2026-11-05T06:01:18.140322"
---

# A boring data bug: one exam PDF, two file names

## Overview

Disclosure: I work on GTU Hero, a site that counts repeated questions in Gujarat Technological University exam papers. This post is about one boring data bug that came up while counting first-year Physics papers, and the small check I would add to any pipeline like this. The setup: download every official paper for a subject code, extract text, tag each sub-question with a topic, and count a topic once per paper. For the Physics guide that meant 22 papers across three subject codes, Summer 2022 to Summer 2026. The bug: the same file under two names The new-scheme Physics code BE01000021 has a sibling code, BE01R00021. For Winter 2025 and Summer 2026, the repository served a PDF under each code. They were the exact same file, headed "BE01000021/BE01R00021". If you count both, every topic in those papers gets counted twice, and a 2 out of 4 topic suddenly looks like 4 out of 6. So the fix is to dedupe on content, not on file name: import hashlib def sha256 ( path ): h = hashlib . sha256 () with open ( path , " rb " ) as f : for block in iter ( lambda : f . read ( 1 << 16 ), b "" ): h . update ( block ) return h . hexdigest () def unique_papers ( paths ): seen = {} for p in sorted ( paths ): seen . setdefault ( sha256 ( p ), []). append ( p ) return seen # hash -> every file name that served the same bytes Any hash with more than one file name is a duplicate. Keep one, and log the others so a human can see why the count dropped. A limit worth knowing Hashing only catches exact copies. A rescanned or re-exported PDF will have a different hash, so it is still worth glancing at the header text of each paper. Say it in the output In the published guide, the two duplicate files are counted once, and the guide says so. That matters because students make real decisions from these numbers. If a duplicate inflates a count and nobody notices, the advice is wrong while the table still looks clean. Two rules I follow now: Dedupe by content hash before counting anything. Write what you deduped into the output, not only into your logs. Neither is clever. Both are cheaper than explaining a wrong number later. If you are curious what the counts look like after this check, the Physics write-up is on GTU Hero .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/offpage_prince/a-boring-data-bug-one-exam-pdf-two-file-names-5dg8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
