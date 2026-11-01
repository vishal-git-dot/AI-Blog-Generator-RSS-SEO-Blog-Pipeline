---
title: "Our homepage serves 24 logo elements for 12 logo files, and four more files nobody has ever requested"
slug: "our-homepage-serves-24-logo-elements-for-12-logo-files-and-four-more-files-nobody-has-ever-requested"
author: "Daniel Pertu"
source: "devto_webdev"
published: "Sun, 01 Nov 2026 12:48:38 +0000"
description: "The CogniPrep landing page has a wall of company logos under the hero with the caption "Some companies that our clients have applied to". Twelve logos, three..."
keywords: "svg, one, grid, bytes, not, four, logos, which"
generated: "2026-11-01T12:58:37.047271"
---

# Our homepage serves 24 logo elements for 12 logo files, and four more files nobody has ever requested

## Overview

The CogniPrep landing page has a wall of company logos under the hero with the caption "Some companies that our clients have applied to". Twelve logos, three rows of four, about as simple as a component gets. Here is what the deployed HTML actually contains: curl -s https://cogniprep.app/ | grep -o '<img[^>]*logos/[a-z-]*\.svg[^>]*>' | wc -l Every logo twice. Why there are two of each The hero is a two-column layout on desktop with the grid in the right column, and a single column on mobile with the grid underneath the buttons. One element cannot be in two places in the DOM, so the page does this: { /* Right Column - Company Grid */ } < div className = "animate-fade-in mt-8 hidden md:block" > < CompanyGrid /> </ div > { /* Mobile company grid */ } < div className = "animate-fade-in md:hidden" > < CompanyGrid /> </ div > hidden md:block and md:hidden , so exactly one is ever visible. This is a completely ordinary thing to write, and the cost is invisible until you count: 24 <img> elements, 24 copies of the props in the streamed RSC payload, and the caption string appearing four times in one response (twice in the HTML, twice in the payload). The browser is fine about the bytes, because both copies point at the same 12 URLs and the second set is a cache hit. What it is not fine about is the hints, which both copies carry: loading = { index < 8 ? ' eager ' : ' lazy ' } fetchPriority = { index < 4 ? ' high ' : ' auto ' } Those indexes were chosen for a 4-column grid, where the first 4 are row one and the first 8 are rows one and two. The mobile grid is grid-cols-2 . On a phone, "the first four" is two rows and "the first eight" is four rows, which on a 70px row height is most of a screen below the fold, marked eager and high priority on a layout that was never measured. The colour we throw away The twelve files are 58,680 bytes of SVG on disk. The wrapper around every one of them is: < div className = "relative h-[70px] w-[140px] brightness-0 invert md:h-[140px] md:w-[280px]" > brightness-0 invert crushes every logo to black and then inverts it, so all twelve render as flat white silhouettes. Every fill, gradient and brand hex in those files is painted over at display time. That is why amazon.svg at 12,357 bytes and hsbc.svg at 1,847 bytes look equally plain on the page: the extra 10 KB is colour information the CSS discards. A monochrome path set would look identical and weigh a fraction, and that is the single best change available here. The optimizer never sees them I expected the usual next/image discussion about the missing sizes prop, because the component uses fill without one. It does not apply, and the HTML says why: <img alt= "HSBC logo" fetchPriority= "high" loading= "eager" decoding= "async" data-nimg= "fill" src= "/logos/hsbc.svg?dpl=dpl_8rF6TpJCpo..." /> The src is the file, not /_next/image?url=... , and there is no srcset at all. SVG sources bypass the optimizer unless you opt in, and we have not: curl -s -o /dev/null -w "%{http_code} \n " \ "https://cogniprep.app/_next/image?url=%2Flogos%2Fhsbc.svg&w=256&q=75" Without dangerouslyAllowSVG in the image config, asking the optimizer for an SVG is a rejected request, so next/image serves the raw file and sizes has nothing to describe. A missing prop that would be a real bug on a raster image is dead config here. The ?dpl= suffix is Vercel's deployment id, which it appends to static asset URLs and which has bitten us elsewhere. The four files on the shelf public/logos holds 16 files. The component names 12. The other four are deployed, reachable and referenced by nothing: rbs.svg 20,729 bytes thales.svg 10,468 bytes network-rail.svg 2,646 bytes tesco.svg 2,601 bytes for f in rbs thales network-rail tesco ; do curl -s -o /dev/null -w " $f %{http_code} %{size_download} \n " \ "https://cogniprep.app/logos/ $f .svg" done Four 200s. 36,444 bytes of the folder is content nothing on the site links to, and the single largest file in the directory is one of them, two and a half times the size of the biggest logo we actually show. Nothing is broken by this. It is the ordinary residue of a grid that was edited a few times: a brand was swapped out of the array and the file stayed, and grep -r "/logos/" returning 12 hits is not a check anybody runs. The sweep worth having is the opposite direction, and it is one line per static directory: list the files, grep the source for each name, print the ones with no hits. The line under the grid One last thing, which is not a performance note. The caption is "Some companies that our clients have applied to", and that wording is deliberate. It is a claim about our own users, which we can support, and not a claim that those companies use us, endorse us or hire through us, which we cannot. The footer on all 375 pages of the site says the rest of it: CogniPrep is an independent practice platform and is not affiliated with or endorsed by any assessment provider, interview platform or employer. All product, company and trademark names are the property of their respective owners and are used for identification only. A logo wall is the easiest place in a product to accidentally claim a relationship that does not exist. If you are building one, write the caption before you pick the logos, because the caption is the part that has to be true. Everything above is checkable against the live page with the three commands in this post, which is the reason to count the HTML rather than read the component: the component says 12.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/daniel_pertu/our-homepage-serves-24-logo-elements-for-12-logo-files-and-four-more-files-nobody-has-ever-3042

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
