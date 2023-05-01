import sys
n , k = map(int,sys.stdin.readline().split())
a = []
cnt = 0
ans = 0
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort(reverse=True)
for i in range(len(a)):
    if k >= a[i]:
        cnt = k // a[i]
        k = k - a[i] * cnt
        ans += cnt

print(ans)