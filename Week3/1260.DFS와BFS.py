import sys
from collections import deque
n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(start):
    visited1[start] = True
    print(start,end=' ')
    for i in graph[start]:
        if not visited1[i]:
            dfs(i)
    
def bfs(v):
    queue = deque([v])
    visited2[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                queue.append(i)

dfs(v)
print()
bfs(v)