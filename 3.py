"""P3: A* Search is an informed search algorithm that finds the shortest path between a start node and a target node in a graph. It combines features of both Dijkstra’s Algorithm (which guarantees the shortest path) and Greedy Best-First Search (which uses heuristics to prioritize nodes closer to the goal). A* works by maintaining a priority queue of nodes to explore, sorted by the sum of the cost from the start node and a heuristic estimate of the cost to reach the goal.
"""

import queue

def a_star(graph, start, goal, h):
    pq = queue.PriorityQueue()
    pq.put((0, start))
    
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not pq.empty():
        current_cost, current = pq.get()

        if current == goal:
            break

        for neighbor, weight in graph[current].items():
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + h[neighbor]
                pq.put((priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path, cost_so_far[goal]

# Example graph and heuristic
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'E': {'G': 2},
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 6, 'E': 1, 'F': 2, 'G': 0}
path, cost = a_star(graph, 'A', 'G', h)

print("Path:", path)
print("Cost:", cost)
