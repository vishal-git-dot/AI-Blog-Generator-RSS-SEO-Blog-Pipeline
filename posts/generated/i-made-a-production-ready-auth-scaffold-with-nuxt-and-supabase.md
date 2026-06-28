---
title: "I made a production ready auth scaffold with Nuxt and Supabase"
slug: "i-made-a-production-ready-auth-scaffold-with-nuxt-and-supabase"
author: "Theo"
source: "devto_webdev"
published: "Sun, 28 Jun 2026 19:33:23 +0000"
description: "I have a lot of ideas. The kind of ideas you get at midnight, the ones that seem brilliant, and then I have to implement auth and all traction on a brilliant..."
keywords: "auth, nuxt, supabase, time, brilliant, idea, through, your"
generated: "2026-06-28T19:38:17.339004"
---

# I made a production ready auth scaffold with Nuxt and Supabase

## Overview

I have a lot of ideas. The kind of ideas you get at midnight, the ones that seem brilliant, and then I have to implement auth and all traction on a brilliant idea gets lost within 15 minutes of overthinking how I want to set up auth this time. The next brilliant idea I got, not at midnight this time was building an auth scaffold for myself that I can simply reuse for every single idea. But the caveat is I decided against just vibe coding it. Auth is a weird one. It's boring enough that you want to hammer through it, but it's also your first line of security. Cutting corners here means cutting corners on the one thing that protects your users. So I actually spent some time clueing myself up on how to do this properly for Nuxt/Supabase projects (my preferred 10x developer stack). I didn't just hook this project up and called it done, I spent time thinking through edge cases, user flows, error handling, user feedback, and my desired initial application behaviour... to be honest I don't think I've ever thought as much as I did with this ever before. Feel free to check out the live demo or dig through the repository . I'd love to hear your thoughts and feedback. What's in the box though? Sign up with email confirmation (optional because I made sure both was supported) Sign in Forgot password + password reset via email link All PKCE code exchanges handled in a dedicated route Protected routes via Supabase's redirect options + a guest middleware that boots authenticated users off the auth pages where they don't belong Live password strength feedback during sign up (built as a composable considering its used in a few places and potentially a few more) Friendly, specific error handling throughout Dark mode (based on the system's preference) Polished UI with Nuxt UI Tech stack What Package Framework Nuxt 4 Auth + DB Supabase UI Nuxt UI 4 Validation Zod Styling Tailwind CSS 4

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/theosucksatcode/i-made-a-production-ready-auth-scaffold-with-nuxt-and-supabase-35m2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
