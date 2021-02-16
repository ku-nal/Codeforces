
import sys,operator,math
from collections import Counter 



#==============To chaliye shuru krte he ====================#
def cuber(cb,rem):
    while cb*cb*cb<rem:
        cb+=1
    while cb*cb*cb>rem:
        cb-=1
    if cb*cb*cb==rem:
        return True
    return False
tc=int(input())
while tc:
    n=int(input())
    N=(10**4)+1
    tr=False
    for i in range(1,N):
        rem=n-(i**3)
        if rem>0:
            cbrem=int(rem**(1/3))
            if cuber(cbrem,rem):
                tr=True
                break
        else:break
    if tr:print("YES")
    else:print("NO")
    tc-=1
    
    # no=n//2
    # lim=int(n**(1/3))
    # id1=int(no**(1/3))
    # P(id1,lim)
    # tr=False
    # for i in reversed(ra(1,id1+1)):
    #     for j in ra(id1,lim+1):
    #         if i**3+j**3==n:
    #             tr=True
    #             break
    # if tr:P("YES")
    # else:P("NO")
    # tc-=1    