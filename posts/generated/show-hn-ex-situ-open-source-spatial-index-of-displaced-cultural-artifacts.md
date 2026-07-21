---
title: "Show HN: Ex Situ – Open-source spatial index of displaced cultural artifacts"
slug: "show-hn-ex-situ-open-source-spatial-index-of-displaced-cultural-artifacts"
author: "hbyel"
source: "hackernews"
published: "Tue, 21 Jul 2026 04:48:32 +0000"
description: "Hi, I designed and developed a spatial index that maps museum artefacts as connecting arcs/hyperlinks from their origin site to institutional location/source..."
keywords: "source, data, open, index, artifacts, museum, origin, institutions"
generated: "2026-07-21T08:36:53.661880"
---

# Show HN: Ex Situ – Open-source spatial index of displaced cultural artifacts

## Overview

Hi, I designed and developed a spatial index that maps museum artefacts as connecting arcs/hyperlinks from their origin site to institutional location/sources. The Index specifically looks at western/euro-american institutions and maps their collection categorised by them under Islamic art, Asian/African art, ethnological collections, Middle East, South America etc. Started as my MA thesis in 2022, kept building since, mostly solo with a little funding. Fully open source, self-hosted, AGPL-3.0, Next.js + Deck.gl on the frontend, Strapi backend, Python ETL pulling from museum open-access APIs. Currently indexing over 100k artifacts from all over the world, across 8 collections (Met, V&A, SMB Berlin). Recently added an md export so researchers can download provenance data for a filtered set of artifacts. The infrastructure is conceptualized as an indexer, not a hoster. Even images are kept as URLs pointing to the source institutions. It's connective tissue between archives that were never designed to speak to each other, with an origin-first search UI concept. The data model is on purpose flat, to avoid encoding problematic taxonomies, and routes researchers directly to the source giving responsibility to the source institutions rather than duplicating institutional data. It indexes the relationship between origin sites and destination collections. Coming from a design background, taking this project from prototype to production app has been incredibly rewarding, but honestly it’s getting a little bit overwhelming to scale alone. I would love community’s feedback on performance scaling, any code contributions, data pipelines for missing museum apis or general feedback. Repo: https://github.com/hburakyel/ex-situ Live: https://exsitu.app Comments URL: https://news.ycombinator.com/item?id=48988158 Points: 28 # Comments: 16

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://exsitu.app/map

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
