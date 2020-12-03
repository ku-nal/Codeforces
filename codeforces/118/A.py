
st=input()
ans=""
for i in st:
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u" or i.lower()=="y":
        continue
    else:
        ans+="."+i.lower()
print(ans)