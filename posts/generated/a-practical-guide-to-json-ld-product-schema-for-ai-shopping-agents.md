---
title: "A practical guide to JSON-LD Product schema for AI shopping agents"
slug: "a-practical-guide-to-json-ld-product-schema-for-ai-shopping-agents"
author: "arnaud BUISINE"
source: "devto_webdev"
published: "Thu, 18 Jun 2026 15:26:00 +0000"
description: "AI shopping is real now. ChatGPT, Perplexity, Gemini and Claude all recommend products in their answers. If you run an e-commerce store, you've probably wond..."
keywords: "product, schema, agents, https, json, your, org, shopping"
generated: "2026-06-18T15:38:46.161781"
---

# A practical guide to JSON-LD Product schema for AI shopping agents

## Overview

AI shopping is real now. ChatGPT, Perplexity, Gemini and Claude all recommend products in their answers. If you run an e-commerce store, you've probably wondered whether your products even show up. Spoiler: probably not. After scanning ~500 stores at MerchantStamp, the average store scores 34/100 on AI-readiness. The most common gap, by far, is incomplete JSON-LD Product schema. This is a practical guide to fixing that — written for developers shipping e-commerce sites who want to be visible to AI agents without becoming a structured-data expert. Why AI agents need JSON-LD specifically AI shopping agents don't crawl your site like Google does. They prefer two sources, in order: Product feeds (Google Merchant, manufacturer feeds, marketplace APIs) JSON-LD Product schema embedded on the page If both exist and agree, your product is a candidate for recommendation. If they disagree, the agent down-weights the product (trust loss). If neither exists, you're invisible. Schema.org Product is a W3C/Schema.org standard with ~50 properties. Most stores implement ~6 and stop. To actually be agent-readable, you need ~12. The minimum viable Product schema Here's what every product page should have: \ `html { " @context ": " https://schema.org/ ", "@type": "Product", "name": "Waterproof Hiking Jacket", "description": "Lightweight, breathable waterproof jacket. Sealed seams, packable.", "image": " https://example.com/images/jacket-front.jpg ", "brand": { "@type": "Brand", "name": "OutdoorGear Co" }, "gtin13": "1234567890123", "sku": "WRJ-BLUE-M", "mpn": "OG-WRJ-2024", "offers": { "@type": "Offer", "url": " https://example.com/products/waterproof-jacket ", "priceCurrency": "EUR", "price": "149.99", "availability": " https://schema.org/InStock ", "seller": { "@type": "Organization", "name": "Example Store" } }, "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "328" } } ` \ The five properties everyone forgets In rank order of impact on AI recommendation rate: gtin13 / gtin12 / gtin — without it, AI can't cross-reference your product. Most underrated field by a country mile. availability — must match the visible page state. "InStock" on a sold-out product is a trust killer. aggregateRating — agents heavily weight this. Even modest ratings (4.0+) significantly improve recommendation rate. mpn — for products with a manufacturer part number, include it. Adds redundancy. shippingDetails inside offers — agents check this to filter by user location. How to verify it works Three tools to validate before shipping: Google Rich Results Test — https://search.google.com/test/rich-results Schema.org Validator — https://validator.schema.org MerchantStamp audit — https://merchantstamp.com/scan (free, no signup, runs the full 23-check battery agents actually use) The MerchantStamp tool goes further than the others because it checks not just schema validity, but agent-specific requirements: which bots are allowed in robots.txt, whether your policies are machine-readable, whether your feed and JSON-LD agree on price, etc. Full methodology at https://merchantstamp.com/methodology . The bigger picture Structured data is no longer a "rich snippets in Google" thing. It's the substrate AI shopping agents are built on. ChatGPT alone has 200M+ weekly users and shopping is becoming a flagship feature. If you're shipping e-commerce code in 2026, complete JSON-LD Product schema is no longer optional. It's the new equivalent of having a sitemap.xml.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arnaud_buisine_eea153b88a/a-practical-guide-to-json-ld-product-schema-for-ai-shopping-agents-46gf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
