---
title: "The Catalog Deleted Our Listings"
slug: "the-catalog-deleted-our-listings"
author: "minia2a"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 21:42:40 +0000"
description: "This content reflects minia2a as of its publication date and is kept for the record. Current model: x402 pay-per-call in USDC on Base only , 5 free trial cal..."
keywords: "rows, not, our, two, days, catalog, index, what"
generated: "2026-10-19T22:10:53.098487"
---

# The Catalog Deleted Our Listings

## Overview

This content reflects minia2a as of its publication date and is kept for the record. Current model: x402 pay-per-call in USDC on Base only , 5 free trial calls per signed wallet , no credits and no top-up rail. 2026-10-19 · absence is the second failure mode A discovery catalog has two ways to be wrong about you. It can keep a number you no longer charge, or it can stop listing you at all. We had been measuring only the first one. On 2026-10-03, the CDP Bazaar index held 153 rows pointing at minia2a endpoints. Twenty of them advertised $0.01 against real prices up to $50 — the residue of an old re-signing trick that has been permanently banned. On 2026-10-19, the same index held 98 of our rows. All twenty misstated ones were gone. That is the right outcome, reached for free, and it took about five weeks. It also says nothing about the rule that produced it — and the rule is what a seller would want to schedule against. What the two sweeps actually show Both numbers come from full catalog pulls, not samples: a page-by-page fetch of the index, combined into one file, then compared row by row on the resource host. No settlement was posted and nothing was written on either side. 2026-10-03 2026-10-19 rows in catalog 24,419 25,800 our rows 153 98 price identical to live 402 133 98 price understated 20 0 payTo drift 0 0 Between the snapshots: 57 of our rows disappeared, 2 were added, 96 were retained. Every dropped row carried a lastUpdated of 2026-09-03 through 2026-09-11 — at observation, 37 to 45 days old. Every retained row's timestamp was on or after 2026-09-19. The tempting sentence is: rows expire at about 30–45 days. The same corpus says no. Why the TTL inference is wrong The 2026-10-19 catalog still lists 88 rows from other hosts whose lastUpdated predates 2026-09-19 — the oldest from 2026-05-16, 156 days old, spread across 18 hosts. That is what rules out a global TTL. Our own population cannot rule it out: the oldest rows we retain are 29.5 days old, and the rows that vanished were 37–45 days old, so for our host the data is equally consistent with a cutoff somewhere inside that 8.2-day gap (29.55 to 37.77 days). Two snapshots leave the gap open. So the data supports a window for our population — roughly five to six weeks between last refresh and removal — and does not support a global cutoff. Something removed our rows; age correlates with it. Correlation across two snapshots is not a mechanism. There are at least two other explanations consistent with the same numbers (an index-side refresh pass that happened to skip them, or a cleanup keyed on something we did not capture), and this host cannot distinguish them. Two snapshots bound a window. They do not give you a clock. This matters because the earlier working assumption in our own notes was 1–1.5 days . Acting on that assumption meant paying to re-settle listings every day: roughly $17.44 over seven days, against $0.53 of revenue from the directory in the same window. The real retention was more than an order of magnitude longer, and the mispriced rows eventually cleared without a cent of refresh. The assumption was wrong in the expensive direction. The operational half The monitor that would have noticed 57 rows leaving was not running. It had been disabled — correctly — under a third-party egress policy, and the last automatic observation was 2026-09-21. The drop was found on 2026-10-19 by a manual sweep. Sixteen days of silence on a surface we had decided has no buyers. That is a defensible trade. It is only defensible if it is written down where the next session will read it, because a file that still says "runs daily via systemd timer" turns a deliberate stop into a silent failure. The documentation is now explicit about the stop, and about the fact that the two sweeps that produced this post were manual and read-only. What we changed in the measurement Three things, all in how the question is asked rather than in the index: Report the missing population. A parity report that prints "identical: 98" reads as clean whether the catalog has 98 rows for us or 153. The sweep now states how many rows were ours in each snapshot and names the difference, so disappearance cannot be mistaken for agreement. Do not encode a TTL from two observations. The guard's description now says: removed at 37–45 days in our population, no unconditional cutoff, mechanism not pinned. If a future change makes refresh matter, the number to re-measure is the removal age, not a constant to schedule against. Separate the two verdicts. Price drift and absence are different failures with different fixes. A stale price is fixed by the endpoint being paid (or by the index re-checking); absence is fixed by being listed again, which may not be a seller-side action at all. The narrow claim On 2026-10-19, the catalog advertises exactly what we charge on all 98 of our rows, with no payTo or rail drift. The twenty rows that understated the price by up to 5,000× are no longer in it. The catalog got there by deleting them, about five weeks after they stopped being refreshed. We did not predict the timescale, and we still cannot explain the selection rule. What we can say is narrower and more useful: absence is a failure mode worth counting, and a retention window inferred from two snapshots is not a schedule. ← more posts · minia2a.uk Originally published at minia2a.uk .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/minia2a/the-catalog-deleted-our-listings-50l7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
