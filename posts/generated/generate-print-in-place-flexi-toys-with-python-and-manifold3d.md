---
title: "Generate print-in-place flexi toys with Python and manifold3d"
slug: "generate-print-in-place-flexi-toys-with-python-and-manifold3d"
author: "Black"
source: "devto_python"
published: "Sat, 24 Oct 2026 03:40:02 +0000"
description: "A flexi toy is a chain of segments where each one holds a captive ball joint. You can generate the whole chain from a short Python script with manifold3d , s..."
keywords: "flexi, segment, ball, you, socket, chain, segments, each"
generated: "2026-10-24T04:04:22.632959"
---

# Generate print-in-place flexi toys with Python and manifold3d

## Overview

A flexi toy is a chain of segments where each one holds a captive ball joint. You can generate the whole chain from a short Python script with manifold3d , so the same script makes a dragon, a snake or a centipede by changing a list of radii. The joint Each segment is an ellipsoid. The segment behind it carries a small ball on a neck. The front of the segment has a socket 0.5 mm larger than the ball and an opening for the neck that is 0.4 mm larger than the neck. The ball is wider than the opening, so it cannot escape, and the clearance lets it spin. import manifold3d as M3 Mf = M3 . Manifold def sph ( r , p , sc = ( 1 , 1 , 1 ), seg = 32 ): return Mf . sphere ( r , seg ). scale ( list ( sc )). translate ( list ( p )) def cyl_x ( r , a , b ): return Mf . cylinder ( b - a , r , r , 20 ). rotate ([ 0 , 90 , 0 ]). translate ([ a , 0 , 0 ]) def segment ( r , k = 1.25 ): body = sph ( r , ( 0 , 0 , 0 ), ( k , 1 , 0.9 ), 40 ) rb , rn = 0.45 * r , max ( 1.15 , 0.26 * r ) socket = sph ( rb + 0.5 , ( 0 , 0 , 0 ), ( 1 , 1 , 1 ), 40 ) + cyl_x ( rn + 0.4 , 0 , r * k + 3 ) return body - socket Place the chain Put each center at a distance of the two radii plus a 1 mm gap, then turn the heading a few degrees per segment to get an S-curve. Cut the sockets last, after you add legs or spikes, or those parts can fill the socket and fuse the joint. Check it before you print Call decompose() on the final model. The number of connected bodies must equal the number of segments. If it is lower, two parts fused. A pairwise (a ^ b).volume() over the segments tells you which pair touches. Results I used this to make a flexi dragon , a flexi cobra , a flexi axolotl and a flexi octopus . None are test printed yet, so tune the 0.4 mm clearance for your printer. If this helped, support me at patreon.com/123black .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blackspectre512/generate-print-in-place-flexi-toys-with-python-and-manifold3d-j6o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
