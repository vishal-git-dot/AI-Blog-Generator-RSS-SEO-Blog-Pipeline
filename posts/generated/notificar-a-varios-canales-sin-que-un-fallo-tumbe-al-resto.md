---
title: "Notificar a varios canales sin que un fallo tumbe al resto"
slug: "notificar-a-varios-canales-sin-que-un-fallo-tumbe-al-resto"
author: "Juan Carlos Isaza"
source: "devto_python"
published: "Sat, 15 Aug 2026 18:28:19 +0000"
description: "Quieres mandar la misma notificación a varios sitios: Slack, Discord, un webhook, un email. La primera versión es un for de tres líneas: for canal in canales..."
keywords: "que, report, canal, por, cada, discord, broadcast, canales"
generated: "2026-08-15T18:36:33.512295"
---

# Notificar a varios canales sin que un fallo tumbe al resto

## Overview

Quieres mandar la misma notificación a varios sitios: Slack, Discord, un webhook, un email. La primera versión es un for de tres líneas: for canal in canales : canal ( mensaje ) Y funciona en las demos. Hasta que un día Discord devuelve un 500, canal(mensaje) lanza, y el email y el Slack que iban detrás nunca salen . Peor: te enteras por el usuario que no recibió la alerta, no por un log. Dos cosas fallan en ese for : No aísla. La primera excepción corta el reparto entero. No reporta. O cada canal se traga su error en un try/except disperso, o el fallo se pierde. La forma correcta Aísla cada canal y recoge el resultado. Lo empaqueté como fanout-broadcast —Python puro, sin dependencias— porque lo reescribía en cada proyecto: from fanout_broadcast import Broadcaster bc = Broadcaster () bc . add ( " discord " , a_discord ) bc . add ( " telegram " , a_telegram ) bc . add ( " email " , a_email , enabled = False ) # apagado por ahora report = bc . broadcast ( " ¡Nueva versión publicada! " ) if not report . ok : for o in report . failed : log . error ( " %s falló: %s " , o . name , o . error ) broadcast llama a todos los canales habilitados, captura la excepción de cada uno por separado , y sigue con el siguiente. Un Discord caído ya no impide que salga el email. Al final tienes un reporte: report . ok # ¿ningún canal falló? report . delivered # los que entregaron report . failed # los que lanzaron (cada uno con su .error) report . skipped # los que estaban deshabilitados Encender y apagar sin ramificar el código Cada canal tiene un interruptor, en runtime o por variable de entorno: from fanout_broadcast import env_enabled bc . add ( " discord " , a_discord , enabled = env_enabled ( " discord " )) # mira DISCORD_ENABLED Esto importa más de lo que parece: separa qué canales existen de cuáles están activos hoy , sin comentar código ni meter if por todos lados. Apagas un canal problemático con una variable de entorno, no con un despliegue. Escalar, pero después de intentarlo todo A veces sí quieres que un fallo se propague. La diferencia está en cuándo : report = bc . broadcast ( mensaje ) report . raise_for_failures () # lanza DESPUÉS de haber intentado todos Al revés que el for ingenuo, que aborta en el primero. Intentas todos los canales, y solo entonces decides si el conjunto fue un fracaso. De dónde viene Salió de un agente que publicaba en varias redes a la vez. Extraje solo la fontanería: qué se publica y a quién es la lógica de cada aplicación; el cómo repartir con aislamiento y reporte es genérico, y sirve igual para notificaciones, alertas o webhooks. Por eso es una librería, no un for . pip install fanout-broadcast Código y tests (centrados en el aislamiento de fallos, verificados por mutación): github.com/isazajuancarlos/fanout-broadcast .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/isazajuancarlos/notificar-a-varios-canales-sin-que-un-fallo-tumbe-al-resto-3b5a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
