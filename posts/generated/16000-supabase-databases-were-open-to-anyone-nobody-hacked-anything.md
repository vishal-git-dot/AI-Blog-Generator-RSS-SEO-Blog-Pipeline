---
title: "16,000 Supabase Databases Were Open to Anyone. Nobody Hacked Anything."
slug: "16000-supabase-databases-were-open-to-anyone-nobody-hacked-anything"
author: "Format stack"
source: "devto_webdev"
published: "Thu, 08 Oct 2026 05:20:19 +0000"
description: "On September 25, UpGuard reported 16,326 Supabase databases with publicly readable tables . More than half showed signs of personal data. Some had passwords ..."
keywords: "key, supabase, data, rls, anon, your, read, project"
generated: "2026-10-08T05:29:48.191898"
---

# 16,000 Supabase Databases Were Open to Anyone. Nobody Hacked Anything.

## Overview

On September 25, UpGuard reported 16,326 Supabase databases with publicly readable tables . More than half showed signs of personal data. Some had passwords and tokens. No one broke in. The data was readable through the front door. What went wrong Supabase's anon key ships in your browser code by design. Row-level security (RLS) decides what that key can read. RLS off means anyone with your project URL and key can read the table. Nothing errors, so nobody notices. UpGuard says many of the apps appear to be built with AI coding agents, though not in every case. Check yours in 2 minutes Turn on RLS and add a policy: alter table public . profiles enable row level security ; create policy "read own profile" on public . profiles for select to authenticated using (( select auth . uid ()) = user_id ); Then test as an anonymous user. You should get an empty result or an error, never rows: curl "https://<project-ref>.supabase.co/rest/v1/profiles?select=*&limit=1" \ -H "apikey: <anon-key>" -H "Authorization: Bearer <anon-key>" Also keep service_role out of client code, and don't store passwords in app tables. Same pattern, everywhere Data rarely leaves through a hack. It leaves because an action moved it somewhere and nothing said so: a missing policy, a debug log, a paste into a random web tool. I wrote up nine of these: Where Developer Data Actually Leaks Have you audited RLS on your project lately? Sources: BleepingComputer, TechCrunch

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/formatstack_2688dca3303f2/16000-supabase-databases-were-open-to-anyone-nobody-hacked-anything-nm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
