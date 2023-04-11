import sys
n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(sys.stdin.readline())

def sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j] and len(a[i]) == len(a[j]):
                _temp = a[j]
                a[j] = a[i]
                a[i] = _temp

set_a = set(a)
a = list(set_a)
a.sort()
a.sort(key=len)

for i in range(len(a)):
    print(a[i])

# sort(a)
