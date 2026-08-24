---
title: "Jak osadzić aplikację Flask w Dockerze - krok po kroku"
slug: "jak-osadzi-aplikacj-flask-w-dockerze-krok-po-kroku"
author: "Andrzej Klusiewicz"
source: "devto_python"
published: "Mon, 24 Aug 2026 07:02:29 +0000"
description: "Krótki, praktyczny przewodnik z bloga JSystems - od gotowego kodu Flask do działającego kontenera, bez zbędnej teorii. W pierwszej kolejności przygotujmy sob..."
keywords: "pliku, docker, app, flask, requirements, txt, obrazu, aplikacji"
generated: "2026-08-24T07:07:50.321979"
---

# Jak osadzić aplikację Flask w Dockerze - krok po kroku

## Overview

Krótki, praktyczny przewodnik z bloga JSystems - od gotowego kodu Flask do działającego kontenera, bez zbędnej teorii. W pierwszej kolejności przygotujmy sobie kod aplikacji Flask: from flask import Flask app = Flask(__name__) @app.route('/') def hello_world(): return 'Hello World!' if __name__ == '__main__': app.run(host='0.0.0.0', debug=True,port=80) Kod ten umieściłem w pliku app.py znajdującym się w głównym katalogu projektu. Jedynym zadaniem aplikacji jest słuchanie na porcie 80 i wyświetlenie "Hello World!" po wejściu na stronę główną aplikacji. Ważne jest by w wywołaniu app.run posłużyć się przełącznikiem host i podać adres, ponieważ bez tego aplikacja nie będzie widoczna spoza kontenera. W kolejnym kroku musimy wygenerować plik requirements.txt który będzie nam potrzebny do instalacji zależności w kontenerze. Generujemy go wywołując z poziomu głównego katalogu aplikacji komendę: pip freeze > requirements.txt W dalszym kroku musimy utworzyć plik Dockerfile w głównym katalogu projektu. Do pliku tego trzeba będzie wprowadzić kilka informacji na temat sposobu budowania obrazu. Wchodzimy na https://hub.[docker](https://jsystems.pl/blog/show_post/kubernetes-vs-docker-roznice).com/ i wyszukujemy obraz posiadający obsługę Pythona: Wybieramy przykładowo taki obraz klikając na jego nazwę: Pod spodem powinna znajdować się taka lista: Wybieramy pierwszy wpis i wprowadzamy poniższą linię z wybranym obrazem go do pustego dotychczas pliku Dockerfile : FROM python:3.14-slim-trixie Linia ta informuje Dockera o obrazie który ma zostać wykorzystany do budowy naszego obrazu. Nie musisz przejmować się pobieraniem żadnego pliku związanego z tym obrazem. Docker pobierze go sam. Musimy wskazać jeszcze czynności jakie mają zostać wykonane w celu uruchomienia aplikacji. Wprowadzamy do Dockerfile poniższe linie: COPY requirements.txt . RUN pip install -r requirements.txt COPY app.py . CMD ["python","app.py"] Zostaną one wykonane w chwili budowania obrazu. Instrukcja COPY powoduje skopiowanie wskazanego pliku (w tym przypadku pliku z listą wymaganych zależności) do obrazu. Kolejna instrukcja RUN powoduje instalację wymaganych zależności przez pip z pliku requirements.txt który stworzyliśmy przy pomocy instrukcji "pip freeze > requirements.txt" wykonanej wcześniej. Kolejne wykonanie komendy COPY to skopiowanie pliku w którym znajduje się nasz program. Ostatnia instrukcja CMD uruchamia pythona nakazując mu wykonanie pliku "app.py". Musimy teraz utworzyć nasz obraz na podstawie pliku Dockerfile. Robimy to wywołując w linii poleceń: docker build -t myrest . "myrest" w powyższej komendzie to nazwa pod jaką później widoczny będzie nasz obraz. Kropka na końcu informuje go o położeniu pliku Dockerfile. Po uruchomieniu powinny pojawiać się linie informujące o zakończeniu tworzenia kolejnych etapów budowy obrazu. Przyszedł czas na uruchomienie kontenera: docker run -p 80:80 myrest Po uruchomieniu możemy wejść przez przeglądarkę na naszą aplikację: Komendę tą możesz wykonać z dowolnego miejsca, ponieważ docker uruchamia obraz po nazwie - w tym przypadku "myrest". Jest to nazwa obrazu którą mu nadaliśmy podczas jego budowania. Pewnego wyjaśnienia może wymagać "-p 80:80". Pierwsza wartośćliczbowa to port na którym apka ma być widoczna na zewnątrz, a druga to port na jakim chodzi apka wewnątrz kontenera. Listę zbudowanych obrazów możesz zobaczyć wywołując komendę: docker image ls Listę uruchomionych kontenerów możesz zobaczyć wywołując komendę : docker container ls Chcąc zatrzymać uruchomiony kontener potrzebujemy jego container_id z powyższej listy, a przynajmniej jego unikalnego początku: docker stop c38

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/andrzej_klusiewicz_08588c/jak-osadzic-aplikacje-flask-w-dockerze-krok-po-kroku-4gb8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
