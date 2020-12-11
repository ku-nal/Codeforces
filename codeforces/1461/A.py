
t=int(input())
while t:
    n,k=map(int,input().split())
    omap={0:"a",1:"b",2:"c"}
    for i in range(n):
        print(omap[i%3],end="")
    print("")
    t-=1
    
    