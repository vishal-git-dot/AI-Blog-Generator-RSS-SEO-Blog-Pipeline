---
title: "Python: checar preço de produto passando por proxy residencial (e calcular o custo por página)"
slug: "python-checar-preo-de-produto-passando-por-proxy-residencial-e-calcular-o-custo-por-pgina"
author: "Nuvem Dev"
source: "devto_python"
published: "Sun, 01 Nov 2026 12:10:53 +0000"
description: "Quando o scraping começa a tomar bloqueio, o culpado costuma ser o IP do seu servidor. Aqui vai um script curto que passa a requisição por um proxy (se você ..."
keywords: "proxy, com, por, custo, https, http, url, python"
generated: "2026-11-01T12:58:37.045094"
---

# Python: checar preço de produto passando por proxy residencial (e calcular o custo por página)

## Overview

Quando o scraping começa a tomar bloqueio, o culpado costuma ser o IP do seu servidor. Aqui vai um script curto que passa a requisição por um proxy (se você tiver um) e já estima quanto aquela página custou em tráfego. Eu rodei esse script de verdade contra um servidor local, sem proxy, só pra validar o código. Não testei com um proxy pago nesta edição. 1. Instala pip install requests 2. O script import os , sys , requests # PROXY_URL no formato http://usuario:senha@host:porta (vem do painel do provedor) proxy = os . getenv ( " PROXY_URL " ) proxies = { " http " : proxy , " https " : proxy } if proxy else None def pega ( url ): r = requests . get ( url , proxies = proxies , timeout = 15 , headers = { " User-Agent " : " Mozilla/5.0 (compatible; checa-preco/0.1) " }) r . raise_for_status () return r if __name__ == " __main__ " : url = sys . argv [ 1 ] r = pega ( url ) kb = len ( r . content ) / 1024 print ( f " status= { r . status_code } tamanho= { kb : . 1 f } KB via_proxy= { bool ( proxy ) } " ) print ( f " custo estimado a US$ 5,51/GB: US$ { kb / 1024 / 1024 * 5.51 : . 6 f } " ) 3. Rodando Sem proxy (testei assim, com uma página local): python checa_preco.py http://localhost:8765/index.html # status=200 tamanho=0.0 KB via_proxy=False Com proxy, é só exportar a variável antes: export PROXY_URL = "http://usuario:senha@host:porta" python checa_preco.py https://exemplo.com.br/produto Por que o custo por página importa Proxy residencial é cobrado por giga de tráfego. Na página oficial do IPRoyal (01/11/2026) o preço vai de US$ 7,35/GB no pacote de 1 GB a US$ 5,51/GB no de 10 GB, e o tráfego não expira. Uma página de 200 KB custa na casa de US$ 0,001. O que pesa mesmo é imagem e JavaScript: se der pra pedir só o HTML, o custo cai bastante. Boas práticas Leia os termos do site e o robots.txt antes de coletar. Se existir API oficial, use a API. Coloque um sleep entre requisições. Rotacionar IP não justifica martelar o servidor dos outros. Preços e planos do IPRoyal: https://go.nowto.link/iproyal Se curtiu, a versão newsletter com os números dos pacotes está na Substack: https://nuvemdev.substack.com . E o tutorial anterior (isolamento de perfil com Playwright) está no meu perfil: https://dev.to/nuvemdev Divulgação: alguns links são de afiliado. Se você comprar, eu posso ganhar uma comissão, sem custo extra pra você.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nuvemdev/python-checar-preco-de-produto-passando-por-proxy-residencial-e-calcular-o-custo-por-pagina-3d9d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
