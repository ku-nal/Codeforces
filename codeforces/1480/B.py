#===========Template===============
from io import BytesIO, IOBase
import sys,os
inpl=lambda:list(map(int,input().split()))
inpii=lambda:map(int,input().split())
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
import sys,math 
# sys.stdin = open('input.txt', 'r')   
# sys.stdout = open('output.txt', 'w')


#==============To chaliye shuru krte he ====================#
test=inpi()
while test:
    a,b,n=inpii()
    li1=inpl()
    li2=inpl()
    idx=li1.index(max(li1))
    li1.append(li1.pop(idx))
    li2.append(li2.pop(idx))
    i=0
    tr=True
    while b>0 and i<n:
        fi=math.ceil(li2[i]/a)
        if i==n-1:
            if b>(fi-1)*li1[i]:
                i+=1
                continue
            else:
                b=0
                tr=False
                break
        elif b<fi*li1[i]:
            b=0
            tr=False
            break
        else:
            b-=fi*li1[i]
        i+=1
    if b>0 or (i>=n and tr):
        print("Yes")
    else:print("No")
    test-=1