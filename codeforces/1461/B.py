
t=int(input())
while t:
    n,m=map(int,input().split())
    li=[]
    for i in range(n):
        li.append(list(input()))
    
    dp=[[0 for i in range(m)] for j in range(n)]
    
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if li[i][j]=="*":
                if i+1<n and j-1>=0 and j+1<m:
                    dp[i][j]=1+min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
                else:
                    dp[i][j]=1
    ans=0        
    for i in range(n):
        for j in range(m):
            ans+=dp[i][j]
    print(ans)
    t-=1
    