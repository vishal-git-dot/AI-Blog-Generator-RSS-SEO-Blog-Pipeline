---
title: "One Prop Per State: Rethinking React's Controlled/Uncontrolled Boilerplate"
slug: "one-prop-per-state-rethinking-reacts-controlleduncontrolled-boilerplate"
author: "wmzy"
source: "devto_webdev"
published: "Tue, 01 Sep 2026 04:23:11 +0000"
description: "If you've ever wrapped a <Select> , <DatePicker> , or <Dialog> , you've written this: function Select ({ value , defaultValue , onChange }) { const [ interna..."
keywords: "state, control, value, react, one, const, controlled, use"
generated: "2026-09-01T04:32:01.152943"
---

# One Prop Per State: Rethinking React's Controlled/Uncontrolled Boilerplate

## Overview

If you've ever wrapped a <Select> , <DatePicker> , or <Dialog> , you've written this: function Select ({ value , defaultValue , onChange }) { const [ internal , setInternal ] = useState ( defaultValue ); const isControlled = value !== undefined ; // runtime mode check const current = isControlled ? value : internal ; // two sources of truth useEffect (() => { if ( isControlled ) setInternal ( value ); // hand-written sync }, [ value , isControlled ]); // ... } One state: three props, two sources, one sync effect, branches everywhere. A component with three controllable states ( value , open , selectedIndex ) needs 9 props, 3 branches, 3 effects . I solved this with react-use-control — an 80-line, zero-dependency hook that works differently from the usual approaches. Ask a different question: where does the state come from? The controlled/uncontrolled duality exists because we ask "does the parent control this state?" and branch. The real question is simpler: If a parent already created the state → use it. If nobody did → create it locally. No second source means no synchronization, and no mode detection. That's what a control object does: function Counter ({ count }) { const [ num , setNum ] = useControl ( count , 0 ); // count is a control, or a plain value return < button onClick = { () => setNum (( n ) => n + 1 ) } > { num } </ button >; } Pass a plain value → uncontrolled; that value is the default. Pass a control → controlled; parent and child share one source of truth. Both modes run the same code path — zero branching inside the component. This is not signals It looks like Solid/Jotai — a token passed around. The mechanism is the opposite: Signals (Solid/Jotai) react-use-control Where state lives Outside the tree — a module-level store Inside the tree — a plain useState How updates flow Subscription + fine-grained re-render React's normal setState flow Lifecycle Global; leaks are your problem Dies with the owning component Module-scope state creation Yes — the whole point No A control is not a container of state. It's a locator : "the useState someone in my ancestry created — or the one I create right now." React stays the store and the scheduler, so SSR, StrictMode, and concurrent rendering work for free. No subscriptions, no cleanup, no leak footguns. The one cost: state can't exist without a mounted component. Freebies: sibling sharing and middleware The same control passed to multiple children shares one state — no Context, no lifting: const [, setCount , countCtl ] = useControl ( 0 ); < Counter count = { countCtl } /> < Counter count = { countCtl } /> { /* both share state with the parent */ } Middle layers transform state without owning it. useThru removes the wrapper's own state entirely — the child stays the owner and the trigger, the wrapper contributes only the transform: const clamped = useThru ( count , mapSetter (( v ) => Math . max ( 0 , v ))); // clamp writes const shown = useThru ( clamped , mapState (( v ) => `$ ${ v } ` )); // map reads const logged = useThru ( shown , watch ( console . log )); // observe writes The value / onChange equivalent of this chain is a parent-owned state and a hand-wrapped callback at every level. Benchmarks (jsdom, identical DOM output) Scenario manual triple Radix useControllableState react-use-control mount (uncontrolled) baseline 1.31× 1.38× controlled prop update baseline 2.26× 2.67× setter update (click) baseline 1.09× tied (0.99×) The controlled-update path is where the architectures diverge: manual and Radix both keep a second source to sync; a control reads the single source directly. The setter path is dominated by React's own dispatch and is a tie — reported honestly, not cherry-picked. Reproduce with pnpm bench . When not to use it Fields managed by a form library (react-hook-form, formik, …) — the form owns that state, the field is permanently controlled, so read and write through the form's API. Control solves the ownership problem; where the problem doesn't exist, it adds nothing. TL;DR One prop per state: Control<T> | T — a value is the default, a control is sharing Single source of truth: no sync effect, no isControlled branch, no uncontrolled→controlled warning 80 lines, 0 deps, built on useState / useMemo / useRef only Powers haze-ui , a component library where every stateful component takes one prop per state Repo: react-use-control · npm i react-use-control Deep dive: Who Owns the State?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wmzy/one-prop-per-state-rethinking-reacts-controlleduncontrolled-boilerplate-2gob

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
