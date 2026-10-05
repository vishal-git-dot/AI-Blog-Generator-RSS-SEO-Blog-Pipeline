---
title: "Tell HN: Uceprotect is extorting website owners"
slug: "tell-hn-uceprotect-is-extorting-website-owners"
author: "goldenmember"
source: "hackernews"
published: "Mon, 05 Oct 2026 12:35:55 +0000"
description: "I recently discovered by accident that our website was being blocked by Orange's security filters. After a quick check, I found that our IP address is listed..."
keywords: "uceprotect, listed, asn, digitalocean, other, your, website, our"
generated: "2026-10-05T14:10:16.262308"
---

# Tell HN: Uceprotect is extorting website owners

## Overview

I recently discovered by accident that our website was being blocked by Orange's security filters. After a quick check, I found that our IP address is listed on UCEPROTECT Level 3. The listing is based on the reputation of the entire ASN 14061 (DigitalOcean, US) [1]. In other words, even if your IP did nothing wrong, it will still be listed because of its ASN. If your site is innocent and listed only because it's hosted on DigitalOcean, UCEPROTECT offers to whitelist it for about $30/month or $108/year [2]. I checked the ASNs of several other popular hosting providers, and they're all listed too. So if your site is hosted on DigitalOcean or any other major provider, it's probably blacklisted as well. That can cut you off from customers on mobile networks like Orange, whose "cybersecurity protection" uses blacklists like UCEPROTECT to filter traffic. Honestly, in my 20-year career, this is the first time I've seen a blacklist misbehave this badly and ask for money when there's clearly been no wrongdoing. [1] http://www.uceprotect.net/en/rblcheck.php?asn=14061 [2] https://www.whitelisted.org/ Comments URL: https://news.ycombinator.com/item?id=49964045 Points: 21 # Comments: 8

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://news.ycombinator.com/item?id=49964045

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
