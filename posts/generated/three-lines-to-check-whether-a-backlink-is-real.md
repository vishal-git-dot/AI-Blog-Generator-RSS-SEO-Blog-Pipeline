---
title: "Three lines to check whether a backlink is real"
slug: "three-lines-to-check-whether-a-backlink-is-real"
author: "Copero"
source: "devto_webdev"
published: "Wed, 18 Nov 2026 15:15:31 +0000"
description: "A directory dashboard told me my product page was live. The page did return 200, and it did have my name, my screenshot and my description on it. There was n..."
keywords: "page, not, link, anchor, live, site, html, check"
generated: "2026-11-18T15:25:47.040504"
---

# Three lines to check whether a backlink is real

## Overview

A directory dashboard told me my product page was live. The page did return 200, and it did have my name, my screenshot and my description on it. There was no link. Not a nofollow link — no anchor pointing at my domain at all. The site embedded my game inside its own page, so visitors played my game without ever leaving their site, and the only thing I had "earned" was a page that mentions me. That was a submission I could have skipped with about ten seconds of checking. Here is the check. First: is the page indexable? curl -sL -A "Mozilla/5.0" -o page.html -w 'HTTP %{http_code}\n' "https://example.com/your-listing" grep -oE '<meta[^>]+name="robots"[^>]*>' page.html If the output contains noindex , stop. Nothing after this matters: the page is telling search engines to ignore it, so the link on it is invisible no matter how clean its rel is. Two real examples, both "live" listings: <meta name = "robots" content = "noindex, follow" > <meta name = "robots" content = "index, follow, max-image-preview:large" /> The first is a free-tier directory page that becomes indexable only after a paid upgrade. It has been live for weeks. It has never passed a link. Second: does the canonical point at itself? grep -oE '<link[^>]+rel="canonical"[^>]*>' page.html You want the canonical URL to be the page you are looking at. If it points somewhere else — the site's homepage, a category page, a different host — you have found a page that is deliberately consolidating away from itself. Any link "on" it is being credited elsewhere or not at all. Watch the host too. https://uneed.best/tool/x redirects to https://www.uneed.best/tool/x , and the canonical there names the www version. That is fine, but it means the URL you submitted is not the URL that counts, and a check against the wrong one can look broken when it is not. Third: the anchor's rel , from the href , not from the text grep -oE '<a [^>]*href="[^"]*YOURDOMAIN[^>]*>' page.html Good output — no nofollow , no ugc , no sponsored : <a href = "https://yourdomain.com/?utm_source=site" rel = "noopener" > Bad output: <a href = "https://yourdomain.com/?ref=site" rel = "noopener nofollow" > And the output that is worse than bad, because it looks like nothing is wrong: <a href = "/go/your-product" rel = "nofollow noopener" > That is a redirect wrapper. The site routes every outbound click through its own /go/ endpoint, so the final destination is your domain but the anchor in the HTML points at theirs, with a nofollow on it. Your domain appears nowhere in the href . Four ways this check lies to you I hit all four of these in one afternoon, so they are not hypothetical. 1. The domain appears on the page but not in a link. On that page my domain appears twelve times — in the meta description, in structured data, in screen-reader text, in a description field — and zero times in an href . Text mentioning you is not a link to you. Grep for the anchor, not the word. 2. A stale file from the previous request. My first attempt at a batch printed HTTP 301 for one URL and left the previous site's HTML in page.html . The next three greps then reported a perfectly formed, followed anchor — belonging to a completely different site. It looked like a pass. Always print the status code and the byte count, and write each URL to its own file ( -o page-1.html , -o page-2.html ). 3. A blocked request read as "no link". One site returns 403 to a plain curl and serves the page fine to a browser. Reading that as "the anchor isn't there" is a false negative, and I made exactly that mistake: I concluded a listing had no link when the truth was that I had never seen the page. 401 , 403 , 405 , 429 , 503 and any captcha interstitial mean unknown , not no . Only a real 404 (or a page that is genuinely there and genuinely linkless) is a "no". 4. The page changes after you check. One listing in my ledger was dofollow on 2026-11-11 and reads rel="noopener noreferrer ugc nofollow" today. A one-time check is a snapshot. If the number matters, re-fetch it on a schedule and keep the date of the last check next to the verdict. Why bother, if the directory already says "live" Because "live" is a statement about their page, not about your link. In my own ledger, of the 13 "submitted" rows that had a public URL to check, the results were: What the page actually was Count Live, anchor is nofollow 5 Live, no anchor to my domain 4 Live, noindex 1 Dead (404) 2 Blocked / unreadable 1 Live with a followed anchor 0 Thirteen pages, all reachable, all describable as "listed" — zero links. The dashboard was not lying in any of those cases. It was answering a different question. What I store now For every listing, one row: URL, HTTP status, whether an anchor to my domain exists, its rel value, the robots meta, the canonical target, the fetch timestamp, and a SHA-256 of the body so I can tell "the page changed" from "I remember it differently". That is the whole system. It is three greps and a timestamp, and it turns "I submitted 21 backlinks" into "five of them are real" — which is a much less exciting sentence and a much more useful one. I build Copero, a free browser football career game — no download, no account: https://copero.games/?utm_source=devto&utm_medium=blog&utm_campaign=backlink-2026-11 Every number above comes from my own ledger, fetched and parsed on 2026-11-18. The commands are the ones I actually ran; the four failure modes are four mistakes I made running them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/copero_games/three-lines-to-check-whether-a-backlink-is-real-o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
