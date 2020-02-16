import random
def random_walk_01(n):
    """Return coordinates after" n block random walk"""
    x=0
    y=0
    for i in range(n):
        dir=random.choice(['N','S','E','W'])
        if dir=='N':
            y+=1
        elif dir=='S':
            y-=1
        elif dir=='E':
            x+=1
        else:
            x-=1
    return x,y



def random_walk_02(n):
    """Return coordinates after" n block random walk"""
    x,y=0,0
    for i in range(n):
        dx,dy=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
    return x,y

for i in range(25):
    walk=random_walk_02(10)
    print(walk, "Distance from home = " ,abs(walk[0]+walk[1]))



number_of_walks=10000
for walk_length in range(1,31):
    no_transport=0
    for i in range(number_of_walks):
        x,y=random_walk_02(walk_length)
        distance=abs(x+y)
        if distance<=4:
            no_transport+=1
    no_transport_percentage=float(no_transport)/number_of_walks
    print("Walk Size = ", walk_length, "/ % of no transport = ",100*no_transport_percentage)