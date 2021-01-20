for _ in range(int(input())):
    n=int(input())
    b=str(input())
    a=[0]*n
    a[0]=1+int(b[0])
    for i in range(1,n):
        if(b[i]=='0'):
            if(a[i-1]==1):
                a[i]=0
            else:
                a[i]=1
        else:
            if(a[i-1]==2):
                a[i]=1
            else:
                a[i]=2
    for i in range(n):
        a[i]=str(a[i]-int(b[i]))
    print("".join(a))
