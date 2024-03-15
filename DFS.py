def DFS(graph, start):
    visited = set()  # Set to keep track of visited nodes
    stack = [start]   # Initialize a stack with the starting node
    
    while stack:  # Continue until the stack is empty
        node = stack.pop()  # Pop a node from the top of the stack
        if node not in visited:
            print(node)  # Visit the node (You can do whatever you want with it)
            visited.add(node)  # Mark the node as visited
            # Push all neighboring nodes that have not been visited onto the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

DFS(graph, 'A')  # Start DFS from node 'A'
