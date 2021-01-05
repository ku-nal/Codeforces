
import math

test = int(input())
while(test):
    n,x=map(int,input().split())
    li=list(map(int,input().split()))
    ma=0
    for i in range(n):
        ma+=int(math.ceil(li[i]/x))
    print(int(math.ceil(sum(li)/x)),ma)
    test-=1