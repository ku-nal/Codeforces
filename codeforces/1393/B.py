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
import sys,operator



#==============To chaliye shuru krte he ====================#
no=100001
n=inpi()
li=inpl()
e=inpi()
arr=[0]*(no)
a4,a2=0,0
for i in ra(n):
    arr[li[i]]+=1
for i in ra(1,no):
    c=arr[i]//4
    a4+=c
    d=(arr[i]%4)//2
    a2+=d
for i in ra(e):
    a,b=input().split()
    b=int(b)
    temp=arr[b]
    if a=="+":
        arr[b]+=1
        if temp//4!=arr[b]//4:
            a4+=1
        if (temp%4)//2>(arr[b]%4)//2:
            a2-=1
        elif (temp%4)//2<(arr[b]%4)//2:
            a2+=1
    else:
        arr[b]-=1
        if temp//4!=arr[b]//4:
            a4-=1
        if (temp%4)//2>(arr[b]%4)//2:
            a2-=1
        elif (temp%4)//2<(arr[b]%4)//2:
            a2+=1
    
    if a4>=1:
        if a4>=2 or a2>=2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
            