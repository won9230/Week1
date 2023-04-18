import heapq
import sys
heap = []

n = int(sys.stdin.readline().strip())

for i in range(n):
    m = int(sys.stdin.readline())
    if m != 0:
        heapq.heappush(heap,(-m,m))
    else :
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)