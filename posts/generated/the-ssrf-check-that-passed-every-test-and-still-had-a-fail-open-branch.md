---
title: "The SSRF check that passed every test and still had a fail-open branch"
slug: "the-ssrf-check-that-passed-every-test-and-still-had-a-fail-open-branch"
author: "takeaseat"
source: "devto_webdev"
published: "Sun, 02 Aug 2026 08:10:12 +0000"
description: "When an SSRF check cannot resolve a hostname, “allow and let the browser fail” is not a safe fallback. A URL-rendering service usually performs two separate ..."
keywords: "not, dns, fail, check, browser, url, address, const"
generated: "2026-08-02T08:30:38.167334"
---

# The SSRF check that passed every test and still had a fail-open branch

## Overview

When an SSRF check cannot resolve a hostname, “allow and let the browser fail” is not a safe fallback. A URL-rendering service usually performs two separate actions: resolve the hostname to decide whether the destination is private; and let a browser fetch the page, including redirects and subresources. If DNS resolution fails and the guard returns “not blocked”, the decision is fail-open. A later retry, a resolver change, or a rebinding window can produce an address the original check never approved. The browser request may also be a different URL from the one checked, so the guard has to run at the request boundary too. The safe default is small and boring: const dns = require ( ' node:dns ' ); async function isBlockedSSRF ( targetUrl ) { const parsed = new URL ( targetUrl ); if ( ! [ ' http: ' , ' https: ' ]. includes ( parsed . protocol )) return ' blocked_scheme ' ; const host = parsed . hostname . toLowerCase (); if ( isPrivateIp ( host )) return ' private_ip ' ; try { const addresses = await dns . promises . lookup ( host , { all : true }); for ( const address of addresses ) { if ( isPrivateIp ( address . address )) return ' resolved_private ' ; } } catch { // Unknown is not public. Fail closed. return `dns_resolution_failed: ${ host } ` ; } return null ; } That function is necessary but not sufficient. In a Playwright renderer, route every browser request ( **/* ), not only the initial page. Apply the same check to images, stylesheets, iframes, fetches, and redirect targets. Block link-local and metadata addresses, IPv4-mapped IPv6 forms, unspecified/local IPv6, and carrier-grade NAT ranges. Keep the URL length and scheme allowlists before DNS work. The regression test should force the resolver to throw, then assert a block reason—not merely assert that the function does not crash. In the implementation I worked on, the production helper was separated from a copied test fixture, the forced-DNS-failure case was added, and the security suite ended at 21 passed and 0 failed. The deployed container was then checked as a non-root node process; its direct origin, independent VM-WAN path, and public edge health all returned HTTP 200 after the change. There is a trade-off: fail-closed DNS behavior can reject legitimate renders during resolver incidents. That is an availability cost, but it is the correct side of the security boundary for a service that fetches attacker-selected URLs. Operators can add retry/backoff or an explicit, audited allowlist later; silently treating an unknown destination as public is not a recovery strategy. If you are building a URL-to-document service, the practical checklist is: reject non-HTTP(S) schemes before DNS; reject private and special-use IPs in every address family; fail closed on resolver errors and empty answers; re-check every browser request and redirect; test the real helper used in production; verify the image contains the helper after deployment. For a live example of the managed PDF API discussed here, see https://pdffleet.com/docs

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/takeaseatventure/the-ssrf-check-that-passed-every-test-and-still-had-a-fail-open-branch-jj6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
