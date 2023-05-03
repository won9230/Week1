import sys
n , k = map(int,sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse = True)
cnt = 0
for i in range(n):
    if k >= coins[i]:
        cnt += (k // coins[i])
        k %= coins[i]
print(cnt)