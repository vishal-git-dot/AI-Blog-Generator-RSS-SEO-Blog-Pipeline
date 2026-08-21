---
title: "Recover a globe image's projection centre from its own pixels, to prove it points where it claims"
slug: "recover-a-globe-images-projection-centre-from-its-own-pixels-to-prove-it-points-where-it-claims"
author: "Kynth Studios"
source: "devto_python"
published: "Fri, 21 Aug 2026 01:07:37 +0000"
description: "A breaking earthquake story leads with a globe and a red dot. If that dot sits over the wrong island, the reader is told the wrong thing, and nothing about t..."
keywords: "math, globe, image, wrong, centre, where, rho, agreement"
generated: "2026-08-21T01:40:10.053677"
---

# Recover a globe image's projection centre from its own pixels, to prove it points where it claims

## Overview

A breaking earthquake story leads with a globe and a red dot. If that dot sits over the wrong island, the reader is told the wrong thing, and nothing about the picture looks off. The dot is drawn in the middle of the disc, always. The renderer centres the view on the event, so the marker lands at the centre by construction, whatever coordinates went in. A globe built from the wrong point comes out as a well formed picture of somewhere else: right colours, right marker, right size, sitting under a headline about another continent. Checking the file catches none of that. It is a valid image, of the right dimensions, inside its byte budget. The only part of the picture that knows where it points is the coastline behind the dot. Reading the coastline back The check works backwards from the published image. Sample a grid of points inside the disc and classify each by colour: ocean navy, land grey, or the tinted country red. Then guess a centre, and for each sample run the projection in reverse to get the latitude and longitude that pixel would be showing if the guess were right. Ask a map of where land is whether that spot is land. Count how often the picture and the map agree. def unproject ( dx , dy , lat0 , lon0 ): """ Orthographic inverse: disc-relative (dx, dy) in [-1,1] → (lat, lon). None off the sphere. """ rho = math . hypot ( dx , dy ) if rho > 1 : return None c = math . asin ( rho ) if rho else 0.0 p0 = math . radians ( lat0 ) sin_c , cos_c = math . sin ( c ), math . cos ( c ) lat = math . asin ( cos_c * math . sin ( p0 ) + ( dy * sin_c * math . cos ( p0 ) / rho if rho else 0 )) lon = math . radians ( lon0 ) + math . atan2 ( dx * sin_c , rho * cos_c * math . cos ( p0 ) - dy * sin_c * math . sin ( p0 ) ) return ( math . degrees ( lat ), ( math . degrees ( lon ) + 540 ) % 360 - 180 ) def agreement ( samples , lat0 , lon0 ): hit = 0 for dx , dy , seen_land in samples : ll = unproject ( dx , - dy , lat0 , lon0 ) # image y grows downward, the projection's grows up if ll is None : continue if is_land ( ll [ 0 ], ll [ 1 ]) == seen_land : hit += 1 return hit / len ( samples ) if samples else 0.0 Run that over a coarse grid of candidate centres, then refine three times, and the centre scoring highest is the one the image was actually drawn on. 895 candidates, under three tenths of a second per image, no network and no key. The entire land reference is an 11,174 byte black and white PNG at quarter degree resolution, sitting next to the script. Then compare the recovered centre to the coordinates stored beside the article, in kilometres. The number is never zero, and that is the point Eight published globe heroes, each checked against its own stored epicentre: 27.9 km for Peru, 83.5 km for the widest, in western China, the rest between 39.8 and 50.1, at 97.1% to 99.2% agreement. None of those gaps are errors in the picture. A quarter of a degree is 27.8 km at the equator, so the land map cannot separate two centres 20 km apart. The pass mark is 100 km because that is the resolution of the evidence. The failure worth catching is hundreds to thousands of kilometres wide, which leaves an order of magnitude on either side of the line. Agreement and distance answer different questions Feed the Vanuatu globe the coordinates of the Peru earthquake and agreement holds at 98.5%, because it is still a real, well drawn globe of somewhere. The distance reads 12,091.7 km. Agreement says the image is a genuine globe centred where it appears to be centred. Only the distance says whether that is where the story happened. Read the same globe off the social card, where the headline sits over the disc and the frame crops it, and it recovers a centre in the empty South Pacific at 94.3% agreement, 5,063.5 km out. A cropped disc yields a wrong bounding box, which yields a wrong radius, which yields a confident wrong answer. So the gate reads the uncropped hero. Image fed to the checker Recovered centre Land/ocean agreement Distance to stored point Vanuatu hero, against its own epicentre -20.25 / 169.625 98.5% 50.1 km, pass Same globe as a social card, type over the disc, same epicentre -25.0 / -141.5 94.3% 5,063.5 km, fail Vanuatu hero, against the Peru epicentre -20.25 / 169.625 98.5% 12,091.7 km, fail The site's 1200x630 share image, no globe in it none not applicable not applicable, unreadable An image the method cannot read fails, rather than being skipped. "I could not tell" is where a silently wrong picture hides, so unreadable is reported as a problem alongside pointing at the wrong continent. That share image comes back with 17 classifiable pixels and the sentence "not a locator globe". This is how we built The Front Wire: https://frontwire.kynth.studio/?utm_source=kynth-devto&utm_medium=social&utm_campaign=kynth One shipped product, taken apart, once a month. What it does, what it cost to build, what the pipeline behind it looks like, and what the numbers did — read off the repository and the live site, not written from memory. Join the list .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kynthstudios/recover-a-globe-images-projection-centre-from-its-own-pixels-to-prove-it-points-where-it-claims-42pl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
