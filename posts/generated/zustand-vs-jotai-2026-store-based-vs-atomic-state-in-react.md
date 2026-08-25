---
title: "Zustand vs Jotai (2026): Store-Based vs Atomic State in React"
slug: "zustand-vs-jotai-2026-store-based-vs-atomic-state-in-react"
author: "Carlos Oliva Pascual"
source: "devto_webdev"
published: "Tue, 25 Aug 2026 06:45:46 +0000"
description: "Both Zustand and Jotai are from the same creator and solve the same core problem: state management without Redux boilerplate. Both are ~3kb. Both work great ..."
keywords: "state, const, items, get, zustand, jotai, quantity, set"
generated: "2026-08-25T06:56:03.873317"
---

# Zustand vs Jotai (2026): Store-Based vs Atomic State in React

## Overview

Both Zustand and Jotai are from the same creator and solve the same core problem: state management without Redux boilerplate. Both are ~3kb. Both work great with TypeScript. The difference is the mental model. Zustand thinks in stores — centralized state with actions. Jotai thinks in atoms — small composable pieces that derive from each other. Core Model Zustand: Store + Selectors // store/useCartStore.ts export const useCartStore = create < CartStore > ()( devtools ( persist ( ( set , get ) => ({ items : [] as CartItem [], isOpen : false , addItem : ( item ) => set ( state => { const existing = state . items . find ( i => i . id === item . id ) if ( existing ) { return { items : state . items . map ( i => i . id === item . id ? { ... i , quantity : i . quantity + 1 } : i ) } } return { items : [... state . items , { ... item , quantity : 1 }] } }), clearCart : () => set ({ items : [] }), toggleCart : () => set ( state => ({ isOpen : ! state . isOpen })) }), { name : ' cart ' } )) ) // Components subscribe only to what they need function CartButton () { const count = useCartStore ( state => state . items . reduce (( s , i ) => s + i . quantity , 0 )) const toggle = useCartStore ( state => state . toggleCart ) return < button onClick = { toggle } > Cart ({ count }) < /button > // Only re-renders when count changes } Jotai: Atoms Compose // store/cartAtoms.ts export const cartItemsAtom = atomWithStorage < CartItem [] > ( ' cart-items ' , []) export const cartOpenAtom = atom ( false ) // Derived atoms — auto-memoized, shared across all subscribers export const cartCountAtom = atom ( get => get ( cartItemsAtom ). reduce (( s , i ) => s + i . quantity , 0 ) ) export const cartTotalAtom = atom ( get => get ( cartItemsAtom ). reduce (( s , i ) => s + i . price * i . quantity , 0 ) ) // Write atom for actions export const addItemAtom = atom ( null , ( get , set , item : Omit < CartItem , ' quantity ' > ) => { const items = get ( cartItemsAtom ) const existing = items . find ( i => i . id === item . id ) set ( cartItemsAtom , existing ? items . map ( i => i . id === item . id ? { ... i , quantity : i . quantity + 1 } : i ) : [... items , { ... item , quantity : 1 }] ) }) function CartButton () { const count = useAtomValue ( cartCountAtom ) const setOpen = useSetAtom ( cartOpenAtom ) return < button onClick = {() => setOpen ( p => ! p )} > Cart ({ count }) < /button > } Async State: The Biggest Practical Difference Zustand — manual loading/error management const useUserStore = create < UserStore > ()(( set ) => ({ user : null , loading : false , error : null , fetchUser : async ( id ) => { set ({ loading : true , error : null }) try { set ({ user : await api . users . getById ( id ), loading : false }) } catch ( err ) { set ({ error : ( err as Error ). message , loading : false }) } } })) Jotai — async atoms + Suspense // The fetch IS the atom — no manual loading state export const userQueryAtom = atomWithQuery ( get => ({ queryKey : [ ' user ' , get ( userIdAtom )], queryFn : () => api . users . getById ( get ( userIdAtom ) ! ), enabled : !! get ( userIdAtom ) })) // Component suspends until data resolves function ProfileContent () { const [{ data : user }] = useAtom ( userQueryAtom ) return < Profile user = { user ! } / > } // Suspense boundary handles the loading state function Page () { return ( < Suspense fallback = { < Spinner /> } > < ProfileContent /> < /Suspense > ) } Derived State Zustand selectors recompute on every render (use useShallow for complex objects). Jotai derived atoms are memoized automatically — all subscribers share the same cached computation. // Zustand — manually memoize expensive selectors const result = useCartStore ( useShallow ( state => ({ items : state . items , total : state . items . reduce (( s , i ) => s + i . price * i . quantity , 0 ) }))) // Jotai — memoization is built in, computed once per change const expensiveItemsAtom = atom ( get => get ( cartItemsAtom ). filter ( i => i . price > 100 )) const expensiveTotalAtom = atom ( get => get ( expensiveItemsAtom ). reduce (( s , i ) => s + i . price * i . quantity , 0 ) ) // Multiple components using expensiveTotalAtom share the same result Decision Framework Situation Choose Coming from Redux Zustand State shared across many unrelated components Zustand Complex actions with side effects Zustand Redux DevTools matters Zustand Suspense-based async pattern Jotai Fine-grained, component-local state Jotai atomWithQuery (TanStack integration) Jotai Coming from Recoil Jotai For most React apps, Zustand is the lower-friction starting point. Its mental model (a bag of values with operations) maps to how most developers already think about state. Jotai becomes genuinely better when state is highly reactive, granular, and benefits from automatic memoization across derived views. Full article at stacknotice.com/blog/zustand-vs-jotai-2026

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/stacknotice/zustand-vs-jotai-2026-store-based-vs-atomic-state-in-react-48mo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
