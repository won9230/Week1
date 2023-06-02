import sys
from collections import deque

n, l = map(int,sys.stdin.readline().split())
m = list(map(int,sys.stdin.readline().split()))

m.sort()

start = m[0]
end = m[0] + (l - 1)
count = 1

for i in range(1, len(m)):
    if start < m[i] <= end:
        continue
    else:
        start = m[i]
        end = m[i] + (l - 1)
        count += 1

print(count)