---
title: "How a three-label softmax router accepted a soup recipe as notes"
slug: "how-a-three-label-softmax-router-accepted-a-soup-recipe-as-notes"
author: "十方空烬 · Ember ☄️"
source: "devto_python"
published: "Mon, 16 Nov 2026 05:33:52 +0000"
description: "I kept this failure in the fixed commit bd2a30de287fe419b7d31838b40f5ae4d2d70061 . "Suggest a soup recipe." does not belong to weather, calendar, or notes, b..."
keywords: "accepted, ood, rows, not, threshold, label, recipe, notes"
generated: "2026-11-16T05:48:00.879479"
---

# How a three-label softmax router accepted a soup recipe as notes

## Overview

I kept this failure in the fixed commit bd2a30de287fe419b7d31838b40f5ae4d2d70061 . "Suggest a soup recipe." does not belong to weather, calendar, or notes, but the saved test prediction for ood-template-4-en has top_route equal to notes, a maximum of 0.486, and accepted true at the 0.4 threshold. This package is small. It turns text into 4,096-dimensional character n-gram counts, applies a linear transform and three-way softmax, and was fit on 96 author-written training records for one 300-epoch CPU run. The 204 synthetic records split into 96 training, 54 validation, and 54 test; the original templates are written and visible to me, so these records were not handled as a human-blind benchmark. The mechanism sits in the softmax denominator. router.py sets confidence to the largest softmax value, then accepts when confidence >= threshold ; below threshold, route is null. Because the three probabilities sum to one, the maximum cannot fall below about 1/3. That lower bound is arithmetic, neither a calibrated probability nor a membership certificate. The recipe's notes score of 0.486 is only about 0.152 above a uniform 1/3. It clears 0.4 because the model slightly prefers notes and the threshold is exactly 0.4. I have not run per-feature attribution, so I cannot say which words pushed notes to the top. The threshold came from a fixed rule. validation-thresholds.json shows that a candidate needed validation accepted precision of at least 0.9, then the chosen threshold was the one with the most correct accepted rows. At 0.4, validation had 44 correct among 47 accepted; 0.5 and 0.6 were also feasible but accepted far fewer. This is empirical selection, not calibration. At 0.4, validation accepted 3 of its 6 OOD rows. On test, test-report.json gives known top-1 44/48, acceptance 52/54, accepted precision 43/52, and OOD false acceptance 6/6. The 52 accepted rows split into 6 OOD plus 46 known rows. Among those 46 known rows, 43 are top-1 correct and 3 are top-1 wrong yet accepted. Two known rows were rejected: one correct and one wrong. The drop to 43/52 therefore combines six OOD accepts and three known wrong accepts, not a single OOD effect. Run this block directly at the package root. It reads saved test-predictions.jsonl with the Python 3 standard library only, and it does not retrain, infer again, or touch the network: python3 - << 'PY' import json with open ( 'test-predictions.jsonl' , encoding = 'utf-8' ) as f: rows = [ json.loads ( line ) for line in f if line.strip ( ) ] recipe = next ( x for x in rows if x [ 'id' ] == 'ood-template-4-en' ) ood = [ x for x in rows if x [ 'label' ] == 'ood' ] known_accepted = [ x for x in rows if x [ 'label' ] != 'ood' and x [ 'accepted' ] ] known_rejected = [ x for x in rows if x [ 'label' ] != 'ood' and not x [ 'accepted' ] ] print ( json.dumps ( { 'recipe_row' : { k: recipe [ k ] for k in ( 'id' , 'top_route' , 'probabilities' , 'threshold' , 'accepted' , 'reason' ) } , 'ood_total' : len ( ood ) , 'ood_accepted' : sum ( x [ 'accepted' ] for x in ood ) , 'test_accepted_total' : sum ( x [ 'accepted' ] for x in rows ) , 'test_known_accepted_correct' : sum ( x [ 'accepted' ] and x [ 'top_route' ] == x [ 'label' ] for x in rows if x [ 'label' ] != 'ood' ) , 'known_accepted_total' : len ( known_accepted ) , 'known_accepted_correct' : sum ( x [ 'top_route' ] == x [ 'label' ] for x in known_accepted ) , 'known_rejected_total' : len ( known_rejected ) , 'known_rejected_correct' : sum ( x [ 'top_route' ] == x [ 'label' ] for x in known_rejected ) , } , ensure_ascii = False, indent = 2 ) ) PY If NumPy 2.5.4 is installed from requirements.txt , replay one CPU inference in the same directory: python router.py model.json "Suggest a soup recipe." The package boundary matters too. It is a local NumPy CPU command-line model, with no hosted App and no Transformers or inference Provider integration that I have verified; it never executes a weather, calendar, or notes action. For reuse, the code, synthetic data, and trained weights are released under Apache-2.0, copyright Renchao Wu. NumPy is installed separately, not vendored, and its own license terms apply as described in DEPENDENCIES.md . This example is useful because it separates two signals. With fixed classes and no explicit reject class, max softmax always gives an out-of-domain request a relative highest route. In a real chain, what matters is which branch a false accept enters and what that branch costs. If route is wired directly to a real note-saving branch, the recipe request may enter that path; the model package itself does not perform that step. Known-route accuracy and threshold precision are useful numbers, but neither alone says the routing is reliable. The data is small, with only three OOD test examples per language. The 20/24 and 24/24 known-route language counts do not support a language superiority claim or an open-world false-accept rate. This counterexample is bounded by the fixed model, data, and threshold rule, and it does not become a general theorem against all softmax abstention schemes. Author: Renchao Wu The model card page keeps the same failure note and local CPU command-line boundary. Its source page is WideChaos/char-router-abstention-study . English original .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/widechaos/how-a-three-label-softmax-router-accepted-a-soup-recipe-as-notes-104p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
