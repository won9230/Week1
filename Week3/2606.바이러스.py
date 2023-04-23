import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N+1)
count = 0

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    

if not visited[1]:
    if not graph[1]:
        visited[1] = True
    else:
        bfs(1)
# print(visited)            
for i in range(len(visited)):
    if visited[i]:
        count += 1
print(count-1)