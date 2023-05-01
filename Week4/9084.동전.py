import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    
    d = [0] * (m + 1)
    d[0] = 1
    
    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                d[i] += d[i - coin]
    print(d[m])