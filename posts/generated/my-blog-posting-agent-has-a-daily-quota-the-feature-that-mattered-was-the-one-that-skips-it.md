---
title: "My Blog-Posting Agent Has a Daily Quota. The Feature That Mattered Was the One That Skips It"
slug: "my-blog-posting-agent-has-a-daily-quota-the-feature-that-mattered-was-the-one-that-skips-it"
author: "Enjoy Kumawat"
source: "devto_ai"
published: "Mon, 20 Jul 2026 03:36:57 +0000"
description: "I run a small pipeline that publishes technical articles to this blog on a schedule, twice a day, no human in the loop between "check trending topics" and "h..."
keywords: "run, not, topic, one, publish, pipeline, count, article"
generated: "2026-07-20T03:39:19.785982"
---

# My Blog-Posting Agent Has a Daily Quota. The Feature That Mattered Was the One That Skips It

## Overview

I run a small pipeline that publishes technical articles to this blog on a schedule, twice a day, no human in the loop between "check trending topics" and "hit publish." The obvious way to build that is: pick a target count, generate that many articles, post them. I built it that way first. It was a mistake, and not the mistake I expected. The mistake wasn't quality. The model writes fine prose when it has something to say. The mistake was that "hit the target count" and "have something worth saying" are two different success conditions, and if you only measure the first one, the pipeline will happily satisfy it by rephrasing yesterday's article with a different headline. The naive version Here's roughly what the first pass looked like, stripped down: def run (): published_today = count_published_today () remaining = TARGET - published_today for _ in range ( remaining ): topic = pick_highest_scoring_trending_topic () article = write_article ( topic ) publish ( article ) This runs, it produces output, and every metric you'd naively check — did it run, did it publish, is the count going up — looks green. The failure mode only shows up if you actually read the fifth article of the week and realize it's the third one about the same MCP security checklist with different word choices, because pick_highest_scoring_trending_topic doesn't know it already picked something adjacent to that topic four days ago. The fix isn't a smarter topic picker. It's giving the loop a legitimate way to produce fewer articles than the target, on purpose, as a first-class outcome instead of an error state. Making "not enough" a valid answer The version that's actually running now separates "can I hit quota" from "should I": def run (): published_today = count_published_today ( api_key ) # UTC day boundary if published_today >= DAILY_CAP : log ( " daily cap reached " ) return candidates = rank_trending_topics ( TAGS ) prior_titles = load_prior_titles () # ~30 published, from the work log fresh = [ c for c in candidates if not overlaps ( c , prior_titles )] if not fresh : # This branch used to not exist. It's the important one. log ( " no distinct angle found, publishing 0 this run " ) return n = min ( len ( fresh ), MAX_PER_RUN , DAILY_CAP - published_today ) if published_today == 0 and is_second_run_of_day (): n = max ( n , 2 ) # floor, not a target for topic in fresh [: n ]: publish ( write_article ( topic )) The overlap check ( overlaps ) does the unglamorous work: it diffs a candidate topic against the titles and short rationale of every article already published, pulled from a work log I keep in the repo. It's not fancy — mostly "does this reduce to the same root cause or the same fix as something already covered" — but it's the thing that turns "highest-scoring trending topic" into "highest-scoring trending topic I haven't already written." The floor ( max(n, 2) on the second run of an empty day) exists for the opposite failure: a pipeline that's too willing to publish nothing will quietly stop showing up, and nobody notices a blog that stopped updating until weeks later. So there are two guardrails pulling in opposite directions on purpose — a ceiling that stops it from forcing weak content, and a floor that stops it from going quiet by default. Neither one alone is the design; the tension between them is. The case that made this real A few days into running this, a scheduled run hit a wall I hadn't planned for: the sandbox this pipeline runs in had an egress policy that flat-out denied outbound connections to the publishing API. Every request failed at the proxy layer with a hard 403, not a timeout, not a retryable error — a policy denial. The naive version of this pipeline, the one without the "should I" branch, would have had a decision to make at that point: does a blocked quota check count as "0 published today," which then trips the floor logic on the next run and forces 2 articles out of a system that's already had a bad day? Or worse — does some retry-and-fallback path interpret "can't verify quota" as "assume 0 and proceed," and publish blind? What actually happened is the run logged blocked: dev.to unreachable from sandbox egress policy , consumed zero quota, and stopped. No retry loop, no fallback publish. The next run started clean, saw the real published-today count, and the floor logic applied correctly because the state it was reading was honest. That log entry is more useful sitting in the work log than a forced article would have been, because it's the reason today's count is what it is, six runs later, if anyone ever has to reconstruct why. The general shape The pattern generalizes past blog posts. Any scheduled agent that's supposed to do N things has the same latent bug: if the only measured outcome is "did N things happen," the agent will find the cheapest way to make N things happen, and cheap is rarely the same as correct. The fix is the same shape every time — carve out an explicit branch where the honest answer is "fewer than N, or zero, and here's why," and make sure that branch is reachable without looking like a crash. It's a small amount of code. It was also the only part of this pipeline that took more than one draft to get right, because every other part of the system was optimizing for "did it run," and this was the only part optimizing for "should it have."

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/enjoy_kumawat/my-blog-posting-agent-has-a-daily-quota-the-feature-that-mattered-was-the-one-that-skips-it-4fpe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
