---
title: "Multi-Agent Debate: Personas Argue, a Critic Probes, and Confidence Falls Out of Consensus"
slug: "multi-agent-debate-personas-argue-a-critic-probes-and-confidence-falls-out-of-consensus"
author: "Devanshu Biswas"
source: "devto_python"
published: "Fri, 07 Aug 2026 18:53:36 +0000"
description: "Ask one model the same question three times and you get three paraphrases and a confident tone — whether or not the answer is actually contested. A multi-age..."
keywords: "not, confidence, answer, debate, three, stance, model, question"
generated: "2026-08-07T19:04:02.692544"
---

# Multi-Agent Debate: Personas Argue, a Critic Probes, and Confidence Falls Out of Consensus

## Overview

Ask one model the same question three times and you get three paraphrases and a confident tone — whether or not the answer is actually contested. A multi-agent debate does the opposite. Three personas answer independently, a critic names each one's flaw, every agent revises or defends, Python tallies the vote, and a judge synthesizes a final answer whose confidence is the agreement itself : unanimous → HIGH, split → LOW. Project 9 in Agentic AI from Zero runs this for real against NVIDIA NIM ( meta/llama-3.1-8b-instruct ) — 8 model calls per debate, two debates, 16 live calls captured. Diversity is engineered, not hoped for A debate is only useful if the debaters disagree. That's done with three distinct system prompts over the same model: PERSONAS = [ Persona ( " cautious " , " Cautious " , " 🛡️ " , " You are the CAUTIOUS debater. Risk-averse and conservative: prefer proven, low-downside " " answers, distrust hype, and double-check the arithmetic and edge cases before committing. " ), Persona ( " creative " , " Creative " , " 💡 " , " You are the CREATIVE debater. Think laterally; back a bold, unconventional answer if the " " upside is high — but flair is no excuse for being wrong on a question with a definite answer. " ), Persona ( " literal " , " Literal " , " 📏 " , " You are the LITERAL debater. Precise and methodical: answer EXACTLY what was asked, show the " " steps, and read nothing into the question that is not there. " ), ] Each proposes cold (temperature 0.7), before seeing anyone else. On a debatable question they split 2 bootstrap / 1 venture capital out of the gate — genuine divergence, not three rewordings. Crucially, each proposal carries a short canonical stance — the position itself, not a description of the method — so two agents who agree emit the identical label and can be counted. The critic answers nothing; the rebuttal moves minds One critic reads all proposals and, for each, returns a verdict ( sound / flawed / unsupported ) and the single most important flaw. It does not answer — its only job is to give the rebuttal something to push against. Then every proposer re-answers, having read the critique and the others, changing its stance only if genuinely convinced. And the mind-change is measured , not trusted from the model's self-report: def detect_mind_changes ( before , after ): # measured from the STANCES, not self-report pre = { p . persona_id : normalize_stance ( p . stance ) for p in before } return [ p . persona_id for p in after if pre [ p . persona_id ] != normalize_stance ( p . stance )] The vote and the confidence are deterministic Python The stance is the ballot. Normalize it so "$0.05" , "0.05" , and ".05" tally together, then count: def tally ( final_proposals ): ballots = { p . persona_id : normalize_stance ( p . stance ) for p in final_proposals } counts = dict ( Counter ( ballots . values ())) winner , votes = sorted ( counts . items (), key = lambda kv : ( - kv [ 1 ], kv [ 0 ]))[ 0 ] # plurality tied = list ( counts . values ()). count ( votes ) > 1 return Tally ( ballots , counts , winner , votes , total = len ( final_proposals ), tied = tied ) def derive_confidence ( t ): r = t . winner_votes / t . total # the consensus ratio if t . winner_votes == t . total and not t . tied : return Confidence ( " high " , r , " unanimous " ) if t . winner_votes > t . total / 2 and not t . tied : return Confidence ( " medium " , r , " a majority " ) return Confidence ( " low " , r , " split — no majority; flagged " ) The judge never gets to assert confidence — it falls out of the math. Two real debates, opposite outcomes On the bat-and-ball question the panel converges: "0.05"×3 , ratio 1.00, judge says "$0.05," HIGH 100% . On bootstrap-vs-VC the critique moves two minds (venture capital → hybrid, bootstrap → venture capital) — but instead of converging, the panel spreads out into a 1/1/1 three-way tie, ratio 0.33, LOW 33% , flagged. That's the whole point: a debate that doesn't converge is a valid result, and a genuine disagreement is visibly low-confidence instead of faked away. The model argues; every part that turns arguments into a verdict is deterministic Python you can read and test. Walk both debates phase by phase here: https://dev48v.infy.uk/agentic/project9-debate.html — repo at https://github.com/dev48v/agentic-ai-from-zero Next up, Project 10: a self-reflective agent that grades its own work.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/multi-agent-debate-personas-argue-a-critic-probes-and-confidence-falls-out-of-consensus-2b8f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
