---
title: "I checked what 31 big websites tell AI crawlers in robots.txt, and found a bug in my own tool"
slug: "i-checked-what-31-big-websites-tell-ai-crawlers-in-robotstxt-and-found-a-bug-in-my-own-tool"
author: "Alba LM"
source: "devto_python"
published: "Thu, 05 Nov 2026 22:59:19 +0000"
description: "Can ChatGPT, Claude or Perplexity read your website? The first place to look is a small text file: robots.txt . I wanted to see what big websites actually sa..."
keywords: "sites, txt, bot, page, user, block, what, robots"
generated: "2026-11-05T23:29:11.049131"
---

# I checked what 31 big websites tell AI crawlers in robots.txt, and found a bug in my own tool

## Overview

Can ChatGPT, Claude or Perplexity read your website? The first place to look is a small text file: robots.txt . I wanted to see what big websites actually say in it, so I picked 40 well-known sites and audited their home pages for 12 AI crawlers. The results split much more cleanly by industry than I expected. The study also found a bug in my own tool. More on that below, because it's a mistake you could easily make too. What I measured On 5 November 2026 I ran PageSignal , the AI visibility API I built, against the home pages of 40 sites: news, e-commerce, SaaS and developer tools, and reference sites. 31 sites gave usable results. 9 sites could not be audited. Most answered with an anti-bot wall, two timed out, and one page was over my 2 MB limit. I split the crawlers into two groups, because they do different jobs: AI search and assistant bots (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User): they fetch pages to answer people. AI training bots (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot, meta-externalagent): they collect content for training models. The results Group Sites audited Block at least one AI search or assistant bot Publish llms.txt News 6 6 0 E-commerce 8 2 2 SaaS and dev tools 10 0 9 Reference 7 2 1 Total 31 10 12 Across all 31 sites: 10 block at least one AI search or assistant bot on their home page. 13 block at least one AI bot of any kind. Three of them (AliExpress, Figma and Notion) only block training bots. 18 block none of the 12 crawlers. The 10 sites that block at least one search or assistant bot were The Guardian, BBC, Reuters, The Verge, TechCrunch, Wired, Amazon, eBay, Reddit and IMDb. Reuters, Reddit and IMDb are a special case. Their general User-agent: * rules close the home page to any bot without its own rules, so this isn't always AI-specific. Reddit's file ends like this: User - agent : * Disallow : / The pattern: publishers close, software companies open All 6 news sites block at least one bot that fetches pages to answer people. None of the 10 SaaS and developer tool companies do, and 9 of those 10 publish an llms.txt file, while no news site does. My guess, and it's only a guess, is that this comes down to the business model. A publisher sells its content, so an AI answer can replace the visit. A software company sells a product, so being mentioned in an AI answer works like free marketing. Neither choice is automatically right. Blocking is often deliberate. The thing to avoid is blocking by accident, for example with a security rule or a template nobody remembers adding. The bug in my own tool My first run said Figma was blocking AI search bots. I double-checked before writing that here, and it was wrong. PageSignal was using Python's built-in urllib.robotparser . It's convenient, but I found two behaviours that don't match the robots.txt standard, RFC 9309 : 1. It doesn't understand $ , the end-of-URL marker. from urllib.robotparser import RobotFileParser parser = RobotFileParser () parser . parse ( """ User-agent: OAI-SearchBot Allow: /$ Disallow: / """ . splitlines ()) print ( parser . can_fetch ( " OAI-SearchBot " , " https://example.com/ " )) # False, should be True Under the standard, the most specific matching rule wins, so Allow: /$ opens the home page. That's how Figma's file is written. 2. It can apply the wrong group when one bot name is contained in another. parser = RobotFileParser () parser . parse ( """ User-agent: Applebot Allow: / User-agent: Applebot-Extended Disallow: / """ . splitlines ()) print ( parser . can_fetch ( " Applebot-Extended " , " https://example.com/ " )) # True, should be False The rule for Applebot gets applied to Applebot-Extended . This made my tool miss a real block on The Verge, Reuters and IMDb. In total, 4 of the 32 sites audited in that first run had wrong crawler results. I replaced the parser with a small RFC 9309 matcher and checked the numbers in this post against a separate implementation. They match. If you read robots.txt with urllib.robotparser (tested on Python 3.12), it's worth testing these two cases. What this study doesn't prove It's a small, hand-picked sample. It shows a pattern in these sites, not the whole web. It only looks at home pages. This matters: Figma opens its home page to AI search bots but closes /pricing to them. A page-level answer can differ from the rest of the site. It's one day's snapshot. These files change. robots.txt is a request, not a lock. It shows what a site asks for, not what each company's crawler really does. Being readable doesn't mean being cited. Passing these checks gives an AI bot access. It can't guarantee a mention. A file doesn't show the whole relationship. A publisher may also have a licensing deal that robots.txt doesn't reveal. Check your own site Look at yoursite.com/robots.txt and search for the bot names above, then look at the User-agent: * block. Check the pages you care about, not only the home page. Also look at your page without JavaScript. Many AI crawlers don't run it, so a page built entirely in the browser can look almost empty to them. If you'd rather not do it by hand, there's a free live demo with no signup. For automated checks, the API is on RapidAPI and API.market . Did you decide on purpose what your robots.txt says about AI crawlers, or is it just whatever your template shipped with? I'd love to hear what you found.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alorenzom/i-checked-what-31-big-websites-tell-ai-crawlers-in-robotstxt-and-found-a-bug-in-my-own-tool-20o6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
