---
title: "Two SKUs, One Model: How Prompt Engineering Alone Creates a $19 vs $29 SOP Generator"
slug: "two-skus-one-model-how-prompt-engineering-alone-creates-a-19-vs-29-sop-generator"
author: "KunStudio"
source: "devto_ai"
published: "Sun, 19 Jul 2026 13:23:39 +0000"
description: "Two SKUs, One Model: How Prompt Engineering Alone Creates a $19 vs $29 SOP Generator AI SOP Builder turns a plain-language process description into a finishe..."
keywords: "tier, sop, model, prompt, pro, one, env, brief"
generated: "2026-07-19T13:36:01.820175"
---

# Two SKUs, One Model: How Prompt Engineering Alone Creates a $19 vs $29 SOP Generator

## Overview

Two SKUs, One Model: How Prompt Engineering Alone Creates a $19 vs $29 SOP Generator AI SOP Builder turns a plain-language process description into a finished Standard Operating Procedure. There's no fine-tuned model and no separate "pro" pipeline — it's a single Claude Haiku call, and the entire product differentiation between the $19 and $29 tiers lives in how the prompt is assembled. One generation function, two tiers Both SKUs — single ($19, standard) and pro ($29, "audit-ready") — route through the same generateSOP() function and the same model ( claude-haiku-4-5 , with an optional SOP_MODEL_PRO env override). What changes is a tier string threaded through the prompt builders: export function buildSystem ( brief , tier ) { return [ " You are a senior operations and quality-management specialist who writes Standard " + " Operating Procedures (SOPs) that pass ISO 9001-style audits... " , " Never invent fake statistics, regulation numbers, certification IDs, or citations. " + " If a step depends on a policy you were not given, refer to it generically (for example " + " 'per your data-retention policy') and flag it as something the owner must fill in... " , tier === " pro " ? " This is the audit-ready edition: add a compact RACI view ... explicit controls, " + " checkpoints, and risk/compliance notes throughout the Procedure, and make the " + " Quality Checklist thorough enough to serve as a sign-off sheet. " : " Keep it practical, complete, and immediately usable by a small team. " , ]. join ( " " ); } Pro doesn't get a different retrieval source or bigger context window — it gets one extra paragraph telling the same model to add a RACI matrix (Responsible/Accountable/Consulted/Informed), inline compliance notes, and a heavier sign-off checklist. The anti-hallucination instruction — never invent a regulation number or certification ID, flag anything unprovided as something "the owner must fill in" — applies to both tiers, since a fabricated ISO clause in an audit file is worse than an SOP that's honestly generic. The free preview is a capped, separate generation — not a truncated one Before payment, /api/preview generates only the "Purpose and Scope" section, capped at 240 output tokens: export async function generateSOP ( env , brief , previewOnly , tier ) { const system = buildSystem ( brief , tier ); const user = buildUser ( brief , previewOnly , tier ); const model = ! previewOnly && tier === " pro " ? env . SOP_MODEL_PRO || undefined : undefined ; return claudeGenerate ( env , system , user , previewOnly ? 240 : tier === " pro " ? 5200 : 3600 , model ); } This isn't the full SOP truncated client-side — in previewOnly mode the prompt itself tells the model to write nothing but that section ("write nothing else — no other section, no numbered steps"). The visitor reads something genuinely specific to their process before paying anything, which is the point: a preview obviously tailored to your input converts differently than a generic marketing screenshot. Fulfillment happens inline with payment capture — deliberately There's no separate "generate" step after checkout. capture-order.js captures the PayPal order and, in the same request, calls generateSOP() for the full document before responding: let sop = "" ; let processingError = false ; try { sop = await generateSOP ( env , b . brief , false , priced . tier ); } catch ( e ) { processingError = true ; } return json ({ status : " COMPLETED " , orderID : body . orderID , tier : priced . tier , sop , processing_error : processingError , support : processingError ? " ghdejr11@gmail.com (auto-refund if unfulfilled) " : undefined , }, 200 ); The important line: status: "COMPLETED" still returns even if generation throws — the payment succeeded, so the response says so, with a processing_error flag and a support contact instead of silently losing the fact that money changed hands. A source comment ties this directly to a lesson from a prior pipe where payments succeeded while fulfillment silently failed with no record of it. Rendering the result without a Markdown library The SOP comes back as Markdown, and the front end renders it with a small hand-written parser — line-by-line regex matching for headings ( ^#{1,4}\s ), numbered lists ( ^\d+[.)]\s ), bullets ( ^[-*]\s ), and **bold** spans — built entirely with createElement / textContent , never innerHTML . It's a deliberately small vocabulary because that's the entire output format the system prompt requires — "render-safe Markdown only... no tables, code fences, or HTML" — so the renderer only has to handle exactly what the model is told to produce. Live: https://ai-sop-builder.pages.dev/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kunstudio/two-skus-one-model-how-prompt-engineering-alone-creates-a-19-vs-29-sop-generator-3ek

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
