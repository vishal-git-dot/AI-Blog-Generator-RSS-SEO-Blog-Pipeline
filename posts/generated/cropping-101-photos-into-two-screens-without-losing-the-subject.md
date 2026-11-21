---
title: "Cropping 101 photos into two screens without losing the subject"
slug: "cropping-101-photos-into-two-screens-without-losing-the-subject"
author: "尚毅段"
source: "devto_python"
published: "Sat, 21 Nov 2026 06:06:53 +0000"
description: "Cropping 101 photos into two screens without losing the subject The iPhone Duo has two displays that don't share an aspect ratio. The inner screen is landsca..."
keywords: "screen, two, cover, image, centre, crop, each, edge"
generated: "2026-11-21T06:33:10.794514"
---

# Cropping 101 photos into two screens without losing the subject

## Overview

Cropping 101 photos into two screens without losing the subject The iPhone Duo has two displays that don't share an aspect ratio. The inner screen is landscape, 2670x1878. The cover screen is portrait, 1398x2034. A wallpaper that looks right on one is usually wrong on the other, so every image on Best iPhone Duo ships as two separate crops plus a 4K version. Doing that with Image.thumbnail() produced 101 wallpapers I didn't want to look at. Centre cropping a landscape photo to 1398x2034 keeps the middle strip and throws away the edges, which on a mountain lake means the horizon sits dead centre and the far ridge disappears. So the build does the crop decision itself. What the crop has to decide For each source image, three targets. The inner screen gets 2670x1878, the 4K download gets 3840x2700, and the cover screen gets 1398x2034. Two are landscape, one is portrait, all from the same photograph. The rule I wanted: keep the part of the image with the most detail, but don't drift so far that the frame looks accidental. Edge density is a decent proxy for "the interesting part" on landscape photos — a treeline, a skyline, a ridge. Edge energy as a crop guide Downscale to 320px wide, convert to greyscale, run an edge filter, then sum edge pixels into a 1D profile along the axis being cropped: def energy_profile ( im , axis ) : g = im . convert ( "L" ) . resize ( ( 320 , max ( 1 , int ( 320 * im . height / im . width ) ) ) , Image . LANCZOS ) e = g . filter ( ImageFilter . FIND_EDGES ) w , h = e . size px = list ( e . getdata ( ) ) if axis == 0 : return [ sum ( px [ y * w + x ] for y in range ( 0 , h , 2 ) ) for x in range ( w ) ] return [ sum ( px [ y * w + x ] for x in range ( 0 , w , 2 ) ) for y in range ( h ) ] That gives you a column profile for horizontal crops and a row profile for vertical ones. Then slide a window the width of the crop across the profile and take the one with the most energy: def pick_offset ( prof , span , total , prefer = 0.5 ) : n = len ( prof ) if span >= n : return 0 win = min ( int ( n * span / total ) or 1 , n - 1 ) best , best_i = - 1 , 0 step = max ( 1 , win // 12 ) for i in range ( 0 , n - win + 1 , step ) : s = sum ( prof [ i : i + win ] ) centre = ( i + win / 2 ) / n s *= ( 1 - 0.25 * abs ( centre - prefer ) * 2 ) if s > best : best , best_i = s , i return int ( best_i / n * total ) The prefer term is the part that matters. Pure max-energy cropping chases a bright sky or a busy foreground and produces frames where the subject is jammed against one edge. Multiplying the score by a penalty on distance from a target centre pulls it back. For the inner screen that target is 0.5, dead centre. For the cover screen it's 0.42, slightly toward the top. That number came from trying a handful of crops and keeping what looked right; there is no data behind it. Two constants, and the crops stopped looking accidental. Output sizes Each photo becomes five files: File Size Used for -open.jpg 2670x1878 inner screen download -cover.jpg 1398x2034 cover screen download -4k.jpg 3840x2700 4K download -open-thumb.jpg 960x675 grid preview -cover-thumb.jpg 420x611 cover preview JPEG throughout, quality 80 for the inner screen, 82 for the cover, 72 for 4K, progressive and optimised. 101 photographs come to 277MB total, which only works because each file is served immutable for a year and the grid only ever loads the thumbnails. The accent colour for each card comes from the same resized image — a 24x24 average, no extra pass over the full-size file. What this doesn't do It's not a face-aware crop. On a photo where the subject is small and off-centre, edge energy can prefer a detailed background over the person. The offsets also aren't stored per image: every wallpaper uses the same two prefer values, so a crop that comes out wrong has to be fixed by replacing the source photo, not by nudging a field in the build. The photos themselves are Creative Commons from Wikimedia Commons, mostly CC BY 4.0, credited to the photographer on each wallpaper page. The gallery is at bestiphoneduo.com if you want to see how the two crops sit next to each other.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/succday/cropping-101-photos-into-two-screens-without-losing-the-subject-30b7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
