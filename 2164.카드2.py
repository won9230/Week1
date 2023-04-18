from collections import deque
import sys
n = int(sys.stdin.readline())
queue = []
queue = deque()
for i in range(1,n+1):
    queue.append(i)


for i in range(n):
    a1 = queue.popleft()
    if len(queue) == 0:
        print(a1)
    else:
        a2 = queue.popleft()
        queue.append(a2)
        