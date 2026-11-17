---
title: "Site Works for Me but Not for Them: A 5-Step Debugging Checklist"
slug: "site-works-for-me-but-not-for-them-a-5-step-debugging-checklist"
author: "Baleeghuddin shaikh"
source: "devto_webdev"
published: "Tue, 17 Nov 2026 15:43:13 +0000"
description: "A client messages you: "The site is down." You open it, and it loads perfectly. You try your phone, and it works there too. So who is right? Usually both. "W..."
keywords: "your, not, step, you, different, dns, site, network"
generated: "2026-11-17T15:45:53.612389"
---

# Site Works for Me but Not for Them: A 5-Step Debugging Checklist

## Overview

A client messages you: "The site is down." You open it, and it loads perfectly. You try your phone, and it works there too. So who is right? Usually both. "Works for me" and "down for them" can both be true at the same time, because the path from their browser to your server is not the same as yours. Different DNS resolvers, different caches, different networks, different devices. This is the checklist I run through, in order. Each step rules out a whole category of problems. Step 1: Check from outside your own network Your browser is the worst witness. It has cached DNS, cached redirects, maybe a cached HSTS policy, and it is sitting on your network. Start with an external check that requests the page from a different location: Or use an online website status checker . If the external check also fails, the site really is down. If it succeeds, keep going. The problem is somewhere between them and you. Step 2: Compare DNS answers If you recently changed hosting or DNS records, different resolvers may still be returning different answers. Their ISP's resolver may hold the old IP for the length of the old TTL. If those two disagree, or disagree with your authoritative nameserver, that is your answer. Wait out the TTL, or ask the user to flush their DNS. A DNS lookup tool shows what public resolvers return without touching your local cache. Step 3: Check the SSL certificate chain This is the one that hides best. If your server sends its certificate but not the intermediate certificate, most desktop browsers quietly fetch the missing piece and show a padlock. Many mobile browsers, older devices and command-line tools do not, and they show a security warning instead. So the site works on your laptop and fails on their phone. Count the certificates in the output. If you only see one, the chain is incomplete. With Let's Encrypt, the fix is almost always pointing your server at fullchain.pem instead of cert.pem . An SSL checker shows the full chain from outside your network. Step 4: Follow the redirects Redirect rules can behave differently depending on cookies, location, device or whether the visitor typed www . A user stuck in ERR_TOO_MANY_REDIRECTS will see a broken site while yours loads fine. This shows every hop and its status code. More than one or two hops, or the same URL appearing twice, means a rule needs fixing. A redirect checker does the same from outside your network. Step 5: Test the port from outside If the page times out for them, a firewall may be dropping traffic from their network or region. Testing from your own machine bypasses that firewall, so it proves nothing. Run that from another network, or use an external open port checker . A refused connection means the service is not listening. A timeout means something is silently dropping the packets. The Short Version When a site works for you but not for someone else, do not start with the server logs. Start by checking the path: an external status check, then DNS answers from public resolvers, then the certificate chain, then the redirect chain, then the port from outside. One of those five almost always explains the difference. I keep free versions of all of these checks at Web Tools Realm . No sign-up, and they run from the server side, so the results are not affected by your browser's cache.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/baleeghuddin_shaikh_ed093/site-works-for-me-but-not-for-them-a-5-step-debugging-checklist-47bo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
