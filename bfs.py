def bfs(open_list,close_list,goal,node):
    if len(open_list)==0:
        return close_list   
    close_list.append(open_list[0])
    if goal in close_list:
        return close_list
    temp1=open_list.pop(0)
    temp2=node[temp1]
    for i in temp2:
        if(i not in close_list and i not in open_list):
            open_list.append(i)
    return bfs(open_list,close_list,goal,node)  
n=int(input("enter the no. of nodes in the graph:"))
node={}
for i in range(n):
    name=input("enter the node:")
    link_no=int(input("enter the no. of nodes linked:"))
    link=[]
    for j in range(link_no):
        link.append(input("enter the neighbor node:"))
    node[name]=link
initial=input("enter the initial node:")
goal=input("enter the goal node:")
open_list=[]
close_list=[]
open_list.append(initial)
bfs_list=bfs(open_list,close_list,goal,node)
print("bfs of the graph:")
for i in bfs_list:
    print(i,end="\t")

