import sys, math
n = sys.stdin.readline().rstrip()
m = []
for i in n:
    m.append(i)

m = list(map(int,m))

graph = [0] * 10

for i in m:
    graph[i] += 1


graph[6] = math.ceil((graph[9] + graph[6]) / 2)
graph[9] = 0

print(max(graph))