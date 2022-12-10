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
def bds(dfs1,dfs2):
    for i in range(len(dfs1)):
        if dfs1[i]==dfs2[i]:
            return dfs1[:i+1]+dfs2[:i],dfs1[i]
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
dfs_front=dfs(node , goal , list1)
dfs_front=dfs_front[0]
print(dfs_front)
list2=[]
dfs2=[]
stack2=[]
stack2.append(goal)
list2.append(dfs2)
list2.append(stack2)
dfs_back=dfs(node,initial,list2)
dfs_back=dfs_back[0]
print(dfs_back)
bds_list,intersect=bds(dfs_front,dfs_back)
print("Bidirectional search  of the graph:")
print("The intersection node is:",intersect)
for i in bds_list:
    print(i,end="\t")
