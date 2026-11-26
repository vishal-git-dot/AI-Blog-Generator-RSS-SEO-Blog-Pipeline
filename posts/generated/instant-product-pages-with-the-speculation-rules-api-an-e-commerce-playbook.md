---
title: "Instant product pages with the Speculation Rules API: an e-commerce playbook"
slug: "instant-product-pages-with-the-speculation-rules-api-an-e-commerce-playbook"
author: "not the same"
source: "devto_webdev"
published: "Thu, 26 Nov 2026 07:36:28 +0000"
description: "On a store, most navigations are predictable: catalog → product, product → another product, product → back to the catalog. Every one of those clicks normally..."
keywords: "page, product, prerender, not, cart, speculation, prefetch, rules"
generated: "2026-11-26T07:44:38.396474"
---

# Instant product pages with the Speculation Rules API: an e-commerce playbook

## Overview

On a store, most navigations are predictable: catalog → product, product → another product, product → back to the catalog. Every one of those clicks normally waits for the network, the server and the render. The Speculation Rules API lets the browser start that work before the click, so the next page appears almost instantly. It's a few lines of JSON, but on a store it needs care. Prerender the wrong URL and you add items to carts, inflate analytics or hammer your server. Here's how we set it up for online stores. 1. Prefetch vs prerender Prefetch downloads the HTML of the next page. Navigation skips the network wait, but the page still renders after the click. Prerender loads and renders the whole page in a hidden tab, scripts included. Navigation is close to instant, but it costs more: CPU, memory, and every request the page makes. For a catalog, prerender on hover is the sweet spot. Prefetch is the safe default everywhere else. 2. Start with document rules and moderate eagerness Instead of listing URLs, let the browser pick links on the page that match a pattern: <script type = "speculationrules" > { "prerender" : [ { "where" : { "and" : [ { "href_matches" : "/product/*" } , { "not" : { "selector_matches" : "[rel~=nofollow]" } } ] } , "eagerness" : "moderate" } ] , "prefetch" : [ { "where" : { "href_matches" : "/category/*" } , "eagerness" : "conservative" } ] } </script> eagerness decides when speculation starts: conservative – on pointer down / touch start; moderate – on hover (desktop) and on pointer down; eager and immediate – as soon as the rule matches. moderate for product links gives a head start of a few hundred milliseconds on desktop without prerendering half the catalog. Chrome also caps how many moderate/conservative prerenders it keeps at once and drops the oldest, so a shopper sweeping the mouse over a grid doesn't load fifty pages. 3. Exclude everything with side effects A prerendered page runs like a real visit. Never speculate on URLs that change state: { "where" : { "and" : [ { "href_matches" : "/*" } , { "not" : { "href_matches" : "/cart*" } } , { "not" : { "href_matches" : "/checkout*" } } , { "not" : { "href_matches" : "/my-account*" } } , { "not" : { "href_matches" : "/*\\?*add-to-cart=*" } } , { "not" : { "href_matches" : "/*logout*" } } ] } , "eagerness" : "conservative" } The classic trap in WooCommerce-style themes is an "Add to cart" link that is a plain <a href="?add-to-cart=123"> . A broad prerender rule turns hovering into adding. Exclude these URLs, or better, make add-to-cart a POST button. 4. Make your own scripts prerender-aware Third-party analytics tags from the big vendors generally wait for activation, but your own code may not. Anything that should only run when a person actually sees the page – view counters, "recently viewed" writes, chat greetings, A/B exposure events – should wait: function whenActivated ( callback ) { if ( document . prerendering ) { document . addEventListener ( 'prerenderingchange' , callback , { once : true } ) ; } else { callback ( ) ; } } whenActivated ( ( ) => { trackProductView ( productId ) ; saveRecentlyViewed ( productId ) ; } ) ; 5. Measure that it works On the destination page you can tell a prerendered navigation by activationStart : const [ nav ] = performance . getEntriesByType ( 'navigation' ) ; const wasPrerendered = nav . activationStart > 0 ; const wasPrefetched = nav . deliveryType === 'navigational-prefetch' ; Send these as a dimension with your page view or LCP data and compare product pages with and without speculation. In Chrome DevTools, Application → Background services → Speculative loads shows which rules matched, what was prerendered and why a speculation failed. 6. If you are on WordPress Since WordPress 6.8, core outputs speculation rules by default: prefetch with conservative eagerness, with cart-like and admin URLs excluded for common setups. That's a good baseline. To move to prerender on hover for products, use the Speculative Loading plugin settings or filter the rules, and keep the exclusions from step 3 for your store's own URLs. Checklist Prerender product links on hover ( moderate ), prefetch the rest on pointer down. Exclude cart, checkout, account, logout and any add-to-cart GET links. Wrap view-tracking and other side effects in a prerenderingchange check. Log activationStart and deliveryType to see the real effect. Check DevTools → Speculative loads after every theme or plugin update. Speculation doesn't fix a slow server or a heavy page, but on a store with a decent baseline it removes most of the wait between "I like this" and "I see it". For the rest of the speed picture, see our PageSpeed optimization guide and website speed and sales . We're not the same , a web development studio from Ukraine working on e-commerce and B2B projects.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ntsame/instant-product-pages-with-the-speculation-rules-api-an-e-commerce-playbook-2jgk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
