---
title: "Your Auto-Generated TypeScript Interfaces Are Lying to You"
slug: "your-auto-generated-typescript-interfaces-are-lying-to-you"
author: "Rasika Dangamuwa"
source: "devto_webdev"
published: "Wed, 15 Jul 2026 19:08:20 +0000"
description: "If you've ever pasted an API response into a JSON-to-TypeScript converter and shipped the result, you've probably shipped a few silent bugs along with it. Th..."
keywords: "you, string, type, converter, field, one, has, json"
generated: "2026-07-15T19:19:36.617386"
---

# Your Auto-Generated TypeScript Interfaces Are Lying to You

## Overview

If you've ever pasted an API response into a JSON-to-TypeScript converter and shipped the result, you've probably shipped a few silent bugs along with it. These tools are useful for a first draft, but naive JSON inference gets several things wrong in ways that don't show up until production. 1. Every field looks required A converter only sees the sample you give it. If a field happens to be present in that one response, it's marked required — even if the API omits it half the time (e.g. discountCode only appears on orders that used one). The fix isn't tooling, it's discipline: check the API docs (or several real responses) before you trust required vs optional? . 2. null and "not present" get merged JSON has null . TypeScript has null , undefined , and "key absent." A converter usually collapses all three into one union member, so you lose the distinction between "this field can be explicitly cleared" and "this field might not be sent at all." If your code branches differently on undefined vs null (a lot of form-state code does), that distinction matters and needs to be added by hand. 3. Numeric-looking strings get typed as number IDs, phone numbers, zip codes with leading zeros, monetary amounts as strings to avoid floating-point rounding — all of these can appear numeric in a sample payload but are semantically strings. A converter has no way to know that "07001" should stay a string. Always sanity-check ID and code fields by hand. 4. Dates stay as string , forever "createdAt": "2026-07-15T10:00:00Z" becomes createdAt: string in every converter I've tried, because JSON has no date type. That's technically correct but throws away intent — nothing stops a future teammate from doing string comparisons on dates instead of parsing them. Consider a branded type ( type ISODateString = string & { __brand: "ISODate" } ) or at least a comment, so the next reader knows to parse before comparing. 5. Arrays only reflect the first element's shape If an array's first item has fewer fields than later items (common with polymorphic lists — think a activity feed mixing "comment," "like," and "mention" events), most converters infer the type from item zero and silently drop fields that only appear in later items. You need a real union type ( type Event = CommentEvent | LikeEvent | MentionEvent ) discriminated on a shared field like type , and that has to be modeled by hand from the real variants, not guessed from one sample. 6. String enums get widened to string If a status field is always one of "pending" | "active" | "cancelled" in your sample, a naive converter still just types it as string , because it can't know the domain is closed. Narrowing that to a literal union is worth the extra minute — it's what turns a typo like "acive" into a compile error instead of a runtime bug. The actual workflow that works Auto-generation is fine as a starting point for boilerplate you'd otherwise type by hand. The failure mode is treating the output as final. A workflow that holds up: Generate the interface from a real sample response (not a made-up one). Cross-reference it against API docs or a couple more real payloads for optional/nullable fields. Manually narrow anything that's secretly an enum, a date, or a discriminated union. Re-run it after the backend changes — schemas drift and nobody update the types. If you want a quick first pass without installing anything, nutilz.com/json-to-typescript does the basic conversion in the browser — just don't treat step 1 as the whole workflow.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rasika_dangamuwa_ed1074fe/your-auto-generated-typescript-interfaces-are-lying-to-you-dfe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
