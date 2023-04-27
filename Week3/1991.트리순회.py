import sys
sys.setrecursionlimit(10**5)
n = []
while True:
    try:
        n.append(int(sys.stdin.readline()))
    except:
        break
    
def p(start,end):
    if start > end:
        return
    mid = end + 1
    
    for i in range(start + 1,end +1):
        if n[start] < n[i]:
            mid = i
            break
    p(start + 1,mid-1)
    p(mid,end)
    print(n[start])

p(0,len(n)-1)