import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# visit = [[0 for _ in range(n)] for _ in range(n)]

maxH = max(max(city))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < n) and (0 <= ny < n) and not c_city[nx][ny] and city[nx][ny] > h :
            c_city[nx][ny] = True
            dfs(nx,ny,h)
         
ans = 1
for k in range(maxH):
    c_city = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] > k and not c_city[i][j]:
                count += 1
                c_city[i][j] = True
                dfs(i,j,k)
    ans = max(ans,count)
    
print(ans)