---
title: "I built a CI/CD gate that blocks energy regressions in Python — and refuses to lie about what it measured"
slug: "i-built-a-cicd-gate-that-blocks-energy-regressions-in-python-and-refuses-to-lie-about-what-it-measured"
author: "BaBARuST"
source: "devto_python"
published: "Sat, 21 Nov 2026 18:37:13 +0000"
description: "**dol8 **is a CI/CD energy regression gate for Python. It blocks pull requests that increase CPU energy consumption by reading real RAPL Joules on bare-metal..."
keywords: "gate, energy, python, cpu, blocks, refuses, joules, measurement"
generated: "2026-11-21T18:56:47.820897"
---

# I built a CI/CD gate that blocks energy regressions in Python — and refuses to lie about what it measured

## Overview

**dol8 **is a CI/CD energy regression gate for Python. It blocks pull requests that increase CPU energy consumption by reading real RAPL Joules on bare-metal Linux, with honest fallbacks to perf counters on VMs and CPU time on Windows. The core is written in Rust (via PyO3) so the measurement does not contaminate itself, with Python handling statistics and orchestration. The differentiator is the honesty layer: every output is tagged with its measurement source and confidence level, the gate refuses to hard-fail CI on noisy data, and cross-tier comparisons (Joules vs CPU-seconds) are blocked by design. It uses 3*IQR outlier rejection and coefficient-of-variation confidence scoring so a single noisy run cannot corrupt the verdict. Currently v0.4-alpha, validated on AMD Ryzen (12.292 J, CoV 1.36%). Intel validation and calibration data population are in progress. MIT licensed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/babarustyhz/i-built-a-cicd-gate-that-blocks-energy-regressions-in-python-and-refuses-to-lie-about-what-it-2635

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
