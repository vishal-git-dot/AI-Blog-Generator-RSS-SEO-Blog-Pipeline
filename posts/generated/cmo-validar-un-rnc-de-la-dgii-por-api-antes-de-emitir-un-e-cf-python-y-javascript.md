---
title: "Cómo validar un RNC de la DGII por API antes de emitir un e-CF (Python y JavaScript)"
slug: "cmo-validar-un-rnc-de-la-dgii-por-api-antes-de-emitir-un-e-cf-python-y-javascript"
author: "OpenData CR"
source: "devto_python"
published: "Sun, 25 Oct 2026 03:32:42 +0000"
description: "Por OpenData CR La DGII extendió hasta el 15 de noviembre de 2026 el plazo de facturación electrónica (e-CF) para contribuyentes pequeños, micros y no clasif..."
keywords: "rnc, code, client, por, del, item, dgii, opendata"
generated: "2026-10-25T04:06:12.672862"
---

# Cómo validar un RNC de la DGII por API antes de emitir un e-CF (Python y JavaScript)

## Overview

Por OpenData CR La DGII extendió hasta el 15 de noviembre de 2026 el plazo de facturación electrónica (e-CF) para contribuyentes pequeños, micros y no clasificados ( aviso de la DGII del 6 de mayo de 2026 ). Si mantiene un ERP, un sistema de facturación o una tienda en línea en República Dominicana, conviene confirmar que el RNC del comprador existe y está activo antes de emitir el comprobante. En este tutorial usamos el Validador de RNC DGII de OpenData CR, que trabaja sobre el padrón público de contribuyentes que publica la DGII ( DGII_RNC.zip ). Qué valida Para cada valor enviado devuelve: formato, dígito verificador, si está en el padrón, estado, razón social, nombre comercial, actividad económica y régimen (NORMAL o RST). Regla práctica para aceptar un RNC en facturación: code == " active " and checkDigitValid == true code Significado active En el padrón, estado ACTIVO inactive En el padrón, con otro estado not_found 9 dígitos, no está en el padrón cedula_not_supported 11 dígitos (persona física): no se consulta invalid_format Otra cantidad de dígitos Guiones, espacios y puntos se ignoran: 1-01-01063-2 y 101010632 son el mismo RNC. Python from apify_client import ApifyClient client = ApifyClient ( " SU_TOKEN_DE_APIFY " ) run = client . actor ( " opendata-cr/dominican-rnc-validator " ). call ( run_input = { " mode " : " validate " , " rncs " : [ " 1-01-01063-2 " , " 101003723 " ]} ) for item in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): ok = item [ " code " ] == " active " and item [ " checkDigitValid " ] print ( item [ " rncFormatted " ], item . get ( " razonSocial " ), " OK " if ok else item [ " code " ]) JavaScript (Node) import { ApifyClient } from ' apify-client ' ; const client = new ApifyClient ({ token : process . env . APIFY_TOKEN }); const run = await client . actor ( ' opendata-cr/dominican-rnc-validator ' ). call ({ mode : ' validate ' , rncs : [ ' 1-01-01063-2 ' , ' 101003723 ' ], }); const { items } = await client . dataset ( run . defaultDatasetId ). listItems (); for ( const i of items ) { const ok = i . code === ' active ' && i . checkDigitValid ; console . log ( i . rncFormatted , i . razonSocial , ok ? ' OK ' : i . code ); } Respuesta de ejemplo (recortada) { "input" : "1-01-01063-2" , "rncFormatted" : "1-01-01063-2" , "checkDigitValid" : true , "found" : true , "code" : "active" , "razonSocial" : "BANCO POPULAR DOMINICANO S A BANCO MULTIPLE" , "nombreComercial" : "BANCO POPULAR DOMINICANO" , "actividadEconomica" : "BANCOS MULTIPLES" , "status" : "ACTIVO" , "regimenPagos" : "NORMAL" , "isActive" : true , "padronFecha" : "2026-10-03" } Cada fila indica la fecha del archivo del padrón usado ( padronFecha ), útil para auditoría. Buscar o exportar empresas Además de validar, puede buscar en el padrón por nombre, actividad o estado: { "mode" : "search" , "nameContains" : "EDENORTE DOMINICANA" , "onlyActive" : true , "maxResults" : 10 } Costo Pago por uso (según la página del Actor): US$0,003 por RNC validado (encontrado o no); US$0,0005 por empresa en búsqueda/exportación; cédulas y valores mal formados no se cobran. Ejemplo publicado: validar 1.000 RNC cuesta US$3. Límites No consulta cédulas (personas físicas). Trabaja con el último archivo público del padrón, no con la Oficina Virtual en tiempo real. ¿Comentarios o casos de uso? Déjelos abajo. Herramienta: https://apify.com/opendata-cr/dominican-rnc-validator

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/opendatacr/como-validar-un-rnc-de-la-dgii-por-api-antes-de-emitir-un-e-cf-python-y-javascript-308a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
