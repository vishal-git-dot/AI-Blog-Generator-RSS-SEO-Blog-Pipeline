---
title: "i18n sin gettext: traducciones en JSON con claves de punto"
slug: "i18n-sin-gettext-traducciones-en-json-con-claves-de-punto"
author: "Juan Carlos Isaza"
source: "devto_python"
published: "Sun, 16 Aug 2026 18:29:59 +0000"
description: "Quieres que tu app hable español e inglés. Buscas cómo, y el ecosistema te empuja a gettext o Babel: ficheros .po , un paso de compilación a .mo , herramient..."
keywords: "idioma, que, por, json, sin, una, translator, con"
generated: "2026-08-16T18:35:30.113718"
---

# i18n sin gettext: traducciones en JSON con claves de punto

## Overview

Quieres que tu app hable español e inglés. Buscas cómo, y el ecosistema te empuja a gettext o Babel: ficheros .po , un paso de compilación a .mo , herramientas de extracción. Potente, sí. Pero para una app pequeña o mediana es un peaje que no querías pagar — solo necesitabas un t() honesto. Lo resolví tantas veces que lo empaqueté: dotkey-i18n , Python puro, sin dependencias. Tus traducciones son JSON que cualquiera puede editar: // locales/es.json { "login" : { "welcome" : "Hola, {name}" , "submit" : "Entrar" }, "menu" : { "reports" : "Informes" , "settings" : "Ajustes" } } from dotkey_i18n import Translator tr = Translator ( " locales " , default_lang = " es " ) tr . t ( " login.welcome " , name = " Juan " ) # "Hola, Juan" tr . t ( " menu.reports " , lang = " en " ) # "Reports" Tres detalles que marcan la diferencia Claves con notación de punto. t("login.submit") navega el JSON anidado. Agrupas las cadenas por pantalla o módulo sin claves planas kilométricas. Fallback al idioma por defecto. Si una clave falta en el idioma pedido, se busca en el idioma por defecto antes de rendirse. Tus traducciones pueden ir incompletas —la vida real— sin dejar huecos en blanco en la interfaz. Nunca revienta la interfaz. Una clave que no existe devuelve la propia clave (un marcador visible, no una excepción a mitad de render). Una interpolación con un campo que falta devuelve el texto sin formatear. Un JSON corrupto se trata como vacío. Nada de esto tumba la pantalla. Agnóstico del framework El idioma actual entra por un lang_getter inyectable, así el mismo Translator sirve en NiceGUI, Flask, FastAPI o un script suelto: # NiceGUI: idioma desde la sesión del usuario tr = Translator ( " locales " , default_lang = " es " , lang_getter = lambda : app . storage . user . get ( " idioma " )) # Flask tr = Translator ( " locales " , lang_getter = lambda : session . get ( " lang " )) La prioridad es clara: lang= explícito → lang_getter() → idioma por defecto. De dónde viene Salió del servicio i18n de un sistema de gestión de informes bilingüe. Estaba atado al framework —leía el idioma directamente de la sesión de NiceGUI—; al extraerlo se desacopló con el lang_getter , y se le añadió el fallback al idioma por defecto que el original no tenía. Extraer para publicar suele mejorar el código original: lo obliga a no depender de su casa. pip install dotkey-i18n Código y tests (notación de punto, fallback, claves ausentes, JSON corrupto; verificados por mutación): github.com/isazajuancarlos/dotkey-i18n .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/isazajuancarlos/i18n-sin-gettext-traducciones-en-json-con-claves-de-punto-48fd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
