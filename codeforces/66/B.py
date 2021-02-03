# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
n=int(input())
arr=list(map(int,input().split()))
ans=float('-inf')
for i in range(n):
    l,r=i,i
    c=0
    idx=0
    while l>0 and arr[l]>=arr[l-1]:
        c+=1
        l-=1
    while r<n-1 and arr[r]>=arr[r+1]:
        c+=1
        r+=1
    if c>ans:
        ans=c
        idx=i
print(ans+1)
    