---
title: "My AI agent keeps a list of how it fools itself"
slug: "my-ai-agent-keeps-a-list-of-how-it-fools-itself"
author: "Stephan Holzbach"
source: "devto_ai"
published: "Wed, 30 Sep 2026 12:09:42 +0000"
description: "I run Postservice.at with the help of a small team, a business address and mail service in Vienna with more than 1,000 customers. I'm a founder, not a develo..."
keywords: "one, agent, new, list, every, not, wrong, check"
generated: "2026-09-30T12:15:50.061646"
---

# My AI agent keeps a list of how it fools itself

## Overview

I run Postservice.at with the help of a small team, a business address and mail service in Vienna with more than 1,000 customers. I'm a founder, not a developer. This year a large part of our work runs through Claude Code: the website, content, deployments, reports and a good share of the back office. The most useful thing we built in that time is not a feature. It's a section in the project's CLAUDE.md called "How I fool myself". Every time the agent reported something that turned out to be wrong, the mistake went into that list, with the date and what was really going on. Every new session reads it before it touches anything. These are the entries that saved us the most time and nerves. 1. When a check finds a lot of problems, suspect the check One evening the agent reported 30 dead external links, 12 FAQ schema mismatches and tracking that fired before cookie consent. The real numbers: 3 dead links, 0 mismatches, no tracking problem. (And I didn't catch that at first and already had a full rework built...) The "dead" links were bot protection. One site answers scripts with 403 and browsers with 200, LinkedIn answers every bot with 999. The schema check replaced HTML tags with spaces, so UID-Prüfer: became UID-Prüfer : and the comparison failed. The consent test ran in a browser profile that had already accepted cookies in an earlier run. The rule now: before a finding gets reported, the check has to show it can fail. A known good case passes, a known broken case fails. Only then does the result count. 2. Make sure you measure the build you just made pkill -f "next start" matches nothing, because the process is called next-server . At one point ten orphaned servers were running, one of them holding port 3000 with a build that was two hours old. Three times in a row the agent concluded that its change "didn't work". pkill -f "next-server" ; sleep 2 npm run build && npm run start Plus a cache buster like ?v=2 in the browser, otherwise the headless browser shows the old page. 3. grep -c exits with 1 when it counts zero grep -c pattern file || echo "missing" prints "missing" whenever the count is zero, because grep returns exit code 1. That's how the agent once wrote "ContactForm.tsx no longer exists" into our docs. The component is used in eight places. 4. A replace that silently does nothing A scripted edit ran s.replace(old, new) against a line that started with } else if instead of else if . No match, no error, green build, change missing. Every scripted edit now checks first: assert s . count ( old ) == 1 s = s . replace ( old , new ) 5. One approval is one approval Everything goes to a preview branch first. Only an explicit "merge" from me moves it to production. On one busy day, after the first merge in the morning, the agent drifted into pushing straight to main. Sixteen times, including a new public tool I had never seen. Nobody decided that, it just happened. The rule now reads: a merge approval counts for exactly one batch. After the merge, back to a new branch, no exceptions. 6. Two lists will drift apart Our tool overview kept its own list of tools, the sitemap kept another one. A new tool was missing from the sitemap from its first day. Another route had 44 URLs hard-coded while the sitemap listed 199. One list, one file, everything else reads from it. A new route goes into the config file, not into the page that happens to use it. 7. A second agent that only checks Anything that goes live gets reviewed by a separate agent that did not write it: facts against sources, links, rendering on desktop and mobile. This week it caught two factual errors in an article about health startups in Vienna. One company was described as a spin-off of the wrong university, and a percentage was attached to the wrong base. The writing agent had read the same sources and missed both. What I'd tell another founder Put the failure modes where the agent reads them at the start of every session. What was said in yesterday's chat is gone. Ask for the check before you ask for the fix. Keep the decision to go live with a person. Expect the agent to be confidently wrong a few times a day. The list doesn't stop that. It makes sure it's wrong in new ways, not the same way twice. What's on your list? And also, do you think this will be a problem in the future, since AIs are getting smarter every day?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/postservice/my-ai-agent-keeps-a-list-of-how-it-fools-itself-34k9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
