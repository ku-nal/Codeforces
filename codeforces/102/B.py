# import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')
s=input()
li=list(map(int,list(s)))
ans=0
while len(li)!=1:
    su=sum(li)
    st=str(su)
    li=list(map(int,list(st)))
    ans+=1
print(ans)
    
    