---
title: "RAG explicado: cómo darle a un LLM tu propia información"
slug: "rag-explicado-cmo-darle-a-un-llm-tu-propia-informacin"
author: "Juan Carlos Isaza"
source: "devto_python"
published: "Sat, 22 Aug 2026 18:25:06 +0000"
description: "Un modelo de lenguaje sabe mucho del mundo, pero no sabe nada de tu empresa : tus manuales, tus políticas, tus productos. Y si le preguntas por algo que no s..."
keywords: "que, tus, pregunta, con, fragmentos, contexto, una, los"
generated: "2026-08-22T18:37:08.475514"
---

# RAG explicado: cómo darle a un LLM tu propia información

## Overview

Un modelo de lenguaje sabe mucho del mundo, pero no sabe nada de tu empresa : tus manuales, tus políticas, tus productos. Y si le preguntas por algo que no sabe, puede inventar una respuesta que suena convincente. RAG (Retrieval-Augmented Generation) resuelve las dos cosas. La idea En lugar de esperar que el modelo "se sepa" tu información, se la das en el momento de la pregunta : Indexas tus documentos: los divides en fragmentos y los conviertes en embeddings (vectores numéricos que capturan el significado). Cuando llega una pregunta, buscas los fragmentos más parecidos a esa pregunta. Le pasas al LLM la pregunta junto con esos fragmentos y le pides que responda usándolos. El modelo ya no adivina: responde a partir de un contexto real que tú controlas. Y puedes pedirle que cite de dónde salió cada dato. El patrón en Python # 1. Indexado (una vez): fragmentos -> embeddings -> base vectorial # (con librerías como sentence-transformers + FAISS, o un servicio gestionado) # 2. En cada pregunta: recuperar los fragmentos relevantes fragmentos = base_vectorial . buscar ( pregunta , k = 4 ) contexto = " \n\n " . join ( fragmentos ) # 3. Generar la respuesta con el contexto from anthropic import Anthropic client = Anthropic () resp = client . messages . create ( model = " claude-opus-4-8 " , max_tokens = 1024 , system = " Responde SOLO con la información del contexto. Si no está, dilo. " , messages = [{ " role " : " user " , " content " : f " Contexto: \n { contexto } \n\n Pregunta: { pregunta } " , }], ) print ( resp . content [ 0 ]. text ) Fíjate en la instrucción del system : pedirle que responda solo con el contexto y que admita cuando no sabe es lo que reduce drásticamente las alucinaciones. ¿Para qué sirve? Asistentes de soporte que responden con tu documentación real. Búsqueda interna en lenguaje natural sobre tus manuales o wikis. Onboarding : un chatbot que conoce tus procesos. Detalles que marcan la diferencia Cómo divides los documentos (chunking) afecta mucho a la calidad. Buenos embeddings y una base vectorial adecuada importan más que el modelo. Citar las fuentes genera confianza y permite verificar. RAG es hoy una de las formas más rentables de aplicar IA en un negocio: no reentrenas nada, y el asistente mejora con solo actualizar tus documentos. ¿Quieres un asistente con tus datos? En Xiliux construyo sistemas RAG en Python de principio a fin. Cuéntame qué información quieres poner a trabajar: contacto .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/isazajuancarlos/rag-explicado-como-darle-a-un-llm-tu-propia-informacion-2a8b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
