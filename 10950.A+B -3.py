n = int(input())
i = 0
c = []

for i in range(n):
    a,b = map(int,input().split())
    c.append(a+b)
    
for i in range(len(c)):
    print(c[i])