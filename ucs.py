def ucs(node,goal,open_list, close_list,cost):
    if goal in close_list:
         return close_list,cost
    elif len(open_list)==0:
        return close_list,cost
    min=open_list[0]
    for i in open_list: 
         if i[1]<min[1]:
             min=i
    temp=node[min[0]]
    close_list.append(min[0])
    cost+=min[1]
    open_list.remove(min)
    for i in temp:
        if i not in open_list and i not in close_list:
            open_list.append(i)
    return ucs(node, goal, open_list,close_list,cost)
n=int(input("enter the no. of node in the graph:"))
node={}
for i in range(n):
    name=input("Enter the node:")
    link=int(input("enter the no. of node linked:"))
    list1=[]
    for j in range(link):
        cost=()
        a=input("Enter the neighbor node:")
        b=int(input("enter the cost to that node:"))
        cost=(a,b)
        list1.append(cost)
    node[name]=list1
a=input("enter the start node:")
goal =input("enter the goal node:")
initial=(a,0)
close_list=[]
open_list=[]
open_list.append(initial)
cost=0
close_list,cost=ucs(node,goal,open_list,close_list,cost)
print("The path found by uniform cost search is:")
for i in close_list:
    print(i,end="\t")
print("\nThe cost for the path found is:",cost)
print(list1)



