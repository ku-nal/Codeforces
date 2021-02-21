tc=int(input())
while tc:
    n,m=map(int,input().split())
    if n%m==0:
        print("YES")
    else:
        print("NO")
    tc-=1