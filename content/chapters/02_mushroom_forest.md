# Chapter 2. The Mushroom Forest Labyrinth and Shortest Path Search

## 2.1 Formulating the Search Problem

Giant mushrooms blocked out the sunlight, turning the forest thicket into a confusing maze. Paths meandered between roots, descending into ominous darkness. Mario tried to take a step forward but immediately got tangled in vines.

— Stop, Mario, — Luigi stopped him, pulling a tablet from his backpack. — The "trial and error" method won't work here. We need a formal mathematical formulation of the search problem. Before the algorithm starts sorting through paths, we must clearly describe the world using five components:

1. Initial State: The point where we are standing right now. Let's denote it as s0=Forest Edge.
2. Actions: The set of valid moves from the current state. For each node, this is A(s)={North,South,East,West}.
3. Transition Model: The function Result(s,a) that mathematically determines which new state s′ the robot will reach if it executes action a in state s.
4. Goal Test: A Boolean function IsGoal(s) that checks whether we have reached the forest exit. It returns True if the state is the goal, and False otherwise.
5. Path Cost: A numeric function g(n) that sums up battery energy expenditure, track wear, and time spent overcoming each segment of the path. The robot's goal is to find the path with the minimum cost.

![Место для изображения: лес-лабиринт](assets/chapter2.jpg)

## 2.2 Uninformed Search: BFS, DFS, and Uniform Cost Search (UCS)

ROBO-LUMA deployed its antenna and began scanning the structure of nearby nodes. Luigi explained to Mario the difference between three classic blind (uninformed) search methods:

- Depth-First Search (DFS): Uses a LIFO (Last In, First Out — stack) data structure. The robot chooses one path and stubbornly follows it to the very end. If it hits a dead end filled with enemies, it backtracks. The memory complexity of DFS is relatively low (O(bm)), but it provides zero guarantee of finding the shortest path and can wander endlessly in cyclic graphs.
- Breadth-First Search (BFS): Uses a FIFO (First In, First Out — deque queue) structure. The robot explores the maze in concentric layers, checking all neighbors at the current level before going deeper. BFS is complete and guarantees finding the shortest number of steps, but only if the cost of each step is uniform (c=1). Its main drawback is the astronomical memory and time complexity of O(bd), where b is the branching factor and d is the search depth.
- Uniform Cost Search (UCS): Uses a priority queue (Min-Heap). Unlike BFS, which only counts the number of steps, UCS expands the node with the lowest total path cost g(n). If graph edges have varying difficulty (e.g., mud requires more energy than a dry path), UCS guarantees finding the absolute optimal path.


## 2.3 Informed Search A∗ and Heuristic Function h(n)

— But uniform cost search works way too slowly when there are thousands of crossroads ahead of us! — Mario exclaimed, looking at the robot's battery indicator.

— Exactly, which is why we're bringing in the heavy artillery — the A∗ heuristic algorithm, — Luigi nodded. — The key element of A∗ is the heuristic function h(n), which provides an estimate of the remaining distance from the current node n to the desired forest exit.

The total cost of a node in the A∗ algorithm is calculated as:

```
f(n)=g(n)+h(n)
```

where:

- g(n) is the exact cost of the path already traveled from the start to node n.
- h(n) is the heuristic estimate of the distance from node n to the goal.

As a heuristic for the maze grid, Luigi implemented the Manhattan Distance, which measures distance vertically and horizontally without diagonal shortcuts:

```
hManhattan(n)=∣xn−xgoal∣ ∣ + yn−ygoal∣
```

Critical Rule: For the A∗ algorithm to guarantee finding the shortest path, the heuristic must be admissible. This means that h(n) must never overestimate the true remaining cost of reaching the goal (h(n)≤h∗(n)).


## 2.4 Practical Implementation of Search in Python

Luigi displayed the working code listing for Uniform Cost Search (UCS) on ROBO-LUMA's processor screen, which the robot uses for autonomous navigation:

```python
import heapq
def uniform_cost_search(graph, start, goal):
 # Priority queue stores tuples: (g(n), current_node, path)
 pq = [(0, start, [start])]
 visited = {}
 while pq:
     cost, node, path = heapq.heappop(pq)
     if node == goal:
        return cost, path
     if node in visited and visited[node] <= cost:
        continue
     visited[node] = cost
     for neighbor, edge_cost in graph.get(node, []):
         new_cost = cost + edge_cost
         if neighbor not in visited or new_cost < visited[neighbor]:
            heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
 return float("inf"), []
# Mushroom Forest path graph with edge weights (energy costs)
forest_graph = {
 'Entrance': [('Glade', 2), ('Ruin', 5)],
 'Glade': [('Bridge', 3), ('Swamp', 8)],
 'Ruin': [('Bridge', 1), ('Cave', 7)],
 'Bridge': [('Exit', 2)],
 'Swamp': [('Exit', 1)],
 'Cave': [('Exit', 3)]
}
cost, path = uniform_cost_search(forest_graph, 'Entrance', 'Exit')
print(f"Optimal route: {path} with energy cost: {cost}")
```

Having successfully executed the script, ROBO-LUMA confidently turned onto the path through "Ruin" and "Bridge," bypassed the dangerous swamps, and successfully led the heroes to the foothills of the World 3 mountain cliffs.