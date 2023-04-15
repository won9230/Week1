import sys
n = int(sys.stdin.readline())
m = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]
white = 0
blue = 0


def Color(_x,_y,_n):
    global blue,white
    p = m[_x][_y]
    
    for i in range(_x,_x+_n):
        for j in range(_y,_y+_n):
            if p != m[i][j]:
                Color(_x,_y,_n//2)
                Color(_x,_y+_n//2,_n//2)
                Color(_x+_n//2,_y,_n//2)
                Color(_x+_n//2,_y+_n//2,_n//2)
                return
    if p == 1:
        blue += 1
    else:
        white += 1
        
Color(0,0,n)
print(white)
print(blue)