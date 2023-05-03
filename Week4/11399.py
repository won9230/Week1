import sys
n = int(sys.stdin.readline())
peo = list(map(int,sys.stdin.readline().split()))
peo.sort()
plue = []
cnt = 0
tmp = peo[0]
plue.append(tmp)
for i in range(1,n):
    tmp += peo[i]
    plue.append(tmp)
print(sum(plue))