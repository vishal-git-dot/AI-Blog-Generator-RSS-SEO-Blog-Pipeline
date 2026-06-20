---
title: "My API Broke Every January 1st — The Timezone Bug That Slipped Past Code Review"
slug: "my-api-broke-every-january-1st-the-timezone-bug-that-slipped-past-code-review"
author: "kol kol"
source: "devto_webdev"
published: "Sat, 20 Jun 2026 14:04:46 +0000"
description: "My API broke at exactly 00:00 UTC on January 1st. Not the users' midnight — UTC midnight . Which meant our users in Tokyo had been living with broken data si..."
keywords: "date, utc, timezone, new, our, production, every, staging"
generated: "2026-06-20T14:15:47.239244"
---

# My API Broke Every January 1st — The Timezone Bug That Slipped Past Code Review

## Overview

My API broke at exactly 00:00 UTC on January 1st. Not the users' midnight — UTC midnight . Which meant our users in Tokyo had been living with broken data since 9 AM their time. And the worst part? The tests all passed. The staging environment worked fine. It only broke in production, because production is in a different timezone than staging. The Bug Here's what the code looked like: function getDailyReport ( date ) { const start = new Date ( date ). toISOString (). split ( ' T ' )[ 0 ]; const end = new Date ( start + ' T23:59:59Z ' ); return db . reports . findMany ({ where : { createdAt : { gte : new Date ( start ), lt : end } } }); } Seems fine, right? toISOString() gives you UTC. We're filtering by date. What could go wrong? Here's what went wrong: new Date(date) when date is just "2026-01-01" (no time component) gets interpreted in the local timezone . In staging (UTC server), "2026-01-01" → 2026-01-01T00:00:00.000Z . In production (US-East server), "2026-01-01" → 2026-01-01T05:00:00.000Z . Five hour offset. Every single date query. For an entire year before anyone noticed. Why Tests Passed Our CI runs in Docker containers set to UTC. Our staging server is also UTC. Our production server? US-East. The timezone mismatch was invisible until New Year's Day rolled around and the date boundary crossed the timezone offset. Staging (UTC): 2026-01-01 → Jan 1 00:00 UTC ✅ Production (EST): 2026-01-01 → Jan 1 05:00 UTC ❌ We lost 5 hours of data on every query. The reports showed numbers that were "close enough" that nobody flagged it for 12 months. The Fix function getDailyReport ( date : string ) { // Always append time to force UTC interpretation const start = new Date ( ` ${ date } T00:00:00Z` ); const end = new Date ( ` ${ date } T23:59:59.999Z` ); return db . reports . findMany ({ where : { createdAt : { gte : start , lt : end } } }); } One line change. Append T00:00:00Z to force the Date constructor into UTC mode. No more ambiguity. The Real Fix (Process, Not Code) The code fix took 30 seconds. The real fix took a week: Added a timezone assertion in CI — our test suite now explicitly checks that process.env.TZ === 'UTC' . If anyone changes the CI timezone, tests fail. Set TZ=UTC in all Dockerfiles — every container, every environment, same timezone. No surprises. Added a timezone check to our deploy script — date +%Z must return UTC before deploy proceeds. Wrote a linter rule — flags any new Date(string) where the string doesn't contain timezone info. The Lesson Timezone bugs are sneaky because they don't crash. They produce wrong data that looks right. Your users won't get an error page — they'll get silently incorrect numbers, and they'll trust them. Three rules I now follow: Never trust the system timezone. Always set TZ=UTC explicitly. Never parse dates without timezones. "2026-01-01" is ambiguous. "2026-01-01T00:00:00Z" is not. Never assume your CI timezone matches production. Assert it in your tests. I've been coding for years. I still got bit by this. If it can happen to me, it can happen to you. Read more developer war stories and technical deep-dives at codcompass.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kollittle/my-api-broke-every-january-1st-the-timezone-bug-that-slipped-past-code-review-j40

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
