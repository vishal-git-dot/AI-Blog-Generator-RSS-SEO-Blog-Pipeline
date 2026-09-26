---
title: "Cifrado al vuelo: encrypt() y decrypt() directo con auto-JSON."
slug: "cifrado-al-vuelo-encrypt-y-decrypt-directo-con-auto-json"
author: "William Rodriguez"
source: "devto_python"
published: "Sat, 26 Sep 2026 11:05:49 +0000"
description: "Cifrar cargas para colas de eventos no debería obligarte a serializar JSON y convertir bytes a mano. encrypt() y decrypt() de wauth procesan strings, listas ..."
keywords: "json, auth, encrypt, decrypt, para, wauth, con, auto"
generated: "2026-09-26T11:08:04.532043"
---

# Cifrado al vuelo: encrypt() y decrypt() directo con auto-JSON.

## Overview

Cifrar cargas para colas de eventos no debería obligarte a serializar JSON y convertir bytes a mano. encrypt() y decrypt() de wauth procesan strings, listas y diccionarios con total transparencia. Esta es la implementación exacta para producción de Direct encrypt() & decrypt() with Auto-JSON : from wauth import WAuth auth = WAuth () # 1. Direct String Encryption token = auth . encrypt ( " Sensitive payload for Kafka topic " ) original_text = auth . decrypt ( token ) # 2. Direct Dictionary (Auto-JSON) Encryption session = { " user_id " : 9941 , " role " : " superadmin " , " permissions " : [ " read " , " write " , " audit " ] } # Automatically serialized to JSON before AES encryption encrypted_token = auth . encrypt ( session ) # Automatically deserialized back into a real Python dictionary! restored_session = auth . decrypt ( encrypted_token ) print ( f " Restored role: { restored_session [ ' role ' ] } " ) Ventajas de ingeniería: Primitivas Directas: auth.encrypt(payload) y auth.decrypt(token) sin escribir en base de datos. Auto-Serialización JSON: Serializa y deserializa tipos dict y list de forma transparente. Listo para Streaming: Ideal para sellar eventos de Kafka, cargas en Redis y webhooks HTTP. Problemas eliminados: Necesidad de cifrar payloads JSON para colas de mensajería sin querer guardarlos en base de datos Hacer malabares con json.dumps() y conversiones de bytes antes de invocar la criptografía Estructuras de diccionarios corruptas por errores manuales de codificación y decodificación Explora el código fuente abierto y auditado en GitHub o instálalo con: pip install wauth Autor: William Steve Rodríguez Villamizar (Wisrovi)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/william_rodriguez_65a5898/cifrado-al-vuelo-encrypt-y-decrypt-directo-con-auto-json-4d90

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
