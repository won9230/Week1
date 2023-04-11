n = int(input())
a = list()

for i in range(n):
    a.append(int(input()))


def sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                _temp = a[j]
                a[j] = a[i]
                a[i] = _temp
sort(a)
for i in range(len(a)):
    print(a[i])
