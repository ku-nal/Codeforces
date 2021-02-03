
n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
i=1
s-=1
while True:
   
    tr=False
    if s-i>=0 or s+i<n:
        if s-i>=0 and s+i<n:
            if arr[s-i] and arr[s+i]:
                ans+=2
            tr=True
        elif s-i>=0:
            if arr[s-i]:
                ans+=1
            tr=True
        elif s+i<=n:
            if arr[s+i]:
                ans+=1
            tr=True
    if not tr:
        break
    i+=1
if arr[s]:
    print(ans+1)
else:
    print(ans)