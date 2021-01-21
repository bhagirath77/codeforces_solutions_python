for _ in range(int(input())):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    z=0
    y=0
    x=0
    for i in range(n):
        y+=r[i]
        if(y>x):
            x=y
    y=x
    x=0
    for i in range(m):
        z+=b[i]
        if(z>x):
            x=z
    print(x+y)
