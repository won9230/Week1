import sys
sys.setrecursionlimit(10**5)

n, m, k = map(int,sys.stdin.readline().split())

graph = list([0] * m for _ in range(n))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(k):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1

visited = list([False] * m for _ in range(n))
cnt = 0
ans = []
def dfs(y,x):
    global cnt
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny,nx)
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            ans.append(dfs(i,j) + 1)
            cnt = 0
print(max(ans))