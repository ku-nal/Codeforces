
from collections import Counter
tc=int(input())
while tc:
    n=input()
    b=list(map(int,input().split()))
    flag=True
    a=Counter(b)
    for i,j in a.items():
        if j>=2:
            flag=False
            print("YES")
            break
    if flag:
        print("NO")
    tc-=1
    