---
title: "A Tiny Python Helper for Sizing Casters on Carts and Racks"
slug: "a-tiny-python-helper-for-sizing-casters-on-carts-and-racks"
author: "Donyaie Charkh"
source: "devto_python"
published: "Fri, 13 Nov 2026 05:33:08 +0000"
description: "If you build internal tools for a warehouse, a workshop or a hospital, sooner or later someone asks a deceptively simple question: "Which casters should we o..."
keywords: "casters, you, capacity, floors, factor, wheels, floor, rough"
generated: "2026-11-13T05:58:50.739699"
---

# A Tiny Python Helper for Sizing Casters on Carts and Racks

## Overview

If you build internal tools for a warehouse, a workshop or a hospital, sooner or later someone asks a deceptively simple question: "Which casters should we order for this cart?" Getting it wrong means wheels that flat-spot in a month, bearings that seize, or a trolley nobody wants to push. The core of the answer is arithmetic, so it fits nicely in a small, testable function. Here is a version I like to keep around. The rule of thumb The common shop-floor rule is: Required capacity per caster = (equipment weight + max load) / (number of casters - 1) Why minus one? Floors are never perfectly flat. On an uneven floor or over a threshold, one caster is often barely touching the ground, so the remaining casters carry the whole load. Dividing by n - 1 builds in that margin. Then you add a safety factor for shock loads, ramps and rough handling. The code from dataclasses import dataclass @dataclass class CasterSpec : capacity_per_caster_kg : float min_wheel_diameter_mm : int note : str def size_casters ( equipment_kg : float , load_kg : float , casters : int = 4 , rough_floor : bool = False , shock : bool = False ) -> CasterSpec : if casters < 3 : raise ValueError ( "Use at least 3 casters for a stable cart" ) total = equipment_kg + load_kg per_caster = total / ( casters - 1 ) factor = 1.0 if rough_floor : factor += 0.2 if shock : factor += 0.3 capacity = round ( per_caster * factor , 1 ) # Bigger wheels roll over cracks and cables more easily. if capacity > 500 or rough_floor : diameter = 150 elif capacity > 150 : diameter = 125 else : diameter = 100 note = "polyurethane on smooth floors" if not rough_floor else "rubber or soft tread for rough floors" return CasterSpec ( capacity , diameter , note ) print ( size_casters ( equipment_kg = 60 , load_kg = 400 , casters = 4 , rough_floor = True ) ) # CasterSpec(capacity_per_caster_kg=184.0, min_wheel_diameter_mm=150, note='rubber or soft tread for rough floors') Tests keep the rule honest def test_divides_by_n_minus_one ( ) : spec = size_casters ( 0 , 300 , casters = 4 ) assert spec . capacity_per_caster_kg == 100.0 def test_rough_floor_bumps_diameter ( ) : assert size_casters ( 0 , 90 , rough_floor = True ) . min_wheel_diameter_mm == 150 What the function does not decide for you Numbers are only half the job. You still have to pick: Wheel material. Polyurethane rolls easily and protects finished floors; rubber is quieter and grips better on rough or wet ground. Swivel vs fixed layout. Two fixed at the back and two swivel at the front tracks straight on long runs; four swivels suit tight rooms. Brakes or a jack stop for anything that must stay put while people work on it. Environment. Cold rooms, ovens and washdown areas each need their own materials. For those choices, real catalogue data beats guessing. As an example, Donyaie Charkh, an industrial caster manufacturer in Iran with branches in Rasht and Tehran, publishes a practical buyer's guide for industrial wheels that walks through load, floor and mounting choices in order, and their range of refrigerator and appliance casters at https://donyaiecharkh.com/category/refrigerator-casters is a good reference for what low-profile, cold-resistant wheels look like. You can find the full catalogue on the Donyaie Charkh website . Wrap-up Wrap the arithmetic in a function, add two or three tests, and your "which casters?" conversations get shorter and more consistent. Then let the floor, the environment and a good catalogue decide the rest.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/donyaiecharkh/a-tiny-python-helper-for-sizing-casters-on-carts-and-racks-4np0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
