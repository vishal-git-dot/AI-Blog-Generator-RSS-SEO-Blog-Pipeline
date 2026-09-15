---
title: "myc: memoria local para agentes de código (Claude Code, Codex) que sobrevive a la compactación del contexto, sin API key"
slug: "myc-memoria-local-para-agentes-de-cdigo-claude-code-codex-que-sobrevive-a-la-compactacin-del-contexto-sin-api-key"
author: "Vitaly Ivasenko"
source: "devto_ai"
published: "Tue, 15 Sep 2026 20:58:01 +0000"
description: "Quien usa Claude Code o Codex más de una hora conoce la escena: acuerdas con el agente «vamos con A, no con B, por C», una hora después el contexto se compac..."
keywords: "con, myc, memoria, contexto, code, una, bun, claude"
generated: "2026-09-15T21:05:12.123948"
---

# myc: memoria local para agentes de código (Claude Code, Codex) que sobrevive a la compactación del contexto, sin API key

## Overview

Quien usa Claude Code o Codex más de una hora conoce la escena: acuerdas con el agente «vamos con A, no con B, por C», una hora después el contexto se compacta y el agente propone B otra vez, con toda naturalidad. El motivo ya no está en su contexto. Encontré en GitHub un proyecto open source hecho exactamente para esto: myc (de mycelium). No es otra API de memoria en la nube: es una capa local de tareas y memoria en un único archivo SQLite junto al proyecto. Qué hace: cola de tareas con dependencias, bloqueos y claim atómico (dos agentes nunca toman la misma tarea); registro de decisiones con búsqueda híbrida (BM25 + vectores); hook de PreCompact: justo antes de la compactación guarda la sesión en disco (secretos enmascarados) y devuelve al contexto un «paquete de rescate» con lo esencial; las decisiones extraídas automáticamente de la conversación entran como candidatas y solo se vuelven hechos cuando un humano las confirma; memoria anclada a fragmentos de código: si el código se mueve, la memoria lo sigue; si desaparece, la entrada se degrada ( [code gone ×0.2] ) en vez de servirse como verdad; índice de código con tree-sitter (TypeScript/JavaScript/Python). La velocidad es una restricción de diseño (100 000 nodos, p99): paquete de contexto 0,6 ms, búsqueda 8 ms, arranque en frío 21 ms, reproducible con bun run scripts/bench-latency.ts ; la build del sitio falla si un número se desvía de la medición. Más de 3 700 tests. Limitaciones dichas de frente: solo corre en Bun (bun:sqlite), macOS/Linux, uso individual, sin servidor ni modo equipo por ahora. MIT. bun install -g @aistastudio/myc myc init && myc wire # conecta Claude Code / Codex / opencode / Kimi Repo: https://github.com/aistastudio/myc · Sitio con mediciones reproducibles: https://aistastudio.github.io/myc/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vitaly_ivasenko_cd7932e08/myc-memoria-local-para-agentes-de-codigo-claude-code-codex-que-sobrevive-a-la-compactacion-del-2eko

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
