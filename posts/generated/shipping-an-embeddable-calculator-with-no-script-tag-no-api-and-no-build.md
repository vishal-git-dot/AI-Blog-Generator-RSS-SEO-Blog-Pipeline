---
title: "Shipping an Embeddable Calculator With No Script Tag, No API and No Build"
slug: "shipping-an-embeddable-calculator-with-no-script-tag-no-api-and-no-build"
author: "牛云鹏"
source: "devto_webdev"
published: "Mon, 26 Oct 2026 03:49:48 +0000"
description: "Every "add our widget to your site" instruction has quietly become the same thing: paste this <script> , load 180 KB of framework, and let us run code in you..."
keywords: "calculator, page, script, iframe, you, host, height, embed"
generated: "2026-10-26T04:10:10.672063"
---

# Shipping an Embeddable Calculator With No Script Tag, No API and No Build

## Overview

Every "add our widget to your site" instruction has quietly become the same thing: paste this <script> , load 180 KB of framework, and let us run code in your page. For a calculator that takes four numbers and does multiplication, that is a bad trade. Here is the version we ship instead, and why each decision went the way it did. One iframe, no script <iframe src= "https://optimetricshub.com/embed/churn" title= "Churn Rate Calculator" width= "100%" height= "700" style= "border:1px solid #e2e8f0;border-radius:12px" loading= "lazy" ></iframe> No script tag, no global object, no postMessage handshake, no CORS configuration, nothing added to the embedding page's bundle. The iframe is same-origin to us and cross-origin to you, which means the browser does the isolation for free. Why not a script tag A script tag needs an iframe anyway if you want real isolation. Once you have a <script src> on a third-party page you have inherited: Global namespace collisions. Two analytics widgets both defining window.__widget is a support ticket nobody can reproduce. CSS bleed. Any stylesheet you inject affects the host page. Shadow DOM fixes it, but then you are shipping the shadow-DOM polyfill or accepting a browser floor. A build to maintain. The script is a separate artefact from the page it mirrors, so formulas drift between your site and your embed. Consent and privacy review. A script that reads document.cookie on someone else's domain is a legal conversation. An iframe with no storage access is not. The iframe avoids all four, and costs one extra HTTP request that loading="lazy" mostly defers. Why the arithmetic runs client-side The calculator does not post the numbers anywhere. It computes in the browser and renders the result, which means: No backend to scale. A traffic spike costs nothing. No data-retention question. We cannot lose what we never receive, and the host page's privacy policy does not have to account for us. Instant results. No round trip between keystroke and answer. The trade-off is that the formulas ship to the reader. For a churn or runway calculator that is not a secret worth protecting — the formula is the product. Sizing without a scrollbar The annoying part of iframes is height. A frame that is 40 px too short produces a scrollbar inside a page that already scrolls, which reads as broken. Two options, in order of preference: Fixed heights per embed. Each calculator has a documented height that is slightly above its real content height. It is boring and it never breaks: no JS, no layout shift, no race between content and resize. postMessage + ResizeObserver . Send the content height from inside the frame and set the iframe height on the host. Correct and adaptive, but it needs a script on the host page — which is the thing we were avoiding. We document fixed heights because option 2 undoes the whole design. The heights are in the embed catalogue , along with the snippet for each calculator. The part that is actually load-bearing The frame contains a visible link back to the full tool page. That link is the entire business model: the calculators are free, there is no signup, and the only requirement for embedding is that the attribution stays. This is also why the embed pages are noindex . An embedded copy of a calculator that got indexed would compete with the canonical tool page for the same query, and the site would be cannibalising itself from the inside. What we gave up A widget with postMessage can do things an iframe cannot: push a result into the host page's form, react to the host's theme, participate in the host's state. If you are building a chart library, use a script. If you are building a calculator that takes four numbers, the iframe wins on every axis that matters. The three free calculators most likely to be useful in a docs page or a course: Churn rate calculator — customer and revenue churn, plus a 12-month compounding projection CAC payback calculator — months to recover acquisition cost Runway calculator — net burn, runway, zero-cash date All six are listed together, with copy-paste snippets, at optimetricshub.com/embeds .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/optimetricshub/shipping-an-embeddable-calculator-with-no-script-tag-no-api-and-no-build-2624

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
