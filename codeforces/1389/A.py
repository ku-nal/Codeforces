tc=int(input())
while tc:
    x,y=map(int,input().split())
    a=x
    if 2*a<=y:
        print(a,2*a)
    else:
        print(-1,-1)
    tc-=1