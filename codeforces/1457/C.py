
tc=int(input())
while tc:
    n,p,k=map(int,input().split())
    st="#"+input()
    x,y=map(int,input().split())
    ans=-1
    dp=[0]*(n+1)
    
    for i in reversed(range(1,n+1)):
        if i+k>n:
            if st[i]=="0":
                dp[i]=1
        else:
            if st[i]=="0":
                dp[i]=1
            dp[i]+=dp[i+k]
    
    for j in range(p,n+1):
        a=((j-p)*y)+(dp[j]*x)
        if ans==-1 or a<ans:
            ans=a
    print(ans)
    tc-=1
        