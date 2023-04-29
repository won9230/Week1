import sys
T = int(sys.stdin.readline())
num = []
for _ in range(T):
    n = int(sys.stdin.readline())
    rank = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    rank_asc = sorted(rank)
    top = 0
    result = 1
    
    for i in range(1,len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    num.append(result)
print(num)