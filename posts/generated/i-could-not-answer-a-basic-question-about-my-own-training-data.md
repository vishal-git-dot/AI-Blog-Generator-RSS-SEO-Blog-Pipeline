---
title: "I could not answer a basic question about my own training data"
slug: "i-could-not-answer-a-basic-question-about-my-own-training-data"
author: "LXSAIHUB"
source: "devto_webdev"
published: "Tue, 10 Nov 2026 22:58:46 +0000"
description: "Someone asked me a simple question about a model I had put into production: where did the training data come from, and could I show that it was appropriate f..."
keywords: "not, data, your, you, what, whether, article, where"
generated: "2026-11-10T23:03:02.010458"
---

# I could not answer a basic question about my own training data

## Overview

Someone asked me a simple question about a model I had put into production: where did the training data come from, and could I show that it was appropriate for what the system does. I had the architecture documented and the evaluation results written down. I did not have a clear, written account of the data itself. The answer lived in several places: a data-processing script, a folder naming convention, a note in a pull request, and my own memory. When I tried to write it down as a coherent account, I found gaps I had not noticed. Which sources were represented, which were thin, and whether any special-category data had slipped into a dataset. None of that was captured anywhere I could point to. So I built a starter that takes a plain description of how your AI system is trained or fed and turns it into an Article 10 data-governance draft. Art10Pack surfaces the themes in what you described, the places where your sources are thin or missing, and flags where special-category data may be present. It produces a draft to work from, not a verdict. Why Article 10 is a data question before it is a documentation question For high-risk systems under the EU AI Act, Article 10 deals with data and data governance. It concerns the training, validation, and test data: where it comes from, how it was collected and prepared, whether it is relevant and representative for the intended purpose, and how bias and errors are examined. It sits alongside other obligations for high-risk systems, including Article 9 on risk management, Article 12 on logging, and Article 14 on human oversight. Whether a system is high-risk at all is a separate classification question tied to the Annex III categories, and I am not going to pretend a text tool can settle that. What struck me is that this is mostly an engineering documentation problem. The obligation asks for an account of your data practices. Most teams have that knowledge distributed and undocumented. The hard part is not inventing a policy; it is noticing what you never wrote down. That is the narrow thing Art10Pack does. It reads your description, organizes it into themes, and marks the evidence gaps where the account is thin. The special-category flags point at where sensitive data may be involved, so you can go look. It is a structured prompt to check your own work. What the starter is, and is not A draft that looks official is easy to over-trust, so let me be exact. Art10Pack is decision-support. It is not legal advice, not a certification, and not a live audit harness. It does not connect to your data pipeline, inspect your actual datasets, or verify a single claim in your description. If you write that a source is licensed and representative, the draft reflects what you wrote. It will not check the license or measure representativeness. The output is a starter: themes, source gaps, and special-category flags built from the text you pasted. Its value is that it makes the gaps visible. An empty "source" section is a signal that you need to go find that information. A flag is a pointer to an investigation, not a finding. I would treat the whole document as a checklist of questions to answer with real evidence, not as the evidence itself. It also cannot decide whether your system is high-risk, whether a specific dataset satisfies Article 10, or whether you have met any obligation. Those determinations need someone who understands your system and the law. The tool maps the terrain; it does not certify the route. The trade-off I accepted I could have built something that inspects a real dataset and scores it. That is a much heavier tool, needs access to your data, and still cannot answer the legal question of whether your governance is adequate. It would also be useless at the stage where I most needed help, before the documentation exists at all. A pasted-description starter works at that stage, when noticing a missing source is cheap. That portability is the limit too. Garbage in, plausible-looking draft out. I built the tool for the failure I personally had: scattered knowledge nobody had assembled into a written account. It is good at making you assemble it. It is not good at telling you the assembled account is true. If your data governance lives in a script and a pull request, Art10Pack will at least get it onto one page so you can see what is missing. FAQ What is Art10Pack? A decision-support starter that turns a pasted description of how your AI system is trained or fed into an Article 10 data-governance draft with themes, source gaps, and special-category flags. Does it inspect my actual training data? No. It works from the text you paste. It does not connect to your pipeline, read your datasets, or verify your claims, and it is not a live audit harness. Can it tell me whether my system is high-risk or compliant? No. Classification under the EU AI Act and any determination of compliance are outside its scope. It is not legal advice and not a certification. What should I do with a source gap or a flag? Go find the real evidence. A gap means the account is thin; a flag means special-category data may be involved. Both are prompts to investigate, not findings.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lixingliangsy/i-could-not-answer-a-basic-question-about-my-own-training-data-4jhb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
