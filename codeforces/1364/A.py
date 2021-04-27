#===========Template===============
from io import BytesIO, IOBase
from math import sqrt
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

def B(n):
    return bin(n).replace("0b","")

def factors(n):
    arr=[]
    for i in ra(2,int(sqrt(n))+1):
        if n%i==0:
            arr.append(i)
            if i*i!=n:
                arr.append(int(n/i))
    return arr  

def dfs(arr,n):
    pairs=[[i+1] for i in ra(n)]
    vis=[0]*(n+1)
    for i in ra(l(arr)):
        pairs[arr[i][0]-1].append(arr[i][1])
    pairs[arr[i][1]-1].append(arr[i][0])
    
    comp=[]
    for i in ra(n):
        stack=[pairs[i]]
        temp=[]
        if vis[stack[-1][0]]==0: 
            while len(stack)>0:
                if vis[stack[-1][0]]==0:
                    temp.append(stack[-1][0])
                    vis[stack[-1][0]]=1
                    s=stack.pop()
                    for j in s[1:]:
                        if vis[j]==0:
                            stack.append(pairs[j-1])
                else:
                    stack.pop()
            comp.append(temp)
    return comp
    
  
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
    n,x=inpm()
    li=inpl()
    su=sum(li)
    tr=False
    for i in ra(n):
        if li[i]%x!=0:
            tr=True
            break
    if tr:
        if su%x!=0:
            P(n)
        else:
            for i in ra(n):
                if li[i]%x!=0:
                    idx1=i
                    break
            for i in rev(ra(n)):
                if li[i]%x!=0:
                    idx2=i
                    break
            ans=max(n-idx1-1,idx2)
            P(ans)
    else:P(-1)
        
        
                  