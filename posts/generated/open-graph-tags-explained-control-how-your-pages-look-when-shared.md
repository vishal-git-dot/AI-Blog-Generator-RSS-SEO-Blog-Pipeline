---
title: "Open Graph Tags Explained: Control How Your Pages Look When Shared"
slug: "open-graph-tags-explained-control-how-your-pages-look-when-shared"
author: "Snappy Tools"
source: "devto_webdev"
published: "Fri, 12 Jun 2026 10:17:35 +0000"
description: "Every time someone shares a link on Twitter/X, LinkedIn, or Slack, a card appears with an image, title, and description. That card is controlled by Open Grap..."
keywords: "meta, image, twitter, content, tags, card, title, page"
generated: "2026-06-12T10:23:24.148604"
---

# Open Graph Tags Explained: Control How Your Pages Look When Shared

## Overview

Every time someone shares a link on Twitter/X, LinkedIn, or Slack, a card appears with an image, title, and description. That card is controlled by Open Graph meta tags — and if you don't set them, the social platform guesses, usually badly. What are Open Graph tags? Open Graph (OG) is a protocol invented by Facebook that lets you control the "preview card" for your page when shared on social networks. You add <meta> tags to your page's <head> , and social platforms read them when generating the link preview. <meta property= "og:title" content= "My Page Title" > <meta property= "og:description" content= "A one-sentence summary of the page." > <meta property= "og:image" content= "https://example.com/og-image.png" > <meta property= "og:url" content= "https://example.com/my-page/" > <meta property= "og:type" content= "website" > <meta property= "og:site_name" content= "My Site" > The minimum required set These four tags are the most important: Tag Purpose Recommended og:title Card headline Under 60 chars og:description Subtitle text Under 155 chars og:image Preview image 1200×630px min og:url Canonical URL of the page Full absolute URL Without og:image , most platforms either show nothing or scrape a random image from the page. Always provide one. Twitter-specific tags Twitter/X uses Open Graph as a fallback but has its own tags for finer control: <meta name= "twitter:card" content= "summary_large_image" > <meta name= "twitter:title" content= "My Page Title" > <meta name= "twitter:description" content= "Short summary here." > <meta name= "twitter:image" content= "https://example.com/og-image.png" > twitter:card has two common values: summary_large_image — wide image above title (most common) summary — small square thumbnail to the left of title Image size and format Recommended : 1200×630px (Facebook, Twitter, LinkedIn) Minimum : 600×315px (lower quality but works) Format : JPEG for photos, PNG for graphics with text File size : under 1MB for fast load Twitter has a 5MB hard limit. LinkedIn accepts JPG, PNG, and GIF. Article-specific tags For blog posts, add og:type and the article properties: <meta property= "og:type" content= "article" > <meta property= "article:author" content= "https://example.com/about" > <meta property= "article:published_time" content= "2026-06-12T10:00:00Z" > For most pages (landing pages, tools, product pages), og:type should be website . Testing your tags After deploying your OG tags, validate them with: Facebook : developers.facebook.com/tools/debug/ Twitter/X : cards-dev.twitter.com/validator LinkedIn : linkedin.com/post-inspector/ These tools show exactly what the card looks like and flag any missing required tags. Common mistakes Relative URLs for og:image : always use absolute URLs including https:// Missing og:url : without this, some platforms generate duplicate entries in their cache Title too long : over 60 chars gets truncated with "…" in most platforms No image : guaranteed poor-looking share — provide one even if it's just a branded default Tools Rather than writing tags from scratch, use a generator to fill in the fields and see a live preview before deploying. The OG Meta Tag Generator at SnappyTools lets you enter your title, description, image URL, and page URL, then shows you what the Twitter card, Facebook card, and LinkedIn card will look like — all in the browser, no URL required.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/snappy_tools/open-graph-tags-explained-control-how-your-pages-look-when-shared-4lnb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
