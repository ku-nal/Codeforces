
st=input().split()
for i in st:
    if i.isupper():
        print(i.lower())
    elif i.islower() and len(i)==1:
        print(i[0].upper(),end="")
        print(i[1:].lower(),end="")
        print("",end=" ")
    elif i[0].islower() and i[1:].isupper():
        print(i[0].upper(),end="")
        print(i[1:].lower(),end="")
        print("",end=" ")
    else:
        print(i) 