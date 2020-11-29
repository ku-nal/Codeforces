from collections import Counter
t=int(input())
while t:
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    a=Counter(lis)
    ans=float('inf')
    for i in a.keys():
        j=0
        tempe=0
        while j<len(lis):
            if lis[j]!=i:
                tempe+=1
                j+=k
            else:
                j+=1
       
        ans=min(ans,tempe) 
    print(ans)
    t-=1 
                
                     
                
                    