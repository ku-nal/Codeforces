
n,m= map(int,input().split())
if (m%n !=0):
	print(-1)
else:
	di = m/n
	count =0
	while(di%2 ==0):
		count +=1
		di /= 2
	while( di%3 ==0):
		count +=1
		di /= 3
	if( di !=1):
		print(-1)
	else:
		print(count)





"""
a,b=map(int,input().split())
flag=True
if b%a!=0:
    print(-1)
elif b==a:
    print(0)
else:
    ans=-1
    def helper(a,b,count):
        global ans
        if a>b:
            return 
        if a==b:
            ans=count
            return count
        q=helper(a*2,b,count+1)
        if q:
            return q
        y=helper(a*3,b,count+1)
        if y:
            return y
        
    ap=helper(a,b,0)
    if ap:
        print(ap)
    else:
        print(-1)      
"""