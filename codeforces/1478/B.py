
test = int(input())
while(test):
    n,d=map(int,input().split())
    li=list(map(int,input().split()))
    for i in li:
        t=i
        flag=True
        tr=False
        while t>=d:
            if t%d==0 or (tr and t%10==0) or (str(d) in str(t)):
                print("YES")
                flag=False
                break
            t-=d
            tr=True
        if flag:
            print("NO")
    test-=1