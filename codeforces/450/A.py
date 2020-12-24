import math
n,m=map(int,input().split())
li=list(map(int,input().split()))
ma=0
ans=0
for i in range(n):
    if math.ceil(li[i]/m)>=ma:
        ma=math.ceil(li[i]/m)
        ans=i+1
print(ans)   
            