---
title: "3 YouTube Data API traps I hit deleting liked videos in bulk"
slug: "3-youtube-data-api-traps-i-hit-deleting-liked-videos-in-bulk"
author: "Sam Wootton"
source: "devto_webdev"
published: "Wed, 25 Nov 2026 21:10:10 +0000"
description: "Years of likes add up. My own Liked videos list holds thousands, a couple of hundred of them now private or deleted, hidden behind "Unavailable videos are hi..."
keywords: "videos, you, youtube, list, liked, likes, your, like"
generated: "2026-11-25T21:26:57.090032"
---

# 3 YouTube Data API traps I hit deleting liked videos in bulk

## Overview

Years of likes add up. My own Liked videos list holds thousands, a couple of hundred of them now private or deleted, hidden behind "Unavailable videos are hidden" . YouTube lets you unlike them one at a time, and that's it. I built TidyList, a web app for cleaning up big YouTube playlists, on the YouTube Data API v3. Liked videos looked like the easy case, since it is just a playlist. It nearly is. These three things weren't. The manual way Open Liked videos on YouTube. Find a video you want gone, open its menu and choose Remove from Liked videos . Repeat, one at a time, across thousands of likes. Private and deleted ones need Show unavailable videos first. Trap 1: the playlist id is a literal, don't build it playlists.list?mine=true only returns playlists you created, so Liked videos is not in it. You get its id from your channel: GET https://www.googleapis.com/youtube/v3/channels?part = contentDetails & mine = true contentDetails.relatedPlaylists holds two ids. uploads is UU followed by your channel id, so it is tempting to assume likes is LL plus the channel id too. It isn't: it is the literal string "LL" . Build it yourself and you get a playlist that doesn't exist. So read it from the response, every time, and never derive it. Once you have it, playlists.list?id=LL returns an ordinary, fully populated playlist, and playlistItems.list reads it like any other. (If you were hoping for Watch Later or watch history here: relatedPlaylists only returns likes and uploads . Both still work on YouTube, but apps can't reach them through the API.) Trap 2: it is a window of 5,000, not all your likes The list holds your most recent 5,000 likes , YouTube's limit for a playlist. Older likes are not in it, and no app can reach them through it. Two smaller surprises around that number: The counts disagree. On my list contentDetails.itemCount said 5000 while playlistItems.list 's pageInfo.totalResults said 4,975. Show your users the number of entries you actually loaded. videos.list?myRating=like looks like a way round the window. It is documented to stop at 1,000, and in my testing it does. If your UI shows a count, say it is the most recent 5,000 once the list is full. Users with more likes than that will otherwise think something is missing. Trap 3: removing an entry unlikes the video Deleting from Liked videos is the ordinary call, by the playlist item's id : await fetch ( `https://www.googleapis.com/youtube/v3/playlistItems?id=${item.id}` , { method : 'DELETE' , headers : { Authorization : `Bearer ${accessToken}` } } ) ; It works, and it does more than tidy a list. On YouTube the like and the entry are the same thing, so removing the entry unlikes the video , which also changes that user's recommendations. Say so in your confirm dialog. It doesn't work in reverse: you can't add a video to Liked videos with playlistItems.insert . A like is created by videos.rate , so treat the list as a source you can copy from and remove from, never a destination. Budget for quota too: each delete costs 50 units, so unliking 200 videos uses the whole 10,000-unit default daily quota of a new project. Or skip the code If you just want your own likes cleared in bulk, TidyList does it . Pick Liked videos, then choose what goes: the private and deleted ones, a whole YouTube category, or anything you find by title. The counts are free. Deleting them is one step with TidyList Pro (£4.99, one-off), and nothing changes on YouTube until you confirm. Questions about the API side are welcome in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/samwootton/3-youtube-data-api-traps-i-hit-deleting-liked-videos-in-bulk-1a9n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
