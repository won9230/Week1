import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
a.sort(key=lambda x:(x[1],x[0]))

cnt = 1
first = a[0][1]
for i in range(1,n):
    if first <= a[i][0]:
        first = a[i][1]
        cnt += 1
print(cnt)