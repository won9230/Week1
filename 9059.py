import sys

n = int(sys.stdin.readline())

# def a(_n):
#     if _n == 1:
#         return 1
#     elif _n == 2:
#         return 2
#     elif _n == 3:
#         return 4
#     else :
#         return a(_n-1)+a(_n-2)+a(_n-3)


# print(a(n))

# def a(_n,arr,cur):
#     global count
#     if sum(cur) > _n:
#         return

#     elif sum(cur) == _n:
#         count += 1
#     else:
#         for i in arr:
#             tmp = list(cur)
#             tmp.append(i)
#             a(_n,arr,tmp)
            
# for i in range(n):
#     count = 0
#     b = int(sys.stdin.readline())
#     a(b,[1,2,3],[])
#     print(count)