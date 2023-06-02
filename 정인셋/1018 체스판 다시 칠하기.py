import sys
n, m = map(int,sys.stdin.readline().split())

CMap = []

for i in range(n):
    CMap.append(sys.stdin.readline().rstrip())

print(CMap[0][0])