test = int(input())
while(test):
    n,x=map(int,input().split())
    li=list(map(int,input().split()))
    su=sum(li)
    a=li[:]
    i=0
    while li[i]%x==0:
        li[i]=li[i]/x
        su+=a[i]
        i=(i+1)%n
    print(su)    
    test-=1