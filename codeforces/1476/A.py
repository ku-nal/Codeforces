import math
test = int(input())
while test:
    n,k=map(int,input().split())

    if k==1:
        print(1)
    else:
        temp=k
        c=int(math.ceil(n/k))
        
        k=c*k
        
        a=k//n
        b=k-(a*n)
        print(a+int(math.ceil(b/n)))
    test-=1
