"""P1: Breadth First Search (BFS) is a graph traversal algorithm used to explore nodes and edges in a graph systematically. 
It starts from a given node (source) and explores all its neighboring nodes at the present depth before moving on to nodes at the next depth level. 
BFS is particularly useful for finding the shortest path in unweighted graphs, where each edge has the same "cost." """

import queue

def bfs(graph, start):
    q = queue.Queue()
    visited = set()
    q.put(start)

    while not q.empty():
        node = q.get()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                q.put(neighbor)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [], 'F': [], 'G': [], 'H': []
}

bfs(graph, 'A')
