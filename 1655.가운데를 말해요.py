import sys
import heapq

n = int(sys.stdin.readline())
max_h,min_h = [],[]
a = []
for i in range(n):
    m = int(sys.stdin.readline())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h,-m)
    else:
        heapq.heappush(min_h,m)

    if min_h and min_h[0] < -max_h[0]:
       max_v = heapq.heappop(max_h)
       min_v = heapq.heappop(min_h)
       
       heapq.heappush(max_h,-min_v)
       heapq.heappush(min_h,-max_v)
                      
    print(-max_h[0])