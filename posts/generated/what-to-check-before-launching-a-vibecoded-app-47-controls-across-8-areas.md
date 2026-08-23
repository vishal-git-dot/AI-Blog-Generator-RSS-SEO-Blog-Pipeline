---
title: "What to check before launching a vibecoded app: 47 controls across 8 areas"
slug: "what-to-check-before-launching-a-vibecoded-app-47-controls-across-8-areas"
author: "Jakub"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 18:19:37 +0000"
description: "The average AI-generated project scores 31 out of 100 on a production-readiness scale. We know because we built Audit Vibe Coding by Inithouse , a profession..."
keywords: "audit, what, code, vibecoded, generated, where, missing, projects"
generated: "2026-08-23T18:35:57.072776"
---

# What to check before launching a vibecoded app: 47 controls across 8 areas

## Overview

The average AI-generated project scores 31 out of 100 on a production-readiness scale. We know because we built Audit Vibe Coding by Inithouse , a professional audit for AI-generated (vibecoded) projects, and have been running it against real apps shipped from tools like Lovable, Cursor, Bolt, Replit and others. Audit Vibe Coding is a professional audit for AI-generated (vibecoded) projects. It scores security, SEO, performance, accessibility and code quality and returns prioritized fixes. The whole thing runs from a URL alone. No repo access, no SDK integration, no account needed. Here is what the 47 checks actually look at and what keeps failing. The eight audit areas Every audit covers the same eight areas. Each area has its own checks, its own severity weights, and its own section in the final scored report. 1. Security and privacy This is where vibecoded projects bleed the most. Exposed API keys in client bundles, missing Content-Security-Policy headers, forms submitting over HTTP, localStorage tokens sitting in plain text. We regularly find Supabase anon keys, Stripe publishable keys, and OpenAI tokens baked into frontend JavaScript. One project had its entire .env file served as a static asset. 2. SEO and discoverability Missing title tags, duplicate meta descriptions, no canonical URLs, broken Open Graph tags. AI code generators tend to produce technically functional HTML but skip everything that helps search engines and social platforms understand the page. Most vibecoded apps we audit have zero structured data markup. 3. Performance Uncompressed images, no lazy loading, render-blocking scripts, bundle sizes above 2 MB for a single-page app. The median Lighthouse performance score for vibecoded projects we have audited sits around 45. Production-ready apps typically land above 85. 4. Accessibility Missing alt text, no focus indicators on interactive elements, color contrast below WCAG AA thresholds, form inputs without labels. The focus state issue is nearly universal: AI-generated components often use outline: none in resets and never add a replacement. Keyboard users hit a dead end. 5. Code quality Unused dependencies, console.log statements left in production, no error boundaries, hardcoded strings where environment variables belong. We also check for leftover TODO comments, which appear in roughly 60% of audited projects. 6. UX flows Broken navigation paths, dead-end states after form submission, missing loading indicators, error messages that say "something went wrong" and nothing else. AI builders are good at generating the happy path but rarely handle edge cases or empty states. 7. Mobile UX Tap targets too small, horizontal overflow, fixed-width layouts that break below 375px, text that needs pinch-zooming. Responsive design is one area where AI tools have improved, but viewport-specific bugs still show up consistently. 8. Stability and error handling No global error boundary, unhandled promise rejections, missing try-catch around API calls, no offline fallback. When the backend goes down, most vibecoded apps show a blank white screen. What a scored report looks like Each check gets a pass/fail result, a severity rating (critical, high, medium, low), and a difficulty estimate for fixing it. The total score rolls up to a single number out of 100. A project scoring 31 has real issues across multiple areas. A score of 80+ means the fundamentals are solid and the remaining items are optimizations, not risks. The report groups fixes by priority: critical security issues first, then high-severity items that affect users directly, then medium and low items that improve quality over time. Each fix comes with a concrete description of what to change and where. Why URL-only matters Traditional code audits need repository access, CI integration, or at least a local build. That works fine for teams with established workflows. It does not work for someone who just shipped from Lovable and wants to know if the thing is safe to send to users. Running the audit from a URL means the barrier is exactly zero. Paste the link, get the report. The audit examines what your users actually see and experience, not what your source code looks like in theory. What we see across audits Three patterns keep repeating. First, security is almost always the weakest area. Exposed keys and missing headers account for most critical findings. These are also the easiest to fix once someone points them out. Second, SEO is consistently neglected. AI tools generate working apps, not discoverable ones. The difference between a project that shows up in search results and one that does not often comes down to five or six meta tags. Third, accessibility scores cluster around 30-40 out of 100. This is partly because AI-generated CSS resets strip default browser styles (including focus rings) and the generated code rarely adds them back. Where Audit Vibe Coding fits in the Inithouse portfolio We run Audit Vibe Coding by Inithouse alongside other tools we have built at Inithouse, including Be Recommended , an AI visibility monitoring tool for brands, and Watching Agents , a platform for AI prediction and monitoring agents. All three share a common thread: they help people understand what AI systems actually do with their work, whether that is code, brand mentions, or forecasts. If you shipped something with an AI code generator and want to know where it stands before real users see it, the audit runs from a URL and covers the 47 checks listed above.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jakub_inithouse/what-to-check-before-launching-a-vibecoded-app-47-controls-across-8-areas-54ed

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
