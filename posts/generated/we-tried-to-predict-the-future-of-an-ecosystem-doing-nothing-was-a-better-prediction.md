---
title: "We Tried to Predict the Future of an Ecosystem. Doing Nothing Was a Better Prediction."
slug: "we-tried-to-predict-the-future-of-an-ecosystem-doing-nothing-was-a-better-prediction"
author: "Emil Fournier"
source: "devto_ai"
published: "Thu, 26 Nov 2026 21:06:18 +0000"
description: "My best friend Timothée and I are working on a project called Arbor. We're trying to find out whether machine learning can predict how ecosystems will evolve..."
keywords: "our, environmental, data, how, arbor, can, model, one"
generated: "2026-11-26T21:14:22.329314"
---

# We Tried to Predict the Future of an Ecosystem. Doing Nothing Was a Better Prediction.

## Overview

My best friend Timothée and I are working on a project called Arbor. We're trying to find out whether machine learning can predict how ecosystems will evolve over the next ten years. The idea came to us in October after watching a documentary about the Amazon rainforest. We had already been working on AI through GreenTrust AI, but this was a very different problem from anything we had worked on before. Our first experiment We built a small experimental model using historical environmental data to predict environmental conditions one year ahead. One of the most interesting things we found was that our model didn't outperform persistence overall. A persistence model essentially predicts that tomorrow's conditions will be the same as today's. In our case, it assumes that environmental conditions will remain unchanged from one year to the next. Many of the areas we were studying were relatively stable over that period. This meant that a very simple prediction was surprisingly difficult to beat. Our experiment was preliminary, and we're currently working on a more rigorous evaluation. But it made us reconsider parts of our approach. Getting a high overall accuracy doesn't necessarily mean that a model is good at predicting environmental changes. The data problem We're currently working with environmental data from sources such as MapBiomas, SoilGrids and OpenLandMap. One of the difficulties is that these datasets have very different spatial resolutions. Some of the data we want to use have a resolution of around 20–30 meters per pixel, while other datasets have resolutions of approximately 9 km per pixel. Local conditions matter, but so does the environment surrounding an area. We're currently exploring a pyramidal data structure that would allow us to work with information at different spatial resolutions. It's still an early idea, and we haven't yet established whether it will be an effective way to organize our training data. For our first larger study, covering around 10,000 km² in the Brazilian state of Pará, we estimate that we'll need approximately 500–700 GiB of environmental data. What we want to predict Rather than predicting a single environmental indicator, we want to explore whether we can predict changes in several variables related to vegetation, soil, water and fire. I've also been developing a mathematical formula to estimate the ecological condition of an area. Eventually, we want to calculate this score from the variables predicted by our models. Our initial target is to make yearly predictions over ten years. Before getting there, we need to answer a few questions: Can deep learning outperform persistence and other simpler models? How well can a model trained in one geographical area generalize to another? Which environmental variables can actually be predicted reliably? How should we estimate and communicate uncertainty? We're considering Markov models, naive Bayes classifiers and persistence models as baselines, depending on the prediction task. We're also interested in evaluating performance separately on stable areas and areas that have actually undergone environmental changes. What's next for Arbor? One of our biggest limitations right now is access to computing resources. We're developing Arbor ourselves, but running larger experiments and properly evaluating our models requires funding. We've launched a campaign on Manifund to help cover these costs. Our funding goal ranges from $500 for smaller experiments to $44,000 for our full research program. If you're interested in the project, our research proposal and funding breakdown are available here: Arbor – Using AI to Restore Nature Worldwide We're also interested in hearing from developers and researchers who have experience with geospatial machine learning or environmental forecasting. Where we're going with this The long-term idea behind Arbor is to help people working in ecological restoration better understand how an ecosystem might evolve before deciding how to intervene. We're not at the point where we can recommend restoration strategies. Predicting environmental changes is already a difficult problem, and predicting the effects of human interventions introduces another set of challenges. Timothée and I are both 17, and we're developing Arbor alongside our studies in Switzerland. We're currently preparing our first research report, which we hope to finish by December 12. We plan to publish our methodology, benchmarks, computational estimates and limitations. I'd be particularly interested in hearing from people who have worked with geospatial machine learning, multiresolution raster data or long-term environmental forecasting. How would you approach the data structure? Which baselines would you use? How would you evaluate a model when most of the observed environment remains stable? I'd love to hear your thoughts.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/emilarbor/we-tried-to-predict-the-future-of-an-ecosystem-doing-nothing-was-a-better-prediction-47j3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
