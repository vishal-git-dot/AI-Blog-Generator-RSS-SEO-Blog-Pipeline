---
title: "Get Google Trends 'Trending now' for any country with Python (RSS + a many-country shortcut)"
slug: "get-google-trends-trending-now-for-any-country-with-python-rss-a-many-country-shortcut"
author: "Hải Hà Phan Thanh"
source: "devto_python"
published: "Fri, 30 Oct 2026 04:56:16 +0000"
description: "Content, SEO and newsroom teams often want one thing from Google Trends: what is spiking right now in a given country. Google has no official API for it, but..."
keywords: "google, trending, trends, now, country, rss, actor, feed"
generated: "2026-10-30T05:13:18.341148"
---

# Get Google Trends 'Trending now' for any country with Python (RSS + a many-country shortcut)

## Overview

Content, SEO and newsroom teams often want one thing from Google Trends: what is spiking right now in a given country. Google has no official API for it, but the "Trending now" page is backed by a public RSS feed that needs no key, cookies or proxy. DIY: read the RSS feed # pip install requests import requests import xml.etree.ElementTree as ET NS = { " ht " : " https://trends.google.com/trending/rss " } def trending ( geo = " US " , n = 3 ): r = requests . get ( " https://trends.google.com/trending/rss " , params = { " geo " : geo }, headers = { " User-Agent " : " Mozilla/5.0 " }, timeout = 20 ) r . raise_for_status () items = ET . fromstring ( r . content ). find ( " channel " ). findall ( " item " )[: n ] return [{ " keyword " : it . findtext ( " title " ), " traffic " : it . findtext ( " ht:approx_traffic " , namespaces = NS ), " published " : it . findtext ( " pubDate " ), " news " : [ x . findtext ( " ht:news_item_title " , namespaces = NS ) for x in it . findall ( " ht:news_item " , NS )]} for it in items ] for t in trending ( " US " ): print ( t [ " traffic " ], " | " , t [ " keyword " ], " | " , t [ " published " ]) Output (30/10/2026): 5000+ | mia pohankova | Thu, 29 Oct 2026 21:40:00 -0700 10000+ | alphabet stock drop 500 billion | Thu, 29 Oct 2026 21:40:00 -0700 500+ | scarlett johansson | Thu, 29 Oct 2026 21:30:00 -0700 What you give up with the RSS feed: Traffic is a string bucket ( "5000+" ), not a number, and there is no % increase, end time, category or related queries. Timezone offsets in pubDate vary by feed, so normalise to UTC before comparing countries. No time window or category filter. You get Google's default list and filter it yourself. One request per country , and you have to dedupe between scheduled runs yourself. Many countries, categories, filters: the actor I built the Google Trends Trending Now actor to cover those gaps. It reads Google's Trending Now data for any country, with a 4/24/48/168-hour window, a category filter, an activeOnly switch and an onlyNew option for scheduled runs. Each record has numeric traffic, % increase, start/end time, active status, related queries, categories, an Explore link, and news items when Google publishes them. # pip install apify-client import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ " APIFY_TOKEN " ]) run = client . actor ( " bachiembmt/google-trends-trending-now " ). call ( run_input = { " countries " : [ " US " , " VN " ], " hours " : " 24 " , " categories " : [ " Technology " ], " maxItemsPerCountry " : 3 , }) for t in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): print ( t [ " country " ], t [ " approxTraffic " ], t [ " increasePercent " ], " % " , " active " if t [ " active " ] else " ended " , " | " , t [ " keyword " ]) Sample output (30/10/2026, abridged): US 5000 100 % ended | t-mobile spacex network deal rejection US 10000 100 % ended | nintendo switch zelda 40th anniversary VN 200 200 % active | apple ipad mini 8 VN 200 200 % ended | cve-2026-98432 A run like this takes a few seconds. Pricing is $1.50 per 1,000 trends, no subscription. When to use which One country, quick look: the RSS script above is enough. Many countries, category filters, numeric volumes, or a daily job that only reports new trends: use the actor, or extend the script yourself. Disclosure: I built and maintain the actor. It reads Google's public Trending Now endpoints.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hi_hphanthanh_41c4083/get-google-trends-trending-now-for-any-country-with-python-rss-a-many-country-shortcut-12kb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
