
n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort(reverse=True)
j=0
for i in range(len(a)):
    if a[i]==0:
        a[i]=b[j]
        j+=1
flag=True
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        flag=False
        print("YES")
        break
if flag:
    print("NO")