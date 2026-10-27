---
title: "Three CSVs In, 1,272 Food Pages Out: PregNut's Boring Static Build"
slug: "three-csvs-in-1272-food-pages-out-pregnuts-boring-static-build"
author: "Yuriy Stasyuk"
source: "devto_webdev"
published: "Tue, 27 Oct 2026 17:29:45 +0000"
description: "PregNut is a free pregnancy food lookup I've been building since 2018. You search a food and see how 100 grams of it stacks up against the daily amounts preg..."
keywords: "food, page, one, has, data, reference, pages, pregnut"
generated: "2026-10-27T17:47:39.000183"
---

# Three CSVs In, 1,272 Food Pages Out: PregNut's Boring Static Build

## Overview

PregNut is a free pregnancy food lookup I've been building since 2018. You search a food and see how 100 grams of it stacks up against the daily amounts pregnancy asks for. It has 1,272 foods and 13 nutrients, and each food gets its own page. There's no database server behind it. It's an Eleventy site that builds from three CSV files and deploys to Cloudflare Pages. I like boring stacks for side projects, and this one has stayed easy to work on through three pregnancies, so here's how it fits together. The inputs The database/ folder has three files: FoodList.csv , NutrientList.csv and daily requirements.csv . The food list has the USDA NDB number, name, food group and a warning field. The nutrient list is long and skinny, one row per food per nutrient with a value and a unit. The requirements file has the daily reference amount for each nutrient as a label like "1000 mg" or "0.3 g." All of it comes from a fixed snapshot of the USDA's SR Legacy data. USDA's final Standard Reference release was in 2018, so the numbers are frozen. For a reference site I count that as a feature. A value doesn't change under you between builds. The cost is that newer data and current product labels can differ, and the About page says that. A tiny build script instead of a dependency scripts/build-fooddata.js reads the CSVs and writes one JSON file the site uses everywhere. I wrote a minimal CSV parser for it, small enough to read in one sitting. It handles quoted fields and doubled quotes, and it strips a byte order mark if there is one. That BOM will quietly rename your first column header if you don't strip it. The requirements file has a reference list under the main table, so the parser stops when it hits the SourceId row. Reference amounts get parsed with a small regex into a number and a unit. One choice I'd make again. If the CSVs aren't present but the JSON already exists, the script prints a warning and keeps the existing JSON instead of failing. That lets a deploy work from the committed JSON alone. One page per food with pagination Eleventy's pagination does the heavy lifting. The food page template paginates over a data file with size: 1 , so every item becomes its own page. The permalink is /food/{{ food.slug }}/ , and the slug starts with the USDA number: /food/15151-shrimp-cooked/ , /food/15152-shrimp-canned/ . Food names repeat a lot in USDA data. The number keeps every URL unique without me thinking about it. The data file is also where per-page decisions live. Title overrides for pages that get search traffic, related blog posts, and special cases. The human milk record, for example, stays in the dataset but is labeled as a historical data record only and left out of the food listings. Units needed a helper. DHA is stored in grams and its benchmark is 0.3 g, while other nutrients are in mg or mcg. There's a small conversion function so comparisons always happen in the same unit. Each page shows two columns: per 100 g, and a serving based on FDA reference amounts. Cooked shrimp shows 3 oz (85 g) next to 100 g. The 100 g column is for comparing foods. The serving column is closer to what's on a plate. What the data can't do The dataset has no iodine values. Rather than fake it, the site has an iodine guide and says the data is missing. Folate is shown as DFE, which isn't the same thing as the folic acid number on a prenatal label, so that gets its own guide too. PregNut is an educational reference and isn't medical advice. Every page says so in the footer. Deploys and one contact form A GitHub Actions workflow runs npm run build and deploys with wrangler. Pushes to master go to pregnut.com. Pull requests get a preview deploy, and the link gets posted on the PR. Previews are only built for branches in the repo, and the actions are pinned to commit SHAs. The *.pages.dev hosts send X-Robots-Tag: noindex from _headers , so Google only indexes the real domain. The one dynamic piece is /api/contact , a Cloudflare Pages Function. I wanted a free email relay and picked FormSubmit, which turned out to refuse requests coming from Workers. So the function does validation, a honeypot, a timing check and rate limiting, and only then hands the browser the relay endpoint to send to. Bots that fail the checks never see it. If you want to see the output, open any food page on pregnut.com and view source. The numbers and the notes are right there in the HTML.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ystasyuk/three-csvs-in-1272-food-pages-out-pregnuts-boring-static-build-2il4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
