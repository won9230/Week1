import sys
n = int(sys.stdin.readline())

b = []

for i in range(n):
    tmp = 0
    m = list(input())
    a = [] 
    for j in range(len(m)):
        if m[j] == '(':
            a.append(m[j])
            tmp += 1
        else:
            if len(a) == 0:
                tmp += 1
                break
            else:
                a.pop()
                tmp -= 1
                
    if tmp == 0 and len(a) == 0:
        b.append('YES')
    else:
        b.append('NO')
for i in range(n):
    print(b[i])