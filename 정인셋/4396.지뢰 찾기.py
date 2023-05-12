import sys
from collections import deque

n = int(sys.stdin.readline())

boomgraph = []
intgraph = []
flag = False
graph = [[0] * n for _ in range(n)]
dx = [0,1,0,-1,1,-1,1,-1]
dy = [1,0,-1,0,1,-1,-1,1]

for _ in range(n):
    boomgraph.append(sys.stdin.readline().rstrip())

for _ in range(n):
    intgraph.append(sys.stdin.readline())


for i in range(n):
    for j in range(n):
        count = 0
        if intgraph[i][j] == 'x':
            for k in range(8):
                if 0 <= i+dy[k] < n and 0 <= j + dx[k] < n:
                    if boomgraph[i+dy[k]][j+dx[k]] == '*':
                        count += 1
            graph[i][j] = str(count)
        if intgraph[i][j] == 'x' and boomgraph[i][j] == '*':
            flag = True

for i in range(n):
    for j in range(n):
        if flag:
            if intgraph[i][j] == '.':
                graph[i][j] = '.'
            if boomgraph[i][j] == '*':
                graph[i][j] = '*'
        else:
            if intgraph[i][j] == '.':
                graph[i][j] = '.'
        
for i in range(n):
    for j in range(n):
        print(graph[i][j],end = '')
    print()