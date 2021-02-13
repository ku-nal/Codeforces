test=int(input())
while test:
    a,b,c,d=map(int,input().split())
    if a==0 and d==0:
        if b%2==0:
            print("Tidak Tidak Ya Tidak")
        else:
            print("Tidak Ya Tidak Tidak")
    elif b==0 and c==0:
        if a%2==0:
            print("Tidak Tidak Tidak Ya")
        else:
            print("Ya Tidak Tidak Tidak")
    elif (a+b)%2==0:
        print("Tidak Tidak Ya Ya")
    else:
        print("Ya Ya Tidak Tidak")
    test-=1