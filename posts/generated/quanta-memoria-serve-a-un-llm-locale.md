---
title: "Quanta memoria serve a un LLM locale?"
slug: "quanta-memoria-serve-a-un-llm-locale"
author: "Hanako H."
source: "devto_ai"
published: "Fri, 06 Nov 2026 13:51:35 +0000"
description: "Prima di scaricare un modello da eseguire in locale, la domanda è se ci sta in memoria. La stima è la somma di tre termini, confrontata con quello che la mac..."
keywords: "per, modello, circa, memoria, sta, una, con, che"
generated: "2026-11-06T14:06:52.633136"
---

# Quanta memoria serve a un LLM locale?

## Overview

Prima di scaricare un modello da eseguire in locale, la domanda è se ci sta in memoria. La stima è la somma di tre termini, confrontata con quello che la macchina può davvero dare al modello: need = weights + KV cache + overhead fits if need <= 0.8 × usable memory I numeri qui sotto seguono la stima usata dal browser dei modelli locali nell'app desktop osFoundry , verificata su quello che l'app mostra per un MacBook M3 da 16 GB. I pesi I pesi sono il numero di parametri per i byte di ogni peso, e questi byte dipendono dalla quantizzazione : Quant Byte per peso FP16 / BF16 2.0 Q8_0 1.0 Q6_K 0.82 Q5_K_M 0.69 Q4_K_M 0.56 Q3_K_M 0.44 Q2_K 0.31 Q4_K_M vale 0.56 e non 0.5 perché i K-quant memorizzano una scala per ogni piccolo blocco di pesi, il che porta a circa 4.5 bit per peso. Per un modello da 14B in Q4_K_M: 14 × 10⁹ × 0.56 = 7.84 × 10⁹ byte, circa 7.3 GiB. Se non riconosci il nome della quantizzazione, assumi FP16. È la scelta pessimistica, così non deciderai mai che qualcosa ci sta quando in realtà non ci sta. La cache KV Durante la generazione il modello conserva chiavi e valori per ogni token del contesto. La dimensione è: 2 × layers × kv_heads × head_dim × context_tokens × bytes_per_element Qwen2.5 14B ha 48 layer, 8 KV head (usa il grouped-query attention) e una dimensione di head di 128. Con una cache in FP16: Contesto da 4K: 2 × 48 × 8 × 128 × 4096 × 2 byte = 768 MiB Contesto da 32K: 6 GiB La cache cresce linearmente con la lunghezza del contesto, quindi un modello che sta comodo a 4K può smettere di starci a 32K. Una stima che non dichiara la lunghezza del contesto serve a poco; quella dello screenshot assume 4K. L'overhead llama.cpp ha bisogno anche di buffer di calcolo e di spazio di lavoro. Un margine approssimativo è il 10% dei pesi più circa 200 MB. Per il modello da 14B sono circa 0.9 GB. Sommando pesi, cache e overhead, un modello da 14B in Q4_K_M sta tra 8 e 9 GB. L'app mostra 8.4 GB. Memoria utilizzabile È la parte in cui si sbaglia più spesso. GPU dedicata: il tetto è la VRAM della scheda. Con una scheda da 12 GB sono 12 GB, qualunque sia la RAM di sistema. Apple Silicon: la memoria è unificata, ma la GPU non può usarla tutta e il sistema operativo ne vuole una parte. Contare il 75% della RAM totale è un valore di lavoro ragionevole, quindi con 16 GB si arriva a circa 12 GB. Poi si confronta: need ≤ 80% della memoria utilizzabile: ci sta, con margine per il sistema operativo e le altre app dall'80% al 100%: al limite; si carica, ma chiudi prima le altre app oltre il 100%: va in paging su disco e diventa inutilizzabile per la lentezza Sul Mac da 16 GB viene fuori: Q4_K_M 8.4 GB (70%, ci sta), Q5_K_M 10.4 GB (87%, al limite), Q6_K 12.3 GB e Q8_0 14.9 GB (oltre). Applicata a più modelli in Q4_K_M, su questa macchina il limite cade tra 20B (11.9 GB, al limite) e 27B (15.9 GB, troppo grande). La velocità dipende dallo stesso numero Per generare ogni token bisogna leggere tutti i pesi dalla memoria una volta, quindi il limite superiore della velocità di generazione è la banda di memoria divisa per la dimensione del modello. Un M3 base ha circa 100 GB/s, perciò un modello da 8.4 GB arriva al massimo a circa 12 token al secondo e un 8B da 4.9 GB a circa 20. I valori reali sono più bassi, ma il rapporto tra i modelli regge bene. La stima della dimensione risponde quindi a due domande insieme: se il modello si carica e, se sì, più o meno quanto velocemente scriverà.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bestaitools-it/quanta-memoria-serve-a-un-llm-locale-5cli

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
