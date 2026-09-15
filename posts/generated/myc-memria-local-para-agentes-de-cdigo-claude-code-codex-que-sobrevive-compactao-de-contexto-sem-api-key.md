---
title: "myc: memória local para agentes de código (Claude Code, Codex) que sobrevive à compactação de contexto, sem API key"
slug: "myc-memria-local-para-agentes-de-cdigo-claude-code-codex-que-sobrevive-compactao-de-contexto-sem-api-key"
author: "Vitaly Ivasenko"
source: "devto_ai"
published: "Tue, 15 Sep 2026 20:58:00 +0000"
description: "Quem usa Claude Code ou Codex por mais de uma hora conhece a cena: você combina com o agente "vamos de A, não de B, por causa de C", uma hora depois o contex..."
keywords: "com, myc, contexto, code, que, uma, bun, claude"
generated: "2026-09-15T21:05:12.124150"
---

# myc: memória local para agentes de código (Claude Code, Codex) que sobrevive à compactação de contexto, sem API key

## Overview

Quem usa Claude Code ou Codex por mais de uma hora conhece a cena: você combina com o agente "vamos de A, não de B, por causa de C", uma hora depois o contexto é compactado e o agente propõe B de novo, com a maior naturalidade. O motivo simplesmente não está mais no contexto dele. Encontrei no GitHub um projeto open source feito só para isso: myc (de mycelium). Não é mais uma API de memória na nuvem - é uma camada local de tarefas e memória que fica num único arquivo SQLite ao lado do projeto. O que ele faz: fila de tarefas com dependências, bloqueios e claim atômico (dois agentes nunca pegam a mesma tarefa); log de decisões com busca híbrida (BM25 + vetores); hook de PreCompact: no instante antes da compactação, grava a sessão em disco (segredos mascarados) e devolve ao contexto um "pacote de resgate" com o essencial; decisões extraídas automaticamente da conversa entram como candidatas - só viram fato depois que um humano confirma; memória ancorada em trechos de código: o código muda de lugar, a memória vai junto; o código some, a entrada é rebaixada ( [code gone ×0.2] ) em vez de ser servida como verdade; índice de código com tree-sitter (TypeScript/JavaScript/Python). Velocidade como restrição de projeto (100 mil nós, p99): pacote de contexto 0,6 ms, busca 8 ms, cold start 21 ms - reproduzível com bun run scripts/bench-latency.ts ; o build do site falha se um número divergir da medição. 3 700+ testes. Limitações ditas na cara: só roda em Bun (bun:sqlite), macOS/Linux, uso individual - sem servidor nem modo de equipe por enquanto. MIT. bun install -g @aistastudio/myc myc init && myc wire # conecta Claude Code / Codex / opencode / Kimi https://github.com/aistastudio/myc

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vitaly_ivasenko_cd7932e08/myc-memoria-local-para-agentes-de-codigo-claude-code-codex-que-sobrevive-a-compactacao-de-2ihc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
