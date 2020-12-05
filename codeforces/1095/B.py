

n=int(input())
li=list(map(int,input().split()))
li.sort()

print(min(li[-2]-li[0],li[-1]-li[1]))

  
        
        