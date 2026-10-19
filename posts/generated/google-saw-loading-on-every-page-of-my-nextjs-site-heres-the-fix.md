---
title: "Google saw "Loading…" on every page of my Next.js site. Here's the fix."
slug: "google-saw-loading-on-every-page-of-my-nextjs-site-heres-the-fix"
author: "Fellipe Gonçalves"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 21:39:23 +0000"
description: "I help run Brasil Afora, a free, nonprofit catalog of scholarships and study programs for Brazilian students. It's a volunteer project on Next.js (App Router..."
keywords: "page, but, server, google, site, fix, after, search"
generated: "2026-10-19T22:10:53.098761"
---

# Google saw "Loading…" on every page of my Next.js site. Here's the fix.

## Overview

I help run Brasil Afora, a free, nonprofit catalog of scholarships and study programs for Brazilian students. It's a volunteer project on Next.js (App Router), Postgres and TanStack Query. A few weeks after we shipped a sitemap, Search Console showed impressions but our detail pages were stuck on page two, and many weren't indexed at all. Those pages are the whole point of the site: they're what should show up when someone searches for a specific scholarship and its deadline. So I fetched a page the way Googlebot would: curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" \ https://brasilafora.org/oportunidades/internacionais/< id > | grep -c "<h1" Zero. The initial HTML was about 40 words and a "Carregando oportunidade…" ("Loading opportunity…") placeholder. The page was a client component that fetched its record with useQuery after mounting. Fine for people, but the first HTML was an empty shell. Google can render JavaScript, but for a new site with no authority that often ends in "crawled, currently not indexed". The fix was to read the record on the server and hand it to React Query as initialData , without rewriting the page. The route became a server component: export default async function NationalOpportunityDetailsPage ( props : PageProps < " /oportunidades/nacionais/[id] " > ) { const { id } = await props . params ; if ( ! ( await getOpportunityMetadata ( " national " , id ))) { notFound (); } return ( < NacionalInfo id = { id } initialOpportunity = { await getNationalOpportunityForPage ( id ) } /> ); } And the hook the page already used just gained one parameter: export const useNationalOpportunityByIdQuery = ( id : string , initialData ?: NationalOpportunity ) => useQuery ({ queryKey : opportunityQueryKeys . nationalById ( id ), queryFn : () => getNationalOpportunityById ( id ), enabled : id . length > 0 , initialData , }); One thing that saved me trouble: the server read lives in a single module, and the /api/opportunities/[id] route uses the same reader. The object the page gets on the server is exactly what the client would have fetched later, so there's no hydration mismatch and no duplicated logic. Two smaller bugs surfaced along the way. Hidden or unknown records returned a 200 with a "not found" message; they now call notFound() and return a real 404. And titles went from just the program name to a search-shaped "<name>: inscrições, prazo e requisitos" (applications, deadline and requirements). After the deploy, the same curl returns about 470 words and an h1. Daily impressions in Search Console went from roughly 15–25 in late September to 20–60 in October. That's too early and too small to credit the fix alone, so I'll update this once there's more data. Two open questions, if you've been here: our URLs are still UUIDs, and I'm unsure whether moving to slugs now helps or just resets what's already indexed. And a few records exist twice (a curated page and a database page), each canonical to itself. My plan is to point the duplicate's canonical at the curated one, but I'd love to hear how that went for others.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fellipe_gonalves_76a4ba3/google-saw-loading-on-every-page-of-my-nextjs-site-heres-the-fix-bj1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
