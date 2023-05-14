import sys

graph = [[0] * 101 for _ in range(101)]

n = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)
        
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny
        
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            ans += 1

print(ans)