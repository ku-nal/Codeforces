
t=int(input())
while t:
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li1=li[:]
    li1.sort()
    j=-1
    for i in reversed(range(n)):
        if li[i]!=li1[i]:
            j=i
            break
    if j!=-1:
        
        ans=0
        for i in range(m):
            k,p=input().split()
            k=int(k)-1
            p=float(p)
            
            if k>=j:
                ans+=(1-ans)*p
        print(ans)
    else:
        for i in range(m):
            k,p=input().split()
        print(1.0)
    t-=1