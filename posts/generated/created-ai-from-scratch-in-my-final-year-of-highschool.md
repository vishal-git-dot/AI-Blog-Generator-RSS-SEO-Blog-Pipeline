---
title: "Created AI from Scratch in my final year of HighSchool"
slug: "created-ai-from-scratch-in-my-final-year-of-highschool"
author: "Aradhya Kumar Chandra"
source: "devto_python"
published: "Thu, 11 Jun 2026 20:11:12 +0000"
description: "Basic Pillars of AI based on Human Thinking~ My First step into Artificial Intelligence As, we all know, an AI ~ Takes decision on it's own It stores it's mi..."
keywords: "decision, down, maze, how, time, mistakes, project, can"
generated: "2026-06-11T20:28:40.307320"
---

# Created AI from Scratch in my final year of HighSchool

## Overview

Basic Pillars of AI based on Human Thinking~ My First step into Artificial Intelligence As, we all know, an AI ~ Takes decision on it's own It stores it's mistakes and learns from it It makes sure it does not repeat any mistake in future and thus takes better decisions . So, if we incoperate this logic into the programming, we will have made an AI!! Making of Maze AI My First AI project So, I am quite trained in Python and have been using it for 3 years now. Hence, I started answering each and every question one by one ~ "How to make a maze ?" -> Use pygame "How to know when to take decisions ?" -> We can throw yellow balls both up and down direction, and wherever it collides with vertical wall , to detect whether their is opening on top or not. Obstruction on top wall,(simply uses rect1.colliderect(rect2) to move forward) ~ And, if no obstruction both up and down, means it has to take decision 3."How to take decision ?" -> Use random module,deciding to go either UP or DOWN "TAKING DECISION" : CHECK ✅ 4."How to know final mistake/blockage(Deadend)" -> When it finally collides with a wall and both the yellow balls detects blockage It then records that the prev pos. where it took the DECISION,(say,Up), was wrong, and next time it should take decision Down After facing the blockage, the stickman automatically re-spawn and restarts at the starting position. 5."How to store mistakes ?" -> Use dictionary, in form of {(x,y):decision}, [where : (x,y) is the coordinate where it took the dicision(Up/Down)] "STORING MISTAKES" : CHECK ✅ 6."How not to repeat mistakes in future ?" -> While taking decision(Up/Down),I started checking the mistakes dict to know whether at that pos a mistake decision was recorded or not(say {(20,30):"Up"}), if yes, it takes other decision("Deciding Down due to mistake") "NOT REPEATING MISTAKES IN FUTURE" : CHECK ✅ 7.Now, a major part which made me Hustle a Lot ~ say, mistakes={(30,40):"Down"} in which it first took decision at (10,20) "Down" , then moving forward again took decision at (30,40) Next, time it takes decision Up at (30,40) and again face a blockage it will then store {(30,40):"UpDown"} So, therefore if any coordinate has "UpDown" both in them, their previous decision which led to this will automatically has to update it -> {(10,20):"Down",(30,40):"UpDown"} 8. The Last Thing -> I put a prize at end, so that when stickman reaches the prize, it knows that the maze is complete Therefore, using best_path list to always follow the shortest optimum path and use less time. 9.I also import time module , to calculate the time it took to find the prize, and the final time it takes to follow the best path when it has found the prize. THE MAZE ~ The Final Output and Results of my AI Hence, I build The Maze, The Stickman and The Prize ~ When I hit Spacebar, it starts moving and as it faces blockages,takes decisions,stores them, or take different decsion due to a registered mistake, It shows the following on screen ~ When, it finally reaches the prize, it prints the time taken and the best optimum path it configured ~ Now, No matter how many times I run it, it will always use the best path and it will take the least time to reach the prize ~ LIMITATIONS "Every First Project has some limitations" -Me (2026) Its, currently just at phase 1 MVP(Minimum Viable Product) The Limitations of my MAZE AI are ~ The stickman can for now only move in Up,Down and Right(Forward) , direction.It cannot turn Backward or go Left . Therfore, whenever facing a deadend, I have to restart at original point It, thus works in a unidirectional Tree Branch Maze. It can only detect the top-most or the lower-most walls for moving forward.But if, its stuck in a loop and there is a opening at the wall in the middle or lower or upper than the extreme ends, it cannot enter it and will go on and on in the loop . Help Me Improve: What's the next step ? Now, that the phase-1 is complete, I would like to get at phase 2 and get new ideas on what new and interesting things I can do with it.And How can I make the stickman navigate through complex mazes! Also, since this was just a project I did at home,just for my own interest,hobby and love for CS . I wanna know whether there are any competitions or platforms where I can show my project/maze ai and partcipate with other people, or get to showcase my project.I would love to get this project out there! Drop your ideas,advices,projects,or infos on where can I showcase my project, down in the comments below 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/redhat143/created-ai-from-scratch-in-my-final-year-of-highschool-1hc3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
