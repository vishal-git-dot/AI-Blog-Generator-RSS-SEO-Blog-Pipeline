---
title: "Building a Real-Time Weapon Detection System with YOLOv8"
slug: "building-a-real-time-weapon-detection-system-with-yolov8"
author: "Urooj Fatima"
source: "devto_python"
published: "Mon, 06 Jul 2026 10:33:08 +0000"
description: "Over the past few weeks I've been working on a computer vision side project: a real-time weapon detection system that watches a live webcam feed and raises a..."
keywords: "weapon, detection, model, time, not, frame, beep, real"
generated: "2026-07-06T10:49:20.343568"
---

# Building a Real-Time Weapon Detection System with YOLOv8

## Overview

Over the past few weeks I've been working on a computer vision side project: a real-time weapon detection system that watches a live webcam feed and raises an alarm the moment it spots something dangerous. Here's how it works, what I learned, and where it still falls short. The idea Most weapon detection demos I found online either worked on static images only, or used a generic pretrained model that wasn't great at spotting weapons specifically (understandably — COCO, the dataset most YOLO models are pretrained on, only has one weapon-adjacent class: knife). I wanted something that could: Detect a wider range of weapons, not just knives Run on a live webcam feed, not just static images Actually alert someone, not just silently label a frame The approach Custom-trained model. I trained a YOLOv8 model from scratch on a 9-class weapon dataset: Automatic Rifle , Bazooka , Grenade Launcher , Handgun , Knife , Shotgun , SMG , Sniper , Sword Dual-model detection. Interestingly, the pretrained YOLOv8 COCO model turned out to be better at detecting knives specifically than my custom model in some lighting conditions (probably because it was trained on a much larger and more varied dataset). So the final pipeline runs both models per frame: The custom model for the 9 weapon classes The pretrained COCO model, filtered to just class 43 (knife) and merges the detections. Real-time webcam loop. Using OpenCV to capture frames from the webcam, run both models, draw bounding boxes with the class name and confidence score, and display a red "🚨 WEAPON DETECTED!" banner when something's found (or a green "✅ Safe" banner when the frame is clear). The annoying part: the alarm sound This is the bit that actually took the longest to get right. My first version played a beep sound synchronously every time a weapon was detected: if weapon_detected : winsound . Beep ( 1000 , 500 ) This works , but it freezes the entire video feed for the duration of the beep — because winsound.Beep is blocking. With a weapon in frame for several seconds, the feed would stutter constantly as it kept re-triggering the beep on every processed frame. The fix was to run the alarm on a background thread, and add simple state tracking so it only triggers once per "detection event" rather than once per frame: import threading def play_alarm (): winsound . Beep ( 1000 , 500 ) if weapon_detected and not currently_alarming : threading . Thread ( target = play_alarm , daemon = True ). start () currently_alarming = True elif not weapon_detected : currently_alarming = False Small fix, but it was the difference between a genuinely usable live demo and a laggy mess. Results Here's the live detection in action — a knife detected with 50% confidence, bounding box drawn in real time: ![Live weapon detection] And the terminal-side alerting, showing detections across a session with confidence scores and the "weapon cleared" state: ![Terminal alerts] Limitations Confidence scores on some classes (knife especially) are on the lower side — 30-50% in imperfect lighting. It works, but it's not something I'd trust for an actual security deployment without a lot more training data and validation. It's webcam-only right now — no multi-camera support, no persistence/logging of detection events beyond the console. The dataset is relatively small for a 9-class problem; some classes likely need more examples to generalize well. What's next I'd like to: Expand the training dataset, especially for the weaker classes Add proper event logging (timestamped detections saved to a file/database instead of just console output) Experiment with a lighter-weight model for better real-time FPS Code The full code is on GitHub if you want to look through it or try it yourself: 🔗 github.com/uroojbuilds/Computer-Vision/tree/main/weapon-detection Built with Python, Ultralytics YOLOv8 , and OpenCV. If you've worked on anything similar — especially around improving low-confidence detections or handling audio/video threading issues — I'd love to hear how you approached it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/codewithurooj/building-a-real-time-weapon-detection-system-with-yolov8-3323

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
