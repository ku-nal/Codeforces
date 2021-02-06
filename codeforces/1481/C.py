from collections import Counter
import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
def input(): return sys.stdin.readline().rstrip("\r\n")
test=int(input())
while test:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    omap={}
    posi={}
    posb={}
    omap2=Counter(b)
    tr=True
    omap3=Counter(c)
    for i in range(n):
        if a[i]!=b[i]:
            if b[i] in omap:
                omap[b[i]]+=1
            else:
                omap[b[i]]=1
            if b[i] in posi:
                posi[b[i]].append(i)
            else:
                posi[b[i]]=[i]
        if b[i] in posb:
            posb[b[i]].append(i)
        else:
            posb[b[i]]=[i]
    
    for k,v in omap.items():
        if k in omap3:
            if omap[k]>omap3[k]:
                tr=False
                break
        else:
            tr=False
            break
    if tr:
        li=[]
        tr1=True
        for i in range(m):
            if c[i] in posi:
                li.append(posi[c[i]].pop(0))
                if len(posi[c[i]])==0:
                    del posi[c[i]]
            elif c[i] in posb:
                li.append(posb[c[i]][0])
            elif len(posi)>0:
                for k,v in posi.items():
                    li.append(v[0])
                    break
            elif i!=m-1:
                if c[m-1] in posb:
                    li.append(posb[c[m-1]][0])
            else:
                tr1=False
                break
        if tr1:
            print("Yes")
            for i in li:
                print(i+1,end=" ")
            print()

        else:
            print("No")
    else:
        print("No")
    test-=1
        
            
                    
            