---
title: "¿Son los subtítulos automáticos de YouTube lo bastante exactos para citarlos?"
slug: "son-los-subttulos-automticos-de-youtube-lo-bastante-exactos-para-citarlos"
author: "Hanako H."
source: "devto_python"
published: "Sat, 07 Nov 2026 21:16:30 +0000"
description: "La mayoría de los vídeos de YouTube tienen transcripción, y en casi todos la escribió un reconocedor de voz. Para seguir el vídeo basta. Para una cita en un ..."
keywords: "una, que, las, pista, con, tracks, para, dos"
generated: "2026-11-07T21:39:06.285432"
---

# ¿Son los subtítulos automáticos de YouTube lo bastante exactos para citarlos?

## Overview

La mayoría de los vídeos de YouTube tienen transcripción, y en casi todos la escribió un reconocedor de voz. Para seguir el vídeo basta. Para una cita en un trabajo académico, una noticia o una nota legal, la pregunta es cuánto se aleja el texto automático de lo que se dijo y si sus marcas de tiempo apuntan al segundo correcto. Un vídeo que tiene los dos tipos de subtítulos da una respuesta directa. El vídeo es la subida de la NASA del discurso del presidente Kennedy en la Universidad de Rice en 1962 ( WZyRbnpGyzQ , 18 minutos). Tiene dos pistas en inglés: una escrita por una persona y otra generada por YouTube. Las dos se pueden listar y descargar con el paquete de Python youtube-transcript-api : from youtube_transcript_api import YouTubeTranscriptApi tracks = YouTubeTranscriptApi (). list ( " WZyRbnpGyzQ " ) for t in tracks : print ( t . language_code , t . is_generated , t . language ) # en False English - Caption # en True English (auto-generated) manual = tracks . find_manually_created_transcript ([ " en " ]). fetch (). to_raw_data () auto = tracks . find_generated_transcript ([ " en " ]). fetch (). to_raw_data () Cada entrada es una línea de texto con un tiempo de inicio y una duración en segundos. Cuánto se separan las dos pistas Comparadas palabra por palabra (en minúsculas, sin puntuación, alineadas con difflib.SequenceMatcher de Python), las dos pistas coinciden en cerca del 95 % del discurso: Escrita por una persona Autogenerada Líneas 183 332 Palabras 2,233 2,211 Signos de puntuación 255 4 Palabras que difieren unas 143 (6 %) El seis por ciento suena poco hasta que se ve qué palabras son. El reconocimiento de voz va bien con las palabras comunes y mal con nombres, números y términos técnicos, justo las partes de las que suele depender una cita: Escrita por una persona Autogenerada President Pitzer President pit launched John Glenn launched John gland a Saturn C-1 booster rocket a satin C1 Cape Canaveral (second mention) canabal we are willing to accept we're willing to accept Además hay un hueco. Hacia el minuto 4:47 la pista automática salta de "both must be" directamente a "determined and cannot be deterred". Las 28 palabras intermedias, "enterprised and overcome with answerable courage. If this capsule history of our progress teaches us anything, it is that man, in his quest for knowledge and progress, is", no están en ella. Nada en la pista automática marca ese salto. Qué pasa con la frase famosa La frase que todo el mundo cita de este discurso está en el 9:18. En la pista humana es una sola línea, con puntuación y un único tiempo de inicio: 558.90 3.65 not because they are easy, but because they are hard, En la pista automática está repartida en tres líneas solapadas, y la primera palabra pertenece a la línea anterior: 555.64 4.80 decade and do the other things not 558.20 6.52 because they are easy but because they 560.44 7.04 are hard because that goal will serve to Los subtítulos automáticos están pensados para mostrarse en rodillo, unas pocas palabras cada vez, así que sus líneas siguen el ritmo del habla y no las frases. De ahí se siguen dos cosas para citar. Copiar la línea de las 9:18 da un fragmento que empieza a mitad de frase, y el tiempo de inicio de la línea que contiene "not" es 9:15, tres segundos antes de la cita. Ninguna de las dos cosas es un error como subtítulo; las dos lo son como referencia. En este caso la gramática se salva, "they are", a diferencia de la versión que mucha gente recuerda ("because it is hard"). Pero unas líneas después "we are willing" se convirtió en "we're willing", y una cita tomada de la pista automática pondría en boca de Kennedy una contracción que no dijo. Elegir la pista y el enlace La herramienta de transcripciones de la aplicación de escritorio de osFoundry , que obtiene los subtítulos desde el ordenador en el que se ejecuta, hace la elección en pocas líneas de Rust. YouTube marca las pistas automáticas con kind: "asr" , y la aplicación toma primero una pista humana en inglés, luego cualquier pista en inglés, luego cualquier pista humana y, si no, la que haya: fn pick_track ( tracks : & [ CaptionTrack ]) -> Option <& CaptionTrack > { tracks .iter () .find (| t | t .language_code .starts_with ( "en" ) && t .kind != "asr" ) .or_else (|| tracks .iter () .find (| t | t .language_code .starts_with ( "en" ))) .or_else (|| tracks .iter () .find (| t | t .kind != "asr" )) .or_else (|| tracks .first ()) } Cuando una línea se guarda como referencia, su tiempo de inicio pasa a ser el parámetro t del enlace. El tiempo se redondea hacia abajo, de modo que el vídeo arranca una fracción de segundo antes de las palabras y no justo después de la primera: url : `https://www.youtube.com/watch?v= ${ transcript . video_id } &t= ${ Math . floor ( segment . start )} s` Para la línea de las 9:18 eso da &t=558s , para una línea que empieza en el segundo 558.9. Cuando solo hay una pista automática Muchos vídeos solo tienen la pista automática. Entonces sirve como índice de búsqueda, no como fuente: úsala para encontrar más o menos dónde se dijo algo, reproduce ese tramo y escribe la cita a partir del audio. Comprueba nombres y cifras con otra fuente y cuenta con tramos que faltan sin ninguna marca. Aun así vale la pena conservar el enlace al segundo, porque permite a un lector hacer la misma comprobación en unos segundos. La aplicación de escritorio usada aquí es gratuita en la página de descarga de osFoundry .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bestaitools-es/son-los-subtitulos-automaticos-de-youtube-lo-bastante-exactos-para-citarlos-89o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
