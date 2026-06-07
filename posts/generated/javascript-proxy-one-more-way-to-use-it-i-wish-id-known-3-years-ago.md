---
title: "JavaScript Proxy: One more way to use it I wish I’d known 3 years ago"
slug: "javascript-proxy-one-more-way-to-use-it-i-wish-id-known-3-years-ago"
author: "Maks"
source: "devto_webdev"
published: "Sun, 07 Jun 2026 19:29:52 +0000"
description: "In our everyday work, we do a lot of data shuffling. We work with heavily loaded data grids. We have built our own RevoGrid for this matter hence market didn..."
keywords: "row, grid, data, prop, source, but, you, target"
generated: "2026-06-07T19:40:41.524230"
---

# JavaScript Proxy: One more way to use it I wish I’d known 3 years ago

## Overview

In our everyday work, we do a lot of data shuffling. We work with heavily loaded data grids. We have built our own RevoGrid for this matter hence market didn't offer all options we need back than. Some of our clients want to pull 400k rows and 5k columns into the UI and look at them on huge monitors. Don’t ask me what they see there. We deliver. For a very long time, our approach was to rely on different event management systems. Based on the event type, we would incrementally update data sources outside of the grid. And this works. But the problem with this approach is that you slowly end up with a lot of different events: cell edit range fill autofill copy/paste row grouping grouping migration column mapping source refresh external updates Trust me, a lot. So we were growing together with these events. One more feature, one more event. One more edge case, one more handler. But we live in the age of reactivity, so why not take one step further and make the source itself reactive? Instead of only reacting to grid events, we can feed the grid a source wrapped with Proxy . The idea is simple: The grid reads from the row through the get trap. And when the grid tries to write something back into the data source, we catch that write through the set trap. So the grid still works with normal-looking row objects: row . price row . quantity row . status But under the hood, we now control how reads and writes actually happen. A very simplified version looks like this: function createRowProxy < T extends object > ( row : T , onWrite : ( row : T , prop : keyof T , value : unknown ) => void , ): T { return new Proxy ( row , { get ( target , prop , receiver ) { return Reflect . get ( target , prop , receiver ); }, set ( target , prop , value , receiver ) { const result = Reflect . set ( target , prop , value , receiver ); onWrite ( target , prop as keyof T , value ); return result ; }, }); } Then we can pass proxied rows into the grid: const source = rawRows . map ( row => createRowProxy ( row , ( row , prop , value ) => { console . log ( ' changed: ' , row . id , prop , value ); // mark field as dirty // update external store // queue backend sync // trigger validation // update derived state }), ); grid . source = source ; Now the interesting part: The grid/component does not need to know anything about your real store architecture. It does not care if your data lives in: a plain array a Map a normalized store a remote cache a local-first database a custom reactive state layer From the grid perspective, it just reads and writes object properties. But from your application perspective, you now have a controlled bridge between the grid and your real data model. For example, the grid can read: row . quantity But internally this can be resolved from something like: rowsById . get ( row . id ). quantity Same for writes. The grid can do: row . quantity = 10 And your proxy can decide what should happen next: set ( target , prop , value ) { updateStore ( target . id , prop , value ); markDirty ( target . id , prop ); queueSave ( target . id ); return true ; } This is where the pattern becomes useful. You stop treating every grid event as the main data pipeline. Instead, the row object becomes an adapter. Events are still useful. I would not remove them completely. You still want events for things like: validation cancellation editor lifecycle analytics permissions before/after hooks custom UX behavior But for data synchronization itself, proxy-based source handling can be much cleaner. Especially when you have many ways to change data: direct cell editing paste autofill range updates programmatic updates grouping changes external source changes Instead of writing separate synchronization logic for every path, you can centralize a big part of it at the data access level. Of course, there are rules. Do not create proxies inside render loops Keep proxy identity stable Avoid mixing too much logic in both edit events and proxy setters, otherwise you will double-handle the same update Think carefully about performance if you are working with very large datasets. But as a pattern, it is surprisingly practical. For me, this changed how I think about data flow - component does not always need to own the data flow. Sometimes it is better to give it an object that looks simple from the outside, but is smart enough inside to route reads and writes into your actual application state. I wrote this while working on editable data-grid internals. We use this pattern in RevoGrid’s proxy source approach, but the idea itself works with any editable table/grid where you want your app state to stay in control. Happy coding!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/revolist/javascript-proxy-one-more-way-to-use-it-i-wish-id-known-3-years-ago-40lk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
