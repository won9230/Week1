import sys
n = int(sys.stdin.readline())
b = []
for i in range(n):
    b.append(int(sys.stdin.readline()))
m = [[1,1,1],[1,1,1],[1,1,1],[1,0,0]]
v = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
tmp = 0
for i in range(4):
    for j in range(3):
        tmp += m[i][j]

a = []
a.append(tmp)

for k in range(1000):
    for i in range(4):
        for j in range(3):
            if m[i][j] == 0:
                continue
            else:
                v[i][j] = 0
                if i - 1 >= 0 :
                    v[i][j] += m[i - 1][j]
                if i + 1 < 4:
                    v[i][j] += m[i + 1][j]
                if j - 1 >= 0 :
                    v[i][j] += m[i][j - 1]
                if j + 1 < 3:
                    v[i][j] += m[i][j + 1]
    tmp = 0
    for i in range(4):
        for j in range(3):
            tmp += v[i][j]
            m[i][j] = v[i][j]
    a.append(tmp % 1234567)

for i in b:
    print(a[i-1])
