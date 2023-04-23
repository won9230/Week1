import sys
import heapq
n = int(sys.stdin.readline())

datas = []
for _ in range(n):
    a,b = list(map(int,sys.stdin.readline().split()))
    datas.append((max(a,b),min(a,b)))

#입력받은 데이터들을 '끝점'기준으로 오름차순 정렬
datas.sort()

d = int(sys.stdin.readline()) # 거리
heap = [] # 기차를 탈 수 있는 사람들의 '출발점'을 담을 최소힙
max_result = 0 #결과를 담을 변수

for item in datas:
    if item[0] - item[1] <= d: #기차를 탈 수 있는 사람들의 '출발점'을 push
        heapq.heappush(heap,item[1])
    else:
        continue

    #heap에 담긴 데이터들 중에서 지금 담은 데이터의 '끝점'과 계산해서 거리가 d를 초과하는 데이터들 전부 제거
    while heap:
        start = heap[0] # 제일 작은 출발점
        if item[0] - start > d: # 지금 담은 데이터의 끝점 - 제일 작은 출발점
            heapq.heappop(heap)
        else:
            break
    max_result = max(len(heap),max_result)
print(max_result)

