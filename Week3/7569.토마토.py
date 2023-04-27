import sys
from collections import deque
m,n,h = map(int,sys.stdin.readline().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    graph.append(tmp)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while (queue):
    x,y,z = queue.popleft()
    for i in range(6):
        _x = x + dx[i]
        _y = y + dy[i]
        _z = z + dz[i]
        if 0 <= _x < h and 0 <= _y < n and 0 <= _z < m and graph[_x][_y][_z] == 0:
            queue.append([_x,_y,_z])
            graph[_x][_y][_z] = graph[x][y][z] + 1
    
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)