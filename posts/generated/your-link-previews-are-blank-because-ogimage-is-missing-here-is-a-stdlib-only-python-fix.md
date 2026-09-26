---
title: "Your link previews are blank because og:image is missing. Here is a stdlib-only Python fix"
slug: "your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix"
author: "rene"
source: "devto_python"
published: "Sat, 26 Sep 2026 15:07:11 +0000"
description: "When you paste a link to your product, docs page or side project into Slack, Discord, X or LinkedIn, the platform builds a preview card from your page's Open..."
keywords: "image, you, your, page, png, cover, meta, bytes"
generated: "2026-09-26T16:08:20.324672"
---

# Your link previews are blank because og:image is missing. Here is a stdlib-only Python fix

## Overview

When you paste a link to your product, docs page or side project into Slack, Discord, X or LinkedIn, the platform builds a preview card from your page's Open Graph tags. If og:image is missing or points at a generic platform default, the preview is a grey box or a stock logo. That hurts clicks, and you usually don't notice because you never see your own link the way other people do. This post covers three things: A 10-second check for whether your pages have this problem A PNG generator in pure Python (standard library only: no Pillow, no ImageMagick) that makes a 1280x720 cover image How to wire the image into your page 1. Check your og:image in 10 seconds curl -s https://your-site.example/page | grep -io '<meta[^>]*og:image[^>]*>' Three things can come back: Nothing. You have no og:image , so every share is a blank card. A generic URL , such as your host's or storefront's default logo. Every page you share looks the same. A page-specific image. You're fine. To see what the scrapers see, also check og:title and og:description : curl -s https://your-site.example/page | grep -io '<meta[^>]*og:[a-z]*[^>]*>' 2. Generate a PNG with only the standard library A PNG file is an 8-byte signature followed by chunks. Each chunk is length + type + data + CRC32 . You need three chunks: IHDR : width, height, bit depth and color type IDAT : the zlib-compressed pixel rows, each row prefixed with a filter byte IEND : an empty end marker struct and zlib are enough to write all three: import struct import zlib def _chunk ( kind : bytes , data : bytes ) -> bytes : body = kind + data return ( struct . pack ( ' >I ' , len ( data )) + body + struct . pack ( ' >I ' , zlib . crc32 ( body ) & 0xFFFFFFFF )) def write_png ( path : str , width : int , height : int , rows : list ) -> None : """ rows: list of `height` bytes objects, each width*3 bytes (RGB). """ raw = b '' . join ( b ' \x00 ' + r for r in rows ) # filter type 0 = None ihdr = struct . pack ( ' >IIBBBBB ' , width , height , 8 , 2 , 0 , 0 , 0 ) # 8-bit RGB png = ( b ' \x89 PNG \r\n\x1a\n ' + _chunk ( b ' IHDR ' , ihdr ) + _chunk ( b ' IDAT ' , zlib . compress ( raw , 9 )) + _chunk ( b ' IEND ' , b '' )) with open ( path , ' wb ' ) as f : f . write ( png ) Now draw something. A diagonal two-color gradient with a solid accent bar already looks far more deliberate than a grey box: def lerp ( a , b , t ): return int ( a + ( b - a ) * t ) def cover ( path , w = 1280 , h = 720 , c1 = ( 24 , 32 , 72 ), c2 = ( 96 , 48 , 160 ), accent = ( 255 , 196 , 0 )): rows = [] for y in range ( h ): row = bytearray () for x in range ( w ): if h - 40 <= y < h - 24 and 64 <= x < 424 : row += bytes ( accent ) # accent bar near the bottom continue t = ( x / ( w - 1 ) + y / ( h - 1 )) / 2 # diagonal blend 0..1 row += bytes (( lerp ( c1 [ 0 ], c2 [ 0 ], t ), lerp ( c1 [ 1 ], c2 [ 1 ], t ), lerp ( c1 [ 2 ], c2 [ 2 ], t ))) rows . append ( bytes ( row )) write_png ( path , w , h , rows ) cover ( ' cover.png ' ) Notes: 1280x720 (16:9) crops cleanly on most platforms' large-card previews. For square thumbnails, run the same code at 600x600. Pure Python is slow per pixel , but a 1280x720 image still renders in a few seconds, which is fine for a build step. If you batch hundreds, run it once in CI and cache the output. Pick colors per product or per page (for example, hash the slug into a hue). Then every link gets a distinct card with no design work. 3. Wire it into the page <meta property= "og:title" content= "Your page title" /> <meta property= "og:description" content= "One sentence on why to click." /> <meta property= "og:image" content= "https://your-site.example/img/cover.png" /> <meta property= "og:image:width" content= "1280" /> <meta property= "og:image:height" content= "720" /> <meta name= "twitter:card" content= "summary_large_image" /> Things that commonly go wrong: Use an absolute URL. Scrapers generally don't resolve relative paths in og:image . Previews are cached. After you fix the tag, platforms may keep showing the old card for a while. Most offer a debugger or re-scrape tool, or you can add a cache-busting query string to the image URL. Hosted storefronts (Gumroad, Notion pages and so on) usually set og:image from the cover image you upload. If you never uploaded one, you get the platform default. The fix there is to upload a cover, not to edit HTML. A ready-made version (free) I packaged this approach as a small free kit: a stdlib-only make_cards.py with a batch CSV mode that writes a 1280x720 cover and a 600x600 thumbnail for each row, plus a README and an example CSV. It's pay-what-you-want, and $0 is fine: 👉 https://renevibe76.gumroad.com/l/kflkqg If you'd rather not download anything, the snippets above are the whole core idea. Run the curl check on your own links today; odds are at least one of them is sharing a blank card.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/renev3408/your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix-o1e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
