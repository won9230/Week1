import sys
n = int(sys.stdin.readline())
m = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]
white = 0
blue = 0

def Color(_n,_x,_y):
    global white,blue
    color = m[_x][_y]
    
    for i in range(_x,_x + _n):
        for j in range(_y,_y+_n):
            if m[i][j] != color:
                Color(_n//2,_x,_y)
                Color(_n//2,_x+_n//2,_y)
                Color(_n//2,_x,_y+_n//2)
                Color(_n//2,_x+_n//2,_y+_n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
        
Color(n,0,0)
print(white)
print(blue)