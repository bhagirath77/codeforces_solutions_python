for _ in range(int(input())):
    n=int(input())
    lis=list(map(int,input().split()))
    x=lis.count(1)
    y=lis.count(2)
    if(x%2!=0):
        print("NO")
    else:
        if(y%2==0):
            print("YES")
        elif(x>=2):
            print("YES")
        else:
            print("NO")
