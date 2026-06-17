---
title: "From ML Tooling to Analytical Governance: Recent Updates to KMDS"
slug: "from-ml-tooling-to-analytical-governance-recent-updates-to-kmds"
author: "Rajiv Sambasivan"
source: "devto_python"
published: "Wed, 17 Jun 2026 04:32:36 +0000"
description: "Over the last few months I've been refining KMDS, a framework for building repeatable and auditable machine learning systems. The original motivation behind ..."
keywords: "analytical, governance, knowledge, feature, design, kmds, machine, learning"
generated: "2026-06-17T04:47:02.509308"
---

# From ML Tooling to Analytical Governance: Recent Updates to KMDS

## Overview

Over the last few months I've been refining KMDS, a framework for building repeatable and auditable machine learning systems. The original motivation behind KMDS was simple: Many machine learning projects fail long before model selection becomes important. Teams struggle with questions such as: What entities are represented in the data? What is the unit of analysis? What temporal structure exists? Which feature engineering strategies are appropriate? Which modeling assumptions were made? How are these decisions preserved over time? Most organizations answer these questions at some point. The problem is that the answers often disappear into notebooks, documents, tickets, or the memories of individual contributors. KMDS is an attempt to make these decisions explicit, structured, and reusable. What Changed? Recent updates have focused on moving beyond workflow automation and toward analytical governance. 1. Metadata-Driven Semantic Data Understanding The workflow begins with semantic tagging and metadata generation. Rather than immediately building features or training models, the system first attempts to understand: attribute types entities temporal structure data quality characteristics The goal is to establish a semantic foundation before modeling begins. 2. Feature Advisor One of the new additions is a Feature Advisor service. Given metadata and project context, the advisor recommends feature engineering strategies for non-numeric attributes. Examples include: hierarchical categorical encoding target encoding strategies TF-IDF pipelines sentence embedding approaches native model handling for modern gradient boosting systems The objective is not automatic feature engineering. The objective is to provide design guidance and rationale that helps practitioners make better decisions. 3. Design Governance A second addition is a Design Governance framework. Machine learning projects contain many decision points: classification vs regression handling class imbalance interpretability vs predictive performance validation strategy calibration requirements graph-based vs tabular approaches The Design Governance layer acts as a design-time advisor that captures these considerations and generates implementation guidance. The output is a structured design blueprint that can be reviewed by humans or supplied to AI coding assistants. 4. Knowledge Preservation Perhaps the most important change is an increased emphasis on preserving analytical knowledge. The long-term goal is not simply to create models. It is to create reusable analytical assets. Using KMDS tooling, project artifacts can be transformed into a knowledge graph representing: data understanding feature engineering decisions modeling assumptions operational considerations generated artifacts This creates a queryable representation of the analytical lifecycle. Why This Matters Most organizations already have documentation. What they often lack is accessible institutional knowledge. Critical analytical decisions are frequently distributed across: repositories notebooks presentations tickets email threads individual contributors When people leave, much of that context leaves with them. My view is that the real asset is not the agent. The real asset is the structured analytical knowledge that the agent can access. If the knowledge is preserved independently of any specific model, tool, or LLM, organizations retain ownership of their analytical reasoning and can recreate capabilities as technology evolves. Current Direction The broader goal of KMDS is to make machine learning systems: more transparent more auditable more reproducible easier to transfer between teams Recent work has focused on feature governance, design governance, metadata-driven workflows, and knowledge graph generation. Future work will continue exploring how analytical context can be captured and preserved as a first-class artifact rather than an afterthought. I would be interested in hearing how others are approaching analytical governance, reproducibility, and knowledge preservation in their own machine learning workflows.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rajivsam/-from-ml-tooling-to-analytical-governance-recent-updates-to-kmds-548n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
