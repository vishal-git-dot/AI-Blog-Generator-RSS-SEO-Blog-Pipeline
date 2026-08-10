---
title: "Joining Two Federal Datasets That Disagree by Design"
slug: "joining-two-federal-datasets-that-disagree-by-design"
author: "member_5432fd74"
source: "devto_python"
published: "Mon, 10 Aug 2026 18:17:48 +0000"
description: "We built a public per-state report from two federal datasets. The interesting engineering problem was not the join. It was deciding which join to refuse. The..."
keywords: "state, not, join, two, addm, data, column, federal"
generated: "2026-08-10T19:03:47.543464"
---

# Joining Two Federal Datasets That Disagree by Design

## Overview

We built a public per-state report from two federal datasets. The interesting engineering problem was not the join. It was deciding which join to refuse. The inputs Three files: IDEA Section 618 child count, school year 2023-24. Administrative census of students served under each special education eligibility category, by state, ages 5 to 21. U.S. Census Bureau population estimates, 2023. Resident population by state and age band. CDC ADDM Network, surveillance year 2022. Clinical autism prevalence for children aged 8, across 16 monitored sites. The join that works The identification rate is a straightforward ratio: rate_per_1000 = ( idea_autism_count [ state ] / census_pop_5_to_21 [ state ]) * 1000 Both sides are state-keyed and both cover the same universe, so the join is on state and nothing else. Two data-quality rules mattered more than the arithmetic: Iowa and New Mexico report special education non-categorically. There is no autism-specific numerator. These rows must be flagged as not applicable and excluded from ranking. Coercing a missing count to zero would place both states at the bottom of a ranked list, which is a fabricated finding. The Census age band has to match the IDEA age band exactly. IDEA Part B counts ages 5 to 21. Using total child population or an under-18 band silently inflates or deflates every rate in the table. The join we refused The ADDM data looks like it belongs in the same table. It is federal, it is autism-specific, and it is state-labeled. It does not belong as a fourth column you can sort against the others. An ADDM site covers a defined community, frequently part of one metro or county, not an entire state. The sampling frame is a surveillance catchment, not a state census. Joining site prevalence to state identification rate produces a column where a "state" value is really a single county, next to a column where the state value is genuinely statewide. Sorting that column ranks metro areas against states. We kept ADDM in the output, in its own column, labeled as a site figure with an explicit footnote, and excluded it from the default sort. The national ADDM figure of 32.2 per 1,000 sits in the summary as context against the national IDEA figure of about 1 in 72, because a national-to-national comparison is defensible where a state-to-site comparison is not. The general rule Two datasets sharing a key are not thereby joinable. Before joining, confirm three things match: the population being counted, the geography the count covers, and the instrument that produced it. Federal open data is especially prone to this failure because the key is always a clean two-letter state code, which makes every join look correct. Output The finished report, table, map, and CSV are at Autism Rates by State . It is published by Special Needs Care Network, which operates a directory of special needs schools and therapy providers in the United States at specialneedsusa.com. Other data reports are at specialneedsusa.com/data . Figures verified August 2026.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/member_5432fd74/joining-two-federal-datasets-that-disagree-by-design-4d0p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
