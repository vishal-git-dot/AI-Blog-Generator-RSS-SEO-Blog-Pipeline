---
title: "Reading a 62 to 0 Hindsight Result Honestly"
slug: "reading-a-62-to-0-hindsight-result-honestly"
author: "vivek manepalli"
source: "devto_python"
published: "Tue, 29 Sep 2026 12:20:21 +0000"
description: "A score of 62 to 0 looks too clean, so before I put it in a post I wanted to know what it actually says. Our review agent, with Hindsight memory on, repeated..."
keywords: "memory, comments, not, category, run, pull, accepted, rejected"
generated: "2026-09-29T12:30:40.035076"
---

# Reading a 62 to 0 Hindsight Result Honestly

## Overview

A score of 62 to 0 looks too clean, so before I put it in a post I wanted to know what it actually says. Our review agent, with Hindsight memory on, repeated 0 rejected kinds of feedback across 21 real pull requests. Without memory it repeated 62. This article covers how I tested that number, where it is weak, and what I would and would not claim from it. The setup in one paragraph The Review Desk is a code review agent. It reads a pull request diff and posts comments under the lines they refer to. A person accepts or rejects each comment, and every decision is stored in Hindsight with retain. Before the next review, the agent recalls those decisions. For the test I replayed 21 merged pallets/flask pull requests in merge order, twice: once with memory off and once with memory on, each with a fresh memory bank. A script played the reviewer. It accepts comments about security, validation, error handling and bugs, and rejects everything else. A repeat rejection is a comment in a category the script had already rejected earlier in the same run. What I measured Memory off Memory on Comments generated 96 47 Repeat-rejected 62 0 Accepted 29 39 Acceptance rate 30% 83% The running totals of repeat rejections were 9 against 0 after 5 pull requests, 24 against 0 after 10, and 59 against 0 after 20. So the gap opens early and keeps growing, which is what you would expect if memory is doing the work. Check one: an earlier run Before this run I did a smaller one on 10 pull requests. It is a different set of pull requests, so it is a second look and not a repeat of the same test. Memory off Memory on Comments generated 51 21 Repeat-rejected 26 0 Accepted 18 14 Acceptance rate 35% 67% Repeat rejections went to 0 again. That is the number I trust, because it is counted against a fixed rule. Check two: the accepted counts Now look at the accepted row in both tables. In the 10-pull-request run, accepted comments went down with memory, from 18 to 14. In the 21-pull-request run they went up, from 29 to 39. They moved in opposite directions, so I do not claim that memory raises or lowers accepted comments. The acceptance rate is a bigger trap. It is 83% with memory partly because memory cut the total number of comments roughly in half. Fewer comments in the denominator makes any rate look better. If you only quote the rate, you are quoting an effect of the comment count. I would rather quote repeats. Check three: what the replay did and did not use The 62 to 0 result came from replay_real.py , which uses Hindsight recall only. The live app does more. It keeps a decision log with a category for every decision, builds category rules from it, and puts those rules first in the prompt, ahead of the recalled notes. Those rules were not part of the measured replay. I also saw that Hindsight can store a rejection as a narrow fact, for example "rejected a docstring on the load function". I added the category rules to the live app because of that. I want to be plain that I cannot fully connect these two things from one run. The replay used recall only and still finished at 0 repeats, and the narrow-fact behavior is the reason I added rules on top. Repeated runs would tell us more about how often it matters. The rule the script uses to decide accept or reject is short. This is the real code: # Scripted "team persona": these categories get accepted, the rest rejected. ACCEPT = { " security " , " validation " , " error_handling " , " bug " } # ... accepted , rejected , repeats = 0 , 0 , 0 for c in comments : ok = c [ " category " ] in ACCEPT if ok : accepted += 1 else : rejected += 1 if c [ " category " ] in rejected_before : repeats += 1 # ... rejected_before |= { c [ " category " ] for c in comments if c [ " category " ] not in ACCEPT } What would make the result stronger Several runs per arm, so I can report a range and not a single number. A real reviewer, or several, in place of the script. Real people are inconsistent, and I have not tested that. Counts per category, to see which kinds of feedback memory suppresses fastest. A run of the live app, with the decision-log rules on, measured the same way. Limits One run per arm. Model output varies, and with a single run I cannot give a range. The team was a script. The comments are model output and unverified. Inline placement is approximate, and at least one security comment about the Host header is a stretch. None of them are confirmed Flask bugs. Category labels drift a little between runs. Hindsight needs about ten seconds to process a retain, so the app tells people to wait before the next review. Decisions are stored in a plain text file, data/decisions.json , with no encryption at rest. Comments show in the UI. They are not posted back to the pull request on GitHub. Takeaways Pick the metric you can count against a rule. Repeat rejections were countable. Acceptance was not clean. When a number moves in opposite directions between runs, stop quoting it. Say which part of the system a result came from. Ours came from recall only. Keep the second run, even when it is smaller. It is the only reason I believe the first. Try it The code is at github.com/abhiram0411/review-desk . A read-only copy with the measured results is at review-desk-z659.onrender.com . It runs on a free host, so the first load can take a minute or two. The Hindsight docs explain the retain and recall calls I used, and the agent memory page on Vectorize gives the wider background. Tagging Code.in .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vivek1111/reading-a-62-to-0-hindsight-result-honestly-2kn1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
