#===========Template===============
from io import BytesIO, IOBase
import sys,os
inpl=lambda:list(map(int,input().split()))
inpm=lambda:map(int,input().split())
inpi=lambda:int(input())
inp=lambda:input()
rev,ra,l=reversed,range,len
P=print
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")

#=========I/p O/p ========================================#
from bisect import bisect_left as bl 
from bisect import bisect_right as br
import sys,operator,math,operator
from collections import Counter 

import random
#==============To chaliye shuru krte he ====================#
tc=inpi()
while tc:
    tc-=1
    n,m=inpm()
    omap={}
    
    li=[]
    upp=int(math.ceil(m/2))
    ans=[0]*m
    for i in ra(m):
        temp=inpl()
        temp.append(i)
        li.append(temp)
        for j in li[-1][1:-1]:
            if j not in omap:
                omap[j]=1
            else:omap[j]+=1
    li.sort()
    tr=False
    di=omap.copy()
    for i in ra(m):
        mi=float('inf')
        temp=0
        for j in ra(1,l(li[i])-1):
            if di[li[i][j]]-omap[li[i][j]]<mi and omap[li[i][j]]>0:
                mi=di[li[i][j]]-omap[li[i][j]]
                temp=li[i][j]
        omap[temp]-=1
        if omap[temp]<0:
            tr=True
            break
        c=di[temp]-omap[temp]
        if c>upp:
            tr=True
            break
        ans[li[i][-1]]=temp
    if not tr:
        P("YES")
        P(*ans)
    else:P("NO")
