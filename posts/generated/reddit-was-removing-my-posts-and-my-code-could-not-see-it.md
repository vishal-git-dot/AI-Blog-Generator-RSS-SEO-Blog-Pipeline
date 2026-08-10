---
title: "Reddit was removing my posts and my code could not see it"
slug: "reddit-was-removing-my-posts-and-my-code-could-not-see-it"
author: "Michael Yousrie"
source: "devto_python"
published: "Mon, 10 Aug 2026 18:03:23 +0000"
description: "I spent this week posting to Reddit through the API and being pleased with how it was going. Every submission returned a URL. Every URL loaded. Four of the l..."
keywords: "you, reddit, karma, not, have, one, your, none"
generated: "2026-08-10T19:03:47.543866"
---

# Reddit was removing my posts and my code could not see it

## Overview

I spent this week posting to Reddit through the API and being pleased with how it was going. Every submission returned a URL. Every URL loaded. Four of the last six were gone and I had no idea. If you automate anything against Reddit, this is the part nobody tells you. A removed post looks completely fine to its author This is the whole problem in one sentence. Reddit does not show you your own removals. Load your post while logged in as the account that made it and you get the title, the body, the score, the comment count. It looks like a post. It is not visible to anybody else. The fix is to read it back with an anonymous client. Same credentials, no user context: import praw # app-only: no username, no password anon = praw . Reddit ( client_id = CLIENT_ID , client_secret = CLIENT_SECRET , user_agent = " removal-check by u/yourname " , ) anon . read_only = True s = anon . submission ( id = " abc123 " ) removed = s . removed_by_category is not None or s . selftext in ( " [removed] " , " [deleted] " ) Two things to note. You need both checks: selftext goes to [removed] in some cases and stays intact in others, while removed_by_category is populated in cases where the body still reads normally. And this only works anonymously. Run the same code with username= and password= set and you will cheerfully report that everything is fine. I also tried a plain HTTP request to reddit.com/user/<name>/about.json as a shadowban check. Don't bother from a server: it returns 403 for datacenter IPs regardless of account state, so you will diagnose a shadowban that isn't there. The app-only PRAW client is the one that tells the truth. removed_by_category is four different stories This field is the useful one and its values are not interchangeable: value who did it what it means automod_filtered AutoModerator a rule, usually with a bot comment explaining it moderator a human someone looked and said no reddit Reddit itself the sitewide spam filter deleted the author not a removal automod_filtered is the friendly one. AutoModerator almost always leaves a comment saying exactly what tripped, and those comments are the only place some rules are ever published. One of mine came back with "you need at least 3 karma earned in this subreddit to post here", a threshold that appears in no rules API, no sidebar, and no flair list. Read those comments; they are documentation. moderator means a person decided. No appeal in code. reddit is the one that should stop you. It isn't about your post, it's about your account. A subreddit rule is a local problem you can fix by writing differently. The sitewide filter deciding your submissions look like spam is a global one, and posting more into it is how it gets worse. The numbers that made me stop Once I could actually measure it: last 6 submissions: 4 removed (2 of them by `reddit`) last 8 comments: 8 live Posting was dead. Commenting was perfectly healthy, and the comment karma was still going up. Those are two completely different signals from the same account on the same day, and I would have guessed the opposite: I assumed comments were riskier because they carry links more often. So the rule I now follow: if the site filter is touching your submissions, stop submitting and keep commenting. Comments are what rebuild standing anyway. The bug that made all of this invisible I had a guard for part of this already. It never fired once. Subreddits can require a minimum comment karma earned in that subreddit before they accept a post. Reddit exposes this: karma = { sr . display_name . lower (): v [ " comment_karma " ] for sr , v in reddit . user . karma (). items ()} And my gate did roughly: have = karma . get ( sub_name ) if have is None or have >= threshold : return None # allow Read that carefully. user.karma() returns only the subreddits where you have karma . A subreddit you have never commented in is not in the dict at all. So in the exact case the gate exists for, a sub you have never participated in, have is None , and None was being treated as "cannot measure, allow it". Absent meant zero. The code read it as unknown. The fix distinguishes the two states properly: karma = fetch_karma () if not karma : return None # the CALL failed: genuinely unknown have = karma . get ( sub_name , 0 ) # absent from a good response: zero if have >= threshold : return None A missing key means "not present in the result". Whether that means zero or unknown depends entirely on whether the call succeeded, and only your code knows that. Same shape as a COUNT(*) returning no row versus returning 0, or a metrics endpoint that omits idle counters. If you branch on is None you are usually collapsing those two into one, and the failure is silent because the code takes the permissive path. Mine had never fired. It was written specifically to prevent a removal, it sat in the pipeline looking reassuring, and the removal it was written for happened anyway. What I'd tell past me Read your own posts back anonymously, on a schedule, rather than when you get suspicious. And treat removed_by_category == "reddit" as a stop signal, not a data point to log. The guard thing still bothers me though. It had never failed, and I read that as it working.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/michael-yousrie/reddit-was-removing-my-posts-and-my-code-could-not-see-it-1bkm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
