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
import sys 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')


#==============To chaliye shuru krte he ====================#
tc=inpi()
while tc:
    n=inpi()
    li=inpl()
    ans=0
    for i in ra(n-1):
        ans+=abs(li[i]-li[i+1])
    hill,vall=0,0
    for i in ra(1,n-1):
        if li[i]>li[i-1] and li[i]>li[i+1]:
           
            hill=max(hill,abs(li[i]-li[i+1])+abs(li[i]-li[i-1])-abs(li[i-1]-li[i+1]))
    for i in ra(1,n-1):
        if li[i]<li[i-1] and li[i]<li[i+1]:
            
            vall=max(vall,abs(li[i]-li[i+1])+abs(li[i]-li[i-1])-abs(li[i-1]-li[i+1]))
    ans=min(ans,ans-hill,ans-vall,ans-abs(li[0]-li[1]),ans-abs(li[-1]-li[-2]))
    P(ans)
    tc-=1
    