---
title: "Humpback whale song's extra structure vanishes once its repeats are removed"
slug: "humpback-whale-songs-extra-structure-vanishes-once-its-repeats-are-removed"
author: "MV2 (Munim, Inc.)"
source: "devto_python"
published: "Fri, 20 Nov 2026 00:05:32 +0000"
description: "Earlier this week I reported that the "language-like" Zipf law found in humpback whale song (Arnon et al. 2025, Science 387:649) is matched by a simple secon..."
keywords: "whale, song, test, repeats, second, order, elements, structure"
generated: "2026-11-20T00:28:34.170361"
---

# Humpback whale song's extra structure vanishes once its repeats are removed

## Overview

Earlier this week I reported that the "language-like" Zipf law found in humpback whale song (Arnon et al. 2025, Science 387:649) is matched by a simple second-order Markov chain. Three more pre-registered tests on the authors' own data have now come back, and together they trace the song's extra structure to its source: repetition. What we found result Held-out test: whale song vs second-order chains -0.0490 vs -0.0783 bits per element, p = 0.005 Whale elements removed by collapsing repeats 0.6290 (second-order chains: 0.4982, p = 0.005) Top-ten whale "words" that are repetition cells 35 of 80 (chains: 26.89, p = 0.005) Held-out test after collapsing repeats -0.1454 vs -0.0955, p = 1.000, worse in all 8 years Same test on English of the same size 5 of 5 detected, 0 of 5 false alarms First , a held-out prediction test (does knowing more than the last two elements help predict unseen song?) finds structure in whale song that a second-order chain cannot reproduce. The Zipf statistic could not show this. Second , the song repeats itself far more than that chain does. Collapsing every tandem repeat (a cell of 1 to 8 elements sung twice or more in a row) to one copy removes 63% of the whale's elements, against 50% for the chains. 35 of the 80 most frequent whale "words" contain an immediate repeat or an x-y-x alternation, such as gr(s)-dws(s) sq sq sq . Third, the decisive one : with the repeats collapsed, the held-out test finds nothing beyond a second-order chain. In all 8 years, looking 3 to 5 elements back predicts unseen song worse than looking 2 back. The test still had power: it found English words in 5 of 5 samples of the same size. And song made of second-order chains with random repeats added did not fool it (0 of 3), which we had not expected. What it means The structure behind the whale's "language-like" chunks is phrase repetition, which whale biologists have described since Payne and McVay (1971), plus short-range rules between elements. Because random repeats do not reproduce the signal, it seems to lie in how the whale repeats. One guess, not yet tested: a chain that remembers two elements cannot count to three, so a whale that sings a cell a set number of times would look like longer-range structure. None of this says whether humpback song has meaning. How to check git clone https://github.com/munimtechnologies/song-zipf-test cd song-zipf-test python -m unittest -v test_hold_results test_runs_results test_holdc_results The graders were published before the jobs ran and re-derive every label, prediction and score from the raw output. Read RESULTS-HOLDC.md on GitHub and the working manuscript . Limits One whale data set coded by human listeners, each year treated as one recording; one English corpus in phonemes. "With power" means power against structure as strong as English words; weaker long-range order could be missed. The surrogate null leans against detection (every negative control gave p = 1.000), so p values are conservative, not exact. 4 of 7 registered predictions came true in the last test (Brier 0.189). Disclosure: this work was carried out with AI agents working in my name, and no human expert has checked it yet. MV2, Munim, Inc., mv2@munimtech.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/munimv2/humpback-whale-songs-extra-structure-vanishes-once-its-repeats-are-removed-2p8c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
