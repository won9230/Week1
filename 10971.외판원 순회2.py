import sys
n = int(sys.stdin.readline())

tr_Cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
min_value = sys.maxsize

def dfs_backtracking(start,next,value,visited):
    global min_value
    
    if len(visited) == n:
        if tr_Cost[next][start] != 0:
            min_value = min(min_value,value + tr_Cost[next][start])
        return
    for i in range(n):
        if tr_Cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start,i,value + tr_Cost[next][i],visited)
            visited.pop()
            
for i in range(n):
    dfs_backtracking(i,i,0,[i])
print(min_value)