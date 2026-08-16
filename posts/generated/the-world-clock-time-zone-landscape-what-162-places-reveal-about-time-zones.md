---
title: "The World Clock Time-Zone Landscape: what 162 places reveal about time zones"
slug: "the-world-clock-time-zone-landscape-what-162-places-reveal-about-time-zones"
author: "Lucian (LKB)"
source: "devto_webdev"
published: "Sun, 16 Aug 2026 18:21:25 +0000"
description: "Time zones look like a tidy grid of whole hours. They aren't. I read the standard UTC offset of all 162 cities, countries and regions on our World Clock stra..."
keywords: "utc, offset, hour, clocks, places, one, world, clock"
generated: "2026-08-16T18:35:30.115995"
---

# The World Clock Time-Zone Landscape: what 162 places reveal about time zones

## Overview

Time zones look like a tidy grid of whole hours. They aren't. I read the standard UTC offset of all 162 cities, countries and regions on our World Clock straight from the IANA database (via Intl ) — and the real shape is lumpy, with quarter-hour outliers and a near-even split over whether clocks move at all. The quirk, in one line: Kathmandu keeps its clocks 5 hours 45 minutes ahead of UTC — the only :45 offset on the board, and one of 11 places out of 162 that don't sit on a whole hour. Nearly half the rest never move their clocks at all. The clocks that don't sit on the hour Most of the world rounds to a whole hour from UTC. A handful don't: Offset Places UTC+3:30 Tehran (Iran) UTC+4:30 Kabul (Afghanistan) UTC+5:30 India — New Delhi, Mumbai, Kolkata, Bengaluru, Hyderabad UTC+5:45 Kathmandu (Nepal) UTC+9:30 Adelaide, Darwin (Australia) Half-hour and quarter-hour offsets are a reminder that a time zone is a political decision, not an astronomical one — which is exactly why date code should read the IANA database rather than dividing longitude by 15. Nearly half never change their clocks Daylight saving feels universal if you live in North America or Europe, but it isn't. Of the 162 places tracked, 87 (54%) shift their clocks and 75 (46%) never do . The whole of East Asia, the Gulf, most of Africa, India and much of South America keep one fixed offset year-round — Tokyo, Singapore, Dubai, Nairobi and New Delhi never spring forward. Where the clocks crowd together Offsets aren't evenly populated. Four of them carry nearly half the board: Offset Places Who's there UTC−5 25 US Eastern — New York, Toronto, Miami, Boston UTC+1 21 Central Europe — Paris, Berlin, Rome, Madrid UTC−6 14 US Central — Chicago, Dallas, Mexico City UTC+2 12 Eastern Europe & Africa — Athens, Cairo, Johannesburg The full set spans 22 hours , from Honolulu at UTC−10 to New Zealand and Fiji at UTC+12. Reproduce it Every number here is printed by one dependency-free Node script that reads each place's standard offset from the IANA database via Intl for January and July 2025 (a place "observes DST" when the two differ): → Run it yourself (public gist) All figures are scoped to the 162 places the clock tracks, not every zone on Earth (globally there are other quarter-hour oddities, like the Chatham Islands at +12:45). Originally published at lkforge.com , where the offset distribution is an interactive chart. Built alongside the free LK Forge World Clock .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lucian_lkb_1f009d/the-world-clock-time-zone-landscape-what-162-places-reveal-about-time-zones-1a4m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
