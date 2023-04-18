import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
queue = []
queue = deque(queue)
b = []
count = 0
for i in range(1,n+1):
    queue.append(i)
    
while len(b) < n:
    count += 1
    if count >= m:
        a1 = queue.popleft()
        b.append(a1)
        count = 0
    else:
        a1 = queue.popleft()
        queue.append(a1)

print("<",end='')
print(', '.join(map(str,b)),end='')
print(">")