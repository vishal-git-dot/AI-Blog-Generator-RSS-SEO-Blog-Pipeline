---
title: "Middleware is not your auth layer (a Next.js footgun I keep finding)"
slug: "middleware-is-not-your-auth-layer-a-nextjs-footgun-i-keep-finding"
author: "Somnath Khadanga"
source: "devto_webdev"
published: "Fri, 30 Oct 2026 12:23:38 +0000"
description: "When I audit Next.js apps built quickly (often with AI tools), one pattern shows up more than any other: routes are protected in middleware.ts , and the API ..."
keywords: "middleware, users, user, session, api, route, admin, return"
generated: "2026-10-30T12:30:58.223667"
---

# Middleware is not your auth layer (a Next.js footgun I keep finding)

## Overview

When I audit Next.js apps built quickly (often with AI tools), one pattern shows up more than any other: routes are protected in middleware.ts , and the API route handlers trust that. // app/api/admin/users/route.ts export async function GET ( request : NextRequest ) { // "middleware already checked" const users = await db . user . findMany () return NextResponse . json ( users ) } Middleware can be skipped by a matcher that doesn't cover a new route, misconfigured during a refactor, or bypassed by calling the API directly. If the handler doesn't check, the data is open. The fix is boring: every handler that touches user data verifies the session and role itself. export async function GET ( request : NextRequest ) { const session = await getServerSession ( authOptions ) if ( ! session ) return NextResponse . json ({ error : ' Unauthorized ' }, { status : 401 }) if ( session . user . role !== ' admin ' ) return NextResponse . json ({ error : ' Forbidden ' }, { status : 403 }) const users = await db . user . findMany () return NextResponse . json ( users ) } Two related checks worth doing while you're there: Hiding the admin dashboard in React when role !== 'admin' is UI gating, not access control. The API behind it still needs the server-side check. Delete a user's session row and make a request with their old cookie. If it still works, revocation isn't wired up. Rule of thumb: middleware is a convenience layer for redirects and early exits. The security boundary is the handler. How do you handle this in your apps: a shared requireUser() helper, or checks inline in each route?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/somnath_khadanga_2e5c2364/middleware-is-not-your-auth-layer-a-nextjs-footgun-i-keep-finding-2n31

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
