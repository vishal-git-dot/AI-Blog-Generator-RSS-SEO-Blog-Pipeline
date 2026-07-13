---
title: "Building a Serverless Interactive Map for 68,000+ Indian Villages with Leaflet, PMTiles, and GitHub Actions"
slug: "building-a-serverless-interactive-map-for-68000-indian-villages-with-leaflet-pmtiles-and-github-actions"
author: "Manideep Chittineni"
source: "devto_webdev"
published: "Mon, 13 Jul 2026 14:42:22 +0000"
description: "Introduction: Navigating government data platforms to find precise administrative borders or village-level information can often be a cumbersome process invo..."
keywords: "data, github, pmtiles, serverless, actions, village, vector, local"
generated: "2026-07-13T14:46:38.575952"
---

# Building a Serverless Interactive Map for 68,000+ Indian Villages with Leaflet, PMTiles, and GitHub Actions

## Overview

Introduction: Navigating government data platforms to find precise administrative borders or village-level information can often be a cumbersome process involving captchas, slow load times, and fragmented data. To address this, we built Village Finder, a fully open-source, interactive mapping tool covering Andhra Pradesh, Telangana, Karnataka, and Tamil Nadu. What makes this project unique is its architecture: it manages data for over 68,000 villages, hosts complete visual maps, serves vector land parcels, updates daily, and features zero server costs. Here is how we built a highly scalable, serverless civic tech app using the modern web stack. The Stack Breakdown: The Data Pipeline (Python + GitHub Actions): Instead of hosting a database, our pipeline runs on a scheduled GitHub Action workflow (update-data.yml). It queries the official local government directory via the data.gov.in API, cross-checks against live site metrics, runs validation tests using pytest, and commits structured JSON/CSV files directly back into the repository. Serverless Vector Mapping (PMTiles & MapLibre): Handling cadastral data (individual survey plots and land parcels) across multiple states results in millions of polygons. Instead of spinning up an expensive PostGIS database and tile server, we compressed the geospatial data into PMTiles—a single-file archive format for vector tiles. The client browser queries specific byte ranges of the PMTiles archive hosted directly on a CORS-enabled cloud storage bucket. Approximating Local Language Support (IndicXlit neural models): A major hurdle was that the upstream API feeds lacked local script names (Telugu, Kannada, Tamil, etc.). To solve this without adding heavy dependencies to the runtime app, we leveraged the AI4Bharat IndicXlit neural model offline during the compilation step, generating a lightweight names_translit.json translation map used at runtime. Key Takeaways: By leaning into static site generation, edge-hosted assets, and GitHub Actions for continuous data integration, you can build incredibly robust, fast, and completely free public utility applications. Check out the live project or contribute a state here: https://github.com/mchittineni/india-village-finder

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mchittineni/building-a-serverless-interactive-map-for-68000-indian-villages-with-leaflet-pmtiles-and-github-4k42

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
