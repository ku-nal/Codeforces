tc=int(input())
while tc:
    tc-=1
    n=int(input())
    ans=0
    stair,x=1,0
    while n-x>0:
        x=int((stair*(stair+1))/2)
        n-=x
        if n>=0:
            ans+=1
            stair=(2*stair)+1
        else:
            break
    print(ans)

        
        