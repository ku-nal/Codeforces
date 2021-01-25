
test = int(input())
while(test):
    n=int(input())
    if n%2==0:
        while n%2==0:
            n/=2
        if n>1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    test-=1