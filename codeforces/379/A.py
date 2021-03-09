n,m=map(int,input().split())
ans=n
while (n/m)>=1:
    ans+=n//m
    n=n//m+(n%m)
print(ans)
    