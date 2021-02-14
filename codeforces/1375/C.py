tc=int(input())
while tc:
    n=int(input())
    li=list(map(int,input().split()))
    if li[0]<li[-1]:
        print("Yes")
    else:
        print("No")
    tc-=1