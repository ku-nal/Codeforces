
te=int(input())
while te:
    li=list(input())
    si=len(li)
    ans=0
    for i in range(si):
        if li[i]!="#":
            if i+1<si and li[i]==li[i+1]:
                li[i+1]="#"
                ans+=1
            if i+2<si and li[i]==li[i+2]:
                li[i+2]="#"
                ans+=1
    print(ans)
            
    
        
        
    te-=1