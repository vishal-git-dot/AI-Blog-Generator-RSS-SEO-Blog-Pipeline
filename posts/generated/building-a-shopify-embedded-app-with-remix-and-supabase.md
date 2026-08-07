---
title: "Building a Shopify Embedded App with Remix and Supabase"
slug: "building-a-shopify-embedded-app-with-remix-and-supabase"
author: "seller-mind"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 13:07:37 +0000"
description: "Building a Shopify app in 2026 means using the Remix framework, App Bridge for embedded UI, and dealing with Shopify session tokens. Here is what I learned b..."
keywords: "app, shopify, session, building, embedded, remix, bridge, parcelglance"
generated: "2026-08-07T13:15:09.530986"
---

# Building a Shopify Embedded App with Remix and Supabase

## Overview

Building a Shopify app in 2026 means using the Remix framework, App Bridge for embedded UI, and dealing with Shopify session tokens. Here is what I learned building Parcelglance. The Stack Remix (React framework) Shopify App Bridge Supabase for session storage Shopify CLI The OAuth Flow App URL receives shop parameter Generate auth URL with correct scopes Redirect to Shopify auth page Callback receives code, exchanges for access token Store session in database Redirect to admin with session token Common Pitfalls Session Storage Use a database, not in-memory sessions. Serverless platforms need persistent storage. Environment Variables Verify your SUPABASE_URL is correct. A single typo means all operations fail silently. CORS and Embedded Mode Your app runs inside an iframe. Ensure proper CSP headers and App Bridge initialization. Webhooks Register webhooks for app/uninstalled, orders/create, and products/update. The App Review Process Shopify reviews every app. Key requirements: Working OAuth flow Proper data handling Privacy policy and ToS GDPR webhooks Try Parcelglance Parcelglance is live on the Shopify App Store. Building a Shopify app? Drop a comment.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sellermind/building-a-shopify-embedded-app-with-remix-and-supabase-3cjf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
