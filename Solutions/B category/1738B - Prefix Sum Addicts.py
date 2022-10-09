from re import L
import sys
import math
from collections import defaultdict, deque,Counter
import random
from functools import lru_cache
 
 
 
# Multi 
 
out  = lambda x,end='\n' : sys.stdout.write(str(x)+end)
SI   = lambda: sys.stdin.readline().rstrip("\r\n")
MI   = lambda: map(int,SI().split())
II   = lambda: int(SI())
LI   = lambda: list(MI())
lcm  = lambda x,y:abs(x * y) // math.gcd(x,y)
FCT  = lambda x:eval('*'.join([str(i) for i in range(1,x+1)])) if x>1 else 1
INF  = float("inf")
 
 
def binary_search(n,arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] > n:
            end = mid - 1
        elif arr[mid] <n:
            start = mid + 1
        else :
            return mid
    return mid
 
 
def isPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True
 
 
 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
 
for _ in range(II()):
    n,k = MI()
    s = LI()
    cur = s[0]/(n-k+1)
    a = 1
    
    for i in range(1,k):
        if s[i] - s[i-1] < cur:
            a = 0 
            break
        cur = s[i] - s[i-1]
    print(['NO','YES'][a])
