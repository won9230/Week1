import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    money = int(sys.stdin.readline())
    suff = [0] * (money + 1)
    suff[0] = 1
    for coin in coins:
        for j in range(1,money + 1):
            suff[j] += suff[j - coin]
    print(suff[-1])