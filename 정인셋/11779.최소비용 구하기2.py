import sys, heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 1e8

graph = [[] for _ in range(n + 1)]

visited = [False]  * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

sCity,eCity = map(int,sys.stdin.readline().split())

p_node = [0] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                p_node[i[0]] = now
                heapq.heappush(q, (dist + i[1], i[0]))
dijkstra(sCity)
print(distance[eCity])

path = [eCity]
now = eCity
while now != sCity:
    now = p_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(*path)