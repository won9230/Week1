import sys
# n = int(sys.stdin.readline())
# a,b = 0,1
# sum = 0
# if n == 0:
#     print(0)
#     exit()
# elif n == 1:
#     print(1)
#     exit()
# else:
#     for i in range(1,n):
#         sum = a + b
#         a = b
#         b = sum
# print(sum)

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