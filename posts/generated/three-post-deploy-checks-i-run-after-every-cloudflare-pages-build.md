---
title: "Three post-deploy checks I run after every Cloudflare Pages build"
slug: "three-post-deploy-checks-i-run-after-every-cloudflare-pages-build"
author: "MORINAGA"
source: "devto_webdev"
published: "Sun, 21 Jun 2026 09:33:33 +0000"
description: "After spending two weeks debugging issues that only showed up in production — a sitemap _redirects rule that was blocking my own sitemap-index.xml and a Blue..."
keywords: "sitemap, com, after, check, deploy, xml, domain, three"
generated: "2026-06-21T09:58:05.292758"
---

# Three post-deploy checks I run after every Cloudflare Pages build

## Overview

After spending two weeks debugging issues that only showed up in production — a sitemap _redirects rule that was blocking my own sitemap-index.xml and a Bluesky image upload race against Cloudflare Pages deploy lag — I added three post-deploy checks to my workflow. They're fast and specific to the failure modes I've actually hit, not a full end-to-end test suite. Three sites (aiappdex.com, findindiegame.com, ossfind.com) on Cloudflare Pages with Astro 5 SSG. Here's what I check. Check 1: Sitemap reachability The simplest check and the one I should have had from day one. After a Cloudflare Pages deploy, I verify that sitemap-index.xml is reachable and returning 200 on all three domains: for domain in aiappdex.com findindiegame.com ossfind.com ; do status = $( curl -s -o /dev/null -w "%{http_code}" "https:// $domain /sitemap-index.xml" ) echo " $domain /sitemap-index.xml → $status " if [ " $status " != "200" ] ; then echo "FAIL: $domain sitemap unreachable" fi done I also check sitemap-0.xml — the actual URL sub-sitemap that @astrojs/sitemap generates — and assert that it contains at least a minimum expected URL count. For aiappdex.com that threshold is 1,000; if it drops below that after a deploy, the ETL data pipeline probably broke silently. The reason this check exists: I had a _redirects rule rewriting sitemap-index.xml → sitemap-0.xml as an emergency workaround that turned out to be wrong. It was live for five days before I found it. The rule was blocking the real sitemap-index.xml from reaching crawlers while appearing fine in the browser (which followed the redirect). Curl with -o /dev/null -w "%{http_code}" doesn't follow redirects by default, so it would have caught this immediately. Check 2: IndexNow batch submission After every successful sitemap check, I run node scripts/indexnow.mjs . The script reads the live sitemap XML from each domain, collects all URLs, and POSTs them to the IndexNow endpoint for Bing, Yandex, Naver, and Seznam using site-specific keys. Output looks like: aiappdex.com: submitted 1179 URLs → 200 OK findindiegame.com: submitted 139 URLs → 200 OK ossfind.com: submitted 144 URLs → 200 OK If a site returns 403 from IndexNow it usually means the key verification file ( /<key>.txt ) wasn't deployed correctly or a _redirects rule is mangling the path. Catching this right after deploy matters because the IndexNow key-verification window isn't instantaneous — letting it sit in a broken state delays indexing. I wrote more about the IndexNow setup in this week's tools post . I run this manually after deploy rather than inline in the GitHub Actions workflow because the Cloudflare Pages build takes 2-3 minutes, and IndexNow works best with live URLs. Running it as a separate workflow_dispatch trigger after the deployment succeeds means I'm submitting URLs that are actually live rather than ones that might still be deploying. Check 3: Weekly Lighthouse spot-check The third check runs on a cron — Monday 04:30 UTC — not after every deploy. It's slower (3-4 minutes per site, nine URLs total), so daily would be wasteful for a static site that doesn't change at runtime. The workflow uses treosh/lighthouse-ci-action with one homepage and one deep entry page per site: matrix : site : - { domain : aiappdex.com , sample : /models/timm-vit-base-patch16-clip-224-openai/ } - { domain : findindiegame.com , sample : /games/dredge-1562430/ } - { domain : ossfind.com , sample : /alternatives/ghost/ } I'm watching for Performance below 80, CLS above 0.1, or accessibility score regression. Astro SSG with no client-side JS should hold steady on all three — if they slip it means something in Tailwind v4 config or the ad slot component changed the layout paint behavior. The results upload to temporaryPublicStorage so I can diff before/after on regressions. I don't set hard failure thresholds that block deploys. These sites are pre-revenue with essentially zero traffic right now; blocking a deploy because a Lighthouse score dropped from 94 to 88 would be disproportionate. I treat Lighthouse as a trend monitor, not a gate. What I'm deliberately not checking No uptime monitoring — I'm relying on Cloudflare's own infrastructure status. No end-to-end user flow tests. No API availability checks — the Turso DB is only queried at build time in SSG mode, so there's nothing to check at runtime. For a dynamically rendered site, those gaps would matter. For a static CDN deployment where the entire runtime is pre-built HTML, CSS, and a handful of JSON files, the three checks above cover the actual failure surface I've encountered. The publish pipeline has its own idempotency layer (it reads published_urls from article frontmatter and skips already-distributed posts), so I don't need to verify cross-posting state after each deploy. That's a separate concern. Part of an ongoing 6-month experiment running three AI-curated directory sites. The technical claims here are real; this article was AI-assisted.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/morinaga/three-post-deploy-checks-i-run-after-every-cloudflare-pages-build-4p0i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
