import sys
from collections import deque
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
m.sort()
m = deque(m)
while len(m) != 1:
    start = m.popleft()
    end = m.pop()
    m.append(end + (start * 0.5))

print(m[0])