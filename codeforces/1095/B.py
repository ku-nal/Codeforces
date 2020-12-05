
from collections import Counter

n=int(input())
li=list(map(int,input().split()))
ma=max(li)
mi=min(li)
li1=Counter(li)
smi=float('inf')
sma=float('-inf')


for i in li:     
    if i>mi and i<smi:
        smi=i
    if i<ma and i>sma:
        sma=i 
if li1[mi]>1:
    smi=mi
if li1[ma]>1:
    sma=ma
print(min(abs(ma-smi),abs(sma-mi)))
 