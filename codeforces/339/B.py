n,m=map(int,input().split())
li=list(map(int,input().split()))
curr=1
ans=0
for i in range(m):
    if li[i]>=curr:
        ans+=li[i]-curr
    else:
        ans+=n-curr+li[i]
    curr=li[i]
print(ans)