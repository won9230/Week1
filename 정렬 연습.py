import sys

n = int(sys.stdin.readline())
a = list()
for i in range(n):
    a.append(int(sys.stdin.readline()))

# def shell(b):
#     n = len(b)
#     h = 1
    
#     while h < n:
#         h = h * 3 + 1
    
#     while h > 0:
#         for i in range(h ,n):
#             j = i - h
#             tmp = b[i]
#             while j >= 0 and b[j] > tmp:
#                 b[j + h] = b[j]
#                 j -= h
#             b[j + h] = tmp
#         h //= 3
# shell(a)

# def qivot(a,left,right):

#     pl = left
#     pr = right
#     x = a[(left + right) // 2]
    
#     while pl <= pr:
#         while a[pl] < x:
#             pl +=1
#         while a[pr] > x:
#             pr -= 1
#         if pl <= pr :
#             a[pl],a[pr] = a[pr],a[pl]
#             pl += 1
#             pr -= 1
#     if left < pr :
#         qivot(a,left,pr)
#     if pl < right : 
#         qivot(a,pl,right)

# def qsort(a):
#     qivot(a,0,len(a)-1)

# qsort(a)


print(a)