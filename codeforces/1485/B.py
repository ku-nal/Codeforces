from collections import deque
import sys 


#==============To chaliye shuru krte he ====================#
n,q,k=map(int,input().split())
li=deque(map(int,input().split()))
if len(li)>1:
    pre=[0]*n
    pre[0]=li[1]-2
    for i in range(1,n-1):
        pre[i]=li[i+1]-li[i-1]-2
    pre[-1]=li[-2]-1
    for i in range(1,n):
        pre[i]+=pre[i-1]

for i in range(q):
    l,r=map(int,input().split())
    ans=0
    if l==r:
        ans+=li[l-1]-1+k-li[l-1]
    else:
        ans=pre[r-2]-pre[l-1]
        ans+=li[l]-2
        ans+=k-li[r-2]-1
        
    print(ans)
# for i in range(q):
#     a,b=map(int,input().split())
#     li1=deque()
#     ans=0
#     for i in range(a-1,b):
#          li1.append(li[i])
#     tr=False
#     if a==b:
#         ans+=li[a-1]-1
#         ans+=k-li[a-1]
#         tr=True
#     else:
#         ans+=li[a]-2
#     #P(ans)
#         for i in range(a,b-1):
#             ans+=li[i+1]-li[i-1]-2
#             #P(ans)
#         #print(li[b-2])
#         ans+=k-li[b-2]-1
        
#     print(ans)