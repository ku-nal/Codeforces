
st=input()
i=0
ans=""
while i<len(st):
    if st[i]==".":
        i+=1
        ans+="0"
    elif st[i:i+2]=="-.":
        ans+="1"
        i+=2
    else:
        ans+="2"
        i+=2
print(ans)