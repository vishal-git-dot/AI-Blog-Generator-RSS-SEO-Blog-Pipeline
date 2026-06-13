---
title: "Orbital mechanics with Python, from circular orbits to Hohmann transfers"
slug: "orbital-mechanics-with-python-from-circular-orbits-to-hohmann-transfers"
author: "I Want To Learn Programming"
source: "devto_python"
published: "Sat, 13 Jun 2026 14:00:07 +0000"
description: "Orbital mechanics sounds like it needs a graduate degree, but the core results are surprisingly reachable with high-school physics and a few lines of Python...."
keywords: "math, orbital, transfer, orbit, sqrt, you, circular, orbits"
generated: "2026-06-13T14:12:06.659558"
---

# Orbital mechanics with Python, from circular orbits to Hohmann transfers

## Overview

Orbital mechanics sounds like it needs a graduate degree, but the core results are surprisingly reachable with high-school physics and a few lines of Python. If you can compute an orbital velocity and a transfer, you understand the foundation that mission planning is built on. A circular orbit For a circular orbit, gravity provides exactly the centripetal force, which gives a clean formula for orbital speed: import math MU = 3.986e14 # Earth's gravitational parameter, m^3/s^2 def circular_velocity ( r ): return math . sqrt ( MU / r ) # m/s at orbital radius r (meters) A satellite in low Earth orbit (about 200 km up, so r is roughly 6,571 km) moves at close to 7.8 km/s. That single formula already explains why orbital speeds are so high: lower orbits need to move faster to stay up. Orbital period How long one lap takes follows from Kepler's third law: def period ( r ): return 2 * math . pi * math . sqrt ( r ** 3 / MU ) # seconds Plug in geostationary radius (about 42,164 km) and you get roughly 24 hours, which is exactly why those satellites appear to hang still over one spot on Earth. The formula predicts the orbit that makes GPS and communications satellites work. The Hohmann transfer The classic, fuel-efficient way to move between two circular orbits is the Hohmann transfer: one burn to enter an elliptical path that just touches both orbits, and a second burn to circularize at the new altitude. The two velocity changes come from the vis-viva equation: def hohmann ( r1 , r2 ): v1 = math . sqrt ( MU / r1 ) v2 = math . sqrt ( MU / r2 ) a = ( r1 + r2 ) / 2 # transfer ellipse semi-major axis vp = math . sqrt ( MU * ( 2 / r1 - 1 / a )) # speed at perigee of transfer va = math . sqrt ( MU * ( 2 / r2 - 1 / a )) # speed at apogee of transfer return abs ( vp - v1 ) + abs ( v2 - va ) # total delta-v That total delta-v is the fuel budget for the maneuver, the number a mission planner actually cares about. With these few functions you can already reason about real transfers, like raising a satellite from a parking orbit to its operational altitude. Build the whole thing This is the kind of problem where coding it is understanding it: change a radius and watch the velocity and delta-v respond. The aerospace with Python track builds orbital mechanics and much more from scratch, graded in your browser. The first project is free. The math of getting to orbit is closer than you think. Start computing it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/iwtlp/orbital-mechanics-with-python-from-circular-orbits-to-hohmann-transfers-415

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
