import sys
n,m = map(int,sys.stdin.readline().split())
tmp = []

def back():
    if len(tmp) == m:
        print(" ".join(map(str,tmp)))
        return
    
    for i in range(1,n+1):
        if i not in tmp:
            tmp.append(i)
            back()
            tmp.pop()

back()