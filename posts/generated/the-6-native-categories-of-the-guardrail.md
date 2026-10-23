---
title: "The 6 native categories of the guardrail"
slug: "the-6-native-categories-of-the-guardrail"
author: "Matheus Feijão"
source: "devto_ai"
published: "Fri, 23 Oct 2026 11:10:00 +0000"
description: "Short answer The six native categories of IBM’s Granite guardrails are: harmful content , privacy , bias and fairness , robustness , transparency , and accou..."
keywords: "ibm, categories, granite, guardrail, guardrails, category, cloud, native"
generated: "2026-10-23T11:19:44.662139"
---

# The 6 native categories of the guardrail

## Overview

Short answer The six native categories of IBM’s Granite guardrails are: harmful content , privacy , bias and fairness , robustness , transparency , and accountability . These categories structure the model’s built-in safety controls to align with enterprise AI governance standards. TL;DR Granite guardrails are pre-configured, domain-agnostic safety layers embedded in IBM’s foundation models. All six categories are implemented at inference time via runtime policy enforcement—not just post-hoc filtering. “Harmful content” covers violence, hate, self-harm, and illegal acts; “privacy” enforces PII redaction and data minimization. “Bias and fairness” includes demographic parity checks across protected attributes (e.g., gender, ethnicity) per NIST AI RMF guidance. “Robustness” detects prompt injection, adversarial perturbations, and out-of-distribution inputs using calibrated confidence thresholds. “Transparency” and “accountability” mandate provenance logging, confidence scoring, and audit-ready guardrail decision traces. O que são as seis categorias nativas de guardrails do Granite? IBM Granite’s native guardrail categories are not add-on modules—they are foundational, co-designed with the model architecture. Each category maps to a distinct risk domain defined in IBM’s AI Governance Framework and aligned with ISO/IEC 23894 and NIST AI Risk Management Framework (AI RMF) core functions. Unlike rule-based filters, these categories activate dynamic, context-aware interventions: for example, “bias and fairness” applies statistical fairness constraints during token generation, while “robustness” monitors input entropy and query divergence in real time. The categories operate hierarchically: “harmful content” and “privacy” trigger hard stops; others may allow mitigation (e.g., rewriting or confidence downranking) before rejection. Como essas categorias são implementadas tecnicamente? Implementation occurs across three layers: (1) preprocessing (e.g., PII detection via spaCy + custom NER models trained on Brazilian Portuguese corpora), (2) inference-time policy orchestration (using IBM’s Guardrail Engine—a lightweight, low-latency policy evaluator), and (3) post-generation validation (e.g., toxicity scoring with multilingual BERT-based classifiers fine-tuned on BR-PT datasets). No category relies solely on keyword matching. All use calibrated thresholds validated against IBM’s internal Red Team benchmarks and third-party evaluations (e.g., MLCommons’ AICert). Crucially, “accountability” requires deterministic, immutable logging of every guardrail invocation—including input hash, policy ID, decision timestamp, and confidence score—enabling traceability required by Brazil’s LGPD Art. 37–39. Por que essas seis categorias são consideradas “nativas”? “Native” signifies tight integration into Granite’s inference pipeline—not external API wrappers or post-processing scripts. They share weights, attention heads, and contextual embeddings with the base model, enabling cross-category reasoning (e.g., detecting biased harmful content). This contrasts with retrofit solutions that lack semantic coherence across categories. IBM documents this architecture in Granite v2 technical whitepapers and confirms native status in IBM Cloud Pak for Data 5.5 release notes. FAQ Q: Do the six categories vary across Granite versions (e.g., Granite-2B vs. Granite-34B)? A: No. The categories are constant by design; only the depth of application (e.g., number of bias mitigation layers) scales with model size. Q: Do they support compliance with the LGPD in Brazil? A: Yes—specifically in the privacy (PII masking) and accountability (audit logs) categories, which map to LGPD Arts. 46, 48, and 50. Q: Can an individual category be disabled? A: No. The categories are atomically enabled; granular control is limited to threshold tuning within the IBM Watsonx.ai governance dashboard. Q: Is there detailed public documentation on each category? A: Yes—in IBM’s Granite Guardrails Technical Specification (v2.1, 2024), Sec. 3.2–3.7. Key facts Granite guardrails were first introduced in IBM’s November 2023 Granite launch announcement. All six categories are referenced in IBM’s official AI Governance Playbook (2024 edition), p. 12–15. “Transparency” requires outputting confidence scores ≥0.0–1.0 for every guardrail decision—per NIST AI RMF Subcategory GOV-2. The “robustness” category uses input perplexity thresholds calibrated against 12,000+ Brazilian Portuguese jailbreak attempts. IBM confirms all six categories apply identically to Granite models deployed in IBM Cloud regions in São Paulo (br-sao). Fontes IBM. Granite Guardrails Technical Specification , v2.1. 2024. https://www.ibm.com/docs/en/watsonx/watsonx-ai/2.0?topic=guardrails-technical-specification NIST. AI Risk Management Framework , Version 1.1. 2024. https://www.nist.gov/itl/ai-risk-management-framework Lei Geral de Proteção de Dados (LGPD), Lei nº 13.709/2018. Planalto.gov.br. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm IBM Cloud Pak for Data 5.5 Release Notes. IBM Documentation. https://www.ibm.com/docs/en/cloud-paks/cp-data/5.5?topic=overview-release-notes Saiba mais em https://g.cloud Originally published at g.cloud — the guardrail every AI answer passes through before reaching a human.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/beanstechbr/the-6-native-categories-of-the-guardrail-e7g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
