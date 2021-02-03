# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
n=int(input())
arr=list(map(int,input().split()))
id1,id2,ma,mi=0,0,arr[0],arr[0]

for i in range(1,n):
    if arr[i]>ma:
        ma=arr[i]
        id1=i
    elif arr[i]<=mi:
        mi=arr[i]
        id2=i

if id1<id2:
    print(id1+(n-id2)-1)
else:
    print(id1+(n-id2)-2)
    