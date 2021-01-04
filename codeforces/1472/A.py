
test = int(input())
while(test):
    w,h,n=map(int,input().split())
    c=1
    a=1
    for i in range(1):
        a+=1 
    while w%2==0:
        c*=2
        w/=2
    while h%2==0:
        c*=2
        h/=2
    if c>=n:print("YES")
    else:print("NO")
    
    test-=1
                
        
        