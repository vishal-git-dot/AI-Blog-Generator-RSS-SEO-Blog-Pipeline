---
title: "How we built an open dataset of 309 Utah marketing agencies"
slug: "how-we-built-an-open-dataset-of-309-utah-marketing-agencies"
author: "Brand Captain"
source: "devto_python"
published: "Tue, 24 Nov 2026 21:51:51 +0000"
description: "We run a directory of Utah marketing agencies . This week we exported the data behind it as an open dataset: 309 agencies in 50 Utah cities, with services, t..."
keywords: "agency, agencies, utah, text, what, city, marketing, listing"
generated: "2026-11-24T22:10:49.159988"
---

# How we built an open dataset of 309 Utah marketing agencies

## Overview

We run a directory of Utah marketing agencies . This week we exported the data behind it as an open dataset: 309 agencies in 50 Utah cities, with services, team size, founding year and published rates. It's CC BY 4.0, and the CSV is on GitHub and Zenodo . This post covers how the list was built, what we cut before releasing it, and two problems we hit while publishing it. Step 1: collect candidates from four sources No single listing site has every agency, so we pulled candidates from four places: Clutch's Utah agency lists and profile pages DesignRush's Utah lists BBB search results for marketing and advertising businesses in Utah a hand-built list of agencies we already knew about Each source spells names and URLs differently. "Acme Digital", "Acme Digital LLC" and "acmedigital.com" are often the same company. We keyed every record on the website's domain and merged on that, falling back to the name only when a listing had no website. That gave us 507 candidates. Step 2: throw out what isn't a real Utah agency A script fetched every candidate's homepage and contact page, then dropped: Dead and parked domains. A regex looks for registrar pages and server errors: "is for sale", HugeDomains, "Website Expired", database errors, bad SSL. Listing sites keep profiles up after an agency closes, and this caught them. No Utah evidence. If neither the site nor any listing put the agency at a Utah address, it went. Agency lists for a state often include out-of-state firms. Video-only shops. Agencies that only appeared on video production lists, with no other marketing listing, were cut. Last, we searched Google Maps for each remaining agency by name and city. That added missing hours and contact details, and it dropped agencies Google marks as permanently closed. 309 made it through. Step 3: tag services from the agency's own words Services come from matching the agency's homepage text against fixed keyword lists for 13 categories: SEO, local SEO, web design, Google Ads, Meta ads, social media, branding, content, ecommerce, email, video, PR and full service. This has a clear limit, and we say so in the data card. If an agency runs Facebook ads but never says it on the homepage, it gets a 0 for Meta ads. Matching the site's own text kept the tags tied to what each agency says it does, not to what a listing site guessed. Each category is also its own 0/1 column ( svc_seo , svc_meta_ads and so on), so you can filter without splitting strings. Step 4: decide what not to publish The directory pages show more than the dataset does. Before releasing the export we dropped: "About" paragraphs copied from agency sites, because that text belongs to the agencies star ratings and review counts from Clutch, Google and BBB, because those belong to the platforms phone numbers and street addresses What's left is facts: name, city, website, services, team size band, founding year, minimum project size, hourly rate band, BBB accreditation, and the source listings for each row. Every row also links back to the directory, to its city page where one exists. Step 5: publish it where data people look The same files went to Zenodo (which gives it a DOI), Kaggle, DoltHub, GitHub and a Datawrapper chart. Two of those needed workarounds. DoltHub's CSV import failed. Dolt infers column types from the first rows and picked a short VARCHAR for the sources column. Rows with long source lists then failed to insert. The fix was to skip CSV import and upload a SQL file with the table created up front: CREATE TABLE agencies ( name TEXT , city TEXT , state TEXT , website TEXT , services TEXT , sources TEXT -- plus the svc_* columns and the rest ) ; INSERT INTO agencies VALUES ( . . . ) ; DoltHub opens the import as a pull request, so you merge it into main afterward. Datawrapper's API rejected our session. Calls to api.datawrapper.de returned 401 even while logged in. The app itself talks to the same API through /api/v3 on app.datawrapper.de , and that path works with the browser session. What's in the data A few numbers from the 309 rows: 70 agencies are in Salt Lake City, 35 in Lehi and 26 in Provo. Those three cities hold 42% of the list. 219 mention SEO on their homepage. Only 60 mention Meta or Facebook ads. Of the 275 agencies with a team size, 237 have fewer than 50 people. Of the 153 with a published hourly rate, 109 start at $100 an hour or more. Use it Browse by city and service: Utah marketing agency directory CSV and JSON: github.com/fedtman/utah-marketing-agencies Cite it: 10.5281/zenodo.24512883 If you spot an agency that's missing, closed or in the wrong city, open an issue on the GitHub repo and we'll fix it in the next refresh.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/brandcaptain/how-we-built-an-open-dataset-of-309-utah-marketing-agencies-4pee

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
