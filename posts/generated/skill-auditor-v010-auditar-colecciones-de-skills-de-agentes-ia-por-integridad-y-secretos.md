---
title: "skill-auditor v0.1.0: auditar colecciones de skills de agentes IA por integridad y secretos"
slug: "skill-auditor-v010-auditar-colecciones-de-skills-de-agentes-ia-por-integridad-y-secretos"
author: "Fenix"
source: "devto_python"
published: "Tue, 14 Jul 2026 02:24:23 +0000"
description: "skill-auditor v0.1.0: auditar colecciones de skills de agentes IA por integridad y secretos Una CLI agent-agnostic (Hermes primero) que escanea skills por in..."
keywords: "skill, skills, una, por, auditor, hermes, solo, secretos"
generated: "2026-07-14T02:53:42.958788"
---

# skill-auditor v0.1.0: auditar colecciones de skills de agentes IA por integridad y secretos

## Overview

skill-auditor v0.1.0: auditar colecciones de skills de agentes IA por integridad y secretos Una CLI agent-agnostic (Hermes primero) que escanea skills por integridad estructural, referencias rotas y secretos hardcodeados, y clasifica cada skill en lenguaje claro. 95% de cobertura de tests, CI verde. El problema Las colecciones de skills de un agente IA crecen sin revisión: 100–200+ entradas en Hermes, Claude Code, OpenCode o Codex. La superficie de prompts del agente es, en la práctica, código ejecutable que carga comandos y (en skills de seguridad) maneja guía sobre credenciales. Nadie la audita. En una colección real de 200 skills de Hermes, una auditoría directa al filesystem encontró: una carpeta duplicada anidada ( software-development/software-development/software-development/ ) que causaba una colisión de nombre activa en runtime y arrastraba un bug de doble escapado; una referencia rota por typo de acento ( anti-evasión vs anti-evasion ); una referencia perdida sin destino en el repo; varios skills citando scripts/ references que nunca se entregaron. El hygiene de secretos estaba limpio (solo placeholders de documentación), pero "limpio porque lo miré una vez" no es un proceso. skill-auditor lo vuelve repetible. Qué hace Audita cualquier directorio de skills (Hermes es el target primario; es agent-agnostic vía name / description en frontmatter YAML): Chequeo Hallazgo Notas Frontmatter YAML parseable FRONTMATTER_ERROR multilínea `\ {% raw %} name presente NAME_MISSING description presente y ≥15 chars DESC_EMPTY / DESC_SHORT name duplicado NAME_DUPLICADO Carpeta anidada X/X/X NESTED_DUPLICATE solo la copia innermost es eliminable Referencias scripts/ references/ rotas REF_ROTA ignora /tmp , /opt , placeholders Secretos hardcodeados SECRET AWS/GH/OpenAI/Anthropic/Google/Slack/GitLab, claves privadas, asignaciones; filtra placeholders Cada skill recibe una clasificación en lenguaje claro : categoría (carpeta superior), propósito de una línea, y estado OK / WARNING / BROKEN . Reportes en terminal (por defecto), md (una sección por skill) y json (para CI gates). Modo --fix (opt-in, solo seguro) Imprime el diff primero y aplica solo correcciones demostrablemente seguras y reversibles: elimina la carpeta duplicada innermost (conserva la outer canónica); corrige una referencia rota por acento/typo cuando el archivo correcto existe en la misma skill; crea un stub de índice mínimo para una referencia perdida cuyo contenido real vive en otra skill del repo (redirección cross-link, sin contenido técnico inventado). Nunca edita valores de secreto, nunca reescribe la prosa del skill, nunca borra la única copia de un skill. Si hay un hallazgo SECRET sobre un archivo, ningún fix lo toca. Cómo funciona (diseño) Discovery — walk recursivo por SKILL.md , determinista y ordenado. Frontmatter — pyyaml.safe_load con fallback regex conservador si pyyaml no está. Los bloques multilínea se preservan como texto real (un parser regex ingenuo los lee como descripción de 1 char — esa fue la clase de falso positivo exacta de un script ad-hoc previo, y es el test de regresión). Duplicados — colisión de name y auto-anidado X/X/.../X con run-length ≥ 3 (solo el innermost es la copia eliminable). Referencias — extrae menciones y comprueba existencia de archivo dentro de la skill; ignora rutas de runtime, contenedor y placeholders. Secretos — regex sobre todos los archivos de la skill; allowlist de placeholders filtra muestras de documentación. Clasificación — categoría, propósito (primera frase, ≤120 chars), estado derivado de los hallazgos. Reportes — terminal / md / json. Fix — solo seguro, diff-first, secret-safe. Verificación El proyecto se construyó por SDD (Spec-Driven Development) con criterios de aceptación Pass/Fail: 28 tests passed , cobertura medida 95% local y 94.51% en CI (gate --cov-fail-under=85 ). ruff clean ( All checks passed! ). CLI en vivo sobre un fixture de 9 skills: detecta FRONTMATTER_ERROR , REF_ROTA , secreto real (placeholder ignorado), NAME_DUPLICADO , NESTED_DUPLICATE ; --fix elimina solo la carpeta inner y deja la outer intacta; re-audit baja de 9 a 8 skills sin nested. Pipeline GitHub Actions: push / PR → checkout → setup-python 3.11 → install → ruff → pytest con cov≥85 → smoke del CLI. Run real: success . Todas las métricas son salida cruda de pytest --cov y del log de CI, no resumen. Pruébalo pip install -e . # auditoría read-only skill-auditor ~/.hermes/skills # reporte markdown skill-auditor ~/.hermes/skills --report md # JSON para CI skill-auditor ~/.hermes/skills --report json # correcciones seguras (muestra diff, luego aplica) skill-auditor ~/.hermes/skills --fix Stack Python 3.11+, pyyaml (única dependencia de runtime), argparse , pytest , ruff . Licencia AGPL-3.0-or-later. Links Repo: https://github.com/amurlaniakea/skill-auditor Licencia: AGPL-3.0-or-later © 2026 Pedro Sordo Martínez — amurlaniakea@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/magopredator/skill-auditor-v010-auditar-colecciones-de-skills-de-agentes-ia-por-integridad-y-secretos-3m47

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
