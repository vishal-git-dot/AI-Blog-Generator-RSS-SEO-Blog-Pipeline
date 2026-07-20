---
title: "agent-shield-runtime v0.1.0: hook de despliegue que conecta 5 sensores de defensa de agentes IA"
slug: "agent-shield-runtime-v010-hook-de-despliegue-que-conecta-5-sensores-de-defensa-de-agentes-ia"
author: "Fenix"
source: "devto_ai"
published: "Mon, 20 Jul 2026 09:22:55 +0000"
description: "agent-shield-runtime v0.1.0: hook de despliegue que conecta 5 sensores de defensa de agentes IA Los sensores de defensa de un agente no sirven si nada los in..."
keywords: "los, sensores, shield, runtime, que, agent, agente, hook"
generated: "2026-07-20T09:25:08.140139"
---

# agent-shield-runtime v0.1.0: hook de despliegue que conecta 5 sensores de defensa de agentes IA

## Overview

agent-shield-runtime v0.1.0: hook de despliegue que conecta 5 sensores de defensa de agentes IA Los sensores de defensa de un agente no sirven si nada los invoca. Este repo intercepta cada tool-call y lo evalúa contra 5 sensores antes de ejecutarlo. El problema En el ecosistema de defensa de agentes IA (scope-lib, adi-shield, wallet-guard, goal-anchor, trajectory-sentinel) los 5 sensores están implementados y auditados. Pero son librerías: nadie los invoca en un agente real. Con los paquetes instalados y sin un hook, el agente ejecuta sus tool-calls directos y los sensores se quedan en disco. La detección que demostramos en tests unitarios no ocurre en producción. La solución agent-shield-runtime es el sexto repositorio: un hook de despliegue que intercepta cada tool-call del agente y lo despacha a los 5 sensores en orden, antes de ejecutarlo: scope-lib — evaluación de alcance (3 criterios, fail-safe). adi-shield — detección de inyección de prompt (ADI) en 5 vectores. wallet-guard — guardrails de bucle y presupuesto. goal-anchor — integridad de objetivo (deriva brusca). trajectory-sentinel — correlación agregada de señales vía bus compartido. Si cualquier sensor dice block , la acción NO se ejecuta. Si hay confirm , se pausa a humano. Solo si todos dicen allow se ejecuta el tool nativo. Cómo funciona El runtime envuelve el executor del agente. El núcleo solo conoce GenericToolCall ; los adaptadores de framework (LangChain, AutoGen, loop propio) traducen el tool-call nativo a ese formato y viven aislados. Así el runtime es reutilizable sin acoplarse a ningún agente concreto, y los 5 sensores no cambian: este repo solo orquesta. Resultados verificados 5 tests de integración end-to-end ( tests/test_integration_e2e.py ) contra los 5 sensores REALES instalados (sin mocks de sensor): AC1 (deny bloquea y no ejecuta), AC2 (inyección ADI bloquea), AC3 (deriva brusca confirma), AC5 (integración sin modificar los sensores). CI verde en GitHub Actions (ruff + pytest + bandit + gitleaks) en entorno limpio. Licencia AGPL-3.0-or-later (texto oficial FSF verbatim). Lo que queda abierto (honestamente) WebTrap sutil no se cierra. El hook extiende la cobertura de despliegue , no la de detección. Los vectores de deriva sutil que preservan apariencia de alcance (T1/T2/T4) siguen sin detectarse en la Capa 1 de goal-anchor (benchmark corregido: TPR=0.25 real, FPR=0.0). Cerrarlos requiere semántica real, descartada por peso en esta fase. Adaptador de framework real pendiente. Hoy solo el adaptador genérico; el cableado al executor nativo de LangChain/AutoGen es el siguiente hito (H3). Auditoría independiente en curso. El repo se hizo público para que un auditor externo lo clone y verifique en fresco. Pruébalo git clone https://github.com/amurlaniakea/agent-shield-runtime.git cd agent-shield-runtime python -m venv .venv && . .venv/bin/activate pip install -e . pytest Stack Componente Rol ShieldRuntime intercepta y decide block/confirm/allow GenericToolCall formato interno neutro LocalSignalBus bus compartido de señales los 5 sensores evaluación por especialidad Links Repo: https://github.com/amurlaniakea/agent-shield-runtime Sensores: scope-lib , adi-shield , wallet-guard , goal-anchor , trajectory-sentinel Licencia: AGPL-3.0-or-later · Autor: Pedro Sordo Martínez

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/magopredator/agent-shield-runtime-v010-hook-de-despliegue-que-conecta-5-sensores-de-defensa-de-agentes-ia-4bg3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
