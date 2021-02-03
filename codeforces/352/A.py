# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
n=int(input())
li=list(map(int,input().split()))
su=sum(li)

tr=True
c=li.count(5)
while su>0:
    t=su
    s=0
    while t>0:
        s+=t%10
        t=t//10
    if s%9==0 and 0 in li:
        print("5"*c+"0"*li.count(0))
        tr=False
        break
    su-=5 
    c-=1
if tr and 0 in li:
    print(0)
elif tr:
    print(-1)   
    