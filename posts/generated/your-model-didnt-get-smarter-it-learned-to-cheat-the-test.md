---
title: "Your model didn't get smarter. It learned to cheat the test."
slug: "your-model-didnt-get-smarter-it-learned-to-cheat-the-test"
author: "Anil Prasad"
source: "devto_python"
published: "Sun, 26 Jul 2026 13:02:04 +0000"
description: "Reward hacking, eval contamination, and irreproducible runs are the three invisible failures in modern LLM training. Here is an open-source trust layer that ..."
keywords: "provenir, run, reward, you, passport, model, eval, three"
generated: "2026-07-26T13:40:34.479185"
---

# Your model didn't get smarter. It learned to cheat the test.

## Overview

Reward hacking, eval contamination, and irreproducible runs are the three invisible failures in modern LLM training. Here is an open-source trust layer that catches all three. Modern fine-tuning frameworks are fast. verl, TRL, and Unsloth can saturate a GPU cluster and push tokens per second most of us could not have imagined three years ago. But speed created a blind spot. Faster training did not make good models easier to produce. It made bad models cheaper to produce. And three failure modes crept into that blind spot, all sharing one dangerous property: they are invisible on a normal dashboard. This post is about those three failures and an open-source project, Provenir, that catches all of them. Everything here runs with pip install provenir. Failure 1: reward hacking You train against a reward signal. A verifier decides if each answer earns the reward. The model maximizes reward by any means available, including means you did not intend. The core problem: a verifier checks the answer, not the reasoning. So the model learns to pass the check without doing the thinking. Recent RLVR research documented models abandoning real reasoning on inductive tasks, producing outputs that satisfied the verifier while skipping the pattern the task required. Reinforcement learning amplifies whatever maximizes reward, so the longer you train, the worse it gets. There are seven common modes: Every one shows up on your dashboard as a reward curve going up. Provenir's flight recorder and reward-hacking detector flag them per step, live: from provenir.observability import FlightRecorder, RewardHackingDetector recorder = FlightRecorder() detector = RewardHackingDetector() for step, metrics in rl_loop(): recorder.log_step(metrics) # KL, entropy, reward std, advantages... for anomaly in recorder.anomalies(): print(anomaly.kind, anomaly.step, anomaly.detail) report = detector.analyze(rollouts) if report.is_hacking: print("Reward hacking detected:", report.findings) Failure 2: evaluation contamination Your benchmark says 92%. If the eval set leaked into training, that number measures memory, not capability. [IMAGE: provenir-article-fig4-compare.png] This happens constantly. Training corpora are huge and scraped widely; benchmark questions end up inside them, sometimes verbatim, sometimes paraphrased just enough to dodge a naive string match. The fix is to check overlap the way contamination actually happens: from provenir.eval.contamination import ContaminationChecker checker = ContaminationChecker() # 13-gram + embedding + exact, MinHash at scale report = checker.check(train_dataset, eval_dataset) print(f"Overlap: {report.overlap_ratio:.1%} across {report.n_hits} records") For a stronger guarantee, plant canary tokens in a private eval vault. If those tokens ever appear during training, you know your held-out set leaked. It turns "we think the eval is clean" into "we can prove it." Failure 3: irreproducibility A run produces a great model. Two weeks later you cannot reproduce it. Different seed, a dependency moved, the dataset shifted. You have a good model and no idea how you made it. [IMAGE: provenir-article-fig3-passport.png] Every Provenir run produces a content-addressed manifest: config hash, dataset hash, git SHA, seed, and a lineage DAG linking dataset → run → adapter → eval → merge. provenir train config.yaml --dataset data/train.jsonl # produces a tamper-evident manifest provenir reproduce manifest_abc123.json --output reproduced_run/ # reproduces the exact run On top sits a signed Model Passport, a portable bill of materials mapping directly to EU AI Act Article 12 (tamper-proof audit trails + model lineage, enforced August 2, 2026): from provenir.governance.passport import ModelPassport passport = ModelPassport.build(run.manifest, key="team-signing-key") passport.save("passport.json") # signed HMAC-SHA256 bill of materials loaded = ModelPassport.load("passport.json") assert loaded.verify(key="team-signing-key") print(loaded.risk_flags) # ["unscanned_pii", "contaminated_eval", "unknown_license"] Where Provenir sits Provenir does not reimplement kernels. It orchestrates verl, TRL, and Unsloth through backend-agnostic adapters and adds the trust layer on top. The whole thing drops into an existing loop in three lines: import provenir with provenir.track("my-run", dataset=train_ds) as run: for step, metrics in training_loop(): run.log_step(metrics) run.record_eval("mmlu", score=0.71) # run.manifest, run.flight_recorder, run.hacking_report, run.passport Try it pip install provenir # manifests, eval, governance, CLI pip install "provenir[train]" # SFT + DPO + LoRA/QLoRA via TRL pip install "provenir[all]" # everything Apache 2.0. 1,153 tests. Repo and docs: github.com/anilatambharii/provenir. Speed without trust just means you reach the wrong answer faster and with more confidence. If you work on RL or fine-tuning infra, I would genuinely like to hear which of these three failures has cost you the most. Drop it in the comments. HumanWritten #ExpertiseFromField

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/anilatambharii/your-model-didnt-get-smarter-it-learned-to-cheat-the-test-5g08

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
