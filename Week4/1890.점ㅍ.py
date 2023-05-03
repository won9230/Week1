import sys
n = int(sys.stdin.readline())
Amap = []
for i in range(n):
    Amap.append(list(map,int(sys.stdin.readline().split())))

Amap[0][0] = 1
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1:
            print(dp[i][j])
            break
        if dp[i][j] != 0: