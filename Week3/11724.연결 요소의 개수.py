import sys
sys.setrecursionlimit(10**5)
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
        

print(count)