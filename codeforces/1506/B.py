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
tc=inpi()
while tc:
    tc-=1
    
    n,k=inpm()
    st=inp()
    i=0
    ans=0
    tr=True
    while i<n and st[i]!="*":
        i+=1
    if i<=n-1:
        ans+=1
        if i!=n-1:
            st=st[:i]+"x"+st[i+1:]
        else:
            st=st[:i]+"x"
    else:
        tr=False
        P(0)       
    if tr:
        tr1=True
        i=n-1
        while i>=0 and st[i]!="*":
            i-=1
        if i<0:
            tr1=False
            P(ans)
        else:
            ans+=1
            if i!=n-1:
                st=st[:i]+"x"+st[i+1:]
            else:
                st=st[:i]+"x"
        if tr1:

            for i in ra(n-1):
                if st[i]=="x":
                    last=0
                    rep=True
                    for j in ra(1,k+1):
                        if i+j<n:
                            if st[i+j]=="*":
                                last=i+j
                    for j in ra(i+1,l(st)):

                        if st[j]=="x":
            
                            if j-i>k:
                                if last+1!=n:
                                
                                    st=st[:last]+"x"+st[last+1:]
                                else:
                                    st=st[:last]+"x"
                                ans+=1
                                break
                            else:
                                break
  
            P(ans)
                    
                        
                            
                    