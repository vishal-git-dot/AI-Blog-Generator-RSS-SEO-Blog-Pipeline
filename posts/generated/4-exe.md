---
title: "Как я собрал 4 проекта в один .exe — и почему это плохая идея"
slug: "4-exe"
author: "Vadik"
source: "devto_python"
published: "Sun, 13 Sep 2026 14:50:27 +0000"
description: "Как я собрал 4 проекта в один .exe — и почему это плохая идея Привет, Хабр! У меня есть четыре пет-проекта на Python: NeoBrain (локальный AI-чат) , NeoSpace ..."
keywords: "exe, manifest, json, path, neobrain, sys, python, projects"
generated: "2026-09-13T15:57:28.536925"
---

# Как я собрал 4 проекта в один .exe — и почему это плохая идея

## Overview

Как я собрал 4 проекта в один .exe — и почему это плохая идея Привет, Хабр! У меня есть четыре пет-проекта на Python: NeoBrain (локальный AI-чат) , NeoSpace OS (виртуальная среда) , NeoReceipt (генератор чеков) и Why Does This Exist? (интерактивная панель) . Каждый — отдельный .py файл со своим GUI. Запускать их было неудобно: открываешь терминал, пишешь python neobrain.py , потом закрываешь, потом python neoreceipt.py … В общем, боль. Я решил сделать лаунчер — одно окно с карточками проектов, кнопка «Запустить» — и всё работает. И вот тут начались грабли, о которых я хочу рассказать. Первая версия: наивная сборка Сделал я лаунчер на Tkinter (просто, быстро, встроено в Python). Выглядит вот так: Дальше — сборка в .exe через PyInstaller . Хотелось один файл, чтобы пользователь скачал и запустил, без установки Python и зависимостей. Написал .spec : a = Analysis ( [ ' launcher.py ' ], datas = [( ' manifest.json ' , ' . ' ), ( ' projects ' , ' projects ' )], ... ) Что это значит: manifest.json и папка projects/ вшиваются внутрь .exe . Всё в одном файле. Красиво же? Собрал. Размер — около 20 МБ . Запустил. Работает. Карточки есть, кнопки нажимаются, проекты открываются. Я был доволен. Проблема Через пару дней я обновил NeoBrain — добавил пару фич, поправил баги. Запускаю лаунчер, жму «Запустить NeoBrain» — открывается старая версия . Почему? Потому что .exe вшил в себя старую версию neobrain.py ещё при сборке. Чтобы обновление сработало, надо: Пересобрать .exe (30-60 секунд). Получить новый файл на 20 МБ . Залить его в релиз. Пользователь скачивает 20 МБ ради одного изменённого .py (в котором 50 КБ ). И так — каждый раз , при любом обновлении любого проекта. Я подумал: «Это же абсурд. Пользователи будут качать гигабайты ради килобайтов изменений». Решение: не вшивать данные Я убрал datas=[...] из .spec . Оставил datas=[] . Теперь .exe — только лаунчер . Проекты и manifest.json — рядом с ним, в папке: NeoLauncher/ ├── NeoLauncher.exe ← 10 МБ, только лаунчер ├── manifest.json ← список проектов └── projects/ ├── neobrain.py ├── neospace.py ├── neoreceipt.py └── whydoes.py Плюсы: Обновил neobrain.py → просто заменил файл. Exe не трогаешь . Пользователь качает только изменённый .py (килобайты), а не 10 МБ. Можно добавлять новые проекты — просто положил .py в projects/ . Казалось бы — идеально. Но была одна проблема . Вторая проблема: exe не находит manifest.json Собрал новый .exe . Запускаю. «❌ Нет проектов» . Почему? Потому что в коде у меня было: self . base_dir = os . path . dirname ( os . path . abspath ( __file__ )) self . manifest_path = os . path . join ( self . base_dir , " manifest.json " ) __file__ — это сам launcher.py . Когда запускаешь как скрипт — всё ок, manifest.json рядом. Но когда запускаешь как .exe , __file__ указывает на временную папку PyInstaller ( %TEMP%\_MEIxxxxx\ ), а не на папку с exe. Итог: лаунчер ищет manifest.json не там, где нужно . Решение: sys.frozen PyInstaller устанавливает флаг sys.frozen = True , когда приложение запущено как собранный exe . Это можно использовать: if getattr ( sys , ' frozen ' , False ): # Запущено как .exe — папка рядом с exe self . base_dir = os . path . dirname ( sys . executable ) else : # Запущено как .py — папка скрипта self . base_dir = os . path . dirname ( os . path . abspath ( __file__ )) Что даёт: В режиме .py — папка скрипта (как раньше). В режиме .exe — папка с exe (там, где manifest.json ). Пересобрал. Запускаю. «✦ 4 ПРОЕКТОВ ГОТОВЫ К ЗАПУСКУ» . Карточки на месте. Кнопки работают. Что получилось в итоге NeoLauncher v2.0.0: .exe — 10 МБ (только лаунчер). Проекты — рядом , обновляются независимо . Релиз на GitHub Releases : пользователь качает .zip → распаковывает → запускает. Обновление проекта — замена .py файла, exe не трогается . Мораль Если вы собираете .exe через PyInstaller и вшиваете в него данные через datas=[...] — подумайте дважды : Как часто эти данные меняются ? Как часто вы готовы пересобирать exe? Готовы ли пользователи качать 10-20 МБ ради килобайтов изменений? Если данные меняются часто — не вшивайте . Пусть exe будет тонким , а данные — рядом . Используйте sys.frozen для корректных путей : if getattr ( sys , ' frozen ' , False ): base_dir = os . path . dirname ( sys . executable ) else : base_dir = os . path . dirname ( os . path . abspath ( __file__ )) Это сэкономит вам часы пересборок и гигабайты пользовательского трафика. Ссылки GitHub: github.com/Sbeuvadyarik67/NeoLauncher- Releases: NeoLauncher v2.0.0 README: в репозитории Вопрос к читателям А вы вшиваете данные в .exe или разделяете ? Сталкивались с похожей проблемой? Расскажите в комментариях — интересно сравнить подходы. Спасибо за внимание!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sbeuvadyarik67/kak-ia-sobral-4-proiekta-v-odin-exe-i-pochiemu-eto-plokhaia-idieia-1fi0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
