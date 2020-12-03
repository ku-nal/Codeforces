import sys 
import math


n,m,a,b=map(int,input().split())

if b/m>a:
    print(a*n)
else:
    ans=min(math.ceil(n/m)*b,(math.floor(n/m)*b)+(a*(n%m)))
    print(ans)
