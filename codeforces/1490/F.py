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
import sys,operator,math,bisect
from collections import Counter 


#==============To chaliye shuru krte he ====================#
tc=inpi()
while tc:
    n=inpi()
    li=inpl()
    omap=Counter(li)
    li1=[]
    for k,v in sorted(omap.items(),key=operator.itemgetter(1)):
        li1.append(v)
    pre=[0]*l(li1)
    pre[0]=li1[0]
    for i in ra(1,l(li1)):
        pre[i]+=pre[i-1]+li1[i]
    ans=float('inf')
    for i in (li1):
        temp=0
        low=bisect.bisect_left(li1,i)
        high=bisect.bisect_right(li1,i)
        if low<=0:
            pass
        else:
            temp+=pre[low-1]
        if high>=len(li1):
            pass
        else:
            temp+=pre[-1]-pre[high-1]-(len(li1)-high)*i
        ans=min(ans,temp)
    P(ans)
    tc-=1

    
                
    