---
title: "A* Search on grid based pathfinding with obstacle avoidance"
slug: "a-search-on-grid-based-pathfinding-with-obstacle-avoidance"
author: "saksham780"
source: "devto_python"
published: "Tue, 06 Oct 2026 13:00:55 +0000"
description: "A* Pathfinding in Python: Build a Grid Navigation Engine Around Obstacles How a smart heuristic guides a shortest-path search, with working Python code. Ever..."
keywords: "grid, path, current, neighbor, row, col, self, start"
generated: "2026-10-06T13:06:53.998241"
---

# A* Search on grid based pathfinding with obstacle avoidance

## Overview

A* Pathfinding in Python: Build a Grid Navigation Engine Around Obstacles How a smart heuristic guides a shortest-path search, with working Python code. Every time an enemy in a video game walks around a wall to find you, or a warehouse robot moves between shelves to reach a package, something has to work out the route. One of the most widely used algorithms for this kind of problem is A* (pronounced “A-star”). The idea is simple: instead of exploring every direction equally, A* asks which available position looks most promising. It combines the cost of the path so far with an estimate of the remaining distance. In this post, we will build an A* pathfinder in Python for a grid with walls. The problem we are solving We have a 2D grid. Each cell is either open ( 0 ) or a wall ( 1 ). We start in one cell and want to reach another, moving up, down, left, or right. Breadth-first search (BFS) can also solve this problem when every move has the same cost. A* can reduce unnecessary exploration by using information about where the goal is. How A* thinks: f(n) = g(n) + h(n) A* gives every candidate cell a score and expands the cell with the lowest score first. Term Name Meaning g(n) Cost so far Exact cost from the start to the current cell. h(n) Heuristic Estimate of the remaining cost to the goal. f(n) Total score g(n) + h(n) . For a four-direction grid, Manhattan distance is a standard heuristic: text h(a, b) = |a.row - b.row| + |a.col - b.col| Manhattan distance does not overestimate the true cost in this setting, which preserves the shortest-path guarantee. The Python implementation python import heapq class Node: def init (self, row, col): self.row = row self.col = col self.g = float("inf") self.h = 0 self.f = float("inf") self.parent = None def __lt__(self, other): return self.f < other.f def manhattan(a, b): return abs(a.row - b.row) + abs(a.col - b.col) def astar(grid, start, goal): rows, cols = len(grid), len(grid[0]) for r, c in (start, goal): if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 1: return [] start_node = Node(*start) goal_node = Node(*goal) start_node.g = 0 start_node.h = manhattan(start_node, goal_node) start_node.f = start_node.h open_heap = [(start_node.f, start_node)] open_lookup = {start: start_node} closed = set() moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] while open_heap: _, current = heapq.heappop(open_heap) pos = (current.row, current.col) if pos in closed: continue open_lookup.pop(pos, None) if pos == goal: path = [] while current: path.append((current.row, current.col)) current = current.parent return path[::-1] closed.add(pos) for dr, dc in moves: nr, nc = current.row + dr, current.col + dc if not (0 <= nr < rows and 0 <= nc < cols): continue if grid[nr][nc] == 1 or (nr, nc) in closed: continue new_g = current.g + 1 neighbor = open_lookup.get((nr, nc)) if neighbor is None: neighbor = Node(nr, nc) neighbor.h = manhattan(neighbor, goal_node) open_lookup[(nr, nc)] = neighbor elif new_g >= neighbor.g: continue neighbor.parent = current neighbor.g = new_g neighbor.f = new_g + neighbor.h heapq.heappush(open_heap, (neighbor.f, neighbor)) return [] Seeing it work python from astar import astar grid = [ [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], ] path = astar(grid, start=(0, 0), goal=(4, 5)) print("Path found in", len(path) - 1, "steps") print(path) Output: text Path found in 9 steps [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)] The route can be visualised as: text S . . . . . # # # # . . . . # . # # . # . * * * * G How fast is it? In the worst case, A* may need to examine many or even all cells. With a binary heap, a common rough bound for this implementation is O(N log N) for N discovered cells. In practice, a good heuristic can keep the search focused. Memory usage is O(N) because the algorithm stores information about discovered cells. Common mistakes to avoid Mixing up row and column. Forgetting the closed-set check. Using a heuristic that overestimates the remaining cost when you need a shortest-path guarantee. Not validating the start and goal. Where to go from here Add diagonal movement and use octile distance. Add weighted terrain. Explore Jump Point Search or hierarchical pathfinding. Visualise the open and closed sets. Final takeaway A* connects a simple mathematical idea with practical software. The formula f(n) = g(n) + h(n) , a priority queue, and a few sets are enough to build a shortest-path solver for a four-direction grid. Once you understand this version, the same structure can be adapted to game maps, road networks, warehouse robots, and other navigation problems. Suggested tags: Python, Algorithms, A-Star, Pathfinding, Data Structures, DSA, Programming

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/saksham780/a-search-on-grid-based-pathfinding-with-obstacle-avoidance-1knm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
