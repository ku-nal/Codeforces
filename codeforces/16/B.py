n,m=map(int,input().split())
li=[]
for i in range(m):
    li.append(list(map(int,input().split())))
li.sort(reverse=True,key=lambda x:x[1])
i=0
ans=0
while i<m and n>0:
   
    if n>=li[i][0]:
        ans+=li[i][0]*li[i][1]
        n-=li[i][0]
    else:
        ans+=n*li[i][1]
        break
    
    i+=1
print(ans)