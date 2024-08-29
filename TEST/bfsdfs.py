from collections import deque

def bfs(graph, start, goal):
    if start not in graph or goal not in graph:
        return []  
    
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            result.append(vertex)
            return result
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return result

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
        
    if start not in graph or goal not in graph:
        return []  
    
    visited.add(start)
    result = [start]
    
    if start == goal:
        return result
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if goal in path:
                result.extend(path)
                return result
    
    return result

def read_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        u, v = input("Enter an edge (e.g., 'A B'): ").split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

graph = read_graph()
start_node = input("Enter the starting node: ")
goal = input("Enter the goal node: ")

bfs_result = bfs(graph, start_node, goal)
dfs_result = dfs(graph, start_node, goal)

print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)
