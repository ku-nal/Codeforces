from collections import Counter
omap={}
n=int(input())
if n==9000:
    print(9012)
else:
    for i in range(n+1,9013):
        st=str(i)
        omap=Counter(st)
        if len(omap)==4:
            print(int(st))
            break
    
    