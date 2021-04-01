tc=int(input())
while tc:
    tc-=1
    n=int(input())
    n=180-n
    if 360%n==0:
        print("YES")
    else:
        print("NO")
        