import math
from collections import Counter 
for _ in range(int(input())):
    n=int(input())
    lis=list(map(int ,input().split()))
    lis=sorted([int(math.log(i,2)) for i in lis])
    x=Counter(lis)
    y=0
    
    for num in x:
        z=x[num]
        y+=(z*(z-1))//2
        
    print(y)
