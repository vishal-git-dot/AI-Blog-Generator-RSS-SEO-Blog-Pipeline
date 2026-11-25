---
title: "3 YouTube Data API traps I hit building playlists in bulk"
slug: "3-youtube-data-api-traps-i-hit-building-playlists-in-bulk"
author: "Sam Wootton"
source: "devto_webdev"
published: "Wed, 25 Nov 2026 21:13:26 +0000"
description: "Most of us already have the videos for the playlist we want. They are just scattered: the workout videos in a playlist called "Saved for later", the recipes ..."
keywords: "playlist, video, videos, you, youtube, one, insert, playlists"
generated: "2026-11-25T21:26:57.089596"
---

# 3 YouTube Data API traps I hit building playlists in bulk

## Overview

Most of us already have the videos for the playlist we want. They are just scattered: the workout videos in a playlist called "Saved for later", the recipes somewhere in Liked videos. On YouTube, building a new playlist from them means saving each video, one menu at a time. I built TidyList, a web app for cleaning up big YouTube playlists, on the YouTube Data API v3, and building new playlists from old ones is half of what it does. Creating the playlist is one call. Filling it properly took three lessons. The manual way Find a video you want in one of your playlists. Open its menu, choose Save and tick the new playlist. Repeat for every video, keeping track yourself of which ones you have already added. Trap 1: insert order is not the order you loop in playlistItems.insert takes an optional snippet.position . Leave it out and each video is appended at the end, which is also where YouTube's own Save puts it. Set position: 0 and each one goes in at the top. I insert at the top, so new videos are the first thing a user sees in the playlist. The catch: insert 1, 2, 3 at position 0 and the playlist reads 3, 2, 1. Each insert pushes the last one down. The fix is to walk the list backwards: // Inserting at position 0 reverses the order, so walk last to first for ( const videoId of [ . . . videoIds ] . reverse ( ) ) { await insertVideo ( playlistId , videoId , 0 ) ; } Whichever you choose, choose it once. If one path appends and another inserts at the top, the same action lands in two different orders depending on how many videos it touched. Trap 2: filtering by category needs a second call, and the names aren't unique Picking videos by category ("all the Music", "all the Education") sounds like a filter on the playlist. It isn't, because playlist items carry no category. You have to ask videos.list for each video's snippet.categoryId , up to 50 ids per call, and skip the call when you have no ids left: an empty id= is answered with a 400. Then you need the category names, from videoCategories.list , and two surprises wait there: The list depends on regionCode . It lists the categories a region offers uploaders, while a video's categoryId is global, so a user's own region can be missing an id their videos use. When I checked, 110 of 111 regions returned the same 31 ids and the US returned 32, lacking nothing the others had, so I always ask for the US and pass the user's language in hl for the names. Titles are not unique. Ids 23 and 34 are both called "Comedy". Count by id, or merge ids that share a title, but never look a category up by its name, or one of them counts twice. Trap 3: YouTube will happily add a video twice, but refuses some outright Two kinds of video need filtering before you insert anything: Duplicates. YouTube lets the same video sit in a playlist more than once. If your source playlists overlap, or the user picks the same video from two of them, you will add it twice unless you de-duplicate by videoId yourself. Private and deleted videos. Their entries are still in the source playlist, titled "Private video" or "Deleted video" with no thumbnail, and playlistItems.insert refuses them with 400 Precondition check failed . Leave them out of the plan, and tell the user how many were left out rather than failing part-way. And budget for quota: each insert costs 50 units, so a 200-video playlist uses the whole 10,000-unit default daily quota of a new project. Or skip the code If you just want to build playlists from your own, that's what TidyList's playlist builder does. Open any playlist or Liked videos, pick videos by YouTube category or title, name the new playlist and check the draft. Picking and drafting are free. Saving it to YouTube is one step with TidyList Pro (£4.99, one-off), and every video lands once, in order. Questions about the API side are welcome in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/samwootton/3-youtube-data-api-traps-i-hit-building-playlists-in-bulk-o2c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
