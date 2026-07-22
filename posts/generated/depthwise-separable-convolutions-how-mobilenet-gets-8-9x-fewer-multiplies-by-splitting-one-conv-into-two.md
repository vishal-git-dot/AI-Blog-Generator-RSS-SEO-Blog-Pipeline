---
title: "Depthwise-separable convolutions: how MobileNet gets ~8-9x fewer multiplies by splitting one conv into two"
slug: "depthwise-separable-convolutions-how-mobilenet-gets-8-9x-fewer-multiplies-by-splitting-one-conv-into-two"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Wed, 22 Jul 2026 08:30:36 +0000"
description: "A standard convolution quietly does two very different jobs at once. It filters space — a Dk×Dk window looks at local pattern — and it mixes channels — it su..."
keywords: "cin, cout, self, cost, channel, depthwise, channels, one"
generated: "2026-07-22T08:36:37.031299"
---

# Depthwise-separable convolutions: how MobileNet gets ~8-9x fewer multiplies by splitting one conv into two

## Overview

A standard convolution quietly does two very different jobs at once. It filters space — a Dk×Dk window looks at local pattern — and it mixes channels — it sums across all Cin inputs to build each of Cout outputs. Because those are fused into one fat Dk×Dk×Cin×Cout tensor, the cost is Dk²·Cin·Cout·Df² multiply-adds, quadratic in both channel count and kernel size. On a phone, stacks of these are the bottleneck. MobileNet asks: do we really need to filter space and mix channels in the same operation? I built a live cost calculator to answer it, and the whole reduction falls out of one clean ratio. The baseline we're trying to beat function stdCost ( Dk , Cin , Cout , Df ) { return Dk * Dk * Cin * Cout * Df * Df ; // one fat tensor does everything } // 3x3, Cin=Cout=512 → 9·512·512 = 2,359,296 weights per layer Step 1 — depthwise: one spatial filter per channel Give each input channel its own Dk×Dk kernel and convolve it in isolation. Channel c in produces channel c out; nothing crosses between channels. The output keeps the same Cin channels, and the cost collapses to Dk²·Cin·Df² — the Cout factor is gone. This is pure spatial pattern extraction; it just can't combine features. function depthwise ( maps , kernels , Dk ) { return maps . map (( m , c ) => conv2d ( m , kernels [ c ])); // c -> c only, no mixing } function dwCost ( Dk , Cin , Df ) { return Dk * Dk * Cin * Df * Df ; } Step 2 — pointwise: a 1x1 conv mixes channels Depthwise never combined channels, so a 1×1 conv does exactly that. At every pixel it takes a weighted sum across all Cin channels to produce each of Cout outputs — a per-pixel matrix multiply, Cin→Cout , with zero spatial extent. This is where new feature combinations are formed and where the channel count changes. function pointwise ( chVals , W ) { // chVals: length Cin at one pixel return W . map ( row => // W: [Cout][Cin] row . reduce (( a , w , c ) => a + w * chVals [ c ], 0 )); } function pwCost ( Cin , Cout , Df ) { return Cin * Cout * Df * Df ; } Chain them — depthwise for where , pointwise for what — and you have a drop-in replacement for one standard conv with identical input and output shapes. In MobileNet each is followed by BatchNorm + ReLU, so the block is DW → BN → ReLU → PW → BN → ReLU . Where the 8-9x comes from Divide separable cost by standard cost and almost everything cancels: (Dk²·Cin·Df² + Cin·Cout·Df²) / (Dk²·Cin·Cout·Df²) = 1/Cout + 1/Dk² Two clean consequences. First, the ratio is independent of the feature-map size Df — it cancels, so the saving is the same at every resolution. Second, for a 3×3 kernel the 1/Dk² = 1/9 term dominates once Cout is reasonably large, so you get roughly 8–9x fewer multiply-adds. function reduction ( Dk , Cout ) { return 1 / Cout + 1 / ( Dk * Dk ); } // 3x3, Cout=256 → 1/256 + 1/9 = 0.115 → ~8.7x cheaper // 5x5, Cout=256 → 1/256 + 1/25 = 0.044 → ~23x cheaper // 1x1 → 1/Cout + 1 > 1 → NO benefit (no spatial work to factor out) The flip side is worth internalizing: a 1×1 kernel gives 1/Cout + 1 , i.e. more cost. The trick only pays off when Dk > 1 , because there has to be a spatial cost to factor out. The accuracy trade-off, and PyTorch Depthwise-separable is an approximation : it can only represent filters that factor into a spatial part and a channel-mixing part, not arbitrary joint filters. In practice MobileNetV1 lost about 1% ImageNet top-1 versus a comparable full-conv net for roughly 8x fewer FLOPs — an overwhelming trade. And you don't write a special layer for depthwise; it's just Conv2d with groups=Cin , which forces each channel into its own group. class SeparableConv ( nn . Module ): def __init__ ( self , Cin , Cout , Dk = 3 , stride = 1 ): super (). __init__ () self . dw = nn . Conv2d ( Cin , Cin , Dk , stride , Dk // 2 , groups = Cin , bias = False ) # space self . pw = nn . Conv2d ( Cin , Cout , 1 , bias = False ) # channels self . bn1 , self . bn2 = nn . BatchNorm2d ( Cin ), nn . BatchNorm2d ( Cout ) def forward ( self , x ): x = torch . relu ( self . bn1 ( self . dw ( x ))) return torch . relu ( self . bn2 ( self . pw ( x ))) On top, MobileNet adds two global shrink dials: a width multiplier α scaling every channel count (cost ∝ α² ) and a resolution multiplier ρ scaling the input (cost ∝ ρ² ), sweeping out a whole family on the accuracy/latency curve. The separable block went on to power MobileNetV2's inverted residuals, V3 (plus squeeze-excite), and EfficientNet — it's now the default building block for anything that runs on a phone. Drag the four dimensions and watch the multiply-adds recompute: https://dev48v.infy.uk/dl/day41-depthwise-separable.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/depthwise-separable-convolutions-how-mobilenet-gets-8-9x-fewer-multiplies-by-splitting-one-conv-4o82

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
