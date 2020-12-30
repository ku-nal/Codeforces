
from collections import Counter

te=int(input())
while te:
    n=int(input())
    li=list(map(int,input().split()))
    om={li[0]:0}
    for i in range(1,n):
        if li[i] in om:
            li[i]+=1
            if li[i] not in om:
                om[li[i]]=0
        else:
            om[li[i]]=0
                
    omap=Counter(li)
    print(len(omap))
    
        
        
    te-=1
            
    