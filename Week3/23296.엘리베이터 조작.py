import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    for i in range(1,n + 1):
        if not visited[i]:
            dfs(a[start])
dfs(a[0])