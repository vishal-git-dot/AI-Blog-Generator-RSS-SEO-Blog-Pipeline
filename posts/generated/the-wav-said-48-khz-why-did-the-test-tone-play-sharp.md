---
title: "The WAV said 48 kHz. Why did the test tone play sharp?"
slug: "the-wav-said-48-khz-why-did-the-test-tone-play-sharp"
author: "SparkLLM"
source: "devto_python"
published: "Wed, 25 Nov 2026 07:44:36 +0000"
description: "The delivery brief asked for 48 kHz. The WAV header agreed. Then the editor played the reference tone. What should have been 1,000 Hz sounded sharp. Kevinche..."
keywords: "khz, header, rate, tone, brief, asked, samples, wav"
generated: "2026-11-25T07:53:48.782783"
---

# The WAV said 48 kHz. Why did the test tone play sharp?

## Overview

The delivery brief asked for 48 kHz. The WAV header agreed. Then the editor played the reference tone. What should have been 1,000 Hz sounded sharp. Kevinchen1104 built that discrepancy into a synthetic test recording. The samples were recorded for 44.1 kHz playback, but the header was changed to 48 kHz. Playing the same samples faster moved the measured peak to 1,088.42 Hz in both channels. ffprobe and the decoder both reported the header rate correctly. Spark-X2.6-4B ran locally on four CPU threads and read the written brief. Asked for the rate in Hz, it returned 48 . Asked which passage specified the delivery rate, it picked the line containing “48 kHz”. Python converted the selected expression to 48,000 Hz. The spectrum measurement came from the decoded samples. In the author’s 22 synthetic Chinese and English cases, the final checker matched 21 expected verdicts. The miss was a brief that mentioned last month’s rate while this week’s was still pending. For ordinary audio without a known reference tone, the report can confirm a header match but leaves the pitch question open. Listen to the two tones in the downloadable offline report . Kevinchen1104’s original walkthrough and reproduction instructions .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sparkllm/the-wav-said-48-khz-why-did-the-test-tone-play-sharp-10ja

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
