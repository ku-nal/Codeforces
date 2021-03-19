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


#==============To chaliye shuru krte he ====================#
ar=[]
def p_s(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for i in ra(n+1):
        if prime[i]:
            ar.append(i)
pre=[0]*((10**7)+1)
def prime_factor(n):
    if pre[n]==0:
        i=0
        val=1
        t=n
        while ar[i]*ar[i]<=n and n>1:
            c=0
            while n%ar[i]==0:
                c+=1
                n/=ar[i]
            c=c%2
            val=int(val*(ar[i]**c))        
            i+=1
        if n>1:
            val*=int(n)
        pre[t]=val
        return val
    return pre[n]

tc=inpi()
while tc:
    n,k=inpm()
    li=inpl()
    p_s(10**4)
    arr=[]
    omap={}
    val=prime_factor(li[0])
    omap[val]=1
    arr.append(omap)
    c=1
    for i in ra(1,n):
        val=prime_factor(li[i])
        if val in arr[-1]:
            temp={}
            temp[val]=1
            c+=1
            arr.append(temp)
        else:
            arr[-1][val]=1
    P(l(arr))
    tc-=1
    
    