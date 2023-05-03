import sys
n = int(sys.stdin.readline())
jump = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n)
dp[0] = 1

for i in range(n):
    if i + jump[i] + 1 > n:
        end = len(jump)
    else:
        end = i+jump[i]+1
    for j in range(i+1,end):
        if dp[j] == 0:
            dp[j] += dp[i] + 1
    if dp[i] == 0:
        print(-1)
        exit()

print(dp[-1]-1)