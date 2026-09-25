---
title: "Agentic Fraud Investigation with TigerGraph"
slug: "agentic-fraud-investigation-with-tigergraph"
author: "Bhagyashri Kale"
source: "devto_python"
published: "Fri, 25 Sep 2026 03:52:58 +0000"
description: "Agentic Fraud Investigation with TigerGraph Introduction Fraud investigation becomes difficult when transaction data, customer information, and related entit..."
keywords: "investigation, fraud, tigergraph, graph, transaction, entities, agent, case"
generated: "2026-09-25T04:22:46.225682"
---

# Agentic Fraud Investigation with TigerGraph

## Overview

Agentic Fraud Investigation with TigerGraph Introduction Fraud investigation becomes difficult when transaction data, customer information, and related entities are spread across different records. For the TigerGraph × HHGoa 2026 challenge, we built an Agentic Fraud Investigation solution to analyze fraud cases and generate structured investigation results. Our solution uses TigerGraph Savanna as the graph layer and a custom Python-based investigation agent. Problem Statement The objective was to investigate fraud cases using transaction and entity relationships and produce useful evidence and investigation decisions for each case. Our solution processes 20 benchmark cases, from HHG-001 to HHG-020. What We Built Our solution includes: TigerGraph Savanna as the graph layer SavannaTransactionGraph Transaction, Customer, and Card entities Relationships between connected entities A custom Python investigation agent Rule-based fraud pattern detection Heuristic risk scoring Structured JSON outputs for each case Architecture The workflow is: Case Input → Data Preparation → TigerGraph Graph → Transaction and Entity Relationships → Python Investigation Agent → Fraud Pattern Analysis → Risk Score → Investigation Decision → JSON Case Output The graph representation helps organize relationships between transactions and related entities for fraud investigation. How We Used TigerGraph We used TigerGraph Savanna as the graph layer for our fraud investigation workflow. The graph used in the project is: SavannaTransactionGraph The graph contains entities such as: Transaction Customer Card These entities are connected through relationships that help organize transaction-related evidence. Investigation Agent The investigation agent is implemented as a custom Python program. It reads the prepared investigation data, applies fraud detection rules, calculates a heuristic risk probability, and generates investigation decisions. The current implementation is rule-based and heuristic. It does not use an external LLM API. Results We successfully processed all 20 benchmark cases: HHG-001 to HHG-020 The final results are stored as individual JSON case files. These outputs contain structured investigation information for each case, including the detected patterns and investigation decision. GitHub Repository The complete project source code and case outputs are available here: https://github.com/Bhagyashrikale01/agentic-fraud-investigation-tigergraph Limitations The current implementation has some limitations: The risk probability is heuristic and is not a trained or validated probability. The investigation uses preprocessed evidence. The current local agent does not use live external integrations. Full direct TigerGraph MCP integration with the agent is planned as future work. Future Improvements Future improvements could include: Full TigerGraph MCP integration GraphRAG-based investigation LLM-assisted investigation reasoning Live data integrations More advanced fraud detection models Improved explainability and investigation reports Conclusion This project gave us practical experience in graph-based fraud investigation, transaction analysis, Python automation, and building an end-to-end investigation workflow. The TigerGraph × HHGoa 2026 challenge helped us understand how graph technology can connect related entities and support fraud investigation. Thank you to TigerGraph and the HHGoa team for the opportunity to work on this challenge. TigerGraph #FraudDetection #Python #Hackathon

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bhagyashri_kale_c500cb884/agentic-fraud-investigation-with-tigergraph-2lmi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
