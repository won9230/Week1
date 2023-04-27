import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited =[[False] * m for _ in range(n)]

queue = deque()
maxS = []
count = 0
dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] += graph[x][y] + 1
                    queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()
for i in range(n):
    for j in range(m):
        count = max(count,graph[i][j])
print(count-1)