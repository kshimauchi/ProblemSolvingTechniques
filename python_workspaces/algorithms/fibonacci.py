# fibonacci Series
# Definition:
# Growth of Pine Cones, Sunflowers, Rabbit proliferation
# Lots of Example in nature follow this pattern
# f(0)= and f(1)=1
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    if n < 0:
        print("This example is for whole numbers!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#print(fibonacci(9))

# Fibonacci Sequence using array for base conditions
Fib =[0.,1]
@lru_cache(maxsize = 1000)
def fibonacci_arry(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("a must be a positive int")
    if n < 0:
        print("Wrong input detected!")
    elif n <= len(Fib):
        return Fib[n-1]
    else:
        temp = fibonacci_arry(n-1)+fibonacci_arry(n-2)
        Fib.append(temp)
        return temp
# print(fibonacci_arry(9))
# Fibonacci Series simply doesn't work well in this manner
@lru_cache(maxsize = 1000)
def fibonacci2(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("a must be a positive int")
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return fibonacci2(n-1) + fibonacci2(n-2)
#for n in range(1, 101):
    #print(n, ":", fibonacci2(n))
# Fibonacci Series
fibonacci_cache ={}
@lru_cache(maxsize = 1000)
def fibonacci3(n):
    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    #Compute the nth term
    if n == 1:
        value = 1
    elif n ==2:
        value = 1
    elif n > 2:
        value = fibonacci3(n-1)+ fibonacci3(n-2)
    #Cache the value and return it
    fibonacci_cache[n] = value
    return value
for i in range(1, 1001):
    print(i, ":", fibonacci3(i))








