a=int(input("enter the no. of litres of water can jug a hold:"))
b=int(input("enter the no. of litres of water can jug b hold:"))
def stategen(state):
     w_a=state[0]
     w_b=state[1]
     x=[a,w_b]
     y=[0,w_b]
     if w_b+w_a>b:
         z=[w_a-(b-w_b),b]
     else:
         z=[0,w_b+w_a]
     if w_a+w_b>a:
         p=[a,w_b-(a-w_a)]
     else:
         p=[w_b+w_a,0]
     return x,y,z,p
def bfs(queue,bfs_list,goal):
    for i in bfs_list:
        if i[0]==goal or i[1]==goal:
            return bfs_list
    if(len(queue)==0):
        return bfs_list
    front=queue.pop(0)
    bfs_list.append(front)
    p=stategen(front)
    for i in p:
         if i not in bfs_list and i not in queue:
            queue.append(i)
    return bfs(queue,bfs_list,goal)
goal=int(input("enter the no. litres to be brought in that jug:"))
bfs_list=[]
queue=[]
queue.append([0,0])
bfs_list=bfs(queue,bfs_list,goal)
print("bfs:")
print(bfs_list)
