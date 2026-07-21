---
title: "Read any URL's title, description, favicon, and OG image with one API call"
slug: "read-any-urls-title-description-favicon-and-og-image-with-one-api-call"
author: "clause-netizen"
source: "devto_webdev"
published: "Tue, 21 Jul 2026 14:00:38 +0000"
description: "Building a link preview means fetching a page, then parsing its <title> , meta description, favicon, and Open Graph tags out of the HTML. Each site nests tho..."
keywords: "com, github, https, url, title, you, rapidapi, favicon"
generated: "2026-07-21T14:05:44.043318"
---

# Read any URL's title, description, favicon, and OG image with one API call

## Overview

Building a link preview means fetching a page, then parsing its <title> , meta description, favicon, and Open Graph tags out of the HTML. Each site nests those in different places, some behind redirects or Cloudflare, and you end up maintaining a small scraper that breaks every few weeks. SiteIntel does the fetch and parse for you and returns the fields as JSON. One request The /v1/analyze endpoint takes a full url query param and returns the page's metadata. Here it is with curl: curl --request GET \ --url 'https://siteintel.p.rapidapi.com/v1/analyze?url=https://github.com' \ --header 'X-RapidAPI-Key: YOUR_KEY' \ --header 'X-RapidAPI-Host: siteintel.p.rapidapi.com' The url value is the full https:// address, not a bare domain. A trimmed response: { "query" : "https://github.com" , "final_url" : "https://github.com/" , "status" : 200 , "fetched_at" : "2026-07-21T14:02:11Z" , "title" : "GitHub · Build and ship software on a single, collaborative platform" , "description" : "Join the world's most widely adopted..." , "canonical" : "https://github.com/" , "lang" : "en" , "favicon" : "https://github.githubassets.com/favicons/favicon.svg" , "open_graph" : { "title" : "GitHub · Build and ship software" , "image" : "https://github.githubassets.com/assets/campaign-social.png" , "site_name" : "GitHub" , "type" : "object" }, "detected_tech" : [ "Ruby on Rails" , "Fastly" ], "social_links" : [ "https://twitter.com/github" ], "emails" : [], "server" : "GitHub.com" } In Node Global fetch covers this, no dependencies needed: async function linkPreview ( target ) { const res = await fetch ( `https://siteintel.p.rapidapi.com/v1/analyze?url= ${ encodeURIComponent ( target )} ` , { headers : { ' X-RapidAPI-Key ' : process . env . RAPIDAPI_KEY , ' X-RapidAPI-Host ' : ' siteintel.p.rapidapi.com ' , }, } ); if ( ! res . ok ) throw new Error ( `SiteIntel returned ${ res . status } ` ); const data = await res . json (); return { title : data . open_graph ?. title || data . title , description : data . description , image : data . open_graph ?. image , favicon : data . favicon , siteName : data . open_graph ?. site_name , url : data . final_url , }; } console . log ( await linkPreview ( ' https://github.com ' )); encodeURIComponent matters here since the target URL has its own query string and slashes that would otherwise break your request. The preview object falls back from the Open Graph title to the plain <title> when a page has no OG tags, which is common on older sites. What the fields give you The open_graph.image and favicon are what you render in a preview card. final_url is the address after redirects, so store that rather than the URL a user pasted. status tells you whether the fetch actually worked before you trust the rest. A practical use: a "paste a link" input in a CMS or chat app. On paste, call analyze , and render a card with the OG image, title, and favicon, the way Slack or Discord unfurl links. Because the parsing runs server-side, your frontend never touches the target page or its CORS rules. The detected_tech array (flat strings like "Fastly" ) and social_links are a bonus if you want to enrich the card or feed a CRM. Two sibling endpoints exist on the same base if you need them: /v1/seo-audit?url=... for an on-page SEO report and /v1/screenshot?url=... for a rendered image of the page. Repo with runnable examples: https://github.com/clause-netizen/siteintel-api (also on RapidAPI if you want a managed key).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/clausenetizen/read-any-urls-title-description-favicon-and-og-image-with-one-api-call-58dj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
