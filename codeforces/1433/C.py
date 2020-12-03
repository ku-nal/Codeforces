from collections import Counter

tc=int(input())
while tc:
    n=int(input())
    li=list(map(int,input().split()))
    a=Counter(li)
    flag=True
    if len(a)==1:
        print(-1)
        flag=False
    if flag:            
        ma=max(li)
        for i in range(n):
            if li[i]==ma  and ((i+1 < n and(li[i+1]<li[i])) or (i-1>=0 and li[i]>li[i-1])):
                print(i+1)
                break
    tc-=1