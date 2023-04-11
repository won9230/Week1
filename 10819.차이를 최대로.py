import sys

def next_p(a):
    k = -1
    m = -1
    
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            k = i
            
    if k == -1:
        return [-1]
    
    for i in range(k,len(a)):
        if a[k] < a[i]:
            m = i
    
    a[k],a[m] = a[m],a[k]
    
    a = a[:k+1] + sorted(a[k+1:])
    return a

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

ans = 0

s = 0

for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s
    
arr = a

while True:
    arr = next_p(arr)
    if arr == [-1]:
        break
    s = 0
    
    for j in range(len(arr) -1):
        s += abs(arr[j] - arr[j+1])
    if s > ans:
        ans = s
        
print(ans)