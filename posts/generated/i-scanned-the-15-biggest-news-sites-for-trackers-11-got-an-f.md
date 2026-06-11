---
title: "I scanned the 15 biggest news sites for trackers. 11 got an F."
slug: "i-scanned-the-15-biggest-news-sites-for-trackers-11-got-an-f"
author: "Ghazanfar Uruj"
source: "devto_python"
published: "Thu, 11 Jun 2026 10:29:05 +0000"
description: "I built a small terminal tool called leakwatch that loads any website in a real browser, clicks through the cookie-consent wall, and shows you every tracker,..."
keywords: "com, leakwatch, yes, you, sites, trackers, fingerprinting, consent"
generated: "2026-06-11T10:47:52.346566"
---

# I scanned the 15 biggest news sites for trackers. 11 got an F.

## Overview

I built a small terminal tool called leakwatch that loads any website in a real browser, clicks through the cookie-consent wall, and shows you every tracker, data broker, fingerprinting trick, and session recorder watching you — rolled up to the companies they actually report to. Then I pointed it at the 15 biggest news sites. The results # Site Leakage Trackers Brokers Fingerprinting 1 foxnews.com 🔴 100 (F) 116 11 yes 2 usatoday.com 🔴 100 (F) 116 11 yes 3 forbes.com 🔴 100 (F) 113 11 yes 4 thesun.co.uk 🔴 100 (F) 113 14 yes 5 businessinsider.com 🔴 100 (F) 109 19 yes 6 cnn.com 🔴 100 (F) 108 13 yes 7 buzzfeed.com 🔴 100 (F) 96 15 yes 8 theguardian.com 🔴 100 (F) 81 12 yes 9 nbcnews.com 🔴 100 (F) 58 5 yes 10 cnbc.com 🔴 100 (F) 48 5 yes 11 of 15 scored a flat F . Business Insider leaks to 19 data brokers . Fox News and USA Today each load 116 trackers . Every single red site fingerprints your browser. (Reuters and Bloomberg sit behind hard paywalls / bot-walls — leakwatch flags those as "under-measured" rather than pretending they're clean.) How it works leakwatch runs a two-phase scan : It loads the page as a fresh anonymous visitor and records every request, cookie, storage write, and fingerprinting call. It defeats the cookie-consent wall — the ~dozen consent frameworks (OneTrust, Sourcepoint, Cookiebot, Quantcast, Didomi…) by their language-independent IDs — and records the tracker surge that only fires after you "accept." That second phase is the interesting part: plenty of sites fire trackers before you ever consent, and many more pile on the moment you click the button. It records only the tracking surface — network metadata, cookies, storage keys, fingerprinting call counts, and response headers. It never downloads or stores page content. Try it on your own sites pip install leakwatch playwright install chromium leakwatch nytimes.com You get a live, colour-coded terminal dashboard: a verdict line, a streaming request feed, a company rollup, and panels for fingerprinting, cookies/storage, and a security-headers grade. Other modes: leakwatch batch sites.txt --format markdown # the leaderboard above leakwatch diff your-site.com -b baseline.json # CI gate: fail on new trackers leakwatch example.com --json # machine-readable output Why I built it Most privacy tools tell you a site is "bad" without the receipts, and security recon usually means digging through devtools by hand. leakwatch does both in one pass and makes the result legible: who's watching you here, how badly, and what data leaves the page. Open source (MIT), built with Python · Textual · Playwright. GitHub: https://github.com/gazzycodes/leakwatch PyPI: pip install leakwatch Scan your own favourite sites and see who they sell you out to. 🔦

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ghazanfaruruj/i-scanned-the-15-biggest-news-sites-for-trackers-11-got-an-f-3in1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
