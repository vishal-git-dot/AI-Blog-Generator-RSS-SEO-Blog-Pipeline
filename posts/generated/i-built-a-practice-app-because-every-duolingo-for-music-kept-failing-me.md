---
title: "I Built a Practice App Because Every "Duolingo for Music" Kept Failing Me"
slug: "i-built-a-practice-app-because-every-duolingo-for-music-kept-failing-me"
author: "Diven Rastdus"
source: "devto_webdev"
published: "Sun, 02 Aug 2026 13:34:22 +0000"
description: "I've lost track of how many "Duolingo for piano" apps I've downloaded and deleted. Simply Piano, Yousician, a few others I don't remember the names of. Every..."
keywords: "you, practice, what, piano, string, instrument, nodes, app"
generated: "2026-08-02T13:39:46.250766"
---

# I Built a Practice App Because Every "Duolingo for Music" Kept Failing Me

## Overview

I've lost track of how many "Duolingo for piano" apps I've downloaded and deleted. Simply Piano, Yousician, a few others I don't remember the names of. Every one of them followed the same shape: score how close your playing matched a reference MIDI file, throw a badge at you, ask for a monthly subscription. None of them ever told me why a passage was hard, or when I was actually ready to move past it. They graded me. They didn't teach me. So I built the app I actually wanted and put it up for anyone else with the same problem. It's called Music Practice , it covers piano, electric guitar, and drums, it's free, and the code is open . No account needed to use any of it. The gap I kept hitting Apps that gamify practice, streaks, XP, song-matching scores, are optimizing for a different thing than learning. They want you to open the app again tomorrow. That's a real goal and I get why it's the business model, but it produces a curriculum that's basically a leveled list: do lesson 4, then 5, then 6, with no visible reason 5 needed 4 first, and no way to tell if you're already past it. What I wanted instead was something that always knew exactly what I should practice next, and could tell me why, in one sentence, before I drilled it. A real DAG, not a leveled list The curriculum is a directed acyclic graph. Every skill node carries its own prerequisites as explicit edges: export interface SkillNode { id : string ; // "g-t1-power", "p-key-C-scale" instrument : Instrument | " shared " ; title : string ; tier : 0 | 1 | 2 | 3 | 4 | 5 | 6 ; category : SkillCategory ; prereqs : string []; // node ids, the DAG edges masteryDrill : string ; unlock : string ; // the capability sentence } A node's live status resolves from its prereqs plus your progress: export function resolveStatus ( nodes : SkillNode [], progress : ProgressMap , ): Map < string , SkillNodeStatus > Locked if a prereq isn't learned yet. Available once every prereq is. In-progress once you've logged reps on it. Learned once you've finished it. nextToLearn() filters for available nodes and sorts by tier, that's the entire "what should I practice tonight" decision. No hand-coded switch statement guessing what unlocks when, just prereq edges getting walked. Right now the tree has 32 piano nodes, 36 guitar nodes, and 20 drum nodes. Drums is practice-pad only for now, no full kit. The instrument-agnostic part matters as much as the DAG. Piano, guitar, and drums share one practice engine through an InstrumentModule interface, and each instrument lives in its own lib/<name>/module.tsx that self-registers on import. The only two components that actually know which instrument you're holding are the fretboard/keyboard visual and the tab/staff notation. The skill tree resolver, the review scheduler, the session generator, none of it cares what instrument it's looking at. Adding drums meant a new lib/drums/ folder and one import line, not a rewrite. Applying the research instead of guessing Before building the technique-drill and review systems I wrote up a research pass on motor learning , because I didn't want to just intuit what "good practice" looks like. A few of those findings actually made it into the app as testable code, not vibes. Slow practice builds an accurate motor pattern. Jumping straight to target tempo doesn't. So technique drills ladder tempo up in small steps and only advance after a clean run at the current speed, no slider you can just drag to "hard." A skill "learned" once and never touched again quietly rots, so REVIEW_INTERVALS_DAYS = [1, 3, 7, 14] brings finished nodes back at expanding intervals instead of letting them vanish the moment you pass them. And the ear training is honestly gated. The app never quizzes you on a chord progression it hasn't actually taught yet. Your effective ear level is clamped to whatever the skill tree has covered, so an advanced learner who self-reports at onboarding gets trusted, but nobody gets tested on theory they've never seen. The stack Next.js 16 and React 19, TypeScript throughout. Tone.js handles audio. VexFlow renders notation. svguitar draws chord diagrams. The skill graph itself, the visual tree on the roadmap page, renders with @xyflow/react and gets laid out with dagre. Nothing exotic, just the right library for each surface. Storage: local-first, cloud optional Everything lives in localStorage by default. No account, no login wall, no server round-trip before you can play a note. That felt like the right default for something you open at night, tired, wanting to just start playing. If you want your progress on a second device, there's an opt-in cloud sync that only activates once you sign in. It's additive, never required, and the local copy stays the source of truth. What's next I'm still filling out gaps in the guitar and drum curricula, and there's a batch of pop-song repertoire work queued that needs a real song list before it can ship. But the core loop, tell you what to practice, explain why, ladder the tempo, bring it back later, is live now. Music Practice is free and open source, live at music.raeduslabs.com . If you use it, even for five minutes, I want to know what confused you or what you wished it did next. Repo's open, issues welcome: github.com/astraedus/piano .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/astraedus/i-built-a-practice-app-because-every-duolingo-for-music-kept-failing-me-4gde

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
