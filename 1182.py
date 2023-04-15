import sys
n , s= map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
count = 0
tmp = []

def a(x):
    global count
    if len(tmp) == x:
        if sum(tmp) == s:
            count += 1
        return
    
    for i in range(x,n):
        tmp.append(i)
        a(i+1)
        tmp.pop()

for i in range(n+1):
    a(i)
print(count)