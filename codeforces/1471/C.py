 
test = int(input())
while(test):
    n,o=map(int,input().split())
    li=list(map(int,input().split()))
    li1=list(map(int,input().split()))
    li.sort(reverse=True)
    c,ans=0,0
    for i in li:
        if li1[c]<li1[i-1]:
            
            ans+=li1[c]
            c+=1
        else:
            ans+=li1[i-1]
    print(ans)
    test-=1
    