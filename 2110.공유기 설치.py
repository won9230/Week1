import sys
n , c = map(int,sys.stdin.readline().split()) #집 개수 , 공유기 설치 개수
x = []
for i in range(n):# 집 좌표
    x.append(int(sys.stdin.readline()))
x.sort()
result = 0
def BShrech(start,end):
    global result

    if start > end:
        result = end
        return 
    #처음집 - 마지막집 // 2 로 중간값 구하기
    h = (start + end) // 2
    count = 1
    cur = x[0]
    #중간 값으로 설치할수 있는 공유기 개수 구하기
    for i in range(1,n):
        if x[i] - cur >= h:
            count += 1
            cur = x[i]
    #설치한 공유기가 공유기 설치 개수랑 같으면 리턴 다르면 재귀
    if count == c:
        result = max(result,h)
    if count >= c:
        BShrech(h + 1 , end)
    else:
        BShrech(start,h - 1)
        
BShrech(1,x[len(x)-1]-x[0])
 
print(result)
