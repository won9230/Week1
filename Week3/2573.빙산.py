import sys
sys.setrecursionlimit(10**5)
#입력
n,m = map(int,sys.stdin.readline().split())
ice = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

year = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
#dfs
def dfs(x,y):
    visited[x][y] = True
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if not visited[nx][ny] and ice[nx][ny] != 0:
            dfs(nx,ny)
        elif ice[nx][ny] == 0:
            breaking[x][y] += 1
while True:
    visited = [[False] * m for _ in range(n)]
    breaking = [[0]*m for _ in range(n)]
    count = 0
    flag = False
    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] != 0:
               flag = True
               break
    if not flag:
        year = 0
        break
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] != 0 and not visited[i][j]:
                dfs(i,j)
                count += 1
                
    for i in range(1,n-1):
        for j in range(1,m-1):
            ice[i][j] -= breaking[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
                
    if count > 1:
        break
    year += 1

print(year)