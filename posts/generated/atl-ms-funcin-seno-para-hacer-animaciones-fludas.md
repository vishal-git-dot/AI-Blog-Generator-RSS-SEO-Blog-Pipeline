---
title: "ATL más Función Seno para hacer animaciones fluídas."
slug: "atl-ms-funcin-seno-para-hacer-animaciones-fludas"
author: "Lily"
source: "devto_python"
published: "Tue, 23 Jun 2026 03:33:10 +0000"
description: "# 1. Mantenemos el transform del "Baile de los Números" init python : import math def efecto_holograma_avanzado ( trans , st , at ): # Movimiento vertical us..."
keywords: "int, renpy, color, return, append, para, def, colores"
generated: "2026-06-23T04:02:13.417804"
---

# ATL más Función Seno para hacer animaciones fluídas.

## Overview

# 1. Mantenemos el transform del "Baile de los Números" init python : import math def efecto_holograma_avanzado ( trans , st , at ): # Movimiento vertical usando enteros para cuidar la GPU trans . yoffset = int ( math . sin ( st * 2.5 ) * 12 ) # Parpadeo de luz con desfase de velocidad (4.0) seno_luz = math . sin ( st * 4.0 ) opacidad_limpia = ( seno_luz + 1.0 ) / 2.0 trans . alpha = 0.4 + ( opacidad_limpia * 0.6 ) return 0 transform baile_holograma : function efecto_holograma_avanzado # 2. Aquí va la lógica de 3 colores (segmentar_en_doble_gradiente) init python : # Función auxiliar para convertir HEX (#ffffff) a tupla RGB (255, 255, 255) def hex_a_rgb ( hex_str ): return [ int ( hex_str [ 1 : 3 ], 16 ), int ( hex_str [ 3 : 5 ], 16 ), int ( hex_str [ 5 : 7 ], 16 )] # 1. Función interna que maneja 3 colores (dos tramos de degradado) def segmentar_en_doble_gradiente ( texto_puro , c1 , c2 , c3 ): r1 , g1 , b1 = hex_a_rgb ( c1 ) r2 , g2 , b2 = hex_a_rgb ( c2 ) r3 , g3 , b3 = hex_a_rgb ( c3 ) tokens_finales = [] largo = len ( texto_puro ) if largo <= 1 : tokens_finales . append (( renpy . TEXT_TAG , f " color= { c1 } " )) tokens_finales . append (( renpy . TEXT_TEXT , texto_puro )) tokens_finales . append (( renpy . TEXT_TAG , " /color " )) return tokens_finales for i , letra in enumerate ( texto_puro ): if letra == " " : tokens_finales . append (( renpy . TEXT_TEXT , " " )) continue # Calculamos el progreso total (de 0.0 a 1.0) progreso_total = i / ( largo - 1 ) if progreso_total < 0.5 : # PRIMER TRAMO: De Color 1 a Color 2 # Normalizamos el progreso para que vaya de 0.0 a 1.0 en esta mitad t = progreso_total * 2.0 r = int ( r1 + ( r2 - r1 ) * t ) g = int ( g1 + ( g2 - g1 ) * t ) b = int ( b1 + ( b2 - b1 ) * t ) else : # SEGUNDO TRAMO: De Color 2 a Color 3 # Normalizamos el progreso para que vaya de 0.0 a 1.0 en esta mitad t = ( progreso_total - 0.5 ) * 2.0 r = int ( r2 + ( r3 - r2 ) * t ) g = int ( g2 + ( g3 - g2 ) * t ) b = int ( b2 + ( b3 - b2 ) * t ) hex_color = f " # { r : 02 x }{ g : 02 x }{ b : 02 x } " tokens_finales . append (( renpy . TEXT_TAG , f " color= { hex_color } " )) tokens_finales . append (( renpy . TEXT_TEXT , letra )) tokens_finales . append (( renpy . TEXT_TAG , " /color " )) return tokens_finales # 2. etiquetas personalizadas de 3 colores def etiqueta_cyberpunk ( tag , argument , contents ): texto_puro = "" . join ([ c for t , c in contents if t == renpy . TEXT_TEXT ]) # Ejemplo: Azul -> Rosa -> Amarillo return segmentar_en_doble_gradiente ( texto_puro , " #00c6ff " , " #ff007f " , " #ffee00 " ) def etiqueta_fuego ( tag , argument , contents ): texto_puro = "" . join ([ c for t , c in contents if t == renpy . TEXT_TEXT ]) # Ejemplo: Rojo -> Naranja -> Amarillo return segmentar_en_doble_gradiente ( texto_puro , " #ff0000 " , " #ff7f00 " , " #ffee00 " ) # 3. Registro en Ren'Py config . custom_text_tags [ " cyberpunk " ] = etiqueta_cyberpunk config . custom_text_tags [ " fuego " ] = etiqueta_fuego define n = Character ( "" , color = " #ff0 " , size = 24 ) label start : scene black with fade # Fusionamos el degradado de 3 colores con el movimiento matemático show text " {size=50}{b}{cyberpunk}SISTEMA DE SEGURIDAD ACTIVADO{/cyberpunk}{/b}{/size} " at baile_holograma : xalign 0.5 yalign 0.5 n " ¡Boom! El texto no solo tiene tres colores degradados letra por letra, sino que flota y parpadea como un holograma real. " hide text with dissolve return

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abrazos_programacion/atl-mas-funcion-seno-para-hacer-animaciones-fluidas-2k9h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
