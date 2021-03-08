s,n=map(int,input().split())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
li.sort()
tr=True
for i in range(n):
    if li[i][0]>=s:
        tr=False
        break
    else:s+=li[i][1]
if tr:print("YES")
else:print("NO")