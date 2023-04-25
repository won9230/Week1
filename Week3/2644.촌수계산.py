import sys
n = int(sys.stdin.readline())
a, b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[0] * (n + 1)for _ in range(n + 1)]
xy = []
dist = 0
flag = False
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    xy.append((x,y))
visited = [False] * (n+1)

def dfs(start,num):
    global dist,flag
    visited[start] = True
    if start == b:
        print(num)
        exit()
    for i in range(1,n+1):
        if not visited[i] and graph[start][i]:
            dfs(i,num + 1)
            
dfs(a,0)
print(-1)