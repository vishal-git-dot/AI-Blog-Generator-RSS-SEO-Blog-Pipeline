---
title: "Generate 3D-printable ornaments in Python: torus knots and golden-angle petals"
slug: "generate-3d-printable-ornaments-in-python-torus-knots-and-golden-angle-petals"
author: "Black"
source: "devto_python"
published: "Fri, 23 Oct 2026 21:02:44 +0000"
description: "Most 3D-print ornaments are the same snowflake and star. Code can make shapes nobody modeled by hand. Here are two short recipes with manifold3d (Python, pip..."
keywords: "math, manifold, knot, petals, translate, sphere, each, rosette"
generated: "2026-10-23T21:14:15.040828"
---

# Generate 3D-printable ornaments in Python: torus knots and golden-angle petals

## Overview

Most 3D-print ornaments are the same snowflake and star. Code can make shapes nobody modeled by hand. Here are two short recipes with manifold3d (Python, pip install manifold3d numpy ). Both output watertight meshes you can slice directly. 1. A torus knot from capsule segments A (p,q) torus knot winds p times around a ring while oscillating q times across the tube. Sample the curve, put a sphere at each point, and union the convex hull of each neighbor pair. That gives a smooth tube with no sweep tool. import math from manifold3d import Manifold import manifold3d as M3 R , r , p , q , t , N = 17 , 5.5 , 3 , 8 , 2.1 , 480 pts = [] for i in range ( N + 1 ): u = 2 * math . pi * i / N rr = R + r * math . cos ( q * u ) pts . append (( rr * math . cos ( p * u ), rr * math . sin ( p * u ), r * math . sin ( q * u ))) sp = [ Manifold . sphere ( t , 14 ). translate ( list ( c )) for c in pts ] segs = [ Manifold . batch_hull ([ sp [ i ], sp [ i + 1 ]]) for i in range ( N )] knot = M3 . Manifold . batch_boolean ( segs , M3 . OpType . Add ) knot = knot . translate ([ 0 , 0 , r + t ]) # lowest point sits on z=0 batch_boolean matters: unioning 480 pieces one by one is far slower. Use a tube radius of at least 1.5x your nozzle width and print it flat with tree supports. 2. Succulent petals from the golden angle Real succulents place each new leaf 137.508 degrees after the last. Scale a sphere into a petal, tilt it, push it outward, and rotate it by i * 137.508 . Small petals start steep in the center and flatten toward the rim. G = math . radians ( 137.508 ) petals = [] for i in range ( 62 ): s = i / 61 L , w , th = 5 + 14 * s , 2.4 + 3.4 * s , 0.9 + 0.5 * s tilt = 78 - 62 * s pt = Manifold . sphere ( 1 , 24 ). scale ([ L , w , th ]) pt = pt . translate ([ L * 0.92 , 0 , 0 ]). rotate ([ 0 , - tilt , 0 ]) pt = pt . translate ([ 1 + 9 * s , 0 , 1.5 + ( 1 - s ) * 7 ]). rotate ([ 0 , 0 , math . degrees ( i * G )]) petals . append ( pt ) rosette = M3 . Manifold . batch_boolean ( petals , M3 . OpType . Add ) rosette = rosette ^ Manifold . cube ([ 200 , 200 , 200 ], True ). translate ([ 0 , 0 , 100 ]) # cut below z=0 The ^ intersection with a big cube keeps only z >= 0 so the model has a flat bed face. Tips that saved me prints Check the render before slicing. A top-down view catches gaps in a knot that a perspective view hides. Hull-of-spheres chains look blobby for organic shapes. For those use Manifold.level_set with a signed distance function. Keep walls at least 2 nozzle widths and bridges short. I turned these into printable ornaments (Celtic knot, succulent rosette, spirograph mandala, Moebius ladder) on Cults3D for $1.27 each if you would rather skip the code. More designs and files on Patreon .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blackspectre512/generate-3d-printable-ornaments-in-python-torus-knots-and-golden-angle-petals-28g5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
