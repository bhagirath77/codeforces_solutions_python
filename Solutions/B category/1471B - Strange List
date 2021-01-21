for _ in range(int(input())):
    n,x=map(int ,input().split())
    a=list(map(int, input().split()))
    i=0
    z=sum(a)
    b=a[:]
    while(1):
        if(b[i%n]%x==0):
            y=b[i%n]//x
            b[i%n]=y
            z+=a[i%n]
            i+=1
        else:
            break
    print(z)
