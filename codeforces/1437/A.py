n=int(input())
for i in range(n):
    l,r=map(int,input().split())
    upp=2*l
    if r<upp:
        print("YES")
    else:
        print("NO")