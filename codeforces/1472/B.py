
test = int(input())
while(test):
    n=int(input())
    li=list(map(int,input().split()))
    o=li.count(1)
    t=li.count(2)
    
    if o%2==0 and t%2==0:
        print("YES")
    elif t%2==1:
        o-=2
        if o>=0 and o%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    test-=1