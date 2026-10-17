---
title: "Is my Supabase database public? A 5-minute check with the anon key"
slug: "is-my-supabase-database-public-a-5-minute-check-with-the-anon-key"
author: "FixLoop"
source: "devto_webdev"
published: "Sat, 17 Oct 2026 20:09:09 +0000"
description: "If you shipped a Lovable (or any Supabase) app, your anon key is in the browser. That's fine, it's supposed to be. The real question is different: can a stra..."
keywords: "anon, table, public, key, rls, can, select, rows"
generated: "2026-10-17T20:22:56.708709"
---

# Is my Supabase database public? A 5-minute check with the anon key

## Overview

If you shipped a Lovable (or any Supabase) app, your anon key is in the browser. That's fine, it's supposed to be. The real question is different: can a stranger read your tables with that key and no login? If Row Level Security is off on a table that still has grants to anon , the answer is yes. Here's a 5-minute check you can run on your own project. Why the anon key isn't the leak The anon key is a public JWT. Postgres then decides what it can do in two layers: Grants decide whether anon can SELECT / INSERT / UPDATE / DELETE the table at all. RLS decides which rows survive that grant. RLS off means the second layer never runs. If anon also has a grant (the old default on public tables), every row is reachable from the REST endpoint. A policy of using (true) is the same hole with RLS "on": the dashboard badge looks fine, the table is still public. The check Open your live app in a private window, DevTools → Network, filter rest/v1 . Grab the project host ( abcdefghij.supabase.co ), a table name from the path, and the apikey header from a signed-out request. Never use the service_role key for this (or anywhere in the client). curl "https://YOUR_PROJECT.supabase.co/rest/v1/YOUR_TABLE?select=*&limit=5" \ -H "apikey: YOUR_ANON_KEY" \ -H "Authorization: Bearer YOUR_ANON_KEY" No cookies, no session. If this returns user data, anyone can do it too. Reading the result 200 + rows : anon can read the table. RLS is off or a policy allows anonymous SELECT. Fix this first. 200 + [] : there's a SELECT grant but no rows passed RLS (or the table is empty). Retry on a table you know has data. If the signed-in app shows rows and anon still gets [] , you're probably fine. 401 : bad or truncated key. This does not mean the table is private. 403 / 42501 : anon has no grant, so the request never reaches RLS. After Oct 30, 2026 this shows up a lot on new tables ( why ). 404 / PGRST205 : wrong table name. Use the one from the network tab. The safe fix Turn RLS on and scope policies to auth.uid() . Don't "fix" an open table by granting more. alter table public . your_table enable row level security ; create policy "select own rows" on public . your_table for select to authenticated using ( auth . uid () = user_id ); create policy "insert own rows" on public . your_table for insert to authenticated with check ( auth . uid () = user_id ); grant select , insert , update , delete on table public . your_table to authenticated ; Don't do any of these: GRANT ALL ON ALL TABLES IN SCHEMA public TO anon; any grant to anon while RLS is off using (true) on a table with private rows the service_role key in frontend env In Lovable, put the same rules in your project instructions so the next migration doesn't recreate the hole. Full guide The longer version with the browser-console variant, a checklist, and an FAQ (should I rotate the anon key? Lovable says RLS is on, can it still be public?) is here: https://fixloop.dev/guides/is-my-supabase-database-public I run FixLoop . There's a free scan for leaked keys and missing headers, and we fix broken Lovable/Supabase apps for a fixed price. No fix, no pay.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fixloopdev/is-my-supabase-database-public-a-5-minute-check-with-the-anon-key-2iil

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
