import sys
n = int(sys.stdin.readline())
cases = list(map(int,sys.stdin.readline().split()))
lis = [0]

for case in cases:
    if lis[-1]< case: 
        lis.append(case)
    else:
        left = 0
        right = len(lis)
        
        while left < right:
            mid = (right + left) // 2
            if lis[mid] < case:
                left = mid + 1
            else:
                right = mid
        lis[right] = case
print(len(lis)-1)