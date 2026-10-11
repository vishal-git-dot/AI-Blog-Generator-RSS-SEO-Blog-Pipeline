---
title: "Google Hotels API: hotel prices by date as JSON"
slug: "google-hotels-api-hotel-prices-by-date-as-json"
author: "Aniruddha Garje"
source: "devto_python"
published: "Sun, 11 Oct 2026 03:55:55 +0000"
description: "Google Hotels shows prices from many booking sites for any city and night. If you want those prices as data, for a price calendar, a daily tracker or a rate ..."
keywords: "hotels, run, prices, eur, you, check, google, hotel"
generated: "2026-10-11T05:08:30.393410"
---

# Google Hotels API: hotel prices by date as JSON

## Overview

Google Hotels shows prices from many booking sites for any city and night. If you want those prices as data, for a price calendar, a daily tracker or a rate check, here is what I learned collecting them, and the request I use. Prices move with the check-in date I priced the first 10 hotels Google listed in Barcelona for check-in 21 and 22 days ahead, on 1 and 2 November 2026, for 2 nights and 2 adults, in EUR (run WpExyDflthAbuKfDG). The median price per night was EUR 122.51 for 1 Nov and EUR 138.38 for 2 Nov. One hotel listed on both days went from EUR 190.66 to EUR 230.92 per night, 21.1% more, one check-in day later. The hotel list moves too The two lists of 10 hotels had only 4 hotels in common. Each date had its own list. So never compare "the first 10 hotels" across dates. Compare the same hotelId across dates. The list also changes between visits, and it can differ from what your browser shows. In my comparison test, two browser visits 12 minutes apart had 87% of their hotels in common. For the hotels a run did return, prices matched the browser within 10% in 99% of cases. You choose the currency Prices come back in the currency you ask for, not the one your location suggests. With currency set to AED, all 20 Dubai prices came back in AED (run Rja3KztI5aZO5DQ5o). For the same night, the median of the first 10 hotels was EUR 103.36 in Lisbon and EUR 113.92 in Porto (run hw8Ld0SQ8Xq9SVcay). The request I use I built an Apify Actor for this, so I get the prices with one HTTP request. You need an Apify account and your API token in the APIFY_TOKEN environment variable. import os import requests url = " https://api.apify.com/v2/acts/garje~google-hotels-scraper/run-sync-get-dataset-items " run_input = { " queries " : [ " hotels in Barcelona " ], " checkInFromDaysAhead " : 21 , " checkInToDaysAhead " : 27 , " nights " : 2 , " adults " : 2 , " currency " : " EUR " , " maxHotelsPerQuery " : 10 , " proxyConfiguration " : { " useApifyProxy " : True , " apifyProxyGroups " : [ " RESIDENTIAL " ]}, } resp = requests . post ( url , json = run_input , headers = { " Authorization " : f " Bearer { os . environ [ ' APIFY_TOKEN ' ] } " }, timeout = 300 , ) resp . raise_for_status () for row in resp . json (): print ( row [ " checkInDate " ], row [ " name " ], row [ " pricePerNight " ], row [ " currency " ]) Each row carries the check-in date, the hotel's name and ID, the price per night, the currency, and the stay length and occupancy it was priced for. I ran the same request with 2 dates and 2 hotels each, and it returned 4 priced rows in EUR (run igBdVfjBIZWsCAS8m). The price is $1.99 per 1,000 hotel prices, and you are charged only for rows saved. Make it a daily tracker checkInFromDaysAhead and checkInToDaysAhead count from the day of the run. Schedule the request daily and the check-in dates move forward by themselves, with no dates to update. If you would rather click than code, the same setup is saved as a public example you can run: Google Hotels prices by date for 10 hotels . Sources What Where it comes from Barcelona medians, the hotel that rose, 4 hotels in common run WpExyDflthAbuKfDG Dubai prices in AED run Rja3KztI5aZO5DQ5o Lisbon and Porto medians run hw8Ld0SQ8Xq9SVcay The request above, 4 rows run igBdVfjBIZWsCAS8m Prices within 10% of the browser in 99% of cases run HZKxhoaE3zdIU5HDE Two browser visits 12 minutes apart, 87% in common browser baseline, 8 Oct 2026 I built the Google Hotels scraper used above, and every week I check it against the live site. I drafted this article with AI help; every number comes from the runs in the table.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/garje/google-hotels-api-hotel-prices-by-date-as-json-123

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
