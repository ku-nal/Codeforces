
tc=int(input())
while tc:
    n,m=map(int,input().split())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    ans=0
    for i in li1:
        if i in li2:
            ans+=1
    print(ans)
    tc-=1
    