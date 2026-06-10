---
title: "I built a zero-dependency city search library with 50,000 cities built-in"
slug: "i-built-a-zero-dependency-city-search-library-with-50000-cities-built-in"
author: "Amit Kumar Raikwar"
source: "devto_webdev"
published: "Wed, 10 Jun 2026 20:29:44 +0000"
description: "Most geo projects need city search, distance calculation, or nearest location logic at some point. The usual answer is "hit a third-party API." But that mean..."
keywords: "novaedgedigitallabs, citykit, cities, search, distance, nearest, api, import"
generated: "2026-06-10T20:38:15.850888"
---

# I built a zero-dependency city search library with 50,000 cities built-in

## Overview

Most geo projects need city search, distance calculation, or nearest location logic at some point. The usual answer is "hit a third-party API." But that means latency, rate limits, API keys, and cost. I built @novaedgedigitallabs/citykit to solve this — a zero-dependency utility library that ships with a full dataset of 49,992 cities across 242 countries , ready to use offline. Install npm install @novaedgedigitallabs/citykit No API key. No setup. Works in Node.js and TypeScript out of the box. What it can do 1. Search cities import { search } from ' @novaedgedigitallabs/citykit ' ; const results = search ( ' Mumbai ' ); console . log ( results ); // [{ name: 'Mumbai', country: 'IN', lat: 19.0760, lng: 72.8777, ... }] Fuzzy-friendly, returns ranked matches. 2. Calculate distance between two cities (Haversine) import { distance } from ' @novaedgedigitallabs/citykit ' ; const km = distance ( { lat : 22.7196 , lng : 75.8577 }, // Indore { lat : 19.0760 , lng : 72.8777 } // Mumbai ); console . log ( km ); // ~590 km Uses the Haversine formula — accurate great-circle distance, no API needed. 3. Find nearest cities to a location import { nearest } from ' @novaedgedigitallabs/citykit ' ; const cities = nearest ({ lat : 22.7196 , lng : 75.8577 }, 5 ); // Returns 5 closest cities to Indore Great for "cities near me" features. 4. Filter by country, state, or continent import { filterByCountry , filterByContinent } from ' @novaedgedigitallabs/citykit ' ; const indianCities = filterByCountry ( ' IN ' ); const europeanCities = filterByContinent ( ' EU ' ); 5. Country and capital data import { getCountry , getCapital } from ' @novaedgedigitallabs/citykit ' ; getCountry ( ' IN ' ); // { name: 'India', code: 'IN', continent: 'AS', ... } getCapital ( ' IN ' ); // 'New Delhi' Why zero dependencies? Most libraries in this space pull in heavy geo packages or call external APIs. citykit bundles the dataset directly — the tradeoff is a slightly larger install size, but you get: Works fully offline No rate limits No API keys to manage No latency from network calls Predictable behavior in serverless / edge environments There's also a lightweight variant if you only need basic search without the full dataset. Real use cases I've used it for Autocomplete city input on a form (no API call on every keystroke) Distance filter for a property listing platform "Nearest branch" feature for a business directory Seeding a database with city/country data 15 functions, one import The full list: search , distance , nearest , filterByCountry , filterByState , filterByContinent , filterByRadius , getCountry , getCapital , getAllCountries , getCitiesByPopulation , getCity , getContinents , listCountries , lightSearch Links npm: npmjs.com/package/@novaedgedigitallabs/citykit GitHub: github.com/novaedgedigitallabs/citykit More OSS from NovaEdge: novaedgedigitallabs.tech/open-source If it saves you time, consider supporting the work . This is v1.2.0 — actively maintained. Issues and PRs welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/amitkumarraikwar/i-built-a-zero-dependency-city-search-library-with-50000-cities-built-in-5ek9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
