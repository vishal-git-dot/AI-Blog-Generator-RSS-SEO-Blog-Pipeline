---
title: "Getting the right favicon for 1,000 domains is harder than it looks"
slug: "getting-the-right-favicon-for-1000-domains-is-harder-than-it-looks"
author: "COFFEE CAT"
source: "devto_python"
published: "Fri, 27 Nov 2026 07:29:02 +0000"
description: "If you have a list of company domains (a CRM export, a directory, a bookmarks app) and want a small logo next to each one, the obvious approach is https://ex..."
keywords: "icon, sizes, favicon, ico, icons, you, link, png"
generated: "2026-11-27T07:44:07.268121"
---

# Getting the right favicon for 1,000 domains is harder than it looks

## Overview

If you have a list of company domains (a CRM export, a directory, a bookmarks app) and want a small logo next to each one, the obvious approach is https://example.com/favicon.ico . It works for maybe half of the sites, and the result is often a blurry 16 px image. Here is what I learned while building a bulk favicon extractor, and the rules I ended up with. 1. /favicon.ico is the fallback, not the answer Most modern sites declare several icons in the HTML head: <link rel = "icon" href = "/favicon-32x32.png" sizes = "32x32" > <link rel = "apple-touch-icon" href = "/apple-touch-icon.png" sizes = "180x180" > <link rel = "mask-icon" href = "/safari-pinned-tab.svg" color = "#000" > <link rel = "manifest" href = "/site.webmanifest" > The 180 px apple-touch-icon is usually the best-looking one. Some sites have no /favicon.ico at all and only declare icons in <link> tags. 2. The biggest icons live in the web-app manifest The 192 px and 512 px icons are often only listed in site.webmanifest : { "icons" : [ { "src" : "/android-chrome-512x512.png" , "sizes" : "512x512" } ] } If you skip the manifest, you miss the highest-resolution logo the site has. 3. Never trust the sizes attribute Declared sizes are frequently wrong: sizes="192x192" on a 32 px file, or icons that return 404. The only reliable way is to download each candidate and read the real dimensions: from io import BytesIO from PIL import Image def measure ( data : bytes ) : with Image . open ( BytesIO ( data ) ) as im : if im . format == "ICO" : # .ico files hold several frames return max ( im . info [ "sizes" ] , key = lambda s : s [ 0 ] * s [ 1 ] ) return im . size 4. ICO files contain several images A favicon.ico typically holds 16, 32 and 48 px frames, and other tools may give you the first (smallest) one. Pillow (checked with 12.0) opens the largest frame by default and lists all of them in im.info["sizes"] . To pick a frame explicitly, assign it to im.size before loading: im = Image . open ( BytesIO ( data ) ) # an .ico file im . size = max ( im . info [ "sizes" ] , key = lambda s : s [ 0 ] * s [ 1 ] ) im . load ( ) im . convert ( "RGBA" ) . save ( "icon.png" ) 5. Ranking rule that worked Prefer icons that were actually downloaded and measured (raster). Then the largest measured edge. Ties: apple-touch-icon / manifest over icon over the default /favicon.ico ; SVG mask icons last (they are single-color silhouettes). 6. Be polite at scale Respect robots.txt . Cap downloads per site (8 icon candidates was enough). Put a hard deadline per site: some servers trickle bytes forever. Refuse private and loopback addresses if users can submit URLs. Don't want to build it? I packaged all of the above as an Apify Actor: paste domains, get every declared icon with measured sizes and the best one saved as PNG. You pay per website where an icon was found, with no start fee: https://apify.com/chivalrous_skyline_vtd/favicon-extractor The rules above are the useful part, though. They work in any language.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/coffee_cat_d04a723cc66298/getting-the-right-favicon-for-1000-domains-is-harder-than-it-looks-1985

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
