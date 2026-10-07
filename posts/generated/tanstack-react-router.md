---
title: "TanStack React Router"
slug: "tanstack-react-router"
author: "Yuri Peixinho"
source: "devto_webdev"
published: "Wed, 07 Oct 2026 22:25:08 +0000"
description: "Introdução É um roteador para React focado em type-safety de ponta a ponta : rotas, parâmetros de URL, query strings e dados carregados por loaders são todos..."
keywords: "const, router, posts, postid, routes, tsx, react, rota"
generated: "2026-10-07T22:56:27.548315"
---

# TanStack React Router

## Overview

Introdução É um roteador para React focado em type-safety de ponta a ponta : rotas, parâmetros de URL, query strings e dados carregados por loaders são todos inferidos pelo TypeScript, sem precisar escrever tipos manualmente. Ele também trata data loading como parte do roteamento (parecido com Remix/Next App Router), não como algo à parte (diferente do React Router clássico). Duas formas de declarar rotas Code-based (tudo em um arquivo, manual) import { createRootRoute , createRoute , createRouter } from ' @tanstack/react-router ' const rootRoute = createRootRoute ({ component : RootLayout }) const indexRoute = createRoute ({ getParentRoute : () => rootRoute , path : ' / ' , component : HomePage , }) const postRoute = createRoute ({ getParentRoute : () => rootRoute , path : ' /posts/$postId ' , component : PostPage , }) const routeTree = rootRoute . addChildren ([ indexRoute , postRoute ]) const router = createRouter ({ routeTree }) File-based (recomendado) a estrutura de pastas/arquivos em src/routes define a árvore, e um plugin (Vite/Webpack/etc.) gera o routeTree.gen.ts automaticamente. Cada arquivo usa createFileRoute('/caminho')({...}) e nunca precisa declarar getParentRoute — o plugin resolve isso pela posição no filesystem. Convenções de nome de arquivo: Arquivo Vira rota routes/__root.tsx layout raiz (obrigatório) routes/index.tsx / routes/about.tsx /about routes/posts/index.tsx /posts/ routes/posts/$postId.tsx /posts/:postId (param dinâmico) routes/posts/$postId.edit.tsx /posts/:postId/edit routes/_authenticated.tsx + pasta routes/_authenticated/ layout sem adicionar segmento na URL (pathless layout) routes/posts/-components/Card.tsx ignorado — prefixo - é só código auxiliar, não vira rota routes/posts.lazy.tsx parte da rota com code-splitting automático O router e o RouterProvider O Register é o truque que faz o TypeScript "conhecer" todas as rotas do app em qualquer componente, sem precisar importar nada específico. import { createRouter , RouterProvider } from ' @tanstack/react-router ' import { routeTree } from ' ./routeTree.gen ' const router = createRouter ({ routeTree }) declare module ' @tanstack/react-router ' { interface Register { router : typeof router // isso dá type-safety global pra Link, useNavigate, etc. } } createRoot ( document . getElementById ( ' root ' ) ! ). render ( < RouterProvider router = { router } /> ) Outlet e layouts aninhados Toda rota com filhas renderiza um <Outlet /> onde a rota filha deve aparecer: export const Route = createRootRoute ({ component : () => ( <> < NavBar /> < Outlet /> </> ), }) Isso permite layouts aninhados: _authenticated.tsx pode renderizar uma sidebar + <Outlet /> , e todas as rotas dentro de _authenticated/ herdam esse layout. Navegação import { Link , useNavigate } from ' @tanstack/react-router ' < Link to = " /posts/$postId " params = {{ postId : ' 123 ' }} > Ver post < /Link > const navigate = useNavigate () navigate ({ to : ' /posts/$postId ' , params : { postId : ' 123 ' } }) Se a rota não existir ou o param faltar, é erro de tipo em tempo de compilação — não em runtime. Params dinâmicos // routes/posts/$postId.tsx export const Route = createFileRoute ( ' /posts/$postId ' )({ component : PostPage , }) function PostPage () { const { postId } = Route . useParams () // tipado como string } Search params (query string) validados Diferente do React Router, aqui a query string é tipada e validada (geralmente com Zod): import { z } from ' zod ' const searchSchema = z . object ({ page : z . number (). catch ( 1 ), filter : z . string (). optional (), }) export const Route = createFileRoute ( ' /posts/ ' )({ validateSearch : searchSchema , component : PostsList , }) function PostsList () { const { page , filter } = Route . useSearch () // já validado e tipado } E <Link search={{ page: 2 }}> também é tipado contra esse schema. 8. Loaders (carregar dados antes de renderizar) export const Route = createFileRoute ( ' /posts/$postId ' )({ loader : async ({ params }) => fetchPost ( params . postId ), component : PostPage , }) function PostPage () { const post = Route . useLoaderData () // tipo inferido do retorno do loader } Loaders rodam antes do componente montar (e podem rodar em paralelo com o parent). Combinado com defaultPreload: 'intent' no createRouter , os dados já começam a carregar no hover/foco de um <Link> , antes mesmo do clique. Estados de pending / erro / not-found export const Route = createFileRoute ( ' /posts/$postId ' )({ loader : ..., pendingComponent : () => < Spinner />, // enquanto o loader roda errorComponent : ({ error , reset }) => ..., // se o loader ou render lançar erro notFoundComponent : () => < p > Não encontrado </ p >, }) Esses fallbacks seguem a hierarquia de rotas: se uma rota não define o seu, o pai assume (até chegar no __root.tsx ). Contexto de rota beforeLoad pode popular um contexto tipado compartilhado por toda a árvore (útil pra auth, QueryClient, etc.): export const Route = createRootRouteWithContext < { queryClient : QueryClient } > ()({...}) // em uma rota filha: loader : ({ context }) => context . queryClient . ensureQueryData ( postsQuery ) Devtools @tanstack/react-router-devtools dá um painel visual da árvore de rotas, matches ativos e estado dos loaders — ótimo pra depurar durante o desenvolvimento.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yuripeixinho/tanstack-react-router-ieg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
