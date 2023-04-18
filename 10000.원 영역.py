import sys

n= int(sys.stdin.readline())

circles = []

for i in range(n):
    x,r = map(int,sys.stdin.readline().split()) #원 하고 반지름 저장
    circles.append((x-r,'(')) #원의 왼쪽 끝점을 ( 로 저장
    circles.append((x+r,')')) #원의 오른쪽 끝점을 ) 로 저장
    
circles = sorted(circles,key= lambda x : ( x[0], -ord(x[1]))) #원의 왼쪽 끝점을 중심으로 오름차순 정렬 수가 같으면 ) 가 먼저 정렬

stack = []

answer = 1
for i in range(n*2):
    position,bracket = circles[i] #circles을 둘로 나눈다
    if len(stack) == 0: #길이가 0이면
        stack.append({'pos':position,'bracket':bracket,'status':0})#위치와 괄호를 저장
        continue
    
    if bracket == ')': #괄호가 ) 면
        if stack[-1]['status'] == 0: 
            answer += 1
        elif stack[-1]['status'] == 1:
            answer += 2
            
        stack.pop()
        if i != n*2-1:
            if circles[i+1][0] != position:
                stack[-1]['status'] = 0
    else:
        if stack[-1]['pos'] == position: # 스택에 있는 pos가 position이랑 같으면(원끼리 겹치면)
            stack[-1]['status'] = 1 #마지막 스택에 있는 status = 1
            stack.append({'pos':position,'bracket':bracket,'status':0})
        else:
            stack.append({'pos':position,'bracket':bracket,'status':0})
print(answer)   
    
    
    