import heapq
start='arad'
goal='bucharest'
current='arad'
graph = {'arad': {'zerind': 75, 'timisora': 118, 'sibiu': 140}, 'zerind': {'arad': 75, 'oradea': 71}, 'timisora': {'arad': 118, 'lugoj': 111}, 'sibiu': {'arad': 140, 'oradea': 151, 'fagaras': 99, 'rimicu': 80}, 'fagaras': {'sibiu': 99, 'bucharest': 211}, 'bucharest': {'fagaras': 211, 'pitesti': 101}, 'pitesti': {'bucharest': 101, 'rimicu': 97}, 'oradea': {'zerind': 71, 'sibiu': 151}, 'dabaeu': {'rimicu': 80}, 'lugoj': {'timisora': 111}, 'rimicu': {'sibiu': 80, 'pitesti': 97, 'dabaeu': 80}}
{'arad':366, 'zerind':374, 'timisora':329, 'sibiu':253, 'fagaras':176, 'bucharest':0, 'pitesti':100, 'oradea':380, 'dabaeu':256, 'lugoj':244, 'rimicu':193}
heuristic={'arad':366, 'zerind':374, 'timisora':329, 'sibiu':253, 'fagaras':176, 'bucharest':0, 'pitesti':100, 'oradea':380, 'dabaeu':256, 'lugoj':244, 'rimicu':193}

open_list = []
heapq.heappush(open_list, (0, start))
came_from = {start: None}
g_costs = {start: 0}
v=graph[current]
print(v.items())

"""tentative_g_cost = g_costs[current] + cost
    if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
        g_costs[neighbor] = tentative_g_cost
        f_cost = tentative_g_cost + heuristic[neighbor]
        heapq.heappush(open_list, (f_cost, neighbor))
        came_from[neighbor] = current"""

