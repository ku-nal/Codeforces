
tc=int(input())
while tc:
    n,x=map(int,input().split())
    li=list(map(int,input().split()))
    pre=[li[0]]
    m=0
    def not_sorted(li):
        for i in range(1,n):
            if li[i]<li[i-1]:
                return 1
        return 0
    m=0
    flag=True
    while(not_sorted(li)):
        m+=1
        i=0
        while i<n and li[i]<=x:
            i+=1
        if i==n:
            flag=False
            break
        li[i],x=x,li[i]
    if flag:
        print(m)
    else:
        print(-1)
    tc-=1