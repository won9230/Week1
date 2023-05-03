import sys
n = int(sys.stdin.readline())
m = []
dp = [0] * (n + 1)

for i in range(n):
    m.append(int(sys.stdin.readline()))

dp[0] = m[0]
dp[1] = m[0] + m[1]
dp[2] = max(m[1] + m[2] , m[0] + m[2])
for i in range(3,n):
    dp[i] = max(dp[i - 3] + m[i - 1] + m[i],dp[i - 2] + m[i])

print(dp[n-1])