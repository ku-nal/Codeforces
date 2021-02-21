t=int(input())
while t:
    n,k=map(int,input().split())
    li=[]
    for i in range(n):
        c,d=map(int,input().split())
        li.append([c,d])
    omap={}
    flag1=True
    for i in range(len(li)):
        for j in range(len(li)):
            if i==j:
                continue
            if abs(li[i][0]-li[j][0])+abs(li[i][1]-li[j][1])<=k:
                if i not in omap:
                    omap[i]=1
                else:
                    omap[i]+=1
        if i in omap and omap[i]==n-1:
            flag1=False
            print(1)
            break
    if flag1:           
        flag2=True
        for i,j in omap.items():
            if j==n-1:
                print(1)
                flag2=False
                break
        if flag2:
            print(-1)
    t-=1