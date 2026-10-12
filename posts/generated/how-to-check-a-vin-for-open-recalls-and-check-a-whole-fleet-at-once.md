---
title: "How to check a VIN for open recalls (and check a whole fleet at once)"
slug: "how-to-check-a-vin-for-open-recalls-and-check-a-whole-fleet-at-once"
author: "CyberMax"
source: "devto_python"
published: "Mon, 12 Oct 2026 14:50:22 +0000"
description: "A safety recall repair is free at any franchised dealer, but only if someone notices the recall. NHTSA received 958 recall campaigns in the last 12 months (2..."
keywords: "vin, recall, nhtsa, recalls, make, recallroll, api, check"
generated: "2026-10-12T14:59:14.187255"
---

# How to check a VIN for open recalls (and check a whole fleet at once)

## Overview

A safety recall repair is free at any franchised dealer, but only if someone notices the recall. NHTSA received 958 recall campaigns in the last 12 months (25 September 2025 to 18 September 2026), covering 43,450,237 vehicles and pieces of equipment . 25 of them told owners not to drive the vehicle until it is fixed, and 24 told owners to park outside , away from buildings, because of fire risk. Check one VIN The 17-character VIN is on the driver-side dashboard (visible through the windscreen), the driver's door pillar and the registration and insurance cards. Enter it at nhtsa.gov/recalls . NHTSA shows the recalls that are still open for that exact vehicle , based on what the manufacturer reports. If a recall is open, call any dealer for the brand. The repair is free, even for a used car you bought second-hand. Treat Do Not Drive and Park Outside notices as urgent: those are the ones where the risk is a crash or a fire. What a VIN tells you A VIN decodes to year, make, model, trim, engine and assembly plant. Take the widely used sample VIN 1HGCM82633A004352 : it decodes to a 2003 Honda Accord EX-V6 coupe , 3.0 L six-cylinder, built in Marysville, Ohio. NHTSA lists 24 recall campaigns for the 2003 Accord: 10 for exterior lighting, 9 for front airbag inflators (driver and passenger side) and 5 others. Try it: check VIN 1HGCM82633A004352 (free, no key): curl 'https://recallroll-api.cybermaxtools.com/api/check?vin=1HGCM82633A004352' A model-year lookup is useful even without a VIN: the 2021 Ford F-150 has 29 recall campaigns on file, including one Do Not Drive notice (21V407000, a steering gear that may be damaged internally, fixed by replacing the gear free of charge). A make/model/year recall list shows every campaign that could apply. Whether one specific vehicle is included, or already repaired, is confirmed by VIN at nhtsa.gov or by a dealer. Which makes recall the most Recall campaigns per make, last 12 months Ford 111 Lincoln 32 Toyota 30 Chevrolet 27 Forest River 23 Jeep 23 Altec 22 Hyundai 22 BMW 22 Honda 21 NHTSA campaigns received 25 Sep 2025 to 18 Sep 2026 that name the make. One campaign can cover several makes. Ford leads by a wide margin in the last 12 months, but raw counts also reflect how many models and vehicles each maker sells. See the per-make pages for models and components, for example Ford, Toyota, Honda and Tesla, or every make. Checking a fleet, a lot or a customer list Typing VINs into a web form works for one car. Dealers checking trade-ins, rental and fleet managers, and insurers need it in a spreadsheet or their own software. Recallroll decodes up to 10 VINs per call with NHTSA vPIC and lists every NHTSA recall for each vehicle, Do Not Drive and Park Outside first, with the component, summary, remedy and a link to NHTSA's page for that VIN. curl "https://recallroll-api.cybermaxtools.com/api/check?vin=1HGCM82633A004352" curl "https://recallroll-api.cybermaxtools.com/api/recalls?make=Ford&model=F-150&year=2021" The same key works as a remote MCP server, so an AI assistant can answer "does this car have open recalls?" with live NHTSA data. Recallroll : VIN in, safety recalls out: decode up to 10 VINs per call and list every NHTSA recall, Do Not Drive first. Free: 50 calls a day, no key and no card. Paid keys from $19/month (2,000 calls), or $5 pay as you go (400, no expiry). See Recallroll plans and pricing Published prices on 27 September 2026: auto.dev charges $0.01 per recall call on its $299/month Growth plan; CarsXE's API starts at $40.83/month billed yearly. Recallroll is free for 50 calls a day (up to 10 VINs each), then $19/month for 2,000 calls, or $5 pay-as-you-go. Prefer a weekly report? The US Vehicle Recall Brief arrives every Monday. Sources: NHTSA recalls and the NHTSA vPIC VIN decoder (public domain). Published automatically by CyberMax. Every number above comes from the linked public data; nothing is estimated.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cybermax/how-to-check-a-vin-for-open-recalls-and-check-a-whole-fleet-at-once-23dh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
