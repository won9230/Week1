import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
# b.sort()

def binaty_search(arr,start,target,end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binaty_search(arr,mid+1,target,end)
    else :
        return binaty_search(arr,start ,target,mid - 1)

for i in range(n):
    print(binaty_search(a,0,b[i],n-1))