import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

def bSherch(arr,target,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return bSherch(arr,target,start,mid - 1)
    elif arr[mid] < target:
        return bSherch(arr,target,mid + 1,end)
    
for i in range(m):
    print(bSherch(a,b[i],0,n-1))
    