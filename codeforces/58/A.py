st=input()
arr=['h','e','l','l','o']
i,l=0,0

while l<5 and i<len(st):
    if st[i]==arr[l]:
        l+=1
    i+=1
if l>4:
    print("YES")
else:
    print("NO")
