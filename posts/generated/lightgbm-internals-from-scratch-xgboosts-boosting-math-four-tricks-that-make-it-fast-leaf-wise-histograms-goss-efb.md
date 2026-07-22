---
title: "LightGBM internals from scratch: XGBoost's boosting math, four tricks that make it fast — leaf-wise, histograms, GOSS, EFB"
slug: "lightgbm-internals-from-scratch-xgboosts-boosting-math-four-tricks-that-make-it-fast-leaf-wise-histograms-goss-efb"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Wed, 22 Jul 2026 08:29:56 +0000"
description: "XGBoost gave us a regularized second-order objective: a gradient gᵢ and Hessian hᵢ per sample, a closed-form leaf weight w* = −G/(H+λ) , and γ-gated gains. L..."
keywords: "leaf, split, gain, one, gradient, edges, lightgbm, def"
generated: "2026-07-22T08:36:37.032163"
---

# LightGBM internals from scratch: XGBoost's boosting math, four tricks that make it fast — leaf-wise, histograms, GOSS, EFB

## Overview

XGBoost gave us a regularized second-order objective: a gradient gᵢ and Hessian hᵢ per sample, a closed-form leaf weight w* = −G/(H+λ) , and γ-gated gains. LightGBM keeps that exact math — every leaf is still −G/(H+λ) , every split scored by the same gain — and rebuilds the parts that make it fast on big data . I built a demo that computes all four accelerators for real, and once you see them the speedup stops being magic. Here they are. The shared core is unchanged Nothing about the statistics is new. A leaf still collapses to two sums, and a split's gain is still the structure-score improvement. def leaf_weight ( G , H , lam ): return - G / ( H + lam ) # closed-form, L2-shrunk def split_gain ( GL , HL , GR , HR , lam = 0. , gamma = 0. ): sim = lambda g , h : g * g / ( h + lam ) G , H = GL + GR , HL + HR return 0.5 * ( sim ( GL , HL ) + sim ( GR , HR ) - sim ( G , H )) - gamma Leaf-wise growth — split the best leaf, not the whole level This is LightGBM's signature. XGBoost grows level-wise (breadth-first): fill each depth level before descending, so the tree stays balanced. LightGBM grows leaf-wise (best-first): keep a priority queue of leaves keyed by their best-split gain, pop the max, split it, push its two children, repeat until num_leaves is hit. For the same leaf budget, leaf-wise always spends its next split where the loss drops most, so it reaches a lower training loss — but the tree goes deeper and lopsided, which is the overfitting risk a max_depth guard exists to fight. import heapq def grow_leafwise ( g , h , x , num_leaves = 31 , max_depth =- 1 , lam = 0. ): def push ( pq , leaf ): gain , thr = best_split ( g [ leaf [ " idx " ]], h [ leaf [ " idx " ]], x [ leaf [ " idx " ]], lam ) deep = max_depth >= 0 and leaf [ " depth " ] >= max_depth if thr is not None and gain > 0 and not deep : heapq . heappush ( pq , ( - gain , id ( leaf ), leaf , gain , thr )) # -gain = max-heap # pop the single best leaf, split, push children, until num_leaves The max_depth guard only bites the leaf-wise tree: it refuses to split a leaf already too deep, forcing the split elsewhere. That is exactly how LightGBM tames best-first growth. Histogram split-finding — bin once, sweep the edges XGBoost's exact split search scores the gain at every one of the n−1 midpoints between sorted values. LightGBM bins each feature once into ~255 buckets, accumulates G,H per bin, and scores gain only at the k−1 bin edges via a running cumulative sum — turning a sort into a single pass, O(#bins) instead of O(#rows) . def hist_best_split ( g , h , x , max_bins = 255 , lam = 0. ): edges = np . unique ( np . quantile ( x , np . linspace ( 0 , 1 , max_bins + 1 ))) # bin ONCE b = np . clip ( np . digitize ( x , edges [ 1 : - 1 ]), 0 , len ( edges ) - 2 ) Gb = np . bincount ( b , weights = g , minlength = len ( edges ) - 1 ) # per-bin sums Hb = np . bincount ( b , weights = h , minlength = len ( edges ) - 1 ) # then one cumulative pass over the k-1 edges scores every candidate split There's a bonus: a child's histogram is the parent's minus its sibling's, so one of the two children comes for free. More bins means the histogram gain curve approaches the exact one; 255 is near-exact at a fraction of the work. GOSS — keep the rows that still matter Gradient-based One-Side Sampling shrinks the data by rows. A sample's gradient magnitude |gᵢ| measures how under-trained it still is, so GOSS keeps every large-gradient row and randomly subsamples the small-gradient rest — then amplifies those survivors by (1−a)/b so the gradient sums stay unbiased. def goss_subset ( g , h , a = 0.2 , b = 0.2 ): n = len ( g ); top = int ( a * n ); rest = int ( b * n ) order = np . argsort ( - np . abs ( g )) # big |gradient| first keep = order [: top ] # keep ALL large-gradient rows samp = np . random . choice ( order [ top :], rest , replace = False ) w = np . ones ( n ); w [ samp ] = ( 1 - a ) / b # up-weight the survivors return np . concatenate ([ keep , samp ]), w # gain uses g*w, h*w On the same row budget its split-gain estimate is consistently tighter than plain uniform sampling. EFB — bundle sparse features into one column Exclusive Feature Bundling shrinks the data by columns. One-hot and count features are mostly zero and rarely nonzero in the same row. EFB builds a conflict graph — an edge between features that clash — and greedily colours it; each colour becomes one bundle, with disjoint value ranges via an offset so a single column carries all of them without losing information. def efb_bundle ( X , max_conflict = 0 ): F = X . shape [ 1 ] conflict = [[ int ( np . sum (( X [:, i ] != 0 ) & ( X [:, j ] != 0 ))) for j in range ( F )] for i in range ( F )] color = [ - 1 ] * F # greedy graph colouring for i in range ( F ): used = { color [ j ] for j in range ( F ) if color [ j ] >= 0 and conflict [ i ][ j ] > max_conflict } c = 0 while c in used : c += 1 color [ i ] = c return color # features sharing a colour merge into one bundle Same second-order engine as XGBoost — far less work per tree: best-first trees held in check by num_leaves and max_depth , histogram splits with a free subtraction trick, fewer rows via GOSS, fewer columns via EFB. Drag the knobs and watch all four compute live: https://dev48v.infy.uk/ml/day41-lightgbm.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/lightgbm-internals-from-scratch-xgboosts-boosting-math-four-tricks-that-make-it-fast--f6k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
