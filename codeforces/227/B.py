
n=int(input())
li=list(map(int,input().split()))
m=int(input())
v,p=0,0
omap={}
q=list(map(int,input().split()))
for i in range(n):
    if li[i] not in omap:
        omap[li[i]]=[i]
    else:
        omap[li[i]].append(i)
for j in range(m):
    v+=omap[q[j]][0]+1
    p+=n-omap[q[j]][-1]
print(v,p)
            
    
    