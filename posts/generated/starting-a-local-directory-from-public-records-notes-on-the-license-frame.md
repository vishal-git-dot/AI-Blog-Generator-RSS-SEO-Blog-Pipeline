---
title: "Starting a Local Directory From Public Records: Notes on the License Frame"
slug: "starting-a-local-directory-from-public-records-notes-on-the-license-frame"
author: "Nearbia"
source: "devto_webdev"
published: "Wed, 28 Oct 2026 12:16:17 +0000"
description: "Most local business directories begin with whatever businesses submit about themselves. We are trying the opposite order for Nearbia : start with the records..."
keywords: "city, license, work, you, not, log, florida, state"
generated: "2026-10-28T12:28:53.743725"
---

# Starting a Local Directory From Public Records: Notes on the License Frame

## Overview

Most local business directories begin with whatever businesses submit about themselves. We are trying the opposite order for Nearbia : start with the records that say who is allowed to do the work, then find websites, then check each site. The directory is not live yet. What is live is a set of plain guides and a work log, and this post walks through the data side of that work. Why start with licenses In Florida, contracting without a state license is a crime, and the state's Department of Business and Professional Regulation (DBPR) is the body that issues trade licenses. For a directory of contractors, that makes the license file a natural "frame": the set of entities that should be in scope before you look at anything else. The license data itself is surprisingly structured. A Florida contractor license number starts with a few letters, and those letters encode two things: The trade. CFC is a certified plumbing contractor, CAC is air conditioning, CGC is general, EC is electrical. Two easy ones to misread: CCC is roofing and CPC is pool/spa. The scope. Codes starting with C are certified (passed a board-approved exam, valid in any Florida jurisdiction). Codes starting with R are registered (met local competency rules, valid only where those rules were met). If you are modelling this, the prefix is effectively a compound key: trade + scope . Treat "certified vs registered" as a first-class field, because it changes where a business can legally work. The stages, as a pipeline The Nearbia work log lays the process out in stages. Paraphrased as a pipeline: National list of websites. Free open datasets of US places are downloaded whole. Each website gets one key so duplicates collapse. License frame. Florida's contractor license file lists everyone allowed to work. The log notes the state site blocks automated downloads, so a saved copy from a public web archive is used, and freshness is not guaranteed. That is an honest constraint worth designing around: version your snapshots and record their dates. City domain list. Sites with a plumbing category or name, inside or near city limits, are pulled from the national list. Other candidate sources. Building permits, the state business entity registry, and paid search listings for the city. Merge into companies. Records join on license number, then phone, then name and city, then final domain after redirects. Place addresses in city limits. A mailing city is not a city boundary. Website check in a real browser. The first slice is deliberately small: one trade (plumbers) in one city (St. Petersburg, Florida). Things that bite you Join order matters. License number is the strongest key when present. Phone numbers are shared, recycled and tracked. Names drift ("Inc." vs "LLC", DBAs). Domains redirect. Ordering joins from strongest to weakest key keeps bad matches from cascading. Mailing city ≠ city. The work log points out that some St. Petersburg ZIP codes reach into Seminole, Kenneth City and Pinellas Park. If your city page filters on the mailing city string, you will list businesses that are not in the city. Geocode and test against the actual boundary. Neighbouring cities overlap. The log reports that St. Petersburg and Clearwater shared about 80% of the same companies within a radius in their tests. Their decision: a city page lists only companies with an office inside that city. Whatever you choose, make the rule explicit, because "serves the area" and "is located here" are different claims. Not every record says what you think. A local business tax receipt is not a contractor license. Registering an LLC does not qualify anyone to contract. If you are merging state corporate filings with license data, keep them as separate attributes rather than collapsing them into one "verified" flag. Public records are a toolbox Beyond licenses, Florida law opens state, county and city records to inspection by anyone, with specific exceptions. For a contractor, that includes corporate filings and fictitious names (Sunbiz), building permits (county portals), code enforcement cases, court dockets and liens, OSHA inspections, and federal exclusions in SAM.gov. Each answers a different question, and each has blind spots. A permit portal, for example, cannot show work that was done without a permit. Where to read more The full write-ups, including the stage table with dates and the record-by-record reference, are in the work log published by Nearbia . If you work with licensing or permit data and have hit any of the same problems, I would be glad to hear how you handled them in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nearbia-notes/starting-a-local-directory-from-public-records-notes-on-the-license-frame-39ih

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
