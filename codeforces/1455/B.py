
tc=int(input())
while tc:
    a=int(input())
    su=0
    i=1
    while su<a:
        su+=i
        i+=1
    if su-a==1:
        print(i)
    else:
        print(i-1)
    tc-=1