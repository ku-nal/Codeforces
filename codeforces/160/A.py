n=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
su=sum(li)
ans=0
temp=0
for i in range(n):
    ans+=1
    temp+=li[i]
    if temp>su-temp:
        break
print(ans)