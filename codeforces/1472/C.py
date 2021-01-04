
test = int(input())
while(test):
    n=int(input())
    li=list(map(int,input().split()))
    dp=[0 for i in range(n)]
    for i in reversed(range(n)):
        if i+li[i]>=n:
            dp[i]=li[i]
        else:
            dp[i]=li[i]+dp[i+li[i]]
    print(max(dp))
    test-=1