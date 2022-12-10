from copy import deepcopy
initial=[]
print("enter the initial state of the puzzle:")
for i in range(3):
        l1=[]
        a,b,c=input("enter the row of the matrix:").split()
        a=int(a)
        b=int(b)
        c=int(c)
        l1.append(a)
        l1.append(b)
        l1.append(c)
        initial.append(l1)
goal=[]
print("enter the goal state of the puzzle:")
for i in range(3):
        l1=[]
        a,b,c=input("enter the row of the matrix:").split()
        a=int(a)
        b=int(b)
        c=int(c)
        l1.append(a)
        l1.append(b)
        l1.append(c)
        goal.append(l1)
def heuristic(state):
    count=0
    # for i in range(3):
    #     for j in range(3):
    #         if state[i][j]!=goal[i][j]:# This is using the no. of misplaced tiles
    #             count+=1
    # count-=1
    # return count
    #following is done using manhattan distance
    list1=[]
    for i in state:
        for j in i:
            if(j==i):
                break
            flag=0
            for k in range(3):
                for l in range(3):
                    if goal[k][l]==j:
                        list1.append(k+l)
                        flag=1
                        break
                if(flag==1):
                    break
    return sum(list1)    
def position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
def possiblegen(state):
    i,j=position(state)
    list1=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    list2=[]
    a=[i,j+1]
    b=[i,j-1]
    c=[i+1,j]
    d=[i-1,j]
    list2.append(a)
    list2.append(b)
    list2.append(c)
    list2.append(d)
    possible=[]
    for k in list2:
        if(k in list1):
           state1=deepcopy(state)
           state1[i][j]=state[k[0]][k[1]]
           state1[k[0]][k[1]]=0
           possible.append(state1)
    return possible
def Astar(path,depth):
    if(goal in path):
        return path
    elif len(path)==0:
        return path
    top=path[len(path)-1]
    possible=possiblegen(top)
    min=possible[0]
    for i in possible:
        if(heuristic(i)+depth<heuristic(min)+depth):
            if(i not in path):
                min=i
    path.append(min)
    depth+=1
    return Astar(path,depth)
def printer(path): 
    for i in path:
        for j in range(3):
            for k in range(3):
                print(i[j][k],end='\t')
            print("\n")
        if(path[len(path)-1]==i):
            break
        print("        ||       ")
depth=0
path=[]
path.append(initial)
print("The initial state of the problem:")
printer(path)
path=Astar(path,depth)
print("The Solution for the Sliding puzzle problem:")
printer(path)


    
            
    


