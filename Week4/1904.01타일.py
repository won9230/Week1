import sys

n = int(sys.stdin.readline())

d = [0] * (n + 2)
d[1] = 1
d[2] = 2
cnt = 0
for i in range(3,n + 2):
    d[i] = (d[i - 2] + d[i - 1]) % 15764
print(d[n])