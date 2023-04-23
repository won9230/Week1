import sys

n= int(sys.stdin.readline())

circles = []

for _ in range(n):
    x,r = map(int,sys.stdin.readline().split())
    #'왼쪽 점인지 오른쪽 점인지 여부'와 점의 위치를 저장한다.
    circles.append(('L',x-r)) #왼쪽 점 = 중심 - 반지름
    circles.append(('R',x+r)) #오른쪽 점 = 중심 + 반지름


# 오른쪽 점 R이 왼쪽 점 L보다 앞으로 오도록 정렬(왼쪽 점과 오른쪽 점이 만나는 경우, 닫히는 점인 오른쪽이 먼저 있어야 힘)
circles.sort(key = lambda x:(x[0]),reverse=True)
circles.sort(key=lambda x : x[1])#왼쪽 점부터 오름차순 정렬

stack = [] # 왼쪽 점과 완선된 원의 정보를 담을 스택
count = 1 # 영역 개수

for circle in circles:
    if circle[0] == 'L': # 현재 점이 왼쪽 점인 경우들만, stack에 담아둔다.
        stack.append(circle)
        continue
    
    #현재 열린 원 안에 원이 들어있는 경우
    total_width = 0
    while stack:
        prev = stack.pop()
        #L을 꺼낸 경우 == 스택에서 꺼낸 게 왼쪽 점인 경우 -> 원이 만들어짐
        if prev[0] == 'L':
            width = circle[1] - prev[1]

            if total_width == width: #현재 만들어진 원의 지름이 이전의 원들 지름의 합과 같을 경우
                count += 2
            else:
                count += 1
            #원이 만들어졌으므로 stack에 원을 의미하는 C와 너비 추가
            stack.append(('C',width))
            break
        #C를 꺼낸 경우 == 스택에서 꺼낸게 원인 경우 -> 현재 원 안에 존재하는 원을 의미
        elif prev[0] == 'C':
            total_width += prev[1]
            
print(count)