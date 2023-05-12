import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(v):
    global count
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
                
for _ in range(t):
    count = 0
    n,m = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n + 1)]
    visited = [False]  * (n + 1)
    for i in range(m):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs(1)
    print(count-1)