import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
tmp = 0
count = 0

for i in range(n):
    _m = m.pop()
    if tmp < _m:
        tmp = _m
        count += 1
print(count)