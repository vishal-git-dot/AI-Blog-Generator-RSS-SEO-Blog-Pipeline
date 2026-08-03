---
title: "The schema defined 2 foreign key pairs. The API reported 4."
slug: "the-schema-defined-2-foreign-key-pairs-the-api-reported-4"
author: "anp0429"
source: "devto_ai"
published: "Mon, 03 Aug 2026 19:38:26 +0000"
description: "I hit this in supabase/mcp a few weeks back, it's merged now ( PR #317 ), and the shape of the bug is worth writing down because it's exactly the kind of thi..."
keywords: "column, order, what, foreign, columns, them, one, fix"
generated: "2026-08-03T19:44:41.768261"
---

# The schema defined 2 foreign key pairs. The API reported 4.

## Overview

I hit this in supabase/mcp a few weeks back, it's merged now ( PR #317 ), and the shape of the bug is worth writing down because it's exactly the kind of thing AI agents consume without blinking. The setup: the MCP server has a list_tables tool. Verbose mode includes foreign key relationships, so an agent asking "how are these tables connected" reads that output as ground truth. For composite foreign keys it was wrong. The SQL joined source and target columns without pairing them positionally, so a 2-column FK came back as 4 pairings and a 3-column FK as 9. Cartesian product. N columns, N squared relationships, and all but N of them don't exist in the schema. Nothing errors. The output looks completely plausible. A human might squint at it. An agent just uses it, and now it's joining on a relationship that was never there. I filed it as a question, not a verdict, because I figured I might be missing context: is this intended behavior? The maintainer confirmed it was a bug and suggested going one better while we're in there: group each constraint's columns into ordered arrays, so the pairing is structural instead of implied by row adjacency. The part I actually want to talk about is proving the fix. The obvious fix is "order the columns." Ordered by what, though. Alphabetical order works on the happy path. Physical column order also works on the happy path. Both are wrong. The pairing has to follow the constraint's own declared column positions, so the fix uses unnest ... WITH ORDINALITY , and I added a test where the FK's declared order differs from both the alphabetical and the physical order. That test is the invariant. Without it, the bug can come back wearing a green suite. Once the grouped shape was pushed, I wanted to sanity-check it beyond my own tests before it merged. So I ran an automated review over the branch: an LLM proposes edge-case tests from the intent and the diff, then a deterministic gate executes every one against the real code. No model anywhere in the pass or fail. It proposed 9 cases past what I'd written. Two independent composite FKs between the same table pair staying separate. Self-referential composite FKs. Cross-schema FKs visible from either side. Single-column FKs correctly emitted as one-element arrays. Repeated calls returning identical output. All 9 executed green, 0 gaps found. I posted the list on the PR and offered to commit them. The maintainer's reply: commit them all, and this merges. So they went in, plus a couple more scenarios that came up in review, and the final suite landed 110/110. Two things I took from this. One, the dangerous bugs in agent-facing APIs aren't crashes. They're confidently wrong data. A crash gets caught by the first retry loop. N squared foreign keys gets built on. Two, "my tests pass" and "the behavior is pinned" are different claims. The nine executed cases didn't find a gap, and that's fine, that's what they were for: turning "I think the fix is right" into "here is what was executed against it and held." What got merged was the evidence, not my confidence. The gate I used is something I've been building in the open. It's called edgeverdict, it's on PyPI, and there's a no-key demo that runs in about half a minute. If you point it at your own repo, tell me where it lies to you. That's genuinely the most useful thing you can do for it. Tool links in the first comment.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/anp0429/the-schema-defined-2-foreign-key-pairs-the-api-reported-4-15c4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
