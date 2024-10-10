def min_max(depth,node_index,player,values,maximum_depth):
    if maximum_depth==depth:
        return values[node_index]
    
    if player:
        best=float('-inf')
        for i in range(2):
            value=min_max(depth+1,node_index*2+i,False,values,maximum_depth)
            best=max(value,best)
        return best
    else:
        best=float("inf")
        for i in range(2):
            value=min_max(depth+1,node_index*2+i,True,values,maximum_depth)
            best=min(value,best)
        return best
'''
def alpha_beta(depth,node_index,player,values,maximum_depth,alpha=float("-inf"),beta=float("inf")):
    if depth==maximum_depth:
        return values[node_index]
    
    if player:
        best=float("-inf")
        for i in range(2):
            value=alpha_beta(depth+1,node_index * 2 + i,False,values,maximum_depth,alpha,beta)
            best=max(value,best)
            print(alpha)
            alpha=max(best,alpha)
            print(alpha)
            if alpha>=beta:
                print(f"the leaf node {values[node_index * 2 + i]} of node{values[node_index]} is pruned")
                break
        return best
    
    else:
        best=float("inf")
        for i in range(2):
            value=alpha_beta(depth+1,node_index*2+i,True,values,maximum_depth,alpha,beta)
            best=min(value,best)
            print(beta)
            beta=min(best,beta)
            print(beta)

            if alpha>=beta:
                print(f"the leaf node {values[node_index*2+i]} of node{values[node_index]} is pruned")
                break
        return best
'''
def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]
    
    if maximizing_player:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"the leaf node {values[node_index*2+i]} of node{values[node_index]} is pruned")
                break
        
        return best
    
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"the leaf node {values[node_index*2+i]} of node{values[node_index]} is pruned")
                break
        
        return best
def read_input():
    maxdepth=int(input("Enter the maximum depth of the graph :"))
    numofnodes=2** maxdepth
    values=[]

    for i in range(numofnodes):
        value=input(f"enter the leaf node value of node {i+1} :")
        values.append(value)

    return values,maxdepth

def main():
    print("\nEnter the Graph \n")
    values,maxdepth=read_input()

    minmax=min_max(0,0,True,values,maxdepth)
    print(f"the Optimal Value using the Min-Max Method is {minmax}")

    alphabeta=alpha_beta(0,0,True,values,float("-inf"),float("inf"),maxdepth)
    print(f"the Optimal Value using the Alpha-Beta Pruning Method is {alphabeta}")

if __name__=="__main__":
    main()