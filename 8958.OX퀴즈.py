n = int(input())
c = list()
a = 0
b = 0
sum = list()

for i in range(n):
    c.append(input())

for i in range(len(c)):
    a = 0
    b = 0
    for j in range(len(c[i])):
        if c[i][j] == 'O':
            a += 1
            b += a
        elif c[i][j] == 'X':
            a = 0
    sum.append(b)

for i in range(len(sum)):
    print(sum[i])
    