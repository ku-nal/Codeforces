
from collections import Counter
import operator
st=input()
k=int(input())
omap=Counter(st)
a=sorted(omap.items(),key=operator.itemgetter(1))
i=0
while k>0 and i<len(a):
    if a[i][1]<=k:
        k-=a[i][1]
        del omap[a[i][0]]
    else:
        omap[a[i][0]]-=k
        k=0
    i+=1
print(len(omap))
ans=""
for i in st:
    if i in omap:
        ans+=i
        omap[i]-=1
        if omap[i]==0:
            del omap[i]
            
#print(len(omap))
print(ans)


    
    