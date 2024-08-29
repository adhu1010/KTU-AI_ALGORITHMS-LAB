from collections import deque

def bfs(adj_list,startnode,visit,goal):
    q = deque()
    visit[startnode]=True
    q.append(startnode)
    path=[]
    while q:
        node = q.popleft()
        path.append(node)
        for i in adj_list[node]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True
    if goal in path:
        for i  in path:
            print(i,end="")
            if i==goal:
                print("\n goal found")
                break
            print("-->",end="")
    else:
        print("goal not found")





def dfsa(adj_list,startnode,visited,path):
    visited.append(startnode)
    path.append(startnode)
    for i in adj_list[startnode]:
        if i not in visited:
            dfsa(adj_list,i,visited,path)
    
def dfs(adj_list,startnode,goal):
    v=deque()
    path=[]
    dfsa(adj_list,startnode,v,path)
    if goal in path:
        for i  in path:
            print(i,end="")
            if i==goal:
                print("\n goal found")
                break
            print("-->",end="")
    else:
        print("goal not found")



    


n=int(input("enter the number of the nodes :"))
adj_list=[[]for i in range(n)]
for i in range(n):
    
    m=int(input(f"enter no of the neighbouirng edges of {i}"))
    print(f"enter the neighbouring edges of {i}")
    for j in range(m):
       
        p=int(input())
        adj_list[i].append(p)
print(adj_list)
visit=[False]*n
st=int(input("enter the start node :"))
g=int(input("enter the goal node :"))
bfs(adj_list,st,visit,g)
dfs(adj_list,st,g)
