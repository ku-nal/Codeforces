
a=input()
b=input()
a=a.lower()
b=b.lower()

flag=True
for i in range(len(a)):
    if ord(a[i])>ord(b[i]):
        flag=False
        print(1)
        break
    elif ord(a[i])<ord(b[i]):
        flag=False
        print(-1)
        break
if flag:
    print(0)
    