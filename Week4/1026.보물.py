import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
c = []
for i in range(n):
    c.append(a[i]*b[i])

print(sum(c))