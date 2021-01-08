
test = int(input())
while(test):
    n=int(input())
    print(9,end="")
    n-=1
    a=8
    while n:
        if a==10:a=0
        print(a,end="")
        a+=1
        n-=1
    print()
    test-=1
    