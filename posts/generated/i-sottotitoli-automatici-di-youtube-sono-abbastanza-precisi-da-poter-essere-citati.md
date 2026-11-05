---
title: "I sottotitoli automatici di YouTube sono abbastanza precisi da poter essere citati?"
slug: "i-sottotitoli-automatici-di-youtube-sono-abbastanza-precisi-da-poter-essere-citati"
author: "Hanako H."
source: "devto_python"
published: "Thu, 05 Nov 2026 23:03:42 +0000"
description: "La maggior parte dei video di YouTube ha una trascrizione, e per quasi tutti è stata scritta da un sistema di riconoscimento vocale. Per seguire il video va ..."
keywords: "una, per, che, tracks, riga, traccia, con, parole"
generated: "2026-11-05T23:29:11.048768"
---

# I sottotitoli automatici di YouTube sono abbastanza precisi da poter essere citati?

## Overview

La maggior parte dei video di YouTube ha una trascrizione, e per quasi tutti è stata scritta da un sistema di riconoscimento vocale. Per seguire il video va bene. Per una citazione in una tesi, in un articolo di giornale o in una nota legale, la domanda è quanto il testo automatico si discosti da ciò che è stato detto e se i suoi timestamp puntino al secondo giusto. Un video che ha entrambi i tipi di sottotitoli dà una risposta diretta. Il video è il caricamento della NASA del discorso del presidente Kennedy alla Rice University nel 1962 ( WZyRbnpGyzQ , 18 minuti). Ha due tracce in inglese: una scritta da una persona e una generata da YouTube. Entrambe si possono elencare e scaricare con il pacchetto Python youtube-transcript-api : from youtube_transcript_api import YouTubeTranscriptApi tracks = YouTubeTranscriptApi (). list ( " WZyRbnpGyzQ " ) for t in tracks : print ( t . language_code , t . is_generated , t . language ) # en False English - Caption # en True English (auto-generated) manual = tracks . find_manually_created_transcript ([ " en " ]). fetch (). to_raw_data () auto = tracks . find_generated_transcript ([ " en " ]). fetch (). to_raw_data () Ogni elemento è una riga di testo con un tempo di inizio e una durata in secondi. Quanto distano le due tracce Confrontate parola per parola (in minuscolo, senza punteggiatura, allineate con difflib.SequenceMatcher di Python), le due tracce coincidono per circa il 95% del discorso: Scritta da una persona Generata automaticamente Righe 183 332 Parole 2,233 2,211 Segni di punteggiatura 255 4 Parole diverse circa 143 (6%) Il sei per cento sembra poco finché non si guarda di quali parole si tratta. Il riconoscimento vocale se la cava bene con le parole comuni e male con nomi, numeri e termini tecnici, cioè proprio i punti su cui una citazione di solito si regge: Scritta da una persona Generata automaticamente President Pitzer President pit launched John Glenn launched John gland a Saturn C-1 booster rocket a satin C1 Cape Canaveral (second mention) canabal we are willing to accept we're willing to accept C'è anche un buco. Intorno a 4:47 la traccia automatica salta da "both must be" direttamente a "determined and cannot be deterred". Le 28 parole in mezzo, "enterprised and overcome with answerable courage. If this capsule history of our progress teaches us anything, it is that man, in his quest for knowledge and progress, is", non ci sono per niente. Nella traccia automatica nulla segnala la lacuna. Che cosa succede alla frase famosa La frase che tutti citano di questo discorso si trova a 9:18. Nella traccia umana è una sola riga, punteggiata, con un solo tempo di inizio: 558.90 3.65 not because they are easy, but because they are hard, Nella traccia automatica è distribuita su tre righe sovrapposte, e la prima parola appartiene alla riga precedente: 555.64 4.80 decade and do the other things not 558.20 6.52 because they are easy but because they 560.44 7.04 are hard because that goal will serve to I sottotitoli automatici sono pensati per la visualizzazione a scorrimento, poche parole alla volta, quindi le loro righe seguono i tempi del parlato e non le frasi. Per chi cita ne derivano due cose. Copiare la riga di 9:18 dà un frammento che comincia a metà frase, e il tempo di inizio della riga che contiene "not" è 9:15, tre secondi prima della citazione. Nessuno dei due è sbagliato come sottotitolo; entrambi sono sbagliati come riferimento. In questo caso la grammatica regge, "they are", a differenza della versione che la maggior parte delle persone ricorda ("because it is hard"). Ma "we are willing" è diventato "we're willing" qualche riga dopo, e una citazione presa dalla traccia automatica metterebbe in bocca a Kennedy una contrazione che non ha detto. Scegliere la traccia, e il link Lo strumento di trascrizione dell'app desktop di osFoundry , che recupera i sottotitoli dal computer su cui gira, fa la scelta in poche righe di Rust. YouTube contrassegna le tracce automatiche con kind: "asr" , e l'app prende prima una traccia inglese umana, poi una qualsiasi in inglese, poi una qualsiasi umana e infine quella che c'è: fn pick_track ( tracks : & [ CaptionTrack ]) -> Option <& CaptionTrack > { tracks .iter () .find (| t | t .language_code .starts_with ( "en" ) && t .kind != "asr" ) .or_else (|| tracks .iter () .find (| t | t .language_code .starts_with ( "en" ))) .or_else (|| tracks .iter () .find (| t | t .kind != "asr" )) .or_else (|| tracks .first ()) } Quando una riga viene salvata come riferimento, il suo tempo di inizio diventa il parametro t del link. Il tempo viene arrotondato per difetto, così il video parte una frazione di secondo prima delle parole e non subito dopo la prima: url : `https://www.youtube.com/watch?v= ${ transcript . video_id } &t= ${ Math . floor ( segment . start )} s` Per la riga di 9:18 è &t=558s , per una riga che inizia a 558.9 secondi. Quando c'è solo una traccia automatica Molti video hanno soltanto la traccia automatica. Allora è un indice di ricerca, non una fonte: serve a trovare più o meno dove è stata detta una cosa, si riproduce quel tratto e si scrive la citazione ascoltando l'audio. Nomi e numeri vanno verificati con un'altra fonte, e bisogna aspettarsi tratti mancanti senza alcun segnale. Vale comunque la pena tenere il link al secondo, perché permette a un lettore di fare lo stesso controllo in pochi secondi. L'app desktop usata qui è gratuita nella pagina di download di osFoundry .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bestaitools-it/i-sottotitoli-automatici-di-youtube-sono-abbastanza-precisi-da-poter-essere-citati-35dc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
