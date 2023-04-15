import sys
from math import inf
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
m.sort()

def bS():
    i = 0
    j = len(m)-1
    r = inf
    while i < j:
        tmp = m[i] + m[j]
        if tmp == 0:
            return m[i],m[j]
        if abs(tmp) < r:
            result = (m[i],m[j])
            r = abs(tmp)
        if tmp < 0:
            i += 1
        else :
            j -= 1
    return result

a = bS()
print(str(a[0]) + " " + str(a[1]))