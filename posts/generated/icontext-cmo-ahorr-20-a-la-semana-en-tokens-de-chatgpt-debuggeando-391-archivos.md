---
title: "iContext: Cómo ahorré $20 a la semana en tokens de ChatGPT debuggeando 391 archivos"
slug: "icontext-cmo-ahorr-20-a-la-semana-en-tokens-de-chatgpt-debuggeando-391-archivos"
author: "A&L digital"
source: "devto_python"
published: "Fri, 07 Aug 2026 06:35:31 +0000"
description: "El problema: perder dinero y tiempo con IA ¿Cuántas veces has pegado 5,000 líneas de código en ChatGPT esperando una solución y la IA: Alucina imports que no..."
keywords: "icontext, archivos, src, que, tokens, con, proyecto, contexto"
generated: "2026-08-07T07:23:56.535322"
---

# iContext: Cómo ahorré $20 a la semana en tokens de ChatGPT debuggeando 391 archivos

## Overview

El problema: perder dinero y tiempo con IA ¿Cuántas veces has pegado 5,000 líneas de código en ChatGPT esperando una solución y la IA: Alucina imports que no existen Sugiere arreglos para archivos que ni siquiera tienes Te pide que le des contexto de 10 archivos diferentes Te cobra $20 a la semana en tokens desperdiciados Yo pasé por eso. Y me harté. La solución: iContext iContext es una herramienta CLI que escanea tu repositorio y le da a la IA el contexto exacto que necesita – sin que le expliques nada. ¿Qué detecta? ✅ Lenguaje y stack (Python, Node, Rust, Go, etc.) ✅ Puntos de entrada (main.py, app.js, Dockerfile...) ✅ Archivos modificados en las últimas 72h (actividad reciente) ✅ TODOs y FIXMEs (trabajo pendiente) ✅ Áreas activas del proyecto (dónde está ocurriendo el desarrollo) ✅ El siguiente paso lógico (para no perder el hilo) Ejemplo de salida real Esto es lo que me devolvió iContext en mi proyecto de 391 archivos en Python: 📁 PROYECTO: mi-api 📄 ARCHIVOS: 391 🔤 LENGUAJE: Python 📦 STACK: Python → FastAPI → SQLAlchemy ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ARQUITECTURA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ✓ src/ ✓ tests/ ✓ docs/ ✓ migrations/ 🚀 PUNTOS DE ENTRADA: main.py, app.py 🔀 RAMA GIT: feature/auth 📝 CAMBIOS SIN COMMIT: 3 M src/auth.py M src/models/user.py ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ACTIVIDAD RECIENTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 08-06 14:32 src/auth.py 08-06 10:15 src/models/user.py 08-05 18:22 src/routes/api.py ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PENDIENTES / TODOs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ → src/auth.py:42 | TODO: Implement JWT refresh → src/routes/api.py:15 | FIXME: Optimize query ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SIGUIENTE PASO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ → Verificar conexión entre auth y user services. Con eso, le pego el output a ChatGPT y la IA entiende el proyecto en 5 segundos. ¿Cómo ahorra tokens? Antes (sin iContext): Pegaba 5-10 archivos manualmente (3,000-5,000 líneas) Gastaba ~10,000 tokens por consulta La IA adivinaba el contexto → respuestas erróneas $20 a la semana en tokens desperdiciados Después (con iContext): 1 comando: ./iContext Output de ~200 líneas (contexto estructurado) Gasto: 95% menos tokens La IA da respuestas precisas en el primer intento Resultado: de horas a 5 minutos de debugging. ¿Cómo se instala? git clone https://github.com/dulcevenganza666777-lang/icontext- cd icontext- chmod +x iContext ./iContext Eso es todo. No necesitas API keys, ni cuenta en la nube, ni configuraciones complejas. Casos de uso reales 1. Debuggear un proyecto legacy "Me bajé un repo de 5 años, no sabía ni por dónde empezar. iContext me dijo los archivos activos, los TODOs y el siguiente paso. En 30 min ya había arreglado el bug principal." 2. Unirse a un equipo nuevo "Llegué a un proyecto con 200+ archivos. iContext me dio el mapa en segundos. Supe dónde estaba la lógica principal sin preguntarle a nadie." 3. Usar IA sin gastar una fortuna "Dejé de pegar 5,000 líneas. Ahora pego 200 líneas de contexto y ChatGPT me da respuestas perfectas. Ahorro $20 a la semana." El futuro de iContext [ ] Soporte para más lenguajes (JavaScript, Rust, Go) [ ] Integración con VS Code [ ] Salida en formato JSON para automatizar [ ] Detección de dependencias obsoletas ¿Quieres probarlo? El repo está en GitHub: 🔗 https://github.com/dulcevenganza666777-lang/icontext- ⭐ Si te sirve, dale una estrella. 🐛 Si encuentras bugs, abre un issue. 💡 Si tienes ideas, abre un PR. Hecho con ❤️ por dulcevenganza666777-lang

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/al_digital_d5f0bc61c6c76/icontext-como-ahorre-20-a-la-semana-en-tokens-de-chatgpt-debuggeando-391-archivos-33j1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
