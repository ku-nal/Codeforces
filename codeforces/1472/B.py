
t = int(input())
while(t):
    n= int(input())
    li = list(map(int,input().split()))
    c2 = li.count(2)
    c1 = li.count(1)
    a=0
    for i in range(2):
        a+=1
    #print(a)
    if(c1%2==1):
        print("NO")
    elif(c2%2==0 and c1%2==0):
        print("YES")
    elif(c2%2==1 and (c1%2==0 and c1-2>=0)):
        print("YES")
    elif(c2%2==1 and (c1%2==1 or c1-2<0)):
        print("NO")
    
    t -= 1