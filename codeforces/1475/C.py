test = int(input())
while(test):
    a,b,k=map(int,input().split())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    posa=[0 for i in range(a+1)]
    posb=[0 for i in range(b+1)]
    for i in li1:
        posa[i]+=1
    for i in li2:
        posb[i]+=1
    ans=0
    for i in range(k):
        ans+=k-posa[li1[i]]-posb[li2[i]]+1
    print(ans//2)
    test-=1