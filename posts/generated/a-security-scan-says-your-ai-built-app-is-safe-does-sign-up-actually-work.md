---
title: "A security scan says your AI-built app is safe. Does sign-up actually work?"
slug: "a-security-scan-says-your-ai-built-app-is-safe-does-sign-up-actually-work"
author: "VibeTierList"
source: "devto_webdev"
published: "Wed, 21 Oct 2026 11:08:40 +0000"
description: "A wave of free scanners for AI-built apps will grade your live URL in under a minute. They're useful. But read their own pages and they're mostly answering o..."
keywords: "app, test, your, can, user, security, scan, what"
generated: "2026-10-21T11:30:28.803053"
---

# A security scan says your AI-built app is safe. Does sign-up actually work?

## Overview

A wave of free scanners for AI-built apps will grade your live URL in under a minute. They're useful. But read their own pages and they're mostly answering one question: what can a stranger grab without logging in? Whether your app actually works for a real user is a different test. Two different questions Security scan: "What can a stranger take?" It reads what your site sends to any browser and makes a few harmless requests: keys in the JavaScript, database tables open to the public key, downloadable .env or .git files, API routes that answer without login, security headers. Logged out, no writes. Functional test: "Does it work for a user?" It uses the app the way a customer would: sign up, log in, create and edit data, tap through it on a phone, log out. It finds the broken button, the stuck sign-up and the page that crashes on an emoji. It can't see a secret key sitting in your code. A security scan can give an A to an app whose sign-up is broken, and a functional test can pass an app that leaks a key. You need both. What five scanners say they check On 20 Oct 2026 we read the pages of five scanners aimed at vibe-coded apps: PreflightVibe, PreflightX, Prodable, Shippable and SafeWeave. This compares methods only (what each page says), not quality. We haven't run them on a test app, and none of them paid us. They overlap heavily on secrets and open data : keys in shipped code, Supabase/Firebase tables or buckets readable without login, API routes that answer without a session. Good, because those leaks expose everyone at once. None of their pages says it tests sign-up, saving data or the phone layout. The ones that say whether they log in say they don't. PreflightVibe is the most direct: it says it can't test what one user can see of another user's data, and tells you to do a two-account test yourself. Full matrix (13 questions × 6 tools, with prices as listed and links to each source page): Security scan vs functional test . Disclosure: we run one of the tools in that matrix (a free functional "Scan my app" beta). It has the same blind spot: it never logs in and blocks every write, and it doesn't look for keys or open tables. What our hands-on test found that no logged-out scan can see On 16 Oct 2026 we built the same multi-user to-do app with Lovable, Bolt, Base44 and v0 on free plans (one run each) and tested every app by hand with real accounts. The problems we found: Buttons that only exist for a mouse (Bolt). Edit and delete appeared only on hover, so on a phone they were invisible. Nothing leaked, so a security check has nothing to find. New users stuck at sign-up (Base44). A new user who closed the email-code page found no way to enter or resend the code from the login screen. You only see this by signing up, closing the tab and coming back. Logging out didn't end the session (Base44). The old access token still worked on the server after logout. A security bug, but a logged-out scan never holds a token to replay. Very short passwords accepted (Lovable). 6-character passwords went through. Finding it means actually creating an account. None of these was a leaked key or an open table. And on the check that matters most, all four apps passed: a second user couldn't see or change the first user's data. That's one run of a simple app, not a promise about yours. What to run before you launch One outside security scan on your live URL, for secret keys, tables readable with your public key and exposed files. Fix anything critical first. A functional pass over your pages: phone layout, buttons, junk input in forms, console and network errors. The logged-in checks, by hand: sign up as a brand-new user (badly), log out and replay the old session, and the two-account test (about 10 minutes with two browser windows). Again after every big change. Each new prompt to your AI builder can quietly undo a fix. The step-by-step version, with a receipt for each step where we have one: 12-step pre-launch checklist for AI-built apps . Originally published on VibeTierList , where we test AI app builders on the same task and publish the receipts. Paying never changes a ranking.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vibetierlist/a-security-scan-says-your-ai-built-app-is-safe-does-sign-up-actually-work-5fe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
