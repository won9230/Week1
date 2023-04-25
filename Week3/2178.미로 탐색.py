import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            
            if _x < 0 or _x > n-1 or _y < 0 or _y > m-1:
                continue
            if graph[_x][_y] == 0:
                continue
            if graph[_x][_y] == 1:
                q.append((_x,_y))
                graph[_x][_y] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))