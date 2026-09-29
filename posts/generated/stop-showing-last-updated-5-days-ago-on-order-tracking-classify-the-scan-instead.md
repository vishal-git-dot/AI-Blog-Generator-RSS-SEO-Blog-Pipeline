---
title: "Stop showing "last updated 5 days ago" on order tracking - classify the scan instead"
slug: "stop-showing-last-updated-5-days-ago-on-order-tracking-classify-the-scan-instead"
author: "24hTrack"
source: "devto_webdev"
published: "Tue, 29 Sep 2026 04:45:30 +0000"
description: "If you build order-status pages, there is a good chance you render something like Last updated 5 days ago and let the customer decide what it means. They dec..."
keywords: "you, return, last, days, carrier, not, handed, number"
generated: "2026-09-29T05:12:37.074133"
---

# Stop showing "last updated 5 days ago" on order tracking - classify the scan instead

## Overview

If you build order-status pages, there is a good chance you render something like Last updated 5 days ago and let the customer decide what it means. They decide it means the parcel is lost, and they open a ticket. Elapsed time is close to useless as a signal on a tracking timeline, because a tracking feed is not a location stream. It is an append-only log of handling events. A row appears only when a human or a machine physically scans the barcode. Between scans the parcel is moving and nothing is written. So "no event for five days" is not an error state - on some legs it is the expected state. The signal you actually have The useful signal is the type and place of the most recent event, not its age. Roughly five classes cover almost everything you will see: Class Typical wording Is silence expected? ORIGIN_DEPARTED departed, left facility, handed to airline Yes - longest gaps in the journey IMPORT_PENDING arrived at destination country, import scan, customs clearance Yes, unless duties or documents were requested DOMESTIC_HUB arrived at a depot or sorting centre in the destination country No - short leg remaining HANDOVER handed over to local partner, transferred to another carrier Yes, permanently - this carrier stops publishing NO_SCAN nothing at all Depends how long since the label was created Once you have that, the copy writes itself, and it is different copy per class rather than one "still on its way" for everything. // deliberately boring: substring rules over a normalised string const classify = ( ev , destCountry ) => { const s = ( ev . description || '' ). toLowerCase () if ( /handed over|transferred to|local partner/ . test ( s )) return ' HANDOVER ' if ( /customs|import|arrived at destination country/ . test ( s )) return ' IMPORT_PENDING ' if ( /departed|left .*facility|handed to airline/ . test ( s ) && ev . country !== destCountry ) return ' ORIGIN_DEPARTED ' if ( ev . country === destCountry ) return ' DOMESTIC_HUB ' return ' IN_TRANSIT ' } const shouldEscalate = ( last , now , destCountry ) => { const cls = classify ( last , destCountry ) const days = ( now - new Date ( last . at )) / 864 e5 if ( cls === ' IMPORT_PENDING ' ) return last . dutiesRequested === true if ( cls === ' DOMESTIC_HUB ' ) return days > 7 // short leg: a week is odd if ( cls === ' HANDOVER ' ) return false // track the second carrier return days > 21 // cross-border linehaul } Two things worth building in beyond the table. A handover is a terminal state for that carrier, not a pause. Once a parcel is handed to a last-mile partner, the original carrier will never add another row. If your UI polls only the primary carrier, it will show "no update" forever while the parcel is being delivered under a different number. Model handover as its own visible state and, where you can, follow the second leg. Distinguish "no scan yet" from "scans stopped". A number that has never had a single event is usually a label that was printed but not handed over - or a customer pasting an order number instead of a tracking number. That is a different email from a parcel that moved and then went quiet, and conflating them is where a lot of support looping comes from. Why this cuts tickets The question behind almost every where-is-my-order contact is not "where is it" but "is something wrong, and do I need to do something". A status line that answers that directly - waiting is correct here, or this one needs you to pay duties, or this is worth chasing - resolves the contact before it is made. Last updated 5 days ago answers none of it. If you want to see what a real timeline looks like across both legs, 24hTrack is free and needs no sign-up: paste a number and the carrier is detected automatically, across 3,200+ carriers. There is also a REST API and an MCP server if you would rather pull events into your own UI, and an open guide repo with status wordings and number formats: https://github.com/doanhnd9989/package-tracking-guide Written by the team at 24hTrack, with AI assistance.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/support24htrack/stop-showing-last-updated-5-days-ago-on-order-tracking-classify-the-scan-instead-m70

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
