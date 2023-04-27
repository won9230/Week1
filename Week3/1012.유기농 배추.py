import sys
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(y,x):
    global count
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < m and ny < n:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny,nx)
        

for i in range(t):
    count = 0
    m , n , k = map(int,sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x,y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i,j)
                count += 1
                
    print(count)