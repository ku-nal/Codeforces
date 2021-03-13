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
# tc=inpi()
# while tc:
#     tc-=1
#     n=inpi()
#     li=inpl()
#     stack,omap=[],{}
#     size=0
#     ms=[]
#     i=0
#     while i<n:
#         if li[i]==0:
#             stack.append(i+1)
#         else:
#             if len(stack)>0:
#                 rem=li[i]-((i+1)-stack[-1])
#                 st=stack[-1]
#                 while rem>0 and len(stack)>0:
#                     omap[st]=1
#                     if st==stack[-1]:
#                         stack.pop()
#                     st-=1
#                     rem-=1
#             omap[i+1]=1
#         i+=1
#     for i in range(1,n+1):
#         if i in omap:
#             P("1",end=" ")
#         else:
#             P("0",end=" ")
#     P()
tc=inpi()
while tc:
    tc-=1
    n=inpi()
    li=inpl()
    dp=[0]*n
    prev=n-2
    for i in reversed(ra(n)):
        if li[i]!=0:
            dp[i]=1
            if i<=prev:
                prev=i-1
            rem=li[i]-(i-prev)
            while rem>0 and prev>=0:
                dp[prev]=1
                prev-=1
                rem-=1
    for i in ra(n):
        if dp[i]:
            P("1",end=" ")
        else:
            P("0",end=" ")
    P()
    
        