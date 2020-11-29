
tc=int(input())
while tc:
    n,m,r,c=map(int,input().split())
    print(max(abs(r-1+c-1),abs(n-r+m-c),abs(r-1+m-c),abs(n-r+c-1)))
    tc-=1