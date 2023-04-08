x,y,w,h = input().split()


if int(x) >= int(w)/2:
    a = int(w)-int(x)
else:
    a = int(x)

if int(y) >= int(h)/2:
    b = int(h)-int(y)
else:
    b = int(y)
    
if a >= b:
    print(b)
else :
    print(a)   