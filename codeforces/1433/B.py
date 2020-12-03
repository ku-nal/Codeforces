
tc=int(input())
while tc:
    n=int(input())
    li=list(map(int,input().split()))
    ans=0
    i=0
    while i<len(li):
        if li[i]==0:
            i+=1
            continue
        j=i+1
        while j<len(li) and li[j]==1:
            j+=1
        k=j+1
        if k<len(li):
            while k<len(li) and li[k]==0:
                k+=1
            if k<len(li):
                ans+=k-j
        i=k
    print(ans)
    tc-=1