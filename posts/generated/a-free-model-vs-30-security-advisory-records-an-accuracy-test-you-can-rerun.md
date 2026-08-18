---
title: "A Free Model vs 30 Security Advisory Records: An Accuracy Test You Can Rerun"
slug: "a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun"
author: "Jordan Huang"
source: "devto_python"
published: "Tue, 18 Aug 2026 01:30:03 +0000"
description: "A single wrong severity label can push a bad dependency upgrade into production. An advisory said "moderate." The package in our tree was critical. The model..."
keywords: "model, not, advisory, test, package, action, expected, severity"
generated: "2026-08-18T01:34:47.475606"
---

# A Free Model vs 30 Security Advisory Records: An Accuracy Test You Can Rerun

## Overview

A single wrong severity label can push a bad dependency upgrade into production. An advisory said "moderate." The package in our tree was critical. The model guessed low. I did not trust the model after that. I wanted a repeatable accuracy test. So I built one. I ran the test through MonkeyCode's free model access and free server option. Disclosure: This article was prepared as part of MonkeyCode's product outreach. The Problem With Advisory Summaries Advisory text is messy. Vendors use different words. One says "important." Another says "moderate." A model must map both to the right action. The model does not need to be perfect. It needs to be safe. A false negative is worse than a false positive. Skipping a critical upgrade hurts more than a wasted review. So I scored both kinds of errors separately. What I Measured I used 30 hand-checked test records. Each record models a public advisory. It has a description, expected package, severity, and action. I did not use 30 live advisories. That would make the test impossible to reproduce later. Vendor pages and model behavior change. My test records are small enough to review by hand. Each record asks two questions. Can the model extract the right package name? Can the model pick the right severity class? I ignore fancy prose. I score only the action label. The Test Harness The script is short. It reads a JSONL file. It calls a JSON-only completion for each record. It compares the parsed result to the expected fields. # .gitlab-ci.yml advisory-eval : image : python:3.12-slim stage : test script : - pip install httpx - python eval_advisories.py --endpoint "$MODEL_ENDPOINT" --token "$MODEL_TOKEN" --input advisories.jsonl artifacts : paths : - advisory-report.json The prompt is strict. It forces JSON and limits output size. PROMPT = """ Return JSON only with keys: package, severity, action. Severity must be one of: low, moderate, critical. Action must be one of: patch, minor, major. Do not include markdown. Advisory: {description} """ The scoring does not check wording. It checks the values. def score ( predicted , expected ): return { " package_ok " : predicted [ " package " ]. strip (). lower () == expected [ " package " ], " severity_ok " : predicted [ " severity " ] == expected [ " severity " ], " action_ok " : predicted [ " action " ] == expected [ " action " ], } One Local Run Your results will differ. This example shows the shape of a run, not a benchmark. Class Precision Recall low 0.80 0.70 moderate 0.60 0.62 critical 0.75 0.90 The model found most criticals. It missed several moderates. That matches my concern. A critical advisory often says "remote code execution." Those words are loud. A moderate advisory often says "denial of service under rare conditions." The model sometimes lowered it to low. A false low creates a larger risk than a false high. Three Recurring Failure Modes Vendor Word Mapping One record used the word "important." The expected class was high. The model returned moderate. The word "important" is ambiguous. This is a vocabulary problem. It is not solved by more tokens. Package Name Collisions One record mentioned "libxml2." The model returned "libxml." Those are different packages. A downstream tool might reject the patch. Or it might apply the wrong fix. Truncated Descriptions Long advisories lose the middle section. The fix version or affected range often sits in the middle. The model then guessed the action from the first sentence. That is dangerous. What I Would Not Automate I would not let this output open a merge request by itself. I might let it draft a note. A human still checks the package and version. A free server run is for triage. It is not a security scanner replacement. Skip this approach if you need audit-ready reporting. Skip it if your upgrade tool acts without human review. Skip it if you handle regulated systems. A Smaller Start Start with ten records. Mark expected values by hand. Run the parser. Read the errors. Ten errors teach more than zero passes. If the failure pattern is stable, add more records. If it is not stable, do not scale the tool yet. That is the whole point. Measure before you trust.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gitlab_3188/a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun-67h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
