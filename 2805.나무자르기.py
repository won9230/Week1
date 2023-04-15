import sys
n1 , m1 = sys.stdin.readline().split()
tree = list(map(int,sys.stdin.readline().split()))
tree.sort()
n = int(n1) # 나무 개수
m = int(m1) # 필요한 나무
h = 0

def bSearch(arr,start,end):
    global h
    h = (start + end) // 2
    
    if start > end:
        return h

    anw = 0
    
    for i in range(len(arr)):
        if arr[i] > h:
           anw = anw + (arr[i] - h)
    
    if m == anw:
        return h
    elif m < anw:
        return bSearch(arr,h+1,end)
    elif m > anw:
        return bSearch(arr,start,h-1)

print(bSearch(tree,1,max(tree)))