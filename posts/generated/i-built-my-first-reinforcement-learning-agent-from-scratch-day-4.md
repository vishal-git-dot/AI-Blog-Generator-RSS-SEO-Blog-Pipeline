---
title: "I Built My First Reinforcement Learning Agent From Scratch - Day 4."
slug: "i-built-my-first-reinforcement-learning-agent-from-scratch-day-4"
author: "Madhumitha Kolkar"
source: "devto_python"
published: "Thu, 23 Jul 2026 03:18:05 +0000"
description: "SERIES: Learning RL and JAX in Public - from zero to DeepMind :) Today was different. Today the agent actually learned something. Days 1 through 3 were JAX f..."
keywords: "agent, reward, state, action, learning, value, table, epsilon"
generated: "2026-07-23T03:24:20.277559"
---

# I Built My First Reinforcement Learning Agent From Scratch - Day 4.

## Overview

SERIES: Learning RL and JAX in Public - from zero to DeepMind :) Today was different. Today the agent actually learned something. Days 1 through 3 were JAX fundamentals - arrays, gradients, jit, vmap. All of it was preparing for this. Day 4 is where reinforcement learning actually begins. I built a Q-learning agent from scratch and watched it navigate a gridworld. By the end of 2000 episodes, it was finding the goal reliably. No hand-coded rules. No labels. Just an agent figuring out the world through trial and error. Here is how it works. The setup : A 4x4 grid. The agent starts at the top-left. The goal is at the bottom-right. There are holes scattered around. Fall in a hole and the episode ends with a negative reward. Reach the goal and you get a positive reward. S . . . . H . H . . . H H . . G S = start, G = goal, H = hole. The agent can move up, down, left, or right. That is it. 16 states, 4 actions. What is a Q-value ? Before writing any code, I had to understand this properly. A Q-value answers one question: if I am in this state and I take this action, how much total reward will I collect from here onwards if I play well? It is a table. Rows are states. Columns are actions. Every cell is a number. UP DOWN LEFT RIGHT state 0: 1.2 3.4 0.8 2.1 state 1: 0.5 0.9 2.3 1.1 ... At state 0, the agent looks at the row, picks the highest number, and takes that action. That is the entire policy. The whole job of Q-learning is to fill this table with the right numbers. The Bellman equation : At the start, every Q-value is zero. The agent knows nothing. After taking an action and getting a reward, it makes a small correction to the relevant cell: Q(s, a) = Q(s, a) + alpha * (target - Q(s, a)) Where target = reward + gamma * best Q-value in the next state. This is the Bellman equation. It says: the value of being here and taking this action should equal the immediate reward plus the best value available from where you end up. The agent does this correction thousands of times. Slowly the table fills with values that reflect how good each action actually is. Exploration vs exploitation : Here is a problem. If the agent always picks the action with the highest Q-value, it never tries anything new. It might settle for a mediocre path because it never explored better ones. The solution is epsilon-greedy: With probability epsilon: pick a random action (explore) With the rest: pick the best known action (exploit) Epsilon starts at 1.0 (fully random) and decays over time toward 0.01 (mostly greedy). At the start the agent wanders. By the end it has earned the right to trust its own table. The training loop in code : for episode in range ( 2000 ): state = START_STATE while True : action = choose_action ( state , q_table , epsilon ) next_state , reward , done = step ( state , action ) # Bellman update target = reward + gamma * np . max ( q_table [ next_state ]) q_table [ state , action ] += alpha * ( target - q_table [ state , action ]) state = next_state if done : break epsilon = max ( 0.01 , epsilon * 0.995 ) That is the whole thing. No neural network. No backpropagation. Just a table being updated one cell at a time. What the agent learned : After 2000 episodes, the policy arrows looked like this: > > v v ^ H v H ^ > v H H > > G It learned to avoid holes. It learned the shortest path. It built this entirely from reward signals, no supervision. The reward curve told the whole story. Early episodes: negative reward, the agent kept falling in holes. Around episode 500: reward starts climbing. By episode 2000: consistently positive, consistently reaching the goal. Why does this matter beyond a gridworld ? Q-learning is the foundation of DQN, which is the foundation of AlphaGo, which is the foundation of everything DeepMind built in the RL space. The gridworld feels toy-sized but the mechanics are identical. The only difference in modern deep RL is that the Q-table gets replaced by a neural network because the state space is too large to enumerate. That is literally the next step in this series. One thing I genuinely did not expect: how satisfying it is to watch an agent learn. There is something different about seeing a system figure something out on its own versus supervising it toward a known answer. I think this is why RL has such a hold on people who work in it. All code from this series, organised by day, is on my GitHub: https://github.com/MadhumithaKolkar/jax-rl-lab Happy learning everyone ! ~ Madhumitha Kolkar (index_0)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/madhumithakolkar/i-built-my-first-reinforcement-learning-agent-from-scratch-day-4-2fp7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
