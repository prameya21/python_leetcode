import random
def myRandom():
    return 4*round(random.random(),3)


def cust_random(s,e):
    len=e-s
    return s+len*random.random()
'''
for i in range(10):
    print(cust_random(3,7))

print('\n\n')

for i in range(10):
    print(random.uniform(3,7))



for i in range(20):
    print(random.normalvariate(5,0.2))


for i in range(20):
    print(random.randint(1,6))
'''



game=['rock','paper','scissors']
for i in range(20):
    print(random.choice(game))