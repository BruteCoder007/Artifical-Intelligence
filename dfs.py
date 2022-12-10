def dfs(node,goal,list1):  
    if goal in list1[0]:
        return list1
    elif len(list1[1])==0:
        return list1
    stack= list1[1]
    top =stack.pop()
    dfs1=list1[0]
    temp=node[top]
    for i in temp:
        if i not in dfs1 and i not in stack:
            stack.append(i)
    dfs1.append(top)
    list1[0]=dfs1
    list1[1]=stack
    return dfs(node,goal, list1)      
n=int(input("enter the no. of node in the graph:"))
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
dfs1=[]
stack=[]
stack.append(initial)
list1=[]
list1.append(dfs1)
list1.append(stack)
dfs_list=dfs(node , goal , list1)
print("dfs of the graph:")
dfs1=dfs_list[0]
for i in dfs1:
    print(i,end="\t")
    