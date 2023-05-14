import sys

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

n, m = map(int,sys.stdin.readline().split())
parent = list(range(n + 1))
ct = 0

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    if find(x) != find(y):
        union(x, y)
        ct += 1
        if ct == n - 2:
            print(0, 0)
            exit()
    
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
edges = []
for i in range(1, n - 1):
    for j in range(i + 1 , n):
        edges.append((i + 1, j + 1, matrix[i][j]))
        
cost = 0
connent = []
for u, v ,w in sorted(edges, key = lambda x: x[2]):
    union(u, v)
    ct += 1
    cost += w
    connent.append((u, v))
    if ct == n - 2:
        print(cost, len(connent))
        for u, v in connent:
            print(u, v)
        break