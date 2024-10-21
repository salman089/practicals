"""P2: Depth First Search (DFS) is another graph traversal algorithm that explores as far along each branch as possible before backtracking. 
The iterative version of DFS avoids recursion by using an explicit stack data structure to store the nodes to be explored."""

import queue

def dfs(graph, start):
    stack = queue.LifoQueue()
    visited = set()  
    stack.put(start)

    while not stack.empty():
        node = stack.get()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.put(neighbor)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [], 'F': [], 'G': [], 'H': []
}

dfs(graph, 'A')
