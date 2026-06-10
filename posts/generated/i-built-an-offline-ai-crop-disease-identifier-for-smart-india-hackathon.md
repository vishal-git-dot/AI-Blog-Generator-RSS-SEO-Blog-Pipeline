---
title: "I Built an Offline AI Crop Disease Identifier for Smart India Hackathon"
slug: "i-built-an-offline-ai-crop-disease-identifier-for-smart-india-hackathon"
author: "Devanshu Biswas"
source: "devto_python"
published: "Wed, 10 Jun 2026 20:02:51 +0000"
description: "🌐 Live demo: https://dev48v.infy.uk/solve/day3-crop-disease.html Day 3 of SolveFromZero — pick a real hackathon brief, ship a working solution. Today's probl..."
keywords: "model, disease, app, dataset, const, hindi, crop, phone"
generated: "2026-06-10T20:38:15.847429"
---

# I Built an Offline AI Crop Disease Identifier for Smart India Hackathon

## Overview

🌐 Live demo: https://dev48v.infy.uk/solve/day3-crop-disease.html Day 3 of SolveFromZero — pick a real hackathon brief, ship a working solution. Today's problem is a perennial Smart India Hackathon: 35% of Indian crop losses come from undiagnosed disease , and the village ag-extension officer can't visit every farm. The fix: a phone app where the farmer photographs a sick leaf, AI returns the disease + a remedy in Hindi or Marathi. Runs fully offline on a ₹6,000 Android phone. The hard constraints Hardware ₹6,000 Android phone, 2 GB RAM Network Patchy 2G in rural areas Model size Must fit in < 20 MB to bundle with the app Inference < 2 seconds per leaf photo UX Hindi / Marathi / Tamil voice output (many farmers can't read) These constraints rule out cloud APIs (no GPT-4V), large vision models (no 100M+ param ResNets), and English-only UI. The pipeline 📷 Phone camera ↓ 🖼 Pre-process (resize 224×224, normalize 0-1) ↓ 🧠 MobileNetV2 (transfer-learned on PlantVillage) → softmax over 38 classes ↓ 🏆 Top class + confidence ↓ 📋 Lookup table: disease → Hindi remedy ↓ 🔊 speechSynthesis.speak(remedy_in_hindi) 5 stages. Each one ~20-30 lines of code. Total: ~200 lines for the whole app. Stage 1 — PlantVillage dataset (free) PlantVillage is the canonical academic dataset: 54,305 labeled leaf photos across 38 disease classes across 14 crops (tomato, potato, grape, corn, apple, ...). Public, free, no attribution required. Download from Kaggle: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset This dataset alone covers most South Asian crops. Stage 2 — Transfer learning from MobileNetV2 Don't train a CNN from scratch — you'd need 100k+ images + days of GPU. Take MobileNetV2 (pre-trained on ImageNet, knows generic visual features), freeze the first 100 layers, replace the final classification head with one for 38 classes, fine-tune the last few layers on PlantVillage. from tensorflow.keras.applications import MobileNetV2 base = MobileNetV2 ( weights = " imagenet " , include_top = False ) for layer in base . layers [: - 30 ]: layer . trainable = False model = Sequential ([ base , GlobalAveragePooling2D (), Dense ( 38 , activation = " softmax " ) ]) model . compile ( optimizer = " adam " , loss = " sparse_categorical_crossentropy " , metrics = [ " accuracy " ]) model . fit ( train_ds , validation_data = val_ds , epochs = 10 ) ~30 minutes on a free Colab T4 GPU. Hits ~95% validation accuracy. Stage 3 — Quantize to fit on phone MobileNetV2 fp32 = 14 MB. Quantize weights to int8 → 3.5 MB. Same accuracy ±1%. converter = tf . lite . TFLiteConverter . from_keras_model ( model ) converter . optimizations = [ tf . lite . Optimize . DEFAULT ] converter . representative_dataset = rep_data_gen tflite_model = converter . convert () # 14 MB → 3.5 MB, < 1% accuracy loss Now it fits in 1.5 MB gzipped over a 2G connection. Stage 4 — Run in-browser with TensorFlow.js (no native code) You can ship as a Progressive Web App — no Play Store hassle, works on any Android with a browser. Convert the Keras model to TF.js layers format and load it from JS: const model = await tf . loadLayersModel ( " /model/model.json " ); fileInput . onchange = async ( e ) => { const img = new Image (); img . src = URL . createObjectURL ( e . target . files [ 0 ]); await img . decode (); const tensor = tf . browser . fromPixels ( img ) . resizeBilinear ([ 224 , 224 ]) . toFloat (). div ( 255 ). expandDims (); const probs = await model . predict ( tensor ). data (); const top = probs . indexOf ( Math . max (... probs )); console . log ( CLASSES [ top ], probs [ top ]); }; Stage 5 — Remedy lookup + Hindi voice const REMEDIES = { " tomato_late_blight " : { treatment : " Spray 2g/L Mancozeb every 7 days for 3 weeks. " , hindi : " मैनकोज़ेब 2 ग्राम/लीटर पानी में मिलाकर 7 दिन में छिड़काव करें। " }, // ... 38 entries }; const r = REMEDIES [ CLASSES [ top ]]; const utter = new SpeechSynthesisUtterance ( r . hindi ); utter . lang = " hi-IN " ; speechSynthesis . speak ( utter ); Many farmers can't read. Voice output is the difference between "interesting demo" and "actually deployable tool." Offline-first PWA (the critical detail) Rural villages have spotty 2G. App must work without network after first install: // service-worker.js self . addEventListener ( " install " , e => { e . waitUntil ( caches . open ( " crop-v1 " ). then ( cache => cache . addAll ([ " / " , " /index.html " , " /app.js " , " /model/model.json " , " /model/weights.bin " // 3.5 MB ]) ) ); }); After the first visit, the app + model are cached. Works in airplane mode. This is what makes the app actually deployable . Try it now 3-tier page with simulated 4-leaf classifier + 9-step understanding: https://dev48v.infy.uk/solve/day3-crop-disease.html What this unlocks Same pipeline (small CNN + lookup table + voice) works for: Problem Model swap Cattle disease ID PlantDoc-style cattle dataset Weed identification DeepWeeds dataset Soil-color → nutrient deficiency Custom dataset + simple classifier Insect pest identification IP102 dataset The CNN + offline PWA + multilingual voice = the template for any rural-village AI deployment. What's next in SolveFromZero Day 4: GitHub repo health scorer (Devpost). Paste a GitHub URL → get a health score based on stars, recent commits, issue/PR ratios. 🌐 All problems: https://dev48v.infy.uk/solvefromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-an-offline-ai-crop-disease-identifier-for-smart-india-hackathon-2a8l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
