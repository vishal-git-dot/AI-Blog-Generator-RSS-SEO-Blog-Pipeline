---
title: "The golden set: 100 labelled examples as the acceptance test for an AI feature"
slug: "the-golden-set-100-labelled-examples-as-the-acceptance-test-for-an-ai-feature"
author: "Slava Kotenev"
source: "devto_ai"
published: "Sun, 01 Nov 2026 05:17:44 +0000"
description: "If you ask three people whether an AI feature "works", you will get three answers, each based on the last few examples they happened to see. A golden set rep..."
keywords: "items, you, set, every, not, real, run, start"
generated: "2026-11-01T05:26:23.417192"
---

# The golden set: 100 labelled examples as the acceptance test for an AI feature

## Overview

If you ask three people whether an AI feature "works", you will get three answers, each based on the last few examples they happened to see. A golden set replaces opinions with a number: a fixed collection of real inputs with agreed correct answers, run every time something changes. About a hundred items is enough to start. Why a hundred With 100 items, one mistake moves the score by one point, and you can still read every failure by hand. That is the point of the first set: not statistical perfection, but a measurement the whole team can inspect. As the feature matures you grow it; you do not start with thousands. A caution on precision: with 100 items the uncertainty is wide. A 95% score can plausibly hide a true rate anywhere from roughly 89% to 98%. Treat it as a tripwire, not a guarantee, and say so in the acceptance document. What goes into it Sample from real data from the process, not from examples someone invented. Then deliberately cover: The typical case , in proportion to how common it is (most of the set). The boring variations : different phrasings, formats, languages, typos. Known hard cases : the pairs people confuse, the odd layouts. Things that must be refused or escalated : out-of-scope questions, missing fields, items the system should hand to a human. A few adversarial ones : instructions hidden in the input, empty input, absurdly long input. Tag each item with its category so you can report per-category results, not just one average that hides a weak spot. Who labels it The process owner, or someone they trust, decides the correct answer. Two people labelling independently, then discussing disagreements, finds the ambiguous items early. Ambiguity found at this stage is a requirements problem, and it is cheaper to fix now than after launch. How to use it Freeze it. The set is not training data. Never tune on it after you start reporting from it, or the score only reflects what you memorised. Run it on every change : a new prompt, a new model version, a new threshold. Write the pass bar before the first run , as a number per category. Example: "at least 95% correct on automated items, and every must-refuse item refused". Read the failures , all of them. Each one is either a bug, a labelling error, or a missing rule. Keep a changelog of scores per version so regressions are visible. A minimal runner is a few lines: def evaluate ( system , items ): results = [( it , system ( it [ " input " ])) for it in items ] ok = [ r for it , r in results if r [ " answer " ] == it [ " expected " ]] return len ( ok ) / len ( items ), [ it for it , r in results if r [ " answer " ] != it [ " expected " ]] Refresh it slowly Every month or so, add 10 to 20 fresh real items, especially ones that came out of the review queue as corrections. Retire items that no longer reflect the process. Keep a separate untouched holdout if you tune a lot. Takeaways Start with about 100 real, labelled items. Cover typical, hard, and must-refuse cases and tag them. Freeze it, write the pass bar first, run it on every change. Be honest about the uncertainty that comes with a small set. Portfolio and contacts: @Kotenev01_bot . I write about practical, measurable AI adoption for business: demos on test data, no invented case studies. Telegram channel: @kotenev01_en

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/slava_kotenev_159/the-golden-set-100-labelled-examples-as-the-acceptance-test-for-an-ai-feature-k5m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
