import sys
_a = []
a = []
all = 0

for i in range(9):
    _a.append(sys.stdin.readline().strip())
a = list(map(int, _a))

a.sort()

all = sum(a)

for i in range(len(a)):
    for j in range(len(a)):
        if (all - 100) == a[i] + a[j] and a[i] != a[j]:
            a.remove(a[i])
            a.remove(a[j-1])
            break
    if len(a) == 7:
        break

for i in range(len(a)):
    print(a[i])