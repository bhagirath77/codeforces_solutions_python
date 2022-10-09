for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    if k == 1: print("Yes"); continue
    l = s[0]
    f,pre = 0, s[1]-s[0]
    if pre*(n-k+1) < s[0]: print("No"); continue
    for i in range(len(s)-1):
        val = s[i+1]-s[i]
        if val < pre:
            f = -1
            break
        pre = val
    
    if f == -1: print("No")
    else : print("Yes")