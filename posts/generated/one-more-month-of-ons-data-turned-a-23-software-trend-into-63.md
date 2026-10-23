---
title: "One more month of ONS data turned a +23% software trend into -6.3%"
slug: "one-more-month-of-ons-data-turned-a-23-software-trend-into-63"
author: "TheCareery"
source: "devto_python"
published: "Fri, 23 Oct 2026 21:02:25 +0000"
description: "Last month a post on this account worked through twelve months of UK online job advert volumes for thirteen graduate entry occupations, taken from the ONS da..."
keywords: "month, not, software, job, adverts, september, edition, ons"
generated: "2026-10-23T21:14:15.041122"
---

# One more month of ONS data turned a +23% software trend into -6.3%

## Overview

Last month a post on this account worked through twelve months of UK online job advert volumes for thirteen graduate entry occupations, taken from the ONS dataset "Labour demand volumes by Standard Occupation Classification (SOC 2020), UK". The headline figure was that adverts for programmers and software development professionals were up 23% across the window. The September 2026 edition was released on 23 October 2026. The same calculation, on the same thirteen occupations, from the same table, now reads -6.3%. Nothing was revised. The window moved by one month. What actually changed Programmers and software development professionals, UK total, new online job adverts: Window Start End Change Sep 2025 to Aug 2026 9,404 11,591 +23.3% Oct 2025 to Sep 2026 10,213 9,570 -6.3% August 2026 was a local high. September 2026 came in below the previous October. That is the whole story, and it is worth sitting with, because a twelve month endpoint to endpoint change is a two number statistic and both of those numbers are a single month of adverts. The earlier headline was not wrong about the data. It was over confident about what two months can carry. The fix is not a smarter metric. It is publishing the series and letting people see the shape. The full thirteen, October 2025 to September 2026 Occupation Oct 2025 Sep 2026 Change Sales accounts and business development managers 14,528 14,051 -3.3% IT business analysts, architects and systems designers 7,674 10,205 +33.0% Programmers and software development professionals 10,213 9,570 -6.3% Human resources and industrial relations officers 6,565 7,072 +7.7% Finance and investment analysts and advisers 6,158 5,213 -15.3% Advertising and marketing associate professionals 5,465 5,111 -6.5% Mechanical engineers 2,609 4,842 +85.6% Management consultants and business analysts 3,501 4,633 +32.3% Civil engineers 2,285 2,795 +22.3% Project support officers 1,621 1,691 +4.3% Data analysts 1,606 1,583 -1.4% Chartered and certified accountants 1,582 1,570 -0.8% Graphic and multimedia designers 1,224 1,266 +3.4% Mechanical engineers at +85.6% deserves the same caution as software did. October 2025 was 2,609 and September 2026 was 4,842, but the twelve months in between run from 1,383 to 4,842 and move around a lot. Read the series, not the headline. Two series changes in this edition The July 2026 gap is filled. The August 2026 edition had no July figure for these occupations. The September edition does. Anything published off the August edition that described a July gap is now out of date. March 2026 is suppressed for all thirteen. ONS marks it [x] . A suppression marker is not a zero and should not be treated as one, and it should not be interpolated. Carry it through verbatim or leave the month out. The extraction script Last month this script lived on one machine, which is the opposite of the point of publishing a series. It is now downloadable at thecareery.com/ons-extract.py , and it is boring on purpose: it selects thirteen SOC codes from Table 3, filters to the rows where the region is Total UK , and reshapes wide month columns into long format. It does not adjust, smooth, interpolate or recompute a single figure, and it carries [x] through unchanged. SOC_CODES = [ 2121 , 2122 , 2133 , 2134 , 2142 , 2421 , 2422 , 2431 , 3543 , 3544 , 3554 , 3556 , 3571 ] SHEET = " Table 3 " HEADER_ROW = 5 UK_LABEL = " Total UK " TREND_MONTHS = 12 It has a --verify-against flag that diffs freshly generated CSVs against a published copy and exits non zero on any difference. That is what makes the monthly refresh checkable rather than trusted. The header check is the part that matters most: if str ( header [ 0 ]). strip () != " Region " : sys . exit ( " unexpected header, ONS may have changed the layout, stop and check " ) A silent column shift in a 50 MB workbook is how a pipeline starts publishing confident nonsense. Fail loudly instead. Source and the pages built from it Office for National Statistics, "Labour demand volumes by Standard Occupation Classification (SOC 2020), UK", January 2017 to September 2026 edition, released 23 October 2026, Table 3. Licensed under the Open Government Licence v3.0. The per occupation breakdowns, including the regional splits and the full twelve month series, are published here: UK job advert volumes by occupation Software developer job adverts Mechanical engineer job adverts Job adverts are not vacancies , the caveat page for anyone tempted to read advert counts as hiring

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/careery/one-more-month-of-ons-data-turned-a-23-software-trend-into-63-16k6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
