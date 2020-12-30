import sys 
import math


te=int(input())
while te:
    n=int(input())
    li=list(map(int,input().split()))
    om=[]
    for i in range(n):
        for j in range(i+1,n):
            fi=math.sqrt((li[i]**2)+1)
            se=math.sqrt((li[j]-li[i])**2)
            th=math.sqrt(li[j]**2+1)
            p=(fi+se+th)/2
            area=math.sqrt(p*(p-fi)*(p-se)*(p-th))
            area=round(area,2)
            """st=str(area)
            t=st.split(".")
            t1=[t[0],t[1][:2]]
            fi='.'.join(t1)"""
            if len(om)==0:
                om.append(area)
            elif area not in om:
                om.append(area)
    print(len(om))
    te-=1
            
    