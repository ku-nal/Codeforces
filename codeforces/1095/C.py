
n,k=map(int,input().split())
arr=[0]*32
for i in range(31):
    if n&(1<<i):
        arr[i]+=1
flag=True
if sum(arr)>k:
    print("NO")
    flag=False
if flag:
    i=31
    while sum(arr)<k and i>=0:
        if i>0 and arr[i]>0:
            arr[i-1]+=2
            arr[i]-=1
        elif arr[i]==0:
            i-=1
        else:
            i-=1
    if sum(arr)<k:
        print("NO")
    else:
        print("YES")
        for i in range(len(arr)):
            for j in range(arr[i]):
                print(2**i,end=" ")
                  
    