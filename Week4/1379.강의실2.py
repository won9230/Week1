import sys
n = int(sys.stdin.readline())
ga = []
for i in range(n):
    ga.append(list(map(int,sys.stdin.readline().split())))
ga.sort(key = lambda x: x[1])

print(ga)