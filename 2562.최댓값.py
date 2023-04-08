c = list()
for i in range(9):
    a = int(input())
    c.append(a)
    
max = c[0]
maxi = 0
for i in range(len(c)):
    if max < c[i]:
        max = c[i]
        maxi = i
        
print(max)
print(maxi+1)
