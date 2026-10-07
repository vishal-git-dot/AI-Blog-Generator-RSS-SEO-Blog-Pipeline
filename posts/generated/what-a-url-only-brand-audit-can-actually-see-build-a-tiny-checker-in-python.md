---
title: "What a URL-Only Brand Audit Can Actually See: Build a Tiny Checker in Python"
slug: "what-a-url-only-brand-audit-can-actually-see-build-a-tiny-checker-in-python"
author: "Ujjwal Dubey"
source: "devto_python"
published: "Wed, 07 Oct 2026 05:02:29 +0000"
description: "There are a lot of "free AI brand audit" tools now. Before trusting any of them, it helps to know what a tool can actually see when all you give it is a URL...."
keywords: "soup, title, text, what, url, you, get, can"
generated: "2026-10-07T05:20:33.231782"
---

# What a URL-Only Brand Audit Can Actually See: Build a Tiny Checker in Python

## Overview

There are a lot of "free AI brand audit" tools now. Before trusting any of them, it helps to know what a tool can actually see when all you give it is a URL. Short answer: less than you think, but more than nothing. I help build one (a free URL-based brand audit tool called Vibe Checker), and this post is the honest version of how the inputs work, with a tiny checker you can run yourself. What is in the HTML From a single fetch you can get: <title> , meta description, Open Graph tags The H1 and the first few headings Visible text above a rough "first screen" cut-off Buttons and links that look like calls to action Image alt text Linked stylesheets and font families Inline colours, if any What you cannot get without rendering: computed colours, real layout, what is actually above the fold on a phone, and anything injected by JavaScript. (If your tool page is client-rendered, crawlers and AI assistants see almost nothing. Ask me how I know.) A tiny checker import re , sys import requests from bs4 import BeautifulSoup CTA_WORDS = re . compile ( r " \b(book|get|start|try|buy|contact|request|schedule|sign up|demo)\b " , re . I ) HYPE = re . compile ( r " \b(revolutionary|world-class|cutting-edge|transform|seamless|best-in-class)\b " , re . I ) def check ( url ): html = requests . get ( url , timeout = 15 , headers = { " User-Agent " : " tiny-brand-check/0.1 " }). text soup = BeautifulSoup ( html , " html.parser " ) for s in soup ([ " script " , " style " , " noscript " ]): s . decompose () title = ( soup . title . string or "" ). strip () if soup . title else "" h1 = [ h . get_text ( " " , strip = True ) for h in soup . find_all ( " h1 " )] desc = soup . find ( " meta " , attrs = { " name " : " description " }) text = soup . get_text ( " " , strip = True ) first_screen = " " . join ( text . split ()[: 120 ]) ctas = [ a . get_text ( " " , strip = True ) for a in soup . find_all ([ " a " , " button " ]) if CTA_WORDS . search ( a . get_text ( " " , strip = True ))] fonts = set ( re . findall ( r " family=([A-Za-z+]+) " , html )) return { " title " : title , " h1_count " : len ( h1 ), " h1 " : h1 [: 2 ], " meta_description " : desc [ " content " ][: 160 ] if desc and desc . get ( " content " ) else None , " words_in_html " : len ( text . split ()), " hype_words_first_screen " : HYPE . findall ( first_screen ), " distinct_ctas " : sorted ( set ( ctas ))[: 8 ], " google_fonts " : sorted ( fonts ), } if __name__ == " __main__ " : for k , v in check ( sys . argv [ 1 ]). items (): print ( f " { k : 24 } { v } " ) Run it: python check.py https://example.com . How to read the output h1_count of 0 or more than 1 : the page has no single main message. words_in_html very low : the content is rendered by JavaScript; crawlers may see a blank page. Hype words in the first screen : big promises without specifics usually read as generic. More than three distinct CTAs : visitors have to choose, and many choose nothing. Title and H1 disagree : search and visitors get two different stories. Where AI helps (and where it does not) The script finds structure. Judging tone (is this playful or corporate? does it match the stated audience?) is where a language model is useful: give it the first-screen text, the CTAs and the stated audience, and ask for a mismatch, not a grade. Keep the output short and actionable; nobody acts on a 40-metric report. What no URL-only tool can see: your customers. Treat any score as a second opinion. If you want the scoring approach we use spelled out, it is in the Vibe Checker scoring write-up.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_dubey_9/what-a-url-only-brand-audit-can-actually-see-build-a-tiny-checker-in-python-b0a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
