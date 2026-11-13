---
title: "How to fix "SPF permerror: too many DNS lookups""
slug: "how-to-fix-spf-permerror-too-many-dns-lookups"
author: "Hanzala Rasool"
source: "devto_webdev"
published: "Fri, 13 Nov 2026 05:43:13 +0000"
description: "SPF has a hard limit: checking your record may take no more than 10 DNS lookups . Go over it and the result is permerror , which many receivers treat as a fa..."
keywords: "spf, your, lookups, you, dkim, record, include, count"
generated: "2026-11-13T05:58:50.742015"
---

# How to fix "SPF permerror: too many DNS lookups"

## Overview

SPF has a hard limit: checking your record may take no more than 10 DNS lookups . Go over it and the result is permerror , which many receivers treat as a failed SPF check, so your mail is more likely to land in spam. It usually creeps up on you as you add more services that send email for you. What counts towards the 10 Counts: include: , a , mx , ptr , exists: and redirect= Doesn't count: ip4: , ip6: and all Nested lookups count too. include:_spf.google.com is one lookup, but Google's record includes others, and those count against your 10 as well. Find what's using your lookups Look at your current record: nslookup -type=txt yourdomain.com Count every include , a , mx , ptr and exists , then repeat for each included domain. Or paste your domain into a checker that does it for you, like this free SPF & DMARC check . If the top level is already close to 10, the includes inside it almost certainly push you over. Five ways to get under the limit Remove services you no longer use. Old newsletter tools and CRMs are the usual culprits. Replace a and mx with ip4: if your own servers have fixed IP addresses. IP addresses don't use lookups. Remove ptr . It's deprecated and slow anyway. Send marketing mail from a subdomain , such as news.yourdomain.com , with its own SPF record. Each domain gets its own 10 lookups. Flatten carefully. Replacing an include with the IP addresses it contains saves lookups, but if the provider changes its IPs your SPF silently breaks. Only flatten with a tool that keeps it updated. Don't forget DKIM DMARC passes if either SPF or DKIM passes and aligns with your domain. Setting up DKIM for every service that sends as you makes SPF less critical, and some services can't be added to SPF at all without going over the limit. Quick end-to-end test: send yourself an email in Gmail, open it, choose Show original , and look for PASS next to SPF, DKIM and DMARC. Originally published at imageconvert.art , where there's also a full SPF, DKIM and DMARC setup guide .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hanzala_rasool_6d069eeab1/how-to-fix-spf-permerror-too-many-dns-lookups-1f0a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
