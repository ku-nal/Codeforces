
n,t=map(int,input().split())
st=list(input())
for i in range(t):
    j=1
    while j<len(st):
        if st[j]=="G" and st[j-1]=="B":
            st[j-1]=st[j]
            st[j]="B"
            j+=2
        else:
            j+=1
print(''.join(st))
