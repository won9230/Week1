import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(a)
while start <= end:
    mid = (end + start) // 2
    cnt = 0
    for i in range(n):
        if a[i] <= mid:
            cnt += a[i]
        else:
            cnt += mid
    if cnt <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
    