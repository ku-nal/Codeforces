
n=int(input())
for i in range(n):
    for j in range(i,n):
        if j==n-1:
            print(" ",end="")
        else:
            print(" ",end=" ")
    for k in range(i+1):
        print(" "+str(k),end="")
    for o in reversed(range(i)):
        print(" "+str(o),end="")
    print("")
for i in range(n+1):
    if i==0:
        print(i,end="")
    else:
        print(" "+str(i),end="")
for i in reversed(range(n)):
    print(" "+str(i),end="")
print("")
for t in reversed(range(n)):
    for i in range(t,n):
        if i==n-1:
            print(" ",end="")
        else:
            print(" ",end=" ")
    for k in range(t+1):
        print(" "+str(k),end="")
    for o in reversed(range(t)):
        print(" "+str(o),end="")
    print("")
                    