import sys
n,m = map(int,sys.stdin.readline().split())
tmp = []
count = 0

def back(start):
    if len(tmp) == m:
        print(' '.join(map(str,tmp)))
        return
    
    for i in range(start,n+1):
            tmp.append(i)
            back(i)
            tmp.pop()
back(1)