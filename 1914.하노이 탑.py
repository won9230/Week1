n = int(input())

def move(n,x,y):
    if n > 1:
        move(n-1,x,6-x-y)
    
    print(str(x) + " " + str(y))
    if n > 1:
        move(n-1,6-x-y,y)

if 20 >= n:
    print((2 ** n) - 1)
    move(n,1,3)
else:
    print((2 ** n)-1)