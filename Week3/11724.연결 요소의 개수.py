# import sys
# from collections import deque

# def bfs(start):
#     queue = deque([start]) #i번 넣기(방문처리 인덱스)
#     visited[start] = True  #방문처리 해준다
#     while queue:
#         node = queue.popleft() #노드를 뺴준다
#         for i in graph[node]:  #graph[node]에 들어있는 인덱스 만큼
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
            
# N,M = map(int,sys.stdin.readline().split())
# graph = [[] for _ in range(N+1)]

# for _ in range(M):
#     a,b = map(int,sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# visited = [False] * (1 + N) #방문 처리 (정점의 수 + 1만큼)
# count = 0

# for i in range(1, N + 1):
#     if not visited[i]:      #방문처리가 되있지 않으면
#         if not graph[i]:    #값이 없으면
#             count += 1
#             visited[i] = True
#         else:               #값이 있으면
#             bfs(i)
#             count += 1
            
# print(count)
            
#DFS##################################################################################
import sys

def dfs(start,depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i,depth+1)

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1+n)
count = 0

for i in range(1,n+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i,0)
            count += 1
print(count)

############################################################
