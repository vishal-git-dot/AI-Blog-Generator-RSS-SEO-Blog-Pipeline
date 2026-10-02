---
title: "FastAPI: emails de prueba con un buzón por ejecución"
slug: "fastapi-emails-de-prueba-con-un-buzn-por-ejecucin"
author: "Olivia Cheng"
source: "devto_python"
published: "Fri, 02 Oct 2026 11:23:25 +0000"
description: "Cuando una API envía un email de verificación, el test suele parecer sencillo: crear usuario, esperar el mensaje y abrir el enlace. El problema aparece cuand..."
keywords: "una, que, test, puede, con, mensaje, del, para"
generated: "2026-10-02T12:13:45.781983"
---

# FastAPI: emails de prueba con un buzón por ejecución

## Overview

Cuando una API envía un email de verificación, el test suele parecer sencillo: crear usuario, esperar el mensaje y abrir el enlace. El problema aparece cuando varios tests comparten el mismo buzón. Un mensaje viejo puede pasar por nuevo, un reintento puede leer el token de otra ejecución y el fallo termina siendo dificil de reproducir. En proyectos con FastAPI he encontrado una solución muy práctica: cada ejecución debe tener su propio buzón lógico, su propio identificador de correlación y una fecha clara de expiración. No hace falta convertir el test en una plataforma enorme. Hace falta que sus datos no se mezclen. El problema de compartir un buzón de prueba Un buzón compartido parece cómodo al principio. El equipo configura una dirección, añade una función para leer el último mensaje y todos los tests avanzan. Pero “el último” no es una propiedad estable cuando hay paralelismo. Los fallos más comunes son estos: Un test encuentra un email de la ejecución anterior. Dos usuarios de prueba reciben mensajes y el filtro solo mira el asunto. Un reintento consume el mismo token que el primer intento. El CI guarda el cuerpo completo del email en un artefacto. La limpieza depende de que el test termine sin errores. Incluso una búsqueda escrita como dummy e mail puede llegar a los logs de soporte. Por eso conviene que la fixture sea legible para una persona, pero que no dependa de interpretar texto libre para saber a qué ejecución pertenece. Qué debe garantizar cada ejecución Mi contrato mínimo tiene cuatro piezas: Identidad única. Genera un run_id y úsalo en la dirección o en el identificador del buzón. Lectura acotada. Busca mensajes después de la hora de inicio, con un destinatario exacto y un asunto conocido. Consumo idempotente. Leer dos veces el mismo mensaje no debe cambiar el resultado del test. Expiración. El buzón y sus mensajes deben poder eliminarse aunque la aserción falle. La dirección no tiene que ser bonita. Algo como qa+run-8f31@example.test comunica más que una dirección fija. También hace más fácil relacionar una petición de FastAPI con el mensaje que la API generó. Esto se parece a medir señales útiles en un onboarding SaaS: no necesitas guardar todo para entender qué pasó. Necesitas escoger señales que permitan reconstruir la secuencia. Un fixture sencillo para FastAPI El siguiente ejemplo muestra la forma del contrato. InboxClient representa el proveedor de buzones de prueba y puede ser un fake local durante los tests unitarios. from dataclasses import dataclass from uuid import uuid4 @dataclass class EmailFixture : address : str run_id : str @classmethod async def create ( cls , inbox_client ) -> " EmailFixture " : run_id = uuid4 (). hex [: 12 ] address = await inbox_client . create_inbox ( label = f " fastapi- { run_id } " ) return cls ( address = address , run_id = run_id ) async def wait_for_verification ( self , inbox_client , timeout = 20 ): return await inbox_client . wait_for ( recipient = self . address , subject = " Verifica tu cuenta " , timeout = timeout , ) async def close ( self , inbox_client ): await inbox_client . delete_inbox ( self . address ) En un test de FastAPI, el cierre debe estar en un bloque finally , no después de la última aserción. Si la aserción falla, el código posterior no se ejecuta. Es un detalle pequeño, pero suele ser la diferencia entre un CI limpio y una colección de buzones abandonados. fixture = await EmailFixture . create ( inbox_client ) try : response = await client . post ( " /signup " , json = { " email " : fixture . address , " password " : " example-only " }, ) assert response . status_code == 201 message = await fixture . wait_for_verification ( inbox_client ) assert " /verify?token= " in message . text finally : await fixture . close ( inbox_client ) El timeout también es parte del diseño. Si cada test espera indefinidamente, una incidencia de entrega puede congelar toda la automatización. Devuelve un error con el run_id , el destinatario y el último estado conocido, pero no con el token completo. Automatizar la limpieza y la evidencia La limpieza debe tener dos capas. Primero, el test intenta borrar su buzón. Segundo, una tarea periódica elimina recursos cuyo expires_at ya pasó. Así, un proceso cancelado no deja datos para siempre. Para depurar, conserva solo evidencia útil: run_id , estado HTTP, identificador del mensaje, timestamps y una versión redactada del asunto. No guardes enlaces de verificación completos en los logs del CI. Esa información hace que un fallo de prueba sea un riesgo innecesario. También ayuda mostrar el estado al desarrollador. Una interfaz con una interfaz React que mantiene el contexto puede enseñar “email solicitado”, “mensaje recibido” y “token consumido” sin saltos confusos. El backend sigue siendo la fuente de verdad, pero la UI no deberia esconder el estado real. Checklist final Antes de dar por terminada la fixture, compruebo lo siguiente: Cada ejecución crea una identidad de buzón diferente. El filtro combina destinatario, asunto y hora de inicio. Un mensaje no se consume dos veces por accidente. El finally elimina el buzón incluso si una aserción falla. Existe una limpieza de respaldo por expiración. Los logs no contienen tokens completos ni cuerpos innecesarios. El timeout produce un diagnóstico accionable. Con este contrato, las pruebas de email dejan de depender de la suerte. La API puede reintentarse, el CI puede ejecutar varios casos en paralelo y el equipo puede leer un fallo sin adivinar qué buzón pertenecia a qué ejecución. Es una mejora pequeña, pero se nota rápido cuando el proyecto crece.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/oliviachen7/fastapi-emails-de-prueba-con-un-buzon-por-ejecucion-m9e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
