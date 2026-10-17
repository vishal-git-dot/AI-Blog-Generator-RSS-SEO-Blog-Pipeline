---
title: "A crontab entry for a second weekly film, and the UTC hour it hides"
slug: "a-crontab-entry-for-a-second-weekly-film-and-the-utc-hour-it-hides"
author: "Robert"
source: "devto_webdev"
published: "Sat, 17 Oct 2026 10:00:00 +0000"
description: "On 14.10.2026 we shipped a second weekly film into the crontab of new-Orqestra. The entry is kids-publish-wednesday, with crontab(hour=7, minute=0, day_of_we..."
keywords: "film, utc, crontab, entry, hour, wednesday, what, time"
generated: "2026-10-17T10:24:53.459252"
---

# A crontab entry for a second weekly film, and the UTC hour it hides

## Overview

On 14.10.2026 we shipped a second weekly film into the crontab of new-Orqestra. The entry is kids-publish-wednesday, with crontab(hour=7, minute=0, day_of_week="3") and kwargs {"fmt": "long", "series": "bajka"}. It fires every Wednesday at 07:00 UTC, beside the 14:00 short. Robert asked for the extra film in the middle of the week on 13.10.2026, and this entry is what turns the slot on. The schedule is written in UTC, and the Polish-time hours in our comment follow from that. The comment above the publish entries names both films as 09:00 Polish time on Wednesday and Sunday. It also records what happens on 25.10.2026: the beat scheduler runs in UTC, so when Polish time moves back the slots come an hour earlier, to 15:00 and 08:00, not later. A scheduled film also needs protecting from our own deploys. In deploy.sh, window_now now refuses a deploy on Wednesday between 06:50 and 07:20 UTC, the same way it already did on Sunday, and the comment on the windows says so. On the board in office.py the entry is named "Środowy film Kids". The change touched 17 files, 111 lines added and 63 removed. The slot table's first test used to pin a week of six shorts and one film, and it now reads eight slots. Write every crontab hour in the scheduler's own timezone, say in a comment what local time that means on both sides of a clock change, and give each scheduled run a no-deploy window around it. Originally published at neuragrowth.co . NeuraGrowth is a one-person digital-products studio; this is the log of what its pipeline does and where it breaks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/robswierk/a-crontab-entry-for-a-second-weekly-film-and-the-utc-hour-it-hides-pd3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
