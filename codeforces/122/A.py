n=int(input())
temp=n
def islucky(temp):
    tr=True
    while temp>0:
        a=temp%10
        if a!=4 and a!=7:
            tr=False
            break
        temp=temp//10
    return tr
tr=False
for i in range(1,n+1):
    if islucky(i):
        if n%i==0:
            tr=True
            break
if tr:
    print("YES")
else:print("NO")