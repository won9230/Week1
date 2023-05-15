import sys
r, c, t = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

clean = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(r):
        if graph[i][0] == -1:
            clean.append(i)

for k in range(t):
    tmpGraph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                a = graph[i][j]
                tmp = 0
                for l in range(4):
                    if 0 <= i + dy[l] < r and 0 <= j + dx[l] < c and graph[i+dy[l]][j+dx[l]] != -1:
                        tmpGraph[i + dy[l]][j + dx[l]] = tmpGraph[i + dy[l]][j + dx[l]] + (graph[i][j] // 5)
                        tmp += 1
                tmpGraph[i][j] = tmpGraph[i][j] + (graph[i][j] - ((graph[i][j] // 5) * tmp))
            elif graph[i][j] == -1:
                tmpGraph[i][j] = -1
    graph = tmpGraph
    for i in range(clean[0], 0, -1):
        if graph[i][0] != -1:
            graph[i][0] = graph[i - 1][0]
    for i in range(c - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(0, clean[0]):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for i in range(c - 1, 0, -1):
        if graph[clean[0]][i - 1] != -1:
            graph[clean[0]][i] = graph[clean[0]][i - 1]
        else:
            graph[clean[0]][i] = 0
        
    for i in range(clean[1], r - 1):     
        if graph[i][0] != -1:   
            graph[i][0] = graph[i + 1][0]
    for i in range(0, c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]
    for i in range(r - 1, clean[1],-1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for i in range(c - 1, 0 , -1):
        if graph[clean[1]][i - 1] != -1:
            graph[clean[1]][i] = graph[clean[1]][i - 1]
        else:
            graph[clean[1]][i] = 0

    for i in range(2):
        graph[clean[i]][0] = -1
cnt = 0
for i in range(r):
    for j in range(c):
        cnt += graph[i][j]
print(cnt + 2)