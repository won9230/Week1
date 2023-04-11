import sys

input = sys.stdin.readline

n = int(input())
a = [0] * 10001

for i in range(n):
    temp = int(input())
    a[temp] += 1
    
for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)