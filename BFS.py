from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node

    while queue:  # Continue until the queue is empty
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            print(node)  # Visit the node (You can do whatever you want with it)
            visited.add(node)  # Mark the node as visited
            # Enqueue all neighboring nodes that have not been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # Start BFS from node 'A'
