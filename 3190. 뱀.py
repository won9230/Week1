import sys
from collections import deque
n = int(sys.stdin.readline()) #보드 길이

borad = [[0 for _ in range(n)]for _ in range(n)]#보드 생성
nk = int(sys.stdin.readline())

for i in range(nk):
    k = list(map(int,sys.stdin.readline().split()))#사과 생성
    borad[k[0]-1][k[1]-1] = 2 #사과 보드 위에 두기
    
nx = int(sys.stdin.readline())
x1 = deque()
for i in range(nx):
    x1.append(sys.stdin.readline().split()) #뱀이 어디로 언제 움직이는 지 확인
for i in range(len(x1)):
    if x1[i][1] == 'D':
        x1[i][1] = 1
    if x1[i][1] == 'L':
        x1[i][1] = -1
x1.append([sys.maxsize,0])
x = [0,1,0,-1] #1은 오른쪽 -1은 왼쪽
y = [-1,0,1,0] #-1은 위쪽 1은 아래쪽
sX = 0 #지금 뱀의 X변수
sY = 0 #지금 뱀의 Y변수
snackDir = 1 #뱀의 길이
dir = 1
lastTrun = True
_x1 = x1.popleft()
trunCount = int(_x1[0]) #몇번쨰 돌지 세주는 카운트
direction = _x1[1] #오른쪽 왼쪽 정해주는 수
snack = deque() #뱀
borad[sX][sY] = 1 #시작 뱀은 1
snack.append([sY,sX]) #뱀몸의 모든 X,Y변수
count = 0
while True:
    #뱀이 머리를 늘림 
    count += 1
    
    if sY + y[dir] >= n or sY + y[dir] < 0 or sX + x[dir] >= n or sX + x[dir] < 0: #밖으로 나가면 게임 끝
        print(count)
        break
    else:
        sY += y[dir]
        sX += x[dir]
        if borad[sY][sX] == 1:   #자기 자신을 만나면 게임 끝
            print(count)
            break
        elif borad[sY][sX] == 2: #뱀이 사과를 확인함
            borad[sY][sX] = 1    #사과가 있으면 사과를 없애고 꼬리를 늘림
            snack.append([sY,sX])
        else:                    #사과가 없으면 몸길이를 줄인다
            borad[sY][sX] = 1
            snack.append([sY,sX])
            _s = snack.popleft()
            borad[_s[0]][_s[1]] = 0

              
    if trunCount <= count and len(x1):    #뱀이 오른쪽으로 갈지 왼쪽으로 갈지 정함
        dir += direction
        if dir >= 4:
            dir = 0
        elif dir < 0:
            dir = 3
        _x1 = x1.popleft()
        trunCount = int(_x1[0]) #몇번쨰 돌지 세주는 카운트
        direction = _x1[1] #오른쪽 왼쪽 정해주는 수
