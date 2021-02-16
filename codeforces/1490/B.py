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
    c0,c1,c2=0,0,0
    for i in ra(n):
        if li[i]%3==0:
            c0+=1
        elif li[i]%3==1:
            c1+=1
        else:
            c2+=1
    avg=(c0+c1+c2)/3
    ans=0
    if c0>avg:
        ans+=c0-avg
        c1+=c0-avg
        if c1>avg:
            ans+=c1-avg
        else:
            ans+=2*(c2-avg)
    elif c1>avg:
        ans+=c1-avg
        c2+=c1-avg
        if c2>avg:
            ans+=c2-avg
        else:
            ans+=2*(c0-avg)
    else:
        ans+=c2-avg
        c0+=c2-avg
        if c0>avg:
            ans+=c0-avg
        else:
            ans+=2*(c1-avg)
    P(int(ans))
    tc-=1
        
    