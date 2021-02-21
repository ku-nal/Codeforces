tc=int(input())
while tc:
    a,b,c=map(int,input().split())
    tot=a+b+c
    if tot%9!=0:
        print("NO")
    else:
        r=tot//9
        if a>=r and b>=r and c>=r:
            print("YES")
        else:
            print("NO")
    tc-=1
