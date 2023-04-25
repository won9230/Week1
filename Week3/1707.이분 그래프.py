import sys
k = int(sys.stdin.readline())#테스트 케이스

def dfs(start,group):
    visited[start] = group
    
    for i in graph[start]:
        if not visited[i]:
            a = dfs(i,-group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

#for문으로 정점 간선 받아오기 
for i in range(k):
    v,e = map(int,sys.stdin.readline().split())
    graph = [[]for i in range(v + 1)]
    visited = [False] * (v + 1)
    for _ in range(e):
        u,v = map(int,sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
        
    for i in range(1,v + 1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
    print('YES' if result else "NO")
