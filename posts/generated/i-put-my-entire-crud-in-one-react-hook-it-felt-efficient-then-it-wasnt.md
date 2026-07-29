---
title: "I put my entire CRUD in one React hook. It felt efficient. Then it wasn’t."
slug: "i-put-my-entire-crud-in-one-react-hook-it-felt-efficient-then-it-wasnt"
author: "Kiara"
source: "devto_webdev"
published: "Wed, 29 Jul 2026 02:40:49 +0000"
description: "They say every bad decision comes from a good intention. I'd say it comes from good intentions… and a little lack of thinking things through. This is the sto..."
keywords: "const, items, hook, one, list, query, filters, update"
generated: "2026-07-29T03:14:29.810977"
---

# I put my entire CRUD in one React hook. It felt efficient. Then it wasn’t.

## Overview

They say every bad decision comes from a good intention. I'd say it comes from good intentions… and a little lack of thinking things through. This is the story of the day I put my entire CRUD inside one React hook — and how that backfired. The good intention I needed a simple admin panel: list, create, read, update, delete. Classic CRUD. What I wanted to avoid: lots of files and boilerplate a hard time managing state splitting every action into its own file (felt like overengineering for "just a screen") So I built useItems : one hook for the whole feature. Where I didn't think it through I was already using React Query — so I wasn't really fighting state the hard way. React Query is that layer. And yes, the screen was simple — but it lived inside a complex app that was going to grow. I optimized for the afternoon, not for the next six months. Still, I went ahead. Into the hook went: a list query (with filters) a find-one-by-id query all mutations: create, update, delete It looked roughly like this: export function useItems ( id ?: number , filters ?: Partial < ItemsQuery > , ) { const api = useFetch (); const listQuery = useQuery ({ queryKey : [ " items " , filters ], queryFn : () => api . get ( " /items " , { params : filters }), }); const detailQuery = useQuery ({ queryKey : [ " item " , id ], queryFn : () => api . get ( `/items/ ${ id } ` ), enabled : !! id , }); const createMutation = useMutation ({ mutationFn : ( body : CreateItemBody ) => api . post ( " /items " , body ), }); const updateMutation = useMutation ({ mutationFn : ({ id , body }: { id : number ; body : Partial < UpdateItemBody > }) => api . patch ( `/items/ ${ id } ` , body ), }); const deleteMutation = useMutation ({ mutationFn : ( id : number ) => api . delete ( `/items/ ${ id } ` ), }); return { items : listQuery . data ?. items , total : listQuery . data ?. total , item : detailQuery . data , create : createMutation . mutateAsync , update : updateMutation . mutateAsync , remove : deleteMutation . mutateAsync , isLoadingList : listQuery . isLoading , isLoadingItem : detailQuery . isLoading , isCreating : createMutation . isPending , isUpdating : updateMutation . isPending , isDeleting : deleteMutation . isPending , }; } Clean. Convenient. Slightly cursed. Why it was a bad decision Different lifecycles, one hook. You can see it in the parameters alone: id and filters . A list, a detail, and a write path are three jobs. I forced them through one door. Cache keys and invalidation fog. Ironically, I got the pain I tried to avoid: things felt hard to control again. The list refetched when I was only editing one item — or didn't refetch after a delete. I'd invalidate wider "to be safe," make everything heavier, then invalidate differently. React Query wasn't broken. My boundary was. Fake reuse. "Reusable" became "configurable." Need only the modal update? Still mount the feature — just flip enabled flags and hope. That's not reuse. That's a monolith with dimmer switches. The symptoms I didn't notice because of architecture theory. I noticed because the UI started arguing with me. Invalidations with a personality — list reloading at the wrong time, or not when it should Unnecessary weight — detail pages and update modals dragging list-query energy they never needed Rerenders. Oh my god, the rerenders The sentence that finally clicked: > This isn't reuse. It's a module disguised as a hook. What I should've done Split by intention: list hook, detail hook, small mutation hooks next to the UI that writes. Shared query keys stay small. Screens import only what they need. // before — every screen dragged the whole feature const { items , item , update , remove , isLoadingList , isLoadingItem } = useItems ( id , filters ); // after — imports = intention const { items , isLoading } = useItemsList ( filters ); // table const { item } = useItem ( id ); // detail const { mutateAsync : updateItem } = useUpdateItem (); // modal / form Less clever. Much calmer. Results clearer imports (the screen says what it cares about) fewer surprise refetches lighter modals and pages And a reusable lesson: good intentions need an expiry date. But, to be fair : a monolith hook isn’t always a crime. For a quick prototype or a tiny CRUD that will stay tiny, one useItems can be the honest move — less ceremony, faster shipping. The mistake wasn’t the pattern itself. It was treating a prototype-shaped abstraction like it could scale inside a growing app without revisiting the boundary. If you've also built a useSomething that returned twelve things and a prayer… hi. We're the same.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kiaravzm/i-put-my-entire-crud-in-one-react-hook-it-felt-efficient-then-it-wasnt-10mf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
