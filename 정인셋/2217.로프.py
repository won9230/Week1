import sys

n = int(sys.stdin.readline())
w = []

for i in range(n):
    w.append(int(sys.stdin.readline()))
    
w.sort(reverse = 1)

result = []

for i in range(1,n + 1):
    a = i * w[i-1]
    result.append(a)
print(max(result))