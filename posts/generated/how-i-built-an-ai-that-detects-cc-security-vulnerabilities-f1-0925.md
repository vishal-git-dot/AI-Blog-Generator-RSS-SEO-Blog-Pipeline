---
title: "How I Built an AI That Detects C/C++ Security Vulnerabilities (F1 0.925)"
slug: "how-i-built-an-ai-that-detects-cc-security-vulnerabilities-f1-0925"
author: "Ali Abbas Shah"
source: "devto_python"
published: "Tue, 11 Aug 2026 12:56:49 +0000"
description: "Finder of one bug in a million lines is still sleeping, but the models have started watching. Static analysis tools like Flawfinder and Cppcheck have been th..."
keywords: "code, codebert, bilstm, model, what, would, vulnerable, real"
generated: "2026-08-11T13:17:02.095999"
---

# How I Built an AI That Detects C/C++ Security Vulnerabilities (F1 0.925)

## Overview

Finder of one bug in a million lines is still sleeping, but the models have started watching. Static analysis tools like Flawfinder and Cppcheck have been the industry standard for years, but they work on predefined rules. They miss what they were never told to look for. This is the story of SecureScan AI — a deep learning model that reads C/C++ source code like a language model reads text, and flags vulnerabilities the way a code reviewer would. We built it for our Deep Learning lab at Air University Lahore, and it runs as a free web demo at securescan-ai.vercel.app . Why CodeBERT instead of rules CodeBERT is a BERT-family transformer pre-trained by Microsoft on both natural language and code pairs. It does not look for bug patterns — it has learned the meaning of code. That matters because: It generalizes to vulnerability types it was never explicitly trained on It catches logic-level issues, not just lexical signatures like strcpy It embeds context: what a variable flows into, what a buffer feeds The task is sequence labeling (or per-function binary classification): given a function, predict Vulnerable or Safe . The architecture C/C++ source code | v microsoft/codebert-base (125M params, first 6 layers frozen) | v 2 stacked BiLSTM layers (hidden 256, bidirectional = 512-dim) | v MLP head (512 -> 256 -> 128 -> 2, ReLU + BatchNorm) | v Vulnerable or Safe Why a BiLSTM on top of a transformer? CodeBERT alone scored F1 0.8612 on our benchmark. Adding the BiLSTM layers gave the model a sequential view of the token flow — it models how one line's taint propagates into the next. Without the BiLSTM, F1 dropped to 0.8832 (-4.2%). The data: 600,000+ labeled samples Dataset Language Samples Notes BigVul C / C++ ~188,000 Real CVEs + NVD entries DiverseVul C / C++ ~319,000 Diverse CVE coverage FormAI Multi ~246,000 AI-generated, labeled Total: 600,000+ labeled vulnerability samples. Results and ablation study Configuration F1 Delta Full model (CodeBERT + BiLSTM + MLP) 0.9252 reference Without BiLSTM 0.8832 -4.2% Without CodeBERT (GloVe) 0.7950 -8.3% Without dropout 0.8910 -3.4% Unidirectional LSTM 0.9056 -2.1% F1 0.9252, accuracy 89.3% , with inference at 42ms on GPU and 380ms on CPU — fast enough to serve as a free web demo, no GPU required. What surprised us Class imbalance is the real enemy. Vulnerable samples are rare in real-world code (roughly 1 in 16). We used BCE with 16:1 class-balancing weights, and this mattered more than any architectural change. Dropping it or the dropout layer cost 3-4% F1. How much the frozen encoder carries. CodeBERT alone (0.8612) beats a hand-built GloVe + BiLSTM pipeline (0.7950) by a huge margin — pre-training on code is worth more than careful feature engineering. Hyperparameter optimization actually works. We ran VAE-driven hyperparameter search mid-project and it lifted our best configuration from 92.68% to 94.82% before final evaluation. What I would do next Sliding-window tokenization — 512-token truncation cuts off real functions mid-body; windowing with overlap would preserve them Per-line vs per-function labeling — per-line localization would make the tool actually usable by developers Real-time IDE integration — an LSP or VS Code extension that flags code as you type Try it Live demo: securescan-ai.vercel.app Source: github.com/aly-abbas11/SecureScan-AI from src.models.securescan_model import SecureScanModel from transformers import AutoTokenizer import torch model = SecureScanModel () tokenizer = AutoTokenizer . from_pretrained ( ' microsoft/codebert-base ' ) code = " char buf[10]; strcpy(buf, user_input); " inputs = tokenizer ( code , return_tensors = ' pt ' , truncation = True , max_length = 512 ) with torch . no_grad (): logits = model ( inputs [ ' input_ids ' ], inputs [ ' attention_mask ' ]) prediction = ' Vulnerable ' if logits . argmax (). item () == 1 else ' Safe ' print ( f " Result: { prediction } " ) # Result: Vulnerable MIT licensed. Built with Salman Tanveer and Hammad Ali. If you build security tooling or have ideas on improving code-tokenization for transformers, I would love to hear from you in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alyabbas11/how-i-built-an-ai-that-detects-cc-security-vulnerabilities-f1-0925-4ifp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
