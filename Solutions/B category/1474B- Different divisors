def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True
 
for _ in range(int(input())):
    x=int(input())
    y=1+x
    while(isPrime(y)==False):
        y+=1
        
    z=y+x
    while(isPrime(z)==False):
        z+=1
        
    print(z*y)
