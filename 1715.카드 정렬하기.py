import sys
import heapq
n = int(sys.stdin.readline())
m = []
#최소 힙 사용해서 제일 작은 두 수 구하기
#둘이 더한 숫자 다시 힙에 넣기
for i in range(n):
    heapq.heappush(m,int(sys.stdin.readline()))

result = 0

if len(m) == 1:
    print(result)
else:
    for i in range(n-1):
        previous = heapq.heappop(m)
        current = heapq.heappop(m)
        
        result += previous + current
        heapq.heappush(m,previous + current)
    
    print(result)
        