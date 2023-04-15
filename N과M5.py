import sys
n,m = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
s.sort()
tmp = []

def back():
    if len(tmp) == m:
        print(" ".join(map(str,tmp)))
        return
    
    for i in range(len(s)):
        if s[i] not in tmp:
            tmp.append(s[i])
            back()
            tmp.pop()
                
back()