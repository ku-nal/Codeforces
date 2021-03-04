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
n,k=inpm()
li=inpl()
omap={}
ans=min(li.count(2),li.count(1))
add=0
for i in ra(k):
    a,b=0,0
    for j in ra(i,n,k):
        if li[j]==2:
            b+=1
        else:
            a+=1
    add+=min(a,b)
# for i in range(2,n):
#     if n%i==0:
#         j=0
#         omapw={}
#         while j<n:
#             if ''.join(li[j:j+i]) in omapw:
#                 omapw[''.join(li[j:j+i])]+=1
#             else:
#                 omapw[''.join(li[j:j+i])]=1
#             j+=i
#         ma=0
#         for k,v in omapw.items():
#             if v>ma:
#                 ma=v
#                 wo=k
#                 v=k
#         add=0

#         for k in range(0,n,i):
#             te=0
#             for t in ra(k,k+i):
#                 if wo[te]!=li[t]:
#                     add+=1
#                 te+=1
                    
#         ans=min(ans,add)
P(min(ans,add))
        
            
