---
title: "MP4 to SRT: Generate Subtitles and Check Their Timing"
slug: "mp4-to-srt-generate-subtitles-and-check-their-timing"
author: "visiohex"
source: "devto_python"
published: "Fri, 20 Nov 2026 15:02:43 +0000"
description: "A transcript can have every word right and still make for frustrating subtitles. A caption might disappear before you finish reading it, trail the speaker af..."
keywords: "srt, you, audio, cues, check, first, start, interview"
generated: "2026-11-20T15:10:11.459959"
---

# MP4 to SRT: Generate Subtitles and Check Their Timing

## Overview

A transcript can have every word right and still make for frustrating subtitles. A caption might disappear before you finish reading it, trail the speaker after an edit, or cover two lines of dialogue that should have been split. When turning an MP4 into an SRT, check the words and the timing separately. Here is a workflow for an interview or screen recording. You will inspect the audio tracks, generate a first-pass SRT, and check the result against the exact MP4 you plan to publish. Start with the final MP4 Transcribe the final cut when you can. Trimming four seconds from the beginning of a video shifts every existing caption by four seconds. Cutting something from the middle makes a global offset insufficient because the captions before the cut are still correct. If the MP4 has multiple audio tracks, find the one carrying the dialogue first: ffprobe -v error -select_streams a \ -show_entries stream = index,codec_name,channels:stream_tags=language,title \ -of json interview.mp4 Stream titles and languages are useful hints. If there are several plausible tracks, listen to a few seconds before you commit. The first audio stream could be commentary or a different language. Generate a first-pass SRT If your speech-to-text tool takes audio files, extract the first audio track into a mono WAV: ffmpeg -hide_banner -i interview.mp4 -map 0:a:0 \ -ac 1 -ar 16000 -c:a pcm_s16le interview.wav 0:a:0 selects the first audio stream in the first input. Use 0:a:1 for the second audio stream. If you need the channels kept separate, such as when each interviewee was recorded on a different channel, omit -ac 1 and check what your transcriber supports. Next, run speech-to-text with timestamps enabled and export SRT. VoceText is the online tool behind this example. It can take the MP4 directly, prepare the audio in your browser and upload the audio for transcription. The WAV extraction step is useful when you want to choose the track yourself or use an audio-only transcriber. FFmpeg extracts the track here. Speech recognition provides the words and their timing. A short SRT file looks like this: 1 00:00:00,500 --> 00:00:02,400 Can you hear the second microphone? 2 00:00:02,700 --> 00:00:04,200 Yes. Let's start the interview. The timestamps use hours, minutes, seconds and milliseconds. Each cue has a start time, an end time and the text to display. A blank line separates cues. Check for overlaps and cues outside the video The following script reads the timing that FFmpeg recognizes in the SRT. It flags overlaps, cues with a non-positive duration and captions that extend beyond the MP4. For this single-speaker-at-a-time workflow, treat overlaps as candidates for review. import json import subprocess import sys from decimal import Decimal def probe ( * args ) : return json . loads ( subprocess . check_output ( [ "ffprobe" , "-v" , "error" , * args , "-of" , "json" ] , text = True , ) ) video , srt = sys . argv [ 1 : ] duration = Decimal ( probe ( "-show_entries" , "format=duration" , video ) [ "format" ] [ "duration" ] ) cues = probe ( "-select_streams" , "s:0" , "-show_packets" , "-show_entries" , "packet=pts_time,duration_time" , srt ) . get ( "packets" , [ ] ) if not cues : raise SystemExit ( "No subtitle cues found" ) latest_end = Decimal ( "0" ) issues = 0 for number , cue in enumerate ( cues , start = 1 ) : start = Decimal ( cue [ "pts_time" ] ) length = Decimal ( cue [ "duration_time" ] ) end = start + length if start < latest_end or length <= 0 or end > duration : print ( f "Check cue {number}: {start}s to {end}s" ) issues += 1 latest_end = max ( latest_end , end ) print ( f "{len(cues)} cues checked, {issues} flagged" ) sys . exit ( 1 if issues else 0 ) Save it as check_srt.py and run python3 check_srt.py interview.mp4 interview.srt . Use the same MP4 you intend to ship. This is a timing check on the cues FFmpeg parsed. It cannot tell you whether the words match the recording or whether every subtitle block survived a malformed export. Fix caption drift before you publish Open the MP4 with the SRT loaded and watch the first spoken line, a line after a cut and a line near the end. If all three are late by about the same amount, apply a single offset in your subtitle editor and run the check again. If the difference changes after a cut, retime the affected segment using the final video as the reference. If it grows steadily, check that the SRT came from the same version and playback speed as the MP4. Take one final pass for readability. Split long captions where a speaker pauses or a phrase ends. Give viewers time to read names, numbers and unfamiliar terms. For web playback, keep the same timing review when you export WebVTT for an HTML video track. For an editing workflow that takes SRT, keep the tested SRT next to the final MP4.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hex_builder/mp4-to-srt-generate-subtitles-and-check-their-timing-1hdm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
