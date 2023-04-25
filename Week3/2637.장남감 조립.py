import sys
from collections import deque

n = int(sys.stdin.readline())
connect = [[] for _ in range(n + 1)] #연결 정보
needs = [[0] * (n + 1) for _ in range(n + 1)]
q = deque()
degree = [0] * (n + 1)
for _ in range(int(sys.stdin.readline())):
    a,b,c = map(int,sys.stdin.readline().split())
    connect[b].append((a,c))
    degree[a] += 1
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    for next,next_need in connect[now]:
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        else:
            for i in range(1,n + 1):
                needs[next][i] += needs[now][i] * next_need
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)
for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)
# print(needs)