n = int(input())
a = list()

for i in range(n):
    a.append(int(input()))

# def shell_sort(a):
#     n = len(a)
#     h = n // 2
    
#     while h < n:
#         h = h * 3 + 1
#     while h > 0:
#         for i in range(h,n):
#             j = i - h
#             tmp = a[i]
#             while j >= 0 and a[j] > tmp:
#                 a[j+h] =a[j]
#                 j-=h
#             a[j+h] = tmp
#         h //= 2

# shell_sort(a)

# def qsort(a , left,right):
#     pl = left
#     pr = right
    
#     x = a[(left+right)//2]
   
#     while pl <= pr :
#         while a[pl] < x : pl += 1
#         while a[pr] > x : pr -= 1
#         if pl <= pr:
#             a[pl],a[pr] = a[pr],a[pl]
#             pl += 1
#             pr -= 1
    
#     if left < pr :
#         qsort(a,left,pr)
#     if pl < right:qsort(a,pl,right)

# def merge_sort(a):
    
#     def _merge_sort(a,left,right):
#         if left < right:
#             center = (left + right) // 2
            
#             _merge_sort(a,left,center)
#             _merge_sort(a,center+1,right)
            
#             p = j = 0
#             i = k = left
            
#             while i <= center:
#                 buff[p] = a[i]
#                 p += 1
#                 i += 1
            
#             while i <= right and j < p :
#                 if buff[j] <= a[i]:
#                     a[k] = buff[j]
#                     j += 1
#                 else:
#                     a[k] = a[i]
#                     i += 1
#                 k += 1
                
#             while j < p:
#                 a[k] = buff[j]
#                 k += 1
#                 j += 1
#     n = len(a)
#     buff = [None] * n
#     _merge_sort(a,0,n-1)
#     del buff

# merge_sort(a)

# def heapsort(a):
#     def down_heap(a,left,right):
#         temp = a[left]
        
#         parent = left
#         while parent < (right + 1) //2:
#             cl = parent * 2 + 1
#             cr = cl + 1
#             child = cr if cr <= right and a[cr] > a[cl] else cl
#             if temp >= a[child]:
#                 break
#             a[parent] = a[child]
#             parent = child
#         a[parent] = temp
    
#     n = len(a)

#     for i in range((n - 1) // 2,-1,-1):
#         down_heap(a,i,n-1)
    
#     for i in range(n - 1,0,-1):
#         a[0],a[i] = a[i] ,a[0]
#         down_heap(a,0,i - 1)
        
# heapsort(a)

def fsort(a,max):
    n = len(a)
    f = [0] * (max + 1)
    b = [0] * n
    
    for i in range(n): f[a[i]] += 1
    for i in range(1,max + 1): f[i] += f[i - 1]
    for i in range(n - 1,-1,-1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
    for i in range(n): a[i] = b[i]

def counting_sort(a):
    fsort(a,max(a))
    
x = [None] * n

counting_sort(a)
print(a)