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
a,b=inpm()
if b<a-1:
    P(-1)
elif b>2*(a+1):
    P(-1)
else:
    if b>2*(a-1):
        rem=b-(2*(a-1))
        ans="011"*(a-1)
        ans+="0"
        if rem==1:
            ans="1"+ans
        elif rem==2:
            ans="11"+ans
        elif rem==3:
            ans="11"+ans+"1"
        elif rem==4:
            ans="11"+ans+"11"
    else:
        ans=""
        rem=b-(a-1)
        ans+="011"*rem
        ans+="01"*((a-1)-rem)
        ans+="0"
    P(ans)
        
    # ans=""
    # zero,one=a,b
    # for i in ra(a):
    #     if i!=a-1:
    #         ans+="0"
    #         zero-=1
    #         ans+="1"
    #         one-=1
    #         if one>zero-1:
    #             ans+="1"
    #             one-=1
    #     else:
    #         ans+="0"
 
    # P(ans)          
