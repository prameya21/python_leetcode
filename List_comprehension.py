def squares_01(n):
    data=[]
    for i in range(1,n):
        data.append(i**2)
    return data



def squares_02(n):
    return [i**2 for i in range(1,n)]


def remainders_5(n):
    return [x**2%5 for x in range(1,n)]

def remainder_11(n):
    return [ x**2%11 for x in range(1,n)]

def p_remainders(p):
    return [x**2%p for x in range(0,p)]



print(remainders_5(101))
print(remainder_11(101))
print(p_remainders(101))