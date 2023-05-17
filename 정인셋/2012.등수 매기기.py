import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))

m.sort()
# for i in range(1, n + 1):
#     if m[i - 1] > n:
#         continue
#     if i != m[i - 1]:
#         tmp1 = m[i - 1]
#         tmp2 = m[m[i - 1]-1]
#         m[m[i - 1]-1] = tmp1
#         m[i - 1] = tmp2
# cnt = 0
# for i in range(1,n + 1):
#     cnt += abs(i - m[i - 1])
    
# print(cnt)
cnt = 0
for i in range(n):
    cnt += abs((i + 1) - m[i])
print(cnt)