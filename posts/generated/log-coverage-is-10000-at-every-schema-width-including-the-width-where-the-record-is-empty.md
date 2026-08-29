---
title: "Log Coverage Is 1.0000 at Every Schema Width, Including the Width Where the Record Is Empty"
slug: "log-coverage-is-10000-at-every-schema-width-including-the-width-where-the-record-is-empty"
author: "Devanshu Biswas"
source: "devto_python"
published: "Sat, 29 Aug 2026 20:26:19 +0000"
description: "Arc Ops Level 6 is audit trails: reconstruct why it did that from the logs alone. 24 runs, 156 steps, a 15-field schema swept at every width. Level page: htt..."
keywords: "width, fields, steps, log, every, exactly, review, schema"
generated: "2026-08-29T20:45:19.186041"
---

# Log Coverage Is 1.0000 at Every Schema Width, Including the Width Where the Record Is Empty

## Overview

Arc Ops Level 6 is audit trails: reconstruct why it did that from the logs alone. 24 runs, 156 steps, a 15-field schema swept at every width. Level page: https://dev48.infy.uk/arcops/level6-audit-trails.html · Repo: https://github.com/dev48v/arc-ops Every number the log reports about itself is perfect Record coverage is 1.0000 at every width — including width 0 , where the record is empty. The hash chain verifies. Records written, bytes written and fields declared all improve monotonically as the schema grows. And the log reconstructs only 84 of 156 decisions. reconstruction overall 53.85% on the 38 irreversible steps 36.84% on the robust steps 81.40% on the fragile steps 43.36% It is 1.46× worse exactly where a review opens it. Why, and it is not carelessness The steps a review opens are the irreversible ones, and those are disproportionately the fragile ones — 78.95% of irreversible steps are fragile against 72.44% overall. A fragile decision is precisely the one whose explanation needs the most fields, and the fields that explain it are the large, sensitive ones that get truncated or redacted first. So the pressure that shrinks a log — size, retention, privacy — removes exactly the records that would have answered the question, while leaving coverage at 1.0000. What the fields are worth Nothing reconstructs below width 12. The last three fields cost 5,264 bytes a run and buy 0 reconstructions. Six fields are worth exactly zero reconstructions : actor , outcome , run_id , step , target , ts — the six every logging standard insists on. The three sensitive fields carry 90 between them, which is why the privacy review and the incident review want opposite things. Ten questions a review actually asks Three are answered on no record at the reference settings. One of those cannot be answered by any schema at any width: what did it NOT see — because a log records what happened. Redaction mode reconstructions bytes none 101 72,852 hash 84 45,884 drop 84 40,620 Hashing and dropping cost exactly the same 17 reconstructions, and hashing still writes 5,264 more bytes. You pay for the hash and get none of the answer back. One pen, proved by parsing all ten modules with ast : 0 imports that could reach a clock, a logger, a socket or a file; exactly 1 call site appending to a Journal. 1,061 tests, standard library only, MIT. 53 verifier asserts, 17 page checks, 0 failures.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/log-coverage-is-10000-at-every-schema-width-including-the-width-where-the-record-is-empty-3e9k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
