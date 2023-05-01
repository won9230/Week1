import sys
n , k = map(int,sys.stdin.readline().split())

backpack = [[0,0]]
suff = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    backpack.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n+1):
    w = backpack[i][0]
    v = backpack[i][1]
    for j in range(1,k+1):
        if j < w:
            suff[i][j] = suff[i - 1][j]
        else:
            suff[i][j] = max(v + suff[i - 1][j - w],suff[i - 1][j])
print(suff[n][k])