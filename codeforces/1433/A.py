
tc=int(input())
while tc:
    st=input()
    li=[]
    for i in range(1,10):
        if i==int(st):
            li.append(str(i))
            break
        j=i
        while j<=10000:
            if j==int(st):
                li.append(str(j))
                break
            li.append(str(j))
            j=j*10+i
        if j==int(st):
            break
    ans=0     
    for i in li:
        ans+=len(i)
    print(ans)
    tc-=1