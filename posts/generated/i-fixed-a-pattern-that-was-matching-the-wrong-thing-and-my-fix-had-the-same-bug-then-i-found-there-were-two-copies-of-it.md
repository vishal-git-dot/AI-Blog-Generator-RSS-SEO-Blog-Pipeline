---
title: "I fixed a pattern that was matching the wrong thing, and my fix had the same bug. Then I found there were two copies of it"
slug: "i-fixed-a-pattern-that-was-matching-the-wrong-thing-and-my-fix-had-the-same-bug-then-i-found-there-were-two-copies-of-it"
author: "Blueticks"
source: "devto_webdev"
published: "Wed, 26 Aug 2026 01:30:22 +0000"
description: "I have a small tool that decides whether a website sells a product of its own. The question matters to me because I write to editors about a measurement I pu..."
keywords: "had, site, same, two, not, one, pattern, link"
generated: "2026-08-26T01:41:06.768046"
---

# I fixed a pattern that was matching the wrong thing, and my fix had the same bug. Then I found there were two copies of it

## Overview

I have a small tool that decides whether a website sells a product of its own. The question matters to me because I write to editors about a measurement I published, and writing to a company that sells a competing tool is a waste of everyone's time. The test is crude and it works: look for a link on their own domain whose path is pricing, or plans, or the same word in a couple of other languages. It threw out a site I wanted to keep. The link it had found was a blog tag archive whose slug happened to be the word pricing. Sixty posts filed under that tag, none of them a price list. The site sells nothing. It writes about what other people charge, which makes it exactly the kind of place I was looking for. So I fixed it: ignore any link whose path sits under a blog, a tag, a category, an archive. The fix had the bug it was fixing Two hours later the same tool threw out another site. Same reason, different path: the link was a category archive, and my new filter had not caught it. I had written the filter to match the word followed by a slash. The path on that site spelled it out in full, with a letter between the word and the slash. My pattern required the boundary to fall exactly where it happened to fall on the first site, and I had verified it on that one site. That is the part I want to keep. The correction and the defect were the same shape: a pattern that matched one real example and was assumed to describe the class . I had just written a note explaining that mistake, and then made it inside the note's own fix. The bug I had not even reached yet I widened the pattern, re-ran the test, and the site was still thrown out. The tool reads two pages, not one. It reads the article, and if it finds no pricing link there it follows the site's about page and looks again, because a site can keep its price list one click from the front door. I had added that second reading the day before. It carries its own copy of the pattern , and I had corrected only the first. The verdict line had been telling me this the whole time. When the link comes from the second reading it gets printed twice, because of how the two results are merged. I read that line three times, in three separate attempts, and never asked why the same address appeared twice on it. What I actually take from this A duplicated pattern is not a style problem, it is a correctness problem with a delay fuse. Both copies were right when I wrote them. The first correction made them disagree, and nothing in the system could notice a disagreement between two literals sitting forty lines apart. I could deduplicate them, and I will. But the more useful habit is smaller: when a fix does not take effect, the next question is not what is wrong with the fix. It is whether the thing I fixed is the thing that ran. There is also a plainer lesson about verification. I tested the first correction on the example that motivated it, which proves nothing about a class. The second time I tested on two examples pulling in opposite directions: one that should now pass, one that must still fail. That is what finally showed the second copy, because the case that should have passed did not. Disclosure I build BlueTicks for Gmail, a Chrome and Firefox extension that shows WhatsApp style ticks in your Gmail sent list, one tick sent and two blue ticks opened. It costs 4 dollars a year, and the free tier covers 30 emails a month. Everything above comes from distributing it in public and writing down what the measurements did. You can find it at blueticks.io . The site that started all this is now a live target with a letter written for it. It nearly went in the bin twice, for the same wrong reason, corrected the wrong way.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blueticks/i-fixed-a-pattern-that-was-matching-the-wrong-thing-and-my-fix-had-the-same-bug-then-i-found-367l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
