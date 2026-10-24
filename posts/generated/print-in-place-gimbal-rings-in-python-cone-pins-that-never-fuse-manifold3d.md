---
title: "Print-in-place gimbal rings in Python: cone pins that never fuse (manifold3d)"
slug: "print-in-place-gimbal-rings-in-python-cone-pins-that-never-fuse-manifold3d"
author: "Black"
source: "devto_python"
published: "Sat, 24 Oct 2026 03:33:04 +0000"
description: "Nested gimbal rings are a nice print-in-place test: every ring has to turn freely, and nothing may fuse. This post builds four rings and a globe in Python wi..."
keywords: "cone, ring, socket, pin, rings, pair, parent, print"
generated: "2026-10-24T04:04:22.633175"
---

# Print-in-place gimbal rings in Python: cone pins that never fuse (manifold3d)

## Overview

Nested gimbal rings are a nice print-in-place test: every ring has to turn freely, and nothing may fuse. This post builds four rings and a globe in Python with manifold3d , and shows the three mistakes that fused my first attempts. 1. A ring is a revolved rectangle from manifold3d import Manifold as Mf , CrossSection as CS w , t = 4.4 , 4.0 # radial width, thickness def ring ( R ): return Mf . revolve ( CS . square ([ w , t ], True ). translate ([ R , 0 ]), 96 ) revolve spins the profile around Z, so the ring lies in the XY plane. Rotate it with .rotate([90,0,0]) and so on to get the other planes. Each pair of neighbours shares one axis: Z, then Y, then X, then Z for the globe. 2. Cone pin and cone socket The child ring grows a cone pin on its outer surface. The parent gets a matching cone socket, offset by the clearance CL = 0.45 . A cone self-centres, and it prints without supports when the tip points sideways or up. def cone ( r1 , r2 , h , pos , d ): # d = unit direction return Mf . cylinder ( h , r1 , r2 , 32 ). transform ( rotm ( d )). translate ( list ( pos )) g = inner_parent - outer_child # gap between the rings L = g + 1.5 # pin reaches 1.5 mm into the parent wall pin = cone ( 2.7 , 1.1 , L , d * outer_child , d ) slope = ( 1.1 - 2.7 ) / L sock = cone ( 2.7 + slope * ( g - 1.2 ) + CL , 2.7 + slope * ( L + 0.7 ) + CL , L + 0.7 - ( g - 1.2 ), d * ( outer_child + g - 1.2 ), d ) parent = parent - sock 3. The three mistakes The socket must start before the wall. A ring wall is curved. A socket that starts exactly at the nominal inner radius leaves a thin skin at the edges of the cone, and the pin fuses to it. Start the socket 1.2 mm earlier. Check every pair with a ^ b . After the final union, decompose() tells you the count of parts. When it is too low, intersect each pair and print the volume. A volume above 0.01 names the fused pair. Keep the stand away from sockets. My pedestal column reached into the lowest socket and filled it. Stop the column at the outer surface of the ring. I have not test printed this yet. The meshes are separate manifold solids with 0.45 mm radial clearance.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blackspectre512/print-in-place-gimbal-rings-in-python-cone-pins-that-never-fuse-manifold3d-4ob1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
