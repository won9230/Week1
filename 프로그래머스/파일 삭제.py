wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]

def solution(wallpaper):
    #제일 작은 #과 제일 큰 #를 구한다
    a = 51
    b = 0
    c = 51
    d = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == "#" and a > j):
                a = j
            if(wallpaper[i][j] == "#" and b < j):
                b = j
            if(wallpaper[i][j] == "#" and c > i):
                c = i
            if(wallpaper[i][j] == "#" and d < i):
                d = i

    answer = [c,a,d+1,b+1]
    return answer

print(solution(wallpaper))