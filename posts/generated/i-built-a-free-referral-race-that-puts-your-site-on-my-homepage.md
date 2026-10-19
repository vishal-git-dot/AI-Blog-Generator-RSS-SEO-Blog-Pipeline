---
title: "I built a free referral race that puts your site on my homepage"
slug: "i-built-a-free-referral-race-that-puts-your-site-on-my-homepage"
author: "Karanga Oliver"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 12:33:36 +0000"
description: "Every side project I have launched hit the same wall. The site works, it looks fine, and then nobody shows up. The usual advice is "share it with your friend..."
keywords: "you, your, link, site, referral, race, homepage, get"
generated: "2026-10-19T12:42:59.622914"
---

# I built a free referral race that puts your site on my homepage

## Overview

Every side project I have launched hit the same wall. The site works, it looks fine, and then nobody shows up. The usual advice is "share it with your friends", but when you do, you get a polite thumbs up and that is about it. So I tried to fix that one problem, and the result is ViralRefer, which launched on TinyLaunch today. The idea What if sharing your link was a game with a visible prize? Your friends would have a reason to tap it, and you would have a reason to keep sending it. ViralRefer is a free referral race. The prize is not cash. It is space on the ViralRefer homepage itself. How the race works You tap Get my referral link . No signup and no email. You get a code that looks like VIRAL-XXXXXXX in about 30 seconds. You paste your website into the Site Drop slot. It appears on the homepage as a 15 minute "Just entered" chip. You send your link anywhere: texts, group chats, social posts. When a friend opens your link and taps Get my link , that counts as a verified referral and your site climbs the ladder: 1 verified friend: a 1 hour Rising card 2 friends: your site in this week's text line Board #2 and #3: the Challenger strip under the banner This week's #1 with 3 friends: a 7 day homepage banner Decisions I am glad I made No accounts. Every signup form loses people. Since the only thing a racer needs is a link and a place to put their website, I skipped accounts completely. Only one action counts. A referral counts only when a friend taps "Get my link" on your link. Page visits and copied links never count. That one rule removes most of the ways a leaderboard gets gamed. Traffic exchanges are off by default. Visits that come through traffic exchange style pages do not write a verified credit unless I deliberately turn that on, and it is off. Rewards at every rung. If only #1 wins, everyone else quits on day one. Giving the first rung a 15 minute spot and the first verified friend a 1 hour card means people see their site on the page right away, which is the moment that makes them want to send the link again. Weekly reset. The board runs on a UTC week, so there is always a fresh race and a new #1 to chase. The stack The whole thing runs on Cloudflare Workers with static assets served by the same Worker. It is a small setup, which matters a lot when you are one person maintaining it. What I would love feedback on Is the ladder clear the first time you land on the homepage? Would you send your link to a friend? If not, what is stopping you? What reward would make the race more fun? If you want to try it, grab a link at viralrefer.app . It is live on TinyLaunch today too: tinylaunch.com/launch/22546-viralrefer . If you like it, an upvote there helps a lot. Thanks for reading. I am happy to answer questions in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vrposter57/i-built-a-free-referral-race-that-puts-your-site-on-my-homepage-f45

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
