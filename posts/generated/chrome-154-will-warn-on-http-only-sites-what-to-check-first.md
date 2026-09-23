---
title: "Chrome 154 Will Warn on HTTP-Only Sites: What to Check First"
slug: "chrome-154-will-warn-on-http-only-sites-what-to-check-first"
author: "WebPixie"
source: "devto_webdev"
published: "Wed, 23 Sep 2026 11:00:00 +0000"
description: "Chrome 154 ships in October 2026 and turns on "Always Use Secure Connections" by default for everyone — not just the ~1 billion users already on Enhanced Saf..."
keywords: "http, subdomain, chrome, you, https, one, redirect, list"
generated: "2026-09-23T11:11:45.086670"
---

# Chrome 154 Will Warn on HTTP-Only Sites: What to Check First

## Overview

Chrome 154 ships in October 2026 and turns on "Always Use Secure Connections" by default for everyone — not just the ~1 billion users already on Enhanced Safe Browsing since Chrome 147 in April. Chrome will try HTTPS first on any public site and warn before falling back to plain HTTP. Google's own announcement confirms the rollout timeline. Finding your subdomains for this isn't the hard part. Knowing which of the ones you find actually need fixing before October is the part most prep guides skip entirely. What actually triggers the warning (and what doesn't) The warning only applies to public sites. Private/local addresses — a router admin page at 192.168.0.1 , a single-label internal hostname, a corporate intranet shortlink — are excluded, since cert coverage doesn't apply cleanly to them. Worth knowing before you panic: Google's Chrome 141 experiment data shows the median user sees fewer than one warning a week, and the 95th-percentile user sees fewer than three. It doesn't repeat once a user's accepted a site. This isn't a wall of scary prompts — it's built to catch the occasional stale link to a subdomain nobody finished migrating. Finding subdomains vs. knowing which ones matter A wildcard Certificate Transparency query returns every subdomain a public CA has ever issued a cert for — including the staging environment and the marketing microsite nobody remembers standing up. That part's mechanical. The actual question Chrome 154 raises is different: a CT log entry tells you a cert was issued for a name. It doesn't tell you if that subdomain is still live, still public, or still HTTP-only. Treating every discovered subdomain as equally urgent turns a 5-minute check into a week of chasing dead ends. Four questions to triage the list: Is it actually reachable right now? A subdomain with a stale DNS record or a decommissioned host won't trigger a warning for anyone, because nobody's loading it. Confirm reachability before spending time on it. Does it redirect to HTTPS, or serve content directly over HTTP? A same-host redirect from HTTP to HTTPS means Chrome never gets far enough to warn. A subdomain serving real content over plain HTTP — or redirecting through a chain with an insecure hop along the way — is the actual risk. Does the redirect chain stay on infrastructure you still control? A chain bouncing through an old CDN entry, a decommissioned redirect service, or a domain you no longer renew is worth flagging even if it currently works — it can silently break in a way that looks identical to the Chrome warning. Is anything on the page still loaded over plain HTTP? An otherwise-HTTPS page pulling an image, script, or stylesheet from an http:// URL creates mixed-content warnings independent of this Chrome change — worth fixing in the same pass since you're already there. A fast first pass For each subdomain on your list, one command shows most of what matters, following every redirect and printing each hop: curl -sIL http://subdomain.example.com A clean 301/302 straight to HTTPS on the same host? Deprioritize it. Anything serving content directly over HTTP, or taking more than one hop to reach HTTPS, goes on the actual fix list. Before October Pull your subdomain list from a wildcard CT log query if you haven't already Run the redirect-chain check on each one — deprioritize clean same-host HTTPS redirects, flag everything else Fix the flagged list, not the whole inventory — most discovered subdomains will already redirect cleanly Put the fixed subdomains under ongoing monitoring — a one-time audit answers today's question, not next quarter's, since a subdomain that passes today can silently regress to HTTP-only later without anyone noticing until the next Chrome release makes it visible to every visitor We covered the exact CT-log query pattern for step one in more depth on the WebPixie blog , including what each log entry actually tells you — and WebPixie's Certificates Manager surfaces that same subdomain list with one click to add any of them to ongoing monitoring, if you'd rather not run the CT query by hand every time.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/webpixie/chrome-154-will-warn-on-http-only-sites-what-to-check-first-1o0g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
