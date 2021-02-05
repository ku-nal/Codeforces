# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
test=int(input())
while test:
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    pos=0
    pt=0
    while k>0 and pt<n-1:
        if li[pt]>=li[pt+1]:
            pt+=1
        else:
            pos=pt+1
            li[pt]+=1
            if pt==0:
                pt=0
            else:
                pt-=1
            k-=1
    if pt>=n-1:
        print(-1)
    else:
        print(pos)
    test-=1
    
            
            
            
            