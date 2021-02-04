# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
n=int(input())
c=0
a=list(map(int,input().split()))
ans=a[0]
i=0
while i<n-1:
    if a[i]>=a[i+1]:
        c+=a[i]-a[i+1]
    else:
        if c>=(abs(a[i]-a[i+1])):
            c-=(abs(a[i]-a[i+1]))
        else:
            ans+=abs(c+a[i]-a[i+1])
            c=0
    i+=1
print(ans)

