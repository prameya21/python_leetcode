from functools import  lru_cache
def fibonacci_01(a):
    if a==1 or a==2:
        return 1
    else:
        return fibonacci_01(a-1)+fibonacci_01(a-2)


cache_01={}
def fibonacci_02(n):
        if n in cache_01:
            return cache_01[n]
        elif n==1 or n==2:
            return 1
        else:
            cache_01[n]=fibonacci_02(n-1)+fibonacci_02(n-2)
            return cache_01[n]


def fibonacci_03(n,cache):
    if n in cache:
        return cache[n]
    elif n==1 or n==2:
        return 2
    else:
        cache[n]=fibonacci_03(n-1,cache)+fibonacci_03(n-2,cache)
        return cache[n]


@lru_cache(maxsize=1000)
def fibonacci_04(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci_04(n-1)+fibonacci_04(n-2)


cache={}
for n in range(1,1001):
    print(n," : ",fibonacci_04(n))