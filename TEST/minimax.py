def minimax(depth, node_index, maximizing_player, values, max_depth):

   
    if depth == max_depth:
        return values[node_index]
    
    if maximizing_player:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, max_depth)
            best = max(best, val)
        return best
    
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, max_depth)
            best = min(best, val)
        return best

def minimax_alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]
    
    if maximizing_player:
        best = float('-inf')
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        
        return best
    
    else:
        best = float('inf')
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        
        return best

def read_input():
    max_depth = int(input("Enter the maximum depth of the game tree: "))
    num_leaf_nodes = 2 ** max_depth
    values = []

    print(f"Enter {num_leaf_nodes} leaf node values (terminal values):")
    for i in range(num_leaf_nodes):
        value = int(input(f"Value for leaf node {i + 1}: "))
        values.append(value)
    
    return values, max_depth

def main():

    print("Choose the algorithm to run:")
    print("1. Minimax")
    print("2. Minimax with Alpha-Beta Pruning")

    choice = input("Enter your choice (1 or 2): ")


    values, max_depth = read_input()

    if choice == '1':
        optimal_value = minimax(0, 0, True, values, max_depth)
        print("The optimal value using Minimax is:", optimal_value)
    elif choice == '2':
        optimal_value = minimax_alpha_beta(0, 0, True, values, float('-inf'), float('inf'), max_depth)
        print("The optimal value using Minimax with Alpha-Beta Pruning is:", optimal_value)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
