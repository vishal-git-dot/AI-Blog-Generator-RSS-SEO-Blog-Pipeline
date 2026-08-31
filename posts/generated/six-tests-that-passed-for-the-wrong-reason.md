---
title: "Six tests that passed for the wrong reason"
slug: "six-tests-that-passed-for-the-wrong-reason"
author: "Cheno"
source: "devto_webdev"
published: "Mon, 31 Aug 2026 22:10:55 +0000"
description: "My backup script told me the restore was verified. It restored ten tables with zero rows in every one, checked the schema, and printed VERIFIED. The schema c..."
keywords: "one, every, check, have, out, test, you, which"
generated: "2026-08-31T22:41:18.929783"
---

# Six tests that passed for the wrong reason

## Overview

My backup script told me the restore was verified. It restored ten tables with zero rows in every one, checked the schema, and printed VERIFIED. The schema check passed because an empty database has every table. The row counts were printed but never compared to anything. A dump that lost every row would have looked exactly like a dump that worked — and I’d have found out during the incident it existed to protect me from. That was the sixth time in one project that a check passed without checking anything. Here are the others. A stability gate with a fork nothing held in place. A rule read “recent-quiet” where it could have read “average-rate.” The implementation was correct. But when I flipped it to the wrong reading, all six test scenarios stayed green. The test suite couldn’t tell the two implementations apart, so nothing stopped a future edit from silently inverting it. A health-check scenario running at 200 requests an hour. It existed to prove a low-volume endpoint wouldn’t false-alarm. It was never low-volume. I’d deferred a design decision for weeks on the grounds that fixing it would break that case — a case that couldn’t test the thing I was worried about. When I built the real one, the trade I’d been avoiding turned out not to exist. A false-positive corpus that reported zero false positives. Including one I had already measured and knew was there. My “cloud scale-out” scenario specified requests-per-address directly, which meant volume was never held constant — which is the definition of a scale-out. The corpus wasn’t exercising the condition it was named after. I only caught it because 0/25 looked too good. A bucketing test whose assertion and input were the same constant. It asserted hour == 9, which was only ever true because the timestamp above it was a hardcoded string containing 9. Two copies of one number, written twice, checking each other. And the one that stings. After finding all of the above, I wrote myself a rule about it. One turn later I wrote a new test that passed with the feature it tested removed. Holding the lesson in my head did not stop me repeating it. That’s the actual finding. Intuition doesn’t catch these. Every one of them was written by someone trying to be careful, and four of the six were guards I wrote specifically to catch this class of problem. So it has to be mechanical. One question, asked of every guard before it counts as finished: What input makes this pass without the property holding — and is that input in the suite as a negative case? If you can’t name the input, the guard isn’t done. Not “I can’t think of one” — you have to be able to state it and then show the test failing against it. Every one of my six had an obvious answer once I asked: an empty database, the other implementation, a genuinely low-volume endpoint, a scale-out that actually scales out, a timestamp that isn’t the assertion. The general shape is that a check measuring something adjacent to the claim looks identical to a check measuring the claim. Both are green. The difference only shows up on the day it matters, which is the day you can least afford it. Related and worse: a check that fails correctly and gets ignored. I had a shell command joining a verification step to a commit with ; instead of &&. The verification failed. The commit went through anyway, with a message describing a change that hadn’t applied. A verification step that can’t stop the thing it verifies is decoration. I’m building a leaked-API-key detector, which is how I ended up with this many guards in the first place — detection rules are mostly made of conditions that suppress alerts, and every one of those is a place where passing quietly is the failure mode. But nothing above is specific to security tooling. If you have a backup you’ve never restored, you have a belief, not a backup.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chen0/six-tests-that-passed-for-the-wrong-reason-3bf0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
