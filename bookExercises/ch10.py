from __future__ import print_function

def vertical(num):
    if num<10:
        print(num)
    else:
        vertical(num/10)
        print(num%10)

def pattern(n):
    if n == 0:
        print(n, end="")
    else:
        pattern(n-1)
        print(n, end="")
        pattern(n-1)

def pattern2(n):
    if n == 0:
        pass
    else:
        pattern2(n-1)
        print('*'*n)
        pattern2(n-1)

def recNeg(lst):
    if lst[0]<0:
        return True
    else:
        if (len(lst)==1):
            return False
        else:
            return recNeg(lst[1:])

def rpower(a,n):
    'a to the nth power, performed recursively'

    global counter
    
    if n==0:
        return 1

    tmp = rpower(a,n/2)

    if n%2==0:
        counter += 1
        return tmp*tmp
    else:
        counter += 2
        return a*tmp*tmp

def power(a,n):
    'a to the nth power'

    global counter

    res = 1
    for i in range(n):
        counter += 1
        res *= a

    return res

import random
def buildInput(n):
    'list of n random integers in range [0,n**2]'
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res

def dup1(lst):
    'regular linear search'
    for item in lst:
        if lst.count(item)>1:
            return True
    return False

def dup2(lst):
    'only one pass but must be sorted'
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i]==lst[i-1]:
            return True
    return False
    
def dup3(lst):
    'linear comparison to new set - no gain'
    s = set()
    for item in lst:
        if item in s:
            return True
        else:
            s.add(item)
    return False

def dup4(lst):
    'compare lst to set version of list - speed depends on set() constructor'
    return len(lst) != len(set(lst))

import time
def test_dup(n):
    lst = buildInput(n)

    print("Starting test of dup1")
    start = time.time()
    print(dup1(lst),end=" ")
    print(time.time()-start, end="\n\n")

    print("Starting test of dup2")
    start = time.time()
    print(dup2(lst),end=" ")
    print(time.time()-start, end="\n\n")

    print("Starting test of dup3")
    start = time.time()
    print(dup3(lst),end=" ")
    print(time.time()-start, end="\n\n")

    print("Starting test of dup4")
    start = time.time()
    print(dup4(lst),end=" ")
    print(time.time()-start, end="\n\n")
    
    
#def timing(
