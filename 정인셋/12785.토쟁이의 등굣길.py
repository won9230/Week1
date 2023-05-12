import sys
x , y = map(int,sys.stdin.readline().split())
tx , ty = map(int,sys.stdin.readline().split())
dp1 = [[0] * (x + 1) for _ in range(y + 1)]
dp2 = [[0] * (x + 1) for _ in range(y + 1)]

dp1[1][1] = 1
dp2[ty][tx] = 1

for i in range(1,ty+1):
    for j in range(1,tx+1):
        dp1[i][j] = dp1[i][j] + dp1[i - 1][j] + dp1[i][j - 1]
        
for i in range(ty,y+1):
    for j in range(tx,x+1):
        dp2[i][j] = dp2[i][j] + dp2[i - 1][j] + dp2[i][j - 1]
        
print(dp1[ty][tx] * dp2[y][x] % 1000007)
        