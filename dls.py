def dls(node,goal,list1,depth):  
    if goal in list1[0]:
        return list1
    elif len(list1[1])==0:
        return list1
    stack= list1[1]
    top =stack.pop()
    dfs1=list1[0]
    temp=node[top]
    if(temp.pop()<depth):
        for i in temp:
            if i not in dfs1 and i not in stack:
                stack.append(i)
    dfs1.append(top)
    list1[0]=dfs1
    list1[1]=stack
    return dls(node,goal, list1,depth)
n=int(input("enter the no. of node in the graph:"))
node={}
for i in range(n):
    name=input("enter the node:")
    d=int(input("enter the depth at which the node is present:"))
    link_no=int(input("enter the no. of nodes linked:"))
    link=[]
    for j in range(link_no):
        link.append(input("enter the neighbor node:"))
    link.append(d)
    node[name]=link
initial=input("enter the initial node:")
goal=input("enter the goal node:")
depth=int(input("enter the depth of the search:"))
dls1=[]
stack=[]
stack.append(initial)
list1=[]
list1.append(dls1)
list1.append(stack)
dls_list=dls(node , goal , list1,depth)
print("dls of the graph:")
dls1=dls_list[0]
for i in dls1:
    print(i,end="\t")
