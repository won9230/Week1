import sys
n , m = map(int,sys.stdin.readline().split())
b = list(map(int,sys.stdin.readline().split()))
b.sort()
tmp = []

def back(start):
    if len(tmp) == m:
        print(" ".join(map(str,tmp)))
        return
    
    for i in range(start,len(b)):
        if b[i] not in tmp:
            tmp.append(b[i])
            back(i)
            tmp.pop()
        
back(0)