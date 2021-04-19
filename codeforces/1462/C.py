t=int(input())
while t:
    x=int(input())
    dp=[0]*(x+1)
    if x>9 and x<=45:
        for i in range(1,10):
            dp[i]=i
        for i in range(10,x+1):
            mi=float('inf')
            l=float('inf')
            j=1
            while  j<=i-j:
                st=str(dp[j])+str(dp[i-j])
                if len(st)<=l:
                    l=len(st)
                    s=set(st)
                    if len(st)==len(s):
                        li=list(st)
                        li.sort()
                        a=int(''.join(li))
                        if a<mi:
                            mi=a
                j+=1
            if mi!=float('inf'):
                dp[i]=mi
            else:
                dp[i]=-1
                break
        print(dp[-1])
            
    else:
        if x>45:
            print(-1)
        else:
            print(x)
    t-=1
    