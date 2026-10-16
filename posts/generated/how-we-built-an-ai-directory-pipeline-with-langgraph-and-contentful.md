---
title: "How We Built an AI Directory Pipeline with LangGraph and Contentful"
slug: "how-we-built-an-ai-directory-pipeline-with-langgraph-and-contentful"
author: "Israel Vásquez"
source: "devto_webdev"
published: "Fri, 16 Oct 2026 16:06:05 +0000"
description: "For Quicknode’s Builder’s Guide, we built a pipeline that populates over 60 structured fields per tool. That makes the content model a useful starting point ..."
keywords: "you, entry, can, directory, category, how, content, before"
generated: "2026-10-16T16:24:14.487371"
---

# How We Built an AI Directory Pipeline with LangGraph and Contentful

## Overview

For Quicknode’s Builder’s Guide, we built a pipeline that populates over 60 structured fields per tool. That makes the content model a useful starting point for understanding the work: each entry has to support discovery and comparison, so generating a readable summary addresses only part of the publishing problem. Our Quicknode case study documents a 5-node LangGraph workflow with retrieval, generation, category validation, and quality scoring before publication. The practical lesson we draw from that structure is to give each concern an explicit role. Evidence gathering, writing, classification, and publication need different acceptance criteria. Define what each field needs to establish A content model defines the fields and relationships that make an entry usable by the application. In a directory, that structure also gives you a way to evaluate generated content at a more specific level than whether the whole profile sounds convincing. When designing a similar pipeline, start by describing the evidence needed for each field. A descriptive summary needs enough context to explain the tool’s purpose. A pricing field needs information about the offer being described. A category assignment needs a definition against which the choice can be checked. These are different questions. Treating them individually helps you decide where generation is appropriate and where a value needs a more direct connection to a source. Define how the pipeline should represent missing information, too. An empty field, an explicit unknown, and a generated guess have different consequences for the reader. Choose that behavior before asking a model to complete an entry; otherwise, completeness can become an incentive to supply unsupported detail. Gather evidence before generating the profile We used the Tavily application programming interface (API) to find websites, documentation, and social links, and GPT-4o to generate descriptions, pricing tiers, and use cases. For a comparable directory, the useful design question is whether the material you retrieve can support the fields you intend to publish. Finding a page about a tool establishes a candidate source. You still need to determine what that page establishes and which part of the entry it can inform. For your own review process, consider pricing. Before accepting a generated value, check whether the source describes a current offer, a limited promotion, or an older announcement. That distinction gives the reviewer something specific to verify beyond the fluency of the generated description. Keep the distinction between evidence and interpretation visible during evaluation. A use case can involve synthesis across sources; a quoted price requires precise support. Applying the same review method to both can hide the difference between a useful explanation and an unsupported factual assertion. Validate classification against the directory’s definitions Our category validation step uses AI reasoning against Contentful definitions. That suggests a practical boundary for classification: the directory’s taxonomy, its defined category vocabulary, should supply the meaning of an accepted assignment. A plausible label is useful only if it corresponds to how the directory organizes its content. When building your own workflow, make those definitions available to the classification step and evaluate the proposed assignment against them. If categories overlap, decide how that overlap should be handled in the content model. Asking a model to choose cannot resolve an editorial ambiguity that the definitions leave open. You can also review classification separately from prose quality. An entry may explain a tool accurately while placing it in an unsuitable category. Conversely, a correct category says little about whether the pricing description is supported. Separate evaluation makes these failures easier to identify and discuss. Make publication criteria explicit We score content quality before publishing through the Contentful Management API , which handles entry creation and asset linking. The case study does not specify the scoring rubric or acceptance threshold. For your implementation, define what a score measures and what action follows from it. You might evaluate factual support, required-field completion, and category fit separately. Those are proposed criteria; they need to be tested against representative entries before you rely on them for publishing decisions. Make the review actionable. A low assessment should point to the field or claim needing attention. That gives you a concrete decision: gather more evidence, revise the generated text, or hold the entry for review. Quicknode’s directory began with 700 manually curated tools; the reported potential scale is over 5,000 profiles. The figure describes potential capacity. When evaluating similar automation, track how many entries meet your publication criteria alongside how many the system can generate. An accepted entry count gives you a useful basis for deciding whether to increase processing volume or improve the workflow first.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/madebymonogram/how-we-built-an-ai-directory-pipeline-with-langgraph-and-contentful-25d1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
