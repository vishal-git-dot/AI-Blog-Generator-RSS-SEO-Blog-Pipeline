---
title: "I Replaced a Q-Table With a Neural Network and Everything Changed - Day 5 (DQN)."
slug: "i-replaced-a-q-table-with-a-neural-network-and-everything-changed-day-5-dqn"
author: "Madhumitha Kolkar"
source: "devto_python"
published: "Fri, 24 Jul 2026 03:06:41 +0000"
description: "SERIES: Learning RL and JAX in Public - from zero to DeepMind :) Day 4 ended with a working Q-learning agent. A table of numbers that an agent used to naviga..."
keywords: "network, state, same, learning, you, target, table, dqn"
generated: "2026-07-24T03:18:16.301130"
---

# I Replaced a Q-Table With a Neural Network and Everything Changed - Day 5 (DQN).

## Overview

SERIES: Learning RL and JAX in Public - from zero to DeepMind :) Day 4 ended with a working Q-learning agent. A table of numbers that an agent used to navigate a gridworld. Clean, simple, satisfying. Day 5 started with one question: what happens when the state space is too large for a table? Imagine instead of a 16-cell grid, your state is the pixels of a video game screen. There are more possible Atari frames than atoms in the universe. You cannot have a table row for each one. The Q-table breaks immediately. DQN is the answer. And it is simpler than it sounds. The one change that makes DQN In Q-learning: q_value = q_table [ state , action ] In DQN: q_values = neural_network ( state ) # returns one Q-value per action That is the whole idea. Replace the table lookup with a neural network forward pass. The Bellman equation stays the same. Epsilon-greedy stays the same. The training loop structure stays the same. The network takes the current state as input and outputs a Q-value for every possible action. You still pick the highest one. The only difference is where the numbers come from. Why neural networks generalise where tables cannot : A Q-table only knows about states it has explicitly visited. State 7 ? Only useful if the agent has been to state 7 before. A neural network learns patterns. If states 3, 7, and 11 all have similar features (say, they are all near a hole), the network learns that similarity and can make reasonable predictions for states it has never visited. This is what allows DQN to scale. The two problems DeepMind had to solve : Before DeepMind's 2013 paper, people had been trying to combine neural networks with RL for years. It kept failing. The network would improve for a while and then suddenly collapse and forget everything. DeepMind solved this with two tricks that are now standard in every RL codebase. Problem 1: Correlated samples : In supervised learning you shuffle your dataset and sample random batches. This is important because the network needs diverse examples each step, not 32 consecutive frames from the same game session. In RL, consecutive transitions are extremely correlated. The agent is in state 4, goes to state 5, then state 6. Training on these in sequence is like training a classifier on 32 pictures of the same cat in a row. Fix: Experience Replay. Store every transition in a buffer. Sample randomly from it when training. Correlation broken. replay_buffer . add ( state , action , reward , next_state , done ) batch = replay_buffer . sample ( batch_size = 32 ) # random, not sequential Problem 2: Moving targets The Bellman target is: target = reward + gamma * max ( Q ( next_state )) But Q(next_state) comes from the same network you are updating. So every time you nudge the network, the target moves too. You are chasing a bullseye that runs away from you every time you take a step. Fix: Target Network. Keep two copies of the network. Update only the online network each step. Every 100 steps, copy the online network weights into the target network. The target network provides stable Bellman targets while the online network trains against them. # use target network for stable bellman target target = reward + gamma * max ( target_network ( next_state )) # update only the online network loss = ( target - online_network ( state )[ action ]) ** 2 What I built today : Same 4x4 gridworld from Day 4. But instead of a Q-table, a three-layer neural network in raw JAX. Input: one-hot encoding of the state. Output: Q-values for all four actions. The training loop : for each episode : while not done : action = epsilon_greedy ( online_network , state ) next_state , reward , done = env_step ( state , action ) replay_buffer . add ( state , action , reward , next_state , done ) if len ( buffer ) >= 200 : batch = replay_buffer . sample ( 32 ) loss , grads = grad_fn ( online_params , target_params , batch ) online_params = update ( online_params , grads ) if step % 100 == 0 : target_params = online_params # refresh anchor After 1500 episodes, the policy arrows matched what Q-learning produced on Day 4. Same environment, same result, different mechanism. The DQN learned it too. The thing that actually hit me today : When I printed the Section 7 comparison at the end of the code: Q-learning: Q-values stored in a table (64 numbers) DQN: Q-values stored in a neural network Same Bellman equation. Same epsilon-greedy. Same goal. The only difference is where the Q-values come from. Six years in ML and I had never sat down and traced the line from Q-learning to DQN to AlphaGo. It is one continuous idea, each step replacing one component with something that scales better. Tables become networks. Networks become deeper. State spaces become images. Rewards become sparse. But the core Bellman intuition runs through all of it. That is the thing about learning from first principles. You stop using tools and start understanding systems. Also worth noting: this is the paper that put DeepMind on the map. "Playing Atari with Deep Reinforcement Learning", 2013. If you have not read it, it is surprisingly readable. The ideas are exactly what we implemented today, just applied to pixel inputs and 18 actions instead of 16 states and 4 actions. All code from this series, organised by day, is on my GitHub: https://github.com/MadhumithaKolkar/jax-rl-lab Happy learning everyone ! ~ Madhumitha Kolkar (index_0)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/madhumithakolkar/i-replaced-a-q-table-with-a-neural-network-and-everything-changed-day-5-dqn-31ag

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
