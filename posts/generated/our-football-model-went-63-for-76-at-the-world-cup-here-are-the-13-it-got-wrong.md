---
title: "Our football model went 63-for-76 at the World Cup. Here are the 13 it got wrong."
slug: "our-football-model-went-63-for-76-at-the-world-cup-here-are-the-13-it-got-wrong"
author: "Waqas R"
source: "devto_python"
published: "Sun, 12 Jul 2026 13:04:48 +0000"
description: "Most football prediction sites publish a hit rate. Almost none publish their losses. So this post was going to be the evidence: every prediction our model ma..."
keywords: "model, our, not, record, group, you, brazil, prediction"
generated: "2026-07-12T13:38:55.216929"
---

# Our football model went 63-for-76 at the World Cup. Here are the 13 it got wrong.

## Overview

Most football prediction sites publish a hit rate. Almost none publish their losses. So this post was going to be the evidence: every prediction our model made at the 2026 World Cup, graded, including the thirteen it got wrong. Then, while assembling it, I found a bug in our own receipts. That turned out to be the more useful post, so you get both. The record: our model's favourite came through in 63 of 76 decisive matches. 82.9%. In the knockouts, its favourite advanced in 20 of 24 ties. The full graded record is public at onsidearena.com/model-record , the raw data is free to reuse under CC BY 4.0 at onsidearena.com/data , and the method is at onsidearena.com/methodology . The 13 misses Round Result We favoured Group Ghana 1-0 Panama Panama Group South Africa 1-0 South Korea South Korea Group Australia 2-0 Turkiye Turkiye Group Ivory Coast 1-0 Ecuador Ecuador Group Turkiye 0-1 Paraguay Turkiye Group Norway 3-2 Senegal Senegal Group Bosnia & Herzegovina 3-1 Qatar Qatar Group Ecuador 2-1 Germany Germany Group Turkiye 3-2 United States United States R32 Germany 1-1 (pens 3-4) Paraguay Germany R32 Netherlands 1-1 (pens 2-3) Morocco Netherlands R16 Brazil 0-2 Norway Brazil R16 Colombia 0-0 (pens 3-4) Switzerland Colombia Norway 2-0 Brazil is the one I'd most like back. The bug: our receipts were not receipts Here is the part worth your time. I wanted to publish each miss with the probability we had assigned before kickoff — because being wrong at 51% and being wrong at 78% are completely different failures, and a scorecard that hides which is which is laundering a bad model. So I went to pull those numbers. And two of our own pages disagreed: /model-record -> Brazil at 64% /world-cup-2026/model-record -> Brazil at 71% Same match. Same model. Two different numbers, live, at the same moment. The cause: we never stored the pre-match probability. Our knockout receipts table stores the fixture, the favourite we picked, and what actually happened. It does not store the number. So every time the page renders, the probability is recomputed from scratch . That would be merely sloppy, except for what it recomputes against. Our engine applies an online isotonic calibration layer that is refitted as real results land. Which means the probability now being displayed for Brazil vs Norway is computed by a calibration map that has already seen Brazil vs Norway. That is textbook leakage, and it is in the one artifact whose entire purpose is to be trustworthy. A receipt you recompute is not a receipt. It's a re-enactment. What is and isn't sound I want to be precise about what survives this, because "we found a bug" is not a licence to throw out everything. Sound: the 63-of-76 record. The favourite's identity is stored, the result is a matter of public record, and the grading question ("did our pick come through?") is binary and was fixed in advance. That number is real and you can check it. Not sound: any probability we attach to a past match retrospectively. So this post does not print them, and we are pulling them from the receipts pages until they are stored properly. The honest version of our claim is therefore weaker and more specific than the one I set out to write: we called the favourite correctly in 82.9% of decisive matches . Not "and here's exactly how confident we were, match by match" — because we did not write that down, and reconstructing it after the fact would be inventing evidence. The fix Store the prediction at prediction time. That's it. That's the whole lesson, and it is embarrassing precisely because it is so obvious. Concretely, for the Premier League season starting 21 August, every prediction gets written to an append-only row before the deadline , containing the probability, the model version, and a timestamp. Nothing about a past prediction is ever recomputed. If we change the model, old rows keep the old numbers, because those are what we actually said. If you are building anything that makes public claims about its own accuracy, the test is simple: Can you regenerate your past predictions from your current code? If yes, they are not receipts. Your model has read the answers. We failed that test. We're fixing it in the open, which is roughly the point of the exercise. The data Free to download, cite and reuse under CC BY 4.0: The graded record — every call and every result: onsidearena.com/model-record The raw data : onsidearena.com/data The methodology : onsidearena.com/methodology If you spot another hole in our grading, I would genuinely rather hear it than not. That's the whole trade: you get to check us, and in exchange the number means something. The same engine now points at Fantasy Premier League, currently at 0.86 mean absolute error across 51,518 out-of-sample predictions . The season starts 21 August. This time the predictions get written down first.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/waqas_r_47bca4fef1922623d/our-football-model-went-63-for-76-at-the-world-cup-here-are-the-13-it-got-wrong-1dk6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
