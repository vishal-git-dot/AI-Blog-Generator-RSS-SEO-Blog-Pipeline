---
title: "citefid 0.1.0: verificar la fidelidad de citas en wikis OKF con NLI (AUC 0.7029 sobre código)"
slug: "citefid-010-verificar-la-fidelidad-de-citas-en-wikis-okf-con-nli-auc-07029-sobre-cdigo"
author: "Fenix"
source: "devto_python"
published: "Thu, 16 Jul 2026 02:28:38 +0000"
description: "citefid 0.1.0: verificar la fidelidad de citas en wikis OKF con NLI (AUC 0.70 sobre código) Los generadores de wikis OKF comprueban que la cita existe, no qu..."
keywords: "que, del, nli, sobre, por, sin, auc, citefid"
generated: "2026-07-16T03:13:36.752273"
---

# citefid 0.1.0: verificar la fidelidad de citas en wikis OKF con NLI (AUC 0.7029 sobre código)

## Overview

citefid 0.1.0: verificar la fidelidad de citas en wikis OKF con NLI (AUC 0.70 sobre código) Los generadores de wikis OKF comprueban que la cita existe, no que su contenido respalde la afirmación. citefid cierra esa brecha: verifica fidelidad, no existencia. El problema Los wikis de conocimiento generados por LLM que siguen el estándar OKF (Open Knowledge Format) incluyen citas a fragmentos de código o documentación. El pipeline típico valida que el archivo citado exista y que el rango de líneas sea válido. Eso no dice nada sobre si el fragmento confirma lo que el texto afirma. La literatura documenta el hueco: citas que apuntan a fuentes que no respaldan el claim (CiteCheck; "Cited but Not Verified"; grounding engañoso). Un lector que confía en la wiki hereda una afirmación sin verificar. citefid no genera wikis. Toma un claim y su cita, y responde si el fragmento fuente lo confirma , contradice o es neutral . Lo que no es No genera wikis OKF (eso lo hacen otras herramientas; citefid verifica después del build). No resuelve fuentes externas fueras del bundle citado (web/PDF ajenos). No hace verificación multi-hop ni razonamiento profundo (MVP: un pasaje por cita). Cómo funciona Pipeline determinista en tres pasos: resolve — La cita se resuelve a su fragmento fuente. Código/CRD: URL blob/<commit>/<path>#Lx-Ly → descarga el archivo en ese commit y recorta las líneas. Prosa: ^[slug.md] → resuelve por prefijo-hash (el archivo real lleva sufijo de hash), exigiendo coincidencia única. retrieve — Recupera el párrafo relevante antes de verificar. Híbrido: keyword primero (tokens distintivos del claim), embeddings (MiniLM) como tie-break. Salta frontmatter YAML. Este paso es obligatorio, no opcional. verify — NLI ( cross-encoder/nli-deberta-v3-small , CPU, sin API key) sobre el pasaje recuperado, agregando sobre N evidencias (soporte = máx. entail − contra). Emite reporte CSV/JSON por-evidencia, determinista. Por qué el retrieve es obligatorio (no decoración) El fallo más caro del desarrollo fue creer que NLI sobre el documento entero bastaba. NLI sobre span[:1500] (truncado) daba un AUC engañoso de 0.92 en prosa: el hecho real estaba más allá del carácter 1500 y el modelo solo veía el frontmatter, "confirmando" por contexto temático. Sin recuperar el pasaje correcto, cualquier número de prosa es humo. De ahí que retrieve sea un paso duro del pipeline. Resultados (con metodología, sin redondear) Sobre el único terreno auditado sin fallos — código/CRD de un claim-ledger real (crossplane), 206 pares (128 fieles / 78 infieles), spans recortados a rango de líneas: Configuración AUC (fiel vs. infiel) NLI sobre span[:1500] 0.7029 NLI sobre pasaje recuperado 0.7219 AUC = P(soporte de par fiel > soporte de par infiel). El label NLI se resuelve por nombre del id2label del modelo, no por índice hardcodeado (un bug de índice que cazamos en implementación daba entail 0.99 incluso a texto de tema ajeno). Prosa larga: sin número fiable. Tres intentos de medir fueron invalidados por defectos de construcción del dataset. No se publica un AUC de prosa. El +0.019 del retrieve está en el orden del ruido sin intervalo de confianza; se justifica cualitativamente (no truncar, saltar frontmatter), no como número. Reproducibilidad El AUC citado es reproducible por cualquiera. El dataset (206 pares) y el script viven en evaluation/ : pip install -e ".[dev]" python evaluation/evaluate.py # AUC (NLI sobre pasaje recuperado) = 0.7219 Estado del proyecto Fase 1 de 3 — MVP funcional y verificado. Lo que queda abierto, honestamente: Fase 2: capa LLM-as-judge para código/CRD y zona gris numérica. Sin validar todavía. Prosa larga sin AUC fiable (tres intentos invalidados por dataset defectuoso). El ciclo de construcción siguió implementación → auditoría independiente en clone limpio → corrección. El bug crítico de label NLI lo encontró la auditoría, no el self-report, y quedó documentado con el dato crudo. Stack Python ≥ 3.12, CPU-only, sin API key. sentence-transformers (all-MiniLM-L6-v2, nli-deberta-v3-small), scikit-learn . CI: ruff + pytest + bandit→SARIF + gitleaks + SonarCloud (condicional). Licencia: AGPL-3.0-or-later. Links Repo: https://github.com/amurlaniakea/citefid RESEARCH.md: metodología completa y hallazgos del spike Licencia: AGPL-3.0-or-later — Copyright (C) 2026 Pedro Sordo Martínez amurlaniakea@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/magopredator/citefid-010-verificar-la-fidelidad-de-citas-en-wikis-okf-con-nli-auc-070-sobre-codigo-1ojf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
