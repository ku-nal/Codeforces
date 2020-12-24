
n=int(input())
li=list(map(int,input().split()))
su=sum(li)
ans=0
for i in range(1,6):
    if (su+i)%(n+1)==1:
        ans+=1
print(5-ans)
            
    
    