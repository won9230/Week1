import sys
n = int(sys.stdin.readline())

f = []
num = 0
for i in range(n + 1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = f[-1] + f[-2]
    f.append(num)
    
print(f[-1])