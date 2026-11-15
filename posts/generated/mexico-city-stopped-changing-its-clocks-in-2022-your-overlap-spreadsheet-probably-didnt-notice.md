---
title: "Mexico City stopped changing its clocks in 2022. Your overlap spreadsheet probably didn't notice"
slug: "mexico-city-stopped-changing-its-clocks-in-2022-your-overlap-spreadsheet-probably-didnt-notice"
author: "Bromena"
source: "devto_python"
published: "Sun, 15 Nov 2026 13:21:32 +0000"
description: "If you work with engineers in Mexico City and you planned your meetings before late 2022, your mental model of the overlap is probably wrong for half the yea..."
keywords: "city, time, mexico, america, date, chicago, shared, hours"
generated: "2026-11-15T13:44:44.197556"
---

# Mexico City stopped changing its clocks in 2022. Your overlap spreadsheet probably didn't notice

## Overview

If you work with engineers in Mexico City and you planned your meetings before late 2022, your mental model of the overlap is probably wrong for half the year. Mexico City dropped daylight saving time. It has been on Zona Centro, UTC-6, all year since October 30, 2022, under the Ley de los Husos Horarios published in the DOF. US cities still change their clocks twice a year. So the shared hours now move only when the US moves. Computing it instead of remembering it Python's zoneinfo reads the IANA time zone database, which already has the 2022 change. A 9-to-6 workday on both sides: from datetime import datetime , date , time , timedelta from zoneinfo import ZoneInfo def workday ( d , tz , start = 9 , end = 18 ) : z = ZoneInfo ( tz ) return datetime . combine ( d , time ( start ) , z ) , datetime . combine ( d , time ( end ) , z ) def overlap_hours ( d , tz ) : a0 , a1 = workday ( d , "America/Mexico_City" ) b0 , b1 = workday ( d , tz ) return max ( timedelta ( 0 ) , min ( a1 , b1 ) - max ( a0 , b0 ) ) . total_seconds ( ) / 3600 for city , tz in [ ( "New York" , "America/New_York" ) , ( "Chicago" , "America/Chicago" ) , ( "Denver" , "America/Denver" ) , ( "Los Angeles" , "America/Los_Angeles" ) ] : print ( city , overlap_hours ( date ( 2027 , 1 , 15 ) , tz ) , overlap_hours ( date ( 2027 , 7 , 15 ) , tz ) ) US city US winter (standard) US summer (daylight) New York, Toronto 8 h 7 h Chicago 9 h 8 h Denver 8 h 9 h Los Angeles, San Francisco 7 h 8 h The part that surprises people Chicago loses an hour in summer. Before 2022 Mexico City and Chicago moved together and always matched. Now they match only in US winter. Denver and the West Coast gain an hour in summer. When the US springs forward, Mountain and Pacific time move closer to UTC-6. New York drops to 7 hours from mid-March. In 2022, a July date gave New York 8 shared hours with Mexico City. In July 2027 it's 7. In 2027 the switch dates for US teams are March 14 and November 7. Those are the two days a recurring "10 AM Mexico" standup lands at a different US time. Takeaways Store meeting times with an IANA zone ( America/Mexico_City ), never a fixed offset or "CST". Recompute overlap per date instead of keeping one number in a doc. If a team spans several US zones, the best shared window changes in March and November. Revisit it then. We publish the per-city table and how we plan shared hours for nearshore teams at https://bromena.com/ — Bromena team

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bromena/mexico-city-stopped-changing-its-clocks-in-2022-your-overlap-spreadsheet-probably-didnt-notice-3nec

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
