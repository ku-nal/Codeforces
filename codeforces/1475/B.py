
test=int(input())
while(test):
    n = int(input())
    x = n // 2020
    ans = x*2020
    a=0
    for i in range(2):
        a+=1
    while(x>0):
        if(ans != n):
            ans += 1
        else:
            break
        x-=1
    if(ans == n):
        print("YES")
    else:
        print("NO")

    test -= 1