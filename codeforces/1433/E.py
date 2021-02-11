from itertools import combinations
import math
n=int(input())
li=[]
for i in range(1,n+1):
    li.append(i)
comb=combinations(li,int(n/2))
li=list(comb)
a=math.factorial((n/2)-1)
print(int((len(li)/2)*a*a))