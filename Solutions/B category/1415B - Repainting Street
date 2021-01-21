for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=99999
    for i in range(1,max(a)+1):
        j,t=0,0
        while j<n:
            if a[j]==i:
                j+=1
            else:
                t+=1
                j+=k
        ans=min(ans,t)
    print(ans)
