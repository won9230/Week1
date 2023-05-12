import sys
n, m = map(int,sys.stdin.readline().split())
x, y, d = map(int,sys.stdin.readline().split())
graph = []
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
if d == 1:
    d = 3
elif d == 3:
    d = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited[i][j] = 1
count = 0
dy = [-1,0,1,0]
dx = [0,-1,0,1]
rotPos = [x,y]
rotD = d
while True:
    flag = False
    if visited[rotPos[0]][rotPos[1]] == 0:
        visited[rotPos[0]][rotPos[1]] = 1
        count += 1
    for i in range(4):
        tmp = 0
        if visited[rotPos[0] + dy[i]][rotPos[1] + dx[i]] == 0 and graph[rotPos[0] + dy[i]][rotPos[1] + dx[i]] == 0:
            flag = True
            break
        
    if flag:
        rotD += 1
        if rotD >= 4:
            rotD = 0
        if visited[rotPos[0] + dy[rotD]][rotPos[1] + dx[rotD]] == 0 and graph[rotPos[0] + dy[rotD]][rotPos[1] + dx[rotD]] == 0:
            rotPos = [rotPos[0] + dy[rotD],rotPos[1] + dx[rotD]]
    else:
        if graph[rotPos[0] - dy[rotD]][rotPos[1] - dx[rotD]] == 0:
            rotPos = [rotPos[0] - dy[rotD],rotPos[1] - dx[rotD]]
        else:
            break
print(count)