---
title: "Internet access rose across six countries, at different speeds"
slug: "internet-access-rose-across-six-countries-at-different-speeds"
author: "Ben Portman"
source: "devto_python"
published: "Thu, 24 Sep 2026 16:33:44 +0000"
description: "A ranking is a snapshot. A time series shows how quickly access broadened. I pulled the World Bank’s internet-use indicator for six countries from 2000 throu..."
keywords: "series, internet, not, row, six, countries, world, country"
generated: "2026-09-24T16:53:21.335893"
---

# Internet access rose across six countries, at different speeds

## Overview

A ranking is a snapshot. A time series shows how quickly access broadened. I pulled the World Bank’s internet-use indicator for six countries from 2000 through 2024 and plotted the share of each population using the internet. The six-country selection is illustrative, not a representative sample of the world. What stands out By 2024, internet use was reported at 94.7% in the United States, 94.4% in Canada, 93.5% in Germany, 92.0% in China, 84.5% in Brazil, and 64.9% in India. All six series rose, but they did not follow the same path. India started from a much lower baseline and its steepest gains came later. Brazil’s adoption also accelerated over time. The three highest lines converged near the mid-90s by the end of this snapshot. That is a description of the series, not an explanation of why the changes happened. Internet-use rates alone do not tell us about connection quality, affordability, hours online, or differences between urban and rural areas. Open the interactive chart to compare the annual values. Reproduce the series The chart uses World Development Indicators series IT.NET.USER.ZS , “Individuals using the Internet (% of population).” The API query below returns the annual observations for the same countries and period: import requests url = ( " https://api.worldbank.org/v2/country/ " " BRA;CAN;CHN;DEU;IND;USA/indicator/IT.NET.USER.ZS " ) response = requests . get ( url , params = { " date " : " 2000:2024 " , " format " : " json " , " per_page " : 2000 }, timeout = 30 , ) response . raise_for_status () metadata , observations = response . json () rows = [ { " country " : row [ " country " ][ " value " ], " year " : int ( row [ " date " ]), " internet_use_pct " : row [ " value " ], } for row in observations if row [ " value " ] is not None ] print ( rows [: 3 ]) The World Bank’s indicator page explains the series. I also saved a dated, reproducible 150-row CSV snapshot with the source metadata ; it includes GDP per person for the same six countries and years. A note on timing This is a static extract downloaded on 24 September 2026, and the latest year available in it is 2024. World Bank values can be revised as source data are updated. They are annual published statistics, not a live count of people coming online. If you want to explore other countries, years, or indicators, GlobalDataTracker.com puts the source-linked country series in an interactive explorer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/globaldatatracker/internet-access-rose-across-six-countries-at-different-speeds-17i9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
