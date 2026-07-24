---
title: "Next.js 15 Caching Explained — Finally Makes Sense"
slug: "nextjs-15-caching-explained-finally-makes-sense"
author: "Anas Sheikh"
source: "devto_webdev"
published: "Fri, 24 Jul 2026 13:51:13 +0000"
description: "Next.js caching confused me for months. The docs are thorough but overwhelming. Nobody explains the simple mental model. Here it is. The Simple Mental Model ..."
keywords: "posts, next, post, data, revalidate, cache, await, const"
generated: "2026-07-24T13:55:42.404892"
---

# Next.js 15 Caching Explained — Finally Makes Sense

## Overview

Next.js caching confused me for months. The docs are thorough but overwhelming. Nobody explains the simple mental model. Here it is. The Simple Mental Model Next.js has one question for every data fetch: "How fresh does this data need to be?" Old data is fine → cache it Always needs to be live → skip cache Refresh every X seconds → revalidate on timer Refresh when something changes → revalidate on demand Everything else follows from this. 1. Default — Cached Forever // Cached on first request — never fetches again const data = await fetch ( ' https://api.example.com/posts ' ); Use this for data that never changes — like static content, documentation, or marketing copy. 2. Never Cache — Always Fresh // Fresh data on every request const data = await fetch ( ' https://api.example.com/orders ' , { cache : ' no-store ' }); Use this for data that must be real-time — user dashboards, live prices, notifications. 3. Revalidate on a Timer // Refetch every 60 seconds const data = await fetch ( ' https://api.example.com/products ' , { next : { revalidate : 60 } }); Use this for data that changes occasionally — blog posts, product listings, leaderboards. Good revalidation times: News feed → 60 seconds Product catalog → 300 seconds (5 mins) Blog posts → 3600 seconds (1 hour) 4. Revalidate on Demand The most powerful pattern — refresh cache exactly when data changes: // app/api/revalidate/route.ts import { revalidatePath , revalidateTag } from ' next/cache ' ; import { NextRequest } from ' next/server ' ; export async function POST ( request : NextRequest ) { const { path , tag , secret } = await request . json (); // Protect with secret key if ( secret !== process . env . REVALIDATION_SECRET ) { return Response . json ({ error : ' Unauthorized ' }, { status : 401 }); } if ( path ) revalidatePath ( path ); // revalidate a specific page if ( tag ) revalidateTag ( tag ); // revalidate tagged fetches return Response . json ({ revalidated : true }); } Call this API from your CMS, database webhook, or admin panel when content changes. Tags — The Missing Piece Tags let you group related fetches and invalidate them together: // Tag your fetches const posts = await fetch ( ' https://api.example.com/posts ' , { next : { tags : [ ' posts ' ] } }); const post = await fetch ( `https://api.example.com/posts/ ${ id } ` , { next : { tags : [ ' posts ' , `post- ${ id } ` ] } }); Now when a post is updated — invalidate just the affected tags: import { revalidateTag } from ' next/cache ' ; // In your Server Action when post is updated export async function updatePost ( id : string , data : PostData ) { await db . posts . update ({ where : { id }, data }); revalidateTag ( `post- ${ id } ` ); // invalidate this specific post revalidateTag ( ' posts ' ); // invalidate the posts list } Real Example — Blog with On-Demand Revalidation // app/blog/page.tsx async function BlogPage () { // Cache for 1 hour, tag as 'posts' const posts = await fetch ( ' https://api.example.com/posts ' , { next : { revalidate : 3600 , tags : [ ' posts ' ] } }). then ( r => r . json ()); return ( < div > { posts . map ( post => ( < article key = { post . id } > < h2 > { post . title } < /h2 > < /article > ))} < /div > ); } // app/blog/[slug]/page.tsx async function BlogPost ({ params }) { const { slug } = await params ; // Tag with specific post ID const post = await fetch ( `https://api.example.com/posts/ ${ slug } ` , { next : { revalidate : 3600 , tags : [ ' posts ' , `post- ${ slug } ` ] } }). then ( r => r . json ()); return < article > { post . content } < /article> ; } // Server Action — called when admin publishes/edits post export async function publishPost ( slug : string ) { ' use server ' ; await db . posts . update ({ where : { slug }, data : { published : true } }); // Instantly refresh affected pages revalidateTag ( `post- ${ slug } ` ); revalidateTag ( ' posts ' ); } When admin clicks "Publish" — both the post page and the blog listing update instantly. No waiting for the timer. Caching with Database Queries The same patterns work with direct database calls using unstable_cache : import { unstable_cache } from ' next/cache ' ; // Cache database query for 5 minutes const getCachedPosts = unstable_cache ( async () => { return db . posts . findMany ({ where : { published : true }, orderBy : { createdAt : ' desc ' } }); }, [ ' posts ' ], // cache key { revalidate : 300 , // 5 minutes tags : [ ' posts ' ] // for on-demand invalidation } ); // Use in server component const posts = await getCachedPosts (); Quick Reference Pattern Code Use when Cache forever fetch(url) Static content Never cache cache: 'no-store' Real-time data Timer revalidate next: { revalidate: 60 } Mostly static Tag revalidate next: { tags: ['x'] } CMS content Path revalidate revalidatePath('/page') After mutation Tag invalidate revalidateTag('x') After mutation Once this clicked for me I stopped over-fetching and under-caching. My Next.js apps became significantly faster with almost no extra code. I use these patterns in all my Next.js templates: https://neurodash-dashbord.vercel.app/ https://og-ai-next.vercel.app/ Get the templates: https://pixelanas.gumroad.com What's your caching strategy? Drop it below 👇 Anas — full-stack Next.js developer. X: @pixelanas

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/anas_sheikh_2/nextjs-15-caching-explained-finally-makes-sense-feb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
