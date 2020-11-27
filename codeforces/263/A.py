
mat1=[]
mat1.append(input().split())
mat1.append(input().split())
mat1.append(input().split())
mat1.append(input().split())
mat1.append(input().split())
for i in range(len(mat1)):
    if "1" in mat1[i]:
        row=i
        for j in range(len(mat1[i])):
            if mat1[i][j]=="1":
                col=j
                break

ans=abs(2-row)+abs(2-col)
print(ans)
