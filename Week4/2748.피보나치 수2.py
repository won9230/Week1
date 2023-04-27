import sys
n = int(sys.stdin.readline())
a,b = 0,1
sum = 0
if n == 0:
    print(0)
    exit()
elif n == 1:
    print(1)
    exit()
else:
    for i in range(1,n):
        sum = a + b
        a = b
        b = sum
print(sum)