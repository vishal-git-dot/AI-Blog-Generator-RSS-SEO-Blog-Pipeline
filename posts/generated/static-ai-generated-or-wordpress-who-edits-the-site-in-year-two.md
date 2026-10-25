---
title: "Static, AI-generated or WordPress: who edits the site in year two?"
slug: "static-ai-generated-or-wordpress-who-edits-the-site-in-year-two"
author: "Wbcom Designs 💡"
source: "devto_webdev"
published: "Sun, 25 Oct 2026 15:47:59 +0000"
description: "The "is WordPress finished?" argument never really goes away, but the shape of it keeps changing. Across the communities we follow, we keep seeing the same s..."
keywords: "site, static, sites, who, cms, edits, one, they"
generated: "2026-10-25T15:52:15.456798"
---

# Static, AI-generated or WordPress: who edits the site in year two?

## Overview

The "is WordPress finished?" argument never really goes away, but the shape of it keeps changing. Across the communities we follow, we keep seeing the same split. On one side: someone replaces a years-old client site with a static build generated from a single AI prompt and declares the CMS era over. An agency moves dozens of small client sites to a static framework over a long weekend. Developers point out that a brochure site has no reason to run PHP and a database, and a big security scare makes that point louder. On the other side: a volunteer at a small nonprofit explains that every text change on their site takes a week, because only one person can make it. A designer moves to WordPress from a hosted builder because they want ten to fifteen client sites on one stack they control. Someone asks whether a site with member logins and a shop can go static at all, and the honest answer is "not really". Both sides are describing real sites. They're just describing different sites. Here's how we see the two cases, and then the parts we genuinely don't know. The case for static (and AI-built) sites Fewer moving parts. No database, no plugin updates, no login page to attack. For a site that is a few pages and a contact form, that's a real win, and the maintenance bill drops close to zero. Speed and hosting cost. Static files are fast almost anywhere and cheap to host. For agencies with many small, rarely changing sites, that adds up. Security posture. Every time a widely used plugin or core component has a serious hole, people who run lots of sites spend a stressful day patching. Static sites mostly skip that day. AI changed the build cost. Generating a clean marketing site from a prompt or a design file is now quick. If the build is nearly free, the argument for a heavy CMS "in case they need it" gets weaker. Honest about who edits. Many small business owners never log in after launch. If the agency makes every change anyway, a CMS is overhead nobody uses. The case for keeping a CMS Someone else has to edit it. This is the one we hear most. The site isn't for the developer, it's for the owner, the volunteer or the marketing hire who joins next year. If they want to add a post, swap a photo or publish an event without opening a ticket, the editing screen is the product. Logged-in people change everything. The moment a human logs in to do something, buy, enrol, post, apply, RSVP, comment, a static site needs a backend anyway. At that point you're either bolting services onto static pages or running an application, and a CMS with users and roles starts looking simpler, not heavier. Migration is the hidden cost. People who moved sites to static generators talk about the hurdles: forms, search, redirects, old URLs, image handling, and content that lived in shortcodes or page builders. The site was easy to rebuild. The content wasn't. Ownership and handover. When a project ends, who owns updates? With a CMS that question is loud and usually lands in a care plan. With a static site it's quieter, but it still exists: someone has to own the repo, the build, the hosting and the domain. Rewrites are rarely worth it. Builders who have done full rewrites tend to say the same thing: the only ones they didn't regret were the ones where the underlying data model was wrong. Moving a working site to a new stack because the old one feels unfashionable is a different decision. Where we land, for now Our rough rule: static for sites nobody edits, a CMS once someone non-technical edits, and an application once logged-in people do things. Most arguments we see are people applying the right answer for their kind of site to someone else's kind of site. But that rule leaves a lot of grey area, and we'd rather hear how you handle it than pretend we've figured it out. The questions we can't settle Does AI editing replace the editing screen? If a client can say "update the opening hours" to an assistant and it edits a static repo, do they still need a CMS? Or does that just move the "one person who can make changes" problem from a developer to a tool? What does year two look like? Most launch decisions are made for launch day. We'd love to hear from people who went static two or three years ago. Did the client stay happy, or did small change requests pile up? Is security a stack problem or a habits problem? One view says the CMS is the risk. Another says lean plugin lists, auto-updates and off-site backups make most of that risk go away, and that static sites have their own weak spots in build pipelines and third-party form services. Which matches your experience? Where's the line for member features? A site with gated PDFs, a members' area or a small shop is in between. Some people bolt on hosted services, some keep a CMS for just that part, some run two sites. What's worked for you? Who decides? Often the developer picks the stack because they'll maintain it. Should the person who edits the site in year two get the deciding vote instead? Your turn Have you moved a site off a CMS, or onto one? What made you do it, and would you do it again? For small client sites, who actually edits the content after launch: you, the client, or nobody? Where do you draw the line between "static is fine" and "this needs a backend"? If AI can make edits for non-technical owners, does that change your answer? We build mostly on WordPress, so we know which way we lean. That's exactly why we want the other side in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wbcomdesigns/static-ai-generated-or-wordpress-who-edits-the-site-in-year-two-6j5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
