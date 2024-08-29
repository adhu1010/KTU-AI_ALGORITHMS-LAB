import heapq

def best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    came_from = {start: None}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)
       
        if current in visited:
            continue
       
        visited.add(current)

        if current == goal:
            break
       
        for neighbor in graph[current]:
            if neighbor not in visited:
                priority = heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    g_costs = {start: 0}
   
    while open_list:
        _, current = heapq.heappop(open_list)
       
        if current == goal:
            break
       
        for neighbor, cost in graph[current]:
            tentative_g_cost = g_costs[current] + cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current
   
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

def get_graph_input_bfs():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors_input = input(f"Enter neighbors of {node} comma-separated names: ")
        if ',' in neighbors_input:
            neighbors = neighbors_input.split(',')
            graph[node] = [neighbor.strip() for neighbor in neighbors]
    return graph

def get_graph_input_astar():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors_input = input(f"Enter neighbors of {node} (format: neighbor1,cost1 neighbor2,cost2): ")
        if ',' in neighbors_input:
            neighbors = neighbors_input.split()
            graph[node] = [(n.split(',')[0].strip(), int(n.split(',')[1].strip())) for n in neighbors]
    return graph
     
def get_heuristic_input():
    heuristic = {}
    num_nodes = int(input("Enter the number of nodes for heuristic values: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        value = int(input(f"Enter heuristic value for {node}: "))
        heuristic[node] = value
    return heuristic

def main():
    print("Choose the search algorithm:")
    print("1. Best-First Search")
    print("2. A* Search")
    choice = input("Enter the number (1 or 2): ")

    if choice == '1':
        graph = get_graph_input_bfs()
        heuristic = get_heuristic_input()
        start = input("Enter the start node: ")
        goal = input("Enter the goal node: ")
        path = best_first_search(graph, start, goal, heuristic)
        print(f"Best-First Search Path found: {path}")
    elif choice == '2':
        graph = get_graph_input_astar()
        heuristic = get_heuristic_input()
        start = input("Enter the start node: ")
        goal = input("Enter the goal node: ")
        path = a_star_search(graph, start, goal, heuristic)
        print(f"A* Search Path found: {path}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
	

