"""P:4 Recursive Best-First Search (RBFS) is an informed search algorithm similar to A*. However, unlike A*, which uses a priority queue to keep track of all possible paths, RBFS uses recursion to explore the most promising paths while maintaining a limited memory footprint. RBFS tries to minimize memory usage by backtracking when necessary, replacing the need to store all possible nodes in memory.
"""

def rbfs_with_stack(start, goal, graph, h):
    stack = [(start, 0)]  # (current_node, f_value)
    best_path = []
    f_limit = h[start]  # Initial f-limit

    while stack:
        node, g = stack.pop()
        f_value = g + h[node]

        if node == goal:
            return best_path + [node]  # Path found

        # Check if the f_value exceeds the limit
        if f_value > f_limit:
            continue

        best_path.append(node)  # Add the current node to the best path

        for neighbor in graph[node]:
            neighbor_g = g + 1  # Assuming cost to neighbor is 1
            neighbor_f = neighbor_g + h[neighbor]
            stack.append((neighbor, neighbor_g))  # Push the neighbor onto the stack

        # Update f_limit for the next iteration
        f_limit = min(f_limit, f_value)

    return None  # No path found


# Example graph and heuristic
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

h = {'A': 5, 'B': 3, 'C': 4, 'D': 1, 'E': 2, 'F': 2, 'G': 0}
start = 'A'
goal = 'G'

path = rbfs_with_stack(start, goal, graph, h)
print("Path:", path)
