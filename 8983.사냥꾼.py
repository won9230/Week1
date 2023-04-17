import sys
m, n, l = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n))
s.sort()
kill = 0

for x,y in animal:
    i , j= 0,len(s) - 1
    while i <= j:
        mid = (i + j) // 2
        if abs(s[mid]-x)+y <= l:
            kill += 1
            break
        
        if s[mid] < x: #동물이 사로보다 멀거나 가까울 때
            i = mid + 1
        else:
            j = mid - 1
            
print(kill)