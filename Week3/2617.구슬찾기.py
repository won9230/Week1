import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

bigger_lst = [[] for _ in range(n+1)]
smaller_lst = [[] for _ in range(n+1)]
mid = (n+1)/2

for i in range(m):
    a,b = map(int,input().split())
    bigger_lst[b].append(a)
    smaller_lst[a].append(b)

def dfs(arr,n):
    global cnt
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(arr,i)

answer = 0
for i in range(1,n+1):
    visited = [False] * n+1
    cnt = 0
    dfs(bigger_lst,i)
    if cnt >= mid:
        answer += 1
    cnt = 0
    dfs(smaller_lst,i)
    if cnt >= mid:
        answer += 1
        
print(answer)