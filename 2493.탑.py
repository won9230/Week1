import sys
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
s = []
a = []

for i in range(n):
    while s:
        if s[-1][1] > m[i]:
            a.append(s[-1][0] + 1)
            break
        else:
            s.pop()
    if not s:
        a.append(0)
    s.append([i,m[i]])
    
print(' '.join(map(str,a)))