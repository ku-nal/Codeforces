n = int(input())
li = []
for i in range(n):
    a, b = list(map(int, input().split()))
    li.append([a, 1])
    li.append([b, 0])
li.sort()
c = 0
m = 0
y = 0
l = len(li)
for i in range(l):
    if li[i][1] == 1:
        c += 1
    else:
        c -= 1
    if m < c:
        m = c
        y = li[i][0]
print(y, m)