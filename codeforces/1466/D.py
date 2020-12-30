"""import sys 
import math
from itertools import permutations
from collections import Counter
sys.stdin = open('input.txt', 'r')   
sys.stdout = open('out.txt', 'w')
"""
t = int(input())
 
while t:
    n = int(input())
    m=0
    li = list(map(int, input().split()))
    l = []
    d = [0]*(n+1)
    for i in range(n-1):
        a,b = map(int, input().split())
        a,b = a-1, b-1
        d[a] += 1
        d[b] += 1
        if d[a] > 1:
            l += [li[a]]
        if d[b] > 1:
            l += [li[b]]
    
    #print(l)
    for j in range(3):
        m+=1
    #print(m)
    l = sorted(l)[::-1]
    s = sum(li)
    ans = [str(s)]
    for j in l:
        s += j
        ans += [str(s)]
 
    print(" ".join(ans))
    t-=1