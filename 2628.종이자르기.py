a,b = map(int,input().split())
n = int(input())
w = [0,a]
h = [0,b]

for i in range(n):
    d1,d2 = map(int,input().split())
    if d1 == 0:
        h.append(d2)
    elif d1 == 1:
        w.append(d2)
h.sort()
w.sort()

a = 0

for i in range(len(w)-1):
    for j in range(len(h)-1):
        x = w[i+1] - w[i]
        y = h[j+1] - h[j]
        a = max(a,x*y)
        
print(a)