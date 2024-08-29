import heapq
class PuzzleState:
    def __init__(self, board, empty_pos, cost=0, parent=None):
        self.board = board
        self.empty_pos = empty_pos
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))


def heuristic(board, goal):
    return sum([1 if board[i] != goal[i] and board[i] != 0 else 0 for i in range(9)])


def generate_moves(state):
    board = state.board
    empty_pos = state.empty_pos
    moves = []
    x, y = divmod(empty_pos, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_empty_pos = new_x * 3 + new_y
            new_board = board[:]
            new_board[empty_pos], new_board[new_empty_pos] = new_board[new_empty_pos], new_board[empty_pos]
            moves.append(PuzzleState(new_board, new_empty_pos, state.cost + 1, state))
    
    return moves


def best_first_search(start_board, goal_board):
    start_state = PuzzleState(start_board, start_board.index(0))
    goal_state = PuzzleState(goal_board, goal_board.index(0))
    
    open_list = []
    closed_set = set()
    
    heapq.heappush(open_list, (heuristic(start_state.board, goal_state.board), start_state))
    
    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state.board == goal_state.board:
            return current_state
        
        closed_set.add(current_state)
        
        for move in generate_moves(current_state):
            if move not in closed_set:
                heapq.heappush(open_list, (heuristic(move.board, goal_state.board), move))
    
    return None


def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]


def read_input():
    print("Enter the start state of the 8-puzzle (use 0 for the empty space):")
    start_board = [int(x) for x in input().split()]
    print(start_board)
    print("Enter the goal state of the 8-puzzle (use 0 for the empty space):")
    goal_board = [int(x) for x in input().split()]
    print(goal_board)
    return start_board, goal_board


def main():
    start_board, goal_board = read_input()
    solution = best_first_search(start_board, goal_board)
    
    if solution:
        path = reconstruct_path(solution)
        print("Solution found! Moves:")
        for step in path:
            for i in range(0, 9, 3):
                print(step[i:i+3])
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
    

