from collections import Counter
import operator
tc=int(input())
while tc:
    st=input()
    omap=Counter(st)
    oma={"R":"P","P":"S","S":"R"}
    for k,v in sorted(omap.items(),key=operator.itemgetter(1),reverse=True):
        s=k
        break
    ans=""
    for i in range(len(st)):
        ans+=oma[s]
    print(ans)
    tc-=1
    