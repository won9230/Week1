import sys

n = int(sys.stdin.readline())
a = list()
for i in range(n):
    a.append(int(sys.stdin.readline()))

def shell(b):
    n = len(b)
    h = 1
    
    while h < n:
        h = h * 3 + 1
    
    while h > 0:
        for i in range(h ,n):
            j = i - h
            tmp = b[i]
            while j >= 0 and b[j] > tmp:
                b[j + h] = b[j]
                j -= h
            b[j + h] = tmp
        h //= 3        
    
shell(a)
print(a)