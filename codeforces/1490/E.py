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

#=========I/p O/p =================
import sys,operator,math
from collections import Counter 



#==============To chaliye shuru krte he ====================#
tc=inpi()
while tc:
    n=inpi()
    li=inpl()
    li1=[]
    for i in ra(n):
        li1.append([li[i],i])
    li1.sort()
    pre=[0]*n
    pre[0]=li1[0][0]
    omap={}
    for i in range(1,n):
        if li[i-1]==li[i]:
            if li1[i][1] in omap:
                omap.append(li1[i-1][1])
            else:
                omap[li1[i][1]]=[li1[i-1][1]]   
        pre[i]+=pre[i-1]+li1[i][0]
    
    dp=[0]*n
    dp[-1]=1
    for i in reversed(ra(n-1)):
        if pre[i]>=li1[i+1][0]:
            dp[i]=dp[i+1]
    ans=[]
    c=0
    for i in ra(n):
        if dp[i]==1:
            c+=1
            ans.append(li1[i][1]+1)
    ans.sort()
    ans=set(ans)
    P(c)
    P(*ans)
    tc-=1

    
                
    