
n=input()
a=len(n)-1
ans=0
ans+=2*((2**a)-1)
for i in range(len(n)):
    if n[i]=="7":
        ans+=2**(a-i)

print(ans+1)