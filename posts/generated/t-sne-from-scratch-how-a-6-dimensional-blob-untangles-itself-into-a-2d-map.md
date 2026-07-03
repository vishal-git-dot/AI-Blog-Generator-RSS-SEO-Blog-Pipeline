---
title: "t-SNE from scratch: how a 6-dimensional blob untangles itself into a 2D map"
slug: "t-sne-from-scratch-how-a-6-dimensional-blob-untangles-itself-into-a-2d-map"
author: "Devanshu Biswas"
source: "devto_python"
published: "Fri, 03 Jul 2026 09:00:22 +0000"
description: "You have data with dozens or hundreds of features and you want to see it. Your screen is flat, so the question is: how do you place every point on a 2D map s..."
keywords: "sne, you, points, one, run, clusters, map, high"
generated: "2026-07-03T09:27:38.731668"
---

# t-SNE from scratch: how a 6-dimensional blob untangles itself into a 2D map

## Overview

You have data with dozens or hundreds of features and you want to see it. Your screen is flat, so the question is: how do you place every point on a 2D map so the picture reflects the structure hiding in high-dim space? t-SNE is the tool built for exactly this, and today I built a working one you can watch run in the browser. Live demo (press Run and watch four clusters pull apart): https://dev48v.infy.uk/ml/day23-tsne.html The problem: high dimensions are invisible Consider a dataset of handwritten-digit images. Each one is 784 numbers — there's no way to look at that. Worse, high-dimensional space plays a cruel trick: as dimensions pile up, nearly every pair of points ends up roughly the same distance apart, so raw distances become weak, mushy signals. Clusters a model finds trivially are invisible to you. Dimensionality reduction squashes the data down to 2D so you can literally look at it. t-SNE (t-distributed Stochastic Neighbour Embedding) does this by making one clear trade: it faithfully preserves who is near whom and cheerfully throws away the global geometry. That trade is the whole story, and it's why t-SNE plots are read a very specific way. The core idea: turn distances into probabilities t-SNE never optimises raw distances. For each point i it asks a softer question: "if I picked a neighbour at random, weighted by a Gaussian over distance, how likely would I pick j?" Nearby points get high probability, far ones essentially zero. Each point's answers form a probability distribution over its neighbours. The Gaussian's width isn't fixed — it's tuned per-point (by binary search) so the distribution hits a target "spread" you choose, the perplexity . Perplexity is roughly the effective number of neighbours each point pays attention to; typical values are 5 to 50. It's the single most important knob: too small and real clusters shatter into confetti, too large and distinct groups blur together. In the demo you can drag it and watch the layout change character. Because i's view of j and j's view of i disagree (different widths), t-SNE averages them into one symmetric joint matrix P , normalised so all pairs sum to 1. That P is the fixed target the 2D map must reproduce. The 2D side, and the one weird trick that makes it work In the 2D map we need similarities too. Here t-SNE does something clever: instead of another Gaussian, it uses a Student-t kernel with one degree of freedom, 1 / (1 + d²) . Why? The crowding problem . There's vastly less room in 2D than in high-dim, so a Gaussian map crushes everything into a central pile. The Student-t's heavy tail decays slowly for distant pairs, letting far-apart points sit comfortably far apart without a big penalty — exactly why t-SNE produces those crisp, well-separated islands you see in embedding plots. The objective: minimise KL divergence We now have two distributions: the high-dim target P and the low-dim map Q. t-SNE measures their mismatch with the Kullback–Leibler divergence, KL(P‖Q) = Σ Pᵢⱼ · log(Pᵢⱼ / Qᵢⱼ) . Because KL is asymmetric, it punishes placing far-apart map points where P said "close" far more than the reverse — so t-SNE fiercely protects local neighbourhoods and stays relaxed about the big picture. There's no closed form for the best layout, so we find it by gradient descent. The gradient has a lovely spring interpretation: each point is attracted to pairs where P > Q (should be closer) and repelled from pairs where Q > P (should be farther), scaled by the Student-t numerator. Add momentum, re-centre the cloud each step, and the points slide into place. In my seeded browser run of 80 points in 6 dimensions (four Gaussian blobs), KL falls from about 1.62 to 0.076 over 500 steps, and the four true clusters go from one indistinguishable pile to tight, well-separated islands — a between/within distance ratio jumping from ~1 to ~19. The colours in the demo mark the true cluster so you can judge the result, but t-SNE never sees the labels. What you must NOT read off a t-SNE plot This is the part people get wrong, so state it as rules: Distance between clusters is not meaningful. Global layout was deliberately sacrificed; two clusters close on the plot aren't "more similar" than two far apart. Cluster size and density are not meaningful. t-SNE tends to equalise sizes — a tight dense group and a sprawling sparse one can look identical. A single run isn't gospel. Different seeds give different (equally valid) maps. Run several perplexities and seeds, trust only structure that persists. Let it converge. A half-finished run shows fake sub-clusters that merge later. Treat a t-SNE plot as the answer to "which points group together?" — never "how far apart are the groups?" or "which is bigger?". Doing it for real Nobody hand-rolls this in production. scikit-learn ships a fast Barnes-Hut version; openTSNE is faster still and can place new points. Standardise your features and PCA down to ~30–50 dims first (t-SNE is O(N²) and slow on raw high-dim input), then run it. from sklearn.manifold import TSNE from sklearn.decomposition import PCA X50 = PCA ( n_components = 50 ). fit_transform ( X ) # speed + denoise emb = TSNE ( n_components = 2 , perplexity = 30 , init = " pca " , random_state = 42 ). fit_transform ( X50 ) The interactive version — perplexity slider, live KL readout, step/run/reset, four clusters separating in real time — is here: https://dev48v.infy.uk/ml/day23-tsne.html Tomorrow: UMAP — faster than t-SNE, keeps more global structure, and can embed new points. It's quietly become the default for these plots.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/t-sne-from-scratch-how-a-6-dimensional-blob-untangles-itself-into-a-2d-map-269f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
