from collections import deque

class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start, goal):

        if start not in self.graph or goal not in self.graph:
            return None

        queue = deque([start])
        came_from = {start: None}

        while queue:
            current = queue.popleft()

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.graph[current]:
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

        return None 
    def dfs(self, start, goal):

        if start not in self.graph or goal not in self.graph:
            return None

        stack = [start]
        came_from = {start: None}

        while stack:
            current = stack.pop()

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.graph[current]:
                if neighbor not in came_from:
                    stack.append(neighbor)
                    came_from[neighbor] = current

        return None 

def create_graph_from_input():

    graph = {}
    
    while True:
        print("\nEnter an edge (format: node1 node2) or 'done' to finish:")
        edge_input = input().strip()
        
        if edge_input.lower() == 'done':
            break
        
        nodes = edge_input.split()
        if len(nodes) != 2:
            print("Invalid input. Please enter two nodes.")
            continue
        
        node1, node2 = nodes
        
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        
        graph[node1].append(node2)
        graph[node2].append(node1)  
    return graph

if __name__ == "__main__":
    print("Welcome to the Graph Search program!")
    graph = create_graph_from_input()

    start_node = input("\nEnter the start node: ").strip()
    goal_node = input("Enter the goal node: ").strip()

    search = GraphSearch(graph)

    bfs_path = search.bfs(start_node, goal_node)
    print("BFS Path:", bfs_path if bfs_path else "No path found")

    dfs_path = search.dfs(start_node, goal_node)
    print("DFS Path:", dfs_path if dfs_path else "No path found")
