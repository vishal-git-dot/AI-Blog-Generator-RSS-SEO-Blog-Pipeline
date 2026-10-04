---
title: "On the N100, OpenVINO was not faster. And I almost measured it wrong"
slug: "on-the-n100-openvino-was-not-faster-and-i-almost-measured-it-wrong"
author: "Israel Negrete Lepe"
source: "devto_python"
published: "Sun, 04 Oct 2026 20:41:44 +0000"
description: "If you work with models on Intel hardware, you know the usual advice: for CPU inference, use OpenVINO. It is Intel's runtime, built for Intel's hardware, and..."
keywords: "not, openvino, model, you, what, one, runtime, precision"
generated: "2026-10-04T21:07:13.178660"
---

# On the N100, OpenVINO was not faster. And I almost measured it wrong

## Overview

If you work with models on Intel hardware, you know the usual advice: for CPU inference, use OpenVINO. It is Intel's runtime, built for Intel's hardware, and on a mini PC with an N100 it would seem the obvious pick over ONNX Runtime. I measured it. On the N100, across the three models I compared, OpenVINO was between 11% and 22% slower than ONNX Runtime. But the result is not the interesting part. The interesting part is that before I got there, I almost measured something else, and the wrong measurement would have passed every check. What happened in the rehearsal Before touching the N100, I rehearsed the protocol on my Mac, which has an ARM CPU. MobileNetV2 in FP32, OpenVINO with its default settings. It came out fast, and it came out right: the outputs matched the reference. The same top class on all twelve test images, and a cosine similarity of 0.999 or more against the expected result. Then I looked at something almost nobody looks at: the precision OpenVINO had decided to run the model in. An FP32 model, and OpenVINO running it in FP16. Without being asked, and without saying so. INFERENCE_PRECISION_HINT = float16 It is a design decision in OpenVINO, not a bug: on that processor, FP16 runs faster. But it is not the one I asked for, and it shows up nowhere unless you go looking for it. In FP16, the model's p50 was 1.46 ms. Forcing f32, the same model on the same machine took 2.39 ms. Had I kept the first number, I would have measured a precision change and credited it to the runtime. Why validation does not catch it This is what I think matters most here. The usual check — does it give the same answers? — passed. And it had to: for image classification, FP16 is enough. The output does not move far enough for an accuracy test to notice. So same results, and faster does not prove the comparison is fair. It proves the precision change was small enough not to show on that model. On another one — deeper, a regression model, one that is already quantized — it may well show. And it may show in production. How I measured it on the N100 After the rehearsal, the protocol changed. In every FP32 case, precision is pinned to f32 when the model is compiled, and after compiling, the effective precision is read back. If it is not f32, the measurement does not count: it is marked invalid, even if everything else passed. compiled = core . compile_model ( model , " CPU " , { " INFERENCE_PRECISION_HINT " : " f32 " }) compiled . get_property ( " INFERENCE_PRECISION_HINT " ) # checked, not assumed With that, on an 8 GB Intel N100 running Ubuntu 24.04, freshly rebooted, one hundred measurements after twenty warm-up runs, batch 1 and default threading: Model ONNX Runtime 1.30.0 OpenVINO 2026.4.0 OpenVINO vs ORT MobileNetV2 FP32 5.7 ms 7.0 ms 22% slower ResNet18 FP32 22.8 ms 26.9 ms 18% slower YOLO26n FP32 57.6 ms 64.0 ms 11% slower These are the p50 of model inference. OpenVINO's effective precision was f32 in all three cases, and in all three the outputs matched the reference. In detection, YOLO26n found the same objects as the reference, not one more, not one fewer. I had not predicted this. Before measuring, I wrote down what I expected from each case, and for this one I left the answer as unknown. The measurement settled it in a direction I did not expect. What this result does not say This is a measurement, not a verdict on OpenVINO. It holds for what was measured, and nothing more: One device. One N100. On a processor with native FP16, or with the matrix instructions of Xeon chips, the story may be different. CPU only. The N100 has an integrated GPU, and OpenVINO knows how to use it. I did not measure it. Batch 1, latency. OpenVINO has a mode built for processing many inputs at once, with several parallel streams. I did not measure that either. Three models, in f32. With reduced precision, or with OpenVINO's own quantization, the numbers change. What it does say is more modest and, I think, more useful: on this device and with this setup, the advantage you would expect did not show up. What I would do differently when comparing runtimes If you are choosing a runtime for an edge device, four things I would have done from the start: Pin the precision, and read back what you got. Not what you asked for: what the runtime chose after compiling. It is two lines of code, and it is the difference between comparing runtimes and comparing precisions. Do not use accuracy as proof that the comparison is fair. Matching outputs say the change did not show on that model. They do not say there was no change. Write down what you expect, first. Even if the answer is I don't know . If you do not write it down, any result seems to confirm what you already thought. Measure on the device, not on your machine. Freshly rebooted, warmed up, and with p50 and p95, not an average. The Mac helped me find the problem; only the N100 gave the answer. The full table — five models on a Raspberry Pi 5 and on the N100, with ONNX Runtime and OpenVINO — is on crtdrops.mx, next to an ONNX model check that runs in your browser without uploading the file anywhere. If you open one of the models I measured, the tool recognizes it and shows you its numbers. Measuring your own model this way, on both devices and with the same protocol, is the next thing I will offer. Try it: the full results table and the in-browser ONNX model check on crtdrops.mx. Israel Negrete Lepe is an electronics engineer. Twenty-five years building systems that make it to production: telemetry, vehicle tracking, municipal video surveillance, RFID asset control and transactional platforms.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/crtdrops/on-the-n100-openvino-was-not-faster-and-i-almost-measured-it-wrong-5bl5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
