import math
test = int(input())
while test:
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    pref=[]
    k=k/100
    su=0
    for i in range(n):
        su+=li[i]
        pref.append(su)
    temp=0
    for i in range(1,n):
        if (li[i]/(pref[i-1]+temp))>k:
            a=math.ceil(round((li[i]-(k*(temp+pref[i-1])))/k,4))
            temp+=a
    print(temp)
    test-=1