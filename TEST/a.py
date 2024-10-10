from collections import deque

def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_new_states(state):
    new_states = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_states.append(new_state)
    
    return new_states

def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        if is_goal(current_state):
            return path
        
        visited.add(tuple(map(tuple, current_state))) 
        
        for new_state in generate_new_states(current_state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [new_state]))
    
    return None 


print("Start state :\n")
start_board = [0,2,3,1,4,6,7,5,8]
start_state=[]
for i in range(0,9,3):
    p=start_board[i:i+3]
    print(p)
    start_state.append(p)
print()

print("Goal state :\n")
goal_board = [1,2,3,4,5,6,7,8,0]
for i in range(0,9,3):
    p=goal_board[i:i+3]
    print(p)
print()



solution = bfs(start_state)


if solution:
    print("Solution found!!! Moves :\n")
    for step in solution:
        for row in step:
            print(row)
        print() 
else:
    print("No solution found.")