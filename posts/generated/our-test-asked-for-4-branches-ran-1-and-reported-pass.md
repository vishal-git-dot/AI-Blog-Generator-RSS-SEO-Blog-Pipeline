---
title: "Our test asked for 4 branches, ran 1, and reported PASS"
slug: "our-test-asked-for-4-branches-ran-1-and-reported-pass"
author: "Devil Scrapes"
source: "devto_python"
published: "Thu, 17 Sep 2026 10:57:49 +0000"
description: "Quick answer: Our cloud test asked for 4 things — sale and rent, across Warszawa, Kraków and Wrocław — with maxResults: 40 . It came back 40 rows that were a..."
keywords: "branch, rows, price, test, rent, city, run, you"
generated: "2026-09-17T11:22:03.941546"
---

# Our test asked for 4 branches, ran 1, and reported PASS

## Overview

Quick answer: Our cloud test asked for 4 things — sale and rent, across Warszawa, Kraków and Wrocław — with maxResults: 40 . It came back 40 rows that were all sale, all Warszawa . Nothing failed. Search #1 ate the entire global budget before search #2 ever started, and three of the four code paths shipped to a test that reported PASS having never executed them. How does a passing test cover nothing? Because a global maxResults and a multi-branch input are two different ideas, and one of them silently wins. The loop is the obvious one. For each city, for each transaction type, fetch pages until the global cap is reached. Warszawa has more sale listings than 40, so it reached 40 alone. The rent branch, Kraków and Wrocław were all dead code for the duration of that run — and the run exited SUCCEEDED with a full dataset. That is the part worth internalising: there was no error to find. 40 rows requested, 40 rows delivered, zero exceptions, green dashboard. The only way to notice is to check the distribution of what came back against the branches you asked for: def assert_branch_coverage ( rows : list [ ResultRow ], searches : list [ Search ]) -> None : """ A row count proves throughput. Only coverage proves the branches ran. """ seen = {( r . city , r . transaction ) for r in rows } missing = {( s . city , s . transaction ) for s in searches } - seen if missing : logger . error ( " branch coverage gap: %s never produced a row " , sorted ( missing )) A green run tells you the code you executed works. It tells you nothing about the code you didn't. Why does this matter more in the cloud than locally? Because cloud QA runs the input-schema prefill , and the prefill is therefore the entire cloud test surface. Any branch the prefill doesn't reach ships to customers having literally never run on the platform — and platform-only bugs (proxy resolution, build mismatch, memory ceilings) are exactly the class local tests cannot see. So the prefill is not a friendly example value. It is a test plan, and a one-item prefill is a one-branch test. The fix here was a per-search budget rather than one global pot, so every branch gets its own floor and the deep run actually walks all four. Re-run: 142 rows, 68 sale, 74 rent, across all three cities. What's actually hard about Otodom itself? The price field, more than the anti-bot surface. Polish listings mix 1 250 000 zł , Zapytaj o cenę (ask for price), and rent figures with a separate + czynsz (admin fee) that is not part of the headline number. A naive numeric cast produces either a crash or, much worse, a plausible wrong integer. Rows therefore carry the raw advertised string and a parsed numeric, plus an explicit flag when there is no price at all, so "ask for price" never silently becomes 0 : { "listing_id" : "64827391" , "url" : "https://www.otodom.pl/pl/oferta/..." , "title" : "Przestronne 3 pokoje, Mokotów" , "transaction" : "rent" , "city" : "Warszawa" , "district" : "Mokotów" , "price_raw" : "3 400 zł" , "price_amount" : 3400 , "price_currency" : "PLN" , "price_on_request" : false , "area_m2" : 62.5 , "rooms" : 3 , "price_per_m2" : 54.4 } Is zero rows for a city a bug? Not necessarily, and conflating the two costs you real money in retries. A district filter with no matches this week is an honest zero. A branch that never ran is a coverage gap. A branch that ran and got blocked is an incident. Those want three different responses, and len(rows) == 0 cannot distinguish any of them — which is precisely how the bug above survived its first test. 😈 Otodom Poland Real Estate Scraper pulls sale and rent listings from Poland's largest property portal — listing ID, URL, title, district, city, advertised and parsed price, area, rooms and price per m² — across multiple cities and both transaction types in a single run, each branch budgeted and fault-isolated. We handle the blocks, the retries, the Polish number formats and the "ask for price" listings, so you get comparable numbers instead of strings. $1.80 per 1,000 listings. FAQ Can I scrape sale and rent in one run? Yes — both transaction types across a list of cities, and each combination gets its own result budget so no single popular city starves the rest. What happens to "Zapytaj o cenę" listings? They are returned with price_on_request: true and a null numeric price, never a zero. A zero would quietly corrupt any average you compute. Is the rent price inclusive of czynsz? price_amount is the advertised headline figure. The admin fee is advertised separately on Otodom and is not silently folded in. Do I need a proxy or a login? No login. These are public listing pages, and the Actor ships with a proxy configuration that works out of the box. How do I know all my cities actually ran? Every row carries its city and transaction , so branch coverage is checkable from the dataset itself — which, as above, is the check that matters.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/devil_scrapes/our-test-asked-for-4-branches-ran-1-and-reported-pass-980

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
