import heapq
import sys
n = int(sys.stdin.readline())
buildings = []
end_points = []

for i in range(n):
    start, height, end = map(int,sys.stdin.readline().split())
    
    buildings.append((i,start,height,0))#빌딩의 시작점을 저장
    buildings.append((i,end,height,1))#빌딩의 끝점을 저장
    
    end_points.append((end)) #빌딩이 끝나는 지점 저장

#x,start,hight높은 순으로 정렬
buildings.sort(key=lambda x:(x[1],x[3],-x[2]))

current_height = 0 #지금 높이
end_list = set()
result = []
not_ended_building = [] # 아직 안 끝난 빌딩

for building in buildings:
    building_idx,x,height,is_end = building #빌딩을 변수들로 나눠준다
    
    #시작점인 경우
    if not is_end:
        if height > current_height:
            current_height = height
            result.append((x,current_height))
        #진행중인 빌딩 최대힙에 높이랑 끝나는 x좌표 저장
        heapq.heappush(not_ended_building,(-height,end_points[building_idx]))
        continue

    end_list.add(x)

    while not_ended_building and not_ended_building[0][1]in end_list:
        heapq.heappop(not_ended_building)
    #진행중인 빌딩이 있으면 이거로 높이 변경  
    if not_ended_building:
        if current_height != -not_ended_building[0][0]:
            current_height = -not_ended_building[0][0]
            result.append((x,current_height))
    #진행중인 빌딩이 없으면
    else:
        if current_height != 0:
            current_height = 0
            result.append((x,current_height))
for r in result:
    print(' '.join([str(r[0]),str(r[1])]),end=' ')