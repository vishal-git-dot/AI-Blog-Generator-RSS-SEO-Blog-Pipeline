---
title: "Reproducing a paper in Python: a random seed is only the first step"
slug: "reproducing-a-paper-in-python-a-random-seed-is-only-the-first-step"
author: "wanqiuxu"
source: "devto_python"
published: "Tue, 10 Nov 2026 14:35:41 +0000"
description: "You follow a machine learning or experimental paper, run the code, and the loss curve or the reported metric doesn't match. You move the same script to anoth..."
keywords: "you, seed, random, torch, same, not, more, can"
generated: "2026-11-10T14:38:48.358509"
---

# Reproducing a paper in Python: a random seed is only the first step

## Overview

You follow a machine learning or experimental paper, run the code, and the loss curve or the reported metric doesn't match. You move the same script to another machine, and the numbers move again. The first guess is almost always: I forgot to set a random seed. So you add torch.manual_seed(0) , and the problem is still there. A seed is necessary. It is usually the first link in the chain, not the whole chain. A more accurate reading is this: the mismatch often isn't "you forgot the seed." There is more than one source of randomness, and more than one runtime environment. PyTorch's official documentation is blunt about it: completely reproducible results are not guaranteed across PyTorch releases, individual commits, or different platforms. Even with identical seeds, results may differ between CPU and GPU. More than one generator Start by taking "random" apart. A training script can easily be using several independent generators at once. Python's built-in random , NumPy's RNG, and PyTorch's CPU and CUDA generators do not share a single switch by default. If you pin only one of them, data augmentation, weight initialization, and shuffle order can still draw from somewhere else. Mix in scikit-learn or another library, and you usually pick up yet another random state. The Python interpreter also hash-randomizes some things, which can change preprocessing that depends on the order of a set or a dict. Variables such as PYTHONHASHSEED generally need to be set before the process starts. Putting them in the middle of a script is often already too late. Data loading is another common hole. Once DataLoader uses multiple workers, each worker has its own random state. Seeding the main process does not automatically seed numpy or random inside every child. The docs recommend a worker_init_fn and a fixed Generator for sampling. Skip that, and you get a familiar bug: it matches with a single process, then drifts as soon as you set num_workers . Dropout, random crops, and shuffling will also pull two runs apart if they live on different random streams. GPUs, versions, and what you should check first On the GPU, algorithm selection can change the result. CUDA convolutions often have several implementations. If cudnn.benchmark is on, the runtime may try a few and keep whichever looks fastest at that moment. If the machine is under a different load, it may pick a different implementation, and the numbers can shift slightly. Turning benchmark off makes the choice more stable, but the chosen algorithm can still be nondeterministic. If you also set torch.use_deterministic_algorithms(True) , the framework will prefer deterministic implementations when they exist. When they don't, some ops raise an error, and some need extra environment variables. The deterministic path is usually slower. You're trading speed for repeatability. Even with those switches on, versions and hardware can still move the last decimals. CUDA, cuDNN, the driver, minor library versions, and the order of floating-point adds all matter. Swap a GPU, or move from GPU to CPU, and you should not expect bit-for-bit agreement. So when you try to reproduce a paper, check these first: is the data split the same, is the preprocessing the same, are the pretrained weights the same file, and are the key dependency versions pinned in an environment file? Plenty of "reproduction failures" are really a different data slice, or a different pretrained checkpoint. A seed matters, but it cannot police an undocumented dataset or an unfrozen environment. Locking requirements.txt or a conda environment, and recording the CUDA version, is often more effective than tweaking the seed again. Here is a minimal setup that gets you closer to a repeatable run. It reduces common sources of randomness. Per the official docs, it still does not promise a perfect match across versions or devices: import os , random import numpy as np import torch # PYTHONHASHSEED should be set before Python starts, for example: # PYTHONHASHSEED=0 python train.py def seed_everything ( seed : int = 0 ) -> None : random . seed ( seed ) np . random . seed ( seed ) torch . manual_seed ( seed ) torch . cuda . manual_seed_all ( seed ) torch . backends . cudnn . benchmark = False torch . use_deterministic_algorithms ( True ) def seed_worker ( _worker_id : int ) -> None : s = torch . initial_seed ( ) % 2 ** 32 random . seed ( s ) np . random . seed ( s ) seed_everything ( 0 ) loader = torch . utils . data . DataLoader ( dataset , # a dataset you have already prepared num_workers = 4 , worker_init_fn = seed_worker , generator = torch . Generator ( ) . manual_seed ( 0 ) , ) Before you start, a short checklist helps: the same data, the same split, the same weights, a locked dependency file, and whether the authors reported variation across multiple runs. If any of those is missing, a mismatch should not surprise you. Some papers average several random seeds in the table. If you run once and compare against that average, you are not comparing the same thing. The more useful bar is also not "every decimal in the paper's table." Recovering the same direction, a similar magnitude, and the main conclusion within a reasonable range usually matters more than chasing a floating-point ghost. If you release code yourself, write down the seed, dependency versions, data split, git commit, and hardware. Then the next person can tell whether a mismatch belongs to the environment — or to the method. More research explainers: https://www.crushsci.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wanqiu_7ad7bc3efc7b7/reproducing-a-paper-in-python-a-random-seed-is-only-the-first-step-34mf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
