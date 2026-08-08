---
title: "Cuando tu clasificador parpadea: histéresis para señales que oscilan"
slug: "cuando-tu-clasificador-parpadea-histresis-para-seales-que-oscilan"
author: "Juan Carlos Isaza"
source: "devto_python"
published: "Sat, 08 Aug 2026 18:19:23 +0000"
description: "Tienes una señal que a cada observación te dice en qué estado estás: un monitor de salud que dice OK o CAÍDO , un detector de conectividad, un clasificador d..."
keywords: "que, estado, para, una, por, con, caido, cada"
generated: "2026-08-08T18:45:17.903154"
---

# Cuando tu clasificador parpadea: histéresis para señales que oscilan

## Overview

Tienes una señal que a cada observación te dice en qué estado estás: un monitor de salud que dice OK o CAÍDO , un detector de conectividad, un clasificador de modo. Y cerca del umbral oscila : OK, CAÍDO, OK, CAÍDO, OK . Cada cambio dispara algo —una alerta, un failover, entrar o salir de una posición— y de repente tu sistema está temblando por ruido, no por una transición real. Es el mismo problema que resuelve el termostato de tu casa desde hace un siglo, y la solución tiene nombre: histéresis . No cambies de estado hasta que el nuevo se haya sostenido. La regla, en una frase Un estado nuevo solo se confirma tras repetirse N observaciones consecutivas. Si el candidato cambia o revierte antes de llegar a N , la cuenta se reinicia. El estado vigente se mantiene estable; los parpadeos se ignoran. Lo empaqueté como librería — hysteresis-state , Python puro, sin dependencias— porque lo reescribía una y otra vez: from hysteresis_state import HysteresisState estado = HysteresisState ( " OK " , confirmations = 3 ) for lectura in stream : # "OK" / "CAIDO" actual = estado . update ( lectura ) # solo cambia tras 3 lecturas seguidas if estado . changed : # ¿esta lectura provocó la transición? alertar ( actual ) Aliméntalo con OK, CAÍDO, OK, CAÍDO, OK y no pasa nada: ningún candidato se sostuvo. Hacen falta tres CAÍDO seguidos para que el cambio se confirme. El detalle que casi siempre falta: histéresis asimétrica Un umbral único tiene un problema sutil. Si exiges 3 confirmaciones para entrar en fallo, también tardas 3 en salir — y a veces quieres justo lo contrario: caer rápido a lo seguro, volver despacio a lo arriesgado . Es el comportamiento de un disyuntor eléctrico: salta a la primera, se rearma con cautela. Se resuelve dejando que el umbral dependa de la transición: # 1 confirmación para caer a "CAIDO", 5 para volver a "OK" conf = lambda desde , hacia : 1 if hacia == " CAIDO " else 5 estado = HysteresisState ( " OK " , confirmations = conf ) estado . update ( " CAIDO " ) # cae al instante # ...ahora hacen falta 5 "OK" seguidos para volver Por qué no basta con "promediar" La tentación es suavizar con una media móvil y umbralizar. Funciona para señales numéricas, pero se rompe con estados discretos (no promedias OK y CAÍDO ), introduce retardo en todas las transiciones por igual, y no te da la asimetría de arriba. La histéresis por confirmación es la herramienta correcta cuando lo que oscila es una etiqueta , no un número. De dónde salió Esto nació dentro de un bot de trading. Su cerebro de régimen clasificaba el mercado en tendencia / rango / caos , y cerca de los umbrales parpadeaba: cada parpadeo congelaba o reactivaba la operativa, que es exactamente lo que no quieres que pase por ruido. La histéresis lo calmó. Pero el mecanismo no sabe nada de mercados —es anti-flapping para cualquier señal discreta—, así que lo liberé. pip install hysteresis-state Código y tests (con los casos límite del conteo y la asimetría, verificados por mutación): github.com/isazajuancarlos/hysteresis-state .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/isazajuancarlos/cuando-tu-clasificador-parpadea-histeresis-para-senales-que-oscilan-1499

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
