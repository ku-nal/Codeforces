import sys,operator,math,operator
from collections import Counter 


n,m,k=map(int,input().split())
li=[]
for i in range(m+1):
    no=int(input())
    li.append(no)
fi=li[-1]
ans=0
for i in range(m):
    temp=0
    f=fi
    for j in range(n):
        xor=f^li[i]
        if xor & 1:
            temp+=1
        f=f>>1
        li[i]=li[i]>>1
    if temp<=k:
        ans+=1
print(ans)

     
    