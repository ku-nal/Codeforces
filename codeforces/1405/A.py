tc=int(input())
while tc:
    tc-=1
    n=int(input())
    li=list(map(int,input().split()))
    print(*li[::-1])
    